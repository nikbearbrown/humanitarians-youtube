# Week 3: Fine-Tuning Platform — End-to-End Validation Report (xLAM Dataset & Laya Model)

**Project:** Fine tuning using RLCD  
**Collaborative Project Repository:** [AmeyaPadwad/fine_tuner](https://github.com/AmeyaPadwad/fine_tuner)  
**Video:** [RL_Environment_AmeyaPadwad](https://drive.google.com/file/d/18QoVeYQo5DZb1EzCfQrX_jtsI49dC3Zh/view?usp=drive_link)  
**Report:** [Work Report](work_report.md)  
**Friction Log:** [Friction Log](FRICTIONAL.md)  
**Hours Log:** [Weekly Hours](HOURS.md)  
**Report Week:** Oct 5 to Oct 11, 2026

---

## Overview of this week

This week validated the Reinforcement Learning with Calibrated Decisions (RLCD) pipeline end to end at scale on GPU using the 60,000-row `Salesforce/xlam-function-calling-60k` tool-selection benchmark and the `convaiinnovations/laya` model. After automatically mapping the xLAM function-calling schema into Laya's `[MASK]` marker sequences and typed candidate options, full-scale RLCD fine-tuning with the Brier proper scoring rule boosted held-out routing accuracy from a ~73% baseline to 99.10% while driving Expected Calibration Error (ECE) down to 0.83%, demonstrating that proper scoring rewards and post-training temperature scaling prevent overconfident misrouting even during sharp accuracy gains.
