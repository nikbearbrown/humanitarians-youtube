# SOURCES — RAG Pipelines, End to End

Primary: Patrick Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", NeurIPS 2020 — https://arxiv.org/abs/2005.11401 (coined "RAG": a retriever over a dense vector index + a generator conditioned on the retrieved passages).
Brief supplied by the requester (Likhith); the 8 points were checked against the primary source and standard practice (retrieved 2026-09-28).

## Evidence (executed, not typed)
- `evidence/cosine_toy.py` → `evidence/cosine_toy.out.txt` — Python 3.14.5, stdlib only, no seed needed (deterministic).
  sha256(cosine_toy.py) = 645e56d1d637fc652028162663336b5fbedac046045754dc7f6002055d0bcc04
  Scores shown in B06 (0.99 / 0.97 / 0.68 / 0.16) are that script's output; RagRetrieve recomputes them from the same vectors at render.

## Corrections / de-sensationalising
- Brief point 8 "answer accurately": RAG improves grounding, it does not guarantee accuracy — narration says "answers about documents it never saw" and adds the limit "only as good as its retrieval" (B09).
- Brief point 1: training data is shown as "public web text / books / code, frozen at a training cutoff" — generic categories, no model-specific claim.
- Brief point 2: "slow and expensive" kept qualitative; no cost or time figures shown.
- Brief point 5: cosine similarity is the common metric, not the only one (dot product, Euclidean also used). Narration names cosine per the brief; nothing claims exclusivity.
- Vectors are 2-D toys, labelled on screen ("real embeddings have hundreds of dimensions"). Handbook, chunks, prompt and answer are illustrative and labelled.
