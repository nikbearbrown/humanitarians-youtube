**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 10 — Fine-Tuning, Evaluation Features, and Pipeline Refinement

**Timeline:** August 30, 2026 – September 5, 2026

**Scope:** Completion of the three-model comparison, QLoRA fine-tuning of Llama 3.1 8B, and a set of calibration, weighting, and robustness refinements.

---

## Qwen2.5-14B Extraction Completion
- Extraction completed across all remaining tickers
- Final three-model Scorecard across 25 tickers, with definitive per-model metrics for Llama 3.1 8B, Mistral-7B, and Qwen2.5-14B

## QLoRA Fine-Tuning
- **Training data:**
  - 200+ human-reviewed extractions formatted as instruction–input–output JSONL triples
  - Each triple contains the system prompt, the chunk with few-shot and temporal context, and the corrected output with a revised reasoning trace
  - Concentrated on the maintained/none boundary
  - Balanced classes, with adversarial boundary examples
- **Model loading:**
  - Llama 3.1 8B with BitsAndBytes NF4 4-bit quantization via Unsloth on a Colab A100
  - VRAM usage of about 5–7 GB
  - Adapters attached to `q_proj`, `k_proj`, `v_proj`, `o_proj`
- **Training configuration:**

| Parameter | Value |
|---|---|
| LoRA rank | 16 |
| Learning rate | 2e-4 |
| Scheduler | Cosine |
| Gradient accumulation | Enabled |
| Epochs | 3–5 |
| Trainer | `trl` SFTTrainer |
| Checkpointing | Every 100 steps to Google Drive |

- **Evaluation:**
  - Held-out data
  - Brier score, skill score, ECE, and Murphy decomposition compared before and after fine-tuning
  - Acceptance criterion: skill score gain > 0.05
- **Integration:**
  - Adapter loaded on top of the base weights at inference time
  - Registered with the calibration watchdog for monitoring and automatic reversion

## Abstention Calibration
- Replaced the flat 0.15 penalty on 2–1 self-consistency votes with a penalty proportional to the confidence spread
- **Examples:**
  - Majority 0.80 vs. minority 0.75: minimal penalty
  - Majority 0.80 vs. minority 0.20: substantial penalty
- Improves calibration without changing the voting mechanism

## Section-Weighted Extraction
- **Section multipliers:** prepared remarks 1.0, Q&A 0.8 (configurable)
- **Rationale:**
  - Prepared remarks are rehearsed and IR-reviewed
  - Q&A is spontaneous and more speculative

## Signal Decay Tracking
- **Horizons compared:** 30, 90, and 180 days
- **`decay_profile` field values:**

| Profile | Pattern |
|---|---|
| Persistent | Correct at all horizons |
| Decaying | Correct at 30 days, incorrect at 180 days |
| Delayed | Incorrect at 30 days, correct at 180 days |

- Identifies readers that produce lasting vs. short-lived predictive value

## Negation Detection
- **Patterns:** "not raising", "won't increase", "no change to", "does not expect", "unlikely to revise"
- **Routing:** flagged chunks are forced into Category B, regardless of fast-pass results
- Mitigates FinBERT's inconsistent handling of negation

## Guidance Keyword Density
- **Metric:** taxonomy matches per chunk, normalized by token length
- **Interpretation:**
  - High density indicates an explicit, strong signal
  - Zero density with only FinBERT firing indicates a sentiment-only signal, which correlates with lower accuracy
- Fed into the triangulator as a weighting factor

## Duplicate Transcript Detection
- Hash of normalized transcript text
- On a hash match (re-filed or amended filings):
  - Extraction is skipped
  - The duplicate is logged with a reference to the original
- Prevents inflated signal counts and redundant compute

## Combined Evaluation
- **Representative re-run:** fine-tuned adapter plus all refinements, to confirm they compose cleanly
- **Full Scorecard, base vs. fine-tuned:**
  - Reader comparison table
  - Calibration curves
  - Per-ticker and trend-stratified metrics
