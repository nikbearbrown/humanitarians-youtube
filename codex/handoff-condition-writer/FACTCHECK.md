# FACTCHECK — handoff-condition-writer

## Claims Table

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B00 | Tests pass is not a handoff condition — it misses the three most common failures that tests never see | ✓ | Ch10: "'Tests pass' is not a handoff condition. It misses the three most common failures that tests never see." Verbatim. | — |
| B01 | Handoff condition must be specific, testable, and binary | ✓ | Ch10: The three properties — specific, testable, binary — are named and defined. Verbatim. | — |
| B01 | Dangerous middle: code that looks complete and is functionally broken | ✓ | Ch10: "The dangerous middle — code that looks complete and is functionally broken." Verbatim. | — |
| B04 | Authentication step condition with 4 elements; all pass specific/testable/binary rubric | Illustrative | Synthetic example illustrating the four-element condition structure from Ch10. | Marked synthetic. |
| B06 | Refactoring step: must-not becomes 'no method renamed without test rename' | Illustrative | Synthetic illustration of how the must-not adapts to step type. Consistent with Ch10's guidance on step-specific failure modes. | Marked synthetic. |
| B07 | Must-not element names the failure that slips through tests | ✓ | Ch10: "The must-not element is the most valuable: it names the failure that would slip through tests." Verbatim in spirit. | — |

## Illustrative Scenarios
- B04: Authentication step condition (auth.py, authenticate signature, pytest test_auth.py, no global session) — SYNTHETIC. Illustrates Ch10's four-element structure.
- B06: Refactoring condition with method-rename must-not — SYNTHETIC. Constructed to illustrate the step-adaptive nature of the must-not element.
- All code outputs are synthetic demonstrations.
