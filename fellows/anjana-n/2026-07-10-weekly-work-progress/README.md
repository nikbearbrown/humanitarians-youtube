**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 2 — Data Layer

**Timeline:** July 5, 2026 – July 11, 2026

**Scope:** Architecture finalization, ingestion, preprocessing, signal schema, normalization, chunking, vector storage, and LLM feasibility assessment.

---

## System Architecture
- Finalized component boundaries, inter-module data flow, and interface contracts
- Documented the directed graph structure for all three LangGraph agent graphs

## Data Ingestion
- **EDGAR fetcher:**
  - Retrieves 8-K filings and exhibits (press releases, CFO commentary) that carry guidance language
  - Throttled to 10 requests per second
- **FMP fetcher:**
  - Retrieves pre-formatted earnings call transcripts
  - Uses a daily call counter with backoff to stay within the 250-call limit
- **Metadata tagging:** every file is tagged with ticker, filing date, and source identifier
- **Local cache:** prevents redundant API calls
  - `data/raw/edgar/{ticker}/{filing_date}.htm`
  - `data/raw/fmp/{ticker}/{transcript_date}.json`

## Preprocessing
- **EDGAR HTML:** removes:
  - 8-K wrappers
  - Safe-harbour statements and forward-looking disclaimers
  - HTML tags and nested tables
  - Formatting artifacts and duplicate headers
- **FMP JSON:** extracts transcript text from the payload and resolves encoding inconsistencies
- **Output:** UTF-8 encoded text with normalized whitespace

## Signal Schema (Pydantic)
- **Shared data contract across the system:**

| Field group | Fields |
|---|---|
| Identity | `ticker`, `transcript_date`, `chunk_index`, `character_offsets` |
| Decision | `direction` (raised / lowered / maintained), `confidence_raw`, `confidence_calibrated`, `source_method` |
| Evidence | `supporting_quote`, `quote_embedding`, `section_label`, `speaker`, `ner_entities` |
| Audit | `reasoning_trace`, `self_consistency_votes`, `verification_status`, `timestamp` |

- **Validation rules:**
  - Confidence must lie in [0, 1]
  - Direction must be a valid enum value
  - Supporting quote must be non-empty
  - Character offsets must form a valid range
- Invalid records raise structured validation errors

## Transcript Normalization
- **Section labelling:** prepared remarks (per speaker) and analyst Q&A
- **Canonical speaker resolution:** "John Smith, CEO", "J. Smith", and "CEO" resolve to one identity
- **Heuristic section detection** for filings without explicit headers, based on:
  - Question-mark frequency
  - Speaker rotation patterns
- **Output:** section-tagged, speaker-normalized text files

## Chunking
- ~400-token chunks with a 50-token overlap
- **Token counting:** uses the FinBERT tokenizer, aligned to its 512-token context window
- **Section-aware:** chunks never cross section boundaries
- **Speaker-aware:** chunks follow speaker boundaries where possible
- **Per-chunk metadata:**
  - Source path and transcript date
  - Ticker, section, and speaker
  - Chunk index and character offsets

## Embeddings and Vector Storage
- **Embedding model:** sentence-transformers MiniLM, producing 384-dimensional vectors
- **Store:** ChromaDB collection `ecis_transcripts`
  - Cosine similarity distance metric
  - Full metadata indexing
- **Verified hybrid retrieval:** semantic similarity combined with ticker, date-range, and section filters

## LLM Feasibility Assessment
- Evaluated Llama 3.1 8B-Instruct in two deployment modes:
  - Local via Ollama
  - Cloud via the Groq free tier
- **Key constraint:** 8-bit quantized local inference requires 5–7 GB of VRAM
