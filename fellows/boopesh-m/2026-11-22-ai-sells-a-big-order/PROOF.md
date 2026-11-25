# PROOF — honest 12-point self-review (0–2 each)

| Criterion | Score | Why |
|---|---|---|
| Explicit framework | 2 | One framework, named on screen and in the narration: impact (sell fast) versus risk (sell slow). The cost + risk penalty is the objective both the agent and the closed form minimise |
| Reusable rubric | 1 | The three-row test (average cost · spread · bad day) on held-out days works for any execution strategy. It is shown, not spelled out as a checklist |
| Worked example | 2 | 10,000 shares at $50 over 10 steps, worked end to end: $49.50 / $5,000 / 100 bps for the dump, then TWAP, then the agent, all from the code |
| Falsifiability / edge | 1 | Held-out days with their own seed, comparison against an independent closed form, the training noise reported in FACTCHECK, and the limitation said aloud (synthetic market). There is no real-data test, and the paper that tested this on real data was not readable |
| Active task | 2 | B80 asks for a prediction before running the code (doubling impact makes the schedule faster or slower?). The answer can be checked against the formula (it gets flatter) |
| Friction | 1 | FRICTIONAL.md logs the blocked approval record, the blocked papers and the Q-learning failures. The video itself does not show a failure |
| **Total** | **9 / 12** | |
