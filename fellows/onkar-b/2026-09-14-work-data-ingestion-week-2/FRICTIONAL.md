# Frictional log — Data Ingestion & Orchestration

## 2026-09-14 — the project update, in two aspect ratios

**What I was working on.** A project update explainer on building the n8n webhook and ChromaDB ingestion pipeline, cut at 16:9 and 9:16.

**What I tried, and what I expected.**
- I sent raw financial reports through the embedding model using a standard 500-token chunking strategy.
- Expected ChromaDB to perfectly retain the financial context.

**Where it resisted, and what I did next.**
- Vector embeddings became fragmented and lost context due to poor chunking (e.g., separating a dollar amount from the quarter it belonged to).
- Fixed by altering the ingestion payload in n8n to retain structural financial markers (strictly formatting as JSON key-value pairs) before embedding.

**What Claude contributed, and what I did with it.**
- Mine: The n8n routing logic, FastAPI webhook, and ChromaDB integration.
- Claude's: Reviewing the video pacing. Claude caught the stale-persona audio (missing the required verbatim intro) in the initial render. I regenerated the audio to match the project rules.

**What I understand now, and what I still do not.**
- Understood: Text chunking for embeddings requires semantic boundaries, not just arbitrary character limits.