# Fellowship Renewal Report: Aniruddha Chitte

- **Project:** Intervene to Debug (RL Environments)
- **Research vertical:** Causal Science (Nenyax-AI team-work)
- **Repository:** [Nenyax-AI/team-work](https://github.com/Nenyax-AI/team-work) · [Project folder: intervene-to-debug](https://github.com/Nenyax-AI/team-work/tree/main/projects/causal-science/intervene-to-debug)
- **Project approved by:** Dhruv, 2026-11-21
- **Current agreement dates:** 11/04/2026 to 11/30/2026 (November 4, 2026 – November 30, 2026)
- **Requested renewal dates:** 12/01/2026 to 02/28/2027 (December 1, 2026 – February 28, 2027 · 3 months)

## Summary

I explored the Research Frontiers verticals, proposed three project ideas, and had the third approved: a simulated environment that tests whether AI agents find the root cause of system failures faster by running experiments than by reading logs. I set up the project with a README, a research plan and a dated work log, built the simulator, and ran the first test of the hypothesis. When observations are ambiguous, log-reading agents are right only 54–59% of the time, while an experimenting agent is right 100% of the time at about twice the time cost.

Unlike existing agent benchmarks for root cause analysis such as [AIOpsLab](https://arxiv.org/abs/2501.06706) and [Cloud-OpsBench](https://arxiv.org/abs/2603.00468), which measure whether agents find the fault, this project isolates whether running interventions beats passive observation, and at what time cost.

## Completed results

### 1. Project proposal and research plan

Reviewed all 12 research verticals and existing projects to avoid overlap. Proposed a RAG retrieval idea and a prompt-cache reuse idea; both were dropped after PM feedback because existing tools already cover them. Proposed Intervene to Debug, approved on 2026-11-21. Set up the project folder with problem statement, hypothesis, approach, end goal, weekly milestones and a dated work log.

**My contribution:** research, proposals, project design and documentation.

**Evidence:**
- [PR #29: project setup (merged)](https://github.com/Nenyax-AI/team-work/pull/29)
- [README with research plan](https://github.com/Nenyax-AI/team-work/blob/main/projects/causal-science/intervene-to-debug/README.md)
- [WORK_PROGRESS.md (dated work log)](https://github.com/Nenyax-AI/team-work/blob/main/projects/causal-science/intervene-to-debug/WORK_PROGRESS.md)

### 2. Simulator v1 and first finding

Built a seeded multi-service failure simulator (5 services in a dependency graph, one hidden root cause per episode, noisy latency/error/CPU metrics, a misleading CPU decoy) with a Gymnasium interface and tests. Two log-reading baselines over 100 episodes: highest-CPU 45%, highest-latency 100%.

**Finding:** in v1 the root cause could be identified from latency alone, so experiments were not needed. The environment had to be redesigned so observation is ambiguous; otherwise the hypothesis could not be tested.

**Evidence:** [PR #30: simulator v1 (merged)](https://github.com/Nenyax-AI/team-work/pull/30)

### 3. Interventions and first test of the hypothesis

Made observations ambiguous (root cause and affected services share the same latency and error ranges), added a restart intervention (cost 3 time units), a scenario generator with separate held-out test seeds, and an experimenter baseline. 21 tests pass.

| Baseline (100 held-out episodes) | Accuracy | Avg time |
|---|---|---|
| Log-reader (highest CPU) | 54% | 5.0 |
| Log-reader (highest latency) | 59% | 5.0 |
| Experimenter (restart suspects) | 100% | 11.0 |

**Result:** once observations are ambiguous, reading metrics is close to chance, while experimenting finds the true cause in every episode at about twice the time cost. The 100% is an upper bound, because recovery after a restart is currently noise-free; the next milestone adds noisy interventions.

**Evidence:** [PR #33: interventions and ambiguous observations (merged)](https://github.com/Nenyax-AI/team-work/pull/33)

## Related work

These benchmarks evaluate AI agents on root cause analysis in cloud systems. Intervene to Debug differs by isolating one question neither answers directly: whether running interventions beats passive observation, and at what time cost.

- [AIOpsLab: A Holistic Framework to Evaluate AI Agents for Enabling Autonomous Clouds (Microsoft Research, 2025)](https://arxiv.org/abs/2501.06706): deploys microservice environments, injects faults and evaluates LLM agents on operations tasks.
- [Cloud-OpsBench: A Reproducible Benchmark for Agentic Root Cause Analysis in Cloud Systems (2026)](https://arxiv.org/abs/2603.00468): a reproducible benchmark that evaluates active reasoning in agentic root cause analysis across many Kubernetes fault types.

## Weekly evidence index

Full weekly breakdown: [HOURS.md](https://github.com/Aniruddhachitte26/humanitarians-youtube/blob/patch-1/fellows/aniruddha-c/HOURS.md)

| Week / dates | Actual hours | Video links | Log and work evidence |
|---|---|---|---|
| Week 1 · Nov 4 – Nov 11, 2026 | 21 | [Week 1 explainer video](https://drive.google.com/file/d/1tgy-UkSkHna_axOX_RmjclLPoX6nmNaE/view?usp=sharing) | [Week 1 in HOURS.md](https://github.com/Aniruddhachitte26/humanitarians-youtube/blob/patch-1/fellows/aniruddha-c/HOURS.md#week-1--nov-4--nov-11-2026): onboarding, program guidelines, background research |
| Week 2 · Nov 12 – Nov 18, 2026 | 23 | [Week 2 explainer video](https://drive.google.com/file/d/1OUeY3OAgJcQ5Y72yTfvIFELiOX8mDZJo/view?usp=sharing) | [Week 2 in HOURS.md](https://github.com/Aniruddhachitte26/humanitarians-youtube/blob/patch-1/fellows/aniruddha-c/HOURS.md#week-2--nov-12--nov-18-2026) · [Work log](https://github.com/Nenyax-AI/team-work/blob/main/projects/causal-science/intervene-to-debug/WORK_PROGRESS.md#2026-11-14-to-2026-11-20-aniruddha-chitte) |
| Week 3 · Nov 19 – Nov 25, 2026 | 26 | [Week 3 explainer video](https://drive.google.com/file/d/1Yyj6ViYm6AfTT2sHJxdx3F1IDYqRfUxe/view?usp=sharing) | [Week 3 in HOURS.md](https://github.com/Aniruddhachitte26/humanitarians-youtube/blob/patch-1/fellows/aniruddha-c/HOURS.md#week-3--nov-19--nov-25-2026) · [PR #29](https://github.com/Nenyax-AI/team-work/pull/29) · [PR #30](https://github.com/Nenyax-AI/team-work/pull/30) · [PR #33](https://github.com/Nenyax-AI/team-work/pull/33) |
| **Total** | **70** | | |

## Hours status

20+ hours documented for every reported week (70 hours total: Week 1 = 21 hrs, Week 2 = 23 hrs, Week 3 = 26 hrs). Weekly breakdown and evidence are in [HOURS.md](https://github.com/Aniruddhachitte26/humanitarians-youtube/blob/patch-1/fellows/aniruddha-c/HOURS.md).

## Degree relevance and supervision

This project applies my MS in Computer Software Engineering (Northeastern University): distributed systems, simulation, Python software engineering, testing, and AI agent evaluation. Project approved and supervised by Dhruv; progress also reported to Shilpa. Proposal feedback and approval are recorded on Discord, and work is reviewed and merged through GitHub pull requests.

## Next period (December 1, 2026 to February 28, 2027)

| Deliverable | Target date |
|---|---|
| Noisy interventions (partial or failed recovery) and an accuracy-vs-time-budget comparison | 2026-12-06 |
| LLM agents (observe-only vs intervene-enabled) and first-guess anchoring analysis | 2026-12-20 |
| Harder scenarios (multiple causes, delayed effects, unseen failure types) and full experiment runs | 2027-01-10 |
| RL agent trained in the environment (e.g. PPO), compared against the baselines and LLM agents | 2027-01-31 |
| Generalization tests on held-out scenario types and ablations of action costs | 2027-02-14 |
| Final report, SKILL.md and reproducible release of the environment | 2027-02-28 |

## Outstanding issues

- Week 1 (Nov 4 – Nov 11) has no dated work log; its work is described in HOURS.md.
