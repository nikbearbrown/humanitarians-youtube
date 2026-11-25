# SHOTLIST — Hedging When Trading Isn't Free (16:9, 3840×2160)

| Beat | Lane | Visual |
|---|---|---|
| B00 | Remotion `ClaudeComposerAsk` | "Hi, Boopesh" composer; question about the paper answered with three lines; folder chip @HumanitariansAI |
| B10 | Remotion `BrutalistHesitantWriter` | "Black–Scholes tells you exactly how to hedge." corrected to "…how to hedge, if trading is free" |
| B20 | Manim `B20_Basics` | sell call → hold Δ shares; typeset Δ = N(d₁) with plain words (no d₁ fraction, per Boopesh's simplicity note); Δ-vs-price curve computed from the formula; "rebalance every day" card |
| B30 | Manim `B30_Cost` | 30 bars of average daily BS turnover (from arrays.npz); stat cards 2.23 shares · $1.11 fees · $2.75 price; "fees eat 40%" |
| B40 | Manim `B40_Move` | state → small network → new position; plain card "score = option money + hedge gains − fees" + typeset entropic utility (the only other formula) |
| B50 | Manim `B50_Results` | overlaid P&L histograms (BS grey, deep teal), 40,000 test paths; stats table, utility row highlighted |
| B60 | Manim `B60_Learned` | one test path: price, then BS vs deep positions as step lines; turnover and fee bars |
| B70 | Manim `B70_Limits` | γ = 0 sanity card (utilities, position gap) + limits list |
| B80 | Remotion `ClaudeComposerAsk` | "Your turn." composer with the prompt |
| B90 | Manim `B90_Outro` | title, SUBSCRIBE + HAI mark + @HumanitariansAI; credit Boopesh M. · Fellow · Brutalist team; paper; AI narration |

Every chart is drawn from `code/arrays.npz` / `code/results.json`; no hand-entered numbers in scenes.
