# FACTCHECK — It Never Says Pass

Status: **GATE F SIGNED — 2026-09-17. 13 rows PASS, 1 PASS-WITH-PRECISION.**

Subject: `D:/Projects/mycroft`, branch `feature/market-sentiment-human-report`,
commit **`aa0c0fe`** ("market-sentiment: add the human report step, completing
all six", 2026-09-17). Episode 4.

Every figure re-derived from a live run of step 6; the commit message was a
claim to check.

| # | Beat | Claim | Verdict | Derivation |
|---|---|---|---|---|
| 1 | B01, B10 | All six steps now exist | ✓ PASS | `STEP_SCRIPTS` lists 6; all six files present under `scripts/` |
| 2 | B04 | "An audit reports what it found; it never says pass" | ✓ PASS | verbatim from the step-6 docstring. Episode title comes from this line |
| 3 | B04 | The sentiment score is an INFERRED finding, not verified | ✓ PASS | docstring "VERIFIED VERSUS INFERRED"; confirmed in the live run's `findings.inferred` |
| 4 | B05 | Defective set: 10 verified, 5 inferred | ✓ PASS | live run `len(findings.verified)`=10, `len(findings.inferred)`=5 |
| 5 | B05 | The overall 64 appears under inferred | ✓ PASS | live run: `"Overall sentiment 64/100 (SLIGHTLY BULLISH) for ticker FAKE"` in `findings.inferred` |
| 6 | B05 | Component scores news 67 · social 67 · price 60 | ✓ PASS | live run, same list |
| 7 | B05 | Envelope declared 7 records but holds 8 | ✓ PASS | live run `findings.verified`, verbatim |
| 8 | B07 | One pass writes both artifacts so they cannot disagree | ✓ PASS | docstring "TWO CUSTOMERS, TWICE", verbatim |
| 9 | B08 | 15 of 15 report sections present | ✓ PASS | live run: `len(report_sections_required)`=15, `len(report_sections_missing)`=0 |
| 10 | B08 | 16 of 16 required log fields | ✓ PASS-WITH-PRECISION | `--no-write` reports exactly the 16 contract fields. A **write** run reports 17 — the extra is `artifact_hashes`, which only exists once files are written. The contract requires 16; the reel says 16 |
| 11 | B08 | Six gates, every one "evidence recorded; awaiting a named human" | ✓ PASS | live run: 6 gate rows, all with that status, `cleared_by: null`, `cleared_at: null` |
| 12 | B08 | Report and audit byte-identical across reruns; log differs in exactly one field | ✓ PASS | two consecutive runs: report and audit SHA-256 identical; log diff = `['generated_at']` only |
| 13 | B08 | `--no-write` creates nothing | ✓ PASS | file-tree snapshot before/after: **0** files created |
| 14 | B09 | Gate 4 is satisfiable by doing nothing | ✓ PASS | live run `gate_results[3].note`, verbatim: "This gate as written is satisfiable by doing nothing: it passes if the script exists OR if the [TODO: DEV] text is still in the recipe. Both are currently true." |
| 15 | B10 | Gate 5 has no approval record; live execution blocked; 9 typed TODOs | ✓ PASS | live run `next_decision.live_execution` = "BLOCKED - no gate-5 approval record exists…"; `len(typed_todos)`=9 |

## The figure that needed precision

Row 10. The commit says "16/16 log fields". That is correct for the contract,
and a `--no-write` run reports exactly those 16. But a **write** run reports
17, because `artifact_hashes` is added once there are artifacts to hash. Saying
"17 fields" would have been wrong about the contract; saying "16/16 required"
is right in both modes, and that is what the reel says.

## Claims deliberately NOT made

- **No claim that any gate passed** — that is the entire point of the episode.
- **No claim that the pipeline is correct or production-ready.** Six steps
  exist and run; the report itself declines to conclude.
- **No accuracy figure.** `logs/RUN_LOG.md` records that none exists (P3).
- **No claim about a model or notification call** — `live_call_performed` and
  `model_call_performed` are both false.
- The conformance figure from the commit ("187 files") was **not re-verified**
  in this session and does not appear in the reel.

## Repo hygiene

The verification runs rewrote one file's `generated_at`
(`logs/…-2026-08-27-clean.json`). It was restored with `git checkout --` and
the working tree left clean.
