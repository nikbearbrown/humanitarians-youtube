# SOURCES — weekly-fixtures-before-validators

Every figure and quoted string that appears on screen or in narration, with how
it was verified. Nothing here was taken from the commit message alone; each
number was re-derived from the repo or from a live run.

Subject: `D:/Projects/mycroft`, commit **`9ef4e7f`**
("market-sentiment: add sample fixtures + verify-provenance step").
Verified 2026-08-27.

| Claim on screen / in narration | Beat | Verified how | Result |
|---|---|---|---|
| 10 files, ~1,200 lines | B09 | `git log --since=midnight --stat` on `9ef4e7f` | 10 files changed, 1,198 insertions |
| Six declared steps, none implemented | B01, B09 | `grep -n "TODO: DEV" recipes/market-sentiment-analysis-part-1.md` | 6 step-script markers (lines 51, 56, 61, 66, 71, 76) |
| Step names (verify-provenance … produce-human-report) | B01 | same grep, script paths read off each line | exact, in recipe order |
| 18 defects | B04 | `len(manifest["defects"])` | 18 (`D01`–`D18`) |
| 7 defect classes | B04 | `{d["class"] for d in defects}` | 7 distinct |
| Per-class counts (4/4/3/3/2/1/1) | B04 | `collections.Counter` over `defects[].class` | duplicate 4, missing_required_field 4, type_violation 3, stale_timestamp 3, malformed_row 2, count_mismatch 1, unparseable_file 1 = 18 |
| D05 record shown verbatim | B03 | copied from `fixture-manifest.json`, `defects[4]` | exact, trimmed to 8 of its keys |
| "id-only dedupe walks past it" | B03 | D05 `identity_key`: "headline (near-duplicate); ids 900001 vs 900011 differ" | supported by the record itself |
| Timestamps pinned to `frozen_at` | B04 | manifest `frozen_at` = `2026-08-27T14:30:00+00:00` | present, single pinned value |
| 14 declared sources | B05, B07 | `len(result["source_paths"])` from a live run | 14 |
| Verdict split 8 / 3 / 1 / 2 | B07 | live run, counted by `verdict` | OK 8, PRESENT_NOT_PARSE_CHECKED 3, OK_UNPARSEABLE_AS_EXPECTED 1, MISSING 2 |
| Digest excludes timestamps; two runs comparable | B06, B07 | ran the script twice, compared | `findings_digest` identical, `checked_at` differs |
| `digest_basis` block shown verbatim | B06 | copied from `...-verify-provenance.py` lines 197–205 | exact, comment included |
| "A missing required source exits 1" | B07 | `raise SystemExit(1 if result['status'] == 'stop' else 0)`, and the P4 note at line 19 | exact behaviour; no required source is currently missing, so the observed exit is 0 |
| Wrong-entity signals are not covered | B08 | manifest `not_covered[0]` | stated in the manifest, including that this class reached a finished brief per `logs/RUN_LOG.md#2026-08-26` |
| `run-envelope.json` absent, gate 2 cannot clear | B09 | live run verdict `MISSING`; matches the commit's own "Not included" note | absent, not required by step 1 |

## Deliberate omissions

- **No accuracy, precision, or coverage figure appears anywhere.** `logs/RUN_LOG.md`
  records that no accuracy rate exists for this system and that none may be
  quoted (P3). The reel therefore claims only what the fixtures and the
  provenance run demonstrate.
- **No claim that steps 3–4 detect the 18 defects.** Those validators are not
  written. The manifest records which step *must* surface each defect; the reel
  says the corpus makes them gradeable, not that they pass.
- **The 11 break tests and the 18/18 locator resolution** cited in the commit
  message were re-checked only to the extent of the locator count. The reel
  mentions 18/18 locators in the ledger (B09) and makes no claim about the break
  tests, which were not re-run here.

## Corrections against the source summary

- The commit summary says "3 defective copies + 1 truncated file carrying 18
  catalogued defects". The manifest lists **7 files** in the fixture set
  (3 clean, 3 defective, 1 truncated) — consistent, but the reel says "one file
  that will not parse at all" rather than restating the count, to avoid implying
  the 18 defects live only in the truncated file.
