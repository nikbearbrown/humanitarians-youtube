# PROMPTS — boondoggle-score

## B02 — ASK (NikBearBrownTerminalAsk)

```
claude "Generate Boondoggle Score table for app tracker Phase 1:
  columns: step#, phase, labor, supervisory capacity, handoff condition
  flag: critical path and highest-risk handoff
  rule: every handoff condition must be machine-checkable"
```

## B05 — CHANGE (NikBearBrownTerminalAsk)

```
claude "Set row 1 handoff condition to: 'Claude completes the data model'.
Re-run scorer. Does it flag this condition as invalid?
Explain why it fails the machine-checkable rule."
```
