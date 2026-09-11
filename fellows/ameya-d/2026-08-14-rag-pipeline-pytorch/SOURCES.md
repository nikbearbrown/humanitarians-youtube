# SOURCES — rag-pdf-pytorch

This is a general technical explainer (not drawn from a repo chapter). The code
is standard, runnable PyTorch; correctness is verified in FACTCHECK.md.

## What the reel is built on
- **RAG pattern:** Lewis et al., "Retrieval-Augmented Generation for
  Knowledge-Intensive NLP Tasks" (2020) — retrieve relevant passages, then
  condition generation on them.
- **Embeddings:** `sentence-transformers` (`all-MiniLM-L6-v2`, 384-dim), which
  runs on PyTorch.
- **PDF text:** `pypdf` page text extraction.
- **Retrieval math:** cosine similarity via L2-normalized dot product;
  `torch.topk` for the k nearest.

## Code shown (real, trimmed to what teaches)
- B03 `rag.py — build the index`: `model.encode(...)` → tensor, then
  `torch.nn.functional.normalize(emb, dim=1)`.
- B06 `rag.py — retrieve + ground`: `q @ emb.T`, `torch.topk`, and a grounded
  prompt that answers only from the retrieved context and cites it.

Both snippets run against a real `paper.pdf` with the named libraries installed
(`pip install sentence-transformers pypdf torch`); `llm(...)` is the viewer's own
model call.

*Educational — the pipeline is a teaching reference, not production code (no
persistence, batching, or re-ranking).*
