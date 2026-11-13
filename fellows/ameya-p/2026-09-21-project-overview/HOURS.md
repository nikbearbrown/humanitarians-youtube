# Weekly Hours: Week 1 — Brainstorming & Project Overview

**Project:** Fine tuning using RLCD  
**Collaborative Project Repository:** [AmeyaPadwad/fine_tuner](https://github.com/AmeyaPadwad/fine_tuner)  
**Report:** [Work Report](work_report.md)  
**Friction Log:** [Friction Log](FRICTIONAL.md)  
**Report Week:** Sep 21 to Sep 25, 2026  
**Total Hours:** 21.0 hrs

---

## Weekly Hours Breakdown

| Category | Activity / Task Description | Hours |
|---|---|---:|
| **Architecture & System Design** | Designing the 5-stage declarative Training Runtime Worker (`job_config.json` schema, pre-flight hardware guard, data ingestion, PEFT/LoRA model loading, training execution, and evaluation/export) for Jev and Laya decision models (`convaiinnovations/laya`) | 6.5 |
| **RLCD Mathematical Formulation** | Formulating Reinforcement Learning with Calibrated Decisions (RLCD) and comparing three candidate reward strategies: per-episode Brier / log proper scoring rules ($R = -(c - y)^2$), two-stage learned empirical calibration regressors, and batch-level soft-binned ECE loss | 6.0 |
| **Prototyping & Sandbox Scoping** | Scoping the `worker/` module hierarchy (`config.py`, `preflight.py`, `data.py`, `models.py`, `train_sft.py`, `train_rl.py`, `evaluate.py`, `export.py`) and rollout trajectory logging schema | 3.0 |
| **Brutalist Video Reel Production** | Scripting `beat_sheet.json`, generating Kokoro `am_onyx` narration, typesetting the Brier score equation, and rendering/checking the 8-beat 4K `project-overview` reel (`1:28`) | 2.0 |
| **Documentation** | Authoring the Week 1 Brainstorming Report (`work_report.md`), `FACTCHECK.md`, `SHOTLIST.md`, and `FRICTIONAL.md` | 1.5 |
| **Meetings** | Team onboarding sync, project scoping discussion, and weekly advisor check-in | 2.0 |
| **Total** | | **21.0** |
