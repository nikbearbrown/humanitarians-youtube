# Sources — Embedding Model Staleness: The Index That Quietly Split in Two

General AI/STEM topic explainer, illustrated with one real, reproducible local demo. An embedding
model is a function trained to map text into a fixed-dimensional vector space shaped entirely by
its own training process (architecture, training objective, and training data). This is a
well-established, broadly-taught fact about how these models work: there is no shared coordinate
system, origin, or scale across two independently-trained embedding models, so a vector produced by
one model and a vector produced by a different model are not directly comparable by any distance
metric (cosine similarity, Euclidean distance, dot product) even when both are valid,
same-dimensional, unit-norm vectors. This video describes the general, settled shape of this idea
qualitatively, and backs its central quantitative claim with one real, named, reproducible
experiment rather than citing any paper's benchmark number.

Four broad, well-documented qualitative points anchor this video's rubric:

- **A vector space is model-specific, not universal:** an embedding model's output space is a
  byproduct of its specific training run (architecture, objective, data). Two different models —
  or two different checkpoints/versions of a model that was retrained or fine-tuned further — are
  not guaranteed to share any alignment between their output spaces, structurally or empirically.
  This is a well-established architectural fact, not a benchmarked claim about any one named
  system.
- **Distance metrics compute a number regardless of whether it means anything:** cosine similarity,
  dot product, and nearest-neighbor search are all pure math operations over whatever vectors they
  are given; nothing in a typical vector index's data model records or checks which embedding model
  produced a given stored vector. Mixing vectors from two different models in one index with one
  distance metric will silently produce a numeric result every time, with no error raised by the
  math itself.
- **Model swaps are a common, real operational trigger:** embedding-model upgrades, cost
  optimization (swapping to a cheaper or faster model), and provider deprecations/migrations are all
  common, realistic events in applied AI/retrieval engineering — broadly discussed in the field as
  situations that require re-indexing, not just swapping the embedding call for new documents going
  forward.
- **The only correct remediation is a full re-embed:** because there is no general, reliable way to
  map one embedding model's space into another's without recomputing the embedding from the
  original text, the standard, well-documented operational guidance for any embedding-model change
  is a full re-embed and index rebuild — not an incremental/partial migration.

## This video's own real, reproducible demo

`verification/embedding_staleness_demo.py` (output captured verbatim in
`verification/demo_output.txt` from one real run on 2026-11-19) uses two real, different, published
HuggingFace sentence-transformer checkpoints, loaded via plain `transformers`
`AutoTokenizer`/`AutoModel` with mean-pooling and L2-normalization applied by hand in the script:

- **Model A:** `sentence-transformers/all-MiniLM-L6-v2` — the same model `mycroft`'s own `rag.py`
  defaults to (see the Real-world note below), chosen specifically so this demo is directly
  relevant to that real-world reference, not an arbitrary pick.
- **Model B:** `sentence-transformers/multi-qa-MiniLM-L6-cos-v1` — a different real, published
  checkpoint in the same MiniLM architecture family (same 384-dim output), trained on a different
  objective (QA-pair retrieval tuned for cosine similarity). Chosen because it is genuinely a
  different trained model, not a second run of the same one, which would only measure float noise.

What the demo actually measured, from one real run (see `verification/demo_output.txt` for full
output):

- **Part 1:** the identical sentence, embedded by both models, has a mean cross-model cosine
  similarity of only 0.7416 (range 0.6832–0.7801) across the 10-sentence corpus — far below the
  ~1.0 a shared geometry would produce for truly identical input.
- **Part 2:** aggregate similarity distributions over 100 cross-model document pairs (mean ≈0.10,
  std 0.225) vs. same-model pairs (mean ≈0.04–0.05, std 0.07–0.08) — the cross-model relationship
  carries far more noise and no usable, consistent signal.
- **Part 3:** on a 10-sentence corpus spanning 10 distinct topics, simulating a partially-migrated
  index (some documents' vectors left stale in Model A's space after a hypothetical switch to Model
  B), cosine similarity for stale documents measurably dropped (e.g. 0.6839→0.5897 and
  0.7774→0.6420 in two of the three tested queries) though top-1 ranking survived in all 3 cases on
  this particular, topically-distinct corpus — reported honestly, including where the ranking did
  NOT flip.
- **Part 4:** on a closer, more confusable real document pair (a "cash refund" sentence vs. a
  "store credit only" sentence, under a query asking specifically about cash vs. credit), the same
  mechanism produced a genuine top-1 rank inversion: the correct document won by a narrow real
  margin (0.6090 vs. 0.5859) when both were embedded with the current model, and LOST to the wrong
  document (0.5109 vs. 0.5859, the wrong document's score unchanged) once it alone was stuck in the
  old model's stale space — the same two real documents and the same real query, with only which
  model produced one document's stored vector changed.

These are this build's own real, reproducible numbers from real, named, open models — not a general
benchmark claim about either model's typical production accuracy, and not fabricated or
hypothetical figures. See `FACTCHECK.md` claims #1–#4 for the full verdict table.

## Real-world tie-in (named directly, per this video's explicit build instruction)

`mycroft`'s `Regulatory_QA` backend retrieval code,
`Core_Components/Regulatory_QA/backend/app/rag.py`, was read directly (read-only reference; no file
inside `mycroft` was modified) to confirm, rather than assume, the following before this video was
built:

- `RegulatoryRAG.__init__` (lines 15–20) builds `HuggingFaceEmbeddings(model_name=
  settings.embedding_model, model_kwargs={'device': 'cpu'})`.
- `app/config.py` line 18: `embedding_model: str = "all-MiniLM-L6-v2"` — the actual default value of
  that setting.
- `RegulatoryRAG.build_vectorstore()` (lines 168–179) calls `Chroma.from_documents(documents=
  documents, embedding=self.embeddings, collection_name="regulatory_feeds",
  persist_directory=None)` — a brand-new, non-persisted Chroma vector store every call.
- `app/routers/chat.py` (lines 8–31): the `POST /api/chat` handler calls `rag =
  get_rag_engine()` then `rag.build_vectorstore(feeds)` inline, on every single request, immediately
  before `rag.query(...)`.

This design rebuilds the entire vector store fresh on every chat request, which sidesteps the
entire embedding-staleness bug class by construction: there is never a persisted index for any
vector to go stale in. The real, honestly-acknowledged trade-off is that every request pays the
full cost of re-embedding the entire feed set from scratch. This is presented in the video strictly
as an illustrative design choice — not a report of a bug, because there isn't one here, confirmed by
direct source read rather than assumed from any summary.

## Distinct from adjacent, already-covered topics in this series

- `2026-09-07-embeddings-how-ai-tells-similar-from-different` teaches what an embedding space is
  and how similarity is measured within one space. This video assumes that mechanism and covers a
  distinct failure mode: a single index silently containing vectors from more than one incompatible
  space.
- `2026-09-22-hallucination-why-sounding-sure-isnt-being-right` covers whether a claim is fabricated
  at all. Unrelated to this video's topic.
- `2026-09-29-tokenization-why-ai-cant-count-its-own-letters` covers how text is chunked into
  tokens. Unrelated.
- `2026-10-06-lost-in-the-middle-why-more-context-isnt-better` covers position within content that
  DOES fit in context. This video is about whether a retrieved vector's distance is meaningful at
  all, a prior question.
- `2026-10-15-chain-of-thought-why-the-reasoning-isnt-always-the-reason` covers whether a stated
  reasoning trace caused the answer. Unrelated.
- `2026-10-21-calibration-why-confidence-isnt-accuracy` covers confidence vs. real accuracy.
  Unrelated.
- `2026-10-28-in-context-learning-limits` covers what a prompt alone can teach a model with no
  weight updates. Unrelated.
- `2026-11-04-goodharts-law-proxy-metrics` covers a tracked number diverging from its real target
  under incentive pressure. Unrelated.
- `2026-11-13-context-window-limits` covers a fixed, per-request token budget and overflow
  behavior — a request-time capacity question. This video covers a stored-index
  geometry-compatibility question, independent of any single request's size.
