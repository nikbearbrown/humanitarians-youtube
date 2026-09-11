# SOURCES — Both Sets Scored 64

Subject: `D:/Projects/mycroft` @ **`253ee74`** (2026-09-10). Episode 3.
Previous: `bdc1bc1` (ep 2) · `9ef4e7f` (ep 1).

| On screen | Beat | Derivation |
|---|---|---|
| 5 of 6 steps written | B01, B10 | steps 1–5 present under `scripts/` |
| FLAG, DO NOT DROP block | B04 | verbatim, `transform-quality-check.py` docstring |
| ID pass: news[2] · price[4] · reddit children[1] | B05 | live run, `duplicates[].basis == identity_key` |
| Headline pass: news[1] · news[2] | B05 | live run, `basis == headline_near_duplicate` |
| 5 findings / 4 rows | B05 | 5 entries, 4 distinct locators (news[2] under both) |
| 6 flags: 3 stale, 3 wrong type | B05 | live run `flags`, kinds counted |
| FAITHFUL PORT block | B07 | verbatim, `run-approved-tools.py` docstring |
| clean 64 · defective 64 | B08 | live runs, `scores.sentiment_analysis.overall_score` |
| 3 flags vs 8 flags | B08 | live runs, `len(scores.flags)` |
| 10-flag catalogue, 5 fire / 5 never | B09 | `FLAG_CATALOGUE` keys vs union of flags raised by both sets |
| 18/18 defects at exact locators | B10 | commit's verification note; step 3 owns 8, step 4 owns 10, manifest `expected_detection.step` splits {3:8, 4:10} |
| scores_digest stable · --no-write writes nothing | B10 | two runs → same digest, differing `generated_at`; `no_write_mode: true` |

## Not claimed

- Nothing about step 6; it is not written.
- No model or notification call was made — three handoffs, all
  `approved_for_live_action: false`.
- No accuracy figure. `logs/RUN_LOG.md` records that none exists (P3).
- The score is not treated as a market signal; the step's own
  `interpretation_warning` says it is arithmetic over a keyword count.
