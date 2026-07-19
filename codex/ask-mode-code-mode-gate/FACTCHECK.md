# FACTCHECK — ask-mode-code-mode-gate

## Claims Table

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B00 | Gate moves cheap work upstream of expensive work; math favorable when one caught assumption saves one rollback | ✓ | Ch05: "The gate moves cheap work upstream of expensive work." Verbatim. | — |
| B01 | Ask Mode gate cost: time to interrogate plan; return: assumptions caught before Code Mode cheaper than rollbacks after | ✓ | Ch05: "assumptions caught before Code Mode runs are cheaper than rollbacks after it runs." Verbatim. | — |
| B01 | Gate is overhead for trivial one-line fixes; not overhead for consequential changes | ✓ | Ch05: "The gate is overhead for trivial one-line fixes. It is not overhead for consequential changes." Verbatim. | — |
| B04 | No-gate path: 3 correction cycles, 1 rollback, 25 minutes | Illustrative | Synthetic scenario illustrating the no-gate failure pattern from Ch05. | Marked synthetic. |
| B04 | Gate path surfaced wrong assumption (username vs email); fixing took 2 min; Code Mode ran once; total 12 min | Illustrative | Synthetic scenario illustrating the gate benefit. Wrong-assumption pattern consistent with Ch05 examples. | Marked synthetic. |
| B04 | Gate cost 2 minutes and prevented 13 | Illustrative | Synthetic calculation from the illustrative scenario. | Marked synthetic. |
| B06 | One-line fix: gate 3 min, no-gate 1 min; gate is overhead for trivial changes | Illustrative | Illustrates Ch05's guidance on when NOT to use the gate. | Marked synthetic. |
| B07 | Gate value proportional to cost of being wrong | ✓ | Ch05: "The gate's value is proportional to the cost of being wrong." Verbatim. | — |

## Illustrative Scenarios
- B04: No-gate vs gate comparison (25min/3cycles vs 12min/0cycles) — SYNTHETIC. Illustrates Ch05's mechanism with specific invented numbers.
- B06: One-line constant fix comparison — SYNTHETIC. Illustrates Ch05's calibration guidance.
- All code outputs are synthetic demonstrations.
