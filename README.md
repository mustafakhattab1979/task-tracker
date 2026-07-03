# Task Tracker

A learning-focused task tracking web application built with Python and FastAPI, using JSON file storage for simplicity. This project demonstrates core REST API and backend engineering concepts including CRUD operations, data validation with Pydantic, overdue task filtering, as well as due dates task filtering plus the combined search filters including status, priority, assignee and feature development using an AI-assisted workflow.

## Tech Stack

- **Python 3.12** - Programming language
- **FastAPI** - Modern web framework for building APIs
- **Uvicorn** - ASGI server to run the application
- **Pydantic** - Data validation and settings management
- **python-dotenv** - Load environment variables from .env file
- **JSON file storage** - Simple file-based data persistence
- **pytest** - Testing framework

## Project Structure

task-tracker/

app/

 __init__.py    # Marks app as a Python package
 
  main.py   # FastAPI app instance and health endpoint
    
 models.py    # Pydantic data models
 
 storage.py   # JSON file read/write operations
 
 routers/
 
 __init__.py  # Marks routers as a Python package
 
 tasks.py  # All task-related API endpoints
 
data/
   tasks.json   # JSON file where tasks are stored

 docs/
     midcourse/
     
           user-stories.md
           
           mini-adr.md
           
           prompt-log.md
           
           verification.md
           
           reflection.md 
           
requirements.txt  # Project dependencies 

.env.example   # Example environment  variables

.gitignore    # Files to ignore in Git
  
 README.md    # Project documentation

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

## Running Tests

pytest

To run with details:
pytest -v

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
