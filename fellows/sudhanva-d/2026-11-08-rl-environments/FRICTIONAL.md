# Week 3 Tasks

## 1. RL Environments project update: "Did They Learn It This Time?"

Week-3 update on the [ant-head-rl-research](https://github.com/sdevanathan96/ant-head-rl-research)
code: taking out the scripted cue, why the first cue-free result was still hand-coded, a
timeout bug, and what the ants learned with the bug fixed and more training.

- [16:9 video](https://drive.google.com/file/d/1bYeYnU09Z8kUu756TaAfLYum6PsrVy25/view?usp=sharing)
- [9:16 video](https://drive.google.com/file/d/1EaL7K2FMit_EfwXLpZlWYme6vi4J-RwX/view?usp=sharing)
- Beat sheets: [16:9](ant-head-rl-research/beat_sheet_16x9.json) · [9:16](ant-head-rl-research/beat_sheet_9x16.json)

## 2. STEM explainer: "How IPPO Learns"

How independent PPO works, and how it is wired in the ant-head-rl-research code.

- [16:9 video](https://drive.google.com/file/d/1SRMySOFjF8a7hGapptrkMuDtkzn5o9Ue/view?usp=sharing)
- [9:16 video](https://drive.google.com/file/d/1ous7hAZcaaa1Uxp69Tqf897_8IlOqxZu/view?usp=sharing)
- Beat sheets: [16:9](ippo/beat_sheet_16x9.json) · [9:16](ippo/beat_sheet_9x16.json)
- Sources: Schulman et al. *Proximal Policy Optimization Algorithms.* arXiv 2017. https://arxiv.org/abs/1707.06347 ·
  de Witt et al. *Is Independent Learning All You Need in the StarCraft Multi-Agent Challenge?* arXiv 2020. https://arxiv.org/abs/2011.09533

## Task Subfolders

- [ant-head-rl-research](ant-head-rl-research/)
- [ippo](ippo/)

---

# Work Done This Week: RL Environments

**Cue removed** (`e7cfa42`). Took out the role assignment and the scripted next-step cue.
Each ant now sees its 5×5 window, its own load and a vector pointing home. Reworked the
shaping so it cannot be farmed: the grab bonus is paid once per piece, and progress pays
only on a new closest distance to the nest. At 150k steps on the grid, IPPO rose from 2.52
to 8.00 of 12 and MAPPO from 3.42 to 5.37.

**Check.** That result was mostly hand-coded. The network made two holders' inputs
identical and training shared their exploration noise, so pairs never disagreed (0 of 988
steps). With both aids off, IPPO fell to 4.33.

**Fix and longer training** (`e478b7b`). The PPO rollout did not end episodes at the time
limit, so it bootstrapped into the value of the next episode's start. Fixed it, removed the
hand-coded syncing so each ant acts on its own, and trained for 1M steps instead of 150k.
All 28 tests pass.

| Grid, 3 seeds, 50 held-out episodes | IPPO | MAPPO |
|---|---|---|
| 1M steps, timeout bug left in | 8.64 | 10.27 |
| 1M steps, fixed | 11.77 | 11.48 |
| Free world, 1M steps, fixed | 8.55 | 7.85 |

Re-ran all 12 saved models; every score matched. An untrained network scores 0. Two ants
on one piece see the same view and share weights, so the fair test is trained against
untrained on the same states: they pick the same move 88–97% of the time against 10–12%,
and pull toward the nest 99% of the time against about 40%. In the free world, where one
ant can drag a piece alone, two ants carried most of the way for 66% of IPPO's pieces.
The oracle (`1166e33`) and hand-synced (`e7cfa42`) results are withdrawn (`8f634e1`).

**Next.** Hide one holder's home vector and see whether the pair still agrees. Rerun IQL,
VDN and QMIX with the fixes.

---

# Frictional Log

## 2026-11-08: RL Environments, week 3

- Last week's timeout "fix" was a bug. Since each ant observes the time step, a timeout
  really does end the episode; changing that sent the critic's estimate into the next
  episode. Undoing it helped, but training longer helped more: the old runs stopped at 150k
  steps, just as carrying was taking off.
- The first cue-free score (8/12) still leaned on code that made paired ants act alike.
  Every result now gets an untrained baseline on the same states.

## 2026-11-08: IPPO explainer

- The first script explained IPPO on the cue-based code, which the project then withdrew.
  Rebuilt it on the current code, so every number on screen comes from the trained models.
