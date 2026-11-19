# PROMPTS.md — Project Ledger – Week 6: Testing and the Timesheet Redesign

All beats render from props in beat_sheet.json. No generated images, no paid API, no open slots.

## BHTF — Your Turn prompt

```
Here is a timesheet design: [paste it]. Write the test plan before rollout: a staging database, many users at once, an access review, and unit tests. For each, say what would count as a pass.
```

Rubric:

- Does every test have a pass condition?
- Does it test who can approve hours?
- Does it include many users at once?
