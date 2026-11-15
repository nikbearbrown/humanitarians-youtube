# Week 4 Tasks

## 1. RL Environments project update: "Which Ants Carry Together?"

Week-4 update on the [ant-head-rl-research](https://github.com/sdevanathan96/ant-head-rl-research)
code: all six learners in both worlds at 1M steps, a new count of pieces carried in pairs, and
how two ants holding one piece coordinate.

- [16:9 video](https://drive.google.com/file/d/1J9dj7HdDP6suvWiFXkZs_uL8dK1Nd6GV/view?usp=sharing)
- [9:16 video](https://drive.google.com/file/d/1vC2mkYfr6dm9lsm8iUy52Ev045bQgo9k/view?usp=sharing)
- Beat sheets: [16:9](ant-head-rl-research/beat_sheet_16x9.json) · [9:16](ant-head-rl-research/beat_sheet_9x16.json)

## 2. STEM explainer: "One Value, Four Ants"

How value decomposition (VDN and QMIX) splits one team value among agents, and how it is wired
in the ant-head-rl-research code.

- [16:9 video](https://drive.google.com/file/d/1g1ZRvAbBfr3G_dTaR5guYI8z3eTj6qCt/view?usp=sharing)
- [9:16 video](https://drive.google.com/file/d/1curbwG4Zqr1iNL5UhczN2F2p6XzZzjqX/view?usp=sharing)
- Beat sheets: [16:9](value-decomposition/beat_sheet_16x9.json) · [9:16](value-decomposition/beat_sheet_9x16.json)
- Sources: Sunehag et al. *Value-Decomposition Networks for Cooperative Multi-Agent Learning.* AAMAS 2018. https://arxiv.org/abs/1706.05296 ·
  Rashid et al. *QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning.* ICML 2018. https://arxiv.org/abs/1803.11485

## Task Subfolders

- [ant-head-rl-research](ant-head-rl-research/)
- [value-decomposition](value-decomposition/)

---

# Work Done This Week: RL Environments

**All six learners** (`83b3e8b`). Ran IQL, IQL-team, VDN, QMIX, IPPO and MAPPO for 1M steps
in both worlds (5 seeds for IPPO and MAPPO, 3 for the rest). The value-based learners now end
episodes at the time limit too. All 33 tests pass.

| 1M steps, 50 held-out episodes | Grid food (/12) | Grid pieces (/4) | Free food (/12) | Free pieces carried in pairs |
|---|---|---|---|---|
| IPPO | 11.75 | 3.90 | 8.49 | 73% |
| MAPPO | 11.42 | 3.77 | 7.91 | 66% |
| VDN | 5.51 | 1.64 | 6.84 | 47% |
| IQL | 3.29 | 0 | 7.82 | 61% |
| IQL-team | 2.73 | 0 | 3.47 | 32% |
| QMIX | 0.08 | 0 | 0.37 | – |

**Paired carries.** In the free world one ant can drag a piece alone, so IQL, which cannot see
its teammates, nearly matches MAPPO on food. Evaluation now counts a piece as paired when two
ants pulled it for at least half the distance it moved. At 3M steps, IPPO reaches 10.69 of 12.

**Coordination.** The two holders of a piece always see the same view. IPPO and MAPPO holders
pull the same way on 93–94% of grid steps, nearly always toward the nest; most failed pulls are
a lone ant pulling while it waits. With one value output per ant, MAPPO matches IPPO on the grid
(11.75); with the team reward alone, its free-world score roughly halves.

**Check.** Re-scored all 62 saved models; every score matched its log.

**Next.** Find out why QMIX climbs to 3.86 and then collapses, and hide one holder's home vector
to see whether the pair still agrees.

---

# Frictional Log

## 2026-11-15: RL Environments, week 4

- In the free world, team food made IQL look as good as MAPPO even though its ants cannot see
  each other. Counting paired carries was the only way to tell them apart.
- QMIX learned to collect crumbs, peaked at 3.86, then fell to near zero in two of three grid
  seeds. Its training error grew before the collapse; finding the cause is next week's work.

## 2026-11-15: Value decomposition explainer

- Checked the "each ant's best move is the team's best" property on the saved models by scoring
  all 1,296 joint moves on nearly 30,000 states. It held every time.
