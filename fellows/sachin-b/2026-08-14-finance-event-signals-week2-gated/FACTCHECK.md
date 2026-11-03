# FACTCHECK — "Claude, Gated." (Week 2)

| Claim (beat) | Verdict | Source |
|---|---|---|
| Four real reject paths, each with a specific reason (B03) | ✓ | `services/validation-svc/main.go` lines 155, 179, 185, 192 (verbatim) |
| Four malformed test events, four dead-lettered with the right reason, full envelope preserved (B04) | ✓ | `RUN_LOG.md` Week 2 PRE_REGISTRATION verification table, GIGO row — PASS |
| LangGraph 0.2.45 rejects a node returning `{}` (B05/B06) | ✓ | `services/enrichment-svc/graph.py` lines 86-90, verbatim, including the real inline comment documenting the bug |
| 97 events → 97 signals, 12 pending_review, 85 withheld, 0 agent errors (B07) | ✓ | `RUN_LOG.md` "Fresh clean run" section |
| ~88% withhold rate, breakdown by event type (B08) | ✓ | `RUN_LOG.md` "Finding — deterministic LLM withhold rate is ~88%" |
| Recipe `todos_open` 6→3, still `DRAFT` (B09) | ✓ | `git show 341b78d:recipes/finance-event-signals.md` frontmatter |
| 400/200/409 sequence for the ClearGate invariant (B10) | ✓ | `RUN_LOG.md` Human-clear-gate verification row |

## Corrections applied

None needed.

## Numbers on screen

None invented — all counts above are direct quotes from RUN_LOG.md or the
real source files.
