# FACTCHECK.md — one-run-still-open (GATE F)

Claims as spoken or shown, each traced to the live checkout at `D:\Code\mycroft\verification-layer`
or to the reel's computed evidence in `assets/evidence/out/` (see `SOURCES.md` for the full pass).

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | Pokemon run: A 1998, B 1996, flagged, waiting for a person | PASS | assets/evidence/out/B00_B07_gated_run_now.json (ec1a3b44, AWAITING_DECISION, 0 decisions) | — |
| 2 | B02 | Only a two-sided mismatch gates; one-sided figures shown for review; pre-gate runs never gated | PASS | assets/evidence/out/B02_trigger.json; validation/gate.py GATING_STATUSES | — |
| 3 | B03 | Five outcomes; reason of at least 20 characters | PASS | validation/gate.py DECISIONS, MIN_RATIONALE=20; assets/B03_gate_open_1280.png | — |
| 4 | B04 | Name recorded as entered, not verified; refusals in words | PASS | assets/evidence/out/B03_B04_decision_rules.json (validate_decision output, nothing recorded) | — |
| 5 | B05 | Decisions superseded, never edited; database blocks edits and deletes | PASS | web/db.py gate_decisions triggers; validation/gate.py gate_state | — |
| 6 | B06 | Investor view withholds values and answers; a trace search result leaked 1998 once; fixed, and after the fix the investor read has 0 x 1998 and 0 x 1996 | CORRECTED | assets/evidence/out/B06_investor_view.json (live + fixture); RUN_LOG claimed neither year appeared, corrected here | reworded in narration v4 |
| 7 | B06 | Token-less reads are served at the stored level | PASS | RUN_LOG 2026-09-25 BG+U3 open issues | — |
| 8 | B07 | No decision recorded on that run | PASS | assets/evidence/out/B00_B07_gated_run_now.json (decisions_recorded 0) | — |
| 9 | B08 | Hard rules: basic >= diluted EPS; FCF = OCF - CapEx; assets = liabilities + equity (2%) | PASS | validation/constraints.py; RUN_LOG B2+B3 | — |
| 10 | B09 | Microsoft: given 82.9B, wrote 828.9B; that attempt halted on format first | PASS | assets/evidence/out/B08_B11_checks.json (run ec40e81b '$828,860,000,000'); RUN_LOG B2+B3 | — |
| 11 | B10 | Google net income ~3x operating income, also in the filing; soft rule does not gate | PASS | assets/evidence/out/B08_B11_checks.json (run e592660c, $112.2B vs $40.77B, gates false) | — |
| 12 | B11 | Apple balance sheet adds up; 5-token request no reply in 60 s; no timeout | PASS | assets/evidence/out/B08_B11_checks.json; assets/evidence/out/B18_ledger.json | — |
| 13 | B12 | Figures located in the real filing; 24 of 24 found, all equal; every figure in the review has a Source button (U6) | PASS | assets/evidence/out/B12_filing_excerpt.json; RUN_LOG BP+U4; 'click it' reworded, no UI exists | reworded in narration v4 |
| 14 | B13 | One shared SEC fetch; lanes show real server events | PASS | assets/evidence/out/B13_stream_events.json; RUN_LOG BP+U4 | — |
| 15 | B14 | A second call to the same model extracts grade, direction, assumptions and key points from the finished answer; ungrounded quotes dropped; failure recorded, run continues | PASS | RUN_LOG 2026-09-26 'Option 1 + B5 + U8'; core/assessment.py; assets/B14_grades_1280.png (run 8ecb0922) | reworded to the extraction design |
| 16 | B15 | Drivers data / assumption / weighting; consensus only when grade and direction agree and no hard failure; reviewer accepts a grade or sets it; investors see no grade until set | PASS | validation/divergence.py; validation/gate.py policy v3; assets/B15_grade_gate_1280.png | — |
| 17 | B16 | Review reads answer first; every review exports as a plain document | PASS | RUN_LOG 2026-09-26 U5, 2026-09-27 B6+U9; assets/evidence/out/B16_export_8ecb0922_auditor.md | — |
| 18 | B18 | Anyone can mint a reviewer token; the grade is the same model judging its own answer; no model-call timeout | PASS | assets/evidence/out/B18_ledger.json; RUN_LOG B5+U8 open issues | — |

**Status:** all claims PASS or CORRECTED against RUN_LOG through B6+U9 (2026-09-27) · Divij Pawar build
