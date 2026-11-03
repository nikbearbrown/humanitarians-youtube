# Weekly Report: Week 6 (Phase 6)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard
**Week:** August 2 – August 8, 2026
**Total hours:** 32.0

---

## Summary

- Model experimentation week: Mistral-7B-Instruct configured alongside Llama 3.1 8B and run through the full extraction pipeline on a representative ticker subset.
- Key finding: the two models fail in complementary ways.
  - **Llama:** errors are calibration-heavy. These are fixable through recalibration.
  - **Mistral:** errors are resolution-heavy. These require architectural intervention.
- Pipeline scaling continued with additional tickers. The feedback loops completed their first full production cycle.
- Dashboard updated with model comparison support.
- Three cross-model integration bugs resolved: Mistral JSON truncation, type mismatches, and chunk ordering.
- Outputs:
  - one Claude artifact
  - two Substack articles
  - two videos

---

## Work Completed

### Pipeline Scaling

#### 1. Ingest and Process Additional Tickers
*Development · Pipeline Scaling*
- Expanded the dataset further with additional AI-sector tickers from EDGAR and FMP.
- **Deliverable:** additional tickers ingested and processed
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/src/ecis/ingestion
- **Status:** Complete

#### 2. Run Full Extraction Pipeline Across New Tickers
*Development · Pipeline Scaling*
- Ran all four readers, triangulation, and deduplication across the expanded set.
- **Deliverable:** full extraction pipeline executed at scale
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graphs/pipeline_graph.py
- **Status:** Complete

#### 3. Batch Outcome Resolution Across Expanded Signal Set
*Development · Pipeline Scaling*
- Resolved outcomes in batch across the expanded signal set.
- **Deliverable:** batch-resolved outcomes
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/outcome_resolver.py
- **Status:** Complete

### Scoring / Evaluation

#### 4. Scorecard Evaluation with Expanded Data
*Development · Scoring / Evaluation*
- Ran the scoring suite across the expanded set.
- **Deliverable:** updated Scorecard evaluation results
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
- **Status:** Complete

### Model Experimentation

#### 5. Configure and Load Mistral-7B-Instruct via Ollama
*Development · Model Experimentation*
- Set up Mistral-7B as a second LLM reader alongside Llama 3.1 8B.
- **Deliverable:** Mistral-7B configured and operational
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/config/settings.py
- **Status:** Complete

#### 6. Run Extraction on Representative Ticker Subset with Mistral-7B
*Development · Model Experimentation*
- Ran the full extraction pipeline with Mistral-7B on a representative subset to generate comparable signals.
- **Deliverable:** Mistral-7B extraction results for comparison
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/llm_reader.py
- **Status:** Complete

#### 7. Scorecard Comparison: Llama 3.1 8B vs. Mistral-7B
*Development · Model Experimentation*
- Side-by-side Scorecard evaluation of both models.
- **Key finding:** the models fail in complementary ways.
  - **Llama:** errors are calibration-heavy, so they can be fixed through recalibration.
  - **Mistral:** errors are resolution-heavy, so they require architectural intervention.
- **Deliverable:** cross-model error decomposition analysis; complementary error profile finding
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
- **Status:** Complete

#### 8. Compare Self-Consistency Behaviour and Hallucination Rates Across Models
*Development · Model Experimentation*
- Compared both models under the three-temperature self-consistency sweep.
- Mistral's hallucination rate rose more under temperature variation, which suggests its extractions are less grounded in the source text.
- **Deliverable:** cross-model self-consistency and hallucination analysis
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/llm_reader.py
- **Status:** Complete

#### 9. Prompt Template Adjustments for Mistral-7B
*Development · Model Experimentation*
- With the Llama-optimized prompts, Mistral-7B truncated its JSON output on ~10–15% of extractions.
- Diagnosed as output format sensitivity.
- Chain-of-thought prompts adjusted specifically for Mistral-7B.
- **Deliverable:** Mistral-specific prompt templates
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/llm_reader.py
- **Status:** Complete

### Feedback Loops

#### 10. Observe and Analyze First Full Watchdog and Learning Graph Cycle
*Development · Feedback Loops*
- Observed the calibration watchdog and orchestration learning graph running their first full production cycle.
- Checked whether the threshold values set in Week 5 produce the expected behavior.
- Evaluated the automated threshold adjustments for overcorrection.
- **Deliverable:** first feedback loop cycle validated; threshold behavior assessed
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graphs/watchdog_graph.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graphs/learning_graph.py
- **Status:** Complete

### Dashboard

#### 11. Model Comparison View + Per-Model Reader Metrics
*Development · Dashboard*
- Added a dashboard view comparing model performance side by side.
- Updated the reader comparison table to show metrics per model.
- **Deliverable:** dashboard updated with model comparison support
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/src/ecis/dashboard
- **Status:** Complete

### Debugging

#### 12. Debugging: Mistral JSON Truncation + Type Mismatches + Chunk Ordering
*Development · Debugging*
- Three issues resolved:
  - Mistral producing truncated JSON output.
  - Type mismatches in the self-consistency vote comparison across models.
  - Non-deterministic chunk ordering breaking cross-model alignment. Fixed with content hashing, which gives each chunk a stable ID.
- **Deliverable:** three cross-model integration bugs resolved
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/tests
- **Status:** Complete

### Research

#### 13. Mistral-7B Architecture, Capabilities, and Configuration
*Research · Compute / LLM*
- Researched Mistral-7B's architecture, known behaviors, and configuration options.
- **Deliverable:** Mistral-7B technical assessment
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

### Artifact

#### 14. Model Comparison Dashboard
*Artifact · Claude Artifact*
- Interactive artifact comparing Llama and Mistral performance side by side.
- Shows Brier scores, error decomposition, self-consistency behavior, and hallucination rates.
- **Deliverable:** Claude Artifact: Model Comparison Dashboard
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### Writing

#### 15. Substack Article: "Model-Level Routing vs. Single-Model Fine-Tuning"
*Writing · Substack Article*
- Argues for one side of a design trade-off with two options:
  - routing chunks to different models based on signal type
  - fine-tuning a single model on its failure mode
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/model-routing-vs-fine-tuning-extraction
- **Status:** Complete (published)

#### 16. Substack Article: "Mistral vs. Llama on Financial Text"
*Writing · Substack Article*
- Compares the two models on financial earnings call extraction.
- The comparison rests on error decomposition rather than leaderboard metrics.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/mistral-vs-llama-on-financial-text
- **Status:** Complete (published)

### Video

Both videos follow the same split.
- **Concept, ideas, narration, and direction:** original work.
- **Assembly:** Claude, using the video generation tool created by Humanitarians AI.

#### 17. Video: "Why AI Dominates the Crypto Market"
*Video · Video Production*
- Thematic video exploring AI's role and dominance in the cryptocurrency market.
- **Deliverable:** Video: Why AI Dominates the Crypto Market
- **Links:**
  - https://www.youtube.com/watch?v=u3l_YiijnSs
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-07-why-ai-dominates-the-crypto-market
- **Status:** Complete

#### 18. Video: "ECIS Explained"
*Video · Video Production*
- Project explainer video covering the ECIS system architecture, purpose, and pipeline design.
- **Deliverable:** Video: ECIS Explained
- **Links:**
  - https://www.youtube.com/watch?v=3mxjvm85JNg
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-07-ecis-explained
- **Status:** Complete
