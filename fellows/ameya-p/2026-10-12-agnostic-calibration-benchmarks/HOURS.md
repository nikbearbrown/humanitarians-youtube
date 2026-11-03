# Weekly Hours: Week 4 — Agnostic Model/Dataset Architecture & Multi-Dataset Calibration Benchmarks

**Project:** Fine tuning using RLCD  
**Collaborative Project Repository:** [AmeyaPadwad/fine_tuner](https://github.com/AmeyaPadwad/fine_tuner)  
**Report:** [Work Report](work_report.md)  
**Friction Log:** [Friction Log](FRICTIONAL.md)  
**Report Week:** Oct 12 to Oct 18, 2026  
**Total Hours:** 23.5 hrs

---

## Weekly Hours Breakdown

| Category | Activity / Task Description | Hours |
|---|---|---:|
| **Dataset-Agnostic Auto-Processing (`rlcd/processing.py`)** | Implementing `auto_prepare_dataset()`, automatic column-role inference, and unified tokenization/splitting across `choice`, `noul`, and `score` decision primitives | 5.5 |
| **Model-Agnostic Loading & Wrapper (`rlcd/models.py`)** | Building the `DecisionModel.load_model()` router and `MarkerDecisionModelWrapper` (`scorer`, `type_emb`, `act_head`) supporting `Laya`, `Von`, `OpenDecision`, `Typical`, and `Decision1` | 5.0 |
| **Multi-Dataset DDP GPU Benchmarking** | Running 8 end-to-end benchmark experiments on Kaggle 2× NVIDIA T4 GPUs (DDP) testing `Typical-small` (~150M) and `Decision 1.0` (600M) across `lmsys/toxic-chat`, `mteb/tweet_sentiment`, `Anthropic/hh-rlhf`, and `NexusRaven_API_eval`, and diagnosing causal-head vs. 3-class ECE behavior | 6.5 |
| **Brutalist Video Reel Production** | Scripting and compiling the 8-beat 4K master cut (`2:13`, Kokoro `af_bella`) with `GATE T` typography verification | 2.5 |
| **Documentation** | Compiling `docs/CONSOLIDATED_BENCHMARK_RESULTS.md`, the Week 4 report (`work_report.md`), and `FRICTIONAL.md` | 1.5 |
| **Meetings** | Weekly fellow sync, benchmark review session, and planning for post-hoc calibration tournament | 2.5 |
| **Total** | | **23.5** |
