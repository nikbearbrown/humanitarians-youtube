# PROMPTS — spec-prompt-audit

## B02 — ASK (NikBearBrownTerminalAsk)

```
claude "Write parse_grades(path) -> list[Grade]
  invariants: stdlib only, no pandas
  UTF-8 BOM tolerated
  empty cells -> None not ''
  run: python -m pytest tests/ -q
  do not modify models/grade.py"
```

**Contrast (weak prompt, not shown in terminal):**
```
claude "Write a function to parse a grades CSV file"
```

## B05 — CHANGE (NikBearBrownTerminalAsk)

```
claude "Run parse_grades prompt twice.
Are outputs functionally equivalent?
Compare: lib choices, empty-cell handling,
BOM handling across both runs."
```
