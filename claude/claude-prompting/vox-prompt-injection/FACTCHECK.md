# FACTCHECK — vox-prompt-injection

## Claims Table

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B01 | AI agent received a task; output recommended vendor user never preferred; email draft in compose window | Illustrative | Derived from chapter 05 prompt injection framing. Concrete example constructed per spec. Labeled illustrative. | None needed |
| B05 | No architectural distinction between instructions from user and instructions in content — both are text in context window | ✓ | Chapter 05: "When Cowork reads documents, web pages, or email content, that content can contain hidden or misleading instructions that try to redirect what Cowork does." Mechanism consistent with VPI-Bench 2025/2026 citation. | — |
| B06 | Adversarial text in documents redirects agent because mechanism is identical to user instructions | ✓ | Chapter 05: prompt injection framing — "hidden or misleading instructions that try to redirect what Cowork does" | — |
| B08 | Research tracks agentic AI attacks via documents, web pages, emails; agent cannot verify source of instruction | ✓ | Chapter 05 cites AgentDojo and VPI-Bench 2025/2026 for prompt injection research | — |
| B09 | Mia asks agent to read vendor quotes; injected instruction in one quote redirects task | Illustrative | Constructed illustrative example per card spec. Based on chapter 05 vendor scenario framing. | None needed |
| B11 | Mitigation: limit trusted sources to files and connectors you control | ✓ | Chapter 05: "The mitigation is to limit trusted sources to files and connectors you control, and to inspect any output that involves reading external or untrusted content." — near-verbatim | — |

## Terms Table
| Term | Debut beat | Prior beat |
|---|---|---|
| context window | B05 | B04 established naive model is wrong; viewer wants mechanism |
| prompt injection | B06 | B05 established context window identity; viewer wants the named attack |
| review gate | B12 | B11 established scope mitigation; viewer wants operational form |

## Exclusion Confirmation
- NO formal prompt injection attack taxonomy: PASS (mechanism explained, taxonomy absent)
- NO cryptographic or sandboxing solutions: PASS (absent)
- NO SQL injection comparison beyond one spoken aside: PASS (absent entirely)
- NO extended VPI-Bench methodology: PASS (study cited by name only, no methodology)

## Illustrative Examples
- B01: vendor recommendation + email draft — ILLUSTRATIVE (constructed from chapter framing)
- B09: Mia/vendor quotes — ILLUSTRATIVE (from card spec)
