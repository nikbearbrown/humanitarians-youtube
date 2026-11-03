# SOURCES — The Check That Never Once Fired

Primary source for every measured claim in this beat sheet:

- `/Users/pranavijs/mycroft/scripts/regulatory-intel/B2-VERIFICATION.md` (dated 2026-08-30) — the
  bug, the live 5-feed test methodology, and the full results table.
- `/Users/pranavijs/mycroft/logs/RUN_LOG.md` — the 2026-08-30 B2 entry.
- `/Users/pranavijs/mycroft/scripts/regulatory-intel/workflow.dev.json` — the hardened n8n
  workflow copy; commit `d59fbd5` in `mycroft` (`feature/regulatory-intelligence-hardening`)
  contains the fix.

## Claim → source mapping

| Beat | Claim (as spoken/shown) | Source | Notes |
|---|---|---|---|
| B03 | The CFTC-detection condition as quoted (`link.includes('commodity-futures')` or `title.includes('cftc')`) | `B2-VERIFICATION.md` "The bug" | Verbatim from `workflow.dev.json` prior to commit `d59fbd5` |
| B04 | Example title "Swap Execution Facility Order Book Requirement for Permitted Transactions" has no "CFTC" in title or agency slug in link | `B2-VERIFICATION.md` "The bug", item 1 | Pulled live from the real CFTC Regulations RSS feed 2026-08-30 |
| B05 | CFTC feed: 12/12 items reclassified | `B2-VERIFICATION.md` "Live verification (2026-08-30)" table | Live test run today against the real feed, not a simulation |
| B05 | Securities-term-search feed: 83/146 items reclassified (real agencies: FCC, EEOC, DOT-Maritime) | Same table | Same live test |
| B05 | SEC / FINRA / Investment Advisor feeds: 0 changed | Same table | Confirms no regression on already-working classifications |
| B06 | Fix reads `dc:creator`; before/after `identifySource()` code | `B2-VERIFICATION.md` "The fix"; `workflow.dev.json` post-fix | — |

## Citation status (open)

- No claim in this beat sheet is sourced from anything outside the two files above and the
  workflow JSON — there is no external web citation to verify.
- The test results (12/146/25/100/100 items) are a snapshot from live RSS feeds as they existed on
  2026-08-30. Feed content changes daily; if this reel is rebuilt or re-narrated later, re-run the
  test described in `B2-VERIFICATION.md` before reusing the exact counts on screen.
- Explicitly **not claimed**: that this misclassification affected any specific email alert or
  report the fellow's live (hand-built) n8n workflow actually sent — the live test measures
  classification behavior, not the history of what already happened in production. See
  `FACTCHECK.md`.
