**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 7 — Pipeline Enhancement

**Timeline:** August 9, 2026 – August 15, 2026

**Scope:** Ticker expansion to 20–25 companies, QLoRA research, targeted accuracy improvements across the pipeline, and a structured ticker registry.

---

## Ticker Expansion (Round 2)
- Coverage extended to 20–25 AI-sector companies using Mistral-7B
- **Full-run runtime:** about 3.5 hours, driven by:
  - Three self-consistency passes per chunk
  - Multi-turn verification
  - Per-chunk retrieval
  - JSON truncation retries

## QLoRA Research
- **Methodology reviewed:**
  - Adapter strategies and rank-selection trade-offs
  - Training-data preparation
- **Tooling reviewed:**
  - NF4 quantization through BitsAndBytes
  - Unsloth for accelerated training
- **Colab resilience:** checkpoint persistence to Google Drive

## Prompt Refinement
- Sharpened the boundary between "no guidance change" (`none`) and "guidance explicitly maintained" (`maintained`)
- Addresses inflation of the maintained class

## Temporal Retrieval
- **Edge cases handled:**
  - Inconsistent fiscal calendars
  - Mid-quarter transcript dates
  - Varying reporting conventions
- **Query change:** filters by ticker and date range instead of exact quarter labels

## Exemplar Expansion
- `ecis_exemplars` extended with examples from newly added tickers
- Improves few-shot coverage across company-specific guidance conventions

## Boilerplate Detection
- Detects disclaimers embedded inside prepared remarks
- Covers softened disclaimer variants missed by the original regex patterns

## Batch Consistency Checking
- Compares FinBERT scores across adjacent chunks in a transcript
- Flags isolated sentiment outliers, such as one strongly negative chunk among positive neighbours
  - These usually point to boilerplate contamination or chunk-boundary artifacts

## Ticker Registry
- SQLite table replacing directory-based ticker management
- **Fields:**
  - Symbol, company name, sector
  - Fiscal calendar and transcript source
  - Transcript count and last ingestion date
  - Extraction status and outcome resolution status
- Migration script populates the table from the existing directory structure
- Pipeline now queries the registry instead of scanning directories
