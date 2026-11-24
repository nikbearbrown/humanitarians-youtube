# PROOF — plain-language self-review (12-point rubric)

_Drafted by Claude for Boopesh to confirm after watching._

| # | Rubric point | How this film does it | Honest grade |
|---|---|---|---|
| 1 | One clear question | "Can a learned hedge beat Black–Scholes once trades cost money?" (B10) | strong |
| 2 | Framework | Hedge = hold Δ shares (B20); cost = fee × shares traded (B30); learned policy + utility (B40) | strong |
| 3 | Reusable rubric | Compare hedges on average, spread, worst 5 %, and the trained utility — not one number (B50 table) | good |
| 4 | Worked example | Real run: 40,000 test paths, every chart from `arrays.npz` (B30, B50, B60) | strong |
| 5 | Math shown properly | Typeset Δ = N(d₁), objective, entropic utility; algebra + numeric check in FACTCHECK | good |
| 6 | Falsifiability / sanity | γ = 0 should give back Black–Scholes — it nearly does, and the film says it's slightly worse (B70) | good |
| 7 | Edge / limits | Toy BS world vs paper's S&P 500/Heston; simulator dependence; wider spread admitted (B50, B70) | good |
| 8 | Active task | B80 prompt: double the fee, retrain, report numbers | good |
| 9 | Friction recorded | FRICTIONAL.md: torch install failure, blocked paper, corrected "holds still" line | good |
| 10 | Sources | Code README (verified) vs abstract summaries (flagged ⚠️) kept apart | partial — paper PDF not read |
| 11 | Disclosure | AI voice disclosed in first sentence and outro | strong |
| 12 | Length / pacing | landscape 2:33, Short 0:51, both < 3 min | ok |

Weakest point: paper-specific claims (affiliations, S&P 500/Heston experiments) are from abstract summaries,
not the paper itself. The replication is a toy and does not reproduce any number from the paper.
