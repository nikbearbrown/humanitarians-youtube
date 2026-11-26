# Fellowship Renewal Request — Sudhanva D.

**Name:** Sudhanva Devanathan  
**Role:** Software Engineer  
**Project:** RL Environments: training ant agents to forage alone, then together, with multi-agent RL  
**Current agreement dates:** October 14 to November 30, 2026  
**Requested renewal dates:** December 1, 2026 to January 31, 2027 (2 months)  
**Reporting period:** October 14 to November 22, 2026 (weeks 1–5); November 23–30 will be appended  
**Supervisors:** Dhruv and Dev  
**Project repository:** [Nenyax-AI/team-work · projects/learning-environments/ant-foraging](https://github.com/Nenyax-AI/team-work/tree/ant-head-research/projects/learning-environments/ant-foraging) (private) · public mirror with the same files: [sdevanathan96/ant-head-rl-research](https://github.com/sdevanathan96/ant-head-rl-research)  
**Fellows folder:** [fellows/sudhanva-d](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/sudhanva-d)

---

## Executive Summary

In five weeks I took the RL Environments project from a literature review to a tested multi-agent RL testbed: two foraging worlds, six learners and 142 evaluated training runs. Pairs of ants now learn to carry food home together from their own local observations (IPPO 11.85 of 12 on the grid), and I found and fixed why QMIX collapsed (0.13 → 8.44 of 12). Every week has at least 20 documented hours (111.5 in total), two Brutalist videos in 16:9 and 9:16, and a dated Frictional log. Every item below links directly to its evidence.

---

## Completed

1. **A tested multi-agent RL testbed for ant foraging.** A grid world and a continuous world in which ants find food, cut large items into pieces and carry the pieces home in pairs. Six learners (IQL, IQL-team, VDN, QMIX, IPPO, MAPPO), a training CLI, held-out evaluation, paired-carry and coordination metrics, and 39 passing tests. The evaluation files of all 142 runs are committed, so every results table can be rebuilt. **Contribution:** I designed the environments, metrics and experiments, ran every training run, and am the sole human author of all 12 project commits (most are co-authored with Claude Code). **Evidence:** [Worlds and learners (`600355b`)](https://github.com/Nenyax-AI/team-work/commit/600355bde928daeec9e0078cec27a23f911ade9e) · [Six learners at 1M steps, paired-carry metric (`3c4e2f3`)](https://github.com/Nenyax-AI/team-work/commit/3c4e2f311ab335e1894b7c0bf7be3069ba704eaf) · [Evaluation files (`f46147a`)](https://github.com/Nenyax-AI/team-work/commit/f46147a76ac552c08b002d05c5b2187dc399874f) · [RESULTS.md](https://github.com/Nenyax-AI/team-work/blob/ant-head-research/projects/learning-environments/ant-foraging/RESULTS.md) · [PR #24](https://github.com/Nenyax-AI/team-work/pull/24)

2. **Cooperative transport learned without shortcuts.** I found that the first 12/12 result came from a scripted cue (a policy that only follows the cue also scores 12/12), and that the first cue-free result relied on hand-coded syncing between paired ants. I removed both, fixed PPO bootstrapping through timeouts into the next episode, and trained longer. Pairs now carry 3.94 (IPPO) and 3.82 (MAPPO) of 4 pieces on the grid from local observations (11.85 and 11.61 of 12 food, 5 seeds), and reach 11.49 and 11.41 in the continuous world at 10M steps. The invalid results are withdrawn in RESULTS.md. **Contribution:** I ran the baseline checks that exposed both shortcuts, and made the fix. **Evidence:** [Cue removed (`e5295c0`)](https://github.com/Nenyax-AI/team-work/commit/e5295c048a34e4195035dd522469eee5cc8574be) · [Timeout fix, honest transport (`518d820`)](https://github.com/Nenyax-AI/team-work/commit/518d820625477a1860d6f5869db98922fddd0d6c) · [Week 2 check](../2026-11-01-rl-environments/FRICTIONAL.md) · [Week 3 check](../2026-11-08-rl-environments/FRICTIONAL.md)

3. **Why QMIX collapsed, and a fairer scoring protocol.** By logging the value prediction and its target, I showed that syncing the target network every 500 updates makes QMIX's team value overshoot (about 40 on the grid while the team scores 0, and over 800,000 in one continuous-world run). Syncing every 2,000 updates with half the learning rate raised grid QMIX from 0.13 to 8.44 and VDN from 6.05 to 8.55. I also made sampled scores the headline, because greedy play can deadlock two holders and understated continuous-world IPPO by 1.1. **Contribution:** diagnosis, tuning screen (18 runs), confirmation runs (24) and the protocol change. **Evidence:** [QMIX diagnosis and retune (`8d85f5f`)](https://github.com/Nenyax-AI/team-work/commit/8d85f5f50061f6b7fe388de7688a3772da38dce6) · [Sampled headline (`c9369a8`)](https://github.com/Nenyax-AI/team-work/commit/c9369a8c450baecbd8efb3d657ac5395402f2a92) · [PR #27](https://github.com/Nenyax-AI/team-work/pull/27) · [Week 5 report](../2026-11-22-rl-environments/FRICTIONAL.md)

I also produced ten Brutalist videos, a project update and a STEM explainer each week, all in 16:9 and 9:16 (links in the index below).

---

## Hours Status

**20+ hours documented for every reported week:** 111.5 hours over weeks 1–5 (22.0, 20.0, 21.0, 23.0 and 25.5). Each week's `HOURS.md` breaks the hours into tasks with evidence links; the summary is in [HOURS.md](../HOURS.md). I did not attend the weekly meeting in week 1. November 23–30, the last week of the current agreement, is in progress and will be appended.

---

## Weekly Evidence Index

| Week / dates | Actual hours | Video links | Log and work evidence |
|---|---:|---|---|
| **Week 1** · Oct 19 – Oct 25, 2026 | 22.0 | Update, "Training Ants to Work Together": [16:9](https://drive.google.com/file/d/1W0RU7rNXytdmMnjRx0wEdUQBcypBMiyk/view?usp=sharing) · [9:16](https://drive.google.com/file/d/1h4WKTlyP00S6VxXQw7pSk7G03tXGndKw/view?usp=sharing) <br> Explainer, "How a Quotient Filter Works": [16:9](https://drive.google.com/file/d/1lzpGy8k3oCavfzcNAN6R8uq3zieloGu0/view?usp=sharing) · [9:16](https://drive.google.com/file/d/1PNO7YuXYJz4CnzdUDjlBJ_Q9jpJZfghL/view?usp=sharing) | [Research report and Frictional log](../2026-10-25-rl-environments/FRICTIONAL.md) · [Weekly hours](../2026-10-25-rl-environments/HOURS.md) · Research week, no code |
| **Week 2** · Oct 26 – Nov 1, 2026 | 20.0 | Update, "Did the Ants Learn to Cooperate?": [16:9](https://drive.google.com/file/d/1_BwCwNFtzX5jRuZSyHROQPy2qHG3VDA-/view?usp=sharing) · [9:16](https://drive.google.com/file/d/1Mf0X9HVxuMVSgomlgt2qJYwSV1YUOyke/view?usp=sharing) <br> Explainer, "How HyperLogLog Counts": [16:9](https://drive.google.com/file/d/1IrxJ0-tlCrfOpzgItNBg5AqLwJSw5tjU/view?usp=sharing) · [9:16](https://drive.google.com/file/d/1dXlN1YILCDm2PSX1D9XoXueLtfp_fZRk/view?usp=sharing) | [Report and Frictional log](../2026-11-01-rl-environments/FRICTIONAL.md) · [Weekly hours](../2026-11-01-rl-environments/HOURS.md) · [`600355b`](https://github.com/Nenyax-AI/team-work/commit/600355bde928daeec9e0078cec27a23f911ade9e) · [`db2195c`](https://github.com/Nenyax-AI/team-work/commit/db2195c59ef4dca3126a5f2ddfb30ae70393c346) · [`bfe4eb3`](https://github.com/Nenyax-AI/team-work/commit/bfe4eb35889b5cf928147487cb76a673548e8c1b) (withdrawn) |
| **Week 3** · Nov 2 – Nov 8, 2026 | 21.0 | Update, "Did They Learn It This Time?": [16:9](https://drive.google.com/file/d/1bYeYnU09Z8kUu756TaAfLYum6PsrVy25/view?usp=sharing) · [9:16](https://drive.google.com/file/d/1EaL7K2FMit_EfwXLpZlWYme6vi4J-RwX/view?usp=sharing) <br> Explainer, "How IPPO Learns": [16:9](https://drive.google.com/file/d/1SRMySOFjF8a7hGapptrkMuDtkzn5o9Ue/view?usp=sharing) · [9:16](https://drive.google.com/file/d/1ous7hAZcaaa1Uxp69Tqf897_8IlOqxZu/view?usp=sharing) | [Report and Frictional log](../2026-11-08-rl-environments/FRICTIONAL.md) · [Weekly hours](../2026-11-08-rl-environments/HOURS.md) · [`e5295c0`](https://github.com/Nenyax-AI/team-work/commit/e5295c048a34e4195035dd522469eee5cc8574be) · [`518d820`](https://github.com/Nenyax-AI/team-work/commit/518d820625477a1860d6f5869db98922fddd0d6c) · [`151a140`](https://github.com/Nenyax-AI/team-work/commit/151a140769b8e653bfa4f5bb6942c4c699caa157) · [`800141b`](https://github.com/Nenyax-AI/team-work/commit/800141bdebc87aec3cbdbe0be1238821ef3fc604) |
| **Week 4** · Nov 9 – Nov 15, 2026 | 23.0 | Update, "Which Ants Carry Together?": [16:9](https://drive.google.com/file/d/1J9dj7HdDP6suvWiFXkZs_uL8dK1Nd6GV/view?usp=sharing) · [9:16](https://drive.google.com/file/d/1vC2mkYfr6dm9lsm8iUy52Ev045bQgo9k/view?usp=sharing) <br> Explainer, "One Value, Four Ants": [16:9](https://drive.google.com/file/d/1g1ZRvAbBfr3G_dTaR5guYI8z3eTj6qCt/view?usp=sharing) · [9:16](https://drive.google.com/file/d/1curbwG4Zqr1iNL5UhczN2F2p6XzZzjqX/view?usp=sharing) | [Report and Frictional log](../2026-11-15-rl-environments/FRICTIONAL.md) · [Weekly hours](../2026-11-15-rl-environments/HOURS.md) · [`3c4e2f3`](https://github.com/Nenyax-AI/team-work/commit/3c4e2f311ab335e1894b7c0bf7be3069ba704eaf) |
| **Week 5** · Nov 16 – Nov 22, 2026 | 25.5 | Update, "Why QMIX Collapsed, and Why Sample over Greedy?": [16:9](https://drive.google.com/file/d/1WKsM7oCrWpoegIH3LdKKdMeDZOLAUqDJ/view?usp=sharing) · [9:16](https://drive.google.com/file/d/1dBu1S78Uozv7ub8eK0RsoymXgjoWtI20/view?usp=sharing) <br> Explainer, "Chasing Its Own Guess.": [16:9](https://drive.google.com/file/d/1tswge_MZtiulv8O_554tqwXmMlLE5OH8/view?usp=sharing) · [9:16](https://drive.google.com/file/d/1ePoxFQde7ZXdspUD4OLm4s9Xm_Sp7WXE/view?usp=sharing) | [Report and Frictional log](../2026-11-22-rl-environments/FRICTIONAL.md) · [Weekly hours](../2026-11-22-rl-environments/HOURS.md) · [WORK_PROGRESS.md](https://github.com/Nenyax-AI/team-work/blob/ant-head-research/projects/learning-environments/ant-foraging/WORK_PROGRESS.md) · [`384d0c9`](https://github.com/Nenyax-AI/team-work/commit/384d0c9a6e53ba57c6d9362a00f84dbc19ece6de) · [`f46147a`](https://github.com/Nenyax-AI/team-work/commit/f46147a76ac552c08b002d05c5b2187dc399874f) · [`8d85f5f`](https://github.com/Nenyax-AI/team-work/commit/8d85f5f50061f6b7fe388de7688a3772da38dce6) · [`c9369a8`](https://github.com/Nenyax-AI/team-work/commit/c9369a8c450baecbd8efb3d657ac5395402f2a92) |
| **Total (Weeks 1–5)** | **111.5** | 20 files: 5 updates and 5 explainers, each in 16:9 and 9:16 | |

---

## Degree Relevance and Supervision

MS in Computer Science, Northeastern University Boston, May 2026. The project applies my coursework in Reinforcement Learning, Machine Learning and Deep Learning directly: designing simulation environments and reward functions, implementing and debugging deep reinforcement learning algorithms (Q-learning with target networks, value decomposition, PPO with centralised and decentralised critics), and running reproducible experiments with held-out evaluation and tests.

**Supervisors:** Dhruv Patel and Dev Shah

---

## Authorization

- **Authorization type:** F-1 Post-Completion OPT

---

## Next Period Plan (December 1, 2026 – January 31, 2027)

**Research question:** which learners really cooperate when cooperation is required, and why? At 1M steps the grid separates cooperative learners from independent ones, but the continuous world does not: a lone ant can drag a piece, so tuned IQL, which cannot see its teammates, scores level with PPO.

| Target date | Deliverable |
|---|---|
| **December 6, 2026** | Home-vector test: hide one holder's home vector and measure whether the pair still agrees and delivers. Log sampled scores during training so the learning curves match the headline. |
| **December 20, 2026** | Tune PPO with the same care as the value-based learners, so the comparison is tuned against tuned. |
| **January 10, 2027** | A continuous-world variant in which delivering a piece requires two ants, and a re-run of all six learners on it. |
| **January 24, 2027** | Tuned QMIX trained longer with more seeds, and an analysis of why value-based holders agree less (63–69% against 93–98% for PPO). Recurrent agents as a stretch goal. |
| **January 31, 2027** | Final results write-up in the project repository, with reproduction commands and all evaluation files committed. |

Every week: a project update and a STEM explainer made with Brutalist (16:9 and 9:16), a weekly presentation deck in the fellows folder (from December 1), a Frictional log entry and an `HOURS.md` record.

---

## Outstanding Issues

- **November 23–30:** hours, videos and log entry are in progress and will be appended.
- **Repository access:** `Nenyax-AI/team-work` is private. The public mirror [sdevanathan96/ant-head-rl-research](https://github.com/sdevanathan96/ant-head-rl-research) holds the same files.
- **Week 1:** I did not attend the weekly meeting.
