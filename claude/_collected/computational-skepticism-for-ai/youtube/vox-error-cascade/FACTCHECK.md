# FACTCHECK — vox-error-cascade

Source: `computational-skepticism-for-ai/chapters/08-validating-agentic-ai-when-autonomous-systems-misbehave.md`

## Terms table

| Term | Definition used in video | Chapter reference |
|---|---|---|
| Cascading hallucination | Multi-agent failure mode where Agent A's wrong output is treated as ground truth by Agent B, compounding errors downstream | Line 335 |
| Single-agent validation | Testing each agent in isolation against clean inputs — does not catch interaction-pattern failures | Line 337, 343 |
| Interaction pattern | The flow of outputs between agents — the unit that must be validated in multi-agent systems | Line 343 |
| Conditioning | Each agent treats prior agent output as ground truth; this propagates rather than filters errors | Line 335 |
| 1% → 30% | Concrete example of cascading dynamics dominating over individual agent error rates | Line 335 |

## Claim-by-claim check

| Beat | Claim | Chapter support | Status |
|---|---|---|---|
| B02 | Three agents each validated at 1%; pipeline produces 30% failure | Line 335: "You validated each agent at one percent; the compound system fails at thirty." | PASS |
| B04 | Single-agent validation tests in isolation with clean inputs; pipeline agents receive prior agent output | Lines 335, 337 | PASS |
| B05 | Each agent treats prior output as ground truth, cannot detect upstream error; mechanism is conditioning not addition | Line 335: "Agent B conditions on it" | PASS |
| B07 | Cascading dynamic dominates; interaction pattern is the failure | Line 335: "error rate is dominated by cascading dynamics, not individual agents' error rates. The interaction pattern is the failure." | PASS |
| B08 | Quote verbatim | Line 335: exact | PASS |
| B09 | Fix: validate interaction patterns; which outputs flow into which inputs; monitor handoff quality | Line 343 | PASS |
| B10 | Quote verbatim | Line 343: exact | PASS |
| B11 | Individual validation is necessary but not sufficient; failure has no single-agent analog | Lines 333, 343 | PASS |

## B12 — THE EXAMPLE beat (illustrative)

| Claim | Status |
|---|---|
| Customer service pipeline: 3 agents (extract, fetch, draft) | illustrative — made-up instance |
| Agent 1 misreads order O-7821 as O-7281 (one-digit transposition) | illustrative |
| Agent 2 fetches the wrong customer record | illustrative |
| Agent 3 drafts a confident, detailed reply about the wrong order | illustrative |
| All three agents were individually cleared | illustrative |

All identifiers and scenario details in B12 are invented and illustrative. They demonstrate the cascading error mechanism (conditioning on wrong prior output) without claiming any specific company or system.

## VERDICT: PASS
