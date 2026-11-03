# SOURCES — The Synonyms the Classifier Never Learned

Primary source for every measured claim in this beat sheet:

- `/Users/pranavijs/mycroft/scripts/regulatory-intel/UNKNOWN-SOURCE-INVESTIGATION.md`
  (dated 2026-08-30) — the starting count, the title-by-title breakdown, the fix, and the full
  5-feed before/after table.
- `/Users/pranavijs/mycroft/scripts/regulatory-intel/FINDINGS.md` — referenced by the investigation
  doc for the earlier 2026-07-24 count (21, vs. 18 measured live 2026-08-30 — explicitly noted as
  expected day-to-day feed drift, not a discrepancy to resolve).
- `/Users/pranavijs/mycroft/scripts/regulatory-intel/workflow.dev.json` — the hardened n8n
  workflow copy containing the `identifySource()` fix.

## Claim → source mapping

| Beat | Claim (as spoken/shown) | Source | Notes |
|---|---|---|---|
| B02/B03 | 18 items across 2 Google News feeds fell to 'Unknown Source'; Google News lacks `dc:creator` | `UNKNOWN-SOURCE-INVESTIGATION.md` "Starting point" | Live count 2026-08-30; doc notes 2026-07-24's `FINDINGS.md` recorded 21 — feed content changes daily |
| B04 | The two example titles (recoverable "Exempt Reporting Advisers" one; not-recoverable "FCA Decision Notice" one) | `UNKNOWN-SOURCE-INVESTIGATION.md` "What was actually failing" | Quoted verbatim |
| B05 | The 2 new synonym-check rules; the 5-feed before/after table (18→8 total) | `UNKNOWN-SOURCE-INVESTIGATION.md` "The fix" and "Live verification (2026-08-30)" | Full 5-row table in source doc |
| B06 | The remaining 8 items' 2 failure categories; framed as a deliberate tradeoff | `UNKNOWN-SOURCE-INVESTIGATION.md` "What's still open, and why this isn't a full close" | Source doc explicitly frames this as a considered stopping point, not an unresolved bug |

## Citation status (open)

- No claim in this beat sheet is sourced from anything outside the three files above — there is
  no external web citation to verify.
- The "18" and "8" counts are live-table snapshots as of 2026-08-30. If this reel is rebuilt or
  re-narrated later, re-run the classifier against the live feeds before reusing these numbers on
  screen.
