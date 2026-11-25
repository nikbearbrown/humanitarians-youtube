# PROOF — plain-language self-review (12-point rubric)

_Drafted by Claude for Boopesh to confirm after watching._

| # | Rubric point | How this film does it | Honest grade |
|---|---|---|---|
| 1 | One clear question | "Why does an AI that tests 10,000 trading strategies always find a brilliant one?" (B00, B10) | strong |
| 2 | Framework | noise market → search → unlock → repeat 200 times → why (noise ≈ 1/√years) → fix (B20–B70) | strong |
| 3 | Reusable rubric | count your trials, hold out data you never touch, demand more as you test more (B70) | strong |
| 4 | Worked example | real run: 10,000 rules on 5 + 2 years of noise; every chart from `results.json` / `curves.npz` | strong |
| 5 | Math shown properly | one typeset formula (Sharpe noise ≈ 1/√years = 0.45), checked against the measured spread 0.44 | good |
| 6 | Falsifiability / sanity | zero edge by construction, so any Sharpe is luck; best-of-N climbs 0.69 → 1.58 while the winners' out-of-sample average stays ≈ 0; the "45 tries → Sharpe ≈ 1" figure recomputed (0.99 theory, 0.91 my search) | strong |
| 7 | Edge / limits | synthetic noise, no trading costs, real markets may hide small real edges (B70); correlated rules (FACTCHECK) | good |
| 8 | Active task | B80 prompt: add a small real edge + trading costs and see if the search finds it | good |
| 9 | Friction recorded | FRICTIONAL.md: paper blocked, "turns down" → "stalls, then slips", one N value 2.7 s.e. above zero, writer fix | good |
| 10 | Sources | paper details only from search summaries (⚠️ marked); no quote used | partial |
| 11 | Disclosure | AI voice disclosed in the first sentence and on the outro; "synthetic noise data" on screen and spoken | strong |
| 12 | Length / pacing | landscape 2:24, Short 0:45, both < 3 min | ok |

Weakest point: the paper itself could not be opened from the build container, so its exact wording (including the
45-trials figure) rests on secondary summaries; the film's own numbers do not depend on it.
