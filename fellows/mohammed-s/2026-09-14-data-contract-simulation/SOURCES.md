# SOURCES — `data-contract-simulation`

Everything on screen traces to the repository, not to a claim about production.

## Primary source

`github.com/mdhussainshariff/Mycroft` → `Data_Quality_Agent/`, branch
`feature/metric-impact-simulation`, commit `4469968`.

| On screen | File |
|---|---|
| `amount_cents → amount`, `/100.0` backfill | `data-contract-agent/fixtures/migrations/0003_subscriptions_amount.py` |
| `amount_cents / 100.0 AS amount_usd` | `mock-analytics/models/staging/stg_subscriptions.sql` |
| `status IN ('active','trialing')` context | `mock-analytics/models/marts/fct_mrr.sql` |
| B03 code (`build_models`) | `data-contract-agent/contract_agent/simulate.py` |
| B06 code (two-pass + `_patch_map`) | `data-contract-agent/contract_agent/simulate.py` |
| 4 models fail as-is | `SimulationReport.as_is_failures`, measured |
| `fct_mrr` ×0.01 post-fix | `tests/test_simulate.py::test_scenario2_mrr_is_100x_low_after_the_mechanical_fix` |
| row count unchanged | `tests/test_simulate.py::test_scenario2_row_count_is_unchanged` |
| `transactions.amount_cents` untouched | `tests/test_simulate.py::test_scenario2_leaves_unrelated_marts_alone` |
| `108,176.33 → 1,081.76` | `Data_Quality_Agent/README.md`, Phase-1 seeded ground truth |

## Corrections applied during the build (DOUBLE-CHECK LAW)

1. **B07's `avg(monthly_amount_usd)` figure.** First draft carried a made-up
   average. Replaced with the value implied by the published pair
   (108,176.33 / 1,152 active+trialing subscriptions = 93.90), and the row count
   pinned to the same 1,152 so the three rows are mutually consistent.
2. **"Four models go red."** Early narration said "three". The measured
   `as_is_failures` for scenario 2 is four — `stg_subscriptions` fails and
   `fct_mrr`, `fct_revenue`, `dim_users` are blocked behind it. Corrected to four,
   and the B04 table lists all six models so the two that survive are visible.
3. **No model version numbers on screen** beyond the composer's own chip, per the
   DOUBLE-CHECK LAW's don't-date-the-video clause.

## Declared worked example

The dollar figures come from the project's deterministic seed, not a production
warehouse — captioned as such on every beat that carries a number. The claim the
reel actually makes is the **ratio**, which is invariant to the data and is
asserted in the test suite.
