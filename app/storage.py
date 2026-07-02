# Handles reading and writing tasks to the JSON file

import json
import os
from typing import List, Optional
from app.models import Task

DATA_FILE = "data/tasks.json"


def read_tasks() -> List[Task]:
    """Read all tasks from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        content = f.read().strip()
        if not content:
            return []
        data = json.loads(content)
        return [Task(**task) for task in data]


def write_tasks(tasks: List[Task]) -> None:
    """Write all tasks to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(
            [json.loads(task.model_dump_json()) for task in tasks],
            f,
            indent=2
        )


def get_task_by_id(task_id: str) -> Optional[Task]:
    """Find a single task by its ID."""
    tasks = read_tasks()
    for task in tasks:
        if task.id == task_id:
            return task
    return None