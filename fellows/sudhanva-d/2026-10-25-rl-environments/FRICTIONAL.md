# Week 1 Tasks

## 1. RL Environments project update: "Training Ants to Work Together"

Research-stage update: what the literature says about training a colony of ant
agents to forage alone and then together. No training code or results are
claimed in this video.

- [16:9 video](https://drive.google.com/file/d/1W0RU7rNXytdmMnjRx0wEdUQBcypBMiyk/view?usp=sharing)
- [9:16 video](https://drive.google.com/file/d/1h4WKTlyP00S6VxXQw7pSk7G03tXGndKw/view?usp=sharing)
- Beat sheets: [16:9](ant-head-rl-research/beat_sheet_16x9.json) · [9:16](ant-head-rl-research/beat_sheet_9x16.json)

## 2. Explainer: "How a Quotient Filter Works"

- [16:9 video](https://drive.google.com/file/d/1lzpGy8k3oCavfzcNAN6R8uq3zieloGu0/view?usp=sharing)
- [9:16 video](https://drive.google.com/file/d/1PNO7YuXYJz4CnzdUDjlBJ_Q9jpJZfghL/view?usp=sharing)
- Beat sheets: [16:9](quotient-filter/beat_sheet_16x9.json) · [9:16](quotient-filter/beat_sheet_9x16.json)

## Task Subfolders

- [ant-head-rl-research](ant-head-rl-research/)
- [quotient-filter](quotient-filter/)

---

# Research Done This Week: RL Environments

**Question.** How should ant agents be trained to forage, first alone and then
cooperating, in a grid world and a free (continuous) world? The jobs are to find
food, bring it home, cut big food into pieces, and carry the pieces home together.

**Findings.**

- **Independent learners hit a ceiling.** They work when an agent can succeed from
  its own view. Tasks that need coordination under partial observability need
  centralised information during training (Papoudakis et al., 2021).
- **Train together, act alone.** VDN sums the per-agent values (Sunehag et al., 2018).
  QMIX mixes them monotonically, ∂Q_tot/∂Q_i ≥ 0 (Rashid et al., 2018). MAPPO uses a
  shared centralised critic (Yu et al., 2022). Parameter sharing helped in the benchmark.
- **Risks.** With sparse rewards, VDN and QMIX did not learn on the benchmark's
  robot-warehouse task. A shared reward invites free riders, so the plan measures
  each ant's share as well as the team total.
- **Environments.** Level-Based Foraging is a grid world that forces cooperative
  loading. The multi-agent particle environments provide a continuous world (Lowe et al., 2017).
- **Real ants.** Groups coordinate transport through the forces in the load, and an
  informed newcomer can steer the group (Feinerman et al., 2018). Ants either cut
  large prey or carry it whole (McCreery & Breed, 2014).

**Plan.** Start with an IQL baseline, then VDN, QMIX and MAPPO with parameter
sharing. Measure team food and each ant's share.

**Sources.**

- Papoudakis, Christianos, Schäfer, Albrecht. *Benchmarking Multi-Agent Deep RL Algorithms in Cooperative Tasks.* NeurIPS 2021 Datasets & Benchmarks. https://arxiv.org/abs/2006.07869
- Sunehag et al. *Value-Decomposition Networks for Cooperative Multi-Agent Learning.* AAMAS 2018.
- Rashid et al. *QMIX: Monotonic Value Function Factorisation for Deep MARL.* ICML 2018. https://arxiv.org/abs/1803.11485
- Yu et al. *The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games.* NeurIPS 2022.
- Lowe et al. *Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments.* NeurIPS 2017.
- Feinerman et al. *The physics of cooperative transport in groups of ants.* Nature Physics 2018.
- McCreery & Breed. *Cooperative transport in ants: a review of proximate mechanisms.* Insectes Sociaux 2014.

---

# Frictional Log

## 2026-10-25: Quotient filter explainer

- Built the explainer on a real quotient filter, so every number on screen is
  measured. At 75% load it gave 0.293% false "maybe"s against 0.292% predicted,
  and it needed 21% more memory than a Bloom filter at equal error, but read
  1 cache line per lookup instead of 10.
- The first cut ran 3.7 minutes; I compressed it to 9 beats (76 s). I also fixed a
  wrong draft line: it is the quotient filter that needs 21% more memory, not the
  Bloom filter 21% less.

## 2026-10-25: RL Environments research update

- Kept this week to research. A quick simulator prototype was stopped, but it showed
  that independently trained ants could max out a too-easy world, so the real
  environments must force cooperation.
