# FACTCHECK — Short

Every claim in the Short is a subset of the 16:9 film's claims. Full table, sources and math
checks: `../FACTCHECK.md`. Numbers come from `../code/results.json` and are asserted in `../make_sheet.py`.

| Beat | Claim | Verdict | Evidence |
|---|---|---|---|
| B00 | "this is an AI voice reading my script" | ✓ | Kokoro am_onyx |
| B20 | all at once costs 100 bps in the synthetic market; $50.00 → $49.50 | ✓ code | strategies.dump |
| B20 | equal slices: the price can drift while you wait | ✓ code | sample_days fan; twap std 33.7 bps |
| B30 | 40M practice runs; sells more early then tapers, close to the Almgren & Chriss formula | ✓ code | params.episodes; rl schedule; gap +1.68% |
| B40 | 20,000 new days, about 13 bps average, bad days lower than equal slices (54 vs 65) | ✓ code | rl mean 13.31, p95 53.59; twap p95 65.37 |
| B50 | synthetic market, not a real one | ✓ | the model in code/execution_rl.py |
| B90 | "Data: synthetic market" | ✓ | — |
