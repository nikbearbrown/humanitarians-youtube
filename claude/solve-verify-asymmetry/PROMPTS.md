# PROMPTS — solve-verify-asymmetry

## B02 — ASK (NikBearBrownTerminalAsk)

```
claude "Write top_three_by_gpa(students) -> list:
  sort by GPA descending
  tie-breaking: alphabetical by last_name ascending
  return top 3 students"
```

## B05 — CHANGE (NikBearBrownTerminalAsk)

```
claude "Audit top_three_by_gpa for tie-breaking correctness.
Does it correctly break ties alphabetically by last_name ascending?"
```
