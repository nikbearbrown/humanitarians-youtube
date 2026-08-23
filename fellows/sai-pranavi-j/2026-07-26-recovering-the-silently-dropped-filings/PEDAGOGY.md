# PEDAGOGY — The Pipeline That Was Lying to Me

Single-insight `ai-explainer` reel for the Humanitarians AI Fellows weekly-report
series. Audience: engineers using Claude Code. Thesis: a pipeline can lose real
data without ever throwing an error — the scariest bugs run clean.

## Act structure
- B00 HOOK — states the thesis as a question the rest of the reel answers ✓
- B01 SETUP — the pipeline shape (5 feeds -> normalize -> score -> Postgres -> alert), enough to place the bug ✓
- B02 DISCOVERY — the actual mechanism (the empty-description filter), named precisely, no vague hand-waving ✓
- B03 PROOF — concrete recovered filings, not abstract "more data" ✓
- B04 FIX — the fix + the measured before/after number, the one hard receipt of the episode ✓
- B05 TAKEAWAY — one-sentence generalizable lesson, earns its place because B00-B04 demonstrated it rather than asserted it ✓
- B06 SIGN-OFF — channel/brand restate, Claude Code credit ✓

One insight, one proof, one takeaway — matches `ai-explainer`'s "tight reel" mandate (not a multi-act documentary).

## Evidence discipline (source: FACTCHECK.md, verified 2026-07-26 against `/Users/pranavijs/mycroft/scripts/regulatory-intel/FINDINGS.md`)
| Claim | Verdict |
|---|---|
| 297 -> 370 items, +73 recovered | PASS |
| Recovered filing names (Cboe Clear U.S., MEMX LLC, Nasdaq GEMX, US v. Edwards LifeSciences) | PASS (names); citations open, non-blocking since this toolkit never publishes |
| Parameterized-insert stress test (370 items, 0 errors) | PASS (background context, not on-screen in this cut) |
| B00 "for months" | REMOVED — dramatization, not measured |
| B04 "production database" phrasing | Flagged as loose; fellow elected to keep as-is |

## Friction protected
- Kept: the single empty-description-filter bug, because it has the cleanest before/after number of all the Layer-1 fixes.
- Deliberately excluded: parameterized-insert fix, feed-isolation fix, HTML escaping, source misclassification, Layer-2 LLM re-scoring — all candidates for future weekly reports, not this one (see `README.md`).

VERDICT: PASS
