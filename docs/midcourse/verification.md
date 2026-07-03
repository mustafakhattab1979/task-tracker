# Verification

## Baseline Check
Before adding features, I ran the app and confirmed the health endpoint returned 200 OK.
curl http://localhost:8000/health returned {status: ok, timestamp: ...}

## Backend Test Results
I ran pytest tests/ -v and all 10 tests passed:
- test_health_endpoint PASSED
- test_create_task PASSED
- test_create_task_with_due_date PASSED
- test_create_task_invalid_due_date PASSED
- test_overdue_filter PASSED
- test_search_filter PASSED
- test_status_filter PASSED
- test_search_no_results PASSED
- test_delete_task PASSED
- test_get_task_not_found PASSED

## Manual Browser Checks

Feature 1: Due Dates + Overdue Filter
- I created a task with due_date 2026-06-01 using POST /tasks/ in the docs UI.
- I confirmed the task was saved correctly in data/tasks.json.
- I called GET /tasks/?overdue=true and confirmed only the overdue task was returned.
- I confirmed tasks with no due_date do not appear in overdue results.

Feature 2: Search + Combined Filters
- I created two tasks: Fix login bug and Write documentation.
- I called GET /tasks/?search=login and confirmed only Fix login bug was returned.
- I called GET /tasks/?status=done and confirmed only done tasks were returned.
- I called GET /tasks/?search=nonexistent and confirmed empty list was returned with 200.

## Behavior Contract

Before refactor:
- POST /tasks/ accepts due_date and returns it in response.
- GET /tasks/?overdue=true returns only past due tasks with status not done.
- GET /tasks/?search=x returns tasks matching x in title or description.

After refactor:
- All behavior above is unchanged and all 10 tests still pass.

## Break Test Evidence

Break Test 1: Invalid due date format
- I sent due_date: not-a-date to POST /tasks/.
- Expected: 422 Validation Error.
- Result: 422 returned correctly. Test passed.

Break Test 2: Search with no matching results
- I searched for a term that does not exist in any task.
- Expected: 200 with empty list [].
- Result: 200 with [] returned correctly. Test passed.
