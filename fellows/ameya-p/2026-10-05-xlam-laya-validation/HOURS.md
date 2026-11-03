# Weekly Hours: Week 3 — End-to-End Validation Report (xLAM Dataset & Laya Model)

**Project:** Fine tuning using RLCD  
**Collaborative Project Repository:** [AmeyaPadwad/fine_tuner](https://github.com/AmeyaPadwad/fine_tuner)  
**Report:** [Work Report](work_report.md)  
**Friction Log:** [Friction Log](FRICTIONAL.md)  
**Report Week:** Oct 5 to Oct 11, 2026  
**Total Hours:** 21.5 hrs

---

## Weekly Hours Breakdown

| Category | Activity / Task Description | Hours |
|---|---|---:|
| **60k xLAM Dataset Preparation & Scaling** | Scaling `helper.py` ingestion, dynamic negative tool distractor sampling, and context-budget reservation across all 60,000 rows of `Salesforce/xlam-function-calling-60k` without clipping `[MASK]` option suffixes | 5.5 |
| **Full-Scale GPU RLCD Fine-Tuning Runs** | Executing end-to-end RLCD training and hyperparameter tuning on `convaiinnovations/laya` using the Brier proper scoring rule reward and post-training temperature scaling on GPU | 7.5 |
| **Held-Out Evaluation & Calibration Analysis** | Evaluating baseline (~73%) vs. post-RLCD (99.10%) tool-selection accuracy, computing held-out Expected Calibration Error (0.83% ECE), and verifying probability reliability curves | 4.5 |
| **Brutalist Video Reel Production** | Authoring `beat_sheet.json`, generating Kokoro `af_bella` narration on the `humanitarians` Plain register preset, and rendering the 5-beat validation reel (`1:00`) | 2.0 |
| **Meetings** | Weekly team progress review and discussion of multi-model benchmark expansion | 2.0 |
| **Total** | | **21.5** |
