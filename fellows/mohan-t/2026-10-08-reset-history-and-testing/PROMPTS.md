# PROMPTS.md — Project Ledger – Week 4: Sign-in, History and Testing

All beats render from props in beat_sheet.json. No generated images, no paid API, no open slots.

## BHTF — Your Turn prompt

```
Here is my app's password reset flow: [paste it]. Walk through it as an attacker. Can a link be reused, guessed, or used after it expires? Point to the exact lines.
```

Rubric:

- Does it check that a link works only once?
- Does it check the expiry in the query itself?
- Does it say how the token is stored?
