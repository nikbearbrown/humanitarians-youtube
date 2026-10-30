# Month-One Renewal Request — Kriti S.


**Modeled request date:** 2026-10-26; authored 2026-10-26. **Group:** RL Environment. **Project:** Memory Architectures for Pi Agent.  
**Current agreement:** 2026-09-21–2026-10-31. **Requested period:** 2026-11-01–2027-01-31 (Three Month Continuation).

---

## Executive Summary

Please consider a three month continuation of the RL Environment research program. Over the initial five-week period (September 21 through October 25, 2026), work progressed from foundational reverse engineering of the Pi coding agent event loop to empirical multi arm evaluations on realistic repository benchmarks, culminating in a clean ablation matrix across 200 software defects. Major technical milestones include:

1. **Architecture & Scoping (Weeks 1–2):** Deconstructed Pi's modular 4-package loop, established an isolated, permanent evaluation environment (`pi_test/iacon_pi/`), and scoped a 6-paradigm cognitive memory taxonomy.
2. **Empirical Benchmarking & Trap Discovery (Week 3):** Deployed a deterministic SQLite WAL memory store; uncovered the *semantic embedding similarity trap* where toy synthetic benchmarks produced 0% lift while realistic SWE-rebench trajectories achieved 50.0% Pass@1.
3. **Subsystem Hooks & In-Flight Backtracking (Week 4):** Engineered runtime lifecycle hooks with dynamic in-flight backtrack buffers, reduced search complexity from $O(b^d)$ to $O(d)$ through negative action pruning, and validated trajectory avoidance across authentic repository defect benchmarks.
4. **Clean E1–E7 Ablation Matrix & Leakage Audits (Week 5):** Audited and resolved an anomalous 100% Pass@1 signal by enforcing strict ground-truth patch isolation; verified progressive gains from baseline E1 (6.5%) up to E7 (63.0% Pass@1) with high statistical significance (McNemar's $p = 1.57 \times 10^{-11}$).

Five completed weekly records document 20 hours each (100 total hours logged contemporaneously). The objective of the requested renewal period (November 1–30, 2026) is to execute **Milestone 1** of the **"Carry the Couch"** cooperative multi-agent reinforcement learning (MARL) program in PyTorch and VMAS: establishing the pinned simulation environment, implementing the parametric Body Design & Budget Module, constructing the 5-level progressive Layout Ladder, and completing baseline scenario transport under a baseline controller, with initial progression into the shared-policy MAPPO training of Milestone 2.

---

## Open the Evidence

### Weekly Project Updates & Hours
- **[Week 1 Project Update](../2026-09-27-week1-project-update/README.md):** Groundwork, Pi agent deep-dive, parameter pinning ([Hours: 20 hrs](../2026-09-27-week1-project-update/weekly_hours.md)).
- **[Week 2 Project Update](../2026-10-04-week2-project-update/README.md):** Phase 0 environment setup, persistent logging, memory architecture finalized ([Hours: 20 hrs](../2026-10-04-week2-project-update/weekly_hours.md)).
- **[Week 3 Project Update](../2026-10-11-week3-project-update/README.md):** SQLite WAL store, SWE-rebench trajectories, 50% Pass@1 ([Hours: 20 hrs](../2026-10-11-week3-project-update/weekly_hours.md)).
- **[Week 4 Project Update](../2026-10-18-week4-project-update/README.md):** Pi subsystem hooks, in-flight backtracking, trajectory benchmarking ([Hours: 20 hrs](../2026-10-18-week4-project-update/weekly_hours.md)).
- **[Week 5 Project Update](../2026-10-25-week5-project-update/README.md):** Clean E1–E7 ablations, leakage resolution, Carry the Couch modules ([Hours: 20 hrs](../2026-10-25-week5-project-update/weekly_hours.md)).

### Topic Explainers & Visual Media
- **[Pi Agent Architecture](../2026-09-27-pi-agent-architecture/README.md):** Procedural while-loop, four thin packages, hook insertion points.
- **[Pi Agent Causal Memory](../2026-10-04-pi-agent-causal-memory/README.md):** 5-slot causal tuple, `beforeToolCall` safety gate, recovery cycles.
- **[Contrastive Episodic Memory](../2026-10-11-contrastive-episodic-memory/README.md):** Trajectory pair alignment, compact delta schema, dreaming consolidation.
- **[Mathematical Counterfactual Learning](../2026-10-18-mathematical-counterfactual-learning/README.md):** Prefix invariance, pivot index $k^*$, dynamic lesson tuples.
- **[Novelty Dampening](../2026-10-25-novelty-dampening/README.md):** Logarithmic access-frequency penalty ($\alpha = 0.15$), diversity without deletion.

---

## Hours and Coverage

- **Documented Total:** 100 hours across 5 complete reporting weeks (20.0 hours/week average), meeting the minimum requirement (20 hrs/week) set forth in Section 2 of the Volunteer Agreement.
- **Breakdown per Week:**
  - Week 1 (Sep 21 – Sep 27): 20 hours (16 engineering + 4 reporting)
  - Week 2 (Sep 28 – Oct 04): 20 hours (16 engineering + 4 reporting)
  - Week 3 (Oct 05 – Oct 11): 20 hours (16 engineering + 4 reporting)
  - Week 4 (Oct 12 – Oct 18): 20 hours (16 engineering + 4 reporting)
  - Week 5 (Oct 19 – Oct 25): 20 hours (16 engineering + 4 reporting)
- **Reporting Period Boundary:** The current agreement concludes on October 31, 2026. The ongoing partial week (October 26–31) is being tracked contemporaneously and will be appended upon period completion. No unverified hours are counted.

---

### Summary of Completed Period (September 21 – October 25, 2026)
- **100 Hours Documented:** 5 consecutive completed weeks at 20 hours/week, fulfilling all OPT volunteer requirements.
- **Key Engineering Deliverables:**
  - Completed reverse-engineering of the Pi coding agent loop and established an auditable execution environment.
  - Implemented high-performance SQLite WAL contrastive episodic storage and pre-execution interception hooks.
  - Engineered dynamic in-flight backtrack buffers and proved search tree complexity reduction ($O(b^d) \to O(d)$) via negative action pruning.
  - Executed the clean E1–E7 ablation matrix across $N=200$ software defects, demonstrating Pass@1 improvement from 6.5% to 63.0% ($p = 1.57 \times 10^{-11}$).
  - Produced 5 weekly progress updates and 5 detailed technical explainer videos using the Brutalist Remotion framework.

---

## Next-Period Goals (November 1, 2026 – November 30, 2026)

### Research Scope: Cooperative MARL ("Carry the Couch")
Develop a multi-agent reinforcement learning system using **VMAS** and **PyTorch**, where identical agents learn to cooperatively transport a couch-shaped load through obstacles, narrow passages, and L-shaped corridors under local observations without predefined roles. The primary research objective is to evaluate whether a shared-parameter policy trained with small teams ($N \in [2, 4]$) can generalize zero-shot to larger teams ($N = 8 \text{ to } 12$) across unseen layouts without retraining.

### Milestone 1: Architecture & Environment Setup 
### Milestone 2 Initiation: Shared-Policy MAPPO Baseline 
### Milestone 3 (Zero-Shot Scaling & Team-Size Transfer)
### Milestone 4 (Skill Packaging & Automated Verification)
