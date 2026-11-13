# Friction Log: Week 3 (Phase 3)

**Project:** Mycroft — ECIS + Decision Scorecard
**Week:** July 12 – July 18, 2026

---

## 1. Focus of the week

- Infrastructure: SQLite databases, LangGraph state schemas, checkpoint store.
- Extraction layer:
  - four readers: keyword, FinBERT, NER, LLM
  - triangulator and semantic deduplicator
  - exemplar collection
  - temporal retrieval
- Debugging: FinBERT truncation and cross-reader schema alignment.
- Research: vLLM and alternative extraction approaches.
- Reading: Mycroft Ch 2–4 with exercises.
- Writing:
  - publication of the four backlogged articles
  - two new articles: "Temperature Sweeps" and "Self-Consistency Decoding"
- Reader Agreement Matrix (Claude artifact).

## 2. What was tried, and what was expected

- **FinBERT batching.** Expectation: batched inference would return the same scores as single-chunk inference, only faster.
- **Shared schema.** Expectation: one shared Pydantic signal schema would accept all four readers' outputs with light mapping.
- **FinBERT mapping.** Expectation: positive or negative sentiment would map fairly directly to raised or lowered guidance.
- **Temporal retrieval.** Expectation: "prior quarter" would be a coherent, queryable concept across companies.
- **Self-consistency.** Expectation: decoding would follow the proposal's specification without much extra design.
- **Triangulator.** Expectation: dynamic weighting as specified in the proposal.

## 3. Points of resistance, and next steps taken

### FinBERT silent truncation (load-bearing)
- **What happened:** during batching, chunks near the 512-token limit were truncated with no error raised. The resulting sentiment scores didn't match single-chunk inference.
- **Cause:** not a config error. A design-level mismatch between the batching logic and FinBERT's tokenizer handling of padding, truncation, and the context window.
- **Next step:** batching aligned with tokenizer behavior, and a pre-batch validation step added to flag over-limit chunks.
- **Why it matters:** the system produced confident, wrong numbers silently. This is a direct instance of the Fluency Trap from Mycroft Ch 1.

### Schema alignment across four readers
- **Four output shapes:**
  - keyword: binary flag + phrases
  - FinBERT: probability distribution
  - NER: entity lists
  - LLM: structured extraction with a reasoning trace
- **Problems found:** type mismatches and missing field mappings.
- **Hardest part:** partial outputs. FinBERT returns sentiment but no direction; NER returns entities but no signal.
- **Next step:** one adapter layer per reader, each handling its own partial-output cases. "Shared schema" turned out to mean four adapter layers.

### FinBERT output → guidance direction
- **What resisted:** positive sentiment does not automatically mean raised guidance.
- **Next step:** iterative decisions on thresholds, mixed distributions, and neutral-as-maintained vs. neutral-as-absent. The proposal does not prescribe this mapping.

### Fiscal calendar inconsistency
- **What resisted:** companies define fiscal quarters differently, so "prior quarter" is not uniform.
- **Next step:** design decisions on temporal query handling and retrieval count. Neither is specified in the proposal.

### Under-specified mechanisms
- **What resisted:** the proposal names these mechanisms but not their details.
  - **Self-consistency edge cases:** structural comparison of outputs, the partial-agreement penalty, and direction agreement with numerical divergence.
  - **Triangulator:** the adjustment rate, the vindication-to-weight mapping, and overcorrection safeguards. These decide whether the triangulator converges or oscillates.
- **Next step:** each detail designed during implementation.

## 4. AI and other contributions: accepted, changed, rejected

### Gru (SDD session)
- Documented the architectural decisions from the extraction layer build.

### Eddy
- Reviewed both Week 3 articles before publication.

### Claude
- Built the Reader Agreement Matrix: simulated side-by-side reader outputs with agreement highlighting and triangulator weighting.
- Design decisions were made in the build; the artifact makes them visible.

## 5. Understood now, and still unresolved

### Understood
- **Silent failure:** the most dangerous failure is the one that raises no error. Confident output is not correct output.
- **Shared schema:** a shared schema across heterogeneous readers requires per-reader adapters and explicit partial-output handling.
- **Self-consistency:** it works as a calibration and hallucination filter. Signals that can't be reproduced across temperatures are likely fabricated.
- **Ch 2–4 principles in the build:**
  - trust over speed → provenance logged at generation time
  - two bosses → human and machine views of the same data
  - elevating the human → review targets flagged-uncertain signals
  - safe over smart → abstain rather than guess

### Unresolved
- **Fine-tuning:** whether to revise the QLoRA approach for the actual compute budget. Carried from Week 2.
- **vLLM vs. Ollama:** decision pending.
- **Extraction layer:** which alternative approaches, if any, replace parts of the current design.
- **Week 4 scope:** not yet set. Orchestration, end-to-end testing, the scoring layer, and hand-labeling are all candidates.
- **Fluency Trap link:** the connection to the silent-truncation bug still needs documenting in the project notes.
