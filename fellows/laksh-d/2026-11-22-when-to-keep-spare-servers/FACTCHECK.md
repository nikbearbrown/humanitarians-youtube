# FACTCHECK: When to Keep Spare Servers

Source of truth: lakshdhamija/rl-autoscaler @ a886c1b ("Add Huawei multi-week traces and a PPO agent that sets HPA's
target", 2026-11-22): its processed Azure and Huawei datasets, `results/stress-hpa.json`, `results/ppo-hpa/*.json`
(30 runs) and `evidence/make_evidence.py`, which asserts every number below against the brief and stops on any
difference. Keys are paths in `evidence/evidence.json`. Checked 2026-11-22.

| Claim (beat) | Verdict | Evidence key / derivation |
|---|---|---|
| The only baseline is HPA (Kubernetes Horizontal Pod Autoscaler) with a fixed target (B01, B02, B10) | ✓ | README Approach "Baseline" and "RL sets HPA's target"; `curves` = HPA at targets 40-90% |
| HPA adds servers past a target, e.g. 70% (B02) | ✓ | `policies.ThresholdPolicy` (desired = load / (600 x target), 10% tolerance, 5-min scale-down window); `window.target` 0.7 |
| On screen: one held-out Huawei function, 18:50-19:20, requests jump 1.8x at 19:00, HPA's first new server serves 3 minutes later, 7 late minutes (B02) | ✓ | `window` (pri-60, day 12, `jump` 1.78, `late_minutes` 7); boot asserted = 3 |
| Most bursts jump within a minute: 72% peak in their first minute, Azure training days (B02) | ✓ | `burst_first_minute_pct.azure` 72 (traffic.find_bursts, minutes to peak = 0) |
| New servers take 3 minutes to boot; 600 requests a minute each (B02, B08) | ✓ | `cluster.boot` 3, `cluster.capacity` 600 (env.ClusterConfig) |
| A 70% target keeps 30% spare, the same all day (B02) | ✓ | definition of a fixed target utilization (100% - 70%); `window.target` |
| PPO picks HPA's target every minute, 40% to 90%; HPA's own rule turns it into servers (B03) | ✓ | `targets` (train.HEADROOM_TARGETS); train.Headroom / HeadroomEnv |
| It sees the last 10 minutes, yesterday's and last week's next 10 minutes, servers running and booting, queue, time of day (B03) | ✓ | env._obs; asserted window 10, yesterday 10, last week 10; sparklines = `window.load[0:10]`, `window.yesterday[10:20]`, `window.last_week[10:20]` |
| Azure Functions 2019: 19 apps, 14 days, 5 held out; Huawei public 8 functions, 26 days, 2 held out; private 26 functions, 33 days, 8 held out; last 7 Huawei days unseen (B04) | ✓ | `sizes` |
| 30% of Huawei functions held out (on screen as counts) | ✓ | `huawei_held_out` (prepare_huawei.TEST_SHARE 0.3; 10 of 34) |
| 456 training days, 42 Azure, 414 Huawei (B04) | ✓ | `train_days` (episodes("train", ..., 7)) |
| 30 runs on Modal: 2 history settings x 5 late penalties x 3 seeds, 3M steps each (B04) | ✓ | `training` (results/ppo-hpa/*.json: steps 3000000, penalties 0.01-1.0, seeds 0-2, bad_days 0 / 0.3) |
| Chart: HPA curve and every run's cost and late % on 4 test sets (B05) | ✓ | `curves`, `points` (stress-hpa.json "normal" = results/ppo-hpa/*.json, asserted equal) |
| On 3 of 4 test sets every run is below HPA's line (B05) | ✓ | `score.{huawei/test_apps, huawei/test_days, azure/test_days}.*.better` = 15 of 15 for both variants |
| Huawei held-out: 15/15, 15% to 57% fewer late requests; misleading-trained 15/15, 5% to 60% (B06) | ✓ | `score.huawei/test_apps` (-57..-15, -60..-5), frontier.rule_late_at at each run's own cost |
| Huawei unseen days 15/15, 15-36%; 15/15, 8-40% (B06) | ✓ | `score.huawei/test_days` |
| Azure unseen days 15/15, 7-29%; 15/15, 2-29% (B06) | ✓ | `score.azure/test_days` |
| Azure held-out apps 8/15 (29% fewer to 33% more); 10/15 (32% fewer to 45% more) (B00, B06) | ✓ | `score.azure/test_apps` |
| Better than HPA in 53 of 60 runs; 55 of 60 when trained with misleading history (B00, B07, B10) | ✓ | `stress.normal.normal_better` 53, `stress.misleading.normal_better` 55 |
| Changes: yesterday or last week x0.2 (holiday), x3 (launch), x0 (metrics outage) (B07) | ✓ | `stress_scenarios` (6), scripts/stress.py SCENARIOS |
| Misleading history: RL beats HPA in 208 of 360 cases (58%) trained on normal history, 273 of 360 (76%) trained with misleading history (B07, B10) | ✓ | `stress.normal` / `stress.misleading` (each run vs HPA under the same change, rule_late_at) |
| Worst case: 93% and 64% more late requests than HPA (B07) | ✓ | `stress.*.worst` |
| 4 of the 5 Azure held-out apps are 2 to 4 times burstier than a typical Azure training app (B08) | ✓ | `burstiness.held_out` 0.033, 0.140, 0.196, 0.248, 0.267; `burstiness.median.azure` 0.065 (ratios 2.2, 3.0, 3.8, 4.1); also 2-4x against the median of all 38 training apps |
| There, lean agents lose and agents with more spare servers win (B08) | ✓ | `azure_apps_by_penalty`: lowest late penalty 0 of 6 runs better, highest 6 of 6 (mean cost 17,901 vs 22,384) on the held-out apps as a set |
| The servers are simulated: same cost per request; real HPA usually scales on CPU, every 15 s (B08) | ✓ | README Limits |
| Next: more varied traffic (web server logs, LLM serving) with balanced training and a bigger held-out set; Huawei's per-minute instance and CPU metrics to calibrate the simulator; which history inputs help (B09) | ✓ | README Plan (next step); plan, not a result |
| AI disclosure (B00) | ✓ | narration is Kokoro af_bella; the project is Laksh's, built with help from Claude Code |
