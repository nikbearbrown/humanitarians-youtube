# FACTCHECK: When History Misleads

Source of truth: lakshdhamija/rl-autoscaler @ a886c1b (clean checkout), its `results/stress-hpa.json`,
`results/ppo-hpa/*.json`, processed Azure trace, and `evidence/make_evidence.py`, which asserts every number below
against the values the script was written for and stops on any difference. Keys refer to `evidence/evidence.json`.
Checked 2026-11-22. `pytest -q`: 21 passed (`evidence/pytest_stdout.txt`).

| Claim (beat) | Verdict | Evidence key / derivation |
|---|---|---|
| Narration is an AI voice; the project is Laksh's, built with help from Claude Code (B00) | ✓ | Kokoro af_bella; metadata.ai_disclosure |
| Composer results: normal training beats HPA in 208 of 360; misleading-history training 273 of 360; worst case 93% more late, now 64% (B00) | ✓ | `stress.normal.better`, `stress.misleading.better`, `stress.*.worst_pct` |
| An autoscaler that plans from yesterday can be fooled when yesterday was unusual (B01) | ✓ | normal-trained agent loses to HPA in 152 of the 360 changed-history cases (`stress.normal`) |
| HPA runs enough servers that each works near a target load (B02) | ✓ | `policies.py` ThresholdPolicy: desired = ceil(load / (capacity x target)), as Kubernetes documents it |
| The agent is reinforcement learning (RL), trained with Proximal Policy Optimization (PPO), and sets HPA's target every minute, 40% to 90% (B02) | ✓ | `train.py` Headroom + HEADROOM_TARGETS; `observation.targets_pct` |
| Server row: servers HPA runs for 6,000 requests a minute at each target (B02) | ✓ illustrative | load 6,000 is an illustration; servers = ceil(6000 / (600 x target)) with `observation.capacity_per_server` = 600 |
| Each minute it sees 35 numbers: last 10 minutes, yesterday's next 10, last week's next 10, 5 more (servers running, booting, queue, time of day as two numbers) (B02) | ✓ | `observation.size`, `observation.groups`; `env.py` _obs with the WEEKLY config |
| Those slices are its only view of the past (B02) | ✓ | PPO "MlpPolicy" (no recurrent state); the observation is its only input |
| Bars in the cells are real loads at minute 235 of the example day (B02) | ✓ | `example.today` / `yesterday` / `last_week` |
| One real day: yesterday's burst came at the same minute (B03) | ✓ | `example` = Azure app ec941895, day 12 (an unseen test day); burst at minute 240 on both days (asserted); whole-day correlation 0.88 |
| New servers take three minutes to boot (B03) | ✓ | `observation.boot_minutes` (ClusterConfig.boot_delay) |
| Holiday x0.2, launch x3, metrics outage 0 (B03) | ✓ | `stress.py` SCENARIOS; the changed lines are drawn with stress.py's own Change (asserted equal) |
| x3 burst: 68k, off the chart (B03) | ✓ | 3 x max(`example.yesterday`) = 3 x 22,514 = 67,542 |
| HPA reads no history: only the current load (B03) | ✓ with note | ThresholdPolicy reads env.history[-1]. A changed last week never reaches HPA (asserted: identical HPA results); a changed yesterday reaches it only at midnight, because the day starts with servers sized for yesterday's last minute (stress.py docstring). HPA is measured under the same change |
| 360 cases = 6 changes x 4 test sets x 15 trained runs, each against HPA at the same cost (B04) | ✓ | `stress.*.cases` = 360, `runs` = 15; `frontier.py` rule_late_at (linear between HPA targets); every PPO cost is inside HPA's cost range (asserted) |
| Normal training: 208 of 360 better (58%); per change 37, 37, 32, 32, 48, 22 of 60 (B04) | ✓ | `stress.normal.better`, `pct`, `per_change`, `grid` (one square per case) |
| At worst, 93% more late requests (B04) | ✓ | `stress.normal.worst_pct_exact` = 93.04 (`worst_case`: yesterday x0.2, Azure held-out apps) |
| In 30% of training episodes, yesterday or last week is scaled at random, 0.1x to 5x, or set to zero (B05) | ✓ | `train.py` real_traffic; model json `bad_days` = 0.3; mirror of the draw checked against the real function on 3,000 draws (`training.checked_share` = 0.296) |
| Cards: 3 of 10 example episodes changed, yesterday x0.14, last week x1.31, yesterday x3.27 (B05) | ✓ example | `training.cards`: first seed (2) whose 10 draws change exactly 3 with both days; labelled as examples |
| 40 example factors (B05) | ✓ example | `training.dots`: the first 40 changed draws of seed 0 |
| This is domain randomization (B05) | ✓ | `train.py` real_traffic docstring; term from Tobin et al. 2017 (SOURCES.md) |
| Misleading-history training: 273 of 360 (76%), was 208; worst case +64%, was +93% (B06) | ✓ | `stress.misleading.better`, `pct`, `worst_pct_exact` = 64.03 |
| Normal history: 55 of 60 runs beat HPA, against 53 (B06) | ✓ | `stress.misleading.normal`, `stress.normal.normal` |
| Tests use the same kinds of change as training, at other sizes (B07) | ✓ | stress.py x0.2, x3, x0 all lie inside real_traffic's x0.1 to x5, or 0; README Limits |
| Real irregular days, like a recorded outage in public web server logs, are the stronger test, and come next (B07) | plan | README Limits ("Real irregular days are the stronger test") and Plan (web server logs); the outage example is Laksh's stated next step, not a result |
| HPA is never fooled by history; the agent sometimes still is: worst case still +64% (B07) | ✓ | HPA reads no history (above); `stress.misleading`: 87 of 360 cases still worse than HPA, worst +64% |
| Verdict card lines (B08) | ✓ | the keys above |

No week numbers, no anecdotes, no em dashes in narration or on-screen text (checked by `grep` over beat_sheet.json and scenes.py).
