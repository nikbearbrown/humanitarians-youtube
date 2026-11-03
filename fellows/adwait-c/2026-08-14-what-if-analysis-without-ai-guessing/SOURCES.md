# Sources

## Primary source — Adwait Changan, Mycroft Finance Investigator (this week)

Project root: `/Users/adwaitchangan/Study/Latest Mycroft/mycroft/projects/Mycroft-Finance-Investigator`

On-screen code and artifacts are trimmed verbatim from:
- `mycroft_finance_investigator/scenario.py` — baseline hash verification in `_load_baseline()` (B04);
  deterministic arithmetic + negative-guard in `_scenario_result()` (B06); the contract in
  `load_scenario_plan()` (B05); the SIMULATION_NOT_FORECAST / Recommendation None / HUMAN_REQUIRED /
  PENDING_HUMAN_REVIEW labels in `run_scenarios()` + `write_scenario_artifacts()` (B09)
- `config/sample-scenarios.json` — the three exercises (B08)
- `schemas/scenario-plan.schema.json` — the plan contract
- `tests/test_scenario.py` — the 8 scenario tests this week

## The three exercises (from sample-scenarios.json; baseline actual EBITDA $230,000)
| Scenario | Assumptions | EBITDA | Δ from baseline |
|---|---|---:|---:|
| Revenue recovery exercise | revenue +5% (PERCENT_OF_ACTUAL) | $275,500 | +$45,500 |
| COGS reduction exercise | cogs −$20,000 (AMOUNT) | $250,000 | +$20,000 |
| Balanced operating exercise | revenue +3%, payroll +$10,000, opex −$5,000 | $252,300 | +$22,300 |

## Contract enforced by scenario.py
- Bound to the exact `baseline_run_id`; verified CSVs re-hashed and checked against the run log.
- Only `AMOUNT` or `PERCENT_OF_ACTUAL`; each assumption keeps `reasoning` + `source` (lineage).
- Rejects: unknown fields, duplicate category assumptions, non-finite values, category-goes-negative.
- Deterministic arithmetic (Decimal, quantized to the cent); **no external LLM**.
- Every output stamped: `SIMULATION_NOT_FORECAST`, `Recommendation: NONE`, `Decision: HUMAN_REQUIRED`,
  `Adequacy: PENDING_HUMAN_REVIEW`.

## Reported figure
Project suite: **32 passing tests** this week (finance 4 + review 7 + evaluation 5 + scenario 8 + others 8).

## Credits
Fellow/builder/narrator-of-record: **Adwait Changan** · Voice: Kokoro `am_onyx` ("Onyx, in for
Humanitarians AI") · Channel: **@HumanitariansAI**
