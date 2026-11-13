# Weekly Report: Week 10 (Phase 10)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard
**Week:** August 30 – September 5, 2026
**Total hours:** 28.5

---

## Summary

- Qwen2.5-14B extraction completed across the full ticker set, with a final three-model Scorecard comparison.
- Second QLoRA round, trained on corrected reasoning traces:
  - Brier skill score improved by 0.09, above the 0.05 threshold.
  - Resolution moved slightly for the first time.
  - Assessed as promising, not proven.
- Six new features built and integrated:
  - abstention calibration
  - section-weighted extraction
  - signal decay tracking
  - negation detection
  - guidance keyword density
  - duplicate transcript detection
- Signal decay finding: raised signals are accurate at 30 days but degrade at 180 days. Reversals show the opposite pattern.
- Outputs: two Claude artifacts, two Substack articles, and two videos.

---

## Work Completed

### Model Expansion

#### 1. Complete Qwen2.5-14B Extraction Across Remaining Tickers
*Development · Model Expansion*
- Final extraction run across the remaining ticker set.
- **Deliverable:** Qwen extraction complete across full ticker set
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/
- **Status:** Complete

### Scoring / Evaluation

#### 2. Final Three-Model Scorecard Comparison with Full Data
*Development · Scoring / Evaluation*
- Ran the complete Scorecard across all three models (Llama, Mistral, Qwen) on the full dataset, giving the definitive cross-model comparison.
- **Deliverable:** final three-model Scorecard comparison
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

### Model Optimization

#### 3. Format Training Triples with Reasoning Traces as JSONL
*Development · Model Optimization*
- Prepared training data with corrected reasoning traces alongside the labels.
- Hypothesis: including reasoning traces teaches discrimination rather than just recalibration.
- **Deliverable:** JSONL training dataset with reasoning traces
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

#### 4. Load Llama 3.1 8B with NF4 via Unsloth on Colab A100
*Development · Model Optimization*
- Model loading and quantization configuration for the second fine-tuning round.
- **Deliverable:** base model loaded with NF4 quantization
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/notebooks/colab/qlora_finetune.ipynb
- **Status:** Complete

#### 5. Configure LoRA Rank-16 Adapters + Run Training
*Development · Model Optimization*
- Ran training with the checkpoint interval set to 100 steps, applying the lesson from the Week 7 Colab disconnect.
- **Deliverable:** fine-tuned LoRA adapter (rank-16, round 2)
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/notebooks/colab/qlora_finetune.ipynb
- **Status:** Complete

#### 6. Scorecard Before-and-After on Held-Out Data
*Development · Model Optimization*
- Skill score improved by 0.09, above the 0.05 threshold.
- Calibration improved further on the maintained/none boundary.
- Resolution moved slightly for the first time. The reasoning traces may be teaching discrimination, not just recalibration.
- The improvement is small enough to be noise at this sample size, so it is assessed as promising, not proven.
- **Deliverable:** before/after Scorecard; 0.09 skill score improvement; first resolution movement observed
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
- **Status:** Complete

#### 7. Integrate Fine-Tuned Adapter into Extraction Pipeline
*Development · Model Optimization*
- Loaded the updated adapter into the production pipeline.
- **Deliverable:** fine-tuned adapter (round 2) integrated into pipeline
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/finetuned_guard.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/config/settings.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graphs/watchdog_graph.py
- **Status:** Complete

### Feature Development

#### 8. Abstention Calibration: Proportional Confidence Penalty
*Development · Feature Development*
- Replaced the flat 0.15 penalty with a penalty proportional to the vote spread in self-consistency decoding.
- Tested linear, logarithmic, and step functions against the Scorecard.
- Linear improved ECE without increasing the abstention rate.
- **Deliverable:** abstention calibration with proportional penalty (linear)
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/llm_reader.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/config/settings.py
- **Status:** Complete

#### 9. Section-Weighted Extraction
*Development · Feature Development*
- Prepared remarks are weighted higher than Q&A in the triangulator.
- Extends the Week 9 speaker weighting: section context and speaker role now both inform signal confidence.
- **Deliverable:** section-weighted extraction integrated into triangulator
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/triangulator.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/config/settings.py
- **Status:** Complete

#### 10. Signal Decay Tracking: Multi-Horizon Scorecard Accuracy
*Development · Feature Development*
- Compared Scorecard accuracy across 30-, 90-, and 180-day horizons for each signal type.
- **Raised signals:** most are correct at 30 days but degrade at 180 days.
- **Reversals:** show the opposite pattern, a delayed signal that becomes more accurate at longer horizons.
- **Deliverable:** signal decay tracking across 30/90/180-day horizons
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/signal_decay.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

#### 11. Negation Detection Flag
*Development · Feature Development*
- Tags negation patterns in chunks and forces Category B routing for them.
- This sends negated content through the LLM reader rather than relying on FinBERT alone.
- **Deliverable:** negation detection with routing override
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/negation.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graphs/pipeline_graph.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graphs/orchestration_agent.py
- **Status:** Complete

#### 12. Guidance Keyword Density Score
*Development · Feature Development*
- Counts taxonomy phrase frequency relative to chunk length.
- Feeds into the triangulator as an additional signal quality dimension.
- **Deliverable:** keyword density scoring integrated into triangulator
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/keyword_density.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/triangulator.py
- **Status:** Complete

#### 13. Duplicate Transcript Detection
*Development · Feature Development*
- Hashes normalized transcript text to skip re-extraction on duplicates.
- Fixed an amended-filing edge case by hashing only the transcript body, not the full filing.
- **Deliverable:** duplicate transcript detection via content hashing
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/duplicate_transcripts.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graphs/pipeline_graph.py
- **Status:** Complete

### Pipeline

#### 14. Re-Run Extraction with Fine-Tuned Model and All New Features
*Development · Pipeline*
- Full pipeline run on a representative subset, with the updated adapter and all six new features active.
- **Deliverable:** full pipeline execution with fine-tuned model + all new features
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graphs/pipeline_graph.py
- **Status:** Complete

### Scoring / Evaluation

#### 15. Full Scorecard Evaluation: Base vs. Fine-Tuned with New Features
*Development · Scoring / Evaluation*
- Complete evaluation confirming that three things compose without interfering:
  - the five triangulator weight dimensions
  - the negation routing overrides
  - the fine-tuned adapter
- Integration complexity exceeds the sum of the individual features.
- **Deliverable:** full base vs. fine-tuned Scorecard evaluation with all features
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/scoring/scorer.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/main.py
- **Status:** Complete

### Debugging

#### 16. Debugging and Issue Resolution
*Development · Debugging*
- Two design-level edge cases in the new features resolved:
  - abstention calibration interacting with the existing confidence gating
  - duplicate detection failing on amended filings
- **Deliverable:** two feature-integration bugs resolved
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/llm_reader.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/triangulator.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/duplicate_transcripts.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/tests/test_remaining.py
- **Status:** Complete

### Research

#### 17. Analysis of Fine-Tuning Results: Resolution Movement Interpretation
*Research · Model Optimization*
- Analyzed the second QLoRA round's results.
- Questions: is the resolution movement signal or noise, and what does it imply about the effectiveness of reasoning traces in training data?
- **Deliverable:** fine-tuning results analysis; resolution movement assessment
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 18. Study of Post-Training and Fine-Tuning Methods
*Research · Model Optimization*
- Studied post-training techniques and fine-tuning methodology more broadly.
- **Deliverable:** post-training and fine-tuning research
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

### Artifacts

#### 19. Five-Dimension Weight Calculator
*Artifact · Claude Artifact*
- Interactive artifact: input all five triangulator dimensions for a signal (reader, model, speaker, quality, section).
- Shows the multiplicative composition, the final confidence, and the dominant factor.
- Sliders let you explore threshold effects and confidence cliffs.
- **Deliverable:** Claude Artifact: Five-Dimension Weight Calculator
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

#### 20. QLoRA Before-and-After Dashboard
*Artifact · Claude Artifact*
- Interactive artifact comparing base and fine-tuned model metrics side by side, with animated transitions.
- Drill into the maintained/none boundary to see the targeted impact.
- **Deliverable:** Claude Artifact: QLoRA Before-and-After Dashboard
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### Writing

#### 21. Substack Article: "Five Weight Dimensions in One Triangulator"
*Writing · Substack Article*
- Explains how the five triangulator weight dimensions compose multiplicatively.
- Shows where confidence cliffs emerge from their interaction.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/five-weight-triangulator-confidence-composition
- **Status:** Complete (published)

#### 22. Substack Article: "QLoRA on the Maintained/None Boundary"
*Writing · Substack Article*
- Reports the second QLoRA round's results, focusing on the calibration/resolution split and the reasoning trace hypothesis.
- Distinguishes what fine-tuning fixed from what it didn't.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/qlora-maintained-none-boundary-fine-tuning
- **Status:** Complete (published)

### Video

Both videos follow the same split:
- **Concept, ideas, narration, and direction:** original work.
- **Assembly:** Claude, using the video generation tool created by Humanitarians AI.

#### 23. Video: "ECIS Episode 5 — Five Dimensions of Confidence"
*Video · Video Production*
- Weekly Mycroft project update covering:
  - the five-dimension triangulator (reader, model, speaker, quality, section)
  - the second QLoRA round's results
  - the resolution movement finding
- **Deliverable:** Video: ECIS EP5
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-04-ecis-explained
  - https://drive.google.com/drive/folders/1J3DRtBHoVtfc3tghfY1pRRKdsmFN-vXv
- **Status:** Complete

#### 24. Video: "What Happens Inside a Financial Chatbot"
*Video · Video Production*
- STEM explainer on what happens under the hood when a financial chatbot processes earnings call text.
- Walks from tokenization and embedding through sentiment classification, signal extraction, and confidence scoring.
- **Deliverable:** Video: What Happens Inside a Financial Chatbot
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-04-financial-chatbot
  - https://drive.google.com/drive/folders/1fEE7UbuwOQMApJnv9naIvZfgio5RKTQ4
- **Status:** Complete
