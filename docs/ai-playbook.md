# My Personal AI Playbook

## When I Reach for AI First
- Generating boilerplate code like Dockerfile, CI workflows, and config files
- Writing documentation and README sections
- Suggesting test cases I might have missed
- Explaining error messages and stack traces
- Reviewing code for security issues I might overlook
- Generating repetitive code like CRUD endpoints

## When I Do Not Reach for AI First
- Understanding the core architecture and design decisions
- Debugging complex issues where I need to understand the root cause myself
- Making decisions about project scope and requirements
- Writing code I cannot explain or verify myself
- Any task involving real credentials, secrets, or personal data

## My Non-Negotiables
- Never paste credentials, tokens, .env values, or personal data into AI tools
- Never accept AI output without running and testing it first
- Never submit code I cannot explain line by line
- Always keep .env in .gitignore and .dockerignore
- Always verify AI-generated commands before running them

## My Review Rules
- Read the full AI response before accepting any part of it
- Run the app and tests after every AI-suggested change
- Grade every AI comment as Useful, Noise, or Wrong with a reason
- Reject suggestions that are out of scope even if they seem good
- Check AI-generated documentation against the actual running app

## What I Am Still Figuring Out
- How to use AI effectively for complex debugging without losing ownership
- When to ask AI for a second opinion versus trusting my own judgment
- How teams should document AI contributions in a shared codebase
- The right balance between AI speed and deep personal understanding

## Decision Card
- New feature: Plan it myself first, then use AI to implement small steps
- Code review: Use AI to find issues, then verify each finding manually
- Debugging: Try to understand the error myself first, then ask AI for help
- Infrastructure: Use AI to generate config files, always verify before running
- Never paste: credentials, secrets, personal data, or production logs
- One rule: If I cannot explain it, I do not submit it
