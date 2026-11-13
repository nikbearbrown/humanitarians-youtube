# FACTCHECK — onprem-rag-chatbot

Source: user-provided guide, "Building a Private, On-Prem 'Chat With Your
Data' System with Open WebUI + Ollama" (pasted 2026-08-23). Format: claim |
verdict | source | fix.

| # | Claim (on screen / narrated) | Verdict | Source | Fix |
|---|---|---|---|---|
| 1 | Open WebUI is a frontend only; inference happens in Ollama, not Open WebUI | ✓ | Source Part 1, "What is Open WebUI?" | — |
| 2 | `OLLAMA_BASE_URL` pointed at the Ollama container (not an external host) is what keeps the stack private | ✓ | Source Part 2, "Confirming zero external API calls" | — |
| 3 | `docker-compose.yml` — both services, `OLLAMA_BASE_URL=http://ollama:11434`, both named volumes (B03) | ✓ verbatim | Source Part 3.1 | — |
| 4 | RAG steps: chunk → embed → store (ChromaDB) → retrieve → generate (B00, B05, B08) | ✓ | Source Part 1, "What is RAG?" | — |
| 5 | 8B model (Llama 3.1 / Qwen3 8B): 8–16GB RAM or 6–8GB VRAM, CPU-viable but slow (B04) | ✓ (simplified to RAM-only bars on screen) | Source Part 1 hardware table | Captioned "Redrawn (simplified)" |
| 6 | Qwen3-30B-A3B: MoE, ~3B active params/token, ~16–24GB RAM/VRAM (B04) | ✓ | Source Part 1 hardware table + Part 2 "LLM for generation" | — |
| 7 | 70B-class model: 40–48GB+ VRAM, not practical without a GPU (B04) | ✓ | Source Part 1 hardware table | — |
| 8 | Embedding models are tiny (100M–600M params), run fine on CPU regardless of LLM choice (B04) | ✓ | Source Part 1, "General rules of thumb" | — |
| 9 | `nomic-embed-text` is the default/most battle-tested embedding model, one `ollama pull` away (B06/B07) | ✓ | Source Part 2, "Embedding model for retrieval" | — |
| 10 | `docker exec -it ollama ollama pull nomic-embed-text` + Admin Panel → Settings → Documents → set embedding engine/model (B07) | ✓ verbatim | Source Part 3.3 | — |
| 11 | Chunk size 500–1000 tokens; chunk size matters more than model size for answer quality (B06/B07/B09) | ✓ | Source Part 1 ("500–1000 tokens") + Part 4 practical tips | — |
| 12 | Without an embedding model configured, nothing can be vectorized, so nothing can be retrieved | ✓ (mechanistic inference, not stated as a single sentence in the source but follows directly from Part 1 steps 2–4) | Source Part 1, "What is RAG?" steps 2–4 | — |
| 13 | The specific HR-handbook / remote-work-policy demo and its fabricated "3 days" answer (B05, B08) | CONSTRUCTED — not in source | n/a — illustrative worked example | Disclosed in `beat_sheet.json` metadata.note and `SOURCES.md`; narration never claims this was an observed real run |

## DOUBLE-CHECK LAW notes
- No model-version-drift numbers presented as permanent (model names are the
  source's current recommendation, framed that way).
- No claim on screen exceeds what the source states or what follows
  mechanically from steps the source itself describes.
- Item 13 is the one constructed scenario in the reel; it is flagged, not
  hidden, in three places (`beat_sheet.json`, `PEDAGOGY.md`, `SOURCES.md`).
