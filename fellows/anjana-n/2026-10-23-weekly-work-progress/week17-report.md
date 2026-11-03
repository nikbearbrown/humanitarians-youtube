# Weekly Report: Week 17 (Phase 17)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard
**Week:** October 18 – October 24, 2026
**Total hours:** 33.0

---

## Summary

- **Signal quality and coverage:**
  - signal decay analysis by type
  - false positive analysis with pattern-based filtering rules
  - multi-quarter signal chaining
  - earnings call quality gates
- **Linguistic depth beyond sentiment:**
  - speech act classification (promises, commitments, hedged intentions, deflections)
  - discourse structure analysis (front-loading vs. burying bad news)
  - metaphor tracking
  - sarcasm detection
- **Feature engineering:** automated feature selection dropped four low-value features and lifted LightGBM AUC from 0.72 to 0.74.
- **Key finding:** dodge score, rising hedging, and defensive language interact. Together they predict negative guidance revisions at 2x the base rate, which none of them shows alone.
- **Embedding drift monitoring** added for the Sentence-BERT space.
- **Outputs:**
  - two  artifacts
  - one Substack article
  - two videos

---

## Work Completed

### Signal Quality & Coverage

#### 1. Signal Decay Analysis by Type
*Development · Signal Quality & Coverage*
- Measures how quickly each signal type loses predictive value across evaluation horizons.
- Identifies which signal categories produce lasting predictions and which are transient.
- **Deliverable:** signal decay analysis module with per-type decay profiles
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/depth/decay_by_type.py
- **Status:** Complete

#### 2. False Positive Analysis
*Development · Signal Quality & Coverage*
- Systematic study of high-confidence wrong predictions.
- Identified recurring error patterns and built filtering rules that suppress false positive signals.
- **Deliverable:** false positive analysis report with pattern-based filtering rules
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/depth/false_positives.py
- **Status:** Complete

#### 3. Multi-Quarter Signal Chaining
*Development · Signal Quality & Coverage*
- Tracks trends across consecutive quarters.
- Weights sustained directional patterns differently from single-quarter spikes.
- **Deliverable:** multi-quarter signal chaining module with trend weighting
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/depth/chaining.py
- **Status:** Complete

#### 4. Earnings Call Quality Scoring
*Development · Signal Quality & Coverage*
- Quality gates catch three problems before extraction:
  - poor transcription
  - missing Q&A sections
  - truncated content
- Keeps low-quality inputs from degrading extraction accuracy.
- **Deliverable:** earnings call quality gate with transcription scoring
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/depth/call_quality.py
- **Status:** Complete

### Linguistic Depth

#### 5. Speech Act Classification
*Development · Linguistic Depth*
- Classifies executive language in earnings calls into four kinds of statement:
  - promises
  - commitments
  - hedged intentions
  - deflections
- **Deliverable:** speech act classification module for financial text
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/depth/speech_acts.py
- **Status:** Complete

#### 6. Discourse Structure Analysis
*Development · Linguistic Depth*
- Detects whether management front-loads or buries bad news in earnings call transcripts.
- Scores where information is placed within the call.
- **Deliverable:** discourse structure analysis module with information placement scoring
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/depth/discourse.py
- **Status:** Complete

#### 7. Metaphor & Analogy Tracking
*Development · Linguistic Depth*
- Flags shifts from concrete to metaphor-heavy language as a potential evasion indicator in management communication.
- **Deliverable:** metaphor tracking module with evasion flagging
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/depth/metaphor.py
- **Status:** Complete

#### 8. Sarcasm & Irony Detection
*Development · Linguistic Depth*
- Context-aware sarcasm and irony detection for Q&A sections.
- Prevents sentiment misreads where standard sentiment models misinterpret analyst or management tone.
- **Deliverable:** context-aware sarcasm detection module for Q&A sections
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/depth/sarcasm.py
- **Status:** Complete

### Feature Engineering

#### 9. Automated Feature Selection
*Development · Feature Engineering*
- Identifies and drops features that add noise to the prediction pipeline.
- Improves model parsimony and generalization.
- Four features dropped:
  - raw transcript length
  - absolute Q&A word count
  - a redundant hedging variant (r = 0.91 with the primary hedging index)
  - an early-version keyword density score
- LightGBM AUC improved from 0.72 to 0.74 after pruning.
- **Deliverable:** automated feature selection module with noise reduction
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/depth/feature_select.py
- **Status:** Complete

#### 10. Feature Interaction Discovery
*Development · Feature Engineering*
- Explicit search for feature combinations that improve prediction beyond individual features.
- **Promoted:** dodge score + rising hedging + defensive language. It predicts negative revisions at 2x the base rate and was added to the feature vector.
- **Monitoring:** metaphor density + declining numerical specificity. Statistically significant, but its lift was marginal.
- **Deliverable:** feature interaction discovery module with combination testing
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/depth/interactions.py
- **Status:** Complete

#### 11. Embedding Drift Monitoring
*Development · Feature Engineering*
- Monitors the stability of the Sentence-BERT embedding space over time.
- Alerts when the embedding distribution shifts beyond acceptable thresholds.
- **Deliverable:** embedding drift monitoring module with stability alerts
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/depth/embedding_drift.py
- **Status:** Complete

### Dashboard

#### 12. Signal Chain, Quality Gate & Linguistic Analysis Views
*Development · Dashboard*
- Added four dashboard views:
  - signal chain trend visualization
  - quality gate indicators
  - speech act breakdowns
  - updated feature importance displays
- **Deliverable:** dashboard views for signal chains, quality gates, and linguistic analysis
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

### Debugging

#### 13. Debugging & Issue Resolution
*Development · Debugging*
- Identified and resolved issues across the pipeline. The main ones:
  - sarcasm false positives on financial idioms
  - DeBERTa class imbalance in speech act training data
  - choosing the window size for discourse structure detection
- **Deliverable:** resolved issues and verified fixes
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/tests/test_phase17.py
- **Status:** Complete

### Research

#### 14. Multi-Quarter Signal Chaining & Temporal Sequence Modeling Research
*Research · Temporal Modeling*
- Researched multi-quarter signal chaining and temporal sequence modeling for tracking sustained guidance patterns across consecutive quarters.
- **Deliverable:** research notes on temporal signal chaining methods
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 15. Speech Act Classification & Discourse Analysis Research
*Research · Discourse Analysis*
- Researched speech act classification and discourse analysis techniques for financial text.
- Covered promise detection, commitment identification, and information structure analysis.
- **Deliverable:** research notes on speech act classification in financial NLP
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 16. Automated Feature Selection & Embedding Stability Research
*Research · Feature Engineering*
- Researched automated feature selection methods and embedding stability monitoring for keeping models robust over time.
- **Deliverable:** research notes on feature selection and embedding drift methods
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

### Writing

#### 17. Substack Article: "Quantizing the Readers Nobody Thinks About"
*Writing · Substack Article*
- Argues that ML pipelines over-optimize the LLM while ignoring the BERT-class models that run on every chunk.
- Walks through int8 quantization for faster inference and embedding quantization for more efficient vector search.
- Frames precision loss against inter-checkpoint variance thresholds.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/quantizing-finbert-embeddings-bert-inference-optimization
- **Status:** Complete (published)

### Artifacts

#### 18. Interactive System Architecture Map
*Artifact · Claude Artifact*
- Interactive diagram of the full ECIS pipeline across all 17 phases.
- Clickable nodes for ingestion, extraction, triangulation, and prediction show data flow, inputs, and outputs.
- **Deliverable:** Claude Artifact: Interactive System Architecture Map
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

#### 19. Earnings Call Quality Scorecard
*Artifact · Claude Artifact*
- Mock scorecard showing how the system grades a transcript before analysis.
- Covers completeness, Q&A depth, speaker coverage, and coherence, with pass/fail quality gate thresholds.
- **Deliverable:** Claude Artifact: Earnings Call Quality Scorecard
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### Video

Both videos follow the same split.
- **Concept, ideas, narration, and direction:** original work.
- **Assembly:** Claude, using the video generation tool created by Humanitarians AI.

#### 20. Video: "ECIS Episode 12: Weekly Project Update"
*Documentation · Video Production*
- Weekly Mycroft ECIS project update covering Week 17 progress, including the signal quality analysis and linguistic depth modules.
- **Deliverable:** Video: ECIS Episode 12
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-23-ecis-explained
  - https://drive.google.com/drive/folders/1C3bVEFbFXSPx_5HNcWsR8mjMULJ6WKLW
- **Status:** Complete

#### 21. Video: "Multimodal RAG Explainer: Retrieving Images, Tables, and Code"
*Documentation · Video Production*
- STEM educational video on multimodal RAG architecture.
- Covers embedding non-text content, layout-aware chunking, and structured extraction before embedding.
- **Deliverable:** Video: Multimodal RAG Explainer
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-23-multimodal-rag-explainer
  - https://drive.google.com/drive/folders/1IDobtpnYhC_zRlGh6yAqbD65gmPp7OBE
- **Status:** Complete
