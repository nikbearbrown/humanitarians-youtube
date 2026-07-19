# FACTCHECK -- human-approval-gates
Source chapter: `claude-agentic-ai/chapters/07-planning-before-acting.md`

## Claims audit
| Claim | Verdict | Source / note |
|---|---|---|
| Gate placement should be designed before the workflow runs, not reactively | SUPPORTED | Chapter 07 on pre-task gate design as part of planning |
| Irreversible actions require gates placed before them | SUPPORTED | Chapter 07 on irreversibility as the primary gate trigger |
| Delete operations receive the highest gate tier regardless of position | SUPPORTED | Chapter 07 on irreversibility and blast radius determining gate tier |
| Four-step contract workflow: read, extract, write, email | ILLUSTRATIVE | Adapted from ch.07 worked example on approval gate design. Synthetic scenario. |
| Three gates prevent the four-hour undo | ILLUSTRATIVE | Adapted from ch.07 framing of gate placement cost asymmetry. Synthetic ratio. |

## Exclusions confirmed
- Formal human-in-the-loop system design: not mentioned, task-level gate design only
- NIST AI RMF full implementation: not mentioned, no NIST references
- Enterprise approval workflows: not mentioned, individual workflow scope only

## Terms table
| Term | Debut beat | Prior beat creating the need |
|---|---|---|
| Approval gate | B01 | B01 establishes gate placement as the design decision |
| Gate tier | B05 | B04 shows two-tier system (none vs BEFORE); B05 introduces highest-tier |
| Blast radius | B03 | B02 ASK names blast radius as a gate placement input |
| Irreversible action | B01 | B01 names irreversibility as the primary gate trigger |
