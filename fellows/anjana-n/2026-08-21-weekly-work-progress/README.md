**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 8 — Architecture Rework and Model Expansion

**Timeline:** August 16, 2026 – August 22, 2026

**Scope:** Native multi-model architecture, Qwen2.5-14B integration, three-model evaluation, full 25-ticker coverage, and reliability and reproducibility hardening.

---

## Architecture Rework
- **Inputs to the review:**
  - Multi-model error divergence
  - Maintained/none boundary errors
  - Scaling friction
  - Feedback-loop behaviour
- **Changes:**
  - Component boundaries redesigned for native multi-model extraction
  - Orchestration state carries a per-chunk model assignment
  - Triangulator accepts model identity as a weighting factor alongside reader identity
- Revised graph diagrams and state-flow documentation

## Qwen2.5-14B Integration
- **Deployment:** AWQ 4-bit quantization via Ollama on a Colab A100
  - VRAM usage of about 8–10 GB
- **Validation:** output format compatibility with the extraction pipeline
- **Architecture review:**
  - Grouped-query attention
  - Stronger multilingual and code representation in training data
- **Extraction run:**
  - Representative ticker subset
  - Same retrieval, self-consistency, and verification as the other models
  - Prompt templates adapted to Qwen's instruction-following style
- **Runtime profile:** higher per-call latency than the 8B models, but fewer retries thanks to more reliable JSON output

## Three-Model Scorecard Comparison
- Llama 3.1 8B, Mistral-7B, and Qwen2.5-14B evaluated on identical data
- **Metrics:**
  - Brier score and skill score
  - Calibration curves and Murphy decomposition
  - Self-consistency behaviour
  - Hallucination rate
- **Research question:** whether model scale closes the shared 7B/8B gaps
  - The maintained/none boundary
  - Hedged language

## Pipeline Scaling
- Coverage completed at 25 AI-sector companies
- Batch outcome resolution executed across the full signal set

## Input Validation Layer
- **Pre-reader rejection criteria:**
  - Empty chunks
  - Boilerplate token ratio > 0.8
  - Below the minimum token threshold
- Rejected chunks logged with a reason and excluded from extraction

## Confidence Gating
- Signals below a configurable minimum confidence are:
  - Persisted to the decision log
  - Flagged as low-confidence
  - Excluded from Scorecard metrics
- **Target:** maintained over-triggering, since false maintained signals cluster at low confidence

## Malformed JSON Retry Logic
- Exponential backoff
- At most 3 retries, each at temperature 0.0
- After the final failure, the chunk is logged as failed with its raw output preserved
- Retry count tracked per signal for model- and chunk-level monitoring

## Signal Provenance Tracking
- **Persisted for every signal:** the full prompt, including:
  - System prompt
  - Retrieved few-shot exemplars
  - Temporal context
  - Populated user template
- **Storage:** compressed JSON blob in the signals database
- **Enables:**
  - Exact reproduction of any extraction
  - Cross-model diagnosis
  - Long-term debugging

## Outcome Cache Improvements
- Cache invalidation on corporate actions (splits, dividends) that change adjusted prices returned by yfinance
- Cache key validation prevents stale outcomes on re-extracted signals with corrected dates

## Dashboard
- **Reader comparison:** per-model metric columns
- **Signal explorer:** model selector filter
- **Calibration curves:** all three models overlaid on one chart
