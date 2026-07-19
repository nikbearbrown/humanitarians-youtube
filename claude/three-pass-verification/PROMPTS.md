# PROMPTS — three-pass-verification

## B02 — ASK (NikBearBrownTerminalAsk)

```
claude "Run three-pass verification on app tracker:
  Pass 1: happy path — does it run?
  Pass 2: edge cases — empty state, zero apps
  Pass 3: read SDD user needs aloud against running build
  Report: PASS/FAIL per pass with evidence"
```

## B05 — CHANGE (NikBearBrownTerminalAsk)

```
claude "Amend SDD: remove 'at a glance' user need.
Re-run Pass 3 against amended SDD.
Does Pass 3 now pass? Show which needs remain."
```
