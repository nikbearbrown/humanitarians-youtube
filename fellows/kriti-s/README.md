# Kriti S. — Humanitarians AI Fellow

- **Role:** AI Engineer
- **Project:** Memory Architectures for Pi Agent
- **Group:** RL Environment
- **GitHub:** [@KritiShahi](https://github.com/KritiShahi)
- **Repository:** [Agentic Memory] (https://github.com/KritiShahi/Agentic_Memory) 
- **Agreement period:** 21 Sep — 31 Oct 2026
- **Drive:** [project videos folder](https://drive.google.com/drive/folders/1NPsodfczXDGIY3LLE0LGyDOh8aWc0-Em?usp=drive_link)

## Research question

Which memory architectures (cognitive, episodic, causal) make the frozen Pi coding agent solve more real software defects, and can that gain be measured cleanly?

Over five weeks the work moved from reverse-engineering Pi's execution loop and setting up an auditable environment, through a SQLite WAL memory store and the discovery of the semantic embedding similarity trap, to pre-execution interception hooks with in-flight
backtracking. It ended with a clean E1–E7 ablation over 200 held-out software defects from the public Nebius SWE-rebench dataset, after removing test-patch leakage from the evaluation.

## Project work

| Week | Work | Result | Evidence | Log |
|---|---|---|---|---|
| [21–27 Sep](./2026-09-27-week1-project-update/README.md) | Groundwork and experimental design | Six memory types studied, Pi's architectural seams mapped, 5-step experimental plan with baselines, pinned version and token budgets | [video](https://drive.google.com/file/d/1mQ6zEhl8dr_QLyXH6MfGbJpPkcwBrtQS/view?usp=drive_link) · [report](./2026-09-27-week1-project-update/README.md) | [log](./2026-09-27-week1-project-update/FRICTIONAL.md) |
| [28 Sep – 4 Oct](./2026-10-04-week2-project-update/README.md) | Pinned baseline and persistent logging | Pi pinned to one version; runner logs moved to permanent directories; six memory designs scoped (three episodic, three causal) | [video](https://drive.google.com/file/d/1SgdIIJpmpgKTf5gCDyWiZwosWo2TYzNb/view?usp=drive_link) · [report](./2026-10-04-week2-project-update/README.md) | [log](./2026-10-04-week2-project-update/FRICTIONAL.md) |
| [5–11 Oct](./2026-10-11-week3-project-update/README.md) | SQLite WAL store and SWE-rebench evaluation | On 40 SWE-rebench trajectories: 50.0% Pass@1 with contrastive episodic memory vs. 16.7% Flat RAG and 0.0% without memory | [video](https://drive.google.com/file/d/1HLzwv4mWH19d5tsqY6rGdPTPAQD-VhnE/view?usp=drive_link) · [report](./2026-10-11-week3-project-update/README.md) | [log](./2026-10-11-week3-project-update/FRICTIONAL.md) |
| [12–18 Oct](./2026-10-18-week4-project-update/README.md) | Subsystem hooks and in-flight backtracking | Hooks and online harvesting built; 3-arm benchmark on 200 held-out defects: Pass@1 30.0% vs. 33.0% for Flat RAG (p = 0.48) | [video](https://drive.google.com/file/d/1BySmRrefx7ZTTlI1L5-ANm53kYXNf29t/view?usp=drive_link) · [report](./2026-10-18-week4-project-update/README.md) | [log](./2026-10-18-week4-project-update/FRICTIONAL.md) |
| [19–25 Oct](./2026-10-25-week5-project-update/README.md) | Clean E1–E7 ablation and leakage audit | 100% Pass@1 anomaly traced to test-patch leakage; clean run: 6.5% (E1) → 63.0% (E7) on 200 defects, McNemar p = 1.57 × 10⁻¹¹ | [video](https://drive.google.com/file/d/1JIj6hXEDv8WmXZKlges4AIuMUXBfKcXT/view?usp=drive_link) · [report](./2026-10-25-week5-project-update/README.md) | [log](./2026-10-25-week5-project-update/FRICTIONAL.md) |
| [26–31 Oct](./2026-10-31-week-6-project-update/README.md) | Carry the Couch Milestone 1 & physics verification | Custom VMAS 2D planar physics, 8D local perception, DeepSets pooling, private whisper symmetry-breaking, 8/8 environment tests pass (26/26 overall, including Test 6 coupled differential thrust/rotation), 6-category action diagnostics | [video](https://drive.google.com/file/d/12M1Yt1ivdba0GYSGlkWkJXk74UzJkaD3/view?usp=drive_link) · [report](./2026-10-31-week-6-project-update/README.md) | [log](./2026-10-31-week-6-project-update/FRICTIONAL.md) |



## Topic explainers

Research, beat sheets, narration scripts and Remotion scenes are mine; the voice is synthetic (Kokoro `am_onyx`).

| Week | Topic | Evidence | Log |
|---|---|---|---|
| [21–27 Sep](./2026-09-27-pi-agent-architecture/README.md) | Pi agent architecture | [video](https://drive.google.com/file/d/12p9n-g-WytTNod9JqK-EiRpuE2CRawxR/view?usp=drive_link) | [log](./2026-09-27-pi-agent-architecture/FRICTIONAL.md) |
| [28 Sep – 4 Oct](./2026-10-04-pi-agent-causal-memory/README.md) | Causal memory and prevention layers | [video](https://drive.google.com/file/d/1cgrPLyHPYWT5n3w6fxOis5dKi2yYOx8j/view?usp=drive_link) | [log](./2026-10-04-pi-agent-causal-memory/FRICTIONAL.md) |
| [5–11 Oct](./2026-10-11-contrastive-episodic-memory/README.md) | Contrastive episodic memory | [video](https://drive.google.com/file/d/1n1zjI2KAiPpv9AsZGwmAc73u5FFHFhTk/view?usp=drive_link) | [log](./2026-10-11-contrastive-episodic-memory/FRICTIONAL.md) |
| [12–18 Oct](./2026-10-18-mathematical-counterfactual-learning/README.md) | Counterfactual learning, mathematical formalization | [video](https://drive.google.com/file/d/1fSU4r-HLR3fgLTpr5V6PRJH-QhBWUsz4/view?usp=sharing) | [log](./2026-10-18-mathematical-counterfactual-learning/FRICTIONAL.md) |
| [19–25 Oct](./2026-10-25-novelty-dampening/README.md) | Novelty dampening | [video](https://drive.google.com/file/d/1pkT49De-_GHOBI-F6t6xB9HxS_LeuFn1/view?usp=drive_link) | [log](./2026-10-25-novelty-dampening/FRICTIONAL.md) |
| [26–31 Oct](./2026-10-31-deep-sets/README.md) | Deep Sets in Multi-Agent RL | [video](https://drive.google.com/file/d/1dYoiJJnA_AUAjisluJ1Ar8t3h_hcg1AO/view?usp=drive_link) | [log](./2026-10-31-deep-sets/FRICTIONAL.md) |

## Next steps

"Carry the Couch": a cooperative multi-agent reinforcement learning system in **VMAS** and **PyTorch**, where identical agents learn to transport a couch-shaped load through
obstacles, narrow passages and L-shaped corridors, using local observations and no predefined roles. The question is whether a shared-parameter policy trained with small
teams (N = 2–4) generalizes zero-shot to larger teams (N = 8–12) on unseen layouts.

- **Milestone 1:** architecture and environment setup. *(Completed)*
- **Milestone 2:** shared-policy MAPPO baseline.
- **Milestone 3:** zero-shot scaling and team-size transfer.
- **Milestone 4:** skill packaging and automated verification.

## Hours and renewal

- [Weekly hours](HOURS.md)
- [Renewal request](RENEWAL.md)
