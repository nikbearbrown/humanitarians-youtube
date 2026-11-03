# Weekly Report: Week 3 (Phase 3)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard
**Week:** July 12 – July 18, 2026
**Total hours:** 29.0

---

## Summary

- Infrastructure completed: SQLite databases, LangGraph state schemas, checkpoint store.
- Extraction layer built:
  - four readers: keyword, FinBERT, NER, LLM
  - few-shot exemplar collection
  - triangulator with dynamic weighting
  - semantic deduplicator
- Debugging focused on two areas: FinBERT silent truncation, and schema alignment across the four readers.
- vLLM and alternative extraction approaches explored; decision pending.
- One Claude artifact and two Substack articles completed.

---

## Work Completed

### 1. SQLite Database Initialization
*Development · Infrastructure*
- Initialized databases for signals, outcomes, agent decisions, and the checkpoint store.
- **Deliverable:** SQLite databases (signals, outcomes, agent decisions, checkpoint)
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/db/init_db.py
- **Status:** Complete

### 2. LangGraph State Schema + Checkpoint Store
*Development · Infrastructure*
- Defined state schemas for the agent graphs.
- Configured the checkpoint store for state persistence.
- **Deliverable:** LangGraph state schemas + checkpoint store
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/src/ecis/graphs
- **Status:** Complete

### 3. FinBERT Reader: Full Build
*Development · FinBERT Reader*
- Built:
  - model loading
  - GPU-efficient batched inference
  - sentiment score processing
  - output mapping to the signal schema
- Silent truncation in batched inference near the 512-token limit found and fixed.
- **Deliverable:** complete FinBERT reader with batched inference + signal schema mapping
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/finbert_reader.py
- **Status:** Complete

### 4. Keyword Reader Implementation
*Development · Keyword Reader*
- Built the keyword reader with regex matching against the taxonomy.
- **Deliverable:** complete keyword reader (baseline)
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/keyword_reader.py
- **Status:** Complete

### 5. NER Reader: spaCy Setup + Entity Structuring
*Development · NER Reader*
- Set up the spaCy model.
- Built the entity extraction pipeline.
- Structured entities into a signal-schema-compatible format.
- **Deliverable:** complete NER reader (spaCy)
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/ner_reader.py
- **Status:** Complete

### 6. LLM Reader: Full Build
*Development · LLM Reader*
- Built:
  - Ollama local setup
  - chain-of-thought prompt template
  - few-shot exemplar retrieval wiring
  - self-consistency decoding: three-pass temperature sweep with majority voting
  - multi-turn verification
  - cross-transcript temporal retrieval
- **Deliverable:** complete LLM reader (Ollama / Llama 3.1 8B) with self-consistency + temporal retrieval
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/llm_reader.py
- **Status:** Complete

### 7. Few-Shot Exemplar Curation + ChromaDB Collection
*Development · Exemplar Curation*
- Curated exemplars and embedded them into a dedicated ChromaDB collection for retrieval at inference time.
- **Deliverable:** exemplar collection in ChromaDB
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/embedding/exemplar_store.py
- **Status:** Complete

### 8. Triangulator + Semantic Deduplicator
*Development · Triangulation*
- Triangulator: dynamic reader weighting with vindication-based adjustments and overcorrection safeguards.
- Semantic deduplicator: cosine-similarity threshold with signal merging.
- **Deliverable:** triangulator with dynamic weighting + semantic deduplicator
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/extraction/triangulator.py
- **Status:** Complete

### 9. Debugging: FinBERT Truncation + Schema Alignment
*Development · Debugging*
- FinBERT batched inference: silent truncation near the 512-token limit.
- Schema alignment across four readers with fundamentally different output structures; each reader needed its own adapter layer.
- **Deliverable:** bug fixes; four reader adapter layers for the shared Pydantic schema
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/readers/finbert_reader.py
  - https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/src/ecis/readers
- **Status:** Complete

### 10. vLLM + Extraction Layer Exploration
*Research · Compute / LLM*
- Explored vLLM as an Ollama alternative for batch inference.
- Explored alternative extraction layer approaches.
- **Deliverable:** feasibility assessment; decision pending
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

### 11. Substack Article: "Temperature Sweeps as a Confidence Diagnostic in Financial NLP"
*Writing · Substack Article*
- Explores how running extraction prompts at multiple temperatures reveals whether a model's stated confidence is genuine or unstable.
- Argues that variance across passes is a more reliable confidence signal than the model's own score.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/temperature-sweeps-confidence-financial-nlp
- **Status:** Complete (published)

### 12. Substack Article: "Self-Consistency Decoding as a Hallucination Filter"
*Writing · Substack Article*
- Explores self-consistency decoding as a hallucination filter for financial signal extraction.
- Exploits the structural difference between grounded findings, which stay stable across temperatures, and hallucinated outputs, which change with temperature.
- Argues that abstention on full disagreement is a design feature in financial systems, not a failure mode.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/self-consistency-hallucination-filter-financial-nlp
- **Status:** Complete (published)

### 13. Reader Agreement Matrix
*Artifact · Claude Artifact*
- Interactive component: input a chunk and see a simulated side-by-side of all four readers' outputs.
- Highlights agreements and disagreements and shows the triangulator weighting.
- **Deliverable:** Claude Artifact: Reader Agreement Matrix
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete
