# SOURCES.md — one-run-still-open (Mycroft 9)

**DOUBLE-CHECK LAW.** Every claim traces to `D:\Code\mycroft\verification-layer`, never to
`Desktop\mycroft\accountability_layer`.
- **Recomputed claims:** recomputed by `assets/evidence/m9_evidence.py`, which opens the database
  read-only and records no decision.
- **Captured claims:** screenshots of the local `/app`, taken with view controls only
  (`assets/evidence/capture_app.mjs`).

**Verification passes:**
- **2026-09-26:** evidence run and first captures.
- **2026-09-27:** re-check against RUN_LOG through B6/U9 (the last roadmap phase); new captures and
  export for B14–B16. The checkout's HEAD is still `c53746a`; all later work is uncommitted.

---

## Sources

| Ref | Source | Used for |
|---|---|---|
| S1 | `logs/RUN_LOG.md`: BG+U3, B2+B3, BP+U4 (2026-09-25); U5+U6, the correction, the verification, B4+U7, option 1 + B5 + U8 (2026-09-26); B6+U9 (2026-09-27) | Narrative and logged figures |
| S2 | `web/data/accountability.db` (read-only) | Run `ec1a3b44` and its decisions; GOOGL `e592660c`; MSFT `ec40e81b` |
| S3 | `validation/gate.py` (`validate_decision`, `gate_state`, `strip_search_content`, `MIN_RATIONALE`, `IDENTITY_NOTE`) | B02–B07, B15 |
| S4 | Fixtures `run_compare_gated_{auditor,investor}.json`, `run_compare_b3_aapl.json` | B02, B06, B11 |
| S5 | The live server, `GET /api/runs/ec1a3b44…` at investor scope (a read) | B06 |
| S6 | `datasources/filings.py` `find_in_document` on `tests/fixtures/aapl_10q_2026q3_trimmed.htm` | B12 |
| S7 | `stream_compare_aapl_2026-09-24.txt` (a real captured stream) | B13 |
| S8 | `web/self_report.py` `KNOWN_ISSUES` | B11, B18 |
| S9 | `core/assessment.py` (extraction, `ground_in`), `validation/divergence.py`, `validation/audit.py` | B14–B16 |
| S10 | `/app` captures: `assets/B03_*`, `B06_*`, `B07_*`, `B14_grades_1280.png`, `B15_grade_gate_1280.png`, `B16_review_top_1280.png` | B03–B07, B14–B16 |
| S11 | `GET /api/runs/8ecb0922…/export.md` at auditor scope → `assets/evidence/out/B16_export_8ecb0922_auditor.md` | B16 |

## Beat-by-beat claims

| Beat | Claim | Verified value | Source |
|---|---|---|---|
| B00, B07 | The Pokémon run is flagged and waiting for a person; nobody has decided | `ec1a3b44`: `release_year MISMATCH 1998 / 1996`, `AWAITING_DECISION`, **0 decisions** | S2 → `out/B00_B07_gated_run_now.json` |
| B02 | Only a two-sided disagreement gates; one-sided figures shown for review; pre-gate runs never gated | run `20c538e4` flagged but `NO_DECISION_NEEDED`; `gate_state({}, [])` → `NOT_GATED` | S3, S4 → `out/B02_trigger.json` |
| B03 | Five outcomes; a reason of at least 20 characters; a checkbox per disputed figure | `DECISIONS`; `MIN_RATIONALE = 20`; form capture | S3; `assets/B03_gate_open_1280.png` |
| B04 | "Recorded as entered; not verified"; refusals in words | `IDENTITY_NOTE`; the server's own refusal strings | S3 → `out/B03_B04_decision_rules.json` |
| B05 | Superseded, never edited; the database blocks edits and deletes | `gate_state` supersede logic; append-only triggers | S1, S3 |
| B06 | Values and answers withheld; a trace search result showed "1998" once | live and fixture investor reads: `1998: 1`, `1996: 0`, inside a press.nintendo.com result | S5, S4 → `out/B06_investor_view.json`; `assets/B06_investor_trace_leak_1280.png` |
| B06 | Fixed: the trace withholds search results while the gate is open; after the fix neither year appears | `strip_search_content()` applied by `redact_for_scope()`; verified on a restarted server: investor reads `1998: 0`, `1996: 0` across runs, sessions, decisions and snippets | S1 (2026-09-26 correction + verification), S3 |
| B06 | A token-less read is served at the stored level | RUN_LOG open issue (`audit-criticals`) | S1, S8 |
| B08 | Hard rules gate; the reviewer can confirm the error | `validation/constraints.py`; `confirmed_error` | S1 (B2+B3) |
| B09 | Microsoft: given $82.9B, wrote $828.9B; that attempt halted on format first | stored `ec40e81b`: "revenue was $828,860,000,000 USD" | S2 → `out/B08_B11_checks.json`, S1 |
| B10 | Google net income ~3× operating income, also in the filing; the soft rule doesn't gate | `e592660c`: `net_le_operating` fails for agent B **and** the filing ($112.2B vs $40.77B), `gates: false` | S2 → `out/B08_B11_checks.json` |
| B11 | Apple's balance sheet adds up; a 5-token request got no reply in 60 s; no timeout | `balance_sheet_filed` pass, $383.3B = $383.3B; ledger `ollama-hangs-under-compare` | S4, S8 |
| B12 | Figures located in the real filing; 24 of 24 found, all equal | "Total net sales" / "109,417" / $109.417B; RUN_LOG BP+U4 tally | S6 → `out/B12_filing_excerpt.json`, S1 |
| B12 | Every figure in the review has a Source button | `SourcePopover.tsx` (U6) | S1 (U5+U6) |
| B13 | One shared SEC fetch; lanes are real server events | 4 shared steps, one LLM step per agent | S7 → `out/B13_stream_events.json` |
| B14 | A second call to the same model extracts grade, direction, assumptions and key points from the finished answer; ungrounded quotes dropped; failure recorded, run continues; labelled model judgment | `core/assessment.py` extraction + `ground_in`, `extraction_failed`; capture of run `8ecb0922`: A AAA/buy, B A/buy | S9, S1 (option 1 + B5 + U8); `assets/B14_grades_1280.png` |
| B15 | Drivers data / assumption / weighting; consensus only when grade and direction agree with no hard failure; accept A, accept B, or set the grade; investors see no grade until one is recorded | `validation/divergence.py`; gate policy v3; `8ecb0922` driver "assumption" (stable vs expanding margins), gate open on "grade" | S9, S3; `assets/B15_grade_gate_1280.png`, `out/B16_export_8ecb0922_auditor.md` |
| B16 | The review reads answer first; every review exports as a plain document | U5 summary order; `GET /api/runs/{id}/export.md`, first lines shown as recorded output | S1 (U5, B6+U9), S11 |
| B17 | A mismatch, failed hard check or grade split stops the run; investors get no disputed value, answer or search result | gate policy v3; `redact_for_scope` + `strip_search_content` | S3, S1 |
| B18 | Name typed, never verified; anyone can mint a reviewer token; storage holds everything; the grade is the same model judging itself; no model-call timeout | `IDENTITY_NOTE`; `audit-criticals`; B5/U8 open issue; ledger | S3, S8, S1 |

## Corrections made by the verification passes

| Date | Where | Draft said | Evidence showed | Now |
|---|---|---|---|---|
| 09-26 | B06 | "Neither year appears anywhere" | "1998" once in a trace search result | narrated as a hole |
| 09-27 | B06 | a hole that is still open | fixed and verified on a restarted server | found, fixed, verified |
| 09-26 | B12 | "click it, the system opens the filing" | no UI existed | "not built yet" |
| 09-27 | B12 | not built | U6 Source button built | narrated as built |
| 09-27 | B14 | agents end with a structured assessment | in-directive assessment reverted (2 of 10 first attempts passed); a separate extraction call is the built design | describes the extraction |
| 09-27 | B15 | consensus when grades match | grade **and** direction must agree | corrected |
| 09-27 | B18, B19 | the trace leak and "no live gated check yet" listed as open | leak fixed; NVDA `9b1a9e0e` had a failed claim-vs-source check under the gate | removed; added "same model judging itself" |

**Findings for the verification layer, both since logged there.** The trace leak and the MSFT
"live" claim were corrected in RUN_LOG on 2026-09-26 ("Correction: two claims in earlier entries
were wrong"). The leak was then fixed and verified.

## Declared simplifications

- **"The login carries a permission level":** the JWT scope, simplified.
- **"A named person":** the name is self-declared, as the video says in B04 and B18.
- **"A second call reads the answer":** this is the extraction call in `core/assessment.py`, the
  same local model with no tools and no directive.

## Not verified here

- Real screen readers and touch devices for the gate form and the Source button.
- The v2 extraction prompt across a batch (RUN_LOG: one live run so far). The video doesn't claim
  its accuracy.
