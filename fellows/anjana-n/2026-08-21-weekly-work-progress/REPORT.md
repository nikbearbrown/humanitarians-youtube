# Weekly Report: Week 8 (Phase 8)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard
**Week:** August 16 – August 22, 2026
**Total hours:** 29.75

---

## Summary

- Third model introduced: Qwen2.5-14B at AWQ 4-bit, to test whether the Week 7 resolution plateau lifts with more parameters. It does not.
- **Key finding:**
  - Qwen improved calibration on the maintained/none boundary, but resolution stayed flat.
  - All three models struggle equally on genuinely ambiguous text.
  - The boundary problem is linguistic ambiguity, not model capacity. Better taxonomy definitions and prompt boundaries will help where more parameters won't.
- Extraction completed across the full ticker set.
- **Pipeline hardening:**
  - input validation
  - confidence gating
  - retry logic for malformed JSON
  - signal provenance tracking
- **Architecture refactor:**
  - model identity carried per chunk
  - model tier added as a triangulator weighting factor
- Outputs: two Claude artifacts and two videos.

---

## Work Completed

### Pipeline Scaling

#### 1. Run Extraction Pipeline Across Remaining Tickers
*Development · Pipeline Scaling*
- Completed extraction across the remaining ticker set.
- **Deliverable:** extraction complete across full ticker set
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graphs/pipeline_graph.py
- **Status:** Complete

#### 2. Batch Outcome Resolution Across Expanded Signal Set
*Development · Pipeline Scaling*
- Resolved outcomes in batch across the full expanded signal set.
- **Deliverable:** full batch outcome resolution
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/outcome_resolver.py
- **Status:** Complete

### Model Experimentation

#### 3. Configure and Load Qwen2.5-14B via Ollama (AWQ 4-bit)
*Development · Model Experimentation*
- Configured and loaded the 14B-parameter model with 4-bit quantization.
- **Deliverable:** Qwen2.5-14B configured and operational
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/config/settings.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/notebooks/colab/ollama_colab.ipynb
- **Status:** Complete

#### 4. Run Extraction on Representative Ticker Subset with Qwen2.5-14B
*Development · Model Experimentation*
- Ran the full extraction pipeline using Qwen on a representative subset.
- **Deliverable:** Qwen2.5-14B extraction results for comparison
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/llm_reader.py
- **Status:** Complete

#### 5. Prompt Template Adjustments for Qwen2.5-14B
*Development · Model Experimentation*
- Adjusted the chain-of-thought prompts for Qwen's output format.
- **Deliverable:** Qwen-specific prompt templates
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/llm_reader.py
- **Status:** Complete

#### 6. Scorecard Evaluation of Qwen2.5-14B Results
*Development · Model Experimentation*
- Ran the Scorecard on Qwen's extraction output.
- **Deliverable:** Qwen Scorecard evaluation
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/config/settings.py
- **Status:** Complete

#### 7. Compare Error Patterns Across Model Tiers (7B/8B vs. 14B)
*Development · Model Experimentation*
- **Key finding:**
  - Qwen improved calibration on the maintained/none boundary.
  - The resolution plateau persists.
  - All three models struggle equally on genuinely ambiguous text.
- **Conclusion:** the boundary problem is linguistic ambiguity, not model capacity. More parameters won't solve it.
- **Deliverable:** cross-model-tier error analysis; resolution plateau confirmed as structural
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/app.py
- **Status:** Complete

### Pipeline Hardening

#### 8. Input Validation Layer
*Development · Pipeline Hardening*
- Built pre-reader validation that rejects three kinds of chunk:
  - empty
  - boilerplate-only
  - under the minimum token count
- Calibrated the minimum token threshold after a false positive on legitimate short-paragraph content.
- Added a per-ticker override capability.
- **Deliverable:** input validation layer with per-ticker overrides
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/preprocessing/chunk_validator.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/preprocessing/boilerplate.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/config/settings.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/init_db.py
- **Status:** Complete

#### 9. Confidence Gating
*Development · Pipeline Hardening*
- Implemented a minimum confidence threshold.
- Signals below it are logged but excluded from Scorecard evaluation.
- **Deliverable:** confidence gating implemented
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/triangulator.py
- **Status:** Complete

#### 10. Retry Logic for Malformed JSON Output
*Development · Pipeline Hardening*
- Added exponential backoff retry when readers produce malformed JSON.
- **Deliverable:** retry logic with exponential backoff
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/llm_reader.py
- **Status:** Complete

#### 11. Signal Provenance Tracking
*Development · Pipeline Hardening*
- Stores the exact prompt for each signal as an audit trail, including the few-shot examples and temporal context.
- Initial 3x storage inflation reduced to 1.4x baseline with compressed JSON.
- **Deliverable:** signal provenance tracking with compressed storage
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/llm_reader.py
- **Status:** Complete

### Infrastructure

#### 12. Ticker Registry Table + Outcome Resolver Caching Improvements
*Development · Infrastructure*
- Created the ticker registry and a migration from the existing directory structure.
- Improved the caching layer based on issues found in earlier weeks.
- **Deliverable:** ticker registry + improved outcome caching
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/ticker_registry.py
- **Status:** Complete

### Architecture Rework

#### 13. Model Identity Per Chunk + Model Tier as Triangulator Weight
*Development · Architecture Rework*
- Refactored pipeline state to record which model processed each chunk, enabling per-model Scorecard analysis.
- Added model tier as a triangulator weighting factor, adjusted over time by vindication results.
- **Deliverable:** multi-model architecture refactor: per-chunk model tracking + tier-based weighting
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graphs/pipeline_graph.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/triangulator.py
- **Status:** Complete

### Dashboard

#### 14. Three-Model Comparison View + Qwen Metrics
*Development · Dashboard*
- Updated the dashboard for side-by-side comparison across Llama, Mistral, and Qwen.
- Extended the reader comparison table with Qwen metrics.
- **Deliverable:** dashboard updated for three-model support
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/src/ecis/dashboard
- **Status:** Complete

### Debugging

#### 15. Debugging: AWQ Kernel Compatibility + Provenance Storage + Validation False Positives
*Development · Debugging*
- Three issues resolved:
  - **AWQ kernel:** Qwen fell back to CPU for some operations. Fixed by switching to a different checkpoint.
  - **Provenance storage:** storage inflated. Fixed with compressed JSON.
  - **Validation false positives:** input validation rejected legitimate short-paragraph content. Fixed with per-ticker overrides.
- **Deliverable:** three pipeline hardening bugs resolved
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/tests
- **Status:** Complete

### Research

#### 16. Qwen2.5-14B Architecture, Capabilities, and Quantization
*Research · Compute / LLM*
- Researched Qwen's architecture, known behaviors, and AWQ quantization configuration.
- **Deliverable:** Qwen technical assessment
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 17. Architecture Review and System Design Exploration
*Research · Architecture*
- Reviewed the overall system architecture.
- Explored design options for the multi-model pipeline in light of the resolution plateau finding.
- **Deliverable:** architecture review; strategic direction assessment
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/architecture
- **Status:** Complete

### Artifacts

#### 18. Parameter Budget Calculator
*Artifact · Claude Artifact*
- Interactive artifact.
- **Inputs:** model size, quantization level, chunk count.
- **Outputs:** estimated VRAM usage, inference time, and compute units.
- **Deliverable:** Claude Artifact: Parameter Budget Calculator
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

#### 19. Three-Model Arena
*Artifact · Claude Artifact*
- Interactive artifact showing Llama, Mistral, and Qwen extractions on the same chunk side by side.
- Includes disagreement highlighting and a triangulator resolution view.
- **Deliverable:** Claude Artifact: Three-Model Arena
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### Video

Both videos follow the same split.
- **Concept, ideas, narration, and direction:** original work.
- **Assembly:** Claude, using the video generation tool created by Humanitarians AI.

#### 20. Video: "Attention in Finance Explained"
*Video · Video Production*
- Thematic video connecting attention mechanisms to the earnings call extraction task.
- Shows how transformer attention patterns apply to financial text analysis.
- **Deliverable:** Video: Attention in Finance Explained
- **Links:**
  - https://www.youtube.com/watch?v=UXW3ar6AWu0
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-21-attention-finance-explained
  - https://drive.google.com/drive/folders/1L18a_VtyzobdgiPDmQ3DM2pVAZ_r-CVy
- **Status:** Complete

#### 21. Video: "ECIS Explained (EP3)"
*Video · Video Production*
- Weekly progress episode covering the three-model comparison, pipeline hardening, and Scorecard evaluation results.
- **Deliverable:** Video: ECIS Explained (EP3)
- **Links:**
  - https://www.youtube.com/watch?v=djilegdvCgM
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-21-ecis-explained
  - https://drive.google.com/drive/folders/1WDuTTxWatMc8jeUoSQiSEjI0Z45TKGa0
- **Status:** Complete
