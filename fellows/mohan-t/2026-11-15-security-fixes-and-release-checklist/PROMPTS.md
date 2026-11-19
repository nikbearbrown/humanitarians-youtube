# PROMPTS.md — Timesheet Redesign – Week 3: Security Fixes and the Release Checklist

All beats render from props in beat_sheet.json. No generated images, no paid API, no open slots.

## BHTF — Your Turn prompt

```
Here is my app's admin account code: [paste it]. Try to change your own account, or take over someone else's, as an admin. Show me each path you find and the line that blocks it.
```

Rubric:

- Did it try different spellings of the same ID?
- Did it try an email change, then a reset?
- Does it point to the exact blocking line?
