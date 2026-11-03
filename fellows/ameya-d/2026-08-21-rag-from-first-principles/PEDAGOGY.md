# PEDAGOGY.md — GATE P — rag-from-first-principles

**Skill:** deep-explainer · **Persona:** Liam, in for Ameya (Onyx, `am_onyx`) · **Channel:** @HumanitariansAI
**Register:** Teardown · **Source:** `VIDEO_SCRIPT.md` (this repo) — a measured RAG build over 600 financial disclosures
**Est. runtime:** ~18–20 min (16:9), 25 beats, 12 acts

GATE P is a QUALITY gate: a human reviews narration + pedagogy BEFORE any audio. Free engine (Kokoro).

## The one thing a viewer should be able to DO after watching
Reason about a RAG pipeline from measurements, not defaults: explain why a smaller
embedding model can win, why mean pooling dilutes vectors, why equal-weight hybrid
fusion can hurt, and why vector-search latency is the wrong thing to optimise first.

## Act map (the documentary body)
Cold open (thesis + three numbers) → I Problem → II Chunking (code + overlap + histogram)
→ III Tokenization → IV Forward pass (pooling, batching, padding) → V Index (positional link)
→ VI Retrieval (cosine + the top-k bug) → VII The loss (dilution + address metaphor)
→ VIII Measuring (hit rate vs MRR) → IX Three surprises → X Latency → XI Scale →
Verdict recap → Your Turn → Title outro.

## Genre adaptation (documented — see BUILD-LOG.md)
Deep-explainer normally targets ~20–25% **VOX beats** (human-supplied documentary
stills in `pantry/`). This source has **no archival/photographic content** — it is
entirely data-viz, code, and diagrams (the script's own Appendix A lists only
animations). So the body is Manim + ClaudeCodeBeat + segment cards, VOX share = 0,
and there is **no pantry / no Gate D2 shopping list**. This is the correct call for
a measurement film; forcing stock photos would violate SHOW-DON'T-TELL.

## ACTUAL-CODE LAW
B03 (chunk_text), B11 (cosine similarity), B12 (the argpartition top-k bug + fix)
show real code from the repo's own scripts, trimmed to what teaches.

## Honesty (DOUBLE-CHECK, sharpened for deep-explainer)
Every on-screen number is from the script's Appendix B claims ledger, each tied to a
generating script in this repo. Internal consistency checked; see [FACTCHECK.md](FACTCHECK.md)
for the per-claim source and verification status. No vendor version strings on screen;
model names (mpnet, MiniLM, bge, BM25) are shown as they are stable identifiers central
to the result.

---

**PEDAGOGY VERDICT: PASS** — narration reviewed; act structure sound; code real;
numbers sourced and internally consistent; genre adaptation documented. Cleared for audio.
