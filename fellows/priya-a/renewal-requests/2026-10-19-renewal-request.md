# Agreement Renewal Request — Priya Adlakha

**Request Date:** October 22, 2026  
**Fellow:** Priya Adlakha  
**Group:** Decision Models & Fine-Tuning Pipeline / Brutalist Team  
**Institution:** Northeastern University Humanitarian AI 
**Current Agreement Period:** September 16, 2026 – October 30, 2026  
**Requested Action:** Agreement Renewal / Continuation (Duration per Humanitarians AI policy and supervisor discretion)  
**Supervising Faculty / Coordinators:** Prof. Nik Bear Brown, Dev Shah, Dhruv 

---

## 1. Executive Summary

Please consider a continuation of my fellowship appointment with Humanitarians AI following the conclusion of my current agreement on **October 30, 2026**. The extension duration and schedule are left entirely to the discretion of the supervising faculty and organizational policy.

During the initial appointment period through October 30, 2026, I completed 92.0 verified hours across five technical milestones, focusing on architecting, testing, benchmarking, and documenting a generalized, model-agnostic, and data-agnostic fine-tuning pipeline for open-weight bidirectional decision models under RLCD (Reinforcement Learning with Calibrated Decisions — Strategy 1: Negative Brier Score Reward).

Key accomplishments include:
1. **Large-Scale Enterprise Fine-Tuning (Google Colab T4 GPU):** Fine-tuned `convaiinnovations/laya` (421M ModernBERT Large) on 60,000 tool selection records (`Salesforce/xlam-function-calling-60k`), driving accuracy from $84.85\% \to \mathbf{99.10\%}$ ($+14.25\%$, 11,892/12,000 correct) while collapsing Expected Calibration Error (ECE) from $9.98\% \to \mathbf{0.83\%}$ (sub-1% calibration).
2. **Multi-Model Cloud GPU Benchmarking (Kaggle Dual NVIDIA T4 GPUs):** Benchmarked `wfzyx/von` (~150M) and `vllm-sr/Decision-1.0-Lex-0.6B` (600M) across four diverse decision primitives (`choice`, `score`, `noul`). Demonstrated massive alignment gains, including slashing safety moderation error on `lmsys/toxic-chat` ($1.28\% \to \mathbf{94.88\%}$ on Von, and $9.65\% \to \mathbf{94.98\%}$ on Decision 1.0) with ECE dropping to $<4\%$.
3. **Diagnosing the Calibration Dilemma & Post-Hoc Calibration Engine:** Uncovered the "coin-flip guessing baseline" on subjective tasks (`Tweet Sentiment` and `Anthropic RLHF`) and diagnosed Cross-Entropy overconfidence. Implemented and empirically verified post-hoc calibration strategies (Temperature Scaling and Platt/Vector Scaling), slashing ECE on subjective tasks from $\sim 17.3\%$ down to $\mathbf{4.76\% - 4.92\%}$ on standard CPU in $<1.5$ seconds with zero accuracy degradation.
4. **Reproducible Pipeline Suite & Documentation:** Authored a complete test suite, consolidated benchmark documentation, published a standalone post-hoc calibration script (`rlcd/run_post_hoc_calibration.py`), submitted PR #232, and generated 1080p Brutalist progress videos for all milestones.

In the upcoming renewal period, the objective is to evolve the pipeline from a static factory into an **autonomous, data-aware self-calibrating decision engine** that dynamically detects class imbalances and automatically selects optimal loss regularization and post-hoc calibration strategies.

---

## 2. Direct Evidence Links

### Core Portfolios & Pull Requests
- **Fellows Portfolio Pull Request:** [nikbearbrown/humanitarians-youtube PR #232](https://github.com/nikbearbrown/humanitarians-youtube/pull/232)
- **Primary Volunteer Code Repository:** [adlakhapriya95/humanitarians-ai-volunteer](https://github.com/adlakhapriya95/humanitarians-ai-volunteer)
- **Collaborative Fine-Tuner Repository:** [AmeyaPadwad/fine_tuner (Branch: `kaggle_benchmarking`)](https://github.com/AmeyaPadwad/fine_tuner/tree/kaggle_benchmarking)
- **Fellowship Weekly Progress Logs (Weeks 1–6):** [humanitarians-ai-volunteer/logs/](https://github.com/adlakhapriya95/humanitarians-ai-volunteer/tree/main/logs)
- **Master Capstone Technical Publication Live on Substack:** [Your Model Got More Accurate after Fine-tuning. Can You Trust Its Confidence?](https://priya413.substack.com/p/your-model-got-more-accurate-after)
- **Autonomous Agent Fine-Tuning Skill:** [`skills/rlcd-fine-tune/SKILL.md`](https://github.com/AmeyaPadwad/fine_tuner/blob/SDK%2Bskill/skills/rlcd-fine-tune/SKILL.md)

### Live GPU Execution Notebooks & Scripts
- **Google Colab Live GPU Run (60K Laya Fine-Tuning):** [Colab Notebook](https://colab.research.google.com/drive/1-f_4z6xMOl80r9vVW6XgYctxtSSg4w3J#scrollTo=FREK-jHrl1_e)
- **Executed Kaggle Dual T4 GPU Notebook (Von 4 Datasets):** [`rlcd_kaggle_benchmark_von_executed.ipynb`](https://github.com/AmeyaPadwad/fine_tuner/blob/kaggle_benchmarking/rlcd/rlcd_kaggle_benchmark_von_executed.ipynb)
- **Executed Kaggle GPU Notebook (Typical / Baseline):** [`rlcd_kaggle_benchmark_executed.ipynb`](https://github.com/AmeyaPadwad/fine_tuner/blob/kaggle_benchmarking/rlcd/rlcd_kaggle_benchmark_executed.ipynb)
- **Reproducible Post-Hoc Calibration Engine:** [`rlcd/run_post_hoc_calibration.py`](https://github.com/AmeyaPadwad/fine_tuner/blob/kaggle_benchmarking/rlcd/run_post_hoc_calibration.py)
- **Empirical Calibration Benchmark CSV:** [`results/post_hoc_calibration_results.csv`](https://github.com/AmeyaPadwad/fine_tuner/blob/kaggle_benchmarking/results/post_hoc_calibration_results.csv)

### Technical Reports & Frictional Logs
- **Consolidated Multi-Model Benchmark Report:** [`CONSOLIDATED_BENCHMARK_RESULTS.md`](https://github.com/adlakhapriya95/humanitarians-ai-volunteer/blob/main/projects/iacon-optimus-tool-selection/docs/CONSOLIDATED_BENCHMARK_RESULTS.md)
- **60K Laya Pipeline Validation Report:** [`PIPELINE_VALIDATION_REPORT.md`](https://github.com/adlakhapriya95/humanitarians-ai-volunteer/blob/main/projects/iacon-optimus-tool-selection/docs/PIPELINE_VALIDATION_REPORT.md)
- **Week 5 Friction Log (Kaggle Timeouts & Desyncs):** [`2026-10-16-multi-model-kaggle-benchmarking/FRICTIONAL.md`](https://github.com/adlakhapriya95/humanitarians-youtube/blob/priya-a/fellows/priya-a/2026-10-16-multi-model-kaggle-benchmarking/FRICTIONAL.md)
- **Week 4 Friction Log (Colab T4 Limits & Data Loaders):** [`2026-10-07-laya-rlcd-60k-pipeline/FRICTIONAL.md`](https://github.com/adlakhapriya95/humanitarians-youtube/blob/priya-a/fellows/priya-a/2026-10-07-laya-rlcd-60k-pipeline/FRICTIONAL.md)

### Video Handoffs (Brutalist Protocol: 1080p, Bella Voiceover)
- **Week 6 Final Capstone Video Update (5m 14s Master Summary):** [JevPipelineUpdate_PriyaA_Week6_FinalSummary.mp4](https://github.com/adlakhapriya95/humanitarians-ai-volunteer/blob/main/videos/JevPipelineUpdate_PriyaA_Week6_FinalSummary.mp4)
- **Week 5 Video Update:** [JevPipelineUpdate_PriyaA_Week5.mp4](https://github.com/adlakhapriya95/humanitarians-ai-volunteer/blob/main/videos/JevPipelineUpdate_PriyaA_Week5.mp4)
- **Week 4 Video Update:** [JevPipelineUpdate_PriyaA_Week4.mp4](https://github.com/adlakhapriya95/humanitarians-ai-volunteer/blob/main/videos/JevPipelineUpdate_PriyaA_Week4.mp4)
- **Week 3 Video Update:** [JevPipelineUpdate_PriyaA.mp4](https://github.com/adlakhapriya95/humanitarians-ai-volunteer/blob/main/videos/JevPipelineUpdate_PriyaA.mp4)

---

## 3. Hours and Weekly Coverage

Total Hours Logged: **112.0 Hours** across six documented weeks through the current appointment (exceeding the mandatory 20.0 hrs/week commitment).

| Week | Date Range | Hours Logged | Focus Area | Evidence Link |
| :---: | :---: | :---: | :--- | :---: |
| **Week 1** | Sept 16 – Sept 18 | 12.0 hrs | Onboarding, agreements, Discord access, Gemma study | [`logs/2026-09-16-to-09-18.md`](https://github.com/adlakhapriya95/humanitarians-ai-volunteer/blob/main/logs/2026-09-16-to-09-18.md) |
| **Week 2** | Sept 21 – Sept 25 | 20.0 hrs | System One decision models, RLCD scope correction | [`logs/2026-09-21-to-09-25.md`](https://github.com/adlakhapriya95/humanitarians-ai-volunteer/blob/main/logs/2026-09-21-to-09-25.md) |
| **Week 3** | Sept 28 – Oct 02 | 20.0 hrs | Config architecture, 6-tier test plan, mock harness | [`logs/2026-09-28-to-10-02.md`](https://github.com/adlakhapriya95/humanitarians-ai-volunteer/blob/main/logs/2026-09-28-to-10-02.md) |
| **Week 4** | Oct 03 – Oct 07 | 20.0 hrs | Full 60K Salesforce xLAM Laya training on Colab T4 | [`logs/2026-10-03-to-10-07.md`](https://github.com/adlakhapriya95/humanitarians-ai-volunteer/blob/main/logs/2026-10-03-to-10-07.md) |
| **Week 5** | Oct 12 – Oct 16 | 20.0 hrs | Multi-model Kaggle Dual T4 benchmarking (Von, Decision 1.0) | [`logs/2026-10-12-to-10-16.md`](https://github.com/adlakhapriya95/humanitarians-ai-volunteer/blob/main/logs/2026-10-12-to-10-16.md) |
| **Week 6** | Oct 19 – Oct 23 | 20.0 hrs | Master capstone, post-hoc calibration, Substack article publication | [`logs/2026-10-19-to-10-23.md`](https://github.com/adlakhapriya95/humanitarians-ai-volunteer/blob/main/logs/2026-10-19-to-10-23.md) |

---

## 4. Work Authorization & Northeastern University OPT Details

- **Student / Fellow:** Priya Adlakha (Northeastern University)
- **Status:** Standard Post-Completion OPT (Ordinary 12-month OPT).
- **Compliance:** Work performed aligns directly with degree field (Computer Science / Artificial Intelligence) at Northeastern University. All hours tracked exceed the mandatory 20.0 hrs/week threshold.
- **Reporting:** In accordance with Humanitarians AI policies, volunteer appointments support standard OPT (not STEM OPT extensions). SEVP updates and university DSO notifications are managed via Northeastern University’s Office of Global Services (OGS).

---

## 5. Next Period Research & Engineering Plan

During the renewed appointment, the engineering roadmap will focus on:
1. **Automated Pipeline Introspection:** Developing a self-adapting pipeline layer that autonomously analyzes input data geometry (detecting class imbalance, label ambiguity, or task primitives) and auto-selects appropriate loss functions (Focal Loss vs. Negative Brier) without manual code modification.
2. **In-Flight & Post-Hoc Calibration Engine Packaging:** Packaging the verified Temperature Scaling and Platt/Vector Scaling modules directly into the primary SDK inference pipeline, allowing downstream enterprise systems to request calibrated probabilities straight out of the box.
3. **Expanding Educational Artifacts & Tutorials:** Developing interactive student notebooks and tutorials based on our published Substack article ([Your Model Got More Accurate after Fine-tuning. Can You Trust Its Confidence?](https://priya413.substack.com/p/your-model-got-more-accurate-after)) detailing the RLCD decision model fine-tuning architecture and empirical results.
4. **Expanding Architecture Benchmarks:** Extending automated benchmarks to the remaining decision models (`Tokz-labs/OpenDecision-Small` and `OzLabs/typical-small`) under headless batch scripts.

---

## 6. Official Submission Notice

*Submitted in accordance with the Humanitarians AI Fellowship renewal protocol. Emailed directly to `hr@humanitarians.ai` and `bear@humanitarians.ai` during official Monday–Wednesday business hours prior to the October 30, 2026 agreement expiration date. Agreements and extension durations are subject to faculty review and approval; agreements are not backdated.*
