# FACTCHECK — Embedding Model Staleness: The Index That Quietly Split in Two

Status: **RESOLVED — fellow reviewed 2026-11-19. Cleared for Gate P (narration lock).**

| # | Beat | Claim (as spoken/shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02/B03 | An embedding model maps text into a vector space shaped by its own training; two different models (or two checkpoints of "the same" model) place the same text in geometrically incompatible spaces — cosine similarity or nearest-neighbor distance between a vector from model A and a vector from model B is not meaningful, even if both are valid unit vectors of the same dimensionality | PASS — standard, well-established fact about how embedding models work: there is no shared coordinate system across independently-trained models, and nothing in the training objective of either model gives their output spaces a common origin, scale, or rotation. Directly confirmed empirically in this build's own real demo (`verification/demo_output.txt`, Part 1): mean cross-model cosine similarity of the IDENTICAL sentence embedded by two real, different sentence-transformer models was 0.7416 (range 0.6832–0.7801) — far below the ~1.0 a shared geometry would produce for identical text, and Part 2's aggregate distributions (same-model mean ≈0.04–0.05 vs. cross-model mean ≈0.10, with much higher cross-model variance, std 0.225) show the cross-model relationship carries no usable, consistent similarity signal | — | — |
| 2 | B02/B04 | Appending new documents embedded with a new model into an index whose old documents were embedded with a different (old) model silently mixes two incompatible geometries in one store, with no error thrown at index-build or query time | PASS — this is a direct, structural consequence of claim #1: a vector index/distance metric (e.g. cosine similarity, ANN search) has no built-in way to detect that two stored vectors come from different embedding spaces; it will compute and return a numeric distance regardless, because nothing in the data format records which model produced a given vector unless the application explicitly tracks that metadata itself | — | — |
| 3 | B04 | Queries embedded with the new model will retrieve nonsense neighbors among old-model vectors, or fail to surface genuinely relevant old documents, because distance in the new model's space doesn't mean what the index's distance metric assumes — all without throwing any error | PASS, with an honestly-reported real demo as evidence, not an assumed outcome — see `verification/demo_output.txt`: (a) Part 3, run on a 10-sentence corpus spanning 10 distinct topics: cosine similarity for a stale (old-model) document dropped measurably (e.g. one case 0.6839→0.5897, another 0.7774→0.6420) once mixed against a new-model query, though this particular corpus's wide topic margins meant top-1 ranking survived in all 3 tested queries — reported honestly as a real, non-flipping result, not hidden; (b) Part 4, on a closer, more confusable real document pair, the identical mechanism produced a genuine top-1 RANK INVERSION: the correct document won when both documents were embedded with the same (current) model (0.6090 vs. 0.5859) and LOST to the wrong document once it was the only one stuck in the old model's space (0.5109 vs. 0.5859, unchanged) — same two real documents, same real query, the only variable changed was which model produced one document's stored vector. No exception was raised in either case | Keep claim hedged as "can silently degrade or flip rankings," not "always flips the top result" — the demo itself shows both a non-flipping and a flipping real case, honestly | — |
| 4 | B04/B05 | The specific illustrative worked-example scenario (a document store fully indexed with one model, later switched to a newer model for new documents only, leaving old vectors un-migrated) and its falsifiability case (the identical switch, but with a full re-embed/rebuild before serving) | ILLUSTRATIVE — these are invented-for-teaching scenarios describing a well-documented, generic operational pattern (embedding-model upgrades, cost optimization swaps, and vendor/provider deprecations are all real, common triggers for exactly this kind of partial migration), not a report of any specific real incident or any specific real company's index. No real company, product, or specific numeric accuracy drop is claimed as representative of a universal rate — the ONE quantified figures in this video come from this build's own real, reproducible local demo (claim #3), reported as exactly that: one real run of two real, named, open models, not a benchmark claim about either model's typical behavior in production | Keep narration/on-screen text generic ("a document store," "a newer, cheaper model") for the worked example itself; keep the demo's real numbers clearly scoped to "this run" | — |
| 5 | B04/B05 | The only correct fix for an embedding-model change is to fully re-embed the entire corpus and rebuild the index from scratch — there is no incremental/partial migration path, because old vectors cannot be projected or adapted into the new model's space without redoing the actual embedding computation | PASS — this follows directly from claim #1: since there is no general, reliable mapping between two independently-trained embedding spaces (no shared coordinate system to "translate" through), the only way to get a vector that is valid in the new model's space is to run the new model's own forward pass on the original text again. This is a structural/mechanistic fact, not an empirical measurement, and is standard, well-documented operational guidance in applied embedding/RAG engineering | — | — |
| 6 | B06 | The real-world note about `mycroft`'s `Regulatory_QA/backend/app/rag.py`: it uses `HuggingFaceEmbeddings(model_name=settings.embedding_model)`, defaulting to `"all-MiniLM-L6-v2"` (confirmed in `app/config.py`), and `build_vectorstore()` calls `Chroma.from_documents(..., persist_directory=None)`, called fresh on every `POST /api/chat` request via `routers/chat.py`'s `rag.build_vectorstore(feeds)` — with the explicit framing that this is a design choice that sidesteps the entire embedding-staleness bug class by construction (no persisted index ever exists to go stale), at the real cost of re-embedding the full feed set from scratch on every request; NOT a report of a real bug, because there isn't one | PASS — confirmed by direct read of the actual source files before building this video (not assumed from the build brief's summary): `/Users/pranavijs/mycroft/scripts/mycroft-main/Core_Components/Regulatory_QA/backend/app/rag.py` lines 15–20 (`__init__`/`HuggingFaceEmbeddings`), lines 168–179 (`build_vectorstore`/`Chroma.from_documents(..., persist_directory=None)`), and `app/routers/chat.py` lines 29–31 (`get_rag_engine()` then `rag.build_vectorstore(feeds)` called inline on every request, before `rag.query(...)`); `app/config.py` line 18 (`embedding_model: str = "all-MiniLM-L6-v2"`). No file inside `mycroft` was modified — read-only reference per the hard constraint | — | — |
| 7 | B07, B08 | The scaffolded audit task (check whether every vector in an index you maintain comes from the same embedding model and version; if not, the only fix is a full re-embed) and the takeaway statement | PASS — a generic, runnable procedure and an editorial summary following directly from claims #1–#5, not a factual claim requiring further citation | — | — |
| 8 | Premise (BEAT-SHEET.md) | One-sentence distinction from the earlier, general embeddings video in this series (`2026-09-07-embeddings-how-ai-tells-similar-from-different`) | PASS — confirmed by checking that video's own title/scope: it teaches what an embedding space is and how similarity is measured within one space; this video assumes that mechanism already and is about a distinct failure mode (what happens when a SINGLE index silently contains vectors from more than one incompatible space) | — | — |

## Dramatization check

No beat claims a specific real production system's measured accuracy drop as if it were universal;
the only quantified numbers in this video are this build's own real, reproducible demo run
(`verification/demo_output.txt`), clearly scoped and reported as "this run," using two real, named,
open, locally-available sentence-transformer checkpoints
(`sentence-transformers/all-MiniLM-L6-v2` and `sentence-transformers/multi-qa-MiniLM-L6-cos-v1`) —
chosen because they are genuinely different, independently-trained, publicly documented models
(not two runs of the same model, which would only show measurement noise), and because
`all-MiniLM-L6-v2` is the same model `mycroft`'s own `rag.py` defaults to, making the demo directly
relevant to the real-world note in B06. The worked example (B04) and its falsifiability case (B05)
are both framed as generic, textbook-level illustrations of a well-documented operational pattern
(model upgrades/cost swaps/provider changes triggering partial re-indexing), consistent with this
fellow's established house style for STEM topic explainers. The real-world note (B06) names a real
project and quotes real source lines verbatim, but explicitly and repeatedly frames this as an
honest design-choice illustration, never as a bug report — because, per direct source confirmation,
there is no bug in mycroft's handling of this (its rebuild-fresh-every-request design has no
persisted index at all, so the staleness failure mode described in B04 structurally cannot occur
there).

## Verbatim accuracy check (B06 on-screen code quotes)

Re-confirmed directly against the live source files immediately before finalizing `scenes.py`, not
assumed from this file's own earlier read:

- `app/rag.py` line 18: `model_name=settings.embedding_model,` — quoted verbatim (trailing comma
  dropped for on-screen legibility, substance unchanged).
- `app/config.py` line 18: `embedding_model: str = "all-MiniLM-L6-v2"` — quoted verbatim in full.
- `app/rag.py` line 177: `persist_directory=None` — quoted verbatim, the exact argument/value pair
  from the real `Chroma.from_documents(...)` call (lines 173–178).
- `app/routers/chat.py` lines 30–31: `rag = get_rag_engine()` / `rag.build_vectorstore(feeds)` —
  quoted verbatim, confirming this executes on every request to `POST /api/chat` (line 8), not at
  startup or on a schedule.

No line was reformatted, reordered, or paraphrased where shown as a direct quote; narration refers
to the same facts in plain spoken language without claiming different wording appears on screen
than actually does.

## Distinct from this fellow's prior videos

This video is explicitly not a re-run of nine adjacent, already-covered topics in this series:

- **Not hallucination** (`2026-09-22-hallucination-why-sounding-sure-isnt-being-right`): whether a
  stated claim is fabricated. Unrelated — this video assumes every retrieved vector is a real,
  valid embedding and asks a geometry-compatibility question instead.
- **Not tokenization** (`2026-09-29-tokenization-why-ai-cant-count-its-own-letters`): how text is
  chunked into tokens before any reasoning happens. Unrelated to vector-space compatibility.
- **Not lost-in-the-middle** (`2026-10-06-lost-in-the-middle-why-more-context-isnt-better`):
  position of a fact within content that DOES fit in context. This video is about whether a
  retrieved vector's distance measurement means anything at all, a prior, structural question.
- **Not chain-of-thought faithfulness**
  (`2026-10-15-chain-of-thought-why-the-reasoning-isnt-always-the-reason`): whether a stated
  reasoning trace caused an answer. Unrelated.
- **Not calibration** (`2026-10-21-calibration-why-confidence-isnt-accuracy`): whether a stated
  confidence number tracks real accuracy. Unrelated.
- **Not in-context learning limits** (`2026-10-28-in-context-learning-limits`): what a prompt alone
  can teach a model with no weight updates. Unrelated.
- **Not Goodhart's Law / proxy metrics** (`2026-11-04-goodharts-law-proxy-metrics`): a tracked
  number diverging from its real target under incentive pressure. Unrelated — this video is about a
  geometry-compatibility failure, not a metric-divergence one.
- **Not context window limits** (`2026-11-13-context-window-limits`): a fixed, per-request token
  budget and what happens when it's exceeded — a capacity/overflow question at query time. This
  video is about a stored-index compatibility question that exists independent of any single
  request's size.
- **Not the earlier general embeddings video**
  (`2026-09-07-embeddings-how-ai-tells-similar-from-different`): that video teaches what an
  embedding space is and how similarity is measured WITHIN one space. This video assumes that
  mechanism is already understood and is about a distinct failure mode: what happens when a single
  index silently contains vectors from more than one incompatible space at once. No rubric name,
  tag, or specific phrasing from that video is reused here.

## Real-world tie-in (named directly, per explicit build instruction — kept strictly honest)

Unlike this series' usual house rule of keeping a real-world tie-in fully generic/unnamed, this
video's build brief explicitly directed naming the real project and file (`mycroft`'s
`Regulatory_QA/backend/app/rag.py`) as an honest illustrative side-note — never as a bug report,
because direct source confirmation shows there is no bug in mycroft's handling of this (see claim
#6 above). `mycroft` was read-only reference throughout; no file inside it was modified, per the
hard constraint.

## Resolved 2026-11-19

1. Confirmed the core mechanism claims (#1–#5) against standard, well-established facts about how
   independently-trained embedding models produce geometrically incompatible vector spaces, and
   confirmed the ONE quantified demo in this video (claim #3) is a real, reproducible run of two
   real, named, open models — not a fabricated or hypothetical number, and not presented as a
   general benchmark of either model.
2. Confirmed the real-world note (claim #6) by directly reading `mycroft`'s actual source files
   (`rag.py`, `config.py`, `routers/chat.py`) rather than taking the build brief's summary as given,
   and confirmed no bug exists there for this failure mode, by construction.
3. Confirmed distinct from nine prior videos in this series, with particular care taken on the two
   closest adjacent topics: the general embeddings video (what similarity means within one space)
   and the context-window-limits video (a different kind of fixed-resource/overflow question).

Gate P (narration review) can proceed.
