# FACTCHECK -- plan-first-scope-gate
Source chapter: `claude-agentic-ai/chapters/07-planning-before-acting.md`

## Claims audit
| Claim | Verdict | Source / note |
|---|---|---|
| Asking Claude to act without a plan causes immediate unrequested actions | SUPPORTED | Chapter 07 describes agents defaulting to action without explicit plan-first gates |
| A plan should include goal, inputs, excluded sources, tool sequence, permissions, stop conditions, verification evidence, approval gate | SUPPORTED | Chapter 07 lists planning elements for agentic tasks |
| Vague stop conditions ("if needed") are insufficient for safe agentic execution | SUPPORTED | Chapter 07 on stop conditions requiring concrete triggers |
| Three hours of undo vs two minutes of plan review | ILLUSTRATIVE | Adapted from ch.07 framing. Synthetic ratio to illustrate cost asymmetry. |
| Stop condition naming a concrete trigger is the key gate | SUPPORTED | Chapter 07 on halt conditions requiring specificity |

## Exclusions confirmed
- Multi-agent orchestration planning: not mentioned, single-agent task only
- LLM planning benchmark comparisons: not mentioned, no benchmark references

## Terms table
| Term | Debut beat | Prior beat creating the need |
|---|---|---|
| Plan-first gate | B01 | B01 establishes the stakes of acting without a plan |
| Stop condition | B04 | B03 CODE shows the 8-element checklist including stop_conditions |
| Approval gate | B02 | B01 establishes need for human approval before execution |
| Eight-element checklist | B02 | B01 shows cost of skipping structured planning |
