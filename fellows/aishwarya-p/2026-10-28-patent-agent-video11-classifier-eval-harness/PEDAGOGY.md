# PEDAGOGY — Measuring the Classifier (hai cli-explainer, patent agent progress video 11)

A progress-recap video on the first real step toward measuring the Claims Agent's scope classifier: an evaluation harness that scores the classifier against human labels (accuracy, Cohen's kappa, majority baseline, collapse check), a single BigQuery pull that returned a 160-patent candidate pool for ~$0.92 at list price, and a real finding about the data: most patents have only 1-3 independent claims, which changed how the 50-claim set was built. It ends honestly: labeling is paused for the project lead's review, so there is no accuracy number yet.

## Act structure

- B00A presenter intro ✓
- B00 cold open — the real problem: an earlier spot check came back all narrow/defensive, and reading outputs can't say whether that's the patents or the prompt ✓
- B01 — the evaluation harness: what it measures, what kappa means, and the offline test with a fake always-narrow/defensive classifier ✓
- B02 — why one query for 160 candidates costs about the same as one patent, and the real scan size and cost ✓
- B03 — the finding: 147 of 160 patents have 1-3 independent claims; how the 16 patents and 50 claims were picked ✓
- B04 — what's not done: labeling paused for lead review, no accuracy number, the narrow/defensive question still open ✓
- B05 — HANDOFF, a concrete check: test one data assumption against a real sample before sizing an eval set ✓
- B06 — OUTRO ✓

## Evidence discipline

| Claim | Source | Verdict |
|---|---|---|
| An earlier spot check came back narrow and defensive on every result | Video 5 narration (2026-09-11, "Broadening the Test", B04) | OK — scoped to that spot check; no claim count stated (see Friction) |
| Harness reports accuracy, Cohen's kappa, majority baseline, collapse check at 80% | `eval_classifier.py` this session (`COLLAPSE_SHARE = 0.80`) | OK — directly verified in code |
| Fake always-narrow/defensive classifier: kappa 0.00 on both dimensions, both collapse warnings fired | Offline `--mock constant` run this session, on synthetic labels | OK — directly observed; no API calls |
| Patents table is not partitioned or clustered | BigQuery table metadata (`get_table`) this session | OK — directly verified |
| One-patent lookup: 127.6 GB, ~$0.73 | Free dry run this session: 127,631,094,884 bytes at $6.25/TiB | OK — directly measured |
| Pool query: 161.8 GB, ~$0.92 at list price, one query, 160 candidates | Dry run and real job this session: 161,830,838,862 bytes, 160 rows | OK — directly measured; billed bytes matched the dry run |
| 147 of 160 candidates have 1-3 independent claims; 13 have 4+ (57/46/44/8/5) | `parse_pool()` over `eval/claims_pool.jsonl` this session | OK — directly counted |
| 50 claims from 16 patents, 2 per CPC section A-H, at most 4 per patent | `eval/labeled_claims.csv` re-checked against the raw pool this session (14×3 + 2×4, no duplicates, all independent) | OK — directly verified |
| Candidates: US grants 2020-2024, 20 per section, picked by hash; patents with fewer than 3 independent claims skipped | `pull_eval_claims.py` query and `select()` this session | OK — directly verified in code |
| Plan assumed ~5 independent claims per patent | CLAUDE.md open item: ~50 claims from 8-10 patents | OK — inferred from the stated plan; narration says "assumed", not "documented" |
| Labeling is paused for project lead review | Aishwarya's instruction this session | OK — stated by the author |

## Friction protected

- Kept: no accuracy number is claimed anywhere. B04 says plainly that whether the classifier is stuck on narrow/defensive is still open.
- Kept: the cost is "$0.92 at list price", not "it cost $0.92". The project may be inside BigQuery's free tier, in which case the actual charge was $0.
- Kept: the B00 spot check gives no claim count. Video 5's narration says "eight" in one beat and "six" in the next, and Video 4 had one broad/offensive reading on a claim from the same semiconductor patent. Aishwarya chose to state the pattern without a count.
- Kept: the offline harness test is described as a test of the harness with a fake classifier, not as a result about the real classifier.
- Kept: B02 and the scene use decimal GB. An earlier draft said "one hundred fifty-one gigabytes", which was the GiB figure. Corrected to 161.8 GB.
- Kept: requiring 3+ independent claims per patent is a selection choice that may skew the set toward broader-drafted patents. B03 states the rule rather than hiding it.

VERDICT: PASS
