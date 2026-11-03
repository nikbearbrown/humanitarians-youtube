# Weekly Report: Week 5 (Phase 5)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard
**Week:** July 26 – August 1, 2026
**Total hours:** 27.0

---

## Summary

- Focus shifted from building to scaling and validation, with the pipeline run across 10–15 new AI-sector tickers.
- Three silent data-integrity bugs found and fixed:
  - EDGAR filing date parsing
  - new transcript formats breaking the normalizer
  - stale cached outcomes
- First multi-ticker Scorecard evaluation completed.
- Fine-tuning decision (open since Week 2) resolved: targeted fine-tuning on the maintained/none boundary, not broad retraining.
- Feedback loops deployed with thresholds derived from observed distributions:
  - calibration watchdog
  - orchestration learning graph
  - vindication aggregation
- Dashboard updated for multi-ticker support.
- One Claude artifact and one Substack article completed.

---

## Work Completed

### Pipeline Scaling

#### 1. Fix EDGAR Filing Date Parsing Edge Cases
*Development · Pipeline Scaling*
- **The problem:** a subset of 8-K filings used the filing acceptance date instead of the earnings call date.
- **Why it mattered:** the 1–3 business day difference shifted the outcome resolver's price fetch window. That could flip correctness grades.
- **The fix:** filename dates cross-referenced against filing metadata, with the period-of-report date used as canonical.
- **Deliverable:** corrected filing date parsing; data integrity issue resolved
- **Links:**
  - https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/src/ecis/ingestion
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/outcome_resolver.py
- **Status:** Complete

#### 2. Re-Extract Signals with Corrected Dates
*Development · Pipeline Scaling*
- Re-ran the extraction pipeline on transcripts using the corrected filing dates.
- Ensures signals are graded against the correct price window.
- **Deliverable:** signals re-extracted with corrected dates
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/src/ecis/ingestion
- **Status:** Complete

#### 3. Ingest and Process 10–15 New AI-Sector Tickers
*Development · Pipeline Scaling*
- Expanded the dataset from the initial sample to a broader set of AI-sector companies via EDGAR and FMP.
- **Deliverable:** expanded ticker dataset ingested and processed
- **Links:**
  - https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/src/ecis/ingestion
  - https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/src/ecis/preprocessing
- **Status:** Complete

#### 4. Run Full Extraction Pipeline Across New Tickers
*Development · Pipeline Scaling*
- Ran all four readers, triangulation, and deduplication across the expanded ticker set.
- **Deliverable:** full extraction pipeline executed at scale across the expanded dataset
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

#### 5. Populate ChromaDB Collections for New Tickers
*Development · Pipeline Scaling*
- Populated the temporal retrieval and RAG collections with embeddings from the expanded transcript set.
- **Deliverable:** ChromaDB collections populated for the expanded ticker set
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/embedding/embedder.py
- **Status:** Complete

### Outcome Resolution

#### 6. Outcome Resolver Caching Layer
*Development · Outcome Resolution*
- Built a caching layer to persist resolved outcomes and skip redundant yfinance fetches.
- Fixed a cache key bug: because `transcript_date` was missing from the key, corrected-date signals received stale cached outcomes.
- **Deliverable:** outcome caching layer with corrected cache key logic
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/outcome_resolver.py
- **Status:** Complete

#### 7. Batch Outcome Resolution Across Expanded Signal Set
*Development · Outcome Resolution*
- Resolved outcomes in batch across the expanded signal set.
- **Deliverable:** batch-resolved outcomes for the expanded dataset
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/outcome_resolver.py
- **Status:** Complete

### Scoring / Evaluation

#### 8. Scorecard Evaluation Across Multiple Tickers
*Development · Scoring / Evaluation*
- Ran the full scoring suite across the expanded signal set: Brier score, skill score, ECE, Murphy decomposition.
- First multi-ticker evaluation.
- Murphy decomposition interpreted at N≈50 to distinguish terminal lack of skill from treatable calibration error.
- **Deliverable:** first multi-ticker Scorecard evaluation results
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
- **Status:** Complete

### Feedback Loops

#### 9. Deploy Calibration Watchdog Graph
*Development · Feedback Loops*
- Deployed the calibration watchdog in production mode.
- Threshold values derived from observed signal distributions rather than defaults.
- **Deliverable:** calibration watchdog deployed with empirically derived thresholds
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graphs/watchdog_graph.py
- **Status:** Complete

#### 10. Deploy Orchestration Learning Graph
*Development · Feedback Loops*
- Deployed the orchestration learning graph with false-negative analysis and threshold adjustment.
- Initial values derived from observed distributions.
- **Deliverable:** orchestration learning graph deployed with empirically derived thresholds
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graphs/learning_graph.py
- **Status:** Complete

#### 11. Vindication Aggregation Across Conflict Resolution Outcomes
*Development · Feedback Loops*
- Aggregated vindication records from conflict resolution to inform dynamic reader weight adjustments.
- Adjustment rate set from observed patterns.
- **Deliverable:** vindication aggregation informing triangulator rebalancing
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/vindication.py
- **Status:** Complete

### Dashboard

#### 12. Dashboard Updates: Multi-Ticker Filters + Reader Comparison + RAG Interface
*Development · Dashboard*
- Signal Explorer updated with ticker filtering.
- Reader Comparison table populated with expanded outcome data.
- RAG query interface improved using the populated ChromaDB collections.
- **Deliverable:** dashboard updated for multi-ticker support
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/src/ecis/dashboard
- **Status:** Complete

### Debugging

#### 13. Debugging: Filing Dates + Transcript Formats + Cache Staleness
*Development · Debugging*
- Three silent correctness issues resolved:
  - EDGAR filing date parsing returning wrong dates
  - new ticker transcript formats breaking the normalizer
  - caching layer serving stale outcomes for re-extracted signals
- **Deliverable:** three silent data integrity bugs identified and resolved
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/tests
- **Status:** Complete

### Research

#### 14. Evaluation of Base System Scorecard Results + Fine-Tuning Decision
*Research · Scoring / Evaluation*
- Categorized error patterns from the expanded Scorecard run. Most errors cluster in two places:
  - retrieval gaps: implicit guidance without temporal context
  - maintained-vs-none misclassification
- Fine-tuning decision (open since Week 2) resolved: targeted fine-tuning on the maintained/none boundary, not broad extraction retraining.
- **Deliverable:** error categorization report; fine-tuning decision resolved (targeted, not broad)
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

### Artifact

#### 15. Signal Distribution Dashboard
*Artifact · Claude Artifact*
- Interactive artifact visualizing the distribution of extracted signals from the expanded pipeline run.
- Signals are broken down by ticker, reader, confidence level, and guidance direction.
- **Deliverable:** Claude Artifact: Signal Distribution Dashboard
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### Writing

#### 16. Substack Article: "When to Stop Prompting and Start Fine-Tuning"
*Writing · Substack Article*
- Argues for a systematic framework for deciding when prompt engineering has reached its limits and fine-tuning becomes the right intervention.
- Grounded in error patterns observed in the ECIS extraction pipeline.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/when-to-stop-prompting-start-fine-tuning
- **Status:** Complete (published)
