# FACTCHECK — Transport, Do Not Repair

Status: **GATE F SIGNED — 2026-09-03. 12 rows PASS, 1 PASS-WITH-CORRECTION.**

Subject: `D:/Projects/mycroft` @ **`bdc1bc1`** ("market-sentiment: add ingest and
shape-validation steps", 2026-09-03). The commit message was treated as a claim
to check, not as evidence — every figure was re-derived from the repo or from a
live run of the scripts.

| # | Beat | Claim | Verdict | Derivation |
|---|---|---|---|---|
| 1 | B01 | Last week ended with run-envelope absent and gate 2 unable to clear | ✓ PASS | Previous episode's `beat_sheet.json` B10 and its SOURCES.md; matches this commit's own message |
| 2 | B01 | Both now closed | ✓ PASS | `data/raw/market-sentiment-analysis-part-1/run-envelope.json` exists; `data/verified/market-sentiment-analysis-part-1/runs/` exists |
| 3 | B04 | Ingest does not recount, dedupe, drop, fill, or coerce | ✓ PASS | Shown verbatim from the script's `TRANSPORT, DO NOT REPAIR` docstring |
| 4 | B04 | Defective envelope declares 7 records while holding 8 | ✓ PASS | Stated in the docstring as D12; live run shows `per_file` news `record_count` 8 against the declared count |
| 5 | B04 | One file does not parse and is copied through unchanged | ✓ PASS | D18, `news-finnhub-unparseable.json.broken`; live run reports it under `parse_errors` at step 3, so it survived transport |
| 6 | B04 | "An ingest script that cleans data destroys the evidence that cleaning was needed" | ✓ PASS | Quoted verbatim from the script. This is the episode title's source |
| 7 | B07 | Step 3 must surface exactly 8 of 18 catalogued defects | ✓ PASS | Manifest: `expected_detection.step` → {3: 8, 4: 10}. Script docstring names the same ids |
| 8 | B07 | The other 10 are deliberately not detected; catching them early would make step 4 untestable | ✓ PASS | Quoted verbatim from the SCOPE docstring |
| 9 | B08 | Clean set: 0 findings, exit 0 | ✓ PASS | Live run: `status: ok`, exit 0 |
| 10 | B08 | Defective set: 4 missing fields, 3 parse errors, 1 count mismatch, exit 1 | ✓ PASS | Live run: `len(missing_fields)`=4, `len(parse_errors)`=3, `len(count_mismatches)`=1, `status: stop`, exit 1 |
| 11 | B08 | "3 parse errors" | ✓ PASS-WITH-CORRECTION | The commit message's "3 parse errors" is a **rollup**. The manifest's own taxonomy for those three is 2 `malformed_row` + 1 `unparseable_file`. The script's `parse_errors` output field does return 3, so the on-screen label "3 parse errors" is the script's term and is correct; the narration does not restate the manifest classes, to avoid implying a 3-way class split that the manifest does not have |
| 12 | B08 | A type violation has no output field; recorded as `types_deferred_to_step_4` rather than smuggled into missing_fields | ✓ PASS | Live run field, verbatim: "This step has no declared field for a type violation… Logged as a P6 contract defect, not worked around." |
| 13 | B09 | `core.autocrlf=true` made a file's SHA-256 platform-dependent; fixed by a scoped `.gitattributes` plus `newline='\n'` at five write sites | ✓ PASS | `.gitattributes` read verbatim (2 path globs, scoped to this recipe). Five write sites confirmed by grep: ingest ×2, gigo ×2, verify-provenance ×1. The sixth `newline=` match is a CSV **reader** in another workflow and is correctly excluded |
| 14 | B10 | 3 of 6 steps written; reruns byte-identical | ✓ PASS | Steps 1–3 exist under `scripts/`; rerun of step 3 over the defective set produced byte-identical SHA-256 across all 6 verified files |

## On-screen hashes (B09) — real, not illustrative

An earlier draft of this beat used invented hash prefixes as stand-ins for "two
different digests". That is an invented figure, which the REBUILD LAW forbids,
so it was replaced with the real thing — the same file's bytes hashed under each
line ending:

```
sample/clean/news-finnhub.json
  LF    3,180 bytes   sha256 441291ec39aed12cf4377c1b3b8e17ec3d369816d4aea67559077ef7b36de9e4
  CRLF  3,261 bytes   sha256 42fdf8fc253741b2e13135f9b1eaa8ec8ddcfab31390c7ac74a621d2ca8b7299
```

Reproduce: read the file's bytes, normalise to `
`, hash; then translate `
`
to `
` and hash again. The on-screen prefixes are the first eight hex digits
of those two digests. Nothing on screen is a placeholder.

## Claims deliberately NOT made

- **No claim that step 4 works.** It is not written.
- **No accuracy or quality figure for the pipeline.** `logs/RUN_LOG.md` records
  that no accuracy rate exists and none may be quoted (P3).
- **No claim that the 8 findings are correct in substance** — only that they are
  the 8 the manifest assigns to step 3, which is what was verified.
