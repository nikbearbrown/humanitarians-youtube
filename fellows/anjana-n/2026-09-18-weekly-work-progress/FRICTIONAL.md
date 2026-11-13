# Friction Log: Week 12 (Phase 12)

**Project:** Mycroft — ECIS + Decision Scorecard
**Week:** September 13 – September 19, 2026

---

## 1. Focus of the week

- **Prediction system:**
  - architecture integration
  - model-agnostic feature pipeline
  - FMP consensus estimates
  - guidance surprise score
- **Cross-company analysis:** correlation matrix and leading/lagging indicator detection.
- **Evaluation:** confidence-stratified evaluation and sector-normalized scoring (sector ETFs replacing SPY).
- **Dashboard:**
  - surprise score in the Signal Explorer
  - correlation heatmap
  - confidence-stratified Scorecard view
- **Research:** correlation pattern analysis (genuine vs. spurious) and an architecture review.
- **Outputs:**
  - two Claude artifacts
  - one Substack article
  - two videos

## 2. What was tried, and what was expected

- **SPY benchmark:** expected outcome grading against SPY to give a fair picture of signal accuracy.
- **Aggregate Scorecard:** expected the aggregate to represent system performance well.
- **Correlations:** expected detected cross-company correlations to reflect real structure.
- **Consensus integration:** expected it to plug into the existing feature pipeline cleanly.
- **Sector mapping:** expected every ticker to map cleanly to a single sector ETF.

## 3. Points of resistance, and next steps taken

### Evaluation shapes what the system can see (load-bearing)
- **Sector normalization:**
  - SPY inflated accuracy during sector-wide moves. Semiconductor stocks outperformed SPY during the AI boom regardless of individual guidance quality.
  - Switching to sector ETFs flipped several signals from correct to incorrect, so earlier aggregate metrics were overstated.
- **Confidence stratification:**
  - The aggregate masked a bimodal pattern. High-confidence signals (above 0.8) were substantially more accurate. Low-confidence signals (below 0.5) performed near random.
  - The blended number undersold the best signals and oversold the worst.
- **Next step:** both normalization methods are stored in the outcomes schema, and evaluation is reported by confidence tier.
- **Lesson:** the bottleneck was the evaluation, not the pipeline.

### The multiple comparison trap
- **What resisted:** 25 tickers produce about 300 pairwise comparisons. At p < 0.05, about 15 would pass by chance alone. Time-lagged analysis doubles the hypothesis space and halves the usable data per pair.
- **Next step:**
  - Applied a Bonferroni correction.
  - Added minimum-sample thresholds.
  - Flagged low-sample correlations separately from statistically supported ones.
  - Surfaced results now, with explicit caveats in the dashboard, rather than waiting for more data.

### ChromaDB population race condition
- **What happened:** after the consensus integration, the feature pipeline ran before ChromaDB was fully populated for new tickers.
  - Temporal retrieval returned empty context, silently.
  - The LLM extracted without prior-quarter context, producing weaker signals that were mixed with fully contextualized ones.
- **Next step:** a population-check gate that verifies ChromaDB data exists for each ticker before extraction.
- **Lesson:** a silent failure. There were no errors, only subtly degraded extractions.

### Consensus data normalization
- **What resisted:** EPS scales differ across companies, so raw consensus deltas aren't comparable. Some tickers also lack analyst coverage.
- **Next step:**
  - Z-score normalization of consensus deltas.
  - A graceful fallback to non-consensus features where coverage is missing.
  - FMP was selected over Yahoo Finance, Alpha Vantage, and direct SEC parsing, for consistent coverage at the free tier.

### Sector ETF mapping edge cases (partially resolved)
- **What happened:** three tickers span multiple sectors, with no clean single-ETF benchmark.
- **Next step:** use the closest ETF plus an approximate-mapping flag. A blended benchmark would be more accurate, but its complexity isn't justified at 25 tickers.
  - The flag is a pragmatic marker, not a full solution.

### Confidence tier boundary sensitivity (unresolved)
- **What happened:** results shift meaningfully with different splits: 0.4/0.7, 0.5/0.8, 0.6/0.9. Higher thresholds shrink the sample and inflate accuracy.
- **Next step:** documented the sensitivity rather than hiding behind a single threshold choice.

## 4. AI and other contributions: accepted, changed, rejected

### Claude + Humanitarians AI video generation tool
- **Original work:** the concept, ideas, narration, and direction for both videos.
- **Claude's part:** assembling the videos, using the video generation tool created by Humanitarians AI.

### Claude (artifacts)
- **Model Comparison Arena:** logistic regression vs. XGBoost on accuracy, calibration, feature importance, and per-ticker performance.
- **Prediction Feature Correlation Explorer:** an interactive correlation matrix of all prediction features, with filtering and drill-down.

### Eddy
- Reviewed the Week 12 article before publication.

### Gru
- No SDD session this week. The new architectural decisions still need SDD documentation.

## 5. Understood now, and still unresolved

### Understood
- **Benchmarks:** changing the baseline changes the findings. Sector-relative grading is the honest measure.
- **Aggregates:** an aggregate can hide a distribution with two distinct modes. Slicing by confidence showed that confidence carries real information.
- **Statistical testing:** with small samples and many comparisons, correction and minimum-sample rules are required to avoid building features on noise.
- **Silent ordering dependencies:** new integrations can introduce them. Gates that verify inputs exist are cheap insurance.
- **Prediction target:** consensus surprise changes what is being predicted. The question moves from "up or down" to "relative to expectations."

### Unresolved
- **Confidence tier boundaries:** there is no objectively correct threshold.
- **Multi-sector tickers:** the blended benchmark is deferred.
- **Routing complexity decision:** carried forward.
- **Signal decay horizon weighting:** carried from Week 10.
- **Latency as a signal:** logging continues.
- **SDD documentation:** still needed for this week's architecture changes.
