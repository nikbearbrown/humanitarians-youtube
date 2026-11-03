**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 3 — Extraction Layer

**Timeline:** July 12, 2026 – July 18, 2026

**Scope:** Persistence layer, graph state definitions, four signal readers, exemplar curation, triangulation, and semantic deduplication.

---

## Persistence
- **Four SQLite databases:**

| Database | Contents |
|---|---|
| Signals | Append-only decision log; all schema fields plus a unique signal ID |
| Outcomes | Per-signal, per-horizon (30 / 90 / 180 days) prices, benchmark prices, excess returns, correctness flags |
| Agents | Audit log: agent name, trigger, action, timestamp, result |
| Checkpoints | LangGraph state: graph ID, node ID, serialized state, timestamp |

- Default reader weights seeded for the triangulator

## LangGraph State and Checkpointing
- **Typed state schemas (TypedDict):**
  - **Orchestration:** current chunk, fast-pass results, escalation category, extraction result
  - **Watchdog:** rolling metrics window, thresholds, triggered actions, interrupt status
  - **Conflict resolution:** conflicting outputs, context window, resolution, vindication record
- **Checkpointing:**
  - Backed by SQLite through `langgraph-checkpoint-sqlite`
  - Supports mid-batch crash recovery, resuming from the last completed checkpoint

## Reader 1 — Keyword
- **Taxonomy:** YAML file with 30–50 guidance phrases per direction (raised / lowered / maintained)
- **Matching:** regex with `\b` word-boundary anchors to prevent substring false positives
- **Output:** matched phrases, inferred direction, binary confidence
- **Runtime:** microseconds per chunk
- **Role:** permanent Brier skill score baseline

## Reader 2 — FinBERT
- **Model:** `ProsusAI/finbert` (Transformers / PyTorch)
- **Loading:** lazy-loaded once in eval mode
- **Device selection:** CUDA, then MPS, then CPU
- **Inference:** batches of 16–32 with padding and attention masks
- **Output mapping:**
  - Threshold-based mapping from the three-class sentiment distribution to guidance direction
  - Explicit handling of ambiguous distributions
  - Positive sentiment is not treated as equivalent to raised guidance
- **Resolved:** silent truncation of chunks near 512 tokens during batching
  - Caused score mismatches against single-chunk inference
  - Fixed with token-level validation before batching

## Reader 3 — NER
- **Model:** spaCy with financial entity recognition
- **Extracted entities:**
  - Organizations
  - Monetary values and percentages
  - Dates and time periods
  - Financial metrics
- **Role:** contextual metadata only; does not vote on direction

## Reader 4 — LLM (Llama 3.1 8B-Instruct)
- **Runtime:** Ollama, q8_0 quantization
  - On Colab: Ollama server at `localhost:11434`, configured via `.env`
  - Model name and temperature configurable
- **Chain-of-thought prompt:**
  - **System prompt:** financial-analyst role, JSON-only output, forward-looking statements only, change vs. reaffirmation rules, conservative default, `none` allowed
  - **Five reasoning steps:** temporal orientation → change vs. reaffirmation → lexical evidence → direction → confidence with justification
  - Full reasoning trace persisted for every extraction
- **Dynamic few-shot retrieval:**
  - 3–5 semantically similar exemplars retrieved from `ecis_exemplars`
  - Exemplars match the chunk's signal category (e.g. revenue chunks get revenue examples)
- **Cross-transcript temporal retrieval:**
  - 2–3 chunks from the same ticker's prior quarter
  - Detects implicit changes (e.g. $4.5B guidance is only a raise against a prior $4.0B)
  - Soft-fails with empty context when no prior data exists
  - Known limitation: inconsistent fiscal calendars across companies
- **Self-consistency decoding (temperatures 0.1 / 0.3 / 0.5):**

| Agreement | Action |
|---|---|
| 3 of 3, confidence within a 0.15 band | Accept at full confidence |
| 2 of 3 | Accept with confidence penalty |
| No agreement | Abstain (`none`) |

  - Individual votes persisted for audit
  - **Resolved:** circular reference when serializing votes, fixed by copying the winning dict before attaching votes
- **Multi-turn verification:**
  - Temperature 0
  - Model reviews its own extraction and returns CONFIRM, REVISE, or REJECT
  - Catches systematic misreadings that are consistent across temperatures

## Exemplar Curation
- **Coverage:**
  - All three directions
  - Signal categories: revenue, earnings, margin, capex, subscribers, segment
  - Explicit numerical and hedged qualitative language
  - Both prepared remarks and Q&A
- **Hard negatives:** 5–10 chunks that resemble guidance but are not guidance
- **Storage:** embedded with MiniLM into the `ecis_exemplars` collection, tagged by guidance type and category

## Triangulator
- **Weighted combination:**

| Component | Weight |
|---|---|
| Keyword | 0.15 |
| FinBERT | 0.20 |
| LLM | 0.50 |
| Agreement bonus | 0.15 |

- **Decision rule:** highest weighted direction wins
- **Reader adapters:** normalize four output types (binary flags, probability distributions, entity lists, structured extractions) into the shared schema, including partial outputs
- **Dynamic weights:** accepts weight updates from the vindication aggregation graph

## Semantic Deduplication
- **Similarity:** cosine similarity on quote embeddings
- **Above 0.90 with the same direction:** merge, keeping the higher-confidence record and both source chunk references
- **Above 0.90 with a conflicting direction:** flagged for review
- **Final check:** all signals validated against the schema before persistence
