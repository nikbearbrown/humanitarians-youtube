# assets/ — the-rule-that-lost

Real evidence only. There are two kinds of file here:

- **Computed outputs** (`evidence/out/*.json`). `evidence/m8_evidence.py` produced them from the live verification layer, read-only.
- **App captures** (`*.png`). `evidence/capture_app.mjs` took them from the locally running
  `/app` with headless Chrome at 2× scale, clicking only view controls.

Per `brutalist.art/docs/EXECUTABLE-EVIDENCE.md`, nothing here is mocked. Show computed
values as recorded output, and show captures as the real app.

**To regenerate** (the server must be running on :8000 for the captures):

```bash
python assets/evidence/m8_evidence.py
node assets/evidence/capture_app.mjs
```

## Files

| File | Beat | Kind | What it is | SHA-256 (first 16) |
|---|---|---|---|---|
| `B10_recorded_verdict_1280.png` | B10 | HOLD | App capture, run 20c538e4: headline counted from rows + 'Recorded verdict (concept-aware rule)' | `ab516f4c5a8700fd` |
| `B12_matrix_1280.png` | B12 | HOLD | App capture, run 20c538e4: comparison matrix, desktop 1280 px @2x | `ec8361a64338d4f5` |
| `B12_matrix_375.png` | B12 | HOLD | App capture, same run, phone 375 px @2x (rows as cards) | `5946a048f5077b15` |
| `B13_shared_rows_1280.png` | B13 | HOLD | App capture: the matrix with the EPS and net income MATCH rows | `4be78b273e0ea6d6` |
| `evidence/capture_app.mjs` | B10-B13 | code | Headless Chrome capture of /app (view controls only) | `8698eed8612db770` |
| `evidence/m8_evidence.py` | all | code | Evidence script (read-only against verification-layer) | `fe107693ea290c57` |
| `evidence/out/B02_B03_what_they_were_handed.json` | B02-B03 | data | Legacy max(end) picks vs select_fact on the real AAPL payload | `587dd3c3d2b48dcf` |
| `evidence/out/B04_search_args_and_retry.json` | B04 | data | Real invented search args + query-only retry (run 1b691654) | `8cfa85d0036a1542` |
| `evidence/out/B05_overlap_from_stream.json` | B05 | data | Start gap 1.0 ms, overlap 39.4 s from the captured stream | `3d073c6f50cf914b` |
| `evidence/out/B06_figures_not_strings.json` | B06 | data | MSFT-format TEST CASE match; NVDA run 2220eba0 '90%' | `f9c6505002d2b86d` |
| `evidence/out/B07_derivation_checks.json` | B07 | data | DERIVED_WRONG 0.13/0.12 vs 0.693; DERIVED_OK net margin, GOOGL ROA | `464dc8f51989c8dd` |
| `evidence/out/B08_old_tagger_on_return_on_assets.json` | B08 | data | tag_numbers on the real sentence: '18.85%' -> Assets | `d2f655db7ef71a33` |
| `evidence/out/B09_corpus_replay.json` | B00, B09 | data | 16 disjoint runs: concept_aware 1, canonical 6 (+ ids) | `6e242c3926d59513` |
| `evidence/out/B10_record_growth.json` | B10 | data | Stored-run keys 7 -> 14 | `1d3e3c0b8999325b` |
| `evidence/out/B11_echo_replay_today.json` | B11 | data | Echo detector replay today: 18 of 184 (logged figure 17 of 135) | `17395b1c78c8b6d2` |
| `evidence/out/B13_first_shared_match.json` | B13 | data | Run 20c538e4 EPS + net income MATCH rows, period not stated | `9b8d3e13ccb32125` |
| `evidence/out/capture_log.txt` | B10-B13 | log | What capture_app.mjs clicked and clipped, with timestamp | `c5672f15b89eb2bf` |
| `evidence/out/run_env.json` | all | env | Python/platform, checkout HEAD + dirty count, input SHA-256 | `37d0584957d79f9f` |

## Still to capture or build

| Beat | Asset | How |
|---|---|---|
| B02 | Companyfacts excerpt image | Render in the Manim scene from out/B02_B03_what_they_were_handed.json (typeset as recorded output). Don't screenshot an editor. |
| B05 | Timeline bars | Draw in Manim from out/B05_overlap_from_stream.json (spans per agent). |
| B07 | MathTex fraction | Typeset in the scene; verify 265.6 / 383.3 = 0.6929 in-scene (MATH-TYPESETTING.md). |
| B11 | Three excerpts | Pull verbatim from stored runs (see examples in out/B11_echo_replay_today.json) when building the scene. |
| B15 | git panel | Re-run `git -C D:/Code/mycroft/verification-layer status --short | wc -l` on recording day. |
