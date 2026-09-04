# PEDAGOGY.md — GATE P — rag-pdf-pytorch

**Skill:** cli-explainer · **Persona:** Liam, in for Ameya (Onyx, `am_onyx`) · **Channel:** @HumanitariansAI
**Register:** Teardown · **Topic:** Retrieval-Augmented Generation over PDFs, in PyTorch
**Est. runtime:** ~3:30 (16:9)

GATE P is a QUALITY gate: a human reviews the narration and pedagogy BEFORE any
audio is generated. Not a cost gate — Kokoro audio is free.

## The one thing a viewer should be able to DO after watching
Explain the four stages of a RAG pipeline — chunk, embed, retrieve, ground — and
read the actual PyTorch that implements them: `model.encode` for embeddings,
L2-normalize so a dot product is cosine similarity, `q @ emb.T` + `torch.topk`
for retrieval, and a grounded prompt that answers only from the retrieved chunks.

## The through-line (problem → build → run → revise → run → meaning → next)
1. **B01 problem:** the model never read your PDF → "I don't know" or a confident hallucination.
2. **B02→B03→B04 (cycle 1, the index):** chunk with overlap, embed to unit vectors, place them in vector space.
3. **B05→B06→B07 (cycle 2, retrieval — the required revision):** embed the query, `q @ emb.T` cosine scores, `topk`, ground the prompt, cite the page.
4. **B08 verdict:** answers from evidence you can point to, not from memory.

## ACTUAL-CODE LAW
B03 and B06 show real, runnable PyTorch (sentence-transformers + torch), trimmed
to the lines that teach — not pseudocode. The ASK prompt plausibly generates the
CODE; the CODE plausibly produces the Manim OUTPUT.

## Honesty / scope
- Technical claims verified in [FACTCHECK.md](FACTCHECK.md): `all-MiniLM-L6-v2`
  emits 384-dim embeddings; L2-normalized dot product == cosine similarity;
  `torch.topk` returns the k largest. The `llm(...)` call is shown as a stand-in
  for the viewer's own model — labelled as such, not a specific product.
- Vector space is drawn in 2D as an explicit simplification of the 384-dim space
  (captioned on screen).

## SHOW-DON'T-TELL / ILLUSTRATE
Output beats (B04, B07) are Manim: the PDF slices into chunks that become points;
the query finds its k nearest and grounds the answer. The Claude UI appears only
at the ask/code/handoff/outro beats.

---

**PEDAGOGY VERDICT: PASS** — narration reviewed; code is real and correct;
show-don't-tell and revision-cycle laws satisfied; cleared for audio generation.
