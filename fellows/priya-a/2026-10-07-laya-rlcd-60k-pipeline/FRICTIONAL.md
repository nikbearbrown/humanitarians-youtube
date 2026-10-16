# Frictional Log: Laya RLCD 60K Fine-Tuning Pipeline

**Date:** 2026-10-07  
**Fellow:** Priya Adlakha  
**Workstream:** Pipeline Hardening, Multi-Scale Testing, Cloud GPU Scaling, and SFT Ablation  

---

### 1. What was attempted and expected
Following Ameya's initial commit of the `rlcd` package on GitHub, the objective was to audit the runtime end-to-end, verify mathematical stability on local hardware, and scale to the full 60,000-example Salesforce xLAM function-calling dataset. The expectation was that the training loop would load the base Laya model, train on CPU, and output well-calibrated decisions.

### 2. Where the system resisted (Friction encountered)
1. **Gated Dataset Authentication:** `Salesforce/xlam-function-calling-60k` threw unauthenticated `DatasetNotFoundError` on Hugging Face Hub because the repository is gated.
2. **Path & Environment Crashes:** `DEFAULT_CACHE_DIR` was `None` when unset in `.env`, triggering a `TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'`. Additionally, `training.py` crashed during metric export due to a missing `import json`.
3. **Rigid Schema Hardcoding:** The data loader hardcoded `query`, `tools`, and `answers`, meaning any non-xLAM dataset (such as emergency clinical triage) crashed immediately with `KeyError: 'query'`.
4. **No Test Partition:** The original script lacked a held-out evaluation partition, throwing all non-calibration data into training.
5. **Compute Bottleneck:** Running 600 examples on an 8-core CPU took 17.15 minutes (1.71s/sample), establishing that running the full 60K dataset locally would take nearly 30 hours.

### 3. What was done about it (Resolution)
- Engineered an automated public mirror fallback in `helper.py` to `lockon/xlam-function-calling-60k` (identical verified 60K APIGen rows).
- Fixed environment path fallbacks to `./.cache` and imported `json`.
- Built `auto_prepare_dataset_for_laya()` to dynamically inspect input schemas across function calling, clinical triage, native Laya formats, and generic NLP columns, automatically serializing nested dictionary contexts to prevent tokenizer crashes.
- Implemented `split_dataset_items()` enforcing a strict 80/20 train/test split.
- Moved the workload to an NVIDIA T4 GPU on Google Colab via a 1-click notebook (`run_60k_on_gpu.ipynb`), cutting training time by 18x to 66.14 minutes for all 60,000 examples.
- Conducted a 3-way ablation study (Base vs. SFT vs. RLCD) on held-out test data, proving that while standard SFT boosts raw accuracy, RLCD is the critical mechanism that eliminates overconfident mistakes (dropping ECE to 0.83%).

### 4. What is now understood & what remains open
- **Understood:** The negative Brier score functions as a strictly proper scoring rule that stably regularizes probabilities at scale without hurting accuracy (reaching 99.10% accuracy on 12,000 test queries).
- **Understood:** Local CPU hardware is great for fast smoke testing (30–150 rows), but GPU acceleration is mandatory for full-dataset training.
- **Open:** Further testing across multi-lingual Laya checkpoints and evaluating out-of-distribution domain transfer on medical/finance tasks.
