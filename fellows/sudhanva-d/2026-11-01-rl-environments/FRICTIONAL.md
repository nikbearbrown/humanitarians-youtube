# Week 2 Tasks

## 1. RL Environments project update: "Did the Ants Learn to Cooperate?"

Week-2 update on the [ant-head-rl-research](https://github.com/sdevanathan96/ant-head-rl-research)
code: what was built, why the first runs failed, what fixed them, and a check of what the
12/12 result actually measures.

- 16:9 video: link to be added
- 9:16 video: link to be added
- Beat sheets: [16:9](ant-head-rl-research/beat_sheet_16x9.json) · [9:16](ant-head-rl-research/beat_sheet_9x16.json)

## 2. STEM explainer: "How HyperLogLog Counts"

- 16:9 video: link to be added
- 9:16 video: link to be added
- Beat sheets: [16:9](hyperloglog/beat_sheet_16x9.json) · [9:16](hyperloglog/beat_sheet_9x16.json)
- Source: Flajolet, Fusy, Gandouet, Meunier. *HyperLogLog: the analysis of a near-optimal cardinality estimation algorithm.* AofA 2007.

## Task Subfolders

- [ant-head-rl-research](ant-head-rl-research/)
- [hyperloglog](hyperloglog/)

---

# Work Done This Week: RL Environments

**Built** (`a3196e4`). Two foraging worlds: a grid world, and a free world where the ants'
pulls on a load add up as forces. Six learners: IQL, IQL-team (independent learners on the
shared team reward), VDN, QMIX, IPPO and MAPPO, with tests for the world rules.

**First results** (`a216048`). Every learner collected crumbs (0.50 to 2.25 of 12 food
units per episode), but no pair of ants ever carried a piece home.

**Fixes** (`1166e33`). Four problems: a reward loophole (grab, let go, grab again), ties
between equally short paths home, exploration breaking a hold, and PPO treating a timeout
as a real ending. The same commit added role assignment and a scripted next-step cue in each
ant's observation. On the grid, QMIX, IPPO and MAPPO then deliver 12 of 12 (VDN 11.90,
IQL 7.28, IQL-team 3.77); MAPPO in the free world also scores 12. All 24 tests pass.

**Check.** Re-ran the saved models (3 seeds, 20 held-out episodes each):

| Policy | Grid | Free |
|---|---|---|
| Trained MAPPO, with the cue | 12 | 12 |
| No learning, just follows the cue | 12 | 12 |
| Trained MAPPO, cue blanked | 0 | 0 |

The cue does the cooperating; the trained ants have learned to follow it.

**Next.** Fade the cue out during training, and report the no-learning baseline and the
cue-blanked score next to every result.

---

# Frictional Log

## 2026-11-01: RL Environments, week 2

- The first runs looked like a learning problem but were four environment and training
  bugs. Fixing them, plus the scripted cue, gave 12/12.
- The 12/12 did not hold up: a policy with no learning that follows the cue also scores
  12/12, and the trained ants score 0 without it. Every result now gets that baseline.

## 2026-11-01: HyperLogLog explainer

- Built the explainer on a real HyperLogLog, so every number on screen is measured:
  1,000,000 visitors in 768 bytes came out as 981,148 (−1.9%), and the error followed
  1.04/√m from 16 to 16,384 registers.
- At 10 visitors the raw formula said 742; counting empty registers gave 10.0.
