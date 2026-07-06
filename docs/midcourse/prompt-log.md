# Prompt Log

## Feature 1: Due Dates + Overdue Filter

### Prompt 1 (Weak prompt - before rewrite)
Prompt: 'Add due dates to tasks'
What AI returned: AI added a datetime field with timezone support and a separate endpoint for overdue tasks.
What I did: I rejected the datetime type and separate endpoint as too complex.

### Prompt 1 (Strong prompt - rewrite)
Prompt: 'Add an optional due_date field using Python date type to the Task, TaskCreate and TaskUpdate Pydantic models in app/models.py. Do not use datetime or timezone. Keep it simple.'
What AI returned: AI added due_date as Optional[date] = None to all three models correctly.
What I accepted: I accepted the change as it matched the requirement exactly.

### Prompt 2
Prompt: 'Add an overdue query parameter to GET /tasks/ in app/routers/tasks.py. If overdue=true, return only tasks where due_date is in the past and status is not done. Use date.today() for comparison.'
What AI returned: AI added the overdue filter correctly using date.today() comparison.
What I accepted: I accepted the full implementation with no changes.

### Prompt 3
Prompt: 'Update app/storage.py to use model_dump_json() instead of model_dump() so that date fields are serialized correctly to JSON string format.'
What AI returned: AI updated write_tasks to use json.loads(task.model_dump_json()) correctly.
What I accepted: I accepted the fix as it solved the date serialization bug.

## Feature 2: Search + Combined Filters

### Prompt 4 (Weak prompt - before rewrite)
Prompt: 'Add search to tasks'
What AI returned: AI suggested adding a full text search library called whoosh with an index file.
What I did: I rejected this as too complex for a learning project.

### Prompt 4 (Strong prompt - rewrite)
Prompt: 'Add an optional search query parameter to GET /tasks/ in app/routers/tasks.py. Search should filter tasks where the search string appears in title or description using Python string matching. Make it case insensitive.'
What AI returned: AI added the search filter using lower() string comparison correctly.
What I accepted: I accepted the full implementation.

### Prompt 5
Prompt: 'Add optional status and priority query parameters to GET /tasks/ so that filters can be combined with search and overdue.'
What AI returned: AI added status and priority as Optional query parameters with correct type hints.
What I accepted: I accepted the implementation and tested it in the browser.

### Prompt 6
Prompt: 'Write pytest tests for due date creation, invalid due date format, overdue filter, search filter, status filter, empty search results, delete task, and task not found. Use setup_function to clear tasks before each test.'
What AI returned: AI wrote 10 tests covering all required cases.
What I accepted: I accepted all tests after running them and confirming they all passed.
