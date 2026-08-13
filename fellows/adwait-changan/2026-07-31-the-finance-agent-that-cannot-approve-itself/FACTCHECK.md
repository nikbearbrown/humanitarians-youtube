# Fact-check gate

Status: **CODE-BOUND** — every code excerpt is trimmed verbatim from the real Mycroft files;
figures are the fellow's confirmed Week-31 values.

| Beat(s) | Claim | Verdict | Evidence |
|---|---|---|---|
| B02 | 43 rows/6 datasets; Budget $350k, Actual $230k, Variance −$120k; 7 steps; 41 evidence. | CONFIRMED | Carried forward from Week 30 (fellow-confirmed). |
| B05 | The agent only opens a request: gate_status OPEN, bound to run_id + SHA-256, reviewer blank, "cannot approve itself" instruction. | CONFIRMED | `review.py build_review_request()` (verbatim, trimmed). |
| B06 | Four rules: bound to run; rejects agents + unknown evidence; APPROVE needs materiality + causal cause; append-only. | CONFIRMED | `review.py` (`AGENT_IDENTITIES`, APPROVE checks, `open("x")`). |
| B07 | `AGENT_IDENTITIES` + `reviewer_name.casefold() in AGENT_IDENTITIES` → ReviewError "cannot clear a human gate"; APPROVE requires APPROVE_DEMO/REPLACE + ≥1 evidence-backed explanation. | CONFIRMED | `review.py` lines shown verbatim. |
| B08 | Schema required fields + enums (decision APPROVE/REQUEST_CHANGES/BLOCK; materiality APPROVE_DEMO/REPLACE/REJECT; each causal_explanation cites ≥1 evidence). | CONFIRMED | `schemas/review-decision.schema.json`. |
| B10 | CLI: `review-request` → OPEN; `record-review` with agent identity → rejected; with a named human + evidence → CLEARED, append-only. | CONFIRMED | `cli.py` subcommands + `review.py` behavior. Illustrative invocation, real behavior. |
| B11 | 7 new review-control tests (named); 19 passing this week. | CONFIRMED | `tests/test_review.py` has exactly 7 review tests; 12 finance + 7 = 19 (Week-31 suite). |
| BVDT | Local deterministic, no external LLM in runtime; sample review request remains OPEN; nothing fabricated. | CONFIRMED | Stated design; the committed sample request is OPEN by construction. |

Note: the live repo has grown beyond Week 31 (later weeks add evaluation/scenario tests); this
report intentionally reflects the **Week-31** state (7 new review tests, 19 total).

## Corrections applied
- (none — code and figures verified before render.)
