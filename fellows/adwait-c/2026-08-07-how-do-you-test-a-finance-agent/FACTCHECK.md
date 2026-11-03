# Fact-check gate

Status: **CODE-BOUND** — every code excerpt is trimmed verbatim from the real Mycroft files;
cases, expectations, and figures are read from `evaluations/cases.json` and the fellow's project.

| Beat(s) | Claim | Verdict | Evidence |
|---|---|---|---|
| B04 | Harness makes an isolated temp copy per case, plants one defect, observes by stage, compares to expectation. | CONFIRMED | `evaluation.py run_evaluation()` (verbatim, trimmed). |
| B05 | Four reconciliation defects: actuals↔ledger, unmapped account, customer↔revenue, headcount↔payroll. | CONFIRMED | `ALLOWED_OPERATIONS` + `cases.json`. |
| B06 | The mutations are one-row/one-dollar edits (ledger −1; pop mapping row; customer +1; headcount +1). | CONFIRMED | `evaluation.py _apply_mutation()` (verbatim). |
| B07 | Two behavioral cases (step-limit exceeded; agent self-approval) REJECTED; baseline reproduces −$120,000, 7 steps, 41 evidence, gate OPEN. | CONFIRMED | `cases.json` expectations. |
| B09 | `evaluate` CLI → scorecard: 7/7 matched, classification SYNTHETIC_ADVERSARIAL_EVALUATION, PASS. Project suite 24 tests. | CONFIRMED | `cli.py evaluate` + `run_evaluation()` summary; suite total 24 this week. |
| B10 / BVDT | A pass verifies only these synthetic cases — not model confidence, production certification, or human adequacy approval (PENDING_HUMAN_REVIEW). | CONFIRMED | `evaluation.py` scorecard text + `adequacy` field, verbatim intent. |

Note: the live repo has grown beyond this week (a later week adds scenario tests, taking the suite
to 32); this report reflects **this week's** state (evaluation added; suite total 24).

## Corrections applied
- (none — code, cases, and figures verified before render.)
