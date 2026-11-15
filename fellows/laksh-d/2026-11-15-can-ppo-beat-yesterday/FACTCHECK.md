# FACTCHECK: Can PPO Beat Yesterday?

Source of truth: lakshdhamija/rl-autoscaler @ 35e922d (local clone ~/code/rl-autoscaler), its `results/ppo/*.json`
(30 runs), and the runs recorded in `evidence/` (`evidence.json`, `pytest_stdout.txt`). Checked 2026-11-15.

| Claim (beat) | Verdict | Source / derivation | Fix |
|---|---|---|---|
| Previously: on 5 unseen apps, same time yesterday cut late requests from 5.47% (Kubernetes rule) to 1.17% (B02, B08) | ✓ | `evidence.json` curves at the 70% target (`train.score`, test_apps) | spoken "five and a half percent", "just over one percent" |
| PPO agents trained with Stable-Baselines3 (B03) | ✓ | `train.py` `stable_baselines3.PPO("MlpPolicy", ...)` | |
| Each minute the agent sees recent traffic, yesterday's traffic and its servers; 25 numbers (B03) | ✓ | `env.py` `_obs()`: last 10 minutes, yesterday's next 10, running, booting, queue, time of day | |
| Adds or removes up to 5 servers (B03) | ✓ | `max_step = 5`, `Discrete(11)` | |
| Reward = minus server cost, minus a penalty per late request (B03) | ✓ | `env.py` `reward = -(cost + c.late_penalty * late)` | |
| Plain PPO learns from nothing, 10M steps (B04) | ✓ | `modal_train.py` `STEPS["plain"] = 10_000_000`; `evidence.json` steps | |
| Residual PPO starts from the same time yesterday rule and learns a correction (B04) | ✓ | `train.py` `Residual`: rule action plus an adjustment of -5..+5; output bias set so the agent starts at the rule; 3M steps | |
| 30 agents on Modal: 2 kinds, 5 late penalties, 3 seeds (B00, B04) | ✓ | `modal_train.py` PENALTIES (0.01, 0.03, 0.1, 0.3, 1.0), SEEDS (0, 1, 2); 30 result files; `make_evidence.py` asserts 30 runs x 3 seeds | |
| Each method is a curve of cost against late requests on the 5 unseen apps (B05) | ✓ | rules at targets 40-80%; PPO = mean of 3 seeds per penalty (`evidence.json` curves, ppo) | |
| Points above 6% late are not shown (B05, on screen) | ✓ | plain 0.01/0.03, residual 0.01/0.03, Kubernetes at 80% are above 6% | stated on screen |
| No agent beats same time yesterday; the best, residual at the highest penalty, only ties it (B00, B01, B05, B08) | ✓ | best: 28,826 server-min/day, 0.52% late (seeds 0.41-0.67%). The rule's curve at that cost is about 0.56% (between 28,218/0.59% and 32,885/0.34%). The gap is smaller than the seed spread, so it is a tie, not a win. Every other PPO point is above the rule's curve | |
| Days 6, 7, 13 and 14 are the quietest and day 8 the busiest (B06, B08) | ✓ | median over the 19 apps of each day's total divided by the app's 14-day mean (`evidence.json` weekly; `make_evidence.py` asserts the days) | |
| The quiet pairs are weekends (B06 "weekly shape") | inferred | the two pairs are 7 days apart; the repo does not record the trace's weekdays | screen says "weekly shape", not "weekends" |
| On day 8, same time yesterday plans from a quiet day (B06) | ✓ | `SeasonalPolicy` reads the load 1,440 minutes earlier: day 7 | |
| Two weeks give each app only one such day (B07) | ✓ | day 8 is the only day after a quiet pair that has a yesterday | |
| B07 four-week calendar | illustration | the 7-day pattern of the 14 days repeated to 28 days; not data | |
| Next: weeks-long traces, a same time last week rule, rules first, then PPO (B07, B08) | ✓ | README Plan, weeks of 16 and 23 Nov | plan, not a result |
| AI disclosure (B00) | ✓ | narration is Kokoro af_bella; project is Laksh's, built with help from Claude Code | |
