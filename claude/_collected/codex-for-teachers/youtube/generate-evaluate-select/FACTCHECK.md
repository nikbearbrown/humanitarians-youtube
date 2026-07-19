# FACTCHECK — generate-evaluate-select
**Generate-Evaluate-Select with Claude: Three Responses, One Real Decision**
Source: `codex-for-teachers/chapters/07-best-of-n.md`

---

## Claims audit

| # | Beat | Claim | Verdict | Source / Note |
|---|------|-------|---------|---------------|
| 1 | B00 | One Claude response is a default; three responses are a choice | ✓ | Chapter thesis: generate-evaluate-select converts a single default output into a deliberate selection. |
| 2 | B01 | The same prompt, three separate sessions, produces three pedagogically different responses | ✓ | Chapter: variance across sessions is a feature, not a bug — it surfaces pedagogical differences that a single response conceals. |
| 3 | B01 | The selection judgment is the supervisory work — it cannot be delegated | ✓ | Chapter: selection and documented reasoning are the Interpretive Judgment (IJ) capacity — specifically named as non-delegatable. |
| 4 | B04 | Response C has an equity flag — "unconventional naming" may reflect non-English naming convention | ✓ | Chapter discusses equity-flagging as a component of the evaluation pass; non-standard naming conventions as a predictable false-positive category. |
| 5 | B04 | Selection: Response B. Reasoning logged: strength-first framing, 3 criteria, no equity issues | SYNTHETIC | Illustrative selection consistent with chapter guidance on evaluation criteria. The specific response characteristics (word counts, criteria counts) are synthetic examples. |
| 6 | B06 | When all three candidates share a framing problem, the problem is in the specification | ✓ | Chapter: generate-evaluate-select functions as a dangerous-middle detector — shared patterns across candidates indicate specification failure, not model variance. |
| 7 | B07 | The documented rationale is what makes the selection auditable | ✓ | Chapter: rationale documentation is required for the selection to function as a supervisory artifact rather than an arbitrary pick. |

---

## Exclusions confirmed
- No discussion of N > 3 candidates
- No discussion of rubric-weighted scoring
- No discussion of inter-rater reliability between teacher and Claude

## Synthetic scenarios
All candidate response characteristics (word counts, framing labels, equity flags) are illustrative examples consistent with the source chapter's evaluation framework. Not transcripts of actual Claude feedback sessions. Response characteristics are constructed to demonstrate the chapter's evaluation criteria.
