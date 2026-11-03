# Sources

## Primary source — Adwait Changan, Mycroft Finance Investigator (this week)

Project root: `/Users/adwaitchangan/Study/Latest Mycroft/mycroft/projects/Mycroft-Finance-Investigator`

On-screen code and artifacts are trimmed verbatim from:
- `mycroft_finance_investigator/evaluation.py` — `run_evaluation()` isolated temp-copy harness
  (`tempfile.TemporaryDirectory`, `shutil.copytree`, `_apply_mutation`, `_matches`) (B04);
  the four defect mutations in `_apply_mutation()` (B06)
- `evaluations/cases.json` — the 7 explicit cases + expectations (baseline, 4 defects, step-limit, self-approval)
- `schemas/evaluation-cases.schema.json` — case contract
- `mycroft_finance_investigator/cli.py` — the `evaluate` subcommand (B09)
- `tests/test_evaluation.py` — the 5 evaluation tests this week

## The 7 evaluation cases (from cases.json)
| id | stage | operation | expected |
|---|---|---|---|
| baseline-investigation-completes | investigation | baseline | COMPLETED_PENDING_HUMAN_REVIEW · ebitda −120000.00 · 7 steps · 41 evidence · gate OPEN |
| reject-ledger-mismatch | validation | ledger_mismatch | REJECTED · "actuals do not reconcile to ledger" |
| reject-unmapped-account | validation | unmapped_account | REJECTED · "unmapped accounts" |
| reject-customer-revenue-mismatch | validation | customer_revenue_mismatch | REJECTED · "customer revenue drivers do not reconcile" |
| reject-headcount-payroll-mismatch | validation | headcount_payroll_mismatch | REJECTED · "headcount cost drivers do not reconcile" |
| enforce-investigation-step-limit | investigation | step_limit | REJECTED · "exceeded the configured 1 step limit" |
| reject-agent-self-approval | review | agent_self_approval | REJECTED · "cannot clear a human gate" |

## Reported figures (this week)
- 7 of 7 expectations matched (4 defects rejected, 2 behaviors rejected, 1 baseline matched).
- Valid baseline reproduces: −$120,000 EBITDA variance, 7 tool steps, 41 evidence references, OPEN human gate.
- Project suite: **24 passing tests** this week (finance 4 + review 7 + evaluation 5 + others 8).

## Provenance rule
Deterministic synthetic adversarial evaluation — no external LLM. `evaluation.py` states in its
own scorecard: "These are deterministic synthetic control checks, not a model-confidence score or
production certification," and marks adequacy `PENDING_HUMAN_REVIEW`. A pass verifies **only these
committed synthetic cases** — not model confidence, production certification, or human adequacy approval.

## Credits
Fellow/builder/narrator-of-record: **Adwait Changan** · Voice: Kokoro `am_onyx` ("Onyx, in for
Humanitarians AI") · Channel: **@HumanitariansAI**
