# Carry-Out Law

## The Carry-Out Line
> "The failure that costs you is the one that does not stop the pipeline."

## Wrong Guess Defeated
The naive assumption that if an automated AI pipeline runs end-to-end without throwing an exception, parses all schemas, and exits with code zero, it is working correctly.

## The Distinction That Matters
- **Loud vs Silent Failures**: A pipeline missing engineering contracts (items 1–4: task, inputs, outputs, tools) crashes immediately. The failure is loud and halts execution. A pipeline missing supervisory additions (items 5–8: plausibility check, failure routing, audit trail, sign-off) runs cleanly. The failure is silent, letting fluently hallucinated or hazardous outputs sail through every green checkmark.
- **Contract vs Partition**: Delegation is not dividing labor between machine and human; it is an explicit contract with testable handoff conditions and accountable human sign-off.
