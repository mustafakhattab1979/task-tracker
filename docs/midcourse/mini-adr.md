# Mini ADR

## Stack Used
I used Python 3.12 with FastAPI and JSON file storage for this project.
I chose JSON file storage because it is simple, easy to inspect, and requires no database setup.

## Feature 1: Due Dates + Overdue Filter

Decision: I added an optional due_date field to the Task model using Python date type.
I computed overdue detection in the backend using date.today() comparison.
I stored tasks as JSON in data/tasks.json using Python 3.12 standard library.

Alternatives AI suggested:
- Use datetime instead of date - I rejected this, date is sufficient for due dates.
- Add a computed is_overdue field to the model - I rejected this, I kept logic in the filter only.
- Store overdue as a separate boolean field - I rejected this, computed on the fly is simpler.

What I rejected as too complex:
- Sending email notifications for overdue tasks - out of scope.
- Recurring due dates - out of scope for learning project.

## Feature 2: Search + Combined Filters

Decision: I extended GET /tasks/ with optional query parameters: search, status, priority, overdue.
I applied filters sequentially in Python 3.12 after reading from JSON file.

Alternatives AI suggested:
- Use a search library like whoosh or elasticsearch - I rejected this, too complex.
- Add a separate GET /tasks/search endpoint - I rejected this, combined filters in one endpoint is cleaner.
- Use SQL LIKE queries - I rejected this, I am using JSON file storage not a database.

What I rejected as too complex:
- Pagination - out of scope for current stage.
- Sorting by field - out of scope for current stage.
