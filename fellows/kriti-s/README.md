# Kriti S.

**Role:** AI Engineer **Project:** RL Environment (Memory Architectures for Pi Agent) **Group:** RL Environment **GitHub:** [KritiShahi](https://github.com/KritiShahi) **Last updated:** 2026-10-26 **Drive Folder:** [https://drive.google.com/drive/folders/1NPsodfczXDGIY3LLE0LGyDOh8aWc0-Em?usp=drive_link]

---

## Executive Summary

Kriti Shahi contributes as an AI Engineer on the RL Environment research program at Humanitarians AI Inc., researching cognitive, episodic, and causal memory architectures for the frozen Pi coding agent. Across five completed reporting weeks (September 21 through October 25, 2026), work progressed from reverse-engineering the upstream Pi execution loop and establishing an auditable virtual environment (`pi_test/iacon_pi/`), to deploying a deterministic SQLite WAL memory store, discovering the semantic embedding similarity trap, and engineering pre-execution interception hooks with dynamic in-flight backtrack buffers. The research culminated in an empirical ablation matrix (E1 to E7) across 200 software defects from the public Nebius SWE-rebench dataset, eliminating evaluation test-patch leakage and demonstrating statistically significant Pass@1 scaling from 6.5% to 63.0% (McNemar's $p = 1.57 \times 10^{-11}$). This repository packages five weekly project update reports, five contemporaneous 20-hour weekly hours breakdowns (100 hours total), and topic explainer video artifacts. The next phase is focussed on "Carry the Couch" robotics simulation where identical agents learn to cooperatively transport a couch-shaped load through different layouts in terms of varying complexity

---

## Quick Review

- **[Month-one Markdown renewal request](renewal-requests/2026-10-26-month-one-renewal-request.md):** Formal request for a three month continuation (November 1– January 31, 2026) with full evidence index and submission email.
- **[Every week’s hours and supporting records](weekly-hours/README.md):** Five weekly breakdowns accounting for 100 total hours (20.0 hrs/week average).
- **[Research and next-month deliverables](renewal-requests/2026-10-26-month-one-renewal-request.md#next-period-goals-november-1-2026--november-30-2026):** Carry the Couch embodied robotics simulation, Body Design Module, and 1,000-token context budget enforcement.

---

## Folder Guide and Evidence

| Folder | What is inside |
|---|---|
| [renewal-requests/](renewal-requests/README.md) | Formal three month Renewal Request and submission email |
| [weekly-hours/](weekly-hours/README.md) | Five weekly breakdowns (100 hours total) and evidence index |
| [2026-09-27-week1-project-update/](2026-09-27-week1-project-update/README.md) | Week 1: Pi agent deep dive, groundwork, and memory scoping |
| [2026-10-04-week2-project-update/](2026-10-04-week2-project-update/README.md) | Week 2: Phase 0 environment setup, persistent logging, and finalized memory architectures |
| [2026-10-11-week3-project-update/](2026-10-11-week3-project-update/README.md) | Week 3: SQLite WAL store, SWE-rebench trajectories, and 50% Pass@1 |
| [2026-10-18-week4-project-update/](2026-10-18-week4-project-update/README.md) | Week 4: Pi subsystem hooks, in-flight backtracking, and trajectory benchmarking |
| [2026-10-25-week5-project-update/](2026-10-25-week5-project-update/README.md) | Week 5: Clean E1–E7 ablation matrix, leakage audits, and Carry the Couch modules |
| [2026-09-27-pi-agent-architecture/](2026-09-27-pi-agent-architecture/README.md) | Explainer: Pi Agent 4-package loop architecture |
| [2026-10-04-pi-agent-causal-memory/](2026-10-04-pi-agent-causal-memory/README.md) | Explainer: 5-slot causal memory and `beforeToolCall` safety gate |
| [2026-10-11-contrastive-episodic-memory/](2026-10-11-contrastive-episodic-memory/README.md) | Explainer: Contrastive episodic trajectory pairs and compact delta schema |
| [2026-10-18-mathematical-counterfactual-learning/](2026-10-18-mathematical-counterfactual-learning/README.md) | Explainer: Mathematical foundations of counterfactual divergence and pivot $k^*$ |
| [2026-10-25-novelty-dampening/](2026-10-25-novelty-dampening/README.md) | Explainer: Logarithmic novelty dampening ($\alpha = 0.15$) and diversity without deletion |