# PEDAGOGY — What the Baseline Found (hai cli-explainer, patent agent progress video 12)

A progress-recap video on the first real measurement of the Claims Agent's scope classifier. Fifty independent claims from sixteen patents were labeled by hand, and the classifier was run on all of them once. Accuracy looked moderate (breadth 0.66, posture 0.60) but fell below the always-same-answer baseline, and Cohen's kappa showed almost no agreement beyond chance (0.08 and 0.00). The surprise was the direction: instead of the suspected collapse onto narrow/defensive, the classifier leaned broad/offensive on functional claim language. The video also covers a real bug: three claims on one patent failed because the model refused partway through its answer, and the fix to the refusal handling.

## Act structure

- B00A presenter intro ✓
- B00 cold open — the suspicion (stuck on narrow/defensive) and the measured result (leaning the other way) ✓
- B01 — the test set: last week's single query and 160 candidates, 50 claims from 16 patents, labeled by hand this week ✓
- B02 — the baseline run: accuracy next to the majority baseline, then kappa ✓
- B03 — the finding: 11 broad/offensive predictions, 10 of them labeled narrow; functional wording vs named parts; the all-defensive label caveat ✓
- B04 — the refusal bug: mid-answer refusals broke the parser, the diagnostic call, the stop_reason fix, 50/50 scored ✓
- B05 — HANDOFF, a concrete check: score an always-most-common-answer model before trusting accuracy ✓
- B06 — OUTRO ✓

## Evidence discipline

| Claim | Source | Verdict |
|---|---|---|
| Earlier readings looked narrow and defensive; the team suspected the classifier was stuck on one answer | Video 5 narration ("Broadening the Test", B04) and Video 11 (B00, B04); the "Classifier evaluation harness" open item in CLAUDE.md | OK — the suspicion is documented, and the narration frames it as a suspicion |
| One BigQuery query, $0.92, 160 candidate patents | Real job this session: 161,830,838,862 bytes at $6.25/TiB list price, 160 rows | OK — directly measured; covered in Video 11 |
| 50 independent claims from 16 patents, 2 per CPC section A-H | `eval/labeled_claims.csv` (50 unique claims, 16 patents, 2 per section) | OK — directly verified |
| All 50 labeled by hand, with breadth, posture and a note | `eval/labeled_claims.csv`, labeled by Aishwarya; every row has a `label_notes` entry | OK — directly verified |
| Labels: 46 narrow / 4 broad; 50 defensive | Count over `eval/labeled_claims.csv` after the six posture cells were cleaned (explanations moved to label_notes) | OK — directly counted |
| Baseline cost at most $0.32 | `eval_classifier.py` estimate: 50 calls, 34,128 input tokens (estimated), 25,000 max output tokens, claude-sonnet-5 at $2/$10 per MTok | OK — an upper bound; actual usage was not recorded, and the narration says "at most" |
| Breadth acc 0.66, kappa 0.08, majority baseline 0.92; posture acc 0.60, kappa 0.00, majority baseline 1.00 | `eval/runs/baseline_report.md` (50 scored, 0 errors) | OK — directly from the report |
| 11 claims predicted broad/offensive; 10 of those labeled narrow | Count over `eval/runs/baseline.jsonl` joined with the labels | OK — directly counted |
| The model treated functional wording ("configured to", "a protrusion") as broad | Model reasoning text in `baseline_report.md` disagreements (US-11083299-B2#1, US-11776821-B2#9, and others) | OK — quoted phrases appear in the model's own reasoning |
| No collapse warning fired | `baseline_report.md` collapse check | OK — directly from the report |
| Three claims on US-11766760-B2 (cryogenic grinding) failed; raising max_tokens 500 → 1000 didn't help | Baseline run and retry this session (claims 1 and 5 failed twice; claim 7 came back declined) | OK — directly observed |
| The model refused partway through its answer: stop_reason "refusal", 155 of 1000 output tokens | One diagnostic call on claim 1 this session | OK — directly observed for claim 1; claim 7's cached result records stop_reason=refusal; claim 5 failed the same way (see Friction) |
| The code only handled empty refusals; fixed to treat any refusal as declined; 50/50 now scored | `claim_classifier.py` diff (commit 3bcf1b1 on nikbearbrown/mycroft); re-scored offline from the cache, 0 API calls | OK — directly verified |
| The prompt fix comes next | Aishwarya's instruction: Phase 4 not started | OK — stated as next, not as done |

## Friction protected

- Kept: $0.32 is said as "at most thirty-two cents" because the harness records no token usage. The actual charge is lower and wasn't measured.
- Kept: B03 states that every gold label is defensive, so this test set can't measure posture agreement well. Without that caveat, "leans offensive" would sound better supported than it is.
- Kept: "leaning broad/offensive" is framed as a direction in the disagreements (11 predictions), not as a collapse. The collapse check didn't fire.
- Kept: the disagreement is shown as a difference in reading (functional wording vs named parts), not as the classifier simply being wrong. The labels are one person's judgment.
- Kept: "three claims kept failing" rather than "three claims refused". The refusal was confirmed directly for claim 1 and recorded for claim 7. Claim 5 failed the same way on the same patent but wasn't tested on its own.
- Kept: the refusal is not explained. The video says it happened and how the code now handles it, with no guess about why the grinding patent triggered it.
- Kept: the prompt fix is named as next work only. No Phase 4 result is shown or implied.

VERDICT: PASS
