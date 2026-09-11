# FACTCHECK.md — rag-pdf-pytorch

Technical claims shown or narrated, with verdicts. This reel teaches a standard
RAG pipeline; the code is real PyTorch and was checked for correctness.

| Beat | Claim | Verdict | Check |
|------|-------|---------|-------|
| B01 | LLMs without retrieval answer "don't know" or hallucinate on unseen docs | ✅ TRUE | well-documented LLM failure mode; RAG (Lewis et al., 2020) is the standard fix |
| B02/B03 | sentence-transformers runs on PyTorch | ✅ TRUE | `sentence-transformers` is built on PyTorch; `SentenceTransformer` wraps `torch.nn.Module` |
| B03 | `all-MiniLM-L6-v2` → 384-dim embeddings | ✅ TRUE | documented embedding dimension of that model is 384 |
| B03 | overlapping chunks avoid cutting a straddling sentence | ✅ TRUE | standard chunking rationale; `size - overlap` stride implements it |
| B03/B06 | L2-normalized vectors → dot product == cosine similarity | ✅ TRUE | cosine(a,b)=a·b/(‖a‖‖b‖); with ‖a‖=‖b‖=1 it reduces to a·b |
| B06 | `q @ emb.T` scores the query against all chunks at once | ✅ TRUE | (1×384)·(384×n)=(1×n) similarity row |
| B06 | `torch.topk(scores, k)` returns the k most similar | ✅ TRUE | topk returns k largest values/indices |
| B06 | grounded prompt ("answer ONLY from context; if not here, say so") reduces hallucination | ✅ TRUE (directionally) | grounding + refusal instruction is the standard mitigation; not a guarantee |
| B07 | citation lets you verify the answer | ✅ TRUE | the retrieved chunk carries its source page; claim is checkable |

## Honest simplifications (logged)
- **2D vector space.** The real space is 384-dim; the Manim scenes draw it in 2D
  and say so on screen. Nearness in the drawing stands in for cosine similarity.
- **`llm(prompt)`** is a placeholder for the viewer's own model call (Claude API,
  a local model, etc.) — shown as a function, not a specific product, so the reel
  doesn't date or advertise.
- Page number in the citation ("p.7") is illustrative of the mechanism (each chunk
  keeps its source page), not a claim about a specific document.

No drift-prone version numbers are shown on screen beyond the model name, which is
a stable identifier.
