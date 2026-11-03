# FACTCHECK — The Update That Almost Lied About What It Sent

Status: **RESOLVED — fellow reviewed 2026-08-30. Both open items (B05 framing, B05 "12" count)
approved below. Cleared for Gate P (narration lock).**

| # | Beat | Claim (as spoken/shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02 | "It was using its own copy of the rule for what counts as high-priority" | PASS | `A7-VERIFICATION.md` "The bug" — the old query's `WHERE` clause is a literal second copy of a threshold/impact condition, independent of `High Priority Filter` | — |
| 2 | B03 | The two conditions as quoted (`> 6` vs. `> 7 OR impact_level IN (...)`) | PASS | Verbatim from `workflow.dev.json` prior to commit `03ad1e0` | — |
| 3 | B04 | `determineImpactLevel()` bypasses the score on enforcement/fraud keyword hits | PASS | Verbatim function body, `A7-VERIFICATION.md` "Why the two rules disagree" | — |
| 4 | B05 | "Twelve real rows, right now" | **PASS — re-verified** | Live query re-run 2026-08-30 21:04 (build day, not just `A7-VERIFICATION.md`'s original 2026-08-30 pass) — same 12 ids (112, 115, 153, 322, 326, 338, 347, 356, 364, 483, 555, 1008), count unchanged | Narration keeps "as of this week" framing regardless — this is a live, growing table, not a fixed constant. Do not present "12" as a permanent number even though it happened to match. |
| 5 | B05 | "The old query would have silently marked [these] sent the next time it ran" | **PASS — approved as written** | This is a *forward-looking, conditional* claim derived from reading the code, not an observed incident. `A7-VERIFICATION.md` explicitly notes it does **not** prove these 12 rows were ever actually mis-marked in the fellow's live hand-built n8n workflow (that workflow's run history vs. `workflow.dev.json` is not tracked). Fellow approved this framing 2026-08-30 — no rewording needed. | Narration keeps the conditional framing ("would have," "next time it ran") — never assert this already happened. |
| 6 | B05 | Example: "SEC Charges 21 Individuals With Alleged Wide-Reaching Insider Trading Scheme" | PASS | Row id 153 in the live table, title copied verbatim | — |
| 7 | B05 (implicit) | All 12 rows are meaningful signal | **NOT CLAIMED — do not add** | `A7-VERIFICATION.md` notes several of the 12 (Sunshine Act Meetings, two procedural CFTC/SEC exemptive-relief orders) are known C1-class noise, consistent with last week's findings | Beat sheet already avoids this by naming only one specific, unambiguous example (row 153) rather than implying all 12 are equally significant. Keep it that way — do not narrate "12 missed enforcement actions." |
| 8 | B06 | Fix description and `id = ANY($1::int[])` query | PASS | `A7-VERIFICATION.md` "Fix"; `workflow.dev.json` post-fix, commit `03ad1e0` | — |
| 9 | B06 | Verification method (rolled-back transaction) | PASS | `A7-VERIFICATION.md` "Verification method" | — |
| 10 | B07 | "A step that copies someone else's rule... is wrong the day the two drift apart" | PASS | Editorial takeaway, consistent with the demonstrated mechanism; not a factual claim requiring a source | — |

## Dramatization check

No beat invents a crash, an outage, or an incident that didn't happen. The one place this reel
could slide into overclaiming is B05 (#5 above) — narrating "these were marked sent" instead of
"these would be marked sent." The beat sheet draft already uses conditional language throughout;
this file exists to make that a deliberate, reviewed choice rather than an accident.

## Resolved 2026-08-30

1. **B05 forward-looking framing** (row #5): approved as written — no edit.
2. **"12" count** (row #4): fellow chose to re-run the query at build time rather than ship the
   original `A7-VERIFICATION.md` snapshot as-is. Re-run 2026-08-30 21:04 against the live
   `regulatory_feeds` table returned the identical 12 ids — see `SOURCES.md` for the updated
   citation.

Both open items are closed. Gate P (narration review) can proceed.
