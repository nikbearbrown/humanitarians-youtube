# Week 4: Fine-Tuning Platform — Agnostic Model/Dataset Architecture & Multi-Dataset Calibration Benchmarks

**Project:** Fine tuning using RLCD  
**Collaborative Project Repository:** [AmeyaPadwad/fine_tuner](https://github.com/AmeyaPadwad/fine_tuner)  
**Video:** [RL_Environment_AmeyaPadwad](https://drive.google.com/file/d/1vSt0JxMK_NULaiTBgMjvm54r55B4b0Qm/view?usp=drive_link)  
**Report:** [Work Report](work_report.md)  
**Friction Log:** [Friction Log](FRICTIONAL.md)  
**Hours Log:** [Weekly Hours](HOURS.md)  
**Report Week:** Oct 12 to Oct 18, 2026

---

## Overview of this week

This week generalized the RLCD platform into a dataset-agnostic and model-agnostic architecture (`rlcd/processing.py` and `rlcd/models.py`) and benchmarked `Typical-small` (~150M Qwen causal backbone) and `Decision 1.0` (600M Lex backbone) across four diverse datasets (`lmsys/toxic-chat`, `mteb/tweet_sentiment`, `Anthropic/hh-rlhf`, and `NexusRaven_API_eval`) spanning all three decision primitives (`score`, `choice`, and `noul`) on 2× NVIDIA T4 GPUs (DDP). Across all 8 benchmark runs, RLCD improved Mean Brier Score in 8/8 runs and reduced Expected Calibration Error (ECE) in 7/8 runs—including slashing `Typical-small` ECE to 0.50% and 0.36% even when causal-head bottlenecks held accuracy flat—while uncovering that sharp multi-class accuracy gains (`Decision 1.0` jumping $+32.96\%$ on 3-class sentiment) can trigger post-training ECE spikes that require richer post-hoc calibration.
