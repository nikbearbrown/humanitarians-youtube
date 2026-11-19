# PROMPTS.md — Timesheet Redesign – Week 2: My Hours, the Daily Limit and PR #16

All beats render from props in beat_sheet.json. No generated images, no paid API, no open slots.

## BHTF — Your Turn prompt

```
Here is my database schema for time entries: [paste it]. Write a rule in the database itself that refuses any day over 24 hours across all projects, and give me tests that prove it.
```

Rubric:

- Is the rule in the database, not just the app?
- Does it count all projects together?
- Do the tests include a day of exactly 24 hours?
