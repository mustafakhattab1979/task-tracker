# Pytest tests for the Task Tracker API

from datetime import date, timedelta

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    """Test the health endpoint returns 200 and ok status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_task():
    """Test creating a new task returns 201."""
    response = client.post("/tasks/", json={
        "title": "Test Task",
        "description": "A test task",
        "status": "todo",
        "priority": "medium"
    })
    assert response.status_code == 201
    assert response.json()["title"] == "Test Task"


def test_create_task_with_due_date():
    """Test creating a task with a due date."""
    response = client.post("/tasks/", json={
        "title": "Task with due date",
        "status": "todo",
        "priority": "high",
        "due_date": "2026-06-01"
    })
    assert response.status_code == 201
    assert response.json()["due_date"] == "2026-06-01"


def test_create_task_invalid_due_date():
    """Test creating a task with a malformed due date returns 422."""
    response = client.post("/tasks/", json={
        "title": "Bad due date task",
        "status": "todo",
        "priority": "medium",
        "due_date": "not-a-date"
    })
    assert response.status_code == 422


def test_overdue_filter():
    """Test that overdue=true returns only past-due, not-done tasks."""
    yesterday = (date.today() - timedelta(days=1)).isoformat()

    overdue = client.post("/tasks/", json={
        "title": "Overdue task",
        "status": "todo",
        "priority": "high",
        "due_date": yesterday
    })
    assert overdue.status_code == 201
    overdue_id = overdue.json()["id"]

    no_due_date = client.post("/tasks/", json={
        "title": "Task without a due date",
        "status": "todo",
        "priority": "low"
    })
    assert no_due_date.status_code == 201
    no_due_date_id = no_due_date.json()["id"]

    response = client.get("/tasks/?overdue=true")
    assert response.status_code == 200
    ids = [t["id"] for t in response.json()]
    assert overdue_id in ids
    assert no_due_date_id not in ids


def test_search_filter():
    """Test searching tasks by keyword matches title/description."""
    client.post("/tasks/", json={
        "title": "Fix login bug",
        "status": "todo",
        "priority": "high"
    })
    response = client.get("/tasks/?search=login")
    assert response.status_code == 200
    results = response.json()
    assert len(results) >= 1
    assert all("login" in t["title"].lower() for t in results)


def test_status_filter():
    """Test filtering tasks by status."""
    client.post("/tasks/", json={
        "title": "Done task for status filter",
        "status": "done",
        "priority": "low"
    })
    response = client.get("/tasks/?status=done")
    assert response.status_code == 200
    results = response.json()
    assert len(results) >= 1
    assert all(t["status"] == "done" for t in results)


def test_search_no_results():
    """Test searching for a term with no matches returns 200 and an empty list."""
    response = client.get("/tasks/?search=zzz_nonexistent_term_zzz")
    assert response.status_code == 200
    assert response.json() == []


def test_delete_task():
    """Test deleting a task returns 204."""
    create = client.post("/tasks/", json={
        "title": "Task to delete",
        "status": "todo",
        "priority": "low"
    })
    task_id = create.json()["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204


def test_get_task_not_found():
    """Test getting a non-existent task returns 404."""
    response = client.get("/tasks/nonexistent-id")
    assert response.status_code == 404
