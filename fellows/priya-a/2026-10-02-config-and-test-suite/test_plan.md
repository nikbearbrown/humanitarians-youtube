# End-to-End Pipeline Test Plan: RLCD Strategy 1 (Proper Scoring Rule Reward)

**Project:** Generalized Fine-Tuning Pipeline for Jev/Laya Decision Models  
**Objective:** Validate that the pipeline accepts any model in the Laya/Jev family and any arbitrary dataset, training it to produce calibrated decisions using Strategy 1 (Proper Scoring Rule / Negative Brier Score as RL reward).

---

## 1. Overview & Objectives

This test plan defines the testing strategy, test levels, test cases, and verification criteria for the end-to-end training pipeline.

### Core Pipeline Capabilities Being Tested:
1. **Model Agnosticism:** Pipeline must successfully initialize and train any Laya-family model (`laya`, `laya-multilingual`, `laya-typed-decisions`, or local checkpoint paths).
2. **Data Agnosticism:** Pipeline must ingest arbitrary input data structures (raw strings, structured JSON/dict contexts, tabular data) across all decision primitives (`choice`, `score`, `noul`) using configurable column mappings.
3. **Strategy 1 Correctness:** Proper scoring rule (negative Brier score $-(p - y)^2$) behaves as a strictly proper reward, optimizes calibration, and blends stably with cross-entropy loss.
4. **Pipeline Robustness:** Full lifecycle execution (config $\to$ data ingestion $\to$ pre-flight $\to$ RLCD training $\to$ checkpointing $\to$ telemetry logging $\to$ calibration eval) operates without regression.

---

## 2. Test Architecture & Pyramidal Tiers

The test suite is structured into 6 distinct tiers:

```
                  ┌───────────────────────────────┐
                  │ Tier 6: Fault & Stress Tests  │
                  ├───────────────────────────────┤
                  │ Tier 5: Calibration Eval (ECE)│
                  ├───────────────────────────────┤
                  │ Tier 4: End-to-End Smoke Runs │
                  ├───────────────────────────────┤
                  │ Tier 3: Strategy 1 Algorithmic│
                  ├───────────────────────────────┤
                  │ Tier 2: Data Ingestion & Map  │
                  ├───────────────────────────────┤
                  │ Tier 1: Config & Pre-flight   │
                  └───────────────────────────────┘
```

- **Tier 1 (Fast Unit, Offline):** Pure Python schema validation, config serialization, pre-flight math.
- **Tier 2 (Fast Unit, Offline):** Dataset parsing, dict context serialization, column mapping, split ratios.
- **Tier 3 (PyTorch Unit, CPU/MPS):** Brier score math, advantage normalization, gradient propagation, sigma annealing.
- **Tier 4 (Integration, Synthetic Data):** 1–2 epoch pipeline smoke runs with mock Laya agent, checkpointing, telemetry.
- **Tier 5 (Quality & Scientific):** ECE calculation, Brier score tracking, reliability curve generation.
- **Tier 6 (Resilience & Edge Cases):** NaN guards, zero variance, corrupted lines, class imbalance.

---

## 3. Detailed Test Specifications

### Tier 1: Configuration & Pre-Flight Validation (`test_schema.py`, `test_preflight.py`)

| Test ID | Test Case | Input / Condition | Expected Behavior |
| :--- | :--- | :--- | :--- |
| **T1.1** | Valid Config Ingestion | `job_config.example.json` | Parses into `JobSpec` with all fields typed correctly. |
| **T1.2** | Missing Required Fields | Missing `job_id` or `dataset.source_path` | Pydantic `ValidationError` raised with clear path. |
| **T1.3** | Invalid Hyperparameter Ranges | `encoder_lr <= 0`, `batch_size = 0`, `rl_ce_fraction = 1.5` | Validation fails with explicit error message. |
| **T1.4** | Sigma Annealing Invariant | `sigma_final > sigma_init` (e.g. init=0.1, final=1.0) | `ValueError: sigma_final should anneal down from sigma_init`. |
| **T1.5** | Pre-flight Missing Dataset | Non-existent path in `source_path` | `DatasetSpec.path_must_exist` rejects before execution. |
| **T1.6** | Pre-flight VRAM Estimation | 421M parameter model with batch_size 8 vs 64 | Returns proportional estimate; flags if estimated VRAM > available. |

---

### Tier 2: Data Ingestion & Transformation (`test_dataset.py`)

The pipeline must handle **any sort of data**, including structured JSON dictionaries and custom tabular schemas.

| Test ID | Test Case | Input / Condition | Expected Behavior |
| :--- | :--- | :--- | :--- |
| **T2.1** | Dict Context Serialization | `context: {"age": 67, "heart_rate": 118, "category": "chest_pain"}` | Serializes gracefully to string representation rather than crashing with `isinstance(str)` error. |
| **T2.2** | Binary Triage (`choice`/`noul`) | Triage row: `decision: "urgent"`, `outcome: 1` | Correctly identified as target `"urgent"`. |
| **T2.3** | Multi-class Tool Selection | Tool selection row: `options: ["search", "calc"]`, `target: "search"` | Parsed into `DecisionExample` with target index = 0. |
| **T2.4** | Explicit Abstention (Null Target) | `target: null` in choice problem | Parsed with `target = None` (abstain / no-tool call). |
| **T2.5** | Continuous Scale (`score`) | `scale: [0, 5]`, `target: 3.5` | Parsed with valid scale tuple and continuous target float. |
| **T2.6** | Custom Column Mapping | `format: "custom"`, mapping `{"text": "context", "label": "target"}` | Correctly re-maps external dataset columns to canonical fields. |
| **T2.7** | Corrupted / Malformed Lines | Corrupted JSON line in `.jsonl` file | Gracefully reports line number and skips row or raises controlled `DatasetError`. |
| **T2.8** | Train / Eval Split Invariance | Split ratio 0.2 on 100 rows with fixed seed | Exactly 80 train rows, 20 eval rows, non-overlapping. |

---

### Tier 3: Strategy 1 Algorithmic & Mathematical Testing (`test_strategy_1.py`)

Validates the mathematical core of **Strategy 1: Proper Scoring Rule as Reward**.

| Test ID | Test Case | Mathematical Specification | Expected Behavior |
| :--- | :--- | :--- | :--- |
| **T3.1** | Exact Brier Score Formula | $R = -(p - y)^2$<br>Case #1023: $p=0.92, y=1$<br>Case #1024: $p=0.60, y=1$<br>Case #1025: $p=0.55, y=0$<br>Case #1026: $p=0.90, y=1$<br>Case #1027: $p=0.85, y=0$ | Reward equals:<br>Case #1023: **-0.0064**<br>Case #1024: **-0.1600**<br>Case #1025: **-0.3025**<br>Case #1026: **-0.0100**<br>Case #1027: **-0.7225** |
| **T3.2** | Strictly Proper Property | True probability $p^* = 0.8$. Evaluate $\mathbb{E}[R(q)]$ across $q \in [0.1, 1.0]$. | Expected reward $\mathbb{E}[R(q)] = p^*(-(q-1)^2) + (1-p^*)(-(q-0)^2)$ peaks uniquely at $q = 0.8$. |
| **T3.3** | Multi-class Brier Extension | Predicted vector $q \in \mathbb{R}^K$, one-hot $y \in \{0, 1\}^K$:<br>$R = -\sum_{k=1}^K (q_k - y_k)^2$ | Correct reward computed over multi-class distributions. |
| **T3.4** | Advantage Normalization | Rewards $[r_1, \dots, r_S]$ across $S$ perturbation samples | Advantage $A_s = (r_s - \mu) / (\sigma + 10^{-6})$ has mean $\approx 0$ and std $\approx 1$. |
| **T3.5** | Sigma Annealing Schedule | Step $t$ from $0 \to T$: $\sigma_t = \sigma_{init} + (\sigma_{final} - \sigma_{init}) \cdot (t / T)$ | $\sigma_t$ monotonically decreases; $\sigma_0 = \sigma_{init}$, $\sigma_T = \sigma_{final}$. |
| **T3.6** | Loss Blending Interpolation | $\text{Loss} = \alpha \cdot \text{Loss}_{RL} + (1 - \alpha) \cdot \text{Loss}_{CE}$ | $\alpha=0 \implies \text{Loss} = \text{Loss}_{CE}$<br>$\alpha=1 \implies \text{Loss} = \text{Loss}_{RL}$<br>$\alpha=0.5 \implies$ equal blend. |
| **T3.7** | Autograd Gradient Flow | Backward pass on blended loss | Non-zero gradients present on both `encoder` and `head` parameters. No `NaN` or `Inf` in gradients. |

---

### Tier 4: End-to-End Pipeline Smoke Runs (`test_pipeline_e2e.py`)

Exercises the complete lifecycle from CLI/entrypoint to output artifacts.

| Test ID | Test Case | Execution Condition | Expected Output |
| :--- | :--- | :--- | :--- |
| **T4.1** | Mock Agent Full Run | 10 synthetic examples, 2 epochs, batch size 2, CPU execution | Exit code 0; training completes all steps. |
| **T4.2** | Model Checkpointing | `save_checkpoint: true` | Checkpoint directory created containing model weights and config snapshot. |
| **T4.3** | Checkpoint Resumption | Load saved checkpoint into fresh agent | Predictions match saved model within floating-point tolerance ($10^{-5}$). |
| **T4.4** | Telemetry Stream Integrity | Inspect generated `events.jsonl` | File contains one JSON entry per `logging_steps`; fields `step`, `train_loss`, `rl_loss`, `ce_loss`, `reward_mean`, and `lr` are valid numbers. |
| **T4.5** | ONNX Export (Conditional) | `export_onnx: true` (if onnx runtime present) | Output directory contains valid `.onnx` graph. |

---

### Tier 5: Calibration & Scientific Evaluation (`test_calibration_eval.py`)

Verifies that Strategy 1 actually improves model calibration without collapsing predictive utility.

| Metric | Definition | Success Threshold |
| :--- | :--- | :--- |
| **Expected Calibration Error (ECE)** | $\sum_{m=1}^M \frac{\|B_m\|}{N} \|\text{acc}(B_m) - \text{conf}(B_m)\|$ | $\text{ECE}_{\text{fine-tuned}} < \text{ECE}_{\text{base}}$ on held-out split. |
| **Mean Brier Score** | $\frac{1}{N} \sum_{i=1}^N (p_i - y_i)^2$ | Lower on evaluation split post-training. |
| **Accuracy Preservation** | $\frac{\text{correct decisions}}{\text{total decisions}}$ | $\text{Accuracy}_{\text{fine-tuned}} \ge \text{Accuracy}_{\text{base}} - 2\%$ (no collapse to trivial constant predictions). |
| **Abstention Reliability** | In tool selection, cases with $y=\text{null}$ | Mean confidence on correct abstentions $\ge 0.70$; low hallucination rate. |

---

### Tier 6: Resilience, Stress & Failure Handling (`test_resilience.py`)

| Test ID | Scenario | Injected Condition | Expected Behavior |
| :--- | :--- | :--- | :--- |
| **T6.1** | Degenerate Perturbations | Zero variance in reward samples ($r_1 = r_2 = \dots = r_S$) | Denominator guard $(\sigma + 10^{-6})$ prevents divide-by-zero; advantage returns zeros without `NaN`. |
| **T6.2** | Extreme Class Imbalance | Dataset where 100% of samples are "urgent" | Pipeline trains without crashing; calibration reflects true base rate without exploding. |
| **T6.3** | Very Long Context | Input context exceeds `max_seq_length` (e.g. 2000 tokens) | Truncated cleanly to `max_seq_length` without out-of-bounds error. |
| **T6.4** | Empty Dataset File | 0-byte `.jsonl` file | Graceful exit with explicit `DatasetError: dataset file is empty`. |

---

## 4. Test Matrix & Environments

| Test Tier | Environment | Hardware Target | Frequency | Execution Time |
| :--- | :--- | :--- | :--- | :--- |
| **Tier 1 (Schema & Preflight)** | Local / CI | CPU | Every commit | < 2 seconds |
| **Tier 2 (Data Ingestion)** | Local / CI | CPU | Every commit | < 3 seconds |
| **Tier 3 (Strategy 1 Math)** | Local / CI | CPU / MPS | Every commit | < 5 seconds |
| **Tier 4 (Smoke E2E)** | Local / CI | CPU / MPS (Synthetic) | PR / Nightly | < 30 seconds |
| **Tier 5 (Calibration Eval)** | Dev Host / Cloud | GPU / Apple Silicon MPS | Release / Milestone | ~2–5 minutes |
| **Tier 6 (Resilience)** | Local / CI | CPU | Weekly / PR | < 10 seconds |

---

## 5. Execution Instructions

### Running the Full Test Suite:
```bash
# In projects/humanitarians-ai/fine_tuner:
pytest tests/ -v
```

### Running Only Strategy 1 Algorithmic Tests:
```bash
pytest tests/test_strategy_1.py -v
```

### Running Fast Unit Tests (Offline / No PyTorch):
```bash
pytest tests/test_schema.py tests/test_dataset.py tests/test_preflight.py -v
```

---

## 6. Live Cloud GPU Test Run (Google Colab)

The full 60,000-example end-to-end training and evaluation run on Salesforce xLAM was executed on an NVIDIA T4 GPU:
- **Interactive Google Colab Notebook:** [https://colab.research.google.com/drive/1-f_4z6xMOl80r9vVW6XgYctxtSSg4w3J#scrollTo=FREK-jHrl1_e](https://colab.research.google.com/drive/1-f_4z6xMOl80r9vVW6XgYctxtSSg4w3J#scrollTo=FREK-jHrl1_e)
- **Held-Out Test Set (12,000 items):**
  - **Accuracy:** $84.85\% \to \mathbf{99.10\%}$ ($\mathbf{+14.25\%}$)
  - **Mean Brier Score:** $-0.2505 \to \mathbf{-0.0168}$ ($\mathbf{+0.2337}$)
  - **Expected Calibration Error (ECE):** $9.98\% \to \mathbf{0.83\%}$ ($\mathbf{-9.15\%}$, sub-$1\%$)
- **Wall-Clock Runtime:** $3968.21\text{s}$ ($66.14\text{ minutes}$ / $1.1\text{ hours}$)
- **Ablation Study (SFT without RLCD):** Benchmarked on the same held-out test split (saved to `results/ablation_no_rlcd_results.json`), demonstrating that while standard SFT achieves high raw accuracy ($93.33\%$), RLCD is necessary to force calibrated uncertainty ($0.83\%$ ECE at scale) and prevent overconfident routing errors.


