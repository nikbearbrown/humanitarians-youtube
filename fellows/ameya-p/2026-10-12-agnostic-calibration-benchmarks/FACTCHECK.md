# FACTCHECK — 2026-10-12-agnostic-calibration-benchmarks (Fine-Tuning Platform)

Every claim the narration makes, mapped to the source document:
`work_report.md`
("Fine-Tuning Platform: Agnostic Model/Dataset Architecture & Multi-Dataset Calibration Benchmarks").

## B00 — Cold open

- **"Last week we proved our RLCD calibration pipeline worked on a single model and dataset."**
  Source §1: "Following the successful end-to-end validation of the Reinforcement Learning with Calibrated Decisions (RLCD) pipeline on the xLAM dataset with the Laya model last week..."
- **"Can we make the pipeline completely model and dataset agnostic, and does calibration hold up across different architectures?"**
  Source §1 objectives 1 and 2: engineering `rlcd/processing.py` and `rlcd/models.py` for automatic schema inference and model loading, and empirical benchmarking on `Typical` and `Decision 1.0` across four datasets.

## B01 — BLUF

- **"When you attach a proper scoring reward to any decision model, calibration reliably improves—even when a model's backbone cannot improve raw accuracy."**
  Source §3 Key Finding: "Across nearly all runs, the RLCD Brier reward strategy consistently improved the Mean Brier Score (all 8/8 runs) and reduced Expected Calibration Error (ECE) (7/8 runs). Even when a model could not improve classification accuracy on hard or ambiguous tasks... RLCD slashed ECE down to 0.50% and 0.36%, respectively, teaching the model to output honest, balanced probabilities (~50%/50%) rather than overconfident errors."

## B02 — Agnostic Architecture (`rlcd/processing.py` & `rlcd/models.py`)

- **"Processing dot py now samples any incoming dataset, infers context, options, and target columns, and maps rows into choice, score, or binary noul primitives."**
  Source §2: "Implemented `auto_prepare_dataset()` to automatically inspect and sample incoming datasets, infer column roles (context, embedded or JSON candidate options, and target labels), and dynamically map records into `choice` (categorical/tool selection), `noul` (binary/contrastive safety pairs), or `score` (ordinal rating scales)."
- **"Models dot py wraps five different model families under one unified marker-readout interface."**
  Source §2: "Built the unified `DecisionModel.load_model()` router with dedicated loaders for `Laya`, `Von`, `OpenDecision`, `Typical`, and `Decision1`. Created `MarkerDecisionModelWrapper` to wrap arbitrary encoder backbones with standardized RLCD marker-readout scoring heads..."

## B03 — Empirical Testing (Toxic-Chat Accuracy)

- **"We tested Typical-small and Decision 1.0 across four benchmarks: toxic-chat, tweet sentiment, Anthropic HH-RLHF, and NexusRaven tool evaluation."**
  Source §3 benchmark table: `lmsys/toxic-chat` (5,082), `mteb/tweet_sentiment` (26,732), `Anthropic/hh-rlhf` (60,000), and `NexusRaven_API_eval` (318).
- **"On toxic-chat ordinal scoring, both models jumped from under ten percent baseline accuracy to nearly ninety-five percent."**
  Source §3 table: `Typical-small` on `lmsys/toxic-chat` (`score`) moved from `0.39% -> 94.88%` (+94.49%), and `Decision 1.0` on `lmsys/toxic-chat` (`score`) moved from `9.65% -> 94.98%` (+85.33%). On screen, values are rounded to integers (1, 95, 10, 95) for bar chart display.

## B04 — Calibration vs. Architecture Twist

- **"8 of 8 runs improved Mean Brier Score; 7 of 8 cut ECE."**
  Source §3 Key Finding: "improved the Mean Brier Score (all 8/8 runs) and reduced Expected Calibration Error (ECE) (7/8 runs)."
- **"Typical-small uses a causal Qwen backbone, so our bidirectional marker head created a bottleneck on sentiment and safety pairs. Even with flat accuracy, Brier reward cut calibration error down to half a percent..."**
  Source §3 Key Finding: `Typical-small` on `tweet_sentiment` (39.54% -> 39.54% accuracy, ECE 8.63% -> 0.50%) and `Anthropic/hh-rlhf` (50.21% -> 49.79% accuracy, ECE 4.67% -> 0.36%); "Unlike bidirectional masked encoders (`Laya`), `Typical-small` uses a Qwen-family causal/autoregressive backbone. Attaching a uniform bidirectional marker-readout head (`MarkerDecisionModelWrapper`) creates a representational bottleneck..."

## B05 — Next Steps Verdict

- **"Build architecture-aware decision heads so causal models pool from the final token while masked encoders gather at markers."**
  Source §4.1: "Replace the uniform `MarkerDecisionModelWrapper` for causal/autoregressive backbones with architecture-appropriate readouts (e.g., sequence-last-token pooling for causal models vs. bidirectional marker gathering for masked encoders)..."
- **"Tune temperature scaling and cross-entropy weights so sharp accuracy jumps never hurt calibration."**
  Source §4.2: "Refine post-hoc temperature scaling, reward weighting (`ce_weight` vs. Brier RL weight), and exploration noise schedules to prevent ECE regressions during sharp accuracy gains..."

## B06 — Your Turn Handoff

- Suggested prompt for the viewer to run `auto_prepare_dataset()` on a benchmark and compare causal vs. bidirectional calibration.

## B07 — Outro

- Title restate only (`week4 (Oct 12).` / `Fine-Tuning Platform`).
