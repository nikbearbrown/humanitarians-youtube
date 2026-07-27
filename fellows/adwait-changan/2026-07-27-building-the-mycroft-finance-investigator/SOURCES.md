# Sources

## Primary source

- **Adwait Changan — the Mycroft Finance Investigator project** (fellow's own work,
  built over three weeks ending July 27, 2026).
- Project root: `/Users/adwaitchangan/Study/Latest Mycroft/mycroft/projects/Mycroft-Finance-Investigator`
- Finance engine excerpt shown in B05: `mycroft_finance_investigator/finance.py` — `ebitda_variance()` (line 162)
- Source artifacts backing every reported number:
  - six synthetic CSV datasets: budgets, actuals, ledger transactions, customers,
    headcount, account mappings (plus per-table schema, provenance, validation rules)
  - deterministic finance engine (revenue / expense / payroll / EBITDA variance,
    materiality rules, control-total reconciliation, calculation-to-source tracing)
  - local, evidence-driven investigation agent — **no external LLM in the loop**
    (conditional tool selection, evidence retention, execution trace, machine + human reports)
  - test suite output and the stored sample run's machine report

## Provenance rule

Narration is limited to results this fellow produced and can point to in the project
artifacts above, plus clearly labeled deductions. The report describes a **synthetic
sample** and a **DRAFT** Mycroft workflow; the verdict states plainly that materiality,
causal explanations, and distribution still require a named human finance reviewer.

## Reported results — CONFIRMED against the stored sample run (2026-07-27)

| Result | Confirmed value |
|---|---|
| Data rows | 43, across six synthetic CSV datasets |
| Datasets | 6 |
| Budget EBITDA | $350,000 |
| Actual EBITDA | $230,000 |
| Variance (actual − budget) | −$120,000 |
| Investigator tool steps | 7 |
| Unique evidence references | 41 |
| Tests passing | 12 |

## Credits

- Fellow / builder / narrator-of-record: **Adwait Changan**
- Presenter voice: Kokoro **`am_onyx`** ("Onyx, in for Humanitarians AI")
- Channel: **@HumanitariansAI**
