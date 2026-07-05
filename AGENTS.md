# AGENTS.md - Task Tracker Repo Guardrails

## Stack
- Python 3.12
- FastAPI 0.115.0
- Uvicorn 0.30.6
- Pydantic 2.9.2
- python-dotenv 1.0.1
- JSON file storage
- Plain HTML/CSS/JS frontend

## Run Commands
- Start API: uvicorn app.main:app --reload --port 8000
- Run tests: pytest tests/ -v
- Run with Docker: docker build -t task-tracker . && docker run -p 8000:8000 task-tracker

## Project Rules
- No authentication, no database, no microservices
- No new product features in final project
- Only change app/ or frontend/ for bug fixes
- No secrets or credentials in the repo
- No .env files committed to GitHub

## Docs-First Guardrails
- Always read AGENTS.md before making changes
- Always read existing code before asking AI to rewrite it
- Always run tests before and after any change
- Always verify AI output before accepting it
- Never paste credentials or secrets into AI tools
