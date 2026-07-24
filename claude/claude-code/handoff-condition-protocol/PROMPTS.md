# PROMPTS — handoff-condition-protocol

## B02 — ASK (NikBearBrownTerminalAsk)

```
claude "Write handoff_validator.py:
  read Boondoggle Score JSON
  run each handoff condition as shell command
  require exit code 0 for PASS
  stop on first FAIL, name the blocking step"
```

## B05 — CHANGE (NikBearBrownTerminalAsk)

```
claude "Fix step 2 condition to match actual test count.
Re-run handoff_validator.py with all 3 conditions passing.
Show the clean success report."
```
