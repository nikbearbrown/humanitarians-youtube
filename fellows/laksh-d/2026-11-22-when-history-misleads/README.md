# When History Misleads

- **Week:** 16–22 Nov 2026 · **Group:** RL Environment
- **Project:** Predictive Autoscaling with Reinforcement Learning
- **Code:** [lakshdhamija/rl-autoscaler](https://github.com/lakshdhamija/rl-autoscaler), commit [a886c1b](https://github.com/lakshdhamija/rl-autoscaler/commit/a886c1b)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **This week's project update:** [When to Keep Spare Servers](../2026-11-22-when-to-keep-spare-servers/README.md)
- **Beat sheets:** [landscape](beat_sheet.json) · [vertical](vertical/beat_sheet.json)

## Topic

An autoscaling agent that reads yesterday's and last week's traffic can be fooled when those days were unusual: a holiday, a launch, or a gap in the metrics. This explainer shows what that does to a PPO agent that sets the Kubernetes HPA rule's target, and how training it with misleading history (a form of domain randomization) helps.

Result, 360 test cases per agent (6 kinds of misleading history × 4 test sets × 15 runs), each against HPA at the same cost: the agent trained on normal history beats HPA in 208 (58%), the agent trained with misleading history in 273 (76%), with no loss on normal history.

## Human and AI work

- **Laksh D.:** asked what happens when yesterday is not a good guide, chose the topic and reviewed the results.
- **Claude Code:** wrote the test, the evidence script, the narration and the scenes and rendered both versions.
- **Voice:** Kokoro `af_bella`, an AI voice. The video says so in its first beat.

## Reproduce

- **Toolkit:** brutalist.art commit `3a6d3979`, checked 2026-11-22 (Fellow Tier `ai-explainer` with the `hai` persona).
- **Source:** `lakshdhamija/rl-autoscaler` at `a886c1b` (`scripts/stress.py`, `results/stress-hpa.json`).
- **Numbers on screen:** `evidence/make_evidence.py` computes every number from the repository and writes `evidence/evidence.json`.
- **Checks:** [FACTCHECK.md](FACTCHECK.md), [SOURCES.md](SOURCES.md).

## Watch and review

| Version | Resolution | Length | SHA-256 |
|---|---|---|---|
| Landscape | 3840×2160 | 2:08 | `bccb9a078a6f0f720f493b2d7bdc89c2cd40c8721196427f8a2134da04f8dc6c` |
| Vertical | 2160×3840 | 2:08 | `0427d5c2e48c88f532501e8674f9c4a6de6a760ca672ba9d9b7845ee8730dd8c` |

- **Files:** `WhenHistoryMisleads_LakshDhamija.mp4` (landscape) and `WhenHistoryMisleads_LakshDhamija-vertical.mp4` in `Week3-Nov-16/` of the [project Drive folder](https://drive.google.com/drive/folders/1IqLdBcMUEMXJP-JBYhMP7OVyV81zTXX3?usp=drive_link).
- **PM review:** pending.
