# Fine-Tuning Platform: Agnostic Model/Dataset Architecture & Multi-Dataset Calibration Benchmarks

---

Volunteer Name: Ameya Padwad  
Report Week: Oct 12 to Oct 18, 2026

## 1. Introduction

Following the successful end-to-end validation of the Reinforcement Learning with Calibrated Decisions (RLCD) pipeline on the xLAM dataset with the Laya model last week, this week focused on two main objectives:

1. Engineering a **dataset-agnostic processing module** (`rlcd/processing.py`) and a **model-agnostic loading module** (`rlcd/models.py`) capable of automatically inferring dataset schemas and loading diverse open-weight decision models into a unified training interface.
2. Conducting empirical multi-task benchmarking on **Typical** (`OzLabs/typical-small`) and **Decision 1.0** (`vllm-sr/Decision-1.0-Lex-0.6B`) across four datasets spanning all three decision primitives (`score`, `choice`, and `noul`) to evaluate cross-architecture accuracy, Brier score, and Expected Calibration Error (ECE).

## 2. Dataset-Agnostic Processing & Model-Agnostic Loading Modules

To decouple the pipeline from any single dataset schema or model architecture, the ingestion and model-loading layers were redesigned to operate automatically:

- **Dataset-Agnostic Auto-Processing (`rlcd/processing.py`):** Implemented `auto_prepare_dataset()` to automatically inspect and sample incoming datasets, infer column roles (context, embedded or JSON candidate options, and target labels), and dynamically map records into **`choice`** (categorical/tool selection), **`noul`** (binary/contrastive safety pairs), or **`score`** (ordinal rating scales). Generalized `prepare_dataset_items()` and `split_dataset_items()` to handle tokenizer-agnostic `[MASK]` / `marker_token_id` sequence packing and reproducible train/calibration/test splits.
- **Model-Agnostic Loading & Wrapping (`rlcd/models.py`):** Built the unified `DecisionModel.load_model()` router with dedicated loaders for `Laya`, `Von`, `OpenDecision`, `Typical`, and `Decision1`. Created `MarkerDecisionModelWrapper` to wrap arbitrary encoder backbones with standardized RLCD marker-readout scoring heads (`scorer`), decision-type embeddings (`type_emb`), and calibration heads (`act_head`).

## 3. Empirical Testing: Typical & Decision 1.0 Across 4 Datasets

Using the new agnostic modules on Kaggle 2x NVIDIA T4 GPUs (DDP), **Typical-small** (~150M, Qwen-based backbone) and **Decision 1.0** (600M, Lex backbone) were evaluated on strictly held-out 20% test splits across four diverse benchmarks (`docs/CONSOLIDATED_BENCHMARK_RESULTS.md`):

| Model               | Dataset (Rows)                  | Primitive |        Baseline $\to$ Final Accuracy        |        Mean Brier Score ($\Delta$)         |           ECE Calibration Error ($\Delta$)           |
| :------------------ | :------------------------------ | :-------: | :-----------------------------------------: | :----------------------------------------: | :--------------------------------------------------: |
| **`Typical-small`** | `lmsys/toxic-chat` (5,082)      |  `score`  | $0.39\% \to \mathbf{94.88\%}$ ($+94.49\%$)  | $-0.9301 \to \mathbf{-0.1024}$ ($+0.8277$) | $25.78\% \to \mathbf{5.11\%}$ ($\mathbf{-20.67\%}$)  |
| **`Typical-small`** | `mteb/tweet_sentiment` (26,732) | `choice`  |      $39.54\% \to 39.54\%$ ($0.00\%$)       | $-0.6715 \to \mathbf{-0.6603}$ ($+0.0111$) |  $8.63\% \to \mathbf{0.50\%}$ ($\mathbf{-8.13\%}$)   |
| **`Typical-small`** | `Anthropic/hh-rlhf` (60,000)    |  `noul`   |      $50.21\% \to 49.79\%$ ($-0.42\%$)      | $-0.5044 \to \mathbf{-0.5000}$ ($+0.0043$) |  $4.67\% \to \mathbf{0.36\%}$ ($\mathbf{-4.31\%}$)   |
| **`Typical-small`** | `NexusRaven_API_eval` (318)     | `choice`  |      $15.87\% \to 15.87\%$ ($0.00\%$)       | $-0.9074 \to \mathbf{-0.8007}$ ($+0.1067$) | $31.14\% \to \mathbf{15.48\%}$ ($\mathbf{-15.66\%}$) |
| **`Decision 1.0`**  | `lmsys/toxic-chat` (5,082)      |  `score`  | $9.65\% \to \mathbf{94.98\%}$ ($+85.33\%$)  | $-0.8272 \to \mathbf{-0.0876}$ ($+0.7396$) | $14.78\% \to \mathbf{4.01\%}$ ($\mathbf{-10.77\%}$)  |
| **`Decision 1.0`**  | `mteb/tweet_sentiment` (26,732) | `choice`  | $46.54\% \to \mathbf{79.50\%}$ ($+32.96\%$) | $-0.6357 \to \mathbf{-0.3687}$ ($+0.2670$) |           $8.04\% \to 17.38\%$ ($+9.33\%$)           |
| **`Decision 1.0`**  | `Anthropic/hh-rlhf` (60,000)    |  `noul`   | $49.14\% \to \mathbf{57.13\%}$ ($+7.98\%$)  | $-0.5132 \to \mathbf{-0.4894}$ ($+0.0238$) |  $6.77\% \to \mathbf{4.45\%}$ ($\mathbf{-2.32\%}$)   |
| **`Decision 1.0`**  | `NexusRaven_API_eval` (318)     | `choice`  | $25.40\% \to \mathbf{58.73\%}$ ($+33.33\%$) | $-0.7754 \to \mathbf{-0.5430}$ ($+0.2324$) | $17.84\% \to \mathbf{12.48\%}$ ($\mathbf{-5.36\%}$)  |

### Key Finding: Consistent Brier & ECE Improvements vs. Architecture-Dependent Accuracy

- **Reliable Calibration & Brier Optimization:** Across nearly all runs, the RLCD Brier reward strategy consistently improved the **Mean Brier Score** (all 8/8 runs) and reduced **Expected Calibration Error (ECE)** (7/8 runs). Even when a model could not improve classification accuracy on hard or ambiguous tasks—such as `Typical-small` on `tweet_sentiment` ($39.54\%$ accuracy) and `Anthropic/hh-rlhf` ($49.79\%$ accuracy)—RLCD slashed ECE down to **$0.50\%$** and **$0.36\%$**, respectively, teaching the model to output honest, balanced probabilities ($\sim 50\%/50\%$) rather than overconfident errors.
- **Why Accuracy Did Not Always Improve:** Unlike bidirectional masked encoders (`Laya`), `Typical-small` uses a Qwen-family causal/autoregressive backbone. Attaching a uniform bidirectional marker-readout head (`MarkerDecisionModelWrapper`) creates a representational bottleneck on complex natural language and multi-function code signatures, limiting accuracy gains even while the Brier reward successfully regularizes probability confidence. Meanwhile, `Decision 1.0` achieved strong accuracy gains across all four tasks (including $+85.33\%$ on `toxic-chat` and $+33.33\%$ on `NexusRaven`), though its sharper confidence updates on 3-class sentiment increased ECE despite a $+0.2670$ Brier improvement.

## 4. Next Steps

Based on these empirical findings, the upcoming focus will be:

1. **Architecture-Aware Decision Heads:** Replace the uniform `MarkerDecisionModelWrapper` for causal/autoregressive backbones with architecture-appropriate readouts (e.g., sequence-last-token pooling for causal models vs. bidirectional marker gathering for masked encoders) so accuracy scales alongside calibration.
2. **Improving the RLCD Pipeline for Better Calibration:** Refine post-hoc temperature scaling, reward weighting (`ce_weight` vs. Brier RL weight), and exploration noise schedules to prevent ECE regressions during sharp accuracy gains (such as those observed on multi-class sentiment tasks).
