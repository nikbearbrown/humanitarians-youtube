# Frictional Log

## 2026-11-15: Project week 2

- **Work and expectation:** train a PPO agent on the environment and beat "same time yesterday" at equal cost. I expected a learned policy to find extra gains on top of a simple rule.
- **What I tried:** plain PPO trained from scratch, then longer (2M, then 10M steps); then residual PPO, which starts at the rule and learns only a correction of -5 to +5 servers. 30 runs on Modal CPUs: 2 kinds, 5 late penalties, 3 seeds.
- **Where it resisted:**
  - In the first batch, late penalties below about 1/600 made a late request cheaper than a server, so the agents learned to run almost no servers. The penalties moved to 0.01 to 1.0.
  - Training longer barely changed plain PPO. Residual PPO did better than the rule on its training days (checked for one seed), but on held-out apps the best agent only ties it.
  - I questioned whether "same time yesterday" holds across a week, with quiet days followed by a busier one. The 14-day trace has that shape: days 6-7 and 13-14 are the quietest and day 8 is the busiest. "Same time yesterday" plans that busy day from a quiet one, and two weeks hold only one such day per app, too few to test.
- **AI and other contributions:** Claude Code wrote the training code, the Modal script, the chart and the video under my direction; I chose the two agent kinds and the sweep, raised the weekly pattern, and reviewed the results. Narration is an AI voice (Kokoro `af_bella`).
- **What I understand now:** a learned agent is not better by default; it has to be tested at equal cost on data it never saw. Before more PPO work, the test data has to cover the patterns a real service has, including the week, so the next step is traces several weeks long and a "same time last week" baseline.
- **Evidence:** [README](README.md#watch-and-review), [FACTCHECK.md](FACTCHECK.md), [rl-autoscaler 35e922d](https://github.com/lakshdhamija/rl-autoscaler/commit/35e922d)
