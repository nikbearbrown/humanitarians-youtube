# Weekly Report: Week 2 (Phase 2)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard
**Week:** July 5 – July 11, 2026
**Total hours:** 21.0

---

## Summary

- System architecture revised based on the Week 1 reformulation and early implementation constraints.
- Data pipeline built end to end against real transcripts from EDGAR and FMP, in this order:
  - ingestion
  - preprocessing
  - normalization
  - chunking
  - embeddings
  - ChromaDB storage
- Pydantic signal schema defined as the ECIS → Scorecard contract.
- One Claude artifact and two Substack articles completed.

---

## Work Completed

### 1. System Architecture Revision
*Development · Architecture*
- Revised the system architecture based on the Week 1 reformulation and on constraints discovered during early implementation.
- **Deliverable:** updated system architecture
- **Links:**
  - https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/architecture
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/docs/workflow.md
- **Status:** Complete

### 2. Dataset Exploration
*Research · Data Sourcing*
- Explored available datasets for the project.
- **Deliverable:** dataset survey
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

### 3. Data Ingestion Pipeline
*Development · Data Pipeline*
- Connected to EDGAR and FMP and downloaded transcripts.
- Established the ingest pathway with provenance recording.
- **Deliverable:** working data ingestion pipeline (EDGAR + FMP)
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/src/ecis/ingestion
- **Status:** Complete

### 4. Signal Schema Definition
*Development · Schema*
- Defined the Pydantic signal schema as the contract between ECIS output and Scorecard input.
- **Deliverable:** Pydantic signal schema
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/schemas/signal.py
- **Status:** Complete

### 5. Data Preprocessing
*Development · Data Pipeline*
- Experimented with multiple preprocessing approaches for raw transcripts.
- **Deliverable:** working preprocessing pipeline
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/src/ecis/preprocessing
- **Status:** Complete

### 6. Transcript Normalization
*Development · Data Pipeline*
- Normalized transcripts across the divergent formats from EDGAR and FMP.
- **Deliverable:** normalized transcript output across sources
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/preprocessing/normaliser.py
- **Status:** Complete

### 7. Text Chunking
*Development · Data Pipeline*
- Built the chunking layer, with decisions on overlap size, token boundaries, and section-awareness.
- Chunking strategy determines what FinBERT's 512-token context window sees.
- **Deliverable:** text chunking module
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/preprocessing/chunker.py
- **Status:** Complete

### 8. Embedding Generation + Vector Storage (ChromaDB)
*Development · Data Pipeline*
- Generated embeddings and integrated ChromaDB.
- Hit embedding dimension mismatches that required end-to-end debugging.
- **Deliverable:** working embedding pipeline + ChromaDB integration
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/embedding/embedder.py
- **Status:** Complete

### 9. Pipeline Visualizer
*Artifact · Claude Artifact*
- Visualization of the updated data pipeline architecture.
- **Deliverable:** Claude Artifact: Pipeline Visualizer
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### 10. Substack Article: "FinBERT's 512-Token Blind Spot"
*Writing · Substack Article*
- Explores FinBERT's application to financial sentiment analysis.
- Examines how its inherited 512-token context window interacts with chunking strategy.
- Argues that preprocessing decisions at the data layer directly shape what the model can and cannot detect in earnings call transcripts.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/finbert-512-token-chunking-sentiment-classification
- **Status:** Complete (published)

### 11. Substack Article: "Designing a Metadata Schema for Financial Vector Stores"
*Writing · Substack Article*
- Examines why metadata schema design matters more than embedding model choice for retrieval quality in domain-specific financial RAG systems.
- Shows how fields like ticker, filing date, section label, and speaker attribution enable filtered retrieval in ChromaDB.
- Argues that this filtering turns a general-purpose vector store into a queryable financial intelligence layer.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/designing-a-metadata-schema-for-financial
- **Status:** Complete (published)
