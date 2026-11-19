# PROMPTS.md — Project Ledger – Week 3: Extending the Database

All beats render from props in beat_sheet.json. No generated images, no paid API, no open slots.

## BHTF — Your Turn prompt

```
Here is my database schema: [paste it]. I need to add [feature]. Write the change using only additions, nothing altered or dropped, and give me a test I can run in a separate schema first.
```

Rubric:

- Does it only add columns and tables?
- Does every new column have a safe default?
- Can you run the test schema step as written?
