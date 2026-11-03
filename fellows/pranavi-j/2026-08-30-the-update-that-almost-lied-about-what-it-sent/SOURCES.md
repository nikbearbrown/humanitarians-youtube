# SOURCES — The Update That Almost Lied About What It Sent

Primary source for every measured claim in this beat sheet:

- `/Users/pranavijs/mycroft/scripts/regulatory-intel/A7-VERIFICATION.md` (dated 2026-08-30)
  — the bug, the code mechanism (`determineImpactLevel()`'s keyword bypass), the live query,
  and the full 12-row result.
- `/Users/pranavijs/mycroft/logs/RUN_LOG.md` — two 2026-08-30 entries: the A7 fix itself, and
  the addendum documenting the live 12-row measurement.
- `/Users/pranavijs/mycroft/scripts/regulatory-intel/workflow.dev.json` — the hardened n8n
  workflow copy; commit `03ad1e0` in `mycroft` (`feature/regulatory-intelligence-hardening`)
  contains the fix.

## Claim → source mapping

| Beat | Claim (as spoken/shown) | Source | Notes |
|---|---|---|---|
| B03 | High Priority Filter uses `urgency_score > 6`; old Mark-email-sent used `urgency_score > 7 OR impact_level IN ('Critical','High')` | `A7-VERIFICATION.md` "The bug" | Both queries quoted verbatim from `workflow.dev.json` prior to the fix |
| B04 | `determineImpactLevel()` sets High/Critical from an enforcement/fraud keyword hit regardless of score | `A7-VERIFICATION.md` "Why the two rules disagree" | Function quoted verbatim from the `Keyword Analysis & Urgency Scoring` node |
| B05 | 12 real rows, as of 2026-08-30, match `impact_level IN ('Critical','High') AND urgency_score <= 6 AND email_sent = FALSE` | `A7-VERIFICATION.md` "Live measurement (2026-08-30)"; **re-verified 2026-08-30 21:04 direct against live DB at build time** — identical 12 ids (112, 115, 153, 322, 326, 338, 347, 356, 364, 483, 555, 1008) | Live query against `regulatory_feeds`, not a simulation. Count will drift as the table grows — accurate as of build time only |
| B05 | Example row: "SEC Charges 21 Individuals With Alleged Wide-Reaching Insider Trading Scheme" (id 153, urgency_score 5, impact_level Critical) | Same table, row `id=153` | Chosen because it is unambiguously a real enforcement action, not one of the known procedural/noise rows in the same result set |
| B06 | Fix: `WHERE id = ANY($1::int[])` sourced from `High Priority Filter`'s output | `A7-VERIFICATION.md` "Fix"; `workflow.dev.json` post-fix | Verified via rolled-back transaction, described in `A7-VERIFICATION.md` "Verification method" |

## Citation status (open)

- No claim in this beat sheet is sourced from anything outside the two files above and the
  workflow JSON — there is no external web citation to verify.
- The "12" count is a live-table snapshot. If this reel is rebuilt or re-narrated after
  2026-08-30, re-run the query in `A7-VERIFICATION.md` before reusing the number on screen.