# Week 2: Data Ingestion & Orchestration — Video Script

**Series:** Provenance Gatekeeper Development Log
**Runtime target:** 2:45
**Format:** 3840 × 2160 (4K UHD), 24 fps. Dual Render: 16:9 AND 9:16.

### SCENE 1 — HOOK
**VISUAL** — Ground fill. A raw JSON file of financial data snaps in.
`{"revenue": 4000000, "quarter": "Q3"}`
**ON SCREEN:** `TRUTH REQUIRES MEMORY`
**VO:**
I am Onkar Bhujbal, a software engineer. You cannot evaluate whether an AI is hallucinating unless you give the system an unshakeable source of truth. This week, we built the memory core for the Provenance Gatekeeper: the data ingestion pipeline and the orchestrator webhook.

### SCENE 2 — THE FRAMEWORK
**VISUAL** — Flowchart snaps in.
`01 N8N ORCHESTRATOR` -> `02 FASTAPI WEBHOOK` -> `03 CHROMADB`
**VO:**
The architecture bridges external workflows with internal vector storage. First, our n8n orchestrator acts as the transport layer, pushing hand-labeled financial ground-truth data toward our system. Our FastAPI backend exposes a dedicated webhook to intercept this data, process it through HuggingFace embeddings, and commit it to a local ChromaDB instance. 

### SCENE 3 — WORKED EXAMPLE
**VISUAL** — Side-by-side comparison.
**LEFT:** n8n node triggering an HTTP POST.
**RIGHT:** FastAPI terminal showing `200 OK: Embedded 15 vectors.`
**VO:**
Watch the handoff. n8n fires a JSON payload containing known financial ledgers. FastAPI catches the webhook, strips out the noise, and mathematically embeds the text. The data is now permanently locked into ChromaDB's geometric space, ready to act as the baseline truth for our future evaluation layer.

### SCENE 4 — FALSIFIABILITY
**VISUAL** — The terminal flashes red.
**ON SCREEN:** `GARBAGE IN, GARBAGE OUT`
**VO:**
Where does this pipeline break? Context fragmentation. If you chunk your financial documents poorly before generating embeddings, ChromaDB will store fragmented sentences that lack numeric context. When the Gatekeeper eventually searches for the truth, it will retrieve mathematical nonsense.

### SCENE 5 — SCAFFOLDED TASK & CLOSE
**VISUAL** — Hard cut to mono text.
`collection.add(documents=["Q3 Revenue is $4M"], ids=["id1"])`
**VO:**
Build the memory. Spin up a local ChromaDB instance and write a Python script to ingest a single string of financial data using a HuggingFace embedding model. See how quickly text becomes coordinates.
Liam, for Onkar Bhujbal and Humanitarians AI.