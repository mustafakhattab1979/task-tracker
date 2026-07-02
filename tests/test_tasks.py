# Tests for the Task Tracker API endpoints

import pytest
from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)

TEST_DATA_FILE = "data/tasks.json"


def setup_function():
    """Clear tasks before each test."""
    with open(TEST_DATA_FILE, "w") as f:
        json.dump([], f)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_task():
    response = client.post("/tasks/", json={
        "title": "Test Task",
        "priority": "high"
    })
    assert response.status_code == 201
    assert response.json()["title"] == "Test Task"


def test_create_task_with_due_date():
    response = client.post("/tasks/", json={
        "title": "Task with due date",
        "due_date": "2026-06-01"
    })
    assert response.status_code == 201
    assert response.json()["due_date"] == "2026-06-01"


def test_create_task_invalid_due_date():
    response = client.post("/tasks/", json={
        "title": "Bad date task",
        "due_date": "not-a-date"
    })
    assert response.status_code == 422


def test_overdue_filter():
    client.post("/tasks/", json={
        "title": "Overdue Task",
        "status": "todo",
        "due_date": "2026-06-01"
    })
    response = client.get("/tasks/?overdue=true")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Overdue Task"


def test_search_filter():
    client.post("/tasks/", json={"title": "Fix login bug"})
    client.post("/tasks/", json={"title": "Write documentation"})
    response = client.get("/tasks/?search=login")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Fix login bug"


def test_status_filter():
    client.post("/tasks/", json={"title": "Todo Task", "status": "todo"})
    client.post("/tasks/", json={"title": "Done Task", "status": "done"})
    response = client.get("/tasks/?status=done")
    assert response.status_code == 200
    data = response.json()
    assert all(t["status"] == "done" for t in data)


def test_search_no_results():
    response = client.get("/tasks/?search=nonexistent")
    assert response.status_code == 200
    assert response.json() == []


def test_delete_task():
    create = client.post("/tasks/", json={"title": "To delete"})
    task_id = create.json()["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204


def test_get_task_not_found():
    response = client.get("/tasks/nonexistent-id")
    assert response.status_code == 404