# FACTCHECK — The Keyword That Cried Wolf

Status: **RESOLVED — fellow reviewed 2026-09-29. Cleared for Gate P (narration lock).**

| # | Beat | Claim (as spoken/shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02/B04 | Medicare rule scored 10/Critical; Nasdaq cluster scored 9/Critical | PASS | `FINDINGS.md` "C1 — keyword scorer misfires"; re-confirmed live 2026-09-29 against real DB rows (ids 4, 966/967) in `C2-VERIFICATION.md` | — |
| 2 | B03 | The `+= 3` scoring rule for "immediate"/"emergency", quoted verbatim | PASS | `C2-VERIFICATION.md` "The problem", quoting `calculateBasicUrgency()` directly | — |
| 3 | B04 | Both titles' real context ("Emergency Medical Treatment and Labor Act", "Notice of Filing and Immediate Effectiveness") | PASS | Real titles pulled live from `regulatory_feeds`, quoted verbatim | — |
| 4 | B05 | The fix design: never overwrites original score, fail-open on error, only reviews items above the alert threshold | PASS | `C2-VERIFICATION.md` "The design" | — |
| 5 | B06 | Live verdicts: both false positives downgraded, SEC case confirmed/untouched | PASS | `C2-VERIFICATION.md` "Live verification" table — real test run, not a hypothetical | — |
| 6 | B06 (implicit) | The SEC case was "left alone" | PASS, **framing must be precise** | The SEC case (id 153) wasn't reviewed by the LLM at all — its `urgency_score` (5) never crosses the alert threshold, so it was correctly skipped, not "reviewed and confirmed" | Narration must not imply the LLM actively reviewed and approved this case — it was correctly excluded from review entirely, same as it would have been with no Layer 2 step at all. Current draft's "left alone, exactly as it should be" is accurate; avoid language like "the AI checked it and approved it" |
| 7 | B07 | The 3 named limitations (conservative correction, small sample, added latency) | PASS | `C2-VERIFICATION.md` "What's honest and NOT overclaimed here" | — |

## Dramatization check

No beat claims this is a comprehensive fix for all scorer noise, or that the correction is more
precise than it measured. The fail-open safety path is shown explicitly rather than only
presenting the happy path — matches this fellow's established honesty pattern for AI-assisted
fixes (e.g. B3's identical "never breaks the run" framing).

## Resolved 2026-09-29

1. **B06 framing distinction** kept as drafted ("left alone, exactly as it should be") — will add a
   small on-screen label "not reviewed — below alert threshold" next to that row for extra clarity
   since the point (never sent to the model, not reviewed-and-approved) is easy to misread at a
   glance.
2. **B07's honest-limits beat kept at full weight** — no softening.

Gate P (narration review) can proceed.
