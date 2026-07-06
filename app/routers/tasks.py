# Defines all task-related API endpoints

import uuid
from typing import List, Optional
from datetime import date
from fastapi import APIRouter, HTTPException, Query
from app.models import Task, TaskCreate, TaskUpdate, TaskStatus, TaskPriority
from app.storage import read_tasks, write_tasks, get_task_by_id

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", response_model=List[Task])
def get_tasks(
    overdue: Optional[bool] = Query(None),
    search: Optional[str] = Query(None),
    status: Optional[TaskStatus] = Query(None),
    priority: Optional[TaskPriority] = Query(None),
):
    """Return all tasks with optional filters."""
    tasks = read_tasks()

    # Filter by overdue
    if overdue is True:
        today = date.today()
        tasks = [
            t for t in tasks
            if t.due_date is not None
            and t.due_date < today
            and t.status != "done"
        ]

    # Filter by status
    if status is not None:
        tasks = [t for t in tasks if t.status == status]

    # Filter by priority
    if priority is not None:
        tasks = [t for t in tasks if t.priority == priority]

    # Search by title or description
    if search is not None:
        search_lower = search.lower()
        tasks = [
            t for t in tasks
            if search_lower in t.title.lower()
            or (t.description and search_lower in t.description.lower())
        ]

    return tasks


@router.post("/", response_model=Task, status_code=201)
def create_task(task_in: TaskCreate):
    """Create a new task."""
    tasks = read_tasks()
    new_task = Task(
        id=str(uuid.uuid4()),
        **task_in.model_dump()
    )
    tasks.append(new_task)
    write_tasks(tasks)
    return new_task


@router.get("/{task_id}", response_model=Task)
def get_task(task_id: str):
    """Return a single task by ID."""
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.patch("/{task_id}", response_model=Task)
def update_task(task_id: str, task_in: TaskUpdate):
    """Update an existing task."""
    tasks = read_tasks()
    for i, task in enumerate(tasks):
        if task.id == task_id:
            updated = task.model_dump()
            updates = task_in.model_dump()
            for k, v in updates.items():
                if v is not None:
                    updated[k] = v
            tasks[i] = Task(**updated)
            write_tasks(tasks)
            return tasks[i]
    raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: str):
    """Delete a task by ID."""
    tasks = read_tasks()
    new_tasks = [t for t in tasks if t.id != task_id]
    if len(new_tasks) == len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    write_tasks(new_tasks)