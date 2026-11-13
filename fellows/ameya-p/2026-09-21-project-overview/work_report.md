# Fine-Tuning Platform: Brainstorming & Project Overview

---

Volunteer Name: Ameya Padwad  
Report Week: Sep 21 to Sep 25, 2026

## 1. Introduction — The Big Picture

The overall goal is to build a **general-purpose fine-tuning platform** capable of taking:

1. **Any decision model from the Jev or Laya model family**,
2. **Any dataset** (conversational, instruction-style, or domain-specific), and
3. **A set of job specifications** (hyperparameters, training method, output requirements),

...and producing a fine-tuned model as output, with minimal manual intervention per run.

The platform is designed as a **self-contained Training Runtime Worker** — it can run locally via CLI, inside a cloud VM/container (RunPod, Modal, Lambda, AWS), or be invoked as a task by an orchestration queue. A single declarative job specification (JSON/YAML) drives the entire run: which base model to load, which dataset to ingest, which training method to use (e.g., QLoRA, full fine-tuning), and what artifacts to export at the end (LoRA adapter, merged weights, GGUF quantized model, metrics, event logs).

## 2. Overall Structure

### 2.1 System Architecture

The Training Runtime Worker processes a job specification through five stages:

1. **Config & Pre-flight Guard** — Pydantic validation of the job spec, plus GPU/VRAM feasibility checks to prevent out-of-memory failures.
2. **Data Ingestion & Formatting Engine** — parses multiple dataset formats (OpenAI/ShareGPT messages, Alpaca, custom), applies model-specific chat templates, masks loss to assistant-only tokens, and creates train/eval splits.
3. **Model & PEFT Setup** — loads the base model (4-bit QLoRA, 8-bit, or 16-bit LoRA), configures PEFT (rank, alpha, target modules), and applies memory optimizations like gradient checkpointing.
4. **Core SFT Training Engine** — built on Hugging Face TRL's `SFTTrainer` + Accelerate, with a structured event callback streaming live JSON-lines metrics.
5. **Post-Training, Evaluation & Export** — computes validation loss/perplexity, exports the LoRA adapter, optionally merges it into the base model, and optionally quantizes to GGUF for local inference (Ollama/llama.cpp).

The job is driven by a single declarative spec (e.g., `job_config.json`) describing the base model, dataset, training method and hyperparameters, and output/export options. Output artifacts include the adapter, merged model, metrics file, and an event log.

### 2.2 Execution & Delivery Plan

The platform is scoped as a **1-month, 20-day build for 2 engineers**, split by ownership:

- **Engineer 1 (ML & Runtime Lead):** model loading, PEFT/QLoRA, hardware guard, trainer loop, checkpointing, weight exporter.
- **Engineer 2 (Data & Systems Lead):** job schema, data parsing, chat templates, response masking, telemetry/callbacks, CLI/packaging.

The plan proceeds week by week: Week 1 delivers core plumbing and a smoke test; Week 2 delivers the full SFT pipeline with telemetry and export; Week 3 stress-tests across multiple model families (Qwen, Llama, Mistral/Gemma), dataset shapes, and failure modes; Week 4 finalizes testing, containerization (Docker), GGUF export, Hugging Face Hub push, documentation, and a tagged `v1.0.0` release.

The recommended technology stack centers on **Python + Pydantic** for schema/config, **PyTorch + Hugging Face Transformers** for the model core, **TRL's SFTTrainer** for the training loop, **PEFT + bitsandbytes** for LoRA/QLoRA, **Accelerate + FlashAttention-2/SDPA** for hardware efficiency, and **Pytest + Docker** for testing and packaging.

---

## 3. Brainstorming: RL Fine-Tuning Using Calibrated Decisions

While the platform above is built around standard supervised fine-tuning (SFT), a separate line of brainstorming explored how to add a **reinforcement learning (RL) based fine-tuning mode**, specifically one that optimizes for **calibrated decision-making** rather than just task accuracy. This would let the same platform support an RL fine-tuning job type alongside SFT.

### 3.1 Candidate Approaches

Seven approaches were discussed for how the RL reward could enforce calibration:

1. **Proper scoring rule as reward** — use a strictly proper scoring rule (e.g., negative Brier score or log score), computed directly from a decision's confidence and its outcome, as the RL reward. Mathematically guaranteed to be maximized only when stated confidence matches true probability of correctness. Simple, per-sample, no extra model needed — best suited to single-shot/bandit-style decisions.

2. **Composite reward (task utility + calibration penalty)** — blend task reward with a batch-level calibration penalty (e.g., a differentiable ECE surrogate, or a GRPO-style group-level calibration adjustment), useful for sequential/MDP-style decisions.

3. **Two-stage auxiliary reward model** — train a small separate model to predict a calibration-aware reward from `(context, decision, confidence)`, using targets derived from observed calibration statistics. This was explored in the most depth (see below).

4. **Constrained RL (Lagrangian) formulation** — treat calibration as a hard constraint (`ECE(π) ≤ ε`) rather than a soft penalty, using an automatically-tuned Lagrange multiplier instead of a hand-set penalty weight.

5. **Warm start + KL anchor** — first calibrate the base model with a cheap supervised method (temperature scaling, isotonic regression), then RL fine-tune with a KL penalty against that calibrated reference policy to prevent calibration drift during RL.

6. **Offline/batch RL** — since calibration is a population-level statistic, compute it over full batches and use off-policy updates (e.g., batch-constrained methods, or GRPO with large groups) instead of noisy per-episode online updates.

7. **Conformal prediction as a safety layer** — wrap outputs with conformal prediction for distribution-free coverage guarantees, and treat coverage violations as an additional penalty signal, useful when provable guarantees (not just low empirical ECE) are required.

A key open question flagged during this brainstorming: whether "calibrated decisions" means **confidence calibration** (stated probabilities match observed frequencies) or **decision calibration** (the decision-theoretic notion where downstream decisions are optimal given reported probabilities) — the reward design differs depending on which is meant.

### 3.2 Deep Dive: Idea 1 vs. Idea 3

Two of the above approaches were worked through in detail using a running example: a medical triage model deciding "urgent" vs. "not urgent," with a confidence score and ground-truth outcome for each case.

#### Idea 1 — Proper Scoring Rule as Reward

Reward is computed per sample, instantly, with no aggregation:

```
reward = -(confidence - outcome)^2
```

| context    | decision     | confidence | outcome     | reward  |
| ---------- | ------------ | ---------- | ----------- | ------- |
| Case #1023 | "urgent"     | 0.92       | correct (1) | -0.0064 |
| Case #1024 | "not urgent" | 0.60       | correct (1) | -0.16   |
| Case #1025 | "urgent"     | 0.55       | wrong (0)   | -0.3025 |
| Case #1026 | "urgent"     | 0.90       | correct (1) | -0.01   |
| Case #1027 | "not urgent" | 0.85       | wrong (0)   | -0.7225 |

Because the Brier score is a strictly proper scoring rule, its expected value is maximized only when stated confidence equals the true probability of being correct — so calibration emerges statistically over many training samples, without needing to explicitly compute any population-level statistic.

**Tradeoffs:** simple, no separate model or retraining loop — but noisy, since a single binary outcome (right/wrong) can swing the reward heavily even when the underlying confidence level is well-calibrated on average.

#### Idea 3 — Learned Auxiliary Reward Model

Since calibration error is fundamentally a population-level statistic, this approach trains a small auxiliary model to learn the mapping from `(context, decision, confidence)` to a calibration-based reward, using data generated from binning/aggregating real rollout logs.

**Data pipeline:**

1. **Collect rollout logs** — run the model on the dataset, logging `(context, decision, confidence, outcome)` for many samples (e.g., 5,000 triage cases). No new labeling is needed; "outcome" comes from existing ground truth.
2. **Bin by confidence, compute empirical accuracy:**

   | Confidence bin | # samples | # correct | Empirical accuracy                                       |
   | -------------- | --------- | --------- | -------------------------------------------------------- |
   | 0.5–0.6        | 420       | 210       | 0.50                                                     |
   | 0.6–0.7        | 380       | 228       | 0.60                                                     |
   | 0.8–0.9        | 500       | 300       | 0.60 (miscalibrated — model claims ~85%, only right 60%) |
   | 0.9–1.0        | 600       | 570       | 0.95                                                     |

3. **Compute per-sample training targets** using the bin's empirical accuracy:

   ```
   target_reward = -(confidence - empirical_accuracy_of_bin)^2
   ```

   | Confidence bin | # samples | # correct | Empirical accuracy | Target reward |
   | -------------- | --------- | --------- | ------------------ | ------------- |
   | 0.5–0.6        | 420       | 210       | 0.50               | -0.0025       |
   | 0.6–0.7        | 380       | 228       | 0.60               | -0.0025       |
   | 0.8–0.9        | 500       | 300       | 0.60               | -0.0625       |
   | 0.9–1.0        | 600       | 570       | 0.95               | 0.0000        |

4. **Train the auxiliary model** — a small regression model (MLP, gradient-boosted trees, etc.) to predict `target_reward` from `(context, decision, confidence)` via MSE loss.
5. **Use it in the RL loop** — call the trained auxiliary model to get an instant per-sample reward for any new decision sampled during policy fine-tuning (PPO/GRPO).
6. **Periodically refresh** — since the policy's confidence distribution shifts during training, the auxiliary model's learned calibration surface can go stale. Mitigations discussed: iterative retraining (EM-style loop), a KL penalty vs. a reference policy, ensembling multiple auxiliary models, and tracking true ECE on a held-out set as an independent sanity check.

---

## 4. Summary

- The platform's **core job** is to take any Jev/Laya model, any dataset, and a job spec, and produce a fine-tuned model — currently architected around a declarative SFT pipeline (config validation → data ingestion → PEFT/QLoRA setup → SFTTrainer loop → evaluation and export).
- A **parallel brainstorming thread** explored adding an RL-based fine-tuning mode focused on producing **calibrated decisions**, with seven candidate reward-design strategies.
- Two of these — **direct proper scoring rules** and a **learned auxiliary calibration reward model** — were explored in depth, including how to source training data for the auxiliary model from ordinary rollout logs, how to represent decision context, and the tradeoffs of using plain regression versus more robust alternatives (ensembles, classifier-based calibration surfaces).

## 5. Next Steps

With the brainstorming phase complete, the next steps are to move from design into a working prototype. Two concrete workstreams are planned:

### 5.1 Sandbox Framework — Model Loading & Dataset Preprocessing

Build a lightweight sandbox that can:

- **Load a Laya model** (any checkpoint in the family) using the existing model-loading utilities from the SFT pipeline (`worker/model.py`), but configured for inference/rollout rather than training — i.e., no PEFT/QLoRA setup needed yet, just a clean forward pass path for generating decisions and confidence scores.
- **Preprocess a dataset** into the `(context, decision, confidence, outcome)` format needed for RL fine-tuning:
  - Reuse the existing dataset ingestion logic (`worker/dataset.py`) for parsing and chat-template application.
  - Add a new transformation step that extracts/derives ground-truth `outcome` labels from the dataset (correct vs. incorrect, or task-specific reward signal).
  - Add a step to extract or compute `confidence` from the model's output (e.g., via logits, a dedicated confidence head, or a prompted self-reported score).
- **Output a standardized rollout log** (e.g., a JSONL file) matching the schema used throughout the brainstorming examples:

```json
{ "context": "...", "decision": "...", "confidence": 0.85, "outcome": 0 }
```

This sandbox is deliberately decoupled from the full production worker — it's meant for fast iteration on reward design before wiring RL into the main pipeline.

### 5.2 RL Training Script — Brier Score Reward

Implement a first working RL fine-tuning script based on **Idea 1 (proper scoring rule / negative Brier score)**, since it requires no auxiliary model and is the fastest path to an end-to-end working loop:

- **Reward function:**

```python
  def brier_reward(confidence: float, outcome: int) -> float:
      return -(confidence - outcome) ** 2
```

- **Training loop:**
  - Sample decisions from the current policy on batches from the preprocessed dataset.
  - Compute `outcome` for each sampled decision against ground truth.
  - Compute `reward = brier_reward(confidence, outcome)` per sample.
  - Feed rewards into a GRPO or PPO update step (e.g., via TRL's RL trainer utilities) to update the policy.
- **Logging:** extend the existing structured event callback (`worker/callbacks.py`) to stream RL-specific metrics — reward per step, average confidence, and a running calibration curve (bucketed accuracy vs. confidence) for monitoring during training.
- **Validation:** after each epoch (or every N steps), compute ECE on a held-out split to verify that calibration is actually improving, not just reward going up.
