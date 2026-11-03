# Fellowship Renewal Request — Ameya P.

**Name:** Ameya Padwad  
**Role:** Machine Learning Engineer  
**Project:** Fine tuning using RLCD (`RL Environment` / `AmeyaPadwad/fine_tuner`)  
**Current agreement dates:** 09/14/2026 to 10/31/2026 (September 14, 2026 – October 31, 2026)  
**Requested renewal dates:** 11/01/2026 to 01/31/2027 (November 1, 2026 – January 31, 2027 · 3 months)  
**Fellows folder:** [fellows/ameya-p](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/ameya-p)

---

## Completed

1. **RLCD Fine-Tuning Runtime & 60k xLAM Validation:** Built the modular RLCD training pipeline (`helper.py`, `models.py`, `reward_strategies/`, `rl_training.py`) using GRPO and Brier proper scoring rewards, raising `convaiinnovations/laya` routing accuracy from ~73% to 99.10% (0.83% ECE) on `Salesforce/xlam-function-calling-60k`. **Contribution:** Sole author of the pipeline code and GPU validation runs. **Evidence:** [Repo](https://github.com/AmeyaPadwad/fine_tuner) · [Commit `b3c6513`](https://github.com/AmeyaPadwad/fine_tuner/commit/b3c6513) · [Week 3 Report](../2026-10-05-xlam-laya-validation/work_report.md)
2. **Model/Dataset-Agnostic Pipeline & Post-Hoc Calibration Bake-Off:** Added automatic schema inference (`processing.py`), unified loaders for 5 decision models (`models.py`), an 8-run multi-GPU benchmark suite, and a 4-strategy post-hoc calibration tournament that cut subjective-task ECE by 73% (<5% final ECE in <2s on CPU) with zero accuracy loss. **Contribution:** Sole engineer of the agnostic modules, benchmark runs, and calibration tournament. **Evidence:** [Commit `acf4851`](https://github.com/AmeyaPadwad/fine_tuner/commit/acf4851) · [Commit `7babb8c`](https://github.com/AmeyaPadwad/fine_tuner/commit/7babb8c) · [Week 4 Report](../2026-10-12-agnostic-calibration-benchmarks/work_report.md) · [Week 5 Report](../2026-10-19-post-hoc-calibration-agent-sdk/work_report.md)
3. **Autonomous Agent SDK (`rlcd`), Skill (`SKILL.md`), & 5 Brutalist 4K Videos:** Packaged the `rlcd` Python SDK, `rlcd-fine-tune` CLI, and `skills/rlcd-fine-tune/SKILL.md` (verified end-to-end by an isolated AI agent across a 3-phase GPU test suite), and produced 5 weekly Brutalist 4K reels with full logs. **Contribution:** Packaged the SDK/CLI, authored `SKILL.md`, and produced all 5 reels. **Evidence:** [Commit `6ce866d`](https://github.com/AmeyaPadwad/fine_tuner/commit/6ce866d) · [Commit `07d36c7`](https://github.com/AmeyaPadwad/fine_tuner/commit/07d36c7) · [Drive Videos](https://drive.google.com/drive/folders/1gH4FUFMF_hLI9aItdn7q8SeatKn2BRNc) · [Fellows Folder](../README.md)

---

## Hours Status

**20+ hours documented for every reported week** across Weeks 1–5 (**114.5 hours total**: Week 1 = 21.0 hrs, Week 2 = 24.0 hrs, Week 3 = 21.5 hrs, Week 4 = 23.5 hrs, Week 5 = 24.5 hrs). Every week meets or exceeds the 20-hour minimum and includes documented engineering/research work, Brutalist video production, and weekly team/supervisor meetings (see [HOURS.md](../HOURS.md) and each week's per-folder `HOURS.md`). No missing or incomplete records for Weeks 1–5; the final week of the current agreement (October 26–31, 2026) is in progress at the time of writing.

---

## Weekly Evidence Index

| Week / dates                       | Actual hours | Video links                                                                                                                                                                                                                       | Log and work evidence                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------- | -----------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Week 1** · Sep 21 – Sep 25, 2026 |         21.0 | [Project Overview Video (16:9)](https://drive.google.com/file/d/1gnYaMmkuXmg6rN2-qe5dR_NawbfcE5Jh/view?usp=drive_link) · [Drive Folder](https://drive.google.com/drive/folders/1gH4FUFMF_hLI9aItdn7q8SeatKn2BRNc)                 | [Frictional log](../2026-09-21-project-overview/FRICTIONAL.md) · [Work report](../2026-09-21-project-overview/work_report.md) · [Weekly hours](../2026-09-21-project-overview/HOURS.md) · [Folder](../2026-09-21-project-overview/)                                                                                                                                                                           |
| **Week 2** · Sep 28 – Oct 4, 2026  |         24.0 | [Laya & RLCD Implementation Video (16:9)](https://drive.google.com/file/d/12uyzcsO7FPG8bhyxweBCAoCdTA_a8whp/view?usp=drive_link) · [Drive Folder](https://drive.google.com/drive/folders/1gH4FUFMF_hLI9aItdn7q8SeatKn2BRNc)       | [Frictional log](../2026-09-28-laya-rlcd-implementation/FRICTIONAL.md) · [Work report](../2026-09-28-laya-rlcd-implementation/work_report.md) · [Weekly hours](../2026-09-28-laya-rlcd-implementation/HOURS.md) · [PR #1 (`b3c6513`)](https://github.com/AmeyaPadwad/fine_tuner/commit/b3c6513)                                                                                                               |
| **Week 3** · Oct 5 – Oct 11, 2026  |         21.5 | [xLAM & Laya Validation Video (16:9)](https://drive.google.com/file/d/18QoVeYQo5DZb1EzCfQrX_jtsI49dC3Zh/view?usp=drive_link) · [Drive Folder](https://drive.google.com/drive/folders/1gH4FUFMF_hLI9aItdn7q8SeatKn2BRNc)           | [Frictional log](../2026-10-05-xlam-laya-validation/FRICTIONAL.md) · [Work report](../2026-10-05-xlam-laya-validation/work_report.md) · [Weekly hours](../2026-10-05-xlam-laya-validation/HOURS.md) · [Folder](../2026-10-05-xlam-laya-validation/)                                                                                                                                                           |
| **Week 4** · Oct 12 – Oct 18, 2026 |         23.5 | [Agnostic Calibration Benchmarks Video (16:9)](https://drive.google.com/file/d/1vSt0JxMK_NULaiTBgMjvm54r55B4b0Qm/view?usp=drive_link) · [Drive Folder](https://drive.google.com/drive/folders/1gH4FUFMF_hLI9aItdn7q8SeatKn2BRNc)  | [Frictional log](../2026-10-12-agnostic-calibration-benchmarks/FRICTIONAL.md) · [Work report](../2026-10-12-agnostic-calibration-benchmarks/work_report.md) · [Weekly hours](../2026-10-12-agnostic-calibration-benchmarks/HOURS.md) · [PR #2 (`acf4851`)](https://github.com/AmeyaPadwad/fine_tuner/commit/acf4851) · [Benchmarks (`2638881`)](https://github.com/AmeyaPadwad/fine_tuner/commit/2638881)     |
| **Week 5** · Oct 19 – Oct 25, 2026 |         24.5 | [Post-Hoc Calibration & Agent SDK Video (16:9)](https://drive.google.com/file/d/1MlWelhpzkbFDfiFVIqieMH__K0b_p_Yr/view?usp=drive_link) · [Drive Folder](https://drive.google.com/drive/folders/1gH4FUFMF_hLI9aItdn7q8SeatKn2BRNc) | [Frictional log](../2026-10-19-post-hoc-calibration-agent-sdk/FRICTIONAL.md) · [Work report](../2026-10-19-post-hoc-calibration-agent-sdk/work_report.md) · [Weekly hours](../2026-10-19-post-hoc-calibration-agent-sdk/HOURS.md) · [Calibration (`7babb8c`)](https://github.com/AmeyaPadwad/fine_tuner/commit/7babb8c) · [SDK & Skill (`6ce866d`)](https://github.com/AmeyaPadwad/fine_tuner/commit/6ce866d) |
| **Total (Weeks 1–5)**              |    **114.5** |                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                               |

---

## Degree Relevance and Supervision

This fellowship directly applies and extends my **Master of Science in Electrical and Computer Engineering** from **Northeastern University** (Boston, MA; graduated December 2025, GPA: 3.76), with a concentration in **Computer Vision, Machine Learning and Algorithms** and graduate coursework in _Reinforcement Learning and Decision Making Under Uncertainty_, _Machine Learning and Pattern Recognition_, _Verifiable Machine Learning_, _Computer Vision_, and _Data Visualization_, as well as graduate research on _Improving Formal Verification Gaps in Neural Network-Based Controllers_. Designing GRPO policy-gradient algorithms with strictly proper scoring rules, optimizing multi-class probabilistic calibration (Brier score, Expected Calibration Error, temperature/Platt/matrix scaling), and verifying autonomous agent execution across neural decision architectures directly exercise my graduate training in reinforcement learning under uncertainty and verifiable machine learning.

**Supervisors:** Dev Shah and Dhruv. Weekly progress, architectural decisions, and benchmark results were reviewed across weekly sync meetings and pull request reviews in [`AmeyaPadwad/fine_tuner`](https://github.com/AmeyaPadwad/fine_tuner).

---

## Authorization

- **Authorization type:** F-1 Post-Completion OPT

---

## Next Period Research & Engineering Plan

**Requested renewal period:** November 1, 2026 – January 31, 2027 (3 months).

**Research focus (Research Frontiers — Open Projects):**  
The current fine-tuning platform project is now complete and concluded. The next three-month period (`November 1, 2026 – January 31, 2027`) will focus on taking up a new, open-ended research question under one of the **Research Frontiers — Open Projects** verticals:

1. **Intelligence Measurement** — Finding capabilities that cannot yet be reliably measured, inventing evaluation methods and benchmarks, testing competing systems, and exposing fundamental limitations.
2. **Learning Environments** — Identifying behaviors worth teaching and building environments, rewards, simulations, and challenges that produce better learning.
3. **Learning Algorithms** — Investigating where existing training methods fail and inventing new optimization techniques, learning rules, or adaptation mechanisms.
4. **Cognitive Architectures** — Exploring how intelligence should be structured across reasoning, memory, planning, and decision-making architectures.
5. **Security & Exploitation** — Investigating weaknesses in real systems, reproducing vulnerabilities in authorized targets, and developing defenses.
6. **Data & Knowledge** — Developing methods to discover, generate, organize, verify, and connect missing, inaccessible, or unreliable information.
7. **Compute & Execution** — Identifying fundamental bottlenecks in computation across compilers, inference, distributed systems, and hardware utilization.
8. **Formal Proof & Verification** — Formalizing mathematical, software, or engineering claims that are difficult to guarantee, constructing proofs or counterexamples, and developing automatic verification methods.

Following the Research Frontiers 5-stage approach (_1. Explore_ a vertical, study existing limitations, identify 3–5 unsolved problems, and obtain lead approval to avoid conflicts or repetition; _2. Choose_ an important, overlooked, or misunderstood problem and form a testable hypothesis; _3. Experiment_ by building, testing ideas, challenging assumptions, and following unexpected findings; _4. Validate_ with reproducible evidence against existing approaches while documenting informative negative results; and _5. Deliver_ reusable knowledge and artifacts), the next period will produce a combination of **`SKILL.md`** specifications, **working artifacts** (code, benchmarks, environments, algorithms, datasets, or prototypes), **research findings**, **learned processes**, and **research reports**.

| Target date                                     | Deliverable                                                                                                                                                                                                                                                                              |
| ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **November 15, 2026** (_Explore & Choose_)      | Select a target Research Vertical, study existing work and limitations, identify 3–5 candidate unsolved problems, obtain lead approval on the chosen research question to avoid conflicts/repetition, and formulate a testable hypothesis.                                               |
| **December 31, 2026** (_Experiment & Validate_) | Build the experimental prototype, benchmark, environment, or algorithm for the selected research question; run iterative experiments against existing baselines; and document empirical findings (including unexpected behavior and negative results).                                   |
| **January 31, 2027** (_Deliver_)                | Complete reproducible validation and deliver the full Research Frontiers output package—reusable `SKILL.md`, working code/artifacts, learned research methodology, and comprehensive research report—alongside weekly Brutalist 4K videos, `FRICTIONAL.md` logs, and `HOURS.md` records. |

---

---
