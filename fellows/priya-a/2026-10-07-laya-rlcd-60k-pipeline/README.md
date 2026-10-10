# Week 4 Submission: Laya RLCD 60K Pipeline Validation & GPU Benchmark

**Date:** October 07, 2026  
**Fellow:** Priya Adlakha  
**Collaborator:** Ameya Padwad  
**Hours Logged:** 20.0 Hours ([View Weekly Log](https://github.com/adlakhapriya95/humanitarians-ai-volunteer/blob/main/logs/2026-10-03-to-10-07.md))  

---

## Key Links & Evidence

- **Video Update (1080p, Bella Voiceover):** [JevPipelineUpdate_PriyaA_Week4.mp4](https://github.com/adlakhapriya95/humanitarians-ai-volunteer/blob/main/videos/JevPipelineUpdate_PriyaA_Week4.mp4)
- **Google Colab Live GPU Execution Run:** [Interactive Notebook](https://colab.research.google.com/drive/1-f_4z6xMOl80r9vVW6XgYctxtSSg4w3J#scrollTo=FREK-jHrl1_e)
- **Shared Repository Pull Request:** [AmeyaPadwad/fine_tuner (Branch: feat/strategy-1-pipeline-and-tests)](https://github.com/AmeyaPadwad/fine_tuner/tree/feat/strategy-1-pipeline-and-tests)
- **Full Validation Report:** [`PIPELINE_VALIDATION_REPORT.md`](PIPELINE_VALIDATION_REPORT.md)
- **Frictional Process Record:** [`FRICTIONAL.md`](FRICTIONAL.md)

---

## Executive Summary & Scorecard

Trained the full 60,000 Salesforce xLAM function-calling dataset on an NVIDIA T4 GPU in 66.14 minutes using RLCD Strategy 1 (negative Brier score reward). Evaluated on **12,000 strictly held-out test queries** (20% unseen data):

| Metric | Baseline (Pre-Training) | Fine-Tuned (Full 60K GPU) | Delta Improvement |
| :--- | :---: | :---: | :---: |
| **Accuracy** | **84.85%** | **99.10%** | **+14.25%** (routed 11,892/12,000 correctly) |
| **Precision** | **85.00%** | **99.12%** | **+14.12%** (zero hallucinated tool calls) |
| **Recall / F1** | **84.85% / 84.92%** | **99.10% / 99.11%** | **+14.25% / +14.19%** |
| **Mean Brier Score** | **-0.2505** | **-0.0168** | **+0.2337** (near zero penalty) |
| **Expected Calib Error (ECE)** | **9.98%** | **0.83%** | **-9.15%** (sub-1% calibration error) |
