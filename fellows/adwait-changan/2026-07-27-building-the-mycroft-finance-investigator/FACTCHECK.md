# Fact-check gate

Status: **CLEARED FOR FINAL** — metrics confirmed by the fellow against the stored sample
run on 2026-07-27; real `finance.py` excerpt substituted into B05.

| Beat(s) | Claim | Verdict | Evidence |
|---|---|---|---|
| B00, verdict | The agent explains the mathematical performance bridge and leaves business causation and final approval to a human finance reviewer. | SUPPORTED | Stated design boundary; carried as the spine + verdict. |
| B02 | Six synthetic CSV datasets: budgets, actuals, ledger transactions, customers, headcount, account mappings. | CONFIRMED | Fellow-confirmed. |
| B03 | 43 data rows across six synthetic datasets; failed rows never reach the engine. | CONFIRMED | "43 data rows across six synthetic CSV datasets." Wording set to "data rows," not "records." |
| B05 | Engine computes revenue/expense/payroll/EBITDA variances; materiality; control-total reconciliation; calculation-to-source tracing. | SUPPORTED | Real code shown: `finance.py:162` `ebitda_variance()` (revenue − costs; variance = actual − budget). |
| B06 | Budget EBITDA $350,000; Actual EBITDA $230,000; Variance −$120,000. | CONFIRMED | On screen as "Variance (actual − budget) −$120,000," matching the code's sign. |
| B07–B08 | Local, evidence-driven agent — **no external LLM** — conditional tool selection, evidence retention, execution trace, machine + human reports. | CONFIRMED | Narration explicitly says "no external model in the loop." |
| B09 | 7 investigator tool steps; 41 unique evidence references; 12 tests passing. | CONFIRMED | Fellow-confirmed against the stored run. |
| Verdict/outro | "Synthetic sample and a DRAFT Mycroft workflow; materiality, causal explanations, and distribution still require a named human finance reviewer." | REQUIRED DISCLOSURE | Added verbatim-in-spirit to BVDT narration + as an on-screen verdict line. |

## Corrections applied

- 2026-07-27 — "43 records" → "43 data rows across six synthetic datasets" (B03 narration, layer, caption).
- 2026-07-27 — Investigator described as "local, evidence-driven agent — no external model in the loop" (B00, B07, B08).
- 2026-07-27 — B05 code replaced with the real `finance.py:162 ebitda_variance()` excerpt.
- 2026-07-27 — B06 variance shown as −$120,000 (actual − budget), matching the code's sign.
- 2026-07-27 — Added the synthetic/DRAFT + human-reviewer disclosure to the verdict.
