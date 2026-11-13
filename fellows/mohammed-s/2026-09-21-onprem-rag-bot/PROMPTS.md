# PROMPTS — onprem-rag-chatbot

No open pantry slots in this reel (see `SHOTLIST.md`) — every beat is a
Remotion pattern or a Manim scene in `scenes.py`, so there are no
archive-search or AI-generation prompts to log here.

For reference, the two on-screen "ask" prompts this reel reconstructs (the
CLI loop's own content, not pantry requests):

- **B02 (cycle 1 ask):** `claude "write a docker-compose.yml that runs Ollama
  + Open WebUI together. Open WebUI's OLLAMA_BASE_URL must point at Ollama's
  OWN container over the internal Docker network — never an external host.
  Expose Open WebUI on 3000, Ollama on 11434, persist both with named
  volumes."`
- **B06 (cycle 2 revision ask):** `claude "the RAG answer above cites
  nothing — that's a hallucination, not a retrieval. Pull the
  nomic-embed-text embedding model in Ollama, set it as Open WebUI's RAG
  embedder (Admin Panel → Settings → Documents), and re-check retrieval on
  the same question. Also tighten chunk size to 500–1000 tokens."`
