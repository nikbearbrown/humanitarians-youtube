# FACTCHECK — six-component-spec

## Claims Table

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B01 | Every vague Claude prompt has six missing components | ✓ | Chapter 03: six-component specification framework described throughout | — |
| B01 | A two-minute specification rewrite turns three wrong drafts into one right artifact | Illustrative | Chapter 03 framing: specification reduces iteration cycles | None needed |
| B03 | Constraints are negative — what Claude must not do — and distinct from the task | ✓ | Chapter 03: "constraints (what it must not do)" — verbatim distinction | — |
| B03 | Evaluation criteria must be measurable — 'good' is not acceptable | ✓ | Chapter 03: evaluation criteria described as measurable, not vague | — |
| B07 | Prompting as specification is about making evaluation criteria legible before the artifact is produced | ✓ | Chapter 03: core thesis — specification makes supervision possible | — |
| B07 | The criteria you cannot write are the ones you cannot supervise | ✓ | Chapter 03: near-verbatim key insight | — |

## Terms Table
| Term | Debut beat | Prior beat |
|---|---|---|
| six-component specification | B01 | none — introduced as hook |
| evaluation criteria | B03 | B01 established the six components |
| diagnosis mode | B05 | B03 showed the six components in code |

## Exclusion Confirmation
- NO XML prompt structures for Claude's API: PASS
- NO system-prompt engineering for production deployments: PASS

## Illustrative Examples
- B04: grant-report example — from ch.03 worked examples
- B06: literature-review diagnosis — ILLUSTRATIVE failure case
