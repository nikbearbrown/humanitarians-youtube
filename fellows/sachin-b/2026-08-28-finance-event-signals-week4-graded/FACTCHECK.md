# FACTCHECK — "Claude, Graded." (Week 4)

| Claim (beat) | Verdict | Source |
|---|---|---|
| Grading rule (`holding_days=1`, `move_threshold=0.5%`) written before the grader was built (B01) | ✓ | `PRE_REGISTRATION.md` Week 4 section, committed before `outcome-grader` existed |
| Every failure path in `grader.py` returns a note, never a guess (B03) | ✓ | `services/outcome-grader/grader.py` lines 75-76, 85-86, 117 (verbatim) |
| 19 actionable signals, 3 graded, 3/3 correct, 16 pending (B04) | ✓ | `RUN_LOG.md` "outcome-grader built and run" section |
| Exotic tickers (BBCQU, LTRYW) return a `grading_note`, never a crash or guessed price (B06/B07) | ✓ | `grader.py` lines 82-83 (verbatim); `RUN_LOG.md` "Predicted vs. actual" table |
| Author's own BCAB prediction was mis-dated by one day, caught by pre-registration (B08) | ✓ | `RUN_LOG.md` "Predicted vs. actual" table, row 1 — disclosed, not corrected |
| Recipe promoted to `RUNNABLE-LIVE`, `todos_open: 0` (B09) | ✓ | Current `recipes/finance-event-signals.md` frontmatter |

## Corrections applied

None needed — the BCAB error is itself the disclosed correction; nothing
here required a second pass.

## Numbers on screen

None invented — all counts are direct quotes from RUN_LOG.md.
