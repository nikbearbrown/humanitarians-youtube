# FACTCHECK.md — the-rule-that-lost (GATE F)

Claims as spoken or shown, each traced to the live checkout at `D:\Code\mycroft\verification-layer`
or to the reel's computed evidence in `assets/evidence/out/` (see `SOURCES.md` for the full pass).

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | A stricter comparator raised 6 alarms instead of 1 on the same 16 labelled runs | PASS | assets/evidence/out/B09_corpus_replay.json (concept_aware 1, canonical 6, 16 disjoint runs) | — |
| 2 | B02 | Revenue handed to agents was fiscal 2018 | PASS | assets/evidence/out/B02_B03_what_they_were_handed.json (val 265595000000, fy 2018, FY, 10-K) | — |
| 3 | B02 | EPS 6.88 was nine months; the quarter was 2.02 | PASS | assets/evidence/out/B02_B03 (272-day span; select_fact 2.02, Q3 FY2026) | — |
| 4 | B02 | Net income was year to date | PASS | assets/evidence/out/B02_B03 (101.464B, 272 days; quarter 29.789B) | — |
| 5 | B03 | Quarters chosen by day span; restatement wins | PASS | datasources/edgar.py select_fact; tests/test_edgar_facts.py | — |
| 6 | B04 | Failed searches were recorded as success; one query-only retry returns real results | PASS | RUN_LOG 2026-09-24 B0; assets/evidence/out/B04_search_args_and_retry.json (run 1b691654, 5 URLs) | — |
| 7 | B05 | Agents started 1 ms apart, overlapped 39 s; speed-up not claimed | PASS | assets/evidence/out/B05_overlap_from_stream.json (1.0 ms, 39.4 s) | — |
| 8 | B06 | EPS to the cent; 0.5% for large figures; 0.1 point for % changes | PASS | validation/facts.py TOLERANCE | — |
| 9 | B06 | 82.9 billion = 82,886,000,000 in a constructed example | CORRECTED | assets/evidence/out/B06_figures_not_strings.json; was presented as a live run, reworded to a constructed example | reworded in narration v4 |
| 10 | B06 | Stored Nvidia run: self-rated 90% had raised the alarm | PASS | assets/evidence/out/B06 (run 2220eba0, divergent ['90%']) | — |
| 11 | B07 | Asset turnover stated 0.13 and 0.12 vs recomputed 0.69 (more than 5x) | PASS | assets/evidence/out/B07_derivation_checks.json (runs 56965308, 8c67de62; 265.6/383.3 = 0.693) | — |
| 12 | B07 | Google ROA stated 18.85, recomputes to 18.96 | CORRECTED | assets/evidence/out/B07 (runs 2c3c4f23, 0f729a69); earlier 'within a tenth of a point' corrected (0.11) | reworded in narration v4 |
| 13 | B08 | Old tagger filed 'Return on Assets' 18.85% under Assets | PASS | assets/evidence/out/B08_old_tagger_on_return_on_assets.json | — |
| 14 | B09 | Old rule 1 alarm, new 6; one is a fabricated D/E 0.34; five have no components | PASS | assets/evidence/out/B09_corpus_replay.json (f4a4c782 divergent ['0.34']; flagged ids listed) | — |
| 15 | B10 | Stored records grew from 7 fields to 14 | PASS | assets/evidence/out/B10_record_growth.json | — |
| 16 | B11 | 17 of 135 conclusions copied the prompt; 3 of 22 used square brackets; final batch 0 first-attempt failures across 8 agents | PASS | RUN_LOG 2026-09-24 (echo entry, B1+U2); today's replay 18 of 184 in assets/evidence/out/B11_echo_replay_today.json | — |
| 17 | B13 | Both agents cited the same net income and EPS, matching the filing | CORRECTED | assets/evidence/out/B13_first_shared_match.json (run 20c538e4); 'same quarter' reworded to 'same filing' (no period stated) | reworded in narration v4 |
| 18 | B13 | One agent said the shared figure was missing although in its input (NVDA, GOOGL) | PASS | RUN_LOG 2026-09-25 B2+B3 | — |
| 19 | B16 | End-card figures (6 of 16, 1 real, 5 unknown; 5x ratio errors) | PASS | same sources as B07 and B09 | — |

**Status:** all claims PASS or CORRECTED · Divij Pawar build, 2026-09-26
