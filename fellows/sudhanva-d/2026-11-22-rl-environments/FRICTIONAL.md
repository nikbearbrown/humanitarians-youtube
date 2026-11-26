# Week 5 Tasks

## 1. RL Environments project update: "Why QMIX Collapsed, and Why Sample over Greedy?"

Week-5 update on the ant-foraging code, now in
[Nenyax-AI/team-work](https://github.com/Nenyax-AI/team-work/tree/ant-head-research/projects/learning-environments/ant-foraging):
why QMIX collapsed and how two settings fixed it, why final scores are now sampled, and how the
retuned value-based learners compare with PPO.

- [16:9 video](https://drive.google.com/file/d/1WKsM7oCrWpoegIH3LdKKdMeDZOLAUqDJ/view?usp=sharing)
- [9:16 video](https://drive.google.com/file/d/1dBu1S78Uozv7ub8eK0RsoymXgjoWtI20/view?usp=sharing)
- Beat sheets: [16:9](ant-head-rl-research/beat_sheet_16x9.json) · [9:16](ant-head-rl-research/beat_sheet_9x16.json)

## 2. STEM explainer: "Chasing Its Own Guess."

How a target network gives Q-learning a frozen copy to learn toward, how it is wired in the
ant-foraging code, and what our logs show when the copy is synced too often.

- [16:9 video](https://drive.google.com/file/d/1tswge_MZtiulv8O_554tqwXmMlLE5OH8/view?usp=sharing)
- [9:16 video](https://drive.google.com/file/d/1ePoxFQde7ZXdspUD4OLm4s9Xm_Sp7WXE/view?usp=sharing)
- Beat sheets: [16:9](target-networks/beat_sheet_16x9.json) · [9:16](target-networks/beat_sheet_9x16.json)
- Sources: Mnih et al. *Human-level control through deep reinforcement learning.* Nature 518, 2015. https://doi.org/10.1038/nature14236 ·
  van Hasselt et al. *Deep Reinforcement Learning with Double Q-learning.* AAAI 2016. https://arxiv.org/abs/1509.06461

## Task Subfolders

- [ant-head-rl-research](ant-head-rl-research/)
- [target-networks](target-networks/)

---

# Work Done This Week: RL Environments

**New home** (`384d0c9`, `f46147a`). The project moved to `Nenyax-AI/team-work`
(`projects/learning-environments/ant-foraging`, branch `ant-head-research`). `WORK_PROGRESS.md`
maps the old commit IDs to the new ones. The evaluation files of every run, plus ten models, are
committed under `results/fix-compare/`.

**Why QMIX collapsed** (`8d85f5f`). The value-based learners now log the TD prediction and
target, the gradient norm and QMIX's mixer weights. With the target network synced every 500
updates, the team value estimate overshoots early: about 40 on the grid while the team scores
0, and 865,716 in one free-world seed by 500k steps. Syncing every 2,000 updates and halving
the learning rate (2.5e-4) fixed it; in 11 screen runs with the slower sync, the prediction
never passed 10.5. The
defaults are unchanged; the tuned runs pass these settings with `--set`.

**Sampled scores** (`c9369a8`). Final models are now scored with every ant sampling its action
as in training, with greedy scores alongside. Greedy play can deadlock when two holders split,
and it understated free-world IPPO (9.59 sampled, 8.49 greedy). No ranking changed.

| 1M steps, sampled, 50 held-out episodes | Grid food (/12) | Grid pieces (/4) | Free food (/12) | Free paired pieces |
|---|---|---|---|---|
| IPPO | 11.85 | 3.94 | 9.59 | 2.29 |
| MAPPO | 11.61 | 3.82 | 9.43 | 1.96 |
| VDN, tuned | 8.55 | 2.75 | 9.48 | 1.39 |
| QMIX, tuned | 8.44 | 2.60 | 5.47 | 0.53 |
| IQL, tuned | 4.76 | 0.64 | 9.45 | 2.18 |
| IQL-team, tuned | 3.21 | 0 | 5.43 | 0.83 |
| QMIX, default | 0.13 | 0 | 0.41 | 0 |

**Longer training and agreement.** In the free world, IPPO and MAPPO reach 11.49 and 11.41 of
12 at 10M steps. On the grid, IPPO holders' sampled agreement rises from 0.31 to 0.83 over the
first 300k steps, as transport is learned.

**Check.** Re-scored the ten committed models and 64 local ones, greedy and sampled; all 78
scores that have a saved file matched it.

**Next.** Hide one holder's home vector to see whether the pair still agrees, and find a
free-world test that separates cooperative learners from independent ones.

---

# Frictional Log

## 2026-11-22: RL Environments, week 5

- Greedy evaluation was hiding part of PPO's free-world score: two holders that split see nearly
  the same thing on the next step and split again. Sampling, as in training, avoids the deadlock.
- Retuned, IQL, which cannot see its teammates, scores level with PPO in the free world and
  pairs nearly as many pieces as IPPO (2.18 against 2.29). At 1M steps only the grid tells
  cooperative and independent learners apart.

## 2026-11-22: Target networks explainer

- In the free-world QMIX run shown in the video, the prediction and the target stayed within a
  few percent of each other while both climbed from 48 to over 800,000, so a small gap was no
  sign of health. The chart needed a log scale to show the climb at all.
