**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 5 — Scaling and Validation

**Timeline:** July 26, 2026 – August 1, 2026

**Scope:** Data correctness fixes, ticker expansion to 15 companies, outcome caching, first large-scale evaluation, feedback loop deployment, and fine-tuning strategy.

---

## Filing Date Correction
- **Issue:** some 8-K filenames use the filing acceptance date rather than the earnings call date
  - The resulting 1–3 business-day offset shifted price windows
  - This could flip correctness grades on signals near earnings reactions
- **Fix:**
  - Filename dates cross-referenced against filing metadata
  - The period-of-report date adopted as the canonical `transcript_date`
- NVIDIA signals re-extracted with the corrected dates

## Ticker Expansion (Round 1)
- Expanded from 2 tickers (NVIDIA, Microsoft) to 15 AI-sector companies
- Full data layer and extraction pipeline executed for every new ticker
- ChromaDB populated for the new tickers, enabling temporal retrieval and RAG queries

## Outcome Resolver Caching
- Resolved outcomes persisted to avoid repeated fetches
- **Resolved:** the cache key omitted `transcript_date`, so corrected-date signals received stale outcomes
  - `transcript_date` added to the key
- Batch outcome resolution executed across the expanded signal set

## Large-Scale Scorecard Evaluation
- **Coverage:** 15 tickers
- **Skill:** the LLM reader shows a positive skill score against the keyword baseline
- **Error profile (Murphy decomposition):**
  - Calibration is the dominant error component, which recalibration can address
  - Resolution, the non-correctable component, is the smaller contributor

## Feedback Loop Deployment
- **Calibration watchdog graph:** recalibration triggers at ECE > 0.10
- **Orchestration learning graph:** false-negative threshold of 5%
- **Vindication-based weight adjustment:** adjustment rate driven by conflict resolution outcomes
- Initial thresholds derived from the observed signal distributions

## Fine-Tuning Strategy
- **Error clusters:**
  - Implicit guidance changes with missing temporal context (a retrieval problem)
  - Maintained vs. `none` misclassification (a prompt-boundary problem)
- **Decision:** targeted fine-tuning on the maintained/none boundary rather than broad extraction retraining
