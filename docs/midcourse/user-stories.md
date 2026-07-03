# User Stories

## Feature 1: Due Dates + Overdue Filter

### Story 1
As a solo developer,
I want to add a due date to a task,
So that I can track when each task needs to be completed.

Acceptance Criteria:
- I can create a task with an optional due_date field
- The due date must be in YYYY-MM-DD format
- If no due date is provided the task is still created successfully

### Story 2
As a solo developer,
I want to see which tasks are overdue,
So that I can prioritize my work and not miss deadlines.

Acceptance Criteria:
- I can filter tasks using GET /tasks/?overdue=true
- Only tasks with due_date in the past and status not done are returned
- Tasks without a due date are not included in overdue results

### Story 3
As a solo developer,
I want to update the due date of an existing task,
So that I can adjust deadlines when my schedule changes.

Acceptance Criteria:
- I can update due_date using PATCH /tasks/{id}
- The updated due date is saved and returned correctly
- I can remove a due date by setting it to null

### Story 4
As a solo developer,
I want to see an overdue warning on tasks in the frontend,
So that I can quickly identify urgent tasks without checking dates manually.

Acceptance Criteria:
- Tasks past their due date show an overdue badge in the UI
- Overdue tasks are highlighted in red in the frontend
- Done tasks are never shown as overdue even if past due date

### Story 5
As a solo developer,
I want to create a task with both a due date and priority level,
So that I can track my most urgent and important deadlines together.

Acceptance Criteria:
- I can set both due_date and priority when creating a task
- Both fields are saved and returned correctly
- The task appears in overdue filter if past due date

AI Assumption Corrected for Feature 1:
- AI initially suggested computing overdue status in the frontend only. I corrected this to also support backend filtering via query parameter so the API is more useful and testable.

---

## Feature 2: Search + Combined Filters

### Story 1
As a solo developer,
I want to search tasks by keyword,
So that I can quickly find a specific task without scrolling through all tasks.

Acceptance Criteria:
- I can search using GET /tasks/?search=keyword
- Search checks both title and description fields
- Search is case insensitive
- Returns empty list if no match found

### Story 2
As a solo developer,
I want to filter tasks by status,
So that I can focus on only todo or in progress tasks.

Acceptance Criteria:
- I can filter using GET /tasks/?status=todo
- Only tasks matching the status are returned
- Invalid status value returns 422 error

### Story 3
As a solo developer,
I want to filter tasks by priority,
So that I can focus on high priority tasks first.

Acceptance Criteria:
- I can filter using GET /tasks/?priority=high
- Only tasks matching the priority are returned
- Works with low, medium, and high values

### Story 4
As a solo developer,
I want to combine search and filters together,
So that I can find very specific tasks quickly and efficiently.

Acceptance Criteria:
- I can combine filters like GET /tasks/?status=todo&priority=high&search=meeting
- All filters are applied together
- Returns empty list if no tasks match all filters

### Story 5
As a solo developer,
I want to use search and filters directly in the frontend,
So that I can manage my tasks without using the API directly.

Acceptance Criteria:
- The frontend has a search box and filter dropdowns
- Results update when I type or change filters
- Empty state message shown when no tasks match

AI Assumption Corrected for Feature 2:
- AI initially suggested adding a separate search endpoint GET /search. I corrected this to add search as a query parameter to the existing GET /tasks/ endpoint to keep the API simple and RESTful.
