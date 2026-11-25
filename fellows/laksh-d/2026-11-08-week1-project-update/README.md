# Why Autoscalers Need Yesterday's Traffic

- **Week:** 2–8 Nov 2026 · **Group:** RL Environment
- **Project:** Predictive Autoscaling with Reinforcement Learning
- **Code:** [lakshdhamija/rl-autoscaler](https://github.com/lakshdhamija/rl-autoscaler), commit [8b126bd](https://github.com/lakshdhamija/rl-autoscaler/commit/8b126bd)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **This week's explainer:** [What real cloud traffic looks like](../2026-11-08-what-real-cloud-traffic-looks-like/README.md)
- **Beat sheets:** [landscape](beat_sheet.json) · [vertical](vertical/beat_sheet.json)

## This week's contribution

Question: can an autoscaler keep fewer requests waiting than the Kubernetes rule, at the same cost?

Built: a Gymnasium environment (one step is one minute, new servers take 3 minutes to boot, reward is minus server cost minus a penalty per late request), real traffic from the Azure Functions Trace 2019 (19 web apps, 14 days each), a synthetic traffic generator fitted to that real traffic, four baselines and 13 tests.

Result on 5 held-out apps and 65 unseen days: a "same time yesterday" rule cut late requests from 5.47% (Kubernetes rule) to 1.17%. The Kubernetes rule at a 50% target spends more (27,371 server-minutes a day against 24,488) and is still late 3.10% of the time.

Next: train a PPO agent (Stable-Baselines3). Its bar is "same time yesterday" at equal cost.

## Human and AI work

- **Laksh D.:** set the project direction with the RL project managers; approved the data source, the train and test split and the baselines; reviewed the code, the results and this video.
- **Claude Code:** wrote most of the code in the repository under Laksh's direction; wrote the narration, the beat sheets and `scenes.py`; rendered both versions and ran the toolkit checks.
- **Voice:** Kokoro `af_bella`, an AI voice. The video says so in its first beat.
- **Corrected during the build:** the toolkit's standard outro carries another channel's handle, so the outro is a custom title card with @HumanitariansAI; the narration spells "Laksh" so the voice says it correctly.

## Reproduce

- **Toolkit:** brutalist.art commit `3a6d3979`, checked 2026-11-08 (Fellow Tier `ai-explainer` with the `hai` persona).
- **Source:** `lakshdhamija/rl-autoscaler` at `8b126bd`. Data: Azure Functions Trace 2019, CC-BY 4.0, Shahrad et al., USENIX ATC 2020.
- **Numbers on screen:** `evidence/make_evidence.py` computes every number and curve from the repository and writes `evidence/evidence.json`. Recorded runs: `evidence/demo_stdout.txt`, `evidence/pytest_stdout.txt`, `evidence/env.txt`.
- **Build:** copy this folder into a reel folder, then `./art run <reel>` for a review cut and `./art final <reel>` for the master. The vertical version uses `vertical/beat_sheet.json` with the same `scenes.py`.
- **Checks:** [FACTCHECK.md](FACTCHECK.md), [SOURCES.md](SOURCES.md).

## Watch and review

| Version | Resolution | Length | SHA-256 |
|---|---|---|---|
| Landscape | 3840×2160 | 2:04 | `e04b67b0a026f9e57cc81587fc47297b03669fdd66e249d9fc2d17ca5e58dc68` |
| Vertical | 2160×3840 | 2:04 | `7366c225590584e9b382d22870d1896b5d0634fb23c05287e13e30a5821bc919` |

- **Files:** `YesterdaysTraffic_LakshDhamija.mp4` (landscape) and `YesterdaysTraffic_LakshDhamija-vertical.mp4` in `Week1-Nov-2/` of the [project Drive folder](https://drive.google.com/drive/folders/1IqLdBcMUEMXJP-JBYhMP7OVyV81zTXX3?usp=drive_link).
- **PM review:** pending.
