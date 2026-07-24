# PROMPTS — five-supervisory-capacities

## B02 — ASK (NikBearBrownTerminalAsk)

```
claude "[PF] Write top_three_by_gpa with tie-breaking by last_name.
  Test set MUST include: at least one tie case (same GPA).
[PA] After output: run tie-case probe immediately.
[TO] If probe fails: re-prompt with exact failure description.
[IJ] Interpret any accuracy threshold before accepting.
[EI] Final: confirm all user needs from SDD are met."
```

## B05 — CHANGE (NikBearBrownTerminalAsk)

```
claude "Run the same GPA sort build WITHOUT supervisory labels.
At which step would the tie-breaking bug have shipped?
Show the unlabeled decision point where the failure entered."
```
