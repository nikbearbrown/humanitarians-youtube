# Fact-check gate

Status: **CODE-BOUND** — every code excerpt is trimmed verbatim from the real Mycroft files; the
three exercise results are read from `config/sample-scenarios.json` + `scenario.py` arithmetic.

| Beat(s) | Claim | Verdict | Evidence |
|---|---|---|---|
| B04 | Every scenario re-hashes the verified CSVs and refuses if any hash ≠ the run log. | CONFIRMED | `scenario.py _load_baseline()` (verbatim). |
| B05 | Two methods only; lineage preserved; duplicate category / non-finite / negative rejected. | CONFIRMED | `load_scenario_plan()` + `_scenario_result()` guards. |
| B06 | Deterministic: PERCENT scales the actual; AMOUNT adds; quantized to cent; negative → ScenarioError. | CONFIRMED | `_scenario_result()` (verbatim, trimmed). |
| B08 | Baseline $230,000 → +5% rev $275,500; −$20,000 COGS $250,000; balanced $252,300. | CONFIRMED | `sample-scenarios.json` assumptions + engine arithmetic (45,500 / 20,000 / 22,300 deltas). |
| B09 | Machine log + decision pack; every output stamped SIMULATION_NOT_FORECAST · Recommendation NONE · Decision HUMAN_REQUIRED · PENDING_HUMAN_REVIEW. | CONFIRMED | `run_scenarios()` + `write_scenario_artifacts()` (verbatim labels). |
| B10 / BVDT | Project suite reached 32 passing tests; no external LLM. | CONFIRMED | Suite total 32 this week (scenario suite = 8 new). |

## Corrections applied
- (none — code, plan, and figures verified before render.)
