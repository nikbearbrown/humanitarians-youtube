# Weekly Report: Week 9 (Phase 9)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard
**Week:** August 23 – August 29, 2026
**Total hours:** 29.25

---

## Summary

- Three new features built, each with its own before/after Scorecard evaluation:
  - **Speaker-weighted extraction** (CFO 1.0, CEO 0.8, analyst 0.3): Brier score improved, mainly by suppressing false positives from analyst speculation in Q&A.
  - **Chunk quality scoring:** ECE improved; low-quality chunks were the main source of overconfident wrong extractions.
  - **Retrospective temporal linking:** consecutive raises showed marginally higher information ratios. Reported as directionally interesting, insufficient sample (only 12 reversals).
- Qwen2.5-14B extraction extended to additional tickers with refined prompts.
- Three-model Scorecard comparison updated with the expanded data.
- Outputs: two Claude artifacts, two Substack articles, and two videos.

---

## Work Completed

### Model Expansion

#### 1. Run Qwen2.5-14B Extraction Across Additional Tickers
*Development · Model Expansion*
- Extended Qwen extraction to additional tickers.
- **Deliverable:** expanded Qwen extraction dataset
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/llm_reader.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graphs/pipeline_graph.py
- **Status:** Complete

#### 2. Refine Qwen Prompt Templates
*Development · Model Expansion*
- Refined the chain-of-thought prompts based on initial Qwen results.
- **Deliverable:** updated Qwen prompt templates
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/llm_reader.py
- **Status:** Complete

#### 3. Updated Three-Model Scorecard Comparison
*Development · Model Expansion*
- Ran the Scorecard across all three models with the expanded data.
- **Deliverable:** three-model Scorecard comparison (expanded)
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
- **Status:** Complete

### Speaker-Weighted Extraction

#### 4. Speaker Role Lookup + Weight Multiplier Configuration
*Development · Speaker-Weighted Extraction*
- Built a role lookup from the existing speaker normalization.
- Set weight values: CFO 1.0, CEO 0.8, analyst 0.3, with other roles scaled in between.
- Analyst weight kept at 0.3 rather than 0.0. This retains cases where analysts surfaced guidance that the company then confirmed.
- **Deliverable:** speaker role lookup + calibrated weight multipliers
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/speaker_roles.py
- **Status:** Complete

#### 5. Integrate Speaker Weight into Triangulator
*Development · Speaker-Weighted Extraction*
- Wired the speaker weight multiplier into the triangulator's signal combination logic.
- **Deliverable:** speaker weighting integrated into triangulation
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/triangulator.py
- **Status:** Complete

#### 6. Scorecard Before-and-After with Speaker Weighting
*Development · Speaker-Weighted Extraction*
- Brier score improved, driven by suppressing false positives from Q&A sections where analyst speculation had been treated as company guidance.
- The 0.3 analyst threshold was validated.
- **Deliverable:** before/after Scorecard evaluation; speaker weighting validated
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
- **Status:** Complete

### Chunk Quality Scoring

#### 7. Chunk Quality Score: Boilerplate Ratio + Token Count + Section Completeness + Speaker Transitions
*Development · Chunk Quality Scoring*
- Scored each chunk on four quality dimensions:
  - boilerplate ratio
  - token count
  - section completeness
  - speaker transitions
- Built a composite 0–1 quality score with iterated weights.
- Boilerplate ratio dominates, as the strongest predictor of extraction error.
- **Deliverable:** composite chunk quality scoring module
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
- **Status:** Complete

#### 8. Integrate Quality Score into Triangulator
*Development · Chunk Quality Scoring*
- Wired the quality score in as a multiplier in the triangulator's combination logic.
- **Deliverable:** quality scoring integrated into triangulation
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/triangulator.py
- **Status:** Complete

#### 9. Scorecard Before-and-After with Quality Scoring
*Development · Chunk Quality Scoring*
- ECE improved.
- Low-quality chunks were the primary source of overconfident wrong extractions. Removing their influence cleaned up the calibration curve.
- **Deliverable:** before/after Scorecard evaluation; quality scoring validated
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
- **Status:** Complete

### Temporal Linking

#### 10. Retrospective Temporal Linking: Query, Pattern Detection, and Trend Labeling
*Development · Temporal Linking*
- Built a temporal query that groups signals by ticker in chronological order.
- Detected consecutive direction patterns and assigned one of five trend labels:
  - `consecutive_raise`
  - `consecutive_lower`
  - `reversal`
  - `single`
  - `stable_maintained`
- Persisted the trend fields to the signal records.
- **Deliverable:** temporal linking module with trend labeling
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/temporal_linking.py
- **Status:** Complete

#### 11. Scorecard Evaluation of Trend-Tagged vs. Isolated Signals
*Development · Temporal Linking*
- Consecutive raises showed marginally higher information ratios than isolated raises.
- Reversals showed the strongest signal, but there are only 12 examples in the dataset.
- Result reported as directionally interesting with an insufficient sample, not claimed as validated.
- **Deliverable:** trend evaluation results; directionally interesting, insufficient sample
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
- **Status:** Complete

### Pipeline

#### 12. Re-Run Extraction with All New Features Enabled
*Development · Pipeline*
- Ran the full pipeline on a representative subset with speaker weighting, chunk quality scoring, and temporal linking all active.
- **Deliverable:** full pipeline execution with all new features
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/triangulator.py
- **Status:** Complete

### Scoring / Evaluation

#### 13. Full Scorecard Evaluation with Updated Signal Set
*Development · Scoring / Evaluation*
- Complete evaluation across the expanded, feature-enhanced signal set.
- **Deliverable:** updated Scorecard evaluation
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
- **Status:** Complete

### Debugging

#### 14. Debugging: Speaker Normalization + Quality/Gate Double-Filtering + Temporal Fiscal Calendars
*Development · Debugging*
- Three issues resolved:
  - **Speaker names:** first-name-only speaker references needed fuzzy matching. Missed matches default high, so company statements aren't suppressed.
  - **Double-filtering:** quality scoring and the confidence gate were filtering the same signals twice. Quality is now applied before the gate.
  - **Fiscal calendars:** temporal linking was thrown off by inconsistent fiscal calendars. It now sorts by transcript date, not quarter label.
- **Deliverable:** three feature-integration bugs resolved
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/tests
- **Status:** Complete

### Research

#### 15. Architecture Review for New Feature Integration
*Research · Architecture*
- Reviewed how speaker weighting, quality scoring, and temporal linking interact within the existing pipeline.
- Evaluated whether the features compound, conflict, or operate independently.
- **Deliverable:** feature interaction assessment
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/docs/architecture/ecis_system_architecture.png
- **Status:** Complete

#### 16. Qwen2.5-14B Technical Research
*Research · Compute / LLM*
- Continued research on Qwen's architecture, quantization behavior, and tokenizer characteristics.
- **Deliverable:** Qwen technical research
- **Status:** Complete

#### 17. Fine-Tuning Methodology Research
*Research · Model Optimization*
- Studied QLoRA adapter strategies, rank selection, and training data preparation for planned fine-tuning work.
- **Deliverable:** fine-tuning preparatory research
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

### Artifacts

#### 18. Speaker Weight Impact Visualizer
*Artifact · Claude Artifact*
- Interactive artifact: toggle speaker weighting on or off and see how triangulated confidence shifts for each signal.
- Shows which signals the weighting change affects most.
- **Deliverable:** Claude Artifact: Speaker Weight Impact Visualizer
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

#### 19. Scorecard Comparison Grid
*Artifact · Claude Artifact*
- Interactive artifact showing before/after metrics side by side, with animated deltas.
- Shows the impact of each new feature on the Scorecard.
- **Deliverable:** Claude Artifact: Scorecard Comparison Grid
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### Writing

#### 20. Substack Article: "Qwen2.5-14B vs. 8B Extraction"
*Writing · Substack Article*
- Compares 14B and 8B model performance on earnings call extraction.
- Uses the comparison to ground the resolution plateau confirmation and its implications for scaling strategy.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/qwen-14b-vs-8b-parameter-scaling-extraction
- **Status:** Complete (published)

#### 21. Substack Article: "Byte-Level BPE vs. WordPiece"
*Writing · Substack Article*
- Examines the tokenizer architecture difference between Qwen/Llama (BPE) and FinBERT (WordPiece).
- Shows how that difference affects chunk alignment across the multi-model pipeline.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/byte-bpe-vs-wordpiece-tokenizer-financial-extraction
- **Status:** Complete (published)

### Video

Both videos follow the same split.
- **Concept, ideas, narration, and direction:** original work.
- **Assembly:** Claude, using the video generation tool created by Humanitarians AI.

#### 22. Video: "ECIS Episode 4 — Not Just What. Who, How Clean, and What Came Before"
*Video · Video Production*
- Weekly progress video covering this week's new features: speaker weighting, chunk quality scoring, and temporal linking.
- **Deliverable:** Video: ECIS EP4
- **Links:**
  - https://www.youtube.com/watch?v=CTM32FIoXxg
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-28-ecis-explained
  - https://drive.google.com/drive/folders/1mkIsMtJORDsH8bME_JjRuRmjJKEFA7Fa
- **Status:** Complete

#### 23. Video: "What Temperature Does to an LLM's Financial Predictions"
*Video · Video Production*
- Thematic video exploring how temperature variation affects LLM extraction stability and confidence in financial text analysis.
- **Deliverable:** Video: What Temperature Does to an LLM's Financial Predictions
- **Links:**
  - https://www.youtube.com/watch?v=6In_XgcBxug
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-28-temperature-llm-finance
  - https://drive.google.com/drive/folders/1uUpYVoeHUYE7Y3DkesHrtUiiWL76USo-
- **Status:** Complete
