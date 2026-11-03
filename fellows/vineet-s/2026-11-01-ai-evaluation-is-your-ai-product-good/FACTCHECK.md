# FACTCHECK — AI Evaluation: How Do You Know Your AI Product Is Good?

Scope: a general explainer. No source document, no statistics, no product or model names, no version numbers, no dated claims.
Method: author self-check of each claim against widely taught concepts. No external sources were consulted for this pass.

| Beat | Claim | Status |
|---|---|---|
| B00-B01 | A demo shows one good moment; evaluation measures how often a product is good and whether it stays good | Standard evaluation framing. VERIFIED (general knowledge) |
| B02 | Six tools: golden dataset, test cases, human evaluation, LLM-as-a-judge, regression testing, launch decision | Author's selection matching the brief; not an industry standard list. OK |
| B03 | Golden dataset of expert-agreed answers; test cases per behavior; edge cases; keep set fixed and private | Standard practice. VERIFIED (general knowledge) |
| B04 | Human reviewers score against a rubric; rubric agreement and multiple raters matter | Standard practice. VERIFIED (general knowledge) |
| B05 | LLM judges scale but have biases (for example favoring longer answers); calibrate against humans | Documented judge behavior; stated as an example. VERIFIED (general knowledge) |
| B06 | Re-run tests on prompt, model, data or retrieval changes; average gains can hide per-case regressions | Standard regression-testing practice. VERIFIED (general knowledge) |
| B07 | Four launch questions: beats current, no new critical failures, cost and speed fit, gradual rollout with rollback | Author's checklist reflecting common practice. OK |
| B08-B09 | Recap and viewer prompt | Restates the above. OK |

Corrections applied: none needed. Soft wording kept soft on purpose.
Limit: this is a self-check, not an independent review. A subject-matter reviewer has not signed it.
