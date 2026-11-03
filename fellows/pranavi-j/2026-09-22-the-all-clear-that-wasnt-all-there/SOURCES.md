# SOURCES — The All-Clear That Wasn't All There

Primary source for every measured claim in this beat sheet:

- `/Users/pranavijs/mycroft/scripts/regulatory-intel/B5-VERIFICATION.md` (dated 2026-09-29) — the
  bug, the fix, and the verification.
- `/Users/pranavijs/mycroft/logs/RUN_LOG.md` — the matching 2026-09-29 B5 entry.
- `/Users/pranavijs/mycroft/scripts/regulatory-intel/workflow.dev.json` — the hardened n8n
  workflow copy containing the fix (`Send email` node); commit `3e32894` on
  `feature/regulatory-intelligence-hardening` (fork `SaiPranaviJ/mycroft`).

## Claim → source mapping

| Beat | Claim | Source | Notes |
|---|---|---|---|
| B03 | The shipped "Monitored Sources" grid listed 4 cards | `B5-VERIFICATION.md` "The bug" | Verbatim card labels |
| B04 | The workflow's 5 real `rssFeedRead` source nodes | `B5-VERIFICATION.md` "The bug" | Extracted directly from `workflow.dev.json` |
| B05 | The fix and its verification (5/5 label match, conformance check) | `B5-VERIFICATION.md` "The fix" and "Verification" | — |
| B06 | The stale `FINDINGS.md` note, confirmed already-fixed via git history | `B5-VERIFICATION.md` "What's NOT touched" | Commit `fa88e05` predates `FINDINGS.md` |

## Citation status (open)

- No claim in this beat sheet is sourced from anything outside the files above — there is no
  external web citation to verify.
