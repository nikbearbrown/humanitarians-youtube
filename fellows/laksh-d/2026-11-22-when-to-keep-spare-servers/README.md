# When to Keep Spare Servers

- **Week:** 16–22 Nov 2026 · **Group:** RL Environment
- **Project:** Predictive Autoscaling with Reinforcement Learning
- **Code:** [lakshdhamija/rl-autoscaler](https://github.com/lakshdhamija/rl-autoscaler), commit [a886c1b](https://github.com/lakshdhamija/rl-autoscaler/commit/a886c1b)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **This week's explainer:** [When History Misleads](../2026-11-22-when-history-misleads/README.md)
- **Beat sheets:** [landscape](beat_sheet.json) · [vertical](vertical/beat_sheet.json)

## This week's contribution

Question: can a reinforcement learning agent beat the Kubernetes Horizontal Pod Autoscaler (HPA) at equal cost by deciding, minute by minute, how many spare servers to keep?

Built: multi-week real traffic from the Huawei Cloud 2023 traces (34 functions, 26 and 33 days), next to the 19 Azure apps. HPA, whose rule is documented, is now the only baseline; rules we had written ourselves ("same time yesterday", "same time last week") are set aside because they are not production autoscalers. The new agent is PPO that picks HPA's target utilization (40% to 90%) every minute; HPA turns it into a server count. It sees the last 10 minutes, yesterday's and last week's traffic at this time, the servers, the queue and the time of day. 30 runs on Modal CPUs (5 late penalties, 3 seeds, trained on normal history and with misleading history), and a test where yesterday or last week misleads.

Result, each run against HPA at the same cost:

| Test set | Trained on normal history | Trained with misleading history |
|---|---|---|
| Huawei, held-out functions | 15 of 15 runs better, 15% to 57% fewer late requests | 15 of 15, 5% to 60% fewer |
| Huawei, unseen days | 15 of 15, 15% to 36% fewer | 15 of 15, 8% to 40% fewer |
| Azure, unseen days | 15 of 15, 7% to 29% fewer | 15 of 15, 2% to 29% fewer |
| Azure, held-out apps | 8 of 15 | 10 of 15 |

When yesterday or last week misleads (a holiday, a launch, a metrics outage), PPO still beats HPA in 58% of 360 cases, and in 76% when it was trained with misleading history.

Limits: 4 of the 5 Azure held-out apps are 2 to 4 times burstier than the typical training app. The servers are simulated (600 requests per minute each, 3-minute boot, every request the same cost).

Next: more varied traffic beyond serverless, balanced training, a validation group and a bigger held-out set; server capacity and request cost from real data; test which history inputs help.

## Human and AI work

- **Laksh D.:** raised the weekly-pattern question, chose the multi-week data, set HPA as the only baseline, asked for the misleading-history test and for a check of the simulator's server assumptions, and reviewed the code, the results and this video.
- **Claude Code:** wrote the data script, the agent, the training batch and the tests under Laksh's direction; wrote the narration, the beat sheets and `scenes.py`; rendered both versions and ran the toolkit checks.
- **Voice:** Kokoro `af_bella`, an AI voice. The video says so in its first beat.
- **Corrected during the work:** three public functions with days far above normal load (likely load tests) are filtered out; that filter also looked at the unseen days, which is fixed in the next data rebuild.

## Reproduce

- **Toolkit:** brutalist.art commit `3a6d3979`, checked 2026-11-22 (Fellow Tier `ai-explainer` with the `hai` persona).
- **Source:** `lakshdhamija/rl-autoscaler` at `a886c1b`. Data: Azure Functions Trace 2019, CC-BY 4.0, Shahrad et al., USENIX ATC 2020; Huawei Cloud traces 2023, CC BY 4.0, Joosen et al., ACM SoCC 2023.
- **Numbers on screen:** `evidence/make_evidence.py` computes every number and curve from the repository (`results/stress-hpa.json`, `results/ppo-hpa/*.json`) and writes `evidence/evidence.json`. Recorded run: `evidence/pytest_stdout.txt`.
- **Build:** copy this folder into a reel folder, then `./art run <reel>` for a review cut and `./art final <reel>` for the master. The vertical version uses `vertical/beat_sheet.json` with the same `scenes.py`.
- **Checks:** [FACTCHECK.md](FACTCHECK.md), [SOURCES.md](SOURCES.md).

## Watch and review

| Version | Resolution | Length | SHA-256 |
|---|---|---|---|
| Landscape | 3840×2160 | 2:26 | `c6418d64f91bfd9d1a3ad780b6807eb8d8f7ab918d33a0bf965304c2d41dd271` |
| Vertical | 2160×3840 | 2:26 | `b06057a1f190cdb78fa3f3aaf4941f7f2d5eab5406264e5e9a2f4291f386721c` |

- **Files:** `SpareServers_LakshDhamija.mp4` (landscape) and `SpareServers_LakshDhamija-vertical.mp4` in `Week3-Nov-16/` of the [project Drive folder](https://drive.google.com/drive/folders/1IqLdBcMUEMXJP-JBYhMP7OVyV81zTXX3?usp=drive_link).
- **PM review:** pending.
