# Weekly STEM Video: Embedding Model Staleness — The Index That Quietly Split in Two

**Fellow:** Sai Pranavi J.
**Series:** Humanitarians AI Fellows — Weekly STEM Video (`ai-explainer`)
**Source status:** General AI/STEM topic explainer, not a report of the fellow's own engineering
work on a live incident. Describes a well-documented, generic fact about embedding-model geometry
incompatibility qualitatively, backed by one real, reproducible local demo using two real, named,
open sentence-transformer models. B06 names a real reference project (`mycroft`'s `rag.py`) as an
honest design-choice illustration, confirmed by direct source read — not a bug report; there is no
bug there, by construction. See `FACTCHECK.md` and `SOURCES.md`.

## Watch

- Landscape (4K 16:9): `deliverables/landscape/EmbeddingModelStaleness_SaiPranaviJ.mp4`
- Vertical (4K 9:16): `deliverables/vertical/EmbeddingModelStaleness_SaiPranaviJ.mp4`

This video teaches a reusable 3-question test — **Check the Checkpoint / Audit the Whole Index /
Watch for Silence** — for reasoning about embedding model staleness: an embedding model maps text
into a vector space shaped entirely by its own training, so two different models — or two
checkpoints/versions of "the same" model — place the same text in geometrically incompatible
spaces, even when both produce valid, same-dimensionality unit vectors. The framework is taught in
full before any example, walked through a worked example (a document store fully indexed with one
embedding model, later switched to a newer model for new documents only, leaving the old vectors
stuck in the old geometry and their search rank silently falling, with no error anywhere), stress-
tested against a falsifiability case where the identical upgrade and the identical old corpus do
NOT produce a silent problem because every old document is fully re-embedded and the index rebuilt
from scratch before serving a single query, tied to a real, honestly-described design choice in a
reference project's actual retrieval code, and closed with a concrete audit task the viewer can run
today against any embedding-backed search or retrieval feature they already maintain.

## What this covers (and what it deliberately leaves out)

Covered: a hook showing a generic vector-index panel holding documents from two different embedding
models at the same dimensionality, posing the video's real question (B02); all 3 tests shown
together, before any example (B03); a worked example (B04) where an illustrative 1,000-document
corpus is split between an old and a new embedding model after an upgrade, and the old documents'
search rank quietly falls once a query only understood in the new model's geometry searches the
whole index at once, tagged "SPLIT GEOMETRY — SILENTLY"; a falsifiability case (B05) where the
identical upgrade and corpus are paired with a full re-embed and index rebuild before serving,
tagged "FULLY RE-EMBEDDED — NOTHING TO MIX"; a real-world note (B06) naming and verbatim-quoting a
reference project's actual retrieval code as an honest design-choice illustration, not a bug
report; a concrete audit task distinct from the framework card (B07); and a closing takeaway.

Deliberately left out: this is not a report of any real system's actual production accuracy drop,
and the only quantified figures anywhere in this video come from this build's own real,
reproducible local demo (`verification/`), reported as a single real run of two real, named, open
models, not a general benchmark claim. This is also a distinct topic from nine adjacent,
already-covered videos in this series — see `FACTCHECK.md`/`SOURCES.md` for the full list,
including the closest two: the earlier general embeddings video
(`2026-09-07-embeddings-how-ai-tells-similar-from-different`, what similarity means WITHIN one
space — this video is about a single index silently containing vectors from more than one
incompatible space) and the context-window-limits video
(`2026-11-13-context-window-limits`, a request-time token-budget capacity question, not a
stored-index geometry-compatibility question).

## Real, reproducible evidence (not hypothetical numbers)

`verification/embedding_staleness_demo.py` (output captured verbatim in
`verification/demo_output.txt` from one real run on 2026-11-19) uses two real, different, published
HuggingFace sentence-transformer checkpoints —
`sentence-transformers/all-MiniLM-L6-v2` (the same model `mycroft`'s own `rag.py` defaults to) and
`sentence-transformers/multi-qa-MiniLM-L6-cos-v1` (a different real, published checkpoint, same
MiniLM-family architecture, different training objective) — loaded via plain `transformers`
`AutoTokenizer`/`AutoModel` with mean-pooling and L2-normalization applied by hand in the script.
Real measured results: the identical sentence embedded by both models has a mean cross-model
cosine similarity of only 0.7416 (far below the ~1.0 a shared geometry would produce); a
partially-migrated 10-document index measurably degrades a stale document's similarity score even
when its rank survives; and a closer, more confusable document pair produces a genuine top-1 RANK
INVERSION — the correct document wins when both are embedded by the current model (0.6090 vs.
0.5859) and loses to a wrong document once it alone is stuck in the old model's stale space (0.5109
vs. 0.5859 unchanged). See `verification/demo_output.txt` for the full real output and
`FRICTIONAL.md` for how this evidence was found and verified.

## Production state

- Plan: **approved (Gate P)** — signed 2026-11-19
- Fact-check gate: **resolved** — see `FACTCHECK.md`
- Narration approval: **approved** — Kokoro `af_bella`, cleared 2026-11-19
- Voice: **Bella (`af_bella`)** — persistent for this fellow's whole series
- Previz: **complete** — 10/10 beats real Manim, no slates, both aspects
- Final render — **16:9 landscape:** `EmbeddingModelStaleness_SaiPranaviJ.mp4`, **3840x2160, 24fps,
  h264/aac, 202.5s (4860 frames)**. GATE V on the true clean master (verified directly, not the
  review slate): **0 BLOCKER, 0 MAJOR.**
- Final render — **9:16 vertical (full-length, native portrait, not a Shorts cut):**
  `EmbeddingModelStaleness_SaiPranaviJ.mp4`, **2160x3840, 24fps, h264/aac, 202.5s (4860 frames)** —
  frame-exact match with the landscape master (not just matching rounded seconds), all 10 beats
  kept, no drops, no duration cap. GATE V on the true clean master (verified directly, not the
  review slate): **0 BLOCKER, 0 MAJOR.**
- Publishing: **ready for review, not authorized** — masters stay in this folder only; requires
  fellow/PM sign-off per `brutalist/docs/FELLOWS-SUBMISSION.md`

## Built under the toolkit's new submission spec

Built under the toolkit's official spec (`brutalist/docs/FELLOWS-SUBMISSION.md`, effective
2026-09-07): `ProjectName_VolunteerName.mp4` naming (no date/aspect suffix), separate
`deliverables/landscape/` and `deliverables/vertical/` folders, and a true full-length 4K
2160x3840 vertical companion built via `./art vertical` (not a <=180s Shorts-style cut) — every
beat, no cuts, no added endcard.

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted and approved
- `beat_sheet.json` / `vertical/beat_sheet.json` — the same plan in the pipeline's structured
  schema, both aspects
- `FACTCHECK.md` — claim-level review confirming the mechanism, worked example, falsifiability
  case, and the real-world note's verbatim accuracy
- `SOURCES.md` — claim → source mapping
- `SHOTLIST.md` / `PROMPTS.md` — beat-by-beat medium/timing table and pantry/asset status (no
  pantry assets needed — all Manim)
- `scenes.py` / `vertical/scenes.py` — the Manim source for both aspects
- `verification/embedding_staleness_demo.py` / `verification/demo_output.txt` — the real,
  reproducible local demo and its captured real output, backing this video's one quantified claim
- `BUILD-LOG.md` — dated build decisions, bugs found and fixed, and gate history
- `FRICTIONAL.md` — contemporaneous build log of what resisted and what Claude contributed
