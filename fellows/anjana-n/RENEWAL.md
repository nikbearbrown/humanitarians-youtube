# Renewal Log — Mycroft ECIS

## The Project

ECIS (Earnings Call Intelligence Signals) is a financial intelligence system that transforms raw earnings call transcripts into structured, confidence-scored guidance signals, and then holds itself accountable by grading every prediction against real market outcomes.

- **Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)
- **Current reporting period:** August 1 – October 31, 2026 

## Summary of Work

Built a complete earnings call intelligence system from scratch that ingests SEC EDGAR filings and Financial Modeling Prep transcripts for 25 AI-sector companies, extracts forward-looking guidance signals using three base language models (Llama 3.1 8B, Mistral-7B, Qwen2.5-14B) plus a QLoRA fine-tuned adapter, and predicts next-quarter guidance direction and revision probability.

Designed a multi-reader extraction architecture where FinBERT sentiment, keyword matching, NER, and LLM chain-of-thought extraction run through a LangGraph orchestration graph with fast-pass routing, escalation classification, and conflict resolution. A triangulator combines outputs across five weight dimensions (reader, model, speaker role, chunk quality, section type) with dynamic weights updated by feedback loops.

Built a prediction layer that forecasts guidance direction from historical signal features, stock momentum, sector aggregates, analyst consensus, and linguistic features, with all predictions pre-registered in an append-only log and graded by a Scorecard with bootstrap confidence intervals and paired permutation tests. Added a guidance revision predictor using six models (logistic regression, XGBoost, Random Forest, LightGBM, MLP, CatBoost).

Developed a full business analytics layer: sector sentiment aggregation with a composite mood index, cross-sector benchmarking, management confidence scoring, CEO-CFO tone divergence detection, guidance language specificity tracking, signal-to-price correlation analysis, three-way surprise score decomposition, and multi-horizon reaction window curves at 1/2/5/10/30 days.

Built advanced Q&A analytics including a dodge score system with cross-encoder reranking and question type weighting that detects when executives evade analyst questions, weighted by question importance. Added market share language scoring using three classifiers (lexicon-based, zero-shot BART-MNLI, stance detection) ensembled to place each call on an offensive-defensive spectrum with quarterly shift tracking.

Developed linguistic depth analysis beyond sentiment: speech act classification (promises vs hedged intentions vs deflections), discourse structure detection (front-loading vs burying bad news), metaphor density tracking, and sarcasm detection for Q&A exchanges. These capture dimensions of executive communication that sentiment analysis alone misses entirely.

Built signal reliability infrastructure: per-signal-type decay half-lives, false positive pattern clustering with confidence modifiers, multi-quarter signal chaining for sustained trend detection, and earnings call quality scoring as a gate before downstream analytics.

Automated feature engineering maintenance across numerous features with three-method consensus pruning, pairwise interaction discovery via ANOVA, and embedding drift monitoring alongside feature-level concept drift detection with PSI/KL divergence.

Migrated the data layer from SQLite to PostgreSQL with TimescaleDB for time-series optimization, Alembic schema versioning, composite indexing, materialized views, and connection pooling. Optimized ChromaDB with embedding versioning, tuned HNSW indexes, and rebalanced exemplar stores.

Built a Streamlit dashboard covering signal exploration, three-model comparison, calibration curves, prediction timelines, sector analytics, management behavior tracking, dodge score trends, market share language timelines, guidance revision probabilities, signal decay curves, false positive patterns, speech act distributions, discourse structure, feature importance rankings, and more. Added Grafana monitoring for reader health, extraction latency, signal throughput, data quality, and embedding drift with threshold alerting.

Implemented data lineage tracking tracing each signal from raw transcript through every transformation to the decision log. Added three feedback loops plus concept drift detection, prediction decay tracking, and embedding drift monitoring. Built input validation, confidence gating, retry logic, negation detection, abstention calibration, section-weighted extraction, and duplicate transcript detection throughout the pipeline.

---

## Weekly Log

### Week 1 (Phase 1): Proposal, architecture, and reformulation
**Jun 29 – Jul 4, 2026** · **21 hrs**

**Work completed**
- Project proposal and initial system architecture for ECIS and the Decision Scorecard.
- Codebase review reformulated the design: ECIS and the Scorecard are built as recipes inside Mycroft's governance framework, reusing its trust loop.
- Seam schema and first ingest scaffold built to the corrected model.

**Evidence**
- **Work folder** (report, friction log, README): [2026-07-03-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-07-03-weekly-work-progress)
- **Substack:**
  - [When the Earnings Call Ends, Who Was Really Listening?](https://mycroftproject.substack.com/p/earnings-call-ai-retail-investor-gap)
  - [Your Data Has Two States: What You Got, and What You're Allowed to Trust](https://mycroftproject.substack.com/p/data-two-states)

---

### Week 2 (Phase 2): Data layer on real transcripts
**Jul 5 – Jul 11, 2026** · **21 hrs**

**Work completed**
- Ingestion from EDGAR and FMP with provenance recording.
- Pydantic signal schema as the ECIS → Scorecard contract.
- Normalization, section-aware chunking for FinBERT's 512-token window, embeddings, and ChromaDB storage.

**Evidence**
- **Work folder** (report, friction log, README): [2026-07-10-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-07-10-weekly-work-progress)
- **Substack:**
  - [FinBERT's 512-Token Blind Spot](https://mycroftproject.substack.com/p/finbert-512-token-chunking-sentiment-classification)
  - [Designing a Metadata Schema for Financial Vector Stores](https://mycroftproject.substack.com/p/designing-a-metadata-schema-for-financial)
---

### Week 3 (Phase 3): Extraction layer
**Jul 12 – Jul 18, 2026** · **29 hrs**

**Work completed**
- Four readers: keyword (baseline), FinBERT, NER (spaCy), and LLM (Llama 3.1 8B).
- LLM reader with chain-of-thought prompts, few-shot retrieval, self-consistency decoding, verification, and temporal retrieval.
- Triangulator with dynamic weighting and a semantic deduplicator; SQLite and LangGraph infrastructure.

**Evidence**
- **Work folder** (report, friction log, README): [2026-07-17-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-07-17-weekly-work-progress)
- **Substack:**
  - [Temperature Sweeps as a Confidence Diagnostic in Financial NLP](https://mycroftproject.substack.com/p/temperature-sweeps-confidence-financial-nlp)
  - [Self-Consistency Decoding as a Hallucination Filter](https://mycroftproject.substack.com/p/self-consistency-hallucination-filter-financial-nlp)
---

### Week 4 (Phase 4): Orchestration, scoring, and dashboard
**Jul 19 – Jul 25, 2026** · **27.5 hrs**

**Work completed**
- End-to-end LangGraph pipeline with an A/B/C/D escalation classifier and a conflict resolution subgraph.
- Point-in-time-safe outcome resolver; Brier, skill score, ECE, Murphy decomposition; Platt and isotonic recalibration.
- Streamlit dashboard with four views.

**Evidence**
- **Work folder** (report, friction log, README): [2026-07-24-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-07-24-weekly-work-progress)
- **Substack:**
  - [Attention Patterns in FinBERT](https://mycroftproject.substack.com/p/attention-patterns-in-finbert-what)

---

### Week 5 (Phase 5): Scaling and validation
**Jul 26 – Aug 1, 2026** · **27 hrs**

**Work completed**
- Expanded to 10–15 AI-sector tickers; first multi-ticker Scorecard evaluation.
- Calibration watchdog, orchestration learning graph, and vindication aggregation deployed with empirically derived thresholds.
- Fine-tuning decision resolved: targeted fine-tuning on the maintained/none boundary.

**Evidence**
- **Work folder** (report, friction log, README): [2026-07-31-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-07-31-weekly-work-progress)
- **Substack:**
  - [When to Stop Prompting and Start Fine-Tuning](https://mycroftproject.substack.com/p/when-to-stop-prompting-start-fine-tuning)

---

### Week 6 (Phase 6): Model experimentation
**Aug 2 – Aug 8, 2026** · **32 hrs**

**Work completed**
- Mistral-7B integrated alongside Llama 3.1 8B.
- Key finding: the models fail in complementary ways. Llama's errors are calibration-heavy; Mistral's are resolution-heavy.
- First full feedback-loop cycle observed; first project videos produced.

**Evidence**
- **Work folder** (report, friction log, README): [2026-08-07-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-07-weekly-work-progress)
- **Videos:**
  - **Weekly implementation:** ECIS Explained — [YouTube](https://www.youtube.com/watch?v=3mxjvm85JNg) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-07-ecis-explained)
  - **STEM/AI:** Why AI Dominates the Crypto Market — [YouTube](https://www.youtube.com/watch?v=u3l_YiijnSs) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-07-why-ai-dominates-the-crypto-market)
- **Substack:**
  - [Model-Level Routing vs. Single-Model Fine-Tuning](https://mycroftproject.substack.com/p/model-routing-vs-fine-tuning-extraction)
  - [Mistral vs. Llama on Financial Text](https://mycroftproject.substack.com/p/mistral-vs-llama-on-financial-text)

---

### Week 7 (Phase 7): Targeted fine-tuning
**Aug 9 – Aug 15, 2026** · **29.5 hrs**

**Work completed**
- QLoRA on Llama 3.1 8B improved Brier skill score by 0.07, above the 0.05 threshold.
- Calibration improved but resolution stayed flat, suggesting a ceiling at 8B parameters.
- Mistral-7B routing for hedged-language chunks; ticker registry; pipeline enhancements.

**Evidence**
- **Work folder** (report, friction log, README): [2026-08-14-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-14-weekly-work-progress)
- **Videos:**
  - **Weekly implementation:** ECIS Explained EP2 — [YouTube](https://www.youtube.com/watch?v=0byQTw6SZSw) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-14-ecis-explained)
  - **STEM/AI:** FinBERT Explainer — [YouTube](https://www.youtube.com/watch?v=7JRFtmd0HEQ) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-14-finbert-explainer)
- **Substack:**
  - [Tokenizer Alignment Across Models](https://mycroftproject.substack.com/p/tokenizer-alignment-across-models)

---

### Week 8 (Phase 8): Architecture rework and a third model
**Aug 16 – Aug 22, 2026** · **29.75 hrs**

**Work completed**
- Qwen2.5-14B added; the resolution plateau persisted, so the problem is linguistic ambiguity, not model capacity.
- Pipeline hardening: input validation, confidence gating, JSON retry logic, signal provenance.
- Per-chunk model identity and model tier as a triangulator weight.

**Evidence**
- **Work folder** (report, friction log, README): [2026-08-21-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-21-weekly-work-progress)
- **Videos:**
  - **Weekly implementation:** ECIS Explained EP3 — [YouTube](https://www.youtube.com/watch?v=djilegdvCgM) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-21-ecis-explained) · [Drive](https://drive.google.com/drive/folders/1WDuTTxWatMc8jeUoSQiSEjI0Z45TKGa0)
  - **STEM/AI:** Attention in Finance Explained — [YouTube](https://www.youtube.com/watch?v=UXW3ar6AWu0) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-21-attention-finance-explained) · [Drive](https://drive.google.com/drive/folders/1L18a_VtyzobdgiPDmQ3DM2pVAZ_r-CVy)

---

### Week 9 (Phase 9): Signal enrichment
**Aug 23 – Aug 29, 2026** · **29.25 hrs**

**Work completed**
- Speaker-weighted extraction (CFO 1.0, CEO 0.8, analyst 0.3) cut Q&A false positives.
- Chunk quality scoring improved ECE.
- Temporal linking: trend signals directionally interesting but reported as an insufficient sample.

**Evidence**
- **Work folder** (report, friction log, README): [2026-08-28-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-28-weekly-work-progress)
- **Videos:**
  - **Weekly implementation:** ECIS EP4 — [YouTube](https://www.youtube.com/watch?v=CTM32FIoXxg) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-28-ecis-explained) · [Drive](https://drive.google.com/drive/folders/1mkIsMtJORDsH8bME_JjRuRmjJKEFA7Fa)
  - **STEM/AI:** What Temperature Does to an LLM's Financial Predictions — [YouTube](https://www.youtube.com/watch?v=6In_XgcBxug) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-28-temperature-llm-finance) · [Drive](https://drive.google.com/drive/folders/1uUpYVoeHUYE7Y3DkesHrtUiiWL76USo-)
- **Substack:**
  - [Qwen2.5-14B vs. 8B Extraction](https://mycroftproject.substack.com/p/qwen-14b-vs-8b-parameter-scaling-extraction)
  - [Byte-Level BPE vs. WordPiece](https://mycroftproject.substack.com/p/byte-bpe-vs-wordpiece-tokenizer-financial-extraction)

---

### Week 10 (Phase 10): Second fine-tuning round and evaluation features
**Aug 30 – Sep 5, 2026** · **28.5 hrs**

**Work completed**
- QLoRA with reasoning traces improved skill score by 0.09; resolution moved for the first time (promising, not proven).
- Six features: abstention calibration, section weighting, signal decay, negation detection, keyword density, duplicate detection.
- Signal decay: raised signals degrade by 180 days, while reversals strengthen.

**Evidence**
- **Work folder** (report, friction log, README): [2026-09-04-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-04-weekly-work-progress)
- **Videos:**
  - **Weekly implementation:** ECIS EP5 — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-04-ecis-explained) · [Drive](https://drive.google.com/drive/folders/1J3DRtBHoVtfc3tghfY1pRRKdsmFN-vXv)
  - **STEM/AI:** What Happens Inside a Financial Chatbot — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-04-financial-chatbot) · [Drive](https://drive.google.com/drive/folders/1fEE7UbuwOQMApJnv9naIvZfgio5RKTQ4)
- **Substack:**
  - [Five Weight Dimensions in One Triangulator](https://mycroftproject.substack.com/p/five-weight-triangulator-confidence-composition)
  - [QLoRA on the Maintained/None Boundary](https://mycroftproject.substack.com/p/qlora-maintained-none-boundary-fine-tuning)

---

### Week 11 (Phase 11): Prediction system
**Sep 6 – Sep 12, 2026** · **30.25 hrs**

**Work completed**
- Next-quarter guidance prediction from the system's own decision log.
- Logistic regression beat both baselines; XGBoost overfit at this data size.
- Pre-registered, append-only prediction log; reader health monitor; latency logging.

**Evidence**
- **Work folder** (report, friction log, README): [2026-09-11-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-11-weekly-work-progress)
- **Videos:**
  - **Weekly implementation:** ECIS EP6 — [YouTube](https://www.youtube.com/watch?v=Wjebghtt8rQ) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-11-ecis-explained) · [Drive](https://drive.google.com/drive/folders/1VnK_DOZScqLAkux7fT9q286O8S6M_Tsz)
  - **STEM/AI:** Inside a Transformer Layer — [YouTube](https://www.youtube.com/watch?v=ZwgNiyJOABI) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-11-transformer-layer) · [Drive](https://drive.google.com/drive/folders/1s67qkp03dgxIX2_WfMDzyDRMjF0YEFjM)
- **Substack:**
  - [Logistic Regression vs. XGBoost for Guidance Direction Forecasting](https://mycroftproject.substack.com/p/logistic-regression-vs-xgboost-guidance-forecasting)
  - [Extraction Latency as a Signal](https://mycroftproject.substack.com/p/extraction-latency-signal-financial-nlp)

---

### Week 12 (Phase 12): Consensus and cross-company analysis
**Sep 13 – Sep 19, 2026** · **30.75 hrs**

**Work completed**
- FMP consensus estimates and a guidance surprise score.
- Cross-company correlation with leading/lagging detection, using Bonferroni correction.
- Sector-normalized scoring and confidence-stratified evaluation.

**Evidence**
- **Work folder** (report, friction log, README): [2026-09-18-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-18-weekly-work-progress)
- **Videos:**
  - **Weekly implementation:** ECIS EP7 — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-18-ecis-explained) · [Drive](https://drive.google.com/drive/folders/16xVbLc724aBClwvYLqwmFe7NLzH7me4R)
  - **STEM/AI:** Embeddings Explainer — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-18-embeddings-explainer) · [Drive](https://drive.google.com/drive/folders/1yZhSYdkvtlZOv1zxxPtIbraw2nOHYi0S)
- **Substack:**
  - [From SQLite to PostgreSQL + TimescaleDB](https://mycroftproject.substack.com/p/sqlite-postgresql-timescaledb-ml-pipeline)


---

### Week 13 (Phase 13): Analytics and database migration
**Sep 20 – Sep 26, 2026** · **38.75 hrs**

**Work completed**
- Linguistic analytics: readability, hedging index, forward-looking density, tone shift.
- Market impact analytics: reaction magnitude, pre-signal drift, timing, abnormal volume.
- Migration to PostgreSQL with TimescaleDB, Alembic, and materialized views.


**Evidence**
- **Work folder** (report, friction log, README): [2026-09-25-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-25-weekly-work-progress)
- **Videos:**
  - **Weekly implementation:** ECIS EP8 — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-25-ecis-explained) · [Drive](https://drive.google.com/drive/folders/1eZm09UfVd6K983PznG7eGJXnrszWY_0E)
  - **STEM/AI:** Vector DB Explainer — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-25-vector-db-explainer) · [Drive](https://drive.google.com/drive/folders/1wbNyPe1w2Y6TaORFW0H3u6A9fK6v8wQD)
- **Substack:**
  - [Connection Pooling Matters: The Infrastructure Problem No Model Upgrade Can Fix](https://mycroftproject.substack.com/p/connection-pooling-ml-pipeline-postgresql)
  - [Why Prompts Can Create Invisible Errors](https://mycroftproject.substack.com/p/invisible-prompt-errors-financial-nlp)

---

### Week 14 (Phase 14): Infrastructure hardening and statistical rigor
**Sep 27 – Oct 3, 2026** · **36.5 hrs**

**Work completed**
- ChromaDB optimization: Recall@10 from 0.89 to 0.94.
- Bootstrap CIs, permutation tests, and power analysis: ~0.6 power at n≈45, so subtle comparisons wait for more data.
- Data lineage, Grafana monitoring, and concept drift detection.

**Evidence**
- **Work folder** (report, friction log, README): [2026-10-02-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-02-weekly-work-progress)
- **Videos:**
  - **Weekly implementation:** ECIS EP9 — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-02-ecis-explained) · [Drive](https://drive.google.com/drive/folders/1cmuifmONniYXUfM26KO_2GqJ3oSKnvlk)
  - **STEM/AI:** Context Window Explainer — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-02-context-window-explainer) · [Drive](https://drive.google.com/drive/folders/1d__3scCkeKfPPCyXvvAaesOk6ePpn7fR)
- **Substack:**
  - [From Transcript to Trade Signal in Under 60 Seconds](https://mycroftproject.substack.com/p/transcript-to-trade-signal-pipeline-latency)
  - [Data Lineage Isn't Optional](https://mycroftproject.substack.com/p/data-lineage-provenance-financial-ai)

---

### Week 15 (Phase 15): Business analytics
**Oct 4 – Oct 10, 2026** · **33.75 hrs**

**Work completed**
- Guidance language tracker and CEO–CFO tone divergence.
- Signal-to-price correlation, three-way surprise analytics, and reaction windows.
- Preliminary finding: NLP-vs-actual surprise outperformed consensus-vs-actual.

**Evidence**
- **Work folder** (report, friction log, README): [2026-10-09-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-09-weekly-work-progress)
- **Videos:**
  - **Weekly implementation:** ECIS EP10 — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-09-ecis-explained) · [Drive](https://drive.google.com/drive/folders/1STQmHnVFLFYWcN2ARxxeVIruCuDszEfv)
  - **STEM/AI:** Why GPUs Beat CPUs for AI — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-09-gpu-vs-cpu-explainer) · [Drive](https://drive.google.com/drive/folders/12zdqQ455NrC1zzBrWvkzrAUQSAmzN2Fq)
- **Substack:**
  - [Turning Earnings Calls into Competitive Intelligence](https://mycroftproject.substack.com/p/earnings-calls-competitive-intelligence-signals)

---

### Week 16 (Phase 16): Guidance models
**Oct 11 – Oct 17, 2026** · **37 hrs**

**Work completed**
- Q&A dodge scoring, weighted by question type.
- Offensive vs. defensive market share language, with three classifiers.
- Six-model guidance revision predictor: tree ensembles led (LightGBM 0.72 AUC); the MLP trailed (0.66).

**Evidence**
- **Work folder** (report, friction log, README): [2026-10-16-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-16-weekly-work-progress)
- **Videos:**
  - **Weekly implementation:** ECIS EP11 — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-16-retrieval-pipeline-explainer) · [Drive](https://drive.google.com/drive/folders/1nhuXcSs3NBvBfnIoYChnB1pp2Ih_J6ll)
  - **STEM/AI:** What a Retrieval Pipeline Looks Like in Production — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-16-retrieval-pipeline-explainer) · [Drive](https://drive.google.com/drive/folders/12lmxHJh3ymFt53A_vrxpRrEOYg4OmM2h)
- **Substack:**
  - [Does Deep Learning Help When the Data Is Small?](https://mycroftproject.substack.com/p/deep-learning-small-data-tree-ensembles-tabular)

---

## Weekly Evidence Index

| Week / dates | Actual hours | Video links | Log and work evidence |
|---|---|---|---|
| **Week 1** · Jun 29 – Jul 4, 2026 | 21 | — | [2026-07-03-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-07-03-weekly-work-progress) |
| **Week 2** · Jul 5 – Jul 11, 2026 | 21 | — | [2026-07-10-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-07-10-weekly-work-progress) |
| **Week 3** · Jul 12 – Jul 18, 2026 | 29 | — | [2026-07-17-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-07-17-weekly-work-progress) |
| **Week 4** · Jul 19 – Jul 25, 2026 | 27.5 | — | [2026-07-24-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-07-24-weekly-work-progress) |
| **Week 5** · Jul 26 – Aug 1, 2026 | 27 | — | [2026-07-31-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-07-31-weekly-work-progress) |
| **Week 6** · Aug 2 – Aug 8, 2026 | 32 | **Weekly implementation:** ECIS Explained — [YouTube](https://www.youtube.com/watch?v=3mxjvm85JNg) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-07-ecis-explained)<br>**STEM/AI:** Why AI Dominates the Crypto Market — [YouTube](https://www.youtube.com/watch?v=u3l_YiijnSs) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-07-why-ai-dominates-the-crypto-market) | [2026-08-07-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-07-weekly-work-progress) |
| **Week 7** · Aug 9 – Aug 15, 2026 | 29.5 | **Weekly implementation:** ECIS Explained EP2 — [YouTube](https://www.youtube.com/watch?v=0byQTw6SZSw) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-14-ecis-explained)<br>**STEM/AI:** FinBERT Explainer — [YouTube](https://www.youtube.com/watch?v=7JRFtmd0HEQ) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-14-finbert-explainer) | [2026-08-14-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-14-weekly-work-progress) |
| **Week 8** · Aug 16 – Aug 22, 2026 | 29.75 | **Weekly implementation:** ECIS Explained EP3 — [YouTube](https://www.youtube.com/watch?v=djilegdvCgM) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-21-ecis-explained) · [Drive](https://drive.google.com/drive/folders/1WDuTTxWatMc8jeUoSQiSEjI0Z45TKGa0)<br>**STEM/AI:** Attention in Finance Explained — [YouTube](https://www.youtube.com/watch?v=UXW3ar6AWu0) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-21-attention-finance-explained) · [Drive](https://drive.google.com/drive/folders/1L18a_VtyzobdgiPDmQ3DM2pVAZ_r-CVy) | [2026-08-21-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-21-weekly-work-progress) |
| **Week 9** · Aug 23 – Aug 29, 2026 | 29.25 | **Weekly implementation:** ECIS EP4 — [YouTube](https://www.youtube.com/watch?v=CTM32FIoXxg) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-28-ecis-explained) · [Drive](https://drive.google.com/drive/folders/1mkIsMtJORDsH8bME_JjRuRmjJKEFA7Fa)<br>**STEM/AI:** What Temperature Does to an LLM's Financial Predictions — [YouTube](https://www.youtube.com/watch?v=6In_XgcBxug) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-28-temperature-llm-finance) · [Drive](https://drive.google.com/drive/folders/1uUpYVoeHUYE7Y3DkesHrtUiiWL76USo-) | [2026-08-28-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-08-28-weekly-work-progress) |
| **Week 10** · Aug 30 – Sep 5, 2026 | 28.5 | **Weekly implementation:** ECIS EP5 — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-04-ecis-explained) · [Drive](https://drive.google.com/drive/folders/1J3DRtBHoVtfc3tghfY1pRRKdsmFN-vXv)<br>**STEM/AI:** What Happens Inside a Financial Chatbot — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-04-financial-chatbot) · [Drive](https://drive.google.com/drive/folders/1fEE7UbuwOQMApJnv9naIvZfgio5RKTQ4) | [2026-09-04-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-04-weekly-work-progress) |
| **Week 11** · Sep 6 – Sep 12, 2026 | 30.25 | **Weekly implementation:** ECIS EP6 — [YouTube](https://www.youtube.com/watch?v=Wjebghtt8rQ) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-11-ecis-explained) · [Drive](https://drive.google.com/drive/folders/1VnK_DOZScqLAkux7fT9q286O8S6M_Tsz)<br>**STEM/AI:** Inside a Transformer Layer — [YouTube](https://www.youtube.com/watch?v=ZwgNiyJOABI) · [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-11-transformer-layer) · [Drive](https://drive.google.com/drive/folders/1s67qkp03dgxIX2_WfMDzyDRMjF0YEFjM) | [2026-09-11-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-11-weekly-work-progress) |
| **Week 12** · Sep 13 – Sep 19, 2026 | 30.75 | **Weekly implementation:** ECIS EP7 — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-18-ecis-explained) · [Drive](https://drive.google.com/drive/folders/16xVbLc724aBClwvYLqwmFe7NLzH7me4R)<br>**STEM/AI:** Embeddings Explainer — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-18-embeddings-explainer) · [Drive](https://drive.google.com/drive/folders/1yZhSYdkvtlZOv1zxxPtIbraw2nOHYi0S) | [2026-09-18-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-18-weekly-work-progress) |
| **Week 13** · Sep 20 – Sep 26, 2026 | 38.75 | **Weekly implementation:** ECIS EP8 — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-25-ecis-explained) · [Drive](https://drive.google.com/drive/folders/1eZm09UfVd6K983PznG7eGJXnrszWY_0E)<br>**STEM/AI:** Vector DB Explainer — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-25-vector-db-explainer) · [Drive](https://drive.google.com/drive/folders/1wbNyPe1w2Y6TaORFW0H3u6A9fK6v8wQD) | [2026-09-25-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-09-25-weekly-work-progress) |
| **Week 14** · Sep 27 – Oct 3, 2026 | 36.5 | **Weekly implementation:** ECIS EP9 — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-02-ecis-explained) · [Drive](https://drive.google.com/drive/folders/1cmuifmONniYXUfM26KO_2GqJ3oSKnvlk)<br>**STEM/AI:** Context Window Explainer — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-02-context-window-explainer) · [Drive](https://drive.google.com/drive/folders/1d__3scCkeKfPPCyXvvAaesOk6ePpn7fR) | [2026-10-02-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-02-weekly-work-progress) |
| **Week 15** · Oct 4 – Oct 10, 2026 | 33.75 | **Weekly implementation:** ECIS EP10 — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-09-ecis-explained) · [Drive](https://drive.google.com/drive/folders/1STQmHnVFLFYWcN2ARxxeVIruCuDszEfv)<br>**STEM/AI:** Why GPUs Beat CPUs for AI — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-09-gpu-vs-cpu-explainer) · [Drive](https://drive.google.com/drive/folders/12zdqQ455NrC1zzBrWvkzrAUQSAmzN2Fq) | [2026-10-09-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-09-weekly-work-progress) |
| **Week 16** · Oct 11 – Oct 17, 2026 | 37 | **Weekly implementation:** ECIS EP11 — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-16-retrieval-pipeline-explainer) · [Drive](https://drive.google.com/drive/folders/1nhuXcSs3NBvBfnIoYChnB1pp2Ih_J6ll)<br>**STEM/AI:** What a Retrieval Pipeline Looks Like in Production — [GitHub](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-16-retrieval-pipeline-explainer) · [Drive](https://drive.google.com/drive/folders/12lmxHJh3ymFt53A_vrxpRrEOYg4OmM2h) | [2026-10-16-weekly-work-progress](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-10-16-weekly-work-progress) |
| **Total** | **481.5** | | |

---

## Plan for the Upcoming Period

- Agentic conversational interface for natural language queries.
- Additional ML model exploration and architecture benchmarking.
- Expand data sources beyond earnings calls.
- API layer and alerting system.
- Portfolio simulation tools.
