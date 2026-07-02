# User Stories

## Feature 1: Due Dates + Overdue Filter

US-1: As a user, I want to set a due date on a task so that I know when it must be completed.
Acceptance criteria: Task can be created with a due_date in YYYY-MM-DD format.
AI assumption corrected: AI suggested using datetime instead of date - changed to date only.

US-2: As a user, I want to see overdue tasks so that I can prioritize urgent work.
Acceptance criteria: GET /tasks/?overdue=true returns only tasks where due_date is in the past and status is not done.

US-3: As a user, I want to update a task due date so that I can reschedule work.
Acceptance criteria: PATCH /tasks/{id} accepts a new due_date and saves it correctly.

US-4: As a user, I want invalid due dates to be rejected so that data stays clean.
Acceptance criteria: Sending a non-date string returns HTTP 422.

US-5: As a user, I want tasks without a due date to be excluded from overdue results.
Acceptance criteria: Tasks with due_date=null never appear in overdue filter results.

## Feature 2: Search + Combined Filters

US-6: As a user, I want to search tasks by title or description so that I can find tasks quickly.
Acceptance criteria: GET /tasks/?search=login returns tasks containing login in title or description.
AI assumption corrected: AI suggested full-text search with a library - simplified to Python string matching.

US-7: As a user, I want to filter tasks by status so that I can see only active or completed tasks.
Acceptance criteria: GET /tasks/?status=done returns only done tasks.

US-8: As a user, I want to filter tasks by priority so that I can focus on high priority work.
Acceptance criteria: GET /tasks/?priority=high returns only high priority tasks.

US-9: As a user, I want to combine filters so that I can narrow down results precisely.
Acceptance criteria: GET /tasks/?status=todo&priority=high returns only todo tasks with high priority.

US-10: As a user, I want an empty list returned when no tasks match so that I know the search worked.
Acceptance criteria: GET /tasks/?search=nonexistent returns 200 with [].
