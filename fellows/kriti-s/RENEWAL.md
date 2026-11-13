# Renewal request — Kriti S.

- **Current agreement:** 21 Sep — 31 Oct 2026
- **Requested period:** 1 Nov 2026 — 31 Jan 2027 (three-month continuation)
- **Project:** Memory Architectures for Pi Agent
- **Repository:** [Agentic Memory](https://github.com/KritiShahi/Agentic_Memory)
- **Group:** RL Environment
- **Request date:** 2026-10-26

## What the current period produced

Six weeks (21 Sep – 31 Oct 2026) took the work from reverse-engineering the Pi coding agent's event loop (weeks 1–2) to a clean ablation matrix across 200 software defects
(week 5), then into Milestone 1 of Carry the Couch (week 6).

Three results:

1. **Clean E1–E7 ablation and leakage audit (week 5).** Traced an anomalous 100% Pass@1 signal to test-patch leakage, rebuilt the oracle boundaries, and reran the matrix:
   Pass@1 rose from 6.5% (E1) to 63.0% (E7), McNemar $p = 1.57 \times 10^{-11}$.
   *My contribution:* the 4-point improvement plan, novelty dampening, the leakage diagnosis, and running the ablation and statistical test.
   Evidence: [week 5 report](./2026-10-25-week5-project-update/README.md#41-the-e1e7-clean-ablation-matrix--experimental-analysis), [video](https://drive.google.com/file/d/1JIj6hXEDv8WmXZKlges4AIuMUXBfKcXT/view?usp=drive_link).
2. **Subsystem hooks and in-flight backtracking (week 4).** Pi hooks with in-flight backtrack buffers and online autonomous harvesting; on 200 held-out defects, Pass@1
   was 30.0% vs. 33.0% for Flat RAG ($p = 0.48$), so reasoning lift remained open.
   *My contribution:* diagnosing the empty `backtrackHistory` gap, building the hooks, the 20/20 train/eval split, and running the 3-arm benchmark.
   Evidence: [week 4 report](./2026-10-18-week4-project-update/README.md#41-in-flight-step--backtrack-tracking-architecture), [video](https://drive.google.com/file/d/1BySmRrefx7ZTTlI1L5-ANm53kYXNf29t/view?usp=drive_link).
3. **SQLite WAL store and the embedding trap (week 3).** Toy synthetic benchmarks showed 0% lift, while 40 SWE-rebench trajectories reached 50.0% Pass@1 with contrastive
   episodic memory vs. 16.7% Flat RAG.
   *My contribution:* test harness validation, synthetic benchmark evaluation and SWE-rebench trajectory auditing.
   Evidence: [week 3 report](./2026-10-11-week3-project-update/README.md#41-multi-arm-benchmark-design), [video](https://drive.google.com/file/d/1HLzwv4mWH19d5tsqY6rGdPTPAQD-VhnE/view?usp=drive_link).


### Evidence

| Week | Report | Video | Hours | Log |
|---|---|---|---|---|
| 1 — groundwork, Pi deep dive, parameter pinning | [report](./2026-09-27-week1-project-update/README.md) | [watch](https://drive.google.com/file/d/1mQ6zEhl8dr_QLyXH6MfGbJpPkcwBrtQS/view?usp=drive_link) | [20](HOURS.md#week-1--2127-sep) | [log](./2026-09-27-week1-project-update/FRICTIONAL.md) |
| 2 — environment setup, persistent logging, memory designs | [report](./2026-10-04-week2-project-update/README.md) | [watch](https://drive.google.com/file/d/1SgdIIJpmpgKTf5gCDyWiZwosWo2TYzNb/view?usp=drive_link) | [20](HOURS.md#week-2--28-sep--4-oct) | [log](./2026-10-04-week2-project-update/FRICTIONAL.md) |
| 3 — SQLite WAL store, SWE-rebench, 50% Pass@1 | [report](./2026-10-11-week3-project-update/README.md) | [watch](https://drive.google.com/file/d/1HLzwv4mWH19d5tsqY6rGdPTPAQD-VhnE/view?usp=drive_link) | [20](HOURS.md#week-3--511-oct) | [log](./2026-10-11-week3-project-update/FRICTIONAL.md) |
| 4 — subsystem hooks, in-flight backtracking | [report](./2026-10-18-week4-project-update/README.md) | [watch](https://drive.google.com/file/d/1BySmRrefx7ZTTlI1L5-ANm53kYXNf29t/view?usp=drive_link) | [20](HOURS.md#week-4--1218-oct) | [log](./2026-10-18-week4-project-update/FRICTIONAL.md) |
| 5 — clean E1–E7 ablation, leakage audit | [report](./2026-10-25-week5-project-update/README.md) | [watch](https://drive.google.com/file/d/1JIj6hXEDv8WmXZKlges4AIuMUXBfKcXT/view?usp=drive_link) | [20](HOURS.md#week-5--1925-oct) | [log](./2026-10-25-week5-project-update/FRICTIONAL.md) |
| 6 — Carry the Couch Milestone 1: VMAS physics, Deep Sets pooling, 8/8 environment tests | [report](./2026-10-31-week-6-project-update/README.md) | [watch](https://drive.google.com/file/d/12M1Yt1ivdba0GYSGlkWkJXk74UzJkaD3/view?usp=drive_link) | [20](HOURS.md#week-6--2631-oct) | [log](./2026-10-31-week-6-project-update/FRICTIONAL.md) |

## Topic explainers

| Week | Topic | Video | Log |
|---|---|---|---|
| [21–27 Sep](./2026-09-27-pi-agent-architecture/README.md) | Pi agent architecture: while-loop, four thin packages, hook points | [video](https://drive.google.com/file/d/12p9n-g-WytTNod9JqK-EiRpuE2CRawxR/view?usp=drive_link) | [log](./2026-09-27-pi-agent-architecture/FRICTIONAL.md) |
| [28 Sep – 4 Oct](./2026-10-04-pi-agent-causal-memory/README.md) | Causal memory: 5-slot causal tuple, `beforeToolCall` safety gate | [video](https://drive.google.com/file/d/1cgrPLyHPYWT5n3w6fxOis5dKi2yYOx8j/view?usp=drive_link) | [log](./2026-10-04-pi-agent-causal-memory/FRICTIONAL.md) |
| [5–11 Oct](./2026-10-11-contrastive-episodic-memory/README.md) | Contrastive episodic memory: trajectory pairs, compact delta schema | [video](https://drive.google.com/file/d/1n1zjI2KAiPpv9AsZGwmAc73u5FFHFhTk/view?usp=drive_link) | [log](./2026-10-11-contrastive-episodic-memory/FRICTIONAL.md) |
| [12–18 Oct](./2026-10-18-mathematical-counterfactual-learning/README.md) | Counterfactual learning: prefix invariance, pivot index $k^*$ | [video](https://drive.google.com/file/d/1UWG-Oooucq-0SzXrK1-eoyOKRRNpSYaq/view?usp=drive_link) | [log](./2026-10-18-mathematical-counterfactual-learning/FRICTIONAL.md) |
| [19–25 Oct](./2026-10-25-novelty-dampening/README.md) | Novelty dampening: logarithmic access penalty ($\alpha = 0.15$) | [video](https://drive.google.com/file/d/1pkT49De-_GHOBI-F6t6xB9HxS_LeuFn1/view?usp=drive_link) | [log](./2026-10-25-novelty-dampening/FRICTIONAL.md) |
| [26–31 Oct](./2026-10-31-deep-sets/README.md) | Deep Sets in multi-agent RL: permutation-invariant sum pooling, $\phi: \mathbb{R}^4 \to \mathbb{R}^{32}$ | [video](https://drive.google.com/file/d/1dYoiJJnA_AUAjisluJ1Ar8t3h_hcg1AO/view?usp=drive_link) | [log](./2026-10-31-deep-sets/FRICTIONAL.md) |

Weekly hours: [HOURS.md](HOURS.md). 120 hours across six weeks (21 Sep – 31 Oct), 20 each
(16 engineering + 4 reporting). Weekly Frictional logs: one per work folder,
listed in [README.md](README.md).

## Plan for the requested period

Milestone 1 of **"Carry the Couch"**, a cooperative multi-agent reinforcement learning (MARL) program in PyTorch and VMAS: a pinned simulation environment, the parametric Body Design & Budget Module, a 5-level progressive Layout Ladder, and baseline transport under a baseline controller, moving into the shared-policy MAPPO training of Milestone 2.

Identical agents learn to carry a couch-shaped load through obstacles, narrow passages and L-shaped corridors from local observations, with no predefined roles. The research
question is whether a shared-parameter policy trained with small teams ($N \in [2, 4]$) generalizes zero-shot to larger teams ($N = 8$ to $12$) on unseen layouts without
retraining.

| Target date | Deliverable |
|---|---|
| 2026-10-31 | **Milestone 1:** architecture and environment setup |
| 2026-11-07 | **Milestone 2:** shared-policy MAPPO baseline |
| 2026-11-14 | **Milestone 3:** zero-shot scaling and team-size transfer |
| 2026-11-28 | **Milestone 4:** skill packaging and automated verification |

## Degree relevance and supervision

- **Degree relevance:** I am employed as AI Engineer at Humanitarians Inc. responsible for applying concepts from my Masters in Applied Machine Learning to design, develop, and evaluate agentic systems.  My duties include designing and implementation of agent workflows as well as developing benchmarks and evaluation frameworks to assess the performance of agents.
- **Supervisor:** Dev, Dhruv and Shilpa

## Authorization

Authorization type and dates are sent privately to HR, not recorded here.
