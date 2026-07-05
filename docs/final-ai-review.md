# Final AI Review and Ownership Evidence

## AGENTS.md Guardrails
- Repo-specific stack and commands included: yes
- Docs-first/read-first guardrail included: yes
- Unexpected app/frontend edits rule included: yes

## AI Code Review Mini-Log
| AI comment | Grade: Useful / Noise / Wrong | Reason | Verification or decision |
|---|---|---|---|
| Add non-root user in Dockerfile for security | Useful | Reduces security risk in container | Implemented useradd appuser in Dockerfile |
| Use --no-cache-dir in pip install | Useful | Reduces Docker image size | Implemented in Dockerfile |
| Add .env to .dockerignore | Useful | Prevents secrets from being copied into image | Implemented in .dockerignore |

## AI Security Mini-Review
| Finding | File evidence | Grade: Valid / False Positive / Noise | Reason | Next action |
|---|---|---|---|---|
| .env file could be accidentally copied into Docker image | .dockerignore | Valid | Secrets should never be in Docker image | Added .env to .dockerignore |
| JSON file storage has no access control | app/storage.py | Noise | This is a learning project not production | Accepted as out of scope |
| No input length validation on task title | app/models.py | Valid | Could cause issues with very long titles | Accepted as known limitation |

## Manual Security Check
I manually checked that the .env file is listed in .gitignore and .dockerignore so it will never be pushed to GitHub or copied into the Docker image. I also verified that no credentials or tokens appear anywhere in the codebase by searching for common patterns like password, secret, and token.

## One AI Output I Rejected or Corrected
AI suggested adding PostgreSQL database support to replace JSON file storage. I rejected this because the project ADR explicitly states JSON file storage is the chosen architecture for learning purposes. Adding a database would be a new product feature which is out of scope for the final project.

## Three AI Usage Rules
1. Never paste: credentials, .env values, tokens, or personal data into AI tools
2. Always verify: run the app and tests after every AI-suggested change before accepting it
3. Record AI contributions by: noting what AI suggested, what I accepted, what I rejected, and why

## Ownership Statement
I built this Task Tracker application across the course modules with AI assistance for code generation and review. I reviewed every AI suggestion before accepting it, ran all tests to verify correctness, and rejected suggestions that were out of scope such as database migration and authentication. I can explain every file and every line of code in this repository. The architecture decisions are documented in the ADR and I understand the tradeoffs involved. I am comfortable submitting this repository as my own work because I made every significant decision myself and used AI as a tool rather than a replacement for my own judgment.
