# FACTCHECK — The Pipeline That Was Lying to Me

Status: **All rows checked against `/Users/pranavijs/mycroft/scripts/regulatory-intel/FINDINGS.md` (2026-07-26). See `SOURCES.md` for full derivation.**

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B00 | Pipeline "quietly dropping real SEC filings for months — and nobody knew, because it never threw an error" | QUALIFY | FINDINGS.md confirms the silent-drop mechanism (B1 row) and that dropped items were real filings; the toolkit has no evidence for the specific duration "for months" — that is dramatization, not a measured fact | Narration should read as illustrative framing, not a measured claim. Consider softening to "quietly dropping real SEC filings — and nobody knew" if strict literalism is required for this audience |
| 2 | B01 | Five feeds (SEC, FINRA, CFTC, Federal Register) → normalize → score → Postgres → email alert | PASS | Matches the pipeline description in the project brief and `workflow.dev.json` structure | — |
| 3 | B02 | A filter silently rejected any item with an empty description; no log, no error | PASS | Matches "B1 recover empty-content" fix description (the removed `content isNotEmpty` filter node) | — |
| 4 | B03 | Recovered items: Cboe Clear U.S., MEMX LLC, Nasdaq GEMX SRO notices, US v. Edwards LifeSciences (DOJ antitrust) | PASS (names) / OPEN (citations) | FINDINGS.md line 24 names exactly these four | Exact filing URLs not yet pulled from `regulatory_feeds` — see `SOURCES.md` "Citation status." Not a blocker since this toolkit never publishes |
| 5 | B04 | "Seventy-three additional real items recovered — per run"; on-screen 297 → 370 | PASS | FINDINGS.md line 19: "OLD 297 → NEW 370 pass = +73 recovered" | — |
| 6 | B04 (narration) | "verified the output against the production database" | QUALIFY | FINDINGS.md specifies the verification was a **rolled-back test transaction against a local DB** (`mycroft_intelligence` @ localhost:5431), cross-checked against real n8n-produced rows — not literally "the production database" | Correct narration to "verified against real production data in a rolled-back test run" to avoid overstating where the check ran |
| 7 | B05 | "Silent filters don't fail loudly. They fail invisibly." | PASS | Editorial takeaway, consistent with the B1 finding; not a factual claim requiring a source | — |
| 8 | B06 | "Fixed with Claude Code, verified against live data before it ever touched production" | PASS | Consistent with FINDINGS.md methodology (live RSS feeds + rolled-back local DB transaction, not simulated data) | — |

## Corrections — resolved 2026-07-26

1. **B00 narration** — "for months" removed (dramatized, not measured). **Applied.**
2. **B04 narration** — "verified the output against the production database" flagged as an overstatement (actual method: rolled-back test transaction against a local DB, cross-checked against real production rows). **Fellow reviewed and elected to keep the line as-is.**

Gate P (narration) can proceed with the above resolution.
