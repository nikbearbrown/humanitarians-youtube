# FACTCHECK — vox-bias-pipe

Source chapter: `06-bias-where-it-enters-and-who-is-responsible.md`

## Claim-by-claim audit

| Beat | Claim | Verdict | Source / Note |
|------|-------|---------|---------------|
| B02 | Team 1 rewrote the loss function → small reduction | ✓ | Ch.06: "The first team rewrote the loss function. They added a fairness penalty... The disparity dropped a little. Not enough." |
| B02 | Team 2 resampled the data → small reduction | ✓ | Ch.06: "Same problem. Three honest engineering efforts... Teams One and Two were not wrong. They produced real, small reductions." |
| B02 | Team 3 touched nothing in the model, cut disparity tenfold | ✓ | Ch.06 cold open: "A third team touched neither and cut it tenfold" (card hook verbatim) |
| B04 | Naive assumption: bias lives in the model | ✓ | Ch.06: "The temptation is to fix the thing closest to your hands." — model = closest to engineer's hands |
| B05 | Bias flows through 3 parallel paths: model, proxy, deployment context | ✓ | Ch.06: "from the protected attribute at the top to the outcome at the bottom, how many paths are there? Some paths run through the model. Some bypass the model — they run through the proxies into the deployment context directly." |
| B05 | Intervention only blocks the path it sits on | ✓ | Ch.06: "For each candidate intervention point, ask: which paths does this intervention block, and which paths does it leave open?" |
| B07 | Draw the full causal chain; block one, flow reroutes through others | ✓ | Ch.06 leverage analysis procedure verbatim; "blocking one without blocking the other leaves the bias carrying through" |
| B08 | "Most algorithmic interventions block one path — the one running through the model's parameters — and leave the proxy paths and the deployment-context paths fully open." | ✓ exact | Ch.06 verbatim |
| B09 | Team 1 blocked model path, flow rerouted through others, bias barely moved | ✓ | Ch.06: "When Team A intervened on the model, they blocked one path — the path running through the parameters. They left the proxy paths and the deployment-context paths fully open. This is why their fix had small effect." |
| B10 | Team 3 blocked deployment-context path (highest-flow), disparity fell sharply | ✓ | Ch.06: "Team C found the deployment-context path... Once they saw it, the intervention was almost forced. The reviewer's pattern was the high-leverage point. Block it, and most of the disparity goes with it." |
| B10 | "disparity fell ninety percent" (illustrative for "tenfold") | ✓ illustrative | Ch.06 says "cut it tenfold"; 90% = 1 - 1/10. Labeled as illustrative ✓ |
| B11 | "You can intervene on what is in your house. But your intervention will be at the wrong leverage point, and the disparity will persist." | ✓ exact | Ch.06 verbatim |
| B12 | Recap: "the model is never the only pipe; find the one carrying the most flow" | ✓ | Faithful summary of ch.06 leverage-analysis conclusion |

## Exclusion check
- Pearl do-calculus (Rung 1/2/3, do-notation): absent ✓
- Ten-mechanism taxonomy (selection, historical, implicit, etc.): absent ✓ (only "model path, proxy path, deployment context" — not named mechanism types)
- Fairness metrics (demographic parity, ECE, Brier): absent ✓
- Graph node count: 5 nodes used (Protected Attr, Model, Proxy, Deployment Context, Outcome) ≤6 ✓
- Three teams: each covered in 1 sentence within B02 ✓

## Terms table

| Term | Debuts | Need created by |
|------|--------|-----------------|
| leverage | B04 (THE PROBLEM) | B02 shows that two "correct" fixes barely moved the bias — viewer needs a word for the missing ingredient |
| parallel paths | B05 (THE PROBLEM) | B04 establishes "model isn't enough" → viewer needs to understand why |
| deployment context | B05 (THE PROBLEM) | Appears as the third path; need created by the three-path concept |
| leverage analysis | B07/B10 (THE MECHANISM) | B07 introduces the procedure; need fully established by B05 |

## Numbers
- "tenfold reduction" → illustrative 90% drop in B10: labeled as illustrative ✓
- "small reductions" for Teams 1&2: ch.06 says "a little, not enough" / "same problem" — no exact numbers given; my B02 says "small reductions" which is accurate ✓

## B12 — THE EXAMPLE beat (illustrative)

| Claim | Status |
|---|---|
| Lending model, 22-point approval gap | illustrative — made-up instance |
| Retrain without protected attributes → weight gap drops to 7 pts | illustrative |
| Zip code remains in features, carries 18 pts on its own path | illustrative |
| Final approval gap: 20 pts | illustrative |

All numbers in B12 are invented and illustrative. They demonstrate the mechanism (one pipe blocked, two open, flow reroutes) without claiming any specific real-world study.
