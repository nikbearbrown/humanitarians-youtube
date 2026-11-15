# Explainer — Redis Caching Layer

**Week:** 09 Nov – 15 Nov 2026
**Type:** Work update

- **Drive:** https://drive.google.com/drive/folders/1qpr3v3ChgIlXmDdV-0Vr64kosfMAcsNV

## What it covers
Implementing a Redis in-memory data store via Docker Compose to cache frequent financial claims. It demonstrates modifying the FastAPI endpoint to check the cache before engaging the PyTorch `SentenceTransformer` and ChromaDB vector search.

## Why this topic, this week
Kicking off Phase 2 (Scale & Speed). Vector similarity searches are computationally expensive. In a production environment where standard financial metrics (e.g., "Q3 Revenue was $50M") might be evaluated repeatedly, caching prevents redundant machine learning inference, radically dropping API latency and reducing server costs.

## Limits
- Source files for the video: see the Drive folder.