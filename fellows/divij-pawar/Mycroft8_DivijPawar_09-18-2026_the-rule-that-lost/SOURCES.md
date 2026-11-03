# SOURCES.md — the-rule-that-lost (Mycroft 8)

**DOUBLE-CHECK LAW.**
- **What must trace:** every factual claim spoken in this reel traces to the live checkout at
  `D:\Code\mycroft\verification-layer`.
- **What never counts as a source:** `Desktop\mycroft\accountability_layer`.
- **How each claim was checked:** where a claim could be recomputed, it was, by
  `assets/evidence/m8_evidence.py` (read-only). The outputs are in `assets/evidence/out/`.
- **When figures were cut:** a figure that couldn't be reproduced was corrected or cut. See
  "Corrections" below.

**Verification pass:** 2026-09-26, 22:49 UTC.
- Python 3.12.6 on Windows 11.
- The checkout's HEAD is `c53746a` (2026-08-21), with **80 uncommitted paths**.
- Input SHA-256 hashes are in `assets/evidence/out/run_env.json`.

---

## Sources read or executed directly

| Ref | Source | How it was used |
|---|---|---|
| S1 | `logs/RUN_LOG.md`: entries BL, B0, "Directive echo, properly", B1+U2, B2+B3, BP+U4 (2026-09-24 → 25) | Narrative and logged figures |
| S2 | `tests/fixtures/edgar_aapl_companyfacts_sample.json` (trimmed real SEC payload) | B02/B03 recomputed: legacy `max(end)` rule vs `select_fact` |
| S3 | `tests/fixtures/cross_agent_real_runs_corpus.json` (labelled corpus) | B07/B08/B09 recomputed with both rules |
| S4 | `web/frontend/tests/fixtures/stream_compare_aapl_2026-09-24.txt` (real captured stream) | B05 overlap recomputed from `started_at` + `duration_ms` |
| S5 | Fixtures `run_compare_auditor.json` (pre-B1), `run_compare_b1.json` (MSFT), `run_compare_b3_aapl.json` (`20c538e4`) | B10 key counts; B13 rows |
| S6 | `web/data/accountability.db` (opened read-only) | B04 real search args; B06 NVDA run `2220eba0`; B11 echo replay |
| S7 | `validation/facts.py`, `validation/concept_linkage.py`, `datasources/edgar.py`, `core/parsing.py`, `core/directive.py` | Called by the evidence script, unmodified |
| S8 | `tests/test_facts.py`, `tests/test_edgar_facts.py`, `tests/test_concurrency_and_stream.py` | Test cases cited on screen |
| S9 | `python -m unittest discover -s tests -t .` → **390 OK**; `npx vitest run` → **74 passed** (2026-09-26) | B12, B14 |
| S10 | `git log -1` / `git status --short` | B15, B16 |
| S11 | Live app `/app` on the local server, captured headless (`assets/evidence/capture_app.mjs`) | B10, B12, B13 screenshots |

## Beat-by-beat claims

| Beat | Claim in narration | Verified value | Source |
|---|---|---|---|
| B00 | Old rule 1 alarm, new 6, on the same 16 runs | `concept_aware_flags: 1`, `canonical_flags: 6`, 16 `disjoint_concepts` runs | S3 → `out/B09_corpus_replay.json` |
| B02 | Revenue handed was fiscal 2018 | Legacy pick: 265,595,000,000, `fy 2018`, `FY`, 10-K, 2017-10-01 → 2018-09-29 | S2 → `out/B02_B03_…json` |
| B02 | EPS 6.88 was nine months; quarter 2.02 | Legacy pick 6.88, 272-day span; B0 selects 2.02 (Q3 FY2026) | same |
| B02 | Net income year to date | Legacy 101,464,000,000 (272 days); B0 29,789,000,000 | same |
| B02 | Assets correct | Instant value; both rules agree | same |
| B03 | Quarter = 80–100 days; YTD last resort; restatement wins | `select_fact` docstring and `tests/test_edgar_facts.py` | S7, S8 |
| B04 | Failed searches recorded as ok | RUN_LOG B0 (the `_call_tool` fix) | S1 |
| B04 | Invented, contradictory settings; query-only retry recovers | Run `1b691654`: `start_date 2026-06-30` after `end_date 2026-03-31`, `include_domains ["NASDAQ:MSFT"]`, `include_images "false"` (a string); retry → 5 URLs; 35 retried steps stored | S6 → `out/B04_…json` |
| B05 | Started 1 ms apart, 39 s overlap | Recomputed: `start_gap_ms 1.0`, `overlap_s 39.4` | S4 → `out/B05_…json` |
| B05 | Speed-up not measured | RUN_LOG BL open issue | S1 |
| B06 | Tolerances: EPS to the cent, 0.5%, 0.1 point | `TOLERANCE` in `validation/facts.py` | S7 |
| B06 | MSFT figure written two ways now one figure | **Test case**: "82,886,000,000.0" vs "$82.9 billion" → `MATCH`, variance 0.02%. The old set difference listed both as divergent | S8 → `out/B06_figures_not_strings.json` |
| B06 | Nvidia run: self-rated 90% had raised the alarm | Run `2220eba0`: stored `divergent_numbers ["90%"]`, flag true; B1 extracts no figure from "90%" | S6 → same file |
| B07 | Two Apple runs: asset turnover 0.13 (and 0.12) vs 0.69 | `56965308` stated 0.13, `8c67de62` stated 0.12; both `DERIVED_WRONG`, recomputed 0.693 | S3 → `out/B07_…json` |
| B07 | Same runs got net margin right | `DERIVED_OK`: 38.1% vs 38.2%; 0.38 vs 0.382 | same |
| B07 | Google ROA 18.96% vs 18.85% | `2c3c4f23`, `0f729a69` (both "Google LLC (GOOGL)"): `DERIVED_OK` | same |
| B08 | Old tagger files ROA under Assets | `tag_numbers` on the real corpus sentence: "18.85%" → `Assets` | S3 → `out/B08_…json` |
| B09 | One of six is Mycroft 5's fabrication | `f4a4c782`, divergent `["0.34"]`, flagged by both rules | S3 → `out/B09_…json` |
| B09 | Five can't be judged (visual names them: ROA for a bank, asset-to-income ratio) | Flagged ids `2db3762c 515f263a a1cbd371 ba546346 ff344935`; RUN_LOG B1+U2 names JPM ×2, NVDA, JNJ, V | S1, S3 |
| B10 | Records went from 7 fields to 14 | Pre-B1 fixture 7 keys; B1 fixture 14 | S5 → `out/B10_…json` |
| B10 | The screen says which rule decided | Screenshot: "Recorded verdict (concept-aware rule): Flagged for review" | S11 → `assets/B10_…png` |
| B11 | 17 of 135 conclusions copied the prompt | Logged figure (RUN_LOG, 2026-09-24). Today's replay: 18 of 184, because more runs have been stored since | S1, S6 → `out/B11_…json` |
| B11 | `[/conclusion]` in 3 of 22 first attempts | RUN_LOG B1+U2 | S1 |
| B11 | Final batch: 0 first-attempt failures, 8 agents | RUN_LOG B1+U2 | S1 |
| B13 | First same-figure agreement, and the filing agreed | Run `20c538e4`: net income $29.79B vs $29.788B `MATCH`; EPS $2.02 = $2.02 `MATCH` (basic/diluted not stated); both source checks pass | S5 → `out/B13_…json`; `assets/B13_…png` |
| B13 | NVDA/GOOGL agent said the figure was missing | RUN_LOG B2+B3 | S1 |

## Corrections made by this verification pass

| Where | Draft said | Evidence showed | Now |
|---|---|---|---|
| B06 | "Microsoft's $82.9B finally equals $82,886,000,000" (as a live result) | It's a unit test (`tests/test_facts.py` ~l.114). No stored run has that row | Narrated and labelled as a test case |
| B07 | Google ROA "within a tenth of a point" | 18.96 − 18.85 = 0.11 | Both numbers spoken; "close enough" |
| B13 | "for the same quarter", row label "EPS diluted" | Neither agent stated a period; the row is "EPS (basic or diluted not stated)" | "from the same filing"; label corrected |
| B12, B14 | 60 / 379 tests | 74 / 390 on 2026-09-26 | Updated |

**Finding for the verification layer, outside this reel.** RUN_LOG's B1+U2 entry lists the MSFT
"82,886,000,000.0 vs $82.9 billion → MATCH" under **Live**, but it comes from a unit test. The
log is append-only, so the human should log a correction there.

## Declared simplifications

- **The "three tiers":** the roadmap's names are simplified to "reconcile, check, classify".
- **"Metric, period, unit, source":** a teaching distillation of the canonical-fact fields
  (entity, metric, period, value, unit, source).
- **"Tagging still works on wording":** the extractor is lexical (alias matching), as the ledger's
  `checks-lexical-coverage` entry and the B1 open issues say.

## Not verified here

- Whether LangFuse nesting works across threads. It is not claimed in the video.
- Any speed-up from concurrency. It is not claimed.
