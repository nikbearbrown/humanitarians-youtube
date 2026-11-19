# Beat Sheet (APPROVED — Gate P, 2026-11-19): "Embedding Model Staleness: The Index That Quietly Split in Two"

**Creator:** Sai Pranavi J. | Weekly STEM video (general AI/STEM topic explainer,
distinct from the weekly project-update report)
**Format:** `ai-explainer`, framework-first teaching structure (same register as this fellow's
prior STEM videos: hallucination, tokenization, lost-in-the-middle, chain-of-thought
faithfulness, calibration, in-context learning limits, Goodhart's Law / proxy metrics, context
window limits)
**Phase:** 2 — approved for narration lock / audio generation. Fully generic worked example, no
real model/vendor benchmarked — see `FACTCHECK.md`.

---

## Premise

**What this covers:** a reusable 3-question test — "Check the Checkpoint / Audit the Whole Index /
Watch for Silence" — for reasoning about embedding model staleness: an embedding model maps text
into a vector space shaped entirely by its own training, so two different models — or even two
versions/checkpoints of "the same" model — place the same sentence in geometrically incompatible
spaces, even though both produce mathematically valid unit vectors of the same dimensionality.
Teaches the test before any example, walks it through a worked example (a generic, invented-for-
teaching scenario: a document store fully indexed with one embedding model, later switched to a
newer model for new documents only, leaving the old vectors stuck in the old geometry — silently
degrading retrieval for the old documents with no error anywhere), stress-tests it against a
falsifiability case designed to show the rubric isn't "any model swap always breaks things" (the
identical swap and the identical old corpus, but this time every old document is fully re-embedded
and the index rebuilt from scratch before serving a single query, so there's only ever one
geometry in the store and nothing to mix), ties the mechanism to a real, honestly-described design
choice in this fellow's own reference project's retrieval code (not a bug report — a real
illustration of dodging the whole bug class by construction, at a real cost), and closes on a
concrete audit task the viewer can run today against any embedding-backed search or retrieval
feature they already maintain.

**What this deliberately avoids:** this is not a report of the fellow's own engineering work on a
live incident, and does not name or benchmark any specific real model's numeric accuracy drop as
if it were a universal, current fact (the real demo in `verification/` measures a real, specific
run of two real, named, open models — reported honestly as exactly that, a single reproducible
run, not a general benchmark claim about either model). This is also a distinct topic from nine
earlier videos in this series: **not hallucination**
(`2026-09-22-hallucination-why-sounding-sure-isnt-being-right`, fabrication), **not tokenization**
(`2026-09-29-tokenization-why-ai-cant-count-its-own-letters`, how text is chunked), **not
lost-in-the-middle** (`2026-10-06-lost-in-the-middle-why-more-context-isnt-better`, position within
content that DOES fit), **not chain-of-thought faithfulness**
(`2026-10-15-chain-of-thought-why-the-reasoning-isnt-always-the-reason`, whether a stated reasoning
trace caused the answer), **not calibration**
(`2026-10-21-calibration-why-confidence-isnt-accuracy`, confidence vs. accuracy), **not in-context
learning limits** (`2026-10-28-in-context-learning-limits`, what a prompt alone can teach), **not
Goodhart's Law / proxy metrics** (`2026-11-04-goodharts-law-proxy-metrics`, a tracked number
diverging from its real target), and **not context window limits**
(`2026-11-13-context-window-limits`, a fixed token-budget capacity ceiling and overflow behavior —
a request-time limit, not a stored-index geometry-compatibility question). There is also an earlier
video in this series on embeddings generally
(`2026-09-07-embeddings-how-ai-tells-similar-from-different`), which teaches what an embedding
space IS and how similarity is measured within one; this video assumes that already and is about a
distinct failure mode — what happens when a SINGLE index silently contains vectors from more than
one incompatible space. No specific context-window size, token budget, or calibration curve from
those videos is reused or re-explained here.

**Real-world tie-in (named directly, by explicit instruction, kept strictly honest — this is a
design-choice illustration, not a bug report):** this fellow's own reference project's retrieval
code, `rag.py` in the `mycroft` repo's `Regulatory_QA` backend
(`Core_Components/Regulatory_QA/backend/app/rag.py`), uses `HuggingFaceEmbeddings(model_name=
settings.embedding_model)` (default `"all-MiniLM-L6-v2"`, confirmed in `app/config.py`) and rebuilds
its Chroma vector store completely fresh (`persist_directory=None`) on every single `POST
/api/chat` request (confirmed via `routers/chat.py`, which calls `rag.build_vectorstore(feeds)`
inline on every request before querying). This sidesteps the entire embedding-staleness bug class
by construction — there is never a persisted index to go stale, because there is never a persisted
index at all — at the real cost of re-embedding the full feed set from scratch on every request.
Confirmed directly by reading the source before building this video, not assumed from a summary;
see `FACTCHECK.md` and `SOURCES.md`. No bug is claimed anywhere in mycroft — there isn't one, by
this exact design.

**Source status:** general AI/STEM topic explainer, illustrated with one real, reproducible local
demo (`verification/embedding_staleness_demo.py` and its captured real output,
`verification/demo_output.txt`) using two real, different, published sentence-transformer
checkpoints. See `FACTCHECK.md`.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated, opens with the required "Hi, I'm Sai Pranavi J., this video is about..." line |
| B03 Framework | All 3 tests shown together as a checklist, before any example | Framework-first |
| B04 Worked example | The corpus split (old-model docs vs. new-model docs), the query, and the old document's rank silently falling, all visible together, tagged "SPLIT GEOMETRY — SILENTLY" | The split, the query, and the silent rank drop must all be visible together so the mechanism is legible, not just asserted |
| B05 Falsifiability | The identical corpus and switch event, with every old document fully re-embedded before serving, tagged "FULLY RE-EMBEDDED — NOTHING TO MIX" | Visibly different resolution from B04 |
| B06 Real-world note | Verbatim-quoted lines from `rag.py`/`config.py`, clearly cited by file, framed as a design choice, not a bug | Exact source text, double-checked against the real file |
| B07 Scaffolded task | The 3 tests restated as a concrete, runnable checklist | Actionable, not a restatement of B03 |
| B09 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi J. |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "Embedding Model Staleness: The Index That Quietly Split in Two" +
@HumanitariansAI. No narration.

**B01. Exec summary (~0:04–0:18)**
VO: "Hi, I'm Sai Pranavi J. This video is about embedding model staleness, why swapping or
upgrading the model that turns your documents into vectors can silently break similarity search,
even when nothing ever throws an error, and three checks for catching it before your users do."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:18–0:40)**
VO: "Every embedding model maps text into its own private geometry, shaped entirely by how it was
trained. Two different models, even two versions of the same one, place the exact same sentence in
spaces that don't line up with each other. Swap your embedding call mid flight, leave the old
vectors sitting in the index, and you've quietly split your search into two incompatible
geometries, mixed together in one store."
Visual: a generic "VECTOR INDEX (ONE SPACE?)" panel showing docs from Model A and Model B at the
same dimensionality, then an overlay posing the real question: two geometries — did anything
notice?

**B03. Framework (~0:40–1:12)**
VO: "Here's the test, before any example, three questions. One, check the checkpoint: is every
vector in this index, old and new, from the exact same embedding model and version, not just the
same vendor name? Two, audit the whole index: when that model changed, was every existing vector
actually recomputed, or only the documents added from that point on? Three, watch for silence: when
two geometries get mixed in one index, does anything error, or does it just hand back worse
neighbors and keep going?"
Visual: checklist card, all 3 tests shown together (Check the Checkpoint / Audit the Whole Index /
Watch for Silence).

**B04. Worked example (~1:12–1:42)**
VO: "Picture a document store, fully indexed with one embedding model. Months later, the team
upgrades to a newer, cheaper model, and only points new documents at it. The old vectors stay
exactly where they were. A query comes in, embedded with the new model, and searches the whole
index at once, as if every vector still meant the same thing. The old documents are still in
there. Their rankings just quietly get worse, sometimes they stop surfacing at all, sometimes the
wrong document wins instead. No error. No crash. Just a steadily worse answer."
Visual: the corpus split (docs embedded with Model A vs. Model B), a query arriving, and the old
document's rank falling silently, tagged "SPLIT GEOMETRY — SILENTLY."

**B05. Falsifiability case (~1:42–2:08)**
VO: "Now the case that would break this test if it were sloppy: the exact same upgrade, the exact
same old corpus. But this time, before a single query is served, the team re-embeds every old
document with the new model and rebuilds the index from scratch. Same switch, same corpus. The
difference is there's only ever one geometry in the store, so there's nothing left to split."
Visual: the identical corpus and switch event as B04, with every document re-embedded before
serving, tagged "FULLY RE-EMBEDDED — NOTHING TO MIX" instead of a silent split.
*[Stress-tests the framework against a naive "any model swap always silently breaks things"
over-trigger — the only variable changed from B04 is whether a full re-embed happened before
serving.]*

**B06. Real-world note (~2:08–2:32)**
VO: "Here's a real, honest illustration, not a bug report. This project's own retrieval code, rag
dot py, in the Regulatory Q and A backend, rebuilds its entire vector store completely from
scratch, on every single chat request, using a small, local embedding model, with no persisted
index at all. That design sidesteps this entire class of bug by construction, there's never an old
index sitting around to go stale. The real trade off, every request pays the full cost of
re-embedding everything, all over again."
Visual: verbatim-quoted lines from `rag.py`/`config.py`, cited by file and line, framed clearly as
a design choice.

**B07. Scaffolded task (~2:32–2:58)**
VO: "Here's something to check today. If you've ever swapped, upgraded, or changed providers for
an embedding model behind a search or retrieval feature, open the index and ask, does every vector
in it come from the exact same model and version? If even one doesn't, there's no partial fix,
appending new vectors won't save it. The only real fix is a full re-embed, rebuilding the index
from scratch."
Visual: the 3 tests restated as a checklist card.

**B08. Takeaway (~2:58–3:14)**
VO: "An embedding model's geometry isn't portable. Swap it, and the old vectors don't adapt, they
just sit there, quietly wrong. The fix was never incremental. It's a full re-embed, every single
time."
Visual: statement card.

**B09. Sign-off (~3:14–3:16)**
VO: "Explained with Claude Code."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi J.

---

## Production Gate Self-Check (pre-review)

- [x] Framework (B03) shown fully, before any example
- [x] B04's corpus split, the query, and the silent rank drop all visible together, mechanism
      legible without narration alone
- [x] Falsifiability case (B05) uses a genuinely different, full-re-embed case — not a strawman —
      and is visibly distinct from B04's silent-split resolution
- [x] Real-world note (B06) is verbatim-accurate against the actual `rag.py`/`config.py` source
      (confirmed by direct read, not the brief's summary), clearly framed as a design choice, not a
      bug report
- [x] Scaffolded task (B07) is a concrete, runnable action, not a restatement of B03
- [x] Silent title card present; brand/fellow sign-off card present
- [x] Worked example and stress-test case are clearly generic/illustrative; the ONE quantified demo
      (`verification/`) is reported as a single real run, not a general benchmark
- [x] Distinct from nine prior videos in this series, including the earlier general embeddings
      video and the adjacent context-window-limits video

**Runtime:** see `SHOTLIST.md` for the measured, pipeline-used per-beat durations and total.

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-11-19. See `FACTCHECK.md`. Cleared to
generate Kokoro audio and proceed to previz.
