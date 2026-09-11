# FACTCHECK — Both Sets Scored 64

Status: **GATE F SIGNED — 2026-09-10. 14 rows PASS, 1 PASS-WITH-PRECISION.**

Subject: `D:/Projects/mycroft` @ **`253ee74`** ("market-sentiment: add
quality-check and scoring steps", 2026-09-10). Episode 3.
Every figure re-derived from a live run; the commit message was a claim to check.

| # | Beat | Claim | Verdict | Derivation |
|---|---|---|---|---|
| 1 | B01 | 5 of 6 recipe steps now written | ✓ PASS | `scripts/` contains steps 1–5; recipe declares 6 |
| 2 | B04 | "Flag, do not drop; flag, do not coerce" | ✓ PASS | verbatim from the step-4 docstring |
| 3 | B04 | `parseFloat(...) \|\| 0` turns "N/A" into a silent 0 | ✓ PASS | stated in the same docstring; matches step 5's FLAG_CATALOGUE entry `coerced_non_numeric_to_zero` |
| 4 | B05 | 5 duplicate findings across 4 rows | ✓ PASS | live run: `len(duplicates)`=5; locators are news[1], news[2]×2, price[4], reddit children[1] → 4 distinct rows |
| 5 | B05 | One row trips both passes | ✓ PASS | news `records[2]` appears under `basis=identity_key` AND `basis=headline_near_duplicate` |
| 6 | B05 | The syndicated copy has a different id and url, same headline | ✓ PASS | news `records[1]`, headline pass only; the manifest's D05 |
| 7 | B05 | 6 flags — 3 stale, 3 wrong type — all kept | ✓ PASS | live run: `len(flags)`=6, kinds `{stale_timestamp: 3, type_violation: 3}`; each carries `action: "flagged and kept"` / `"flagged and left as found"` |
| 8 | B07 | "Faithful port, loud substitutions" and the reason not to fix | ✓ PASS | verbatim from the step-5 docstring |
| 9 | B07 | A stream with no rows scores 50, a default that reads neutral | ✓ PASS | `FLAG_CATALOGUE['score_is_no_data_default']`, verbatim |
| 10 | **B08** | **Clean set scores 64; defective set scores 64** | ✓ PASS-WITH-PRECISION | live runs: clean `overall_score` 64 (`overall_score_unrounded` 63.75), defective 64 (unrounded 64.0). **Both report 64; the unrounded values differ.** The narration says "the same headline number", never "identical", and the on-screen figure is the reported score |
| 11 | B08 | 3 flags clean vs 8 flags defective | ✓ PASS | live runs: clean `[scoring_params_unattributed, untested_threshold_path, ticker_not_derived_from_question]`; defective adds `multi_quote_first_wins` + 4× `scored_row_carries_quality_flag` |
| 12 | B08 | 4 flagged rows still fed the score | ✓ PASS | 4 occurrences of `scored_row_carries_quality_flag` in the defective run |
| 13 | B09 | Catalogue has 10 flags; 5 fire on the corpus, 5 never do | ✓ PASS | parsed `FLAG_CATALOGUE` (10 keys) against the union of flags raised by both fixture sets (5 distinct) |
| 14 | B09 | The 5 unreachable ones are the substitution paths | ✓ PASS | never-fired set = coerced_missing_field_to_zero, coerced_non_numeric_to_zero, score_is_no_data_default, denominator_exceeds_scored_rows, js_undefined_concatenated |
| 15 | B10 | scores_digest stable across runs; `--no-write` writes nothing | ✓ PASS | two consecutive runs → identical `scores_digest`, differing `generated_at`; `no_write_mode: true`, `action_taken: computed_scores_no_write` |

## The one figure that needed care

Row 10. Saying the two scores are "identical" would be **false** — the
unrounded values are 63.75 and 64.0. What is true, and what the reel says, is
that both runs **report 64** as `overall_score`. The distinction matters
because the beat's whole point is that the reported number cannot distinguish
clean data from corrupted data. Overstating it to "identical" would have been
a small fabrication in service of a better line.

## Claims deliberately NOT made

- **No claim that 64 is a good or bad score.** The step's own
  `interpretation_warning` says it is "arithmetic over a keyword count, not a
  market observation"; the reel does not treat it as a market signal.
- **No claim about step 6.** Not written.
- **No claim that any model or notification ran.** All three live-call handoffs
  carry `approved_for_live_action: false` and `live_call_performed: false`.
- **No accuracy figure for the pipeline** — `logs/RUN_LOG.md` records that none
  exists and none may be quoted (P3).
