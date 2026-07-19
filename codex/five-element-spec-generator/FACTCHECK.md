# FACTCHECK — five-element-spec-generator

## Claims Table

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B01 | 'Add user authentication' is an invitation for Codex to make decisions you didn't know you were delegating | ✓ | Ch09: "A weak request — 'Add user authentication' — is an invitation for Codex to make decisions you didn't know you were delegating." Verbatim. | — |
| B01 | Five-element spec: specific task, invariants, context, output format, negative constraints | ✓ | Ch09: The five elements are named and defined. Verbatim. | — |
| B04 | Weak request touches 7 files, introduces flask-login, creates global session object | Illustrative | Synthetic Flask example illustrating the weak-request failure mode from Ch09. | Marked synthetic. |
| B04 | Five-element spec: Codex touches 2 files, no new dependencies, session in existing User model | Illustrative | Synthetic result illustrating how the spec constrains Codex output. | Marked synthetic. |
| B06 | Without negative constraints, Codex introduces a global session variable | Illustrative | Illustrates the mechanism from Ch09: "Negative constraints are the most load-bearing element for any task with dangerous defaults." | Marked synthetic. |
| B07 | Without Specific task, Codex picks its own scope; without Invariants, modifies whatever it wants | ✓ | Ch09: "Without Specific task, Codex picks its own scope. Without Invariants, it modifies whatever it wants." Verbatim in spirit. | — |

## Illustrative Scenarios
- B04: Flask authentication comparison (7 files vs 2 files) — SYNTHETIC. Illustrates Ch09's spec-vs-weak-request contrast.
- B06: Global session variable appearing when negative constraints removed — SYNTHETIC. Mechanism is consistent with Ch09's explanation of dangerous defaults.
- All code outputs are synthetic demonstrations.
