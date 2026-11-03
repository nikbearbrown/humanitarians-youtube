# Week 1: Fine-Tuning Platform — Brainstorming & Project Overview

**Project:** Fine tuning using RLCD  
**Collaborative Project Repository:** [AmeyaPadwad/fine_tuner](https://github.com/AmeyaPadwad/fine_tuner)  
**Video:** [RL_Environment_AmeyaPadwad](https://drive.google.com/file/d/1gnYaMmkuXmg6rN2-qe5dR_NawbfcE5Jh/view?usp=drive_link)  
**Report:** [Work Report](work_report.md)  
**Friction Log:** [Friction Log](FRICTIONAL.md)  
**Hours Log:** [Weekly Hours](HOURS.md)  
**Report Week:** Sep 21 to Sep 25, 2026

---

## Overview of this week

This week focused on architecting a general-purpose fine-tuning platform for the Jev and Laya decision model families (`convaiinnovations/laya`) and formulating the Reinforcement Learning with Calibrated Decisions (RLCD) methodology. The design defines a declarative 5-stage Training Runtime Worker driven by a single job specification (`job_config.json`)—covering pre-flight hardware checks, schema-aware data ingestion and `[MASK]` tokenization, PEFT/LoRA model setup, training execution, and evaluation/export—while addressing the core calibration problem where standard binary rewards drive models toward overconfident errors. By comparing candidate RL reward formulations (per-episode Brier and log proper scoring rules, two-stage learned empirical calibration regressors, and batch-level soft-binned Expected Calibration Error), this phase established the strictly proper Brier score ($R = -(c - y)^2$) paired with post-training temperature scaling as the foundation for the RLCD runtime.
