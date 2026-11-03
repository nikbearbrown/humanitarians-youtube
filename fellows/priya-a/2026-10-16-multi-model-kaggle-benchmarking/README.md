# Week 5 Submission: Multi-Model Decision Benchmarking (Cloud GPU)

**Date:** October 16, 2026  
**Fellow:** Priya Adlakha  
**Collaborator:** Ameya Padwad  
**Hours Logged:** 20.0 Hours ([View Weekly Log](https://github.com/adlakhapriya95/humanitarians-ai-volunteer/blob/main/logs/2026-10-12-to-10-16.md))  

---

## Deliverables & Key Evidence

- **Week 5 Video Update (1080p, Bella Voiceover):** [JevPipelineUpdate_PriyaA_Week5.mp4](https://github.com/adlakhapriya95/humanitarians-ai-volunteer/blob/main/videos/JevPipelineUpdate_PriyaA_Week5.mp4)
- **Consolidated Master Benchmark Report:** [`CONSOLIDATED_BENCHMARK_RESULTS.md`](CONSOLIDATED_BENCHMARK_RESULTS.md)
- **Executed Multi-Model Kaggle GPU Notebook:** [`rlcd_kaggle_benchmark_executed.ipynb`](rlcd_kaggle_benchmark_executed.ipynb)
- **Raw Benchmark CSV:** [`typical_small_4datasets_benchmark.csv`](typical_small_4datasets_benchmark.csv)
- **Frictional Process Record:** [`FRICTIONAL.md`](FRICTIONAL.md)

---

## Summary of Accomplishments (20.0 Hours)
1. **Architecture Discussions (1.0 hr):** Sync calls with Ameya aligning on multi-model `DecisionModel` architecture and Kaggle dual-T4 distributed benchmarking.
2. **Brutalist Video Production (1.5 hrs):** Authored Week 5 video script, generated Bella (`af_bella`) narration, and rendered 1080p video update.
3. **Multi-Model Decision Architecture & Code Audit (5.5 hrs):** Audited `kaggle_benchmarking` branch, fixed hardcoded `DEVICE="cuda"` CPU crash, added `--device` CLI flag, and verified `MarkerDecisionModelWrapper`.
4. **Kaggle GPU Benchmarking on `Typical-Small` (6.0 hrs):** Executed distributed benchmark across 4 datasets on 2x T4 GPUs. Surged Toxic-Chat accuracy to 94.88% (+94.49%), cut ECE to 0.50% on Sentiment, 0.36% on Anthropic, and halved Raven error.
5. **Cross-Model Expansion & Architectural Discovery (6.0 hrs):** Launched benchmark runs for Von and OpenDecision AI, and documented the fundamental limitation that causal backbones require architecture-aware readout heads for true model agnosticism.
