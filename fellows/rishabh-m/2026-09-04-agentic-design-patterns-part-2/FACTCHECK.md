# FACTCHECK — agentic-design-patterns-part-2

DOUBLE-CHECK LAW: every claim spoken or shown, checked against the source and
rewritten in the HAI Plain register. Source: `agentic-patterns-part2.md`
(Master Class Part 2), in `Agentic Design Video/`.

| # | Claim (beat) | Verdict | Source |
|---|---|---|---|
| 1 | Multi-agent = manager + specialists sharing one store (B03) | ✓ | §P7, "distributing a complex task among multiple specialized agents… coordinated by a central manager agent"; "share a **common memory mechanism**" |
| 2 | Concurrent writes without locks corrupt state (B03) | ✓ | §P7, "If multiple agents write to the shared memory simultaneously without locks or transaction boundaries, state corruption occurs" |
| 3 | Read-only snapshot in, atomic patch out, orchestrator validates (B03) | ✓ | §P7 Q&A, verbatim mechanism — "read-only snapshot"; "atomic patch"; "validates the patch against the current state version" |
| 4 | Memory splits short-term / episodic / long-term (B04) | ✓ | §P8, "classifying incoming information into short-term (conversational), episodic (events), or long-term (knowledge) stores" |
| 5 | Long-term structured profile never decays; episodic decays (B04) | ✓ | §P8 Q&A, "This structured DB never decays, while the episodic vector embeddings undergo exponential decay" |
| 6 | Retrieval scores similarity + recency + frequency (B04) | ✓ | §P8, the composite score formula: `w1·SemanticSimilarity + w2·Recency + w3·Frequency` |
| 7 | Similarity alone poisons context (B04 note) | ✓ | §P8 Cons, "risk of context window poisoning (retrieving old, irrelevant memories that dilute focus)" |
| 8 | Feedback must be denoised; malicious feedback teaches wrong behaviour (B05) | ✓ | §P9, "If a user provides malicious or incorrect feedback… the system must filter it out to prevent learning the wrong behaviors" |
| 9 | Prefer prompt/few-shot updates over real-time fine-tuning (B05) | ✓ | §P9, "Real-time fine-tuning is rare and risky; dynamic retrieval of few-shot examples (Prompt Tuning) is much more robust" |
| 10 | KPIs are latency, token spend, step count (B06) | ✓ | §P10, "API latency, token spend limits, task execution steps" |
| 11 | Drift = deviation of multiple standard deviations (B06) | ✓ | §P10, "When metrics deviate by multiple standard deviations from the expected mean, a drift analyzer determines if the issue is a simple failure or a structural change" |
| 12 | Conflicting goals (speed vs cost) deadlock (B06 note) | ✓ | §P10 Cons, "Can introduce goal conflicts (e.g., speed vs. cost) resulting in deadlocks" |
| 13 | Errors classify temporary / permanent / critical (B07) | ✓ | §P11 diagram + prose: temporary → exponential backoff; permanent → Plan B; critical → escalate to human |
| 14 | Alert fatigue; alert on critical only (B07) | ✓ | §P11 Q&A, "engineers ignore the notifications entirely"; tiered escalation with silent handling of temporary errors |
| 15 | HITL suspends state indefinitely without leaking resources (B08) | ✓ | §P12, "persisting state (e.g., freezing the thread) indefinitely while waiting for human input without leaking resources" |
| 16 | HITL latency is bound to human response speed (B08 note) | ✓ | §P12 Cons, "Massive latency overhead (the system is throttled by human response speed)" |
| 17 | RAG = rewrite → search → rerank → ground (B09) | ✓ | §P13 diagram + "An LLM should rewrite the query, perform semantic search, and use a Cross-Encoder Reranker" |
| 18 | Chunking must be semantic, not fixed-size (B09) | ✓ | §P13, "Fixed-size chunking is simple but bad; semantic or context-aware chunking is necessary" |
| 19 | Too large a K → "lost in the middle" → hallucination (B09) | ✓ | §P13, "high K increases token costs and causes the LLM to get lost in the middle, introducing hallucinations" |
| 20 | "Patterns 7–13 of 20" (B02) | ✓ | Source header, "Patterns 7-13"; Part 1 established the 20-pattern scope |

## Corrections and editorial notes

- **"State is the hard part" is OUR thesis**, not a sentence in the source. It is
  a synthesis: the source names state conflicts (P7), context bloat (P8),
  feedback poisoning (P9), drift (P10), error recovery (P11), state suspension
  (P12) and index drift (P13) as the primary bottleneck of each pattern in turn.
  The claim is defensible from the source's own Orchestration Matrix, which
  lists a state-related bottleneck for all four patterns it summarises. Flagged
  here as interpretation rather than reportage.
- **The "orchestration / memory / fail-safes" grouping** (B02) is the source's
  own — it is the document's title.
- **B10's worked example is ours**, assembling the source's customer-service,
  memory, RAG and approval examples into one conversation. Not a source figure.
- **B11 ("when not to") has no counterpart in the source**, which advocates for
  each pattern without arguing the null case. Written independently so the reel
  does not oversell; consistent with Part 1's B10.
- **Numbers on screen:** only "7–13" and "20" (pattern counts), and the σ
  threshold shown as a symbol, not a fabricated figure. No invented metrics.
- **Bracketed citation markers** (`[22]`, `[34, 35]`…) index a bibliography not
  reproduced in the notes; not followed, and no claim rests on one alone.

## Dating risk

No model names, versions, vendor pricing or benchmark numbers. Named
technologies (vector DB, Redis, MCP) appear in the source; only generic terms
("vector store", "shared store") are used on screen, so the reel should not date.
