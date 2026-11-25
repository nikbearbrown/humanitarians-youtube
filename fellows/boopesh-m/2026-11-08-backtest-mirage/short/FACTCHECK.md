# FACTCHECK — The Backtest Mirage (Short, 9:16)

Same sources and evidence as [../FACTCHECK.md](../FACTCHECK.md) ([RUN] = `../code/backtest_mirage.py`, synthetic
noise data, seed 42; [PAPER] = Bailey et al. 2014, ⚠️ not read directly).

| Beat | Claim | Source | Status |
|---|---|---|---|
| B00 | results from my own experiment on synthetic noise data; best Sharpe 1.69 → −0.37 on new data | [RUN] | ✅ |
| B10 | a search tries rules on pure random noise, no real edge exists | [RUN] by construction | ✅ |
| B10 | best of 1: near zero; of 100: 1.1; of 10,000: 1.6 (median of 200 noise markets) | [RUN] −0.075 / 1.055 / 1.575 | ✅ (rounded) |
| B10 | "Sharpe 1, usually called good" (caption) | practitioner rule of thumb | opinion |
| B20 | the best of 10,000, tested on two years it never saw: Sharpe −0.4 (−0.37 on screen) | [RUN] −0.369 | ✅ |
| B20 | across 200 noise markets the winners average about zero (−0.02) | [RUN] −0.022 ± 0.052 | ✅ |
| B30 | count trials, hold out data, demand more as you test more | editorial fix (paper's trial-count point ⚠️ via summaries) | editorial |
| B30 | "otherwise you are just picking the luckiest coin" | editorial | opinion |
| B90 | "Paper: Bailey et al., 2014" | [PAPER] | ⚠️ not read directly |
