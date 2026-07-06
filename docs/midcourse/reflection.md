# Reflection

## AI Tools Used
I used two AI tools throughout this project: Claude AI and GitHub Copilot.
I used Claude in the browser chat interface on claude.ai to plan, implement, test, and debug the two features.
I used GitHub Copilot inside Cursor code editor to get inline code suggestions while typing.

## How I Used AI
I used Claude to generate the initial code for the models, storage, and router files.
I used Claude to write the pytest tests after describing what each test should check.
I used Claude to debug errors when they appeared in the terminal.
I used Claude to write the documentation files in the docs/midcourse folder.
I used Copilot inside Cursor to get quick inline suggestions while editing code files.

## One Moment AI Helped
Claude helped me quickly identify the date serialization bug in storage.py.
When the overdue filter was returning empty results, I checked the JSON file and saw the date was not stored correctly.
Claude suggested using model_dump_json() instead of model_dump() which fixed the bug immediately.
This saved me a lot of time that I would have spent searching for the problem myself.

## One Moment AI Slowed Me Down
When I asked Claude to add search to tasks with a weak prompt, it suggested using a full text search library called whoosh.
This was too complex for a learning project and not aligned with the JSON file storage architecture.
I had to reject the suggestion and rewrite a stronger prompt that specified Python string matching instead.
This taught me that weak prompts produce answers that are technically correct but not suitable for the project constraints.

## One Place Where My Review Changed the Result
Claude initially suggested using datetime with timezone support for the due_date field.
I reviewed the requirement and decided that a simple date type was sufficient.
I corrected the prompt and asked Claude to use Optional[date] instead.
This kept the implementation simple and aligned with the ADR decision to avoid unnecessary complexity.

## What I Learned
I learned that AI tools like Claude and Copilot are powerful but require clear and specific prompts to get useful results.
I learned that reviewing AI output critically is more important than accepting it blindly.
I learned that testing each layer of the application before moving to the next prevents difficult bugs later.
I learned that Python 3.12 with FastAPI and JSON file storage is a simple and effective stack for learning backend development.
