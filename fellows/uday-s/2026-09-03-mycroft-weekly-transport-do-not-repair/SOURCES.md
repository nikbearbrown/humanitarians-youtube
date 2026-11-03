# SOURCES — Transport, Do Not Repair

Subject: `D:/Projects/mycroft` @ **`bdc1bc1`** (2026-09-03),
"market-sentiment: add ingest and shape-validation steps".
Previous episode: `weekly-fixtures-before-validators` @ `9ef4e7f`.

Every figure was re-derived here; the commit message was a claim to check.

| On screen | Beat | Derivation |
|---|---|---|
| run-envelope exists · gate 2 clears | B01, B10 | `data/raw/market-sentiment-analysis-part-1/run-envelope.json` present |
| gate 3 clears | B01, B10 | `data/verified/market-sentiment-analysis-part-1/runs/` present |
| TRANSPORT, DO NOT REPAIR block | B04 | verbatim, `scripts/ingest/...-ingest-inputs.py` docstring |
| declares 7 records, holds 8 (D12) | B04 | named in the docstring; step-3 live run reports news `record_count` 8 |
| the .broken file copied through unchanged (D18) | B04 | survives to step 3, where it appears in `parse_errors` |
| SCOPE block · 8 of 18 · ids named | B07 | verbatim, `scripts/gigo/...-validate-data-shape.py` docstring |
| 8 / 10 defect split | B07 | manifest `expected_detection.step` → `{3: 8, 4: 10}` |
| clean: 0 findings, exit 0 | B08 | live run, `status: ok`, returncode 0 |
| defective: 4 / 3 / 1, exit 1 | B08 | live run: `len(missing_fields)`=4, `len(parse_errors)`=3, `len(count_mismatches)`=1, `status: stop`, returncode 1 |
| types have no field at all | B08 | live run `types_deferred_to_step_4`, verbatim |
| LF 3,180 B · sha256 441291ec… | B09 | recomputed: file bytes normalised to `\n`, sha256 |
| CRLF 3,261 B · sha256 42fdf8fc… | B09 | recomputed: same bytes with `\n`→`\r\n`, sha256 |
| .gitattributes + newline='\n' × 5 | B09 | `.gitattributes` read verbatim (2 globs); five write sites confirmed by grep — ingest ×2, gigo ×2, verify-provenance ×1 |
| 3 of 6 steps written | B10 | steps 1–3 exist under `scripts/`; recipe declares 6 |
| reruns byte-identical | B10 | step 3 rerun over the defective set → identical sha256 for all 6 verified files |

## Not claimed

- Nothing about step 4; it is not written.
- No accuracy/quality figure — `logs/RUN_LOG.md` records that none exists and
  none may be quoted (P3).
- The 8 findings are verified as *the 8 the manifest assigns to step 3*, not as
  substantively correct judgements about market data.
