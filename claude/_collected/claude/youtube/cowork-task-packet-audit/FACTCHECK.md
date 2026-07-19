# FACTCHECK — cowork-task-packet-audit

## Claims Table

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B01 | One wrong folder permission and a Cowork session reads three years of personnel files | ✓ | Chapter 05: opening scenario — full Documents folder, no forbidden actions listed | — |
| B01 | Task packet audit catches the permission error in sixty seconds | Illustrative | Chapter 05 framing: validator as quick pre-session check | None needed |
| B02 | Six dimensions: inputs_named, forbidden_explicit, irreversibles_gated, output_format, verification_steps, no_sensitive_data | ✓ | cli-ideas.md candidate 05: six dimensions verbatim | — |
| B04 | Bad packet correctly fails on: inputs not named, forbidden not explicit, irreversibles not gated | ✓ | Chapter 05: opening-scene example fails all three | — |
| B05 | Seventh dimension: stop conditions defined | ✓ | cli-ideas.md candidate 05: "add a seventh dimension — 'stop conditions defined'" | — |
| B07 | Task packet is the specification that makes supervision possible | ✓ | Chapter 05: near-verbatim framing | — |

## Terms Table
| Term | Debut beat | Prior beat |
|---|---|---|
| task packet | B01 | none — introduced as hook |
| forbidden actions | B02 | B01 established the packet concept |
| stop conditions | B05 | B02 showed the six dimensions |

## Exclusion Confirmation
- NO Cowork connector configuration: PASS
- NO MCP server setup: PASS
- NO computer-use sessions: PASS

## Illustrative Examples
- B04: bad packet → six fails — from ch.05 opening scenario
- B06: good packet → seven passes — from ch.05 correctly specified example
