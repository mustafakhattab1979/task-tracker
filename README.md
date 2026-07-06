# Task Tracker

A learning-focused task tracking web application built with Python and FastAPI, using JSON file storage for simplicity. This project demonstrates core REST API and backend engineering concepts including CRUD operations, data validation with Pydantic, overdue task filtering, as well as due dates task filtering plus the combined search filters including status,priority, assignee and feature development using an AI-assisted workflow.

## Tech Stack

- **Python 3.12** - Programming language
- **FastAPI** - Modern web framework for building APIs
- **Uvicorn** - ASGI server to run the application
- **Pydantic** - Data validation and settings management
- **python-dotenv** - Load environment variables from .env file
- **JSON file storage** - Simple file-based data persistence
- **pytest** - Testing framework

## Project Structure

task-tracker

   app/

      __init__.py     # Marks app as a Python package

         main.py      # FastAPI app instance and health endpoint
         
         models.py     # Pydantic data models
         
         storage.py    # JSON file read/write operations
         
 routers/
 
         __init__.py       # Marks routers as a Python package
         
         
           tasks.py        # All task-related API endpoints
           
    data/
    
        tasks.json          # JSON file where tasks are stored
        
 docs/
 
    midcourse/
 
          user-stories.md
       
          mini-adr.md
       
          prompt-log.md
         
          verification.md
         
          reflection.md
          
          requirements.txt         # Project dependencies

          .env.example             # Example environment variables

          .gitignore               # Files to ignore in Git
 
           README.md               # Project documentation

## Features

### Core Features
- Create tasks with title, description, status, and priority
- Read all tasks or a single task by ID
- Update any task field
- Delete tasks by ID
- Auto-generated interactive API documentation

### Mid Course Project Features
- **Due Dates** - Add optional due date to any task
- **Overdue Filter** - Filter tasks that are past their due date
- **Search** - Search tasks by title or description
- **Combined Filters** - Filter by status, priority, and overdue together

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check with timestamp |
| GET | /tasks/ | Get all tasks |
| GET | /tasks/?overdue=true | Get only overdue tasks |
| GET | /tasks/?search=keyword | Search tasks by keyword |
| POST | /tasks/ | Create a new task |
| GET | /tasks/{id} | Get a single task by ID |
| PATCH | /tasks/{id} | Update an existing task |
| DELETE | /tasks/{id} | Delete a task |

## Task Model

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | auto | Unique identifier |
| title | string | yes | Task title |
| description | string | no | Task description |
| status | enum | no | todo, in_progress, done |
| priority | enum | no | low, medium, high |
| due_date | date | no | Due date in YYYY-MM-DD format |

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/mustafakhattab1979/task-tracker.git
cd task-tracker

### 2. Create and activate virtual environment

Windows PowerShell:
python -m venv venv
venv\Scripts\Activate.ps1

### 3. Install dependencies
pip install -r requirements.txt

### 4. Configure environment variables
Copy-Item .env.example .env

## Running the Server

uvicorn app.main:app --reload --port 8000

The API will be available at http://localhost:8000

## Testing the Health Endpoint

curl http://localhost:8000/health

Expected response:
{"status": "ok", "timestamp": "2026-07-02T12:00:00.000000+00:00"}

## Interactive API Documentation

FastAPI generates automatic interactive documentation.
Open your browser and go to:
http://127.0.0.1:8000/docs

You can test all endpoints directly from the browser without any extra tools.

## Running the Frontend

The frontend is a single static file (no build step, no separate server required).

1. Make sure the backend is already running (see "Running the Server" above) at `http://127.0.0.1:8000`.
2. Open `frontend/index.html` directly in your browser:
   - **Windows**: double-click the file, or run `start frontend\index.html`
   - **macOS**: `open frontend/index.html`
   - **Linux**: `xdg-open frontend/index.html`
3. The page will load tasks from the running backend automatically. You can:
   - Add a task using the "Add New Task" form
   - Filter/search using the controls at the top
   - Mark a task done or delete it

**How to confirm the frontend is actually connected to the backend:**
- If it's connected, you'll see either your existing tasks in the grid, or "No tasks found." — and adding a task via the form will make it appear immediately without reloading the page.
- If it's *not* connected, you'll see the message "Could not connect to server. Make sure the backend is running." This can happen if the backend isn't running, is on a different port than 8000, or if the browser blocks the request as cross-origin (CORS) — the backend in this project is configured with CORS enabled specifically so this works when the frontend is opened as a local file.

The backend must stay running in its own terminal window while the frontend page is open — closing the terminal (or stopping uvicorn) will make the frontend show the "could not connect" message again.

## Running Tests

pytest

To run with details:
pytest -v

The test suite (`tests/test_tasks.py`) contains 10 tests:

1. `test_health_endpoint` - health check returns 200 and status "ok"
2. `test_create_task` - creating a task returns 201
3. `test_create_task_with_due_date` - creating a task with a due date
4. `test_create_task_invalid_due_date` - malformed due date returns 422
5. `test_overdue_filter` - overdue=true returns only past-due, not-done tasks
6. `test_search_filter` - search matches title/description
7. `test_status_filter` - filtering tasks by status
8. `test_search_no_results` - search with no matches returns 200 and []
9. `test_delete_task` - deleting a task returns 204
10. `test_get_task_not_found` - getting a non-existent task returns 404

All 10 pass in a clean environment (`10 passed`).

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| PORT | 8000 | Port to run the server on |
| APP_ENV | development | Application environment |

## Architecture Decision

This project uses JSON file storage instead of a database because:
- Lower learning curve for beginners
- No database setup required
- Easy to inspect and modify stored data manually
- Fewer moving parts and dependencies

For production use, migrating to SQLite or PostgreSQL would be recommended.

## Author

Mustafa Khattab
GitHub: https://github.com/mustafakhattab1979
