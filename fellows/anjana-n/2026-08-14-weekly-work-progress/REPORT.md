# Weekly Report: Week 7 (Phase 7)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard
**Week:** August 9 – August 15, 2026
**Total hours:** 29.5

---

## Summary

- Targeted QLoRA fine-tuning on the maintained-vs-none boundary executed and tested on held-out data.
- **Result:** Brier skill score improved by 0.07, above the 0.05 threshold.
  - Gains were concentrated where the Week 5 error taxonomy predicted.
  - Calibration improved but resolution stayed flat, suggesting a representation ceiling at 8B parameters.
- **Model routing:** Mistral-7B integrated for Category B hedged-language chunks.
  - Fine-tuning narrowed the routing benefit.
  - Routing is still warranted for hedged downgrades.
- Pipeline enhancements:
  - maintained/none prompt boundary
  - temporal retrieval edge cases
  - exemplar collection
  - boilerplate detection
  - batch-level consistency checking
  - ticker registry
- Outputs:
  - one Claude artifact
  - one Substack article
  - two videos

---

## Work Completed

### Pipeline Scaling

#### 1. Run Extraction Pipeline Across Additional Companies (Mistral-7B)
*Development · Pipeline Scaling*
- Ran the extraction pipeline with Mistral-7B on additional tickers to expand the comparison dataset.
- **Deliverable:** expanded Mistral-7B extraction dataset
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/llm_reader.py
- **Status:** Complete

### Pipeline Enhancement

#### 2. Refine Maintained-vs-None Classification Boundary in Prompt
*Development · Pipeline Enhancement*
- Refined the prompt template to sharpen the distinction between two labels:
  - **maintained:** the company reaffirms prior guidance
  - **none:** no guidance signal is present
- Added handling for soft reaffirmation language.
- **Deliverable:** refined maintained/none prompt boundary
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/llm_reader.py
- **Status:** Complete

#### 3. Improve Temporal Retrieval Query Construction for Edge Cases
*Development · Pipeline Enhancement*
- Improved ChromaDB temporal queries for three edge cases:
  - inconsistent fiscal calendars
  - mid-quarter guidance updates
  - non-standard reporting periods
- **Deliverable:** improved temporal retrieval for edge cases
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/llm_reader.py
- **Status:** Complete

#### 4. Populate ChromaDB Exemplar Collection with Expanded Examples
*Development · Pipeline Enhancement*
- Added exemplars from new tickers to the few-shot retrieval collection.
- **Deliverable:** expanded exemplar collection
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/embedding/exemplar_store.py
- **Status:** Complete

#### 5. Improve Boilerplate Detection in Normalizer
*Development · Pipeline Enhancement*
- Updated the normalizer to handle non-standard transcript formats from new tickers.
- **Deliverable:** updated normalizer for new format variations
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/preprocessing/boilerplate.py
- **Status:** Complete

#### 6. Batch-Level Consistency Checking Across Adjacent Chunks
*Development · Pipeline Enhancement*
- Added validation that checks adjacent chunks in the same transcript against each other.
- It catches contradictions and duplications between them.
- **Deliverable:** batch-level consistency validation
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/finbert_reader.py
- **Status:** Complete

### Infrastructure

#### 7. Ticker Registry Table in SQLite + Migration Script
*Development · Infrastructure*
- Created a structured ticker registry in SQLite.
- Wrote a migration script from the existing directory structure.
- **Deliverable:** ticker registry + migration script
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/ticker_registry.py
- **Status:** Complete

### Model Optimization

#### 8. Targeted QLoRA Fine-Tuning on Maintained-vs-None Boundary
*Development · Model Optimization*
- Ran QLoRA fine-tuning on Llama 3.1 8B, using an A100 on Colab, targeting the maintained-vs-none classification boundary.
- Training data composition required judgment on:
  - example selection
  - boundary balancing
  - reasoning trace correction
- **Deliverable:** fine-tuned Llama 3.1 8B adapter (maintained/none boundary)
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/src/ecis/notebooks
- **Status:** Complete

#### 9. Scorecard Before-and-After Comparison on Held-Out Data
*Development · Model Optimization*
- Brier skill score improved by 0.07, above the 0.05 threshold.
- Gains concentrated in maintained-vs-none, as the Week 5 error taxonomy predicted.
- **Murphy decomposition:**
  - calibration improved
  - resolution stayed flat, suggesting a representation ceiling at 8B parameters
- **Deliverable:** before/after Scorecard comparison; 0.07 Brier skill score improvement confirmed
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
- **Status:** Complete

#### 10. Integrate Mistral-7B as Secondary Model for Hedged Language Chunks
*Development · Model Optimization*
- Implemented initial routing logic that sends Category B hedged-language chunks to Mistral-7B.
- After fine-tuning, the routing benefit is narrower than expected but still warranted for hedged downgrades.
- **Deliverable:** Mistral-7B routing integration for hedged language
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/src/ecis/notebooks
- **Status:** Complete

### Scoring / Evaluation

#### 11. Full Scorecard Evaluation + Platt/Isotonic Recalibration
*Development · Scoring / Evaluation*
- Ran a full evaluation across the expanded and corrected signal set.
- Ran recalibration with the expanded outcome data.
- **Deliverable:** updated Scorecard evaluation + recalibration
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/recalibrator.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
- **Status:** Complete

#### 12. Per-Ticker Reader Comparison Analysis
*Development · Scoring / Evaluation*
- Analyzed reader performance by ticker.
- The goal was to find company-specific language patterns that systematically favor one reader over another.
- **Deliverable:** per-ticker reader performance analysis
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
- **Status:** Complete

### Dashboard

#### 13. RAG Query Interface Improvements + Per-Ticker Performance View
*Development · Dashboard*
- Improved the RAG query interface.
- Added a per-ticker performance breakdown view.
- **Deliverable:** dashboard updated with per-ticker views
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/src/ecis/dashboard
- **Status:** Complete

### Debugging

#### 14. Debugging: Colab Checkpoint Gap + Tokenization Drift
*Development · Debugging*
- Two issues resolved:
  - **Colab checkpoint gap:** a QLoRA Colab disconnect hit with no intermediate checkpoint. Fixed by reducing the checkpoint interval to 100 steps.
  - **Tokenization drift:** the fine-tuned adapter's tokenization drifted, causing content hash mismatches. Fixed with whitespace normalization before hashing.
- **Deliverable:** two model optimization bugs resolved
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/tests
- **Status:** Complete

### Research

#### 15. QLoRA Fine-Tuning Study + Mistral-7B Exploration
*Research · Compute / LLM*
- Studied adapter strategies, rank selection, and training data preparation for QLoRA.
- Continued exploring Mistral-7B behavior and configuration.
- **Deliverable:** fine-tuning and model configuration research
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 16. Evaluation of Fine-Tuning Results: Routing Reassessment
*Research · Model Optimization*
- Post-fine-tuning evaluation of whether model routing remains justified, given the narrowed benefit.
- Routing is still warranted for hedged language.
- Whether that narrower benefit justifies the operational complexity remains open.
- **Deliverable:** routing reassessment post-fine-tuning
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

### Artifact

#### 17. Fine-Tuning Data Reviewer
*Artifact · Claude Artifact*
- Interactive artifact for reviewing training data composition.
- It visualizes the example distribution across the maintained/none boundary and flags memorization risks.
- **Deliverable:** Claude Artifact: Fine-Tuning Data Reviewer
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### Writing

#### 18. Substack Article: "Tokenizer Alignment Across Models"
*Writing · Substack Article*
- Examines the tokenization mismatch between FinBERT and Llama.
- Chunks defined by FinBERT's tokenizer cross token boundaries when Llama processes them, which affects extraction consistency.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/tokenizer-alignment-across-models
- **Status:** Complete (published)

### Video

Both videos follow the same split.
- **Concept, ideas, narration, and direction:** original work.
- **Assembly:** Claude, using the video generation tool created by Humanitarians AI.

#### 19. Video: "FinBERT Explainer"
*Video · Video Production*
- Explainer video on FinBERT's role in the extraction pipeline.
- Covers sentiment classification, batched inference, and the 512-token context window constraint.
- **Deliverable:** Video: FinBERT Explainer
- **Links:**
  - https://www.youtube.com/watch?v=7JRFtmd0HEQ
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-14-finbert-explainer
- **Status:** Complete

#### 20. Video: "ECIS Explained (EP2)"
*Video · Video Production*
- Weekly project explainer video.
- Reflects the pipeline enhancements, fine-tuning results, and expanded ticker coverage.
- **Deliverable:** Video: ECIS Explained (EP2)
- **Links:**
  - https://www.youtube.com/watch?v=0byQTw6SZSw
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-14-ecis-explained
- **Status:** Complete
