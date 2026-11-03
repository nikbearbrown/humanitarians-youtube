# Fine-Tuning Platform: Implementation Report — Laya Model & RL Fine-Tuning Runtime (RLCD)

---

Volunteer Name: Ameya Padwad  
Report Week: Sep 28 to Oct 4, 2026

## 1. Introduction
Following the initial brainstorming phase documented in `week1 (Sep 21).md`, this work transitions the **Reinforcement Learning with Calibrated Decisions (RLCD)** design into an executable, verified implementation for the **Laya model family** (`convaiinnovations/laya`).

The primary objective is to implement a complete, modular, and self-contained RL fine-tuning pipeline capable of:

1. Ingesting both structured typed-decision benchmarks (e.g., `LocalLLaMA/typed-decisions`) and generic dataset formats (e.g., `Salesforce/xlam-function-calling-60k`).
2. Constructing tokenized sequences and decision marker positions for Laya's encoder-head architecture.
3. Executing a policy gradient RL loop with Group Relative Policy Optimization (GRPO) logit exploration and strictly proper scoring calibration rewards.
4. Performing post-training temperature calibration via L-BFGS optimization on an unbiased, held-out calibration slice.
5. Exporting production-ready Laya agent artifacts (`model.safetensors`, tokenizer, encoder configs, and calibrated `rl_agent_config.json`).
6. Verifying all components with comprehensive, deterministic smoke tests.

The implementation is located under the `rlcd/` package within the workspace.

---

## 2. Overall Architecture & Module Implementation

The implementation is organized into four core modules, a modular reward strategy package, and a unified smoke test harness:

```text
rlcd/
├── .env.example                     # Environment template (HF_TOKEN, DEFAULT_LAYA_MODEL, etc.)
├── helper.py                        # Hugging Face Hub authentication & dataset loading
├── models.py                        # Laya model instantiation & dataset adaptation
├── reward_strategies/               # Modular reward strategies for calibration
│   ├── __init__.py
│   ├── brier.py                     # Brier score proper scoring rule implementation
│   ├── RLCD Reward Strategies.md    # Documentation of proper scoring vs. auxiliary models
│   └── smoke_tests.py               # Deterministic unit tests for reward strategies
├── rl_training.py                   # Full RL fine-tuning engine & evaluation benchmark
└── smoke_tests.py                   # Master smoke test runner across all modules
```

---

### 2.1 Helper Module (`helper.py`)

`helper.py` provides the foundational authentication and data ingestion plumbing:

- **`hf_login()`**: Reads `HF_TOKEN` from the `.env` configuration file and authenticates with Hugging Face Hub. If no token is provided, it falls back gracefully to locally cached credentials without failing, enabling offline and local smoke testing.
- **`load_dataset(dataset_name=None)`**: Loads datasets from Hugging Face Hub or local paths with fallback to `DEFAULT_DATASET_NAME` (`Salesforce/xlam-function-calling-60k`).

---

### 2.2 Model Loading & Data Adaptation (`models.py`)

`models.py` implements the `Laya` namespace class, providing model lifecycle management and dataset schema transformations:

- **`Laya.load_model(model_name=None, device="cpu")`**:
  - Downloads or checks local disk cache (`DEFAULT_CACHE_DIR/laya/<model_name>/`) for the Laya checkpoint.
  - Applies `_fix_tokenizer_config()` to normalize Hugging Face tokenizer configurations.
  - Instantiates `AutoTokenizer` and parses `rl_agent_config.json`.
  - Builds the trainable bidirectional `DecisionModel` (encoder + decision head) using `laya.common.build_model`.
  - Loads model weights from `model.safetensors` with strict parameter checking and moves the model to the requested target device.
- **`Laya.row_to_laya_input(row, context_fn, decision_type="choice", options_fn=None, target_fn=None, scale=None)`**:
  - Translates raw dataset records into Laya's canonical input format:
    $$\{ \text{"context"}: \text{str}, \text{"decision\_type"}: \text{str}, \text{"target"}: \text{Any}, \text{"options"}: \text{list}[\text{str}] \mid \text{None}, \text{"scale"}: \text{tuple} \mid \text{None} \}$$
  - Validates constraints across the three supported decision primitives:
    - `"choice"`: requires `options_fn`.
    - `"score"`: requires `scale=(min, max)`.
    - `"noul"`: binary assertion decision (always resolved as `[false, true]`).
- **`Laya.prepare_dataset_for_laya()`**:
  - Vectorizes row conversion across Hugging Face `Dataset`/`DatasetDict` objects (using `.map()`) or arbitrary Python iterables.
- **`Laya.prepare_xlam_for_laya(dataset)`**:
  - Domain adapter tailored for `Salesforce/xlam-function-calling-60k`, mapping user tool selection queries into multi-choice decision questions.

---

### 2.3 Reward Strategies (`reward_strategies/brier.py`)

As conceptualized in Week 1, strictly proper scoring rules ensure that an agent's expected reward is mathematically maximized if and only if its reported confidence matches the true empirical probability of correctness.

`reward_strategies/brier.py` implements the **Brier score reward strategy** (Idea 1):

- **Individual Reward Formulation**:
  $$R(\hat{p}, y) = -(\hat{p} - y)^2$$
  where $\hat{p} \in [0, 1]$ is the model's reported confidence and $y \in \{0, 1\}$ is the ground truth outcome.
- **`Brier.reward(confidence, outcome)`**: Validates input boundaries and returns the per-decision Brier penalty (ranging from $0.0$ for perfect calibration down to $-1.0$).
- **`Brier.batch_reward(rollouts)`**: Scores batches of logged rollouts without modifying rollout order or metadata.
- **`Brier.mean_reward(rollouts)`**: Aggregates batch calibration performance into a single scalar metric trending toward $0.0$.

---

## 3. RL Fine-Tuning Engine (`rl_training.py`)

`rl_training.py` ports and productionizes the Kaggle 2×T4 Laya fine-tuning pipeline (`laya_finetune_typed_decisions_2xT4_kaggle.ipynb`), integrating GRPO-style logit exploration, strictly proper scoring calibration rewards, dual-objective loss formulation, decoupled parameter optimization, post-training temperature fitting, and artifact export.

### 3.1 Job & Hyperparameter Configuration (`RLTrainingConfig`)

Configuration is managed via a strongly typed dataclass:

```python
@dataclass
class RLTrainingConfig:
    model_name_or_path: str = "convaiinnovations/laya"
    output_dir: str = "./laya_finetuned_rl"
    cache_dir: Optional[str] = "./.cache"

    # Token budgets
    max_len: int = 1024
    head_max_len: int = 256
    max_tokens_per_batch: int = 4096
    gradient_checkpointing: bool = True

    # Training & GRPO
    epochs: int = 4
    micro_batch_size: int = 8
    grad_accum_steps: int = 4
    group_size: int = 4         # G logit perturbations per sequence
    lr_encoder: float = 2.5e-5
    lr_head: float = 1.0e-4
    sigma_start: float = 0.4    # Initial exploration noise
    sigma_end: float = 0.1      # Final exploration noise
    ce_weight: float = 1.0      # Soft cross-entropy guidance weight
    act_reg_weight: float = 0.0

    # Reward
    reward_strategy: str = "proper"  # "proper" or "brier"
    w_sph: float = 0.75
    w_rps: float = 1.0

    # Calibration holdout
    calib_max: int = 400
    calib_ratio: float = 0.1
    calib_seed: int = 20260922
    calib_batch_size: int = 16
```

---

### 3.2 Data Collation & Sequence Representation

Laya relies on sequence packing where decision options are marked with `[MASK]` tokens:

`[CLS] <type> question: <instructions> [SEP] [MASK] opt0 [MASK] opt1 ... [SEP] <state> [SEP]`

- **`build_training_item()`**: Preprocesses benchmark records (`state`, `questions`, `gold`) for `choice`, `score`, and `noul` questions.
- **`build_item_from_laya_row()`**: Preprocesses generic rows from `Laya.prepare_dataset_for_laya`.
- **`collate_train_batch()`**: Pads variable-length token IDs, marker positions, and target distributions into batch tensors:
  - `input_ids`: $(B, L)$
  - `attention_mask`: $(B, L)$
  - `marker_pos`: $(B, K_{\max})$
  - `marker_mask`: $(B, K_{\max})$
  - `target`: $(B, K_{\max})$ (soft probability distributions or one-hot targets)
  - `qtype`: $(B,)$ (0: choice, 1: score, 2: noul)
  - `label`: $(B,)$

---

### 3.3 The RL Optimization Step (GRPO + Calibration Reward)

The training step executes the following mathematical sequence:

1. **Forward Pass**:
   The model evaluates token representations and gathers hidden states at the `[MASK]` marker positions:
   $$\text{logits}, \text{act} = \text{model}(X, M_{\text{att}}, P_{\text{marker}}, M_{\text{marker}}, q_{\text{type}})$$

2. **GRPO Logit Perturbation with Zero-Mean Projection**:
   To explore probability distributions without disturbing sequence representations, $G$ perturbations are sampled in logit space:
   $$\epsilon \sim \mathcal{N}(0, \sigma^2), \quad \epsilon \leftarrow \left(\epsilon - \frac{1}{K}\sum_{i=1}^K \epsilon_i\right) \odot M_{\text{marker}}$$
   $$z_g = \text{logits} + \epsilon_g, \quad q_g = \text{softmax}(z_g)$$
   The exploration noise decays linearly across epochs:
   $$\sigma(e) = \sigma_{\text{start}} + (\sigma_{\text{end}} - \sigma_{\text{start}}) \cdot \frac{e}{E - 1}$$

3. **Pluggable Calibration Reward Evaluation**:
   - **Proper Scoring Rule** (`laya.common.proper_reward`):
     $$R(q, y) = \sum_{k} y_k \log q_k + w_{\text{sph}} \frac{y \cdot q}{\|q\|_2} - w_{\text{rps}} \text{RPS}(q, y) \cdot \mathbb{I}(q_{\text{type}} = \text{score})$$
   - **Brier Calibration Reward**:
     $$R_{\text{Brier}}(q, y) = - \sum_{k} (q_k - y_k)^2$$
   - **Advantage Normalization**:
     $$\text{adv}_g = \frac{r_g - \bar{r}}{\text{std}(r) + 10^{-6}}$$

4. **Dual-Objective Policy Gradient & Guidance Loss**:
   $$\log p(z_g \mid \text{logits}) = -\frac{\|z_g - \text{logits}\|^2}{2\sigma^2}$$
   $$\mathcal{L}_{\text{RL}} = - \frac{1}{G} \sum_{g=1}^G \text{adv}_g \cdot \log p(z_g \mid \text{logits})$$
   $$\mathcal{L}_{\text{CE}} = - \sum_{k} y_k \log \text{softmax}(\text{logits})_k$$
   $$\mathcal{L}_{\text{total}} = \frac{\mathcal{L}_{\text{RL}} + \lambda_{\text{CE}} \mathcal{L}_{\text{CE}}}{\text{accum\_steps}} + \lambda_{\text{act}} \|\text{act}\|_1$$

5. **Decoupled Optimizer & Scheduling**:
   - Pretrained encoder parameters are updated with a conservative learning rate ($\eta_{\text{enc}} = 2.5 \times 10^{-5}$).
   - Decision head parameters are updated with a higher learning rate ($\eta_{\text{head}} = 1.0 \times 10^{-4}$).
   - `CosineAnnealingLR` decays learning rates smoothly to $1.0 \times 10^{-6}$.
   - Gradients are clipped to a maximum norm of $1.0$.

---

### 3.4 Post-Training Temperature Calibration

To ensure probability outputs match true probabilities on unseen cases:

1. **Unbiased Holdout**: A calibration slice ($N \le 400$, 10% of items) is withheld using a fixed seed (`20260922`) before worker sharding, ensuring no rank trains on calibration data.
2. **L-BFGS Optimization**:
   For each decision type $t \in \{\text{choice}, \text{score}, \text{noul}\}$, an optimal temperature $T_t = \exp(\theta_t)$ is fitted on logits $Z$ and targets $Y$ by minimizing negative log-likelihood:
   $$\min_{\theta_t} - \frac{1}{N_t} \sum_{i=1}^{N_t} \sum_{k} Y_{ik} \log \text{softmax}\left(\frac{Z_{ik}}{\exp(\theta_t)}\right)$$
3. **Clamping & Export**: Temperatures are clamped into $[T_{\min}, T_{\max}] = [0.5, 3.0]$ and stored in `rl_agent_config.json`.

---

### 3.5 Artifact Packaging & Evaluation

- **Rolling Checkpoint** (`checkpoint_latest/`): Preserves training progress after each epoch (`model.safetensors`, tokenizer, encoder config, and metadata).
- **Final Export Package**: Contains the calibrated agent ready for inference with `laya.Agent(output_dir)`.
- **Benchmark Evaluation** (`evaluate_laya_benchmark()`): Computes the standard evaluation suite:
  - Accuracy (discrete top-1 match)
  - Soft Accuracy ($\sum_k p_k y_k$)
  - Brier Score ($\sum_k (p_k - y_k)^2$)
  - Expected Calibration Error (ECE via 15 probability bins)
  - Score MAE & Within-1-Level accuracy (for ordinal questions)
  - Median inference latency (ms/case)

---

## 4. Verification & Testing (`smoke_tests.py`)

A comprehensive smoke test suite verifies every module:

```bash
# Run all smoke tests across helper, models, and rl_training
python rlcd/smoke_tests.py

# Or run the isolated RL training smoke test
python rlcd/rl_training.py --smoke_test

# Or run the reward strategy smoke test
python rlcd/reward_strategies/smoke_tests.py
```

### 4.1 Test Results Summary

| Test Suite                 | Component Tested             | Verification Target                                                       | Status   |
| :------------------------- | :--------------------------- | :------------------------------------------------------------------------ | :------- |
| **`HelperSmokeTests`**     | `hf_login()`                 | Non-crashing auth with `.env` / cached token fallback                     | **PASS** |
|                            | `load_dataset()`             | Fetch and inspect `Salesforce/xlam-function-calling-60k`                  | **PASS** |
| **`LayaSmokeTests`**       | `Laya.load_model()`          | Fetch & build `convaiinnovations/laya` (safetensors + config)             | **PASS** |
|                            | `prepare_dataset_for_laya()` | Correct shape `{context, decision_type, options, target}`                 | **PASS** |
|                            | `prepare_xlam_for_laya()`    | 100 rows parsed into Laya choice format                                   | **PASS** |
| **`BrierSmokeTests`**      | `Brier.reward()`             | Verified against documented worked example in `RLCD Reward Strategies.md` | **PASS** |
|                            | `Brier.batch_reward()`       | Exact order and reward consistency across 5 rollouts                      | **PASS** |
|                            | `Brier.mean_reward()`        | Exactly matches expected mean reward (`-0.24028`)                         | **PASS** |
| **`RLTrainingSmokeTests`** | `collate_train_batch()`      | Token padding, attention mask, marker position alignment                  | **PASS** |
|                            | `compute_rewards()`          | Brier & proper scoring reward calculation over tensor batches             | **PASS** |
|                            | `fit_one_temp()`             | L-BFGS convergence and temperature clamping ($[0.5, 3.0]$)                | **PASS** |
|                            | `compute_rl_step()`          | Forward pass, GRPO perturbation, policy gradient + CE backward pass       | **PASS** |

All tests pass cleanly on CPU and GPU without missing dependencies or broken assertions.

---

## 5. Summary & Key Takeaways

1. **Unified Pipeline**: The platform now possesses an end-to-end RL fine-tuning pipeline tailored for the Laya model family, complementing the earlier SFT design.
2. **Strict Calibration Guarantees**: By incorporating both Brier score rewards and Laya's native strictly proper scoring rules, fine-tuning directly optimizes confidence calibration rather than uncalibrated overconfident predictions.
3. **Hardware Agnostic**: The training script functions seamlessly on local workstations (CPU/GPU) for testing and development, while supporting multi-GPU distributed execution (`torchrun --nproc_per_node=2`) for Kaggle dual-T4 or cloud cluster runs.
4. **Zero-Defect Test Coverage**: All modules (`helper.py`, `models.py`, `brier.py`, `rl_training.py`, `smoke_tests.py`) are fully validated with automated smoke tests.

---

## 6. Next Steps

With the core RL loop and plumbing verified:

1. **Full-Scale Dual-T4 Training Run**: Launch a full 4-epoch fine-tuning run on Kaggle dual-T4 GPUs or a cloud VM using the 6,000 typed decisions from `LocalLLaMA/typed-decisions`.
2. **Benchmark Comparison Against TypeSafe Jev**: Evaluate the resulting fine-tuned checkpoint against TypeSafe Jev 1.13.0 and ModernBERT baselines to verify parity with the reported Kaggle metrics (Accuracy $\ge 0.72$, ECE $\le 0.15$, Brier $\le 0.15$).
3. **Learned Auxiliary Reward Model (Idea 2)**: Implement the two-stage calibration regressor outlined in `RLCD Reward Strategies.md`, training a small MLP to smooth empirical bin accuracies across decision contexts.
4. **Integration into Production Worker**: Wrap `LayaRLTrainer` into the declarative job configuration specification schema (`job_config.json`) alongside the SFT trainer.
