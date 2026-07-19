# FACTCHECK — vox-vigilance-decay

Source: `computational-skepticism-for-ai/chapters/09-delegation-trust-and-the-supervisory-role.md`

## Terms table

| Term | Definition used in video | Chapter reference |
|---|---|---|
| Overtrust | Supervisor accepts AI output when they should not; verification silently skipped | Line 222 |
| Automation complacency | Degraded monitoring under low signal rates; the mechanism behind overtrust | Line 224 |
| Low signal rate | Condition where the AI rarely fails, leading reviewers to check less frequently | Line 224 |
| Calibrated trust | Supervisor reliance that matches actual AI reliability; requires monitoring infrastructure and consistent discipline | Line 226 |
| Verification cost | Whether a human can check AI output cheaply; high cost pushes toward accepting output | Line 100 |

## Claim-by-claim check

| Beat | Claim | Chapter support | Status |
|---|---|---|---|
| B02 | Reviewer stamps outputs, vigilance drains, error arrives undetected | Lines 222, 224 (automation complacency, degraded monitoring) | PASS |
| B04 | Overtrust = supervisor accepts output, verification silently skipped; least visible because no immediate flags | Line 222: exact | PASS |
| B05 | Verification cost mechanism — cost structure pushes toward accepting outputs; not a character flaw | Line 100: "cost structure itself quietly pushes the supervisor toward accepting the output rather than checking it. That is not a character flaw; it is economics acting on attention." | PASS |
| B07 | Rarely-failing systems produce low signal rates; low signal rates degrade monitoring | Line 224: "complacency, degraded monitoring under low signal rates" | PASS |
| B08 | Quote verbatim (condensed) | Line 222: "It produces uncaught errors that are discovered later, often by the affected user." | PASS |
| B09 | Fix: calibrated trust, systematic verification regardless of recent performance | Line 226 | PASS |
| B10 | Quote verbatim (condensed) | Line 226: "knowing the AI's actual reliability for this kind of case...and acting on that knowledge consistently" | PASS |
| B11 | Workflow that supports discipline rather than fighting it | Line 226 | PASS |

## B12 — EXAMPLE beat (illustrative)

All numbers in B12 are invented for illustration and are not derived from any cited source:
- Month 1 review time: 25 sec/board — illustrative
- Month 5 review time: 3 sec/board — illustrative
- "Batch 17" — illustrative
- 340 defective units shipped — illustrative
- Four months / 99.1 percent accuracy — illustrative
- "Week seventeen" — illustrative

The underlying mechanism (degraded monitoring over a streak, error arriving when checking has eroded) is sourced to lines 222–224.

## VERDICT: PASS
