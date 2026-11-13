# SOURCES — The Keyword That Cried Wolf

Primary source for every measured claim in this beat sheet:

- `/Users/pranavijs/mycroft/scripts/regulatory-intel/C2-VERIFICATION.md` (dated 2026-09-29) — the
  design, the live verification table, the fail-open test, and the honest limitations.
- `/Users/pranavijs/mycroft/scripts/regulatory-intel/FINDINGS.md` (dated 2026-07-24) — the two
  originally-named C1 misfire patterns and their original scores.
- `/Users/pranavijs/mycroft/logs/RUN_LOG.md` — the matching 2026-09-29 C2 entry.
- `/Users/pranavijs/mycroft/scripts/regulatory-intel/workflow.dev.json` — the hardened n8n
  workflow copy containing the new `Layer 2 - LLM Re-Score` node; commit `3e32894` on
  `feature/regulatory-intelligence-hardening` (fork `SaiPranaviJ/mycroft`).

## Claim → source mapping

| Beat | Claim | Source | Notes |
|---|---|---|---|
| B02/B04 | Medicare rule 10/Critical; Nasdaq cluster 9/Critical | `FINDINGS.md` "C1"; re-confirmed live against DB rows id 4, 966/967 in `C2-VERIFICATION.md` | Real titles/scores, not constructed examples |
| B03 | The `+3` scoring rule for "immediate"/"emergency" | `C2-VERIFICATION.md` "The problem", quoting `calculateBasicUrgency()` | Verbatim from `Keyword Analysis & Urgency Scoring` node |
| B05 | The Layer 2 design (never overwrites, fail-open, threshold-gated) | `C2-VERIFICATION.md` "The design" | — |
| B06 | Live verdicts for all 3 test cases | `C2-VERIFICATION.md` "Live verification" table | Real node code executed via a `$input.all()` harness, not a hypothetical |
| B07 | The 3 named limitations | `C2-VERIFICATION.md` "What's honest and NOT overclaimed here" | — |

## Citation status (open)

- No claim in this beat sheet is sourced from anything outside the files above — there is no
  external web citation to verify.
- The local-Ollama setup (`llama3.2:3b`) matches an existing internal convention already used by
  `Regulatory_QA` (`backend/app/config.py`), not a new external dependency introduced here.
