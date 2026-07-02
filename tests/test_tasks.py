# Pytest tests for the Task Tracker API

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
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


def test_get_tasks():
    """Test getting all tasks returns 200."""
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


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


def test_search_tasks():
    """Test searching tasks by keyword."""
    response = client.get("/tasks/?search=Test")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


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


def test_task_not_found():
    """Test getting a non-existent task returns 404."""
    response = client.get("/tasks/nonexistent-id")
    assert response.status_code == 404