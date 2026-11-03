# SOURCES — onprem-rag-chatbot

## Primary source
User-provided guide, pasted directly into the build conversation on
2026-08-23: "Building a Private, On-Prem 'Chat With Your Data' System with
Open WebUI + Ollama." No other source was fetched; every factual claim in
the beat sheet traces to this document.

## What is verbatim / trimmed
- **B03** `docker-compose.yml` — verbatim from the source's Part 3.1, both
  services and both named volumes intact, comments added only to point at
  the `OLLAMA_BASE_URL` line.
- **B07** pull command + Admin Panel settings path — verbatim from the
  source's Part 3.3 (`docker exec -it ollama ollama pull nomic-embed-text`,
  Admin Panel → Settings → Documents, embedding engine/model fields).
- **B04** hardware figures — the source's Part 1 table, simplified to
  RAM-only bars (source gives RAM-or-VRAM ranges per tier); captioned
  "Redrawn (simplified)" on screen per the REBUILD LAW.
- **B06/B07** "500–1000 token" chunk range and "chunk size matters more than
  model size" — the source's own Part 4 practical tip, restated.

## What is constructed for illustration (not claimed as an observed event)
- **B05 → B08's HR-handbook scenario.** The source states, generally, that
  (a) an LLM has no access to your private documents without RAG, and
  (b) RAG cannot retrieve anything without an embedding model producing
  vectors first. Neither the specific document ("HR-handbook.pdf"), the
  specific question ("what's the remote-work policy?"), nor the specific
  fabricated answer ("3 days") appear in the source — they are a constructed
  worked example built to demonstrate a real, well-documented RAG failure
  mode (missing embedder → zero retrieval → the model falls back to its own
  parametric memory and answers fluently but ungrounded). This is disclosed
  in `beat_sheet.json`'s `metadata.note` and in `PEDAGOGY.md` item 5.

## Model/version-drift language avoided
Model names (Llama 3.1 8B, Qwen3-30B-A3B, nomic-embed-text) are presented as
the source document's current recommendation, never as a permanent "best"
claim — matching the DOUBLE-CHECK LAW's instruction to strip anything that
will date the video.

## No corrections needed
The source document is internally consistent and technically accurate on
its own terms (RAG mechanics, Docker networking, WCAG-unrelated hardware
sizing); no factual errors were found that required correction before
scripting.
