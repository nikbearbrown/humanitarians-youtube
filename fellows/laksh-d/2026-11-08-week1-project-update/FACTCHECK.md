# FACTCHECK: Why Autoscalers Need Yesterday's Traffic

Source of truth: lakshdhamija/rl-autoscaler @ 8b126bd, and the
runs recorded in `evidence/` (`demo_stdout.txt`, `pytest_stdout.txt`, `evidence.json`). Checked 2026-11-08.

| Claim (beat) | Verdict | Source / derivation | Fix |
|---|---|---|---|
| A new server takes minutes to boot; 3 minutes in the simulator (B01, B04, B08) | ✓ | `env.py` ClusterConfig `boot_delay = 3` | |
| The Kubernetes rule only adds servers after the load arrives (B04) | ✓ | `policies.py` ThresholdPolicy (HPA rule: 70% target, 10% tolerance, 5-min scale-down window) reacts to `env.history[-1]`, the last observed minute | |
| Gymnasium environment, one step is one minute (B02) | ✓ | `env.py` `AutoscaleEnv(gym.Env)`, docstring "One step is one simulated minute" | |
| The agent adds or removes servers (up to 5 per minute) (B02, B07) | ✓ | `max_step = 5`, `Discrete(11)` action space | |
| Pays for every server, including booting ones (B02 "billed") | ✓ | `cost = server_cost * (running + len(booting))` | |
| Loses points for every late request (B02) | ✓ | `reward = -(cost + c.late_penalty * late)` (shown verbatim on screen) | |
| B02 per-minute values (servers, countdowns, requests, capacity, late) | ✓ | real `AutoscaleEnv` run of ThresholdPolicy on held-out app 8c2b9304 day 10, minutes 898-913 (`evidence.json` burst.*). Requests are the env's input, scaled to the 50-server cluster by `data.scale()` | |
| 13 tests pass (B00) | ✓ | `evidence/pytest_stdout.txt`: "13 passed" | |
| 19 web apps from Microsoft's public Azure Functions trace, 14 days each (B00, B03) | ✓ | `data/azure2019_http_apps.json` (14 train + 5 test apps; 14 days) | |
| 14 apps train, 5 stay hidden; days 11-14 unseen (B03) | ✓ | same file: `train_days [1,10]`, `test_days [11,14]`, `test_apps` x5 | |
| 72% of bursts reach their peak in the first minute (B04, B08) | ✓ | `demo_stdout.txt` "real (training days) ... 72%"; `evidence.json` peak_dist[0] = 0.718 over 3,351 training bursts | |
| Histogram of minutes to peak (B04 bars 1-4+) | ✓ data, unlabelled | `evidence.json` peak_dist (training days, `find_bursts`) | numbers other than 72% are not stated |
| Many bursts come back at the same time the next day (B05) | minor | repo metric is "another day, within 5 minutes" (`traffic.repeat_share`); the B05 example is literally the next day: the same held-out app had its burst at minute 905 yesterday too (`evidence.json` burst.yesterday) | wording kept from the narration brief |
| The agent sees what traffic did at this time yesterday (B05) | ✓ | `_obs()`: yesterday's load for the next 10 minutes (`yesterday_window = 10`) | |
| 5 held-out apps, 65 unseen days (B00, B06) | ✓ | `demo_stdout.txt` "real, unseen apps (5 held-out apps): 65 days" | |
| Threshold 19,986 server-min/day, 5.47% late; same time yesterday 24,488, 1.17% (B06, B07, B08) | ✓ | `demo_stdout.txt` | |
| Linear forecast 22,858, 4.63%; fixed for the peak 39,445, 0.07% (B06) | ✓ | `demo_stdout.txt` | |
| Threshold at 50% target 27,371, 3.10%: spends more and is still worse (B06) | ✓ | `demo_stdout.txt` "cost against late requests, real, unseen apps" | |
| "five and a half percent to just over one percent" (B06) | ✓ | 5.47% and 1.17% | spoken rounding |
| "cut waiting requests by more than half" (B08) | ✓ | 1.17 / 5.47 = 0.21, a 79% cut | |
| Next week: PPO with Stable-Baselines3 in Colab; bar = beat same time yesterday at equal cost (B07, B08) | ✓ | README Plan (week of 9 Nov) and Results paragraph | plan, not a result |
| 25 numbers in the observation (B07) | ✓ | `observation_space` shape `window + yesterday_window + 5` = 25 | |
| B04/B05 burst chart | ✓ | held-out app 8c2b9304 day 10 (the day `scripts/demo.py` plots), minutes 896-917; y axis is scaled requests (labelled "scaled") | |
| Data credit | ✓ | Shahrad et al., Serverless in the Wild, USENIX ATC 2020; CC-BY 4.0 (shown in B03) | |
| B00 summary: an autoscaler that only reacts is already late; yesterday's traffic helps | ✓ | boot delay 3 min (env.py); same time yesterday 5.47% -> 1.17% (demo_stdout.txt) | |
| AI disclosure (B00) | ✓ | narration is Kokoro af_bella; project is Laksh's, built with help from Claude Code | |

Not used in this video: the "73% vs 5% by chance" repeat example (see the companion explainer's FACTCHECK: the
5% chance figure did not reproduce here).
