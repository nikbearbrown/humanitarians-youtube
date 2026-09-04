# FACTCHECK — weekly-fixtures-before-validators

Status: **GATE F SIGNED — 2026-08-27. 14 rows PASS, 1 row PASS-WITH-WORDING.
No unresolved fixes.**

First-party source: the subject repo itself, `D:/Projects/mycroft` @ `9ef4e7f`.
Every row was re-derived from the repo or from a live run of the script — the
commit message was treated as a claim to check, not as evidence. Derivations
are recorded in `SOURCES.md`.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B00–B01 | The recipe declares six development steps and none had an implementation | ✓ PASS | `grep -n "TODO: DEV" recipes/market-sentiment-analysis-part-1.md` → 6 step-script markers, lines 51/56/61/66/71/76 | — |
| 2 | B01 | The six step names, in recipe order | ✓ PASS | Script paths read off those six lines: verify-provenance, ingest-inputs, validate-data-shape, transform-quality-check, run-approved-tools, produce-human-report | — |
| 3 | B02 | Three clean fixtures, one per stream — Alpha Vantage prices, Finnhub news, Reddit posts | ✓ PASS | `sample/clean/` contains exactly price-alpha-vantage.json, news-finnhub.json, reddit-wallstreetbets.json | — |
| 4 | B03 | The D05 record, shown verbatim | ✓ PASS | Copied from `fixture-manifest.json` → `defects[4]`; 8 of its keys shown, none altered | — |
| 5 | B03 | D05 is a syndicated story: different id, different url, identical headline | ✓ PASS | D05 `identity_key`: "headline (near-duplicate); ids 900001 vs 900011 differ"; `description` names the syndication case | — |
| 6 | B03 | An id-only dedupe misses it and inflates the news denominator | ✓ PASS | Stated in D05's own `description` field; consistent with `duplicate_counting_rule` | — |
| 7 | B04 | Eighteen defects | ✓ PASS | `len(manifest["defects"])` = 18, ids D01–D18 contiguous | — |
| 8 | B04 | Across seven classes, with the named classes | ✓ PASS | Counter over `defects[].class`: duplicate 4, missing_required_field 4, type_violation 3, stale_timestamp 3, malformed_row 2, count_mismatch 1, unparseable_file 1 → 7 classes, 18 total | — |
| 9 | B04 | Timestamps pinned to a frozen value, never `now()` | ✓ PASS | `frozen_at` = `2026-08-27T14:30:00+00:00`; single pinned value, plus a stated `freshness_policy` | — |
| 10 | B05, B07 | Fourteen declared sources | ✓ PASS | Live run: `len(result["source_paths"])` = 14 | — |
| 11 | B07 | Checked for existence, size, SHA-256 and parseability | ✓ PASS | Each finding carries `exists`, `size_bytes`, `sha256`, `parsed_ok` | — |
| 12 | B07 | 8 parse clean · 3 present · 1 unparseable as declared · 2 absent | ✓ PASS | Live run verdict tally: OK 8, PRESENT_NOT_PARSE_CHECKED 3, OK_UNPARSEABLE_AS_EXPECTED 1, MISSING 2 = 14 | — |
| 13 | B06, B07 | The digest excludes timestamps, so two runs over unchanged files are comparable | ✓ PASS | Ran the script twice: `findings_digest` identical, `checked_at` differs. Code comment and `digest_basis` key list confirm the exclusion | — |
| 14 | B07 | "A missing required source exits 1" | ✓ PASS-WITH-WORDING | `raise SystemExit(1 if result['status'] == 'stop' else 0)`; P4 note at line 19. No required source is currently missing, so the observed run exits 0 | Narration states the RULE, not the observed exit. Kept in the conditional ("would exit nonzero" / "exits 1" as the rule). Do not let this drift into a claim that the run failed |
| 15 | B08 | Wrong-entity signals are not covered, and that class reached a finished brief | ✓ PASS | Manifest `not_covered[0]`, which cites `logs/RUN_LOG.md#2026-08-26` for the finished-brief incident | — |
| 16 | B09 | 10 files, ~1,200 lines, step 1 of 6 closed; run-envelope absent, gate 2 cannot clear | ✓ PASS | `git show --stat 9ef4e7f` → 10 files, 1,198 insertions; live run marks `run-envelope.json` MISSING; matches the commit's own "Not included" note | — |

## Claims deliberately NOT made

- **No accuracy, precision, recall or coverage figure appears anywhere.**
  `logs/RUN_LOG.md` records that no accuracy rate exists for this system and
  that none may be quoted (P3). Any such number would be a fabrication.
- **No claim that steps 3–4 detect the 18 defects.** Those validators do not
  exist yet. The reel says the corpus makes them *gradeable*, which is what the
  manifest's `expected_detection` fields support.
- **No claim about the 11 break tests** cited in the commit message. They were
  not re-run during this build, so the reel does not mention them.
- **No verdict on the pipeline's fitness for real market data.** Out of scope
  and unevidenced.

## DOUBLE-CHECK LAW — dating

Stripped: no model version numbers, no tool version numbers, no "as of today"
phrasing. The one date on screen is the commit short SHA (`9ef4e7f`) in B09,
which is a stable identifier rather than a drifting count.
