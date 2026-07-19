# PROMPTS — fluency-correctness-gap

## B02 — ASK (NikBearBrownTerminalAsk)

```
claude "Write top_three_by_gpa with tie-breaking.
Generate 5 test cases.
Run all tests.
Report: which pass, which fail, and the pass rate."
```

## B05 — CHANGE (NikBearBrownTerminalAsk)

```
claude "Add a semantic correctness check to gpa_test.py.
Not just compilation — audit tie-breaking correctness.
Does top_three_by_gpa handle equal GPAs correctly?"
```
