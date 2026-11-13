# Friction Log: Week 2 (Phase 2)

**Project:** Mycroft — ECIS + Decision Scorecard
**Week:** July 5 – July 11, 2026

---

## 1. Focus of the week

- Implementation against real data: ingestion, preprocessing, normalization, chunking, embeddings, ChromaDB.
- Signal schema (Pydantic) as the ECIS → Scorecard contract.
- Architecture and toolkit revisions driven by implementation constraints.
- LLM and compute feasibility: Llama 3.1 8B via Ollama and Groq.
- Mycroft Ch 1 (The Fluency Trap): reading and exercises.
- Two Substack articles: "FinBERT's 512-Token Blind Spot" and "Designing a Metadata Schema."
- Pipeline visualizer (Claude artifact).

## 2. What was tried, and what was expected

- **Sources.** Expectation: EDGAR and FMP transcripts would arrive in roughly comparable, usable formats.
- **Preprocessing.** Expectation: a straightforward cleaning step before extraction.
- **Chunking.** Initially treated as a neutral preprocessing step.
- **Embeddings.** Expectation: the move from the hashing-based stand-in to production embeddings + ChromaDB would plug in cleanly.
- **Compute.** Proposal assumption: compute would be enough for local inference and QLoRA fine-tuning.
- **Publishing.** Expectation: articles and artifacts would publish soon after review.

## 3. Points of resistance, and next steps taken

### Data source format divergence
- The sources diverged more than anticipated:
  - EDGAR: transcripts buried in boilerplate
  - FMP: pre-formatted JSON with inconsistent speaker labels
- Several preprocessing and normalization approaches tried; not all produced clean output on the first pass.
- **Next step:** decided on rules for section boundaries and for speaker attribution when a source contradicts itself.

### Chunking is not neutral
- Chunk boundaries determine what FinBERT's 512-token window sees, and therefore which signals can be extracted at all.
- **Next step:** treated chunking as a classification decision, setting overlap size, token boundaries, and section-awareness deliberately.
- Carried into the Substack article "FinBERT's 512-Token Blind Spot."

### Embedding dimension mismatch
- Vector store configuration and embedding model output dimensions did not align.
- Fixing it took tracing the pipeline end to end, through chunk generation, embedding, storage, and retrieval, rather than changing one config value.
- Not blocking, but a concrete example of the gap between "architecturally specified" and "working on real data."

### Compute budget reality check
- Ollama local inference needs 5–7 GB VRAM for 4-bit quantized Llama 3.1 8B.
- QLoRA on Colab depends on A100 availability.
- The proposal's compute assumption may not hold. The constraint is now concrete, not theoretical.
- **Next step:** groundwork laid for revising the fine-tuning method. Decision deferred.

### Publication backlog (since resolved)
- At week's end: four articles written (two from Week 1, two from Week 2) and none published.
- Blocker: GitHub access and an unclear publication workflow.
- All articles have since been published.

## 4. AI and other contributions: accepted, changed, rejected

### Gru (SDD session)
- Documented the architectural decisions made during implementation.

### Eddy
- Reviewed both Week 2 articles before publication.
- Open question at the time: whether Eddy or CRITIQ is the right tool for article review.

### Claude
- Built the pipeline visualizer for the updated architecture.

## 5. Understood now, and still unresolved

### Understood
- **Chunking:** chunking strategy is a classification decision that shapes downstream extraction quality.
- **Metadata:** metadata schema (ticker, filing date, section label, speaker) matters more than embedding model choice for filtered financial retrieval.
- **Real data:** real data exposes problems offline stand-ins cannot, including format divergence and dimension mismatches.
- **Fluency trap:** a system that emits confidence-scored signals is itself exposed to the fluency trap. FinBERT softmax scores run hot.

### Unresolved
- **Fine-tuning:** whether to revise the QLoRA approach for the actual compute budget.
- **Fluency trap in practice:** how the framing concretely changes confidence presentation in ECIS output.
- **Review tool:** Eddy vs. CRITIQ for article review.
