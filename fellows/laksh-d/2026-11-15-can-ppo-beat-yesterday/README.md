# Can PPO Beat Yesterday?

- **Week:** 9–15 Nov 2026 · **Group:** RL Environment
- **Project:** Predictive Autoscaling with Reinforcement Learning
- **Code:** [lakshdhamija/rl-autoscaler](https://github.com/lakshdhamija/rl-autoscaler), commit [35e922d](https://github.com/lakshdhamija/rl-autoscaler/commit/35e922d)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **This week's explainer:** [What PPO is, in plain words](../2026-11-15-what-is-ppo/README.md)
- **Beat sheets:** [landscape](beat_sheet.json) · [vertical](vertical/beat_sheet.json)

## This week's contribution

Question: can a PPO agent beat "same time yesterday", the best rule so far, at equal cost?

Built: PPO agents (Stable-Baselines3) of two kinds: plain PPO, which learns from nothing, and residual PPO, which corrects the rule's action by -5 to +5 servers. 30 runs on Modal CPUs (2 kinds × 5 late penalties × 3 seeds) and 4 new tests (17 in total).

Result on 5 held-out apps: no agent beats the rule at equal cost. The best, residual PPO at the highest penalty, ties it: 0.52% late against about 0.56% for the rule at the same cost, a gap smaller than the spread between seeds.

Finding: the 14 days have a weekly shape. Days 6–7 and 13–14 are the quietest and day 8 is the busiest, so on day 8 "same time yesterday" plans from a quiet day. Two weeks hold only one such day per app, too few to test.

Next: real traces several weeks long, a "same time last week" baseline, the baselines tested first, then PPO again.

## Human and AI work

- **Laksh D.:** chose the two agent kinds and the 30-run sweep; raised the weekly pattern and moved the plan to multi-week data; reviewed the code, the results and this video.
- **Claude Code:** wrote the training code, the Modal script and the chart under Laksh's direction; wrote the narration, the beat sheets and `scenes.py`; rendered both versions and ran the toolkit checks.
- **Voice:** Kokoro `af_bella`, an AI voice. The video says so in its first beat.
- **Corrected during the build:** the B06 headline first said "Quiet weekends", but the trace does not record weekdays, so the screen says "A weekly shape". The best agent is called a tie, not a win, because its lead over the rule is smaller than the seed spread.

## Reproduce

- **Toolkit:** brutalist.art commit `3a6d3979`, checked 2026-11-15 (Fellow Tier `ai-explainer` with the `hai` persona).
- **Source:** `lakshdhamija/rl-autoscaler` at `35e922d`. Data: Azure Functions Trace 2019, CC-BY 4.0, Shahrad et al., USENIX ATC 2020.
- **Numbers on screen:** `evidence/make_evidence.py` computes every number and curve from the repository (including its `results/ppo/*.json`) and writes `evidence/evidence.json`. Recorded run: `evidence/pytest_stdout.txt`.
- **Build:** copy this folder into a reel folder, then `./art run <reel>` for a review cut and `./art final <reel>` for the master. The vertical version uses `vertical/beat_sheet.json` with the same `scenes.py`.
- **Checks:** [FACTCHECK.md](FACTCHECK.md), [SOURCES.md](SOURCES.md).

## Watch and review

| Version | Resolution | Length | SHA-256 |
|---|---|---|---|
| Landscape | 3840×2160 | 2:24 | `b3fcb88591510d18b1e2d90391e73f6cb3cbdc9d4facc9662ded75bdfd39cbc3` |
| Vertical | 2160×3840 | 2:24 | `26943edea4c9d62639cb8baf5bd720b2063c8adca9d4930052e38f374ff76b76` |

- **Files:** `CanPPOBeatYesterday_LakshDhamija.mp4` (landscape) and `CanPPOBeatYesterday_LakshDhamija-vertical.mp4` in `Week2-Nov-9/` of the [project Drive folder](https://drive.google.com/drive/folders/1IqLdBcMUEMXJP-JBYhMP7OVyV81zTXX3?usp=drive_link).
- **PM review:** pending.
