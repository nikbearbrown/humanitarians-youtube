# Hours and Weekly Progress: Aniruddha Chitte

- **Project:** Intervene to Debug (RL Environments)
- **Research vertical:** Causal Science (Nenyax-AI team-work)
- **Repository:** [Nenyax-AI/team-work](https://github.com/Nenyax-AI/team-work) · [Project folder: intervene-to-debug](https://github.com/Nenyax-AI/team-work/tree/main/projects/causal-science/intervene-to-debug)
- **Current agreement dates:** 11/04/2026 to 11/30/2026 (November 4, 2026 – November 30, 2026)

## Summary

| Week | Dates | Actual hours | Focus | Evidence |
|---|---|---|---|---|
| Week 1 | Nov 4 – Nov 11, 2026 | 21 | Onboarding, program guidelines and background research | [Week 1 details](#week-1--nov-4--nov-11-2026)|
| Week 2 | Nov 12 – Nov 18, 2026 | 23 | Research exploration and first two proposals | [Work log](https://github.com/Nenyax-AI/team-work/blob/main/projects/causal-science/intervene-to-debug/WORK_PROGRESS.md#2026-11-14-to-2026-11-20-aniruddha-chitte) |
| Week 3 | Nov 19 – Nov 25, 2026 | 26 | Project approval, setup, simulator and first hypothesis test | [PR #29](https://github.com/Nenyax-AI/team-work/pull/29) · [PR #30](https://github.com/Nenyax-AI/team-work/pull/30) · [PR #33](https://github.com/Nenyax-AI/team-work/pull/33) |
| **Total** | | **70** | | |

Related work: [AIOpsLab](https://arxiv.org/abs/2501.06706) · [Cloud-OpsBench](https://arxiv.org/abs/2603.00468). These benchmarks evaluate agents on root cause analysis; this project isolates whether intervening beats observing.

---

## Week 1 · Nov 4 – Nov 11, 2026

**Actual hours:** 21

**Work done:**
- Signed the fellowship agreement and completed onboarding.
- Learned the Fellows program guidelines: weekly work logs, required videos, hours documentation and renewal requirements.
- Studied the Nenyax-AI Research Frontiers program: the 12 research verticals, how projects are proposed, approved and organized, and the project folder rules.
- Researched background literature and found articles across candidate research areas to identify open problems for a project proposal.

**Evidence:** Background reading and program onboarding; no dated log was kept for this week.

## Week 2 · Nov 12 – Nov 18, 2026

**Actual hours:** 23

**Work done:**
- Explored all 12 Research Frontiers verticals and every existing project to avoid overlap.
- Proposed a RAG-based knowledge retrieval idea (Nov 17); dropped after PM feedback because existing document-processing tools already cover it.
- Proposed a prompt-cache reuse idea for agent workloads (Nov 18); dropped after PM feedback because existing tools already cover it.

**Evidence:**
- [Work log: 2026-11-14 to 2026-11-20](https://github.com/Nenyax-AI/team-work/blob/main/projects/causal-science/intervene-to-debug/WORK_PROGRESS.md#2026-11-14-to-2026-11-20-aniruddha-chitte)

---

## Week 3 · Nov 19 – Nov 25, 2026

**Actual hours:** 26

**Work done:**
- **Nov 19:** Proposed Intervene to Debug, a simulated environment that tests whether AI agents find the root cause of system failures faster by running experiments than by reading logs.
- **Nov 21:** Project approved by Dhruv.
- **Nov 22:** Set up the ArkenOS workspace and the project folder with README (problem statement, hypothesis, approach, end goal, plan) and a dated work log.
- **Nov 23:** Built simulator v1: 5 services in a dependency graph, one hidden root cause per seeded episode, noisy metrics, a misleading CPU decoy, a Gymnasium interface and 12 tests. Finding: the root cause could be identified from latency alone (100%), so the environment needed redesign.
- **Nov 25:** Made observations ambiguous and added restart interventions, held-out test seeds and an experimenter baseline (21 tests). On 100 held-out episodes: log-readers 54% and 59%, experimenter 100% at about twice the time cost (upper bound, because interventions are currently noise-free).

**Evidence:**
- [Work log: approval](https://github.com/Nenyax-AI/team-work/blob/main/projects/causal-science/intervene-to-debug/WORK_PROGRESS.md#2026-11-21-aniruddha-chitte)
- [PR #29: project setup, README and work log](https://github.com/Nenyax-AI/team-work/pull/29)
- [PR #30: simulator v1, 12 tests, two baselines](https://github.com/Nenyax-AI/team-work/pull/30)
- [PR #33: interventions, ambiguous observations, held-out seeds, 21 tests](https://github.com/Nenyax-AI/team-work/pull/33)

---

## Related work

These benchmarks evaluate AI agents on root cause analysis in cloud systems. Intervene to Debug differs by isolating one question neither answers directly: whether running interventions beats passive observation, and at what time cost.

- [AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds (Microsoft Research, 2025)](https://arxiv.org/abs/2501.06706): deploys microservice environments, injects faults and evaluates LLM agents on operations tasks.
- [Cloud-OpsBench: A Reproducible Benchmark for Agentic Root Cause Analysis in Cloud Systems (2026)](https://arxiv.org/abs/2603.00468): a reproducible benchmark that evaluates active reasoning in agentic root cause analysis across many Kubernetes fault types.
