# Release Evidence

## Baseline
- Branch: final-project
- Date: 2026-07-05
- Local app run command: uvicorn app.main:app --reload --port 8000
- /health result: {"status": "ok", "timestamp": "2026-07-05T..."}
- Frontend check: Opened frontend/index.html in browser. Kanban board and create/edit task flow are visible and working.
- Test command: pytest tests/ -v
- Test result: 10 passed in 1.03s

## CI Evidence
- Workflow file: .github/workflows/ci.yml
- Latest run link: https://github.com/mustafakhattab1979/task-tracker/actions
- Test command used by CI: pytest tests/ -v
- Shortcut check: no continue-on-error / no || true / pytest is not skipped

## Docker Evidence
- Build command: docker build -t task-tracker .
- Run command: docker run -p 8000:8000 task-tracker
- /health check: curl http://localhost:8000/health returns 200 ok
- Non-root check: useradd appuser implemented in Dockerfile
- No-baked-secrets check: .dockerignore excludes .env and venv/

## Documentation Claim-vs-Reality Log
| Claim checked | Evidence used | Result | Change made, if any |
|---|---|---|---|
| uvicorn starts the API on port 8000 | Ran uvicorn app.main:app --reload --port 8000 | Confirmed working | None |
| pytest runs 10 tests and all pass | Ran pytest tests/ -v | 10 passed in 1.03s | None |
| /health returns status ok | curl http://localhost:8000/health | Returns 200 with ok status | None |
