# What PPO Is, In Plain Words

- **Week:** 9–15 Nov 2026 · **Group:** RL Environment
- **Type:** STEM explainer, told on my project's environment
- **Code:** [lakshdhamija/rl-autoscaler](https://github.com/lakshdhamija/rl-autoscaler), commit [8b126bd](https://github.com/lakshdhamija/rl-autoscaler/commit/8b126bd); Stable-Baselines3 2.9.2
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **This week's project update:** [Can PPO Beat Yesterday?](../2026-11-15-can-ppo-beat-yesterday/README.md)
- **Beat sheets:** [landscape](beat_sheet.json) · [vertical](vertical/beat_sheet.json)

## This week's contribution

What is Proximal Policy Optimization (PPO), the algorithm my autoscaler trains with? Told on my own environment, where every minute the agent sees 25 numbers and picks one of 11 actions (remove 5 to add 5 servers), and the reward is minus server cost minus a penalty per late request:

- a policy network turns what the agent sees into a probability for each action;
- training collects a batch of steps (2,048 by default), then improves the policy from it;
- the advantage says how much better an action did than expected; a critic network makes that estimate;
- the ratio between the new and the old probability of an action is clipped to 0.8 to 1.2 in the objective, L = E[min(r A, clip(r, 1−ε, 1+ε) A)] (Schulman et al. 2017), so one update is less likely to wreck a policy that already works;
- each batch is used for 10 passes (Stable-Baselines3 defaults).

No PPO results for the autoscaler are stated; those are in this week's project update.

Takeaway: if RL training suddenly collapses, check the size of each update first.

## Human and AI work

- **Laksh D.:** chose the topic; asked for two accuracy fixes after reviewing the preview; reviewed this video.
- **Claude Code:** wrote the narration, the beat sheets, `scenes.py` and `evidence/check_facts.py`; rendered both versions and ran the toolkit checks.
- **Voice:** Kokoro `af_bella`, an AI voice. The video says so in its first beat.
- **Corrected during the build:** "an update cannot wreck the policy" and "the ratio stays between 0.8 and 1.2" were softened to the correct claims ("less likely to wreck", "clipped to"); the letter "A" is respelled so the voice says it as a letter.

## Reproduce

- **Toolkit:** brutalist.art commit `3a6d3979`, checked 2026-11-11 (Fellow Tier `ai-explainer` with the `hai` persona).
- **Source:** `lakshdhamija/rl-autoscaler` at `8b126bd`; stable-baselines3 2.9.2. Paper: Schulman et al., "Proximal Policy Optimization Algorithms", arXiv:1707.06347.
- **Numbers on screen:** `evidence/check_facts.py` reads them from the installed Stable-Baselines3 and the repository's `env.py`; output in `evidence/facts_stdout.txt`.
- **Build:** copy this folder into a reel folder, then `./art run <reel>` for a review cut and `./art final <reel>` for the master. The vertical version uses `vertical/beat_sheet.json` with the same `scenes.py`.
- **Checks:** [FACTCHECK.md](FACTCHECK.md), [SOURCES.md](SOURCES.md).

## Watch and review

| Version | Resolution | Length | SHA-256 |
|---|---|---|---|
| Landscape | 3840×2160 | 2:28 | `44ff9a590875fcdcdefc8b51575831e3ede6ff2178b8b461dadbccdebc31ed92` |
| Vertical | 2160×3840 | 2:28 | `4a3fa7c314dbc96c643031455889e60651664140de7ef0e36fce7c4b56bd28c5` |

- **Files:** `WhatIsPPO_LakshDhamija.mp4` (landscape) and `WhatIsPPO_LakshDhamija-vertical.mp4` in `Week2-Nov-9/` of the [project Drive folder](https://drive.google.com/drive/folders/1IqLdBcMUEMXJP-JBYhMP7OVyV81zTXX3?usp=drive_link).
- **PM review:** pending.
