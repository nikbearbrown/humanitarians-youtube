# SOURCES — claude-rag-no-default

*"There Is No Default." · RAG Foundations, Chapters 4–6 — the summary*
*DOUBLE-CHECK LAW record.*

---

## What this reel is

A **summary explainer** over three reels already built and QC'd, following the
convention set by the Chapters 1–3 summary (`2026-09-01-claude-summary`).

| Source reel | Chapter | Skill |
|---|---|---|
| `2026-09-08-claude-rag-chunking` | 4 — Chunking Documents | ai-explainer |
| `2026-09-08-claude-cli-rag-vector-databases` | 5 — Vector Databases & ANN | cli-explainer |
| `2026-09-08-claude-cli-rag-retrieval-methods` | 6 — Retrieval Methods | cli-explainer |

## The governing rule

Inherited verbatim from the Chapters 1–3 summary:

> Every on-screen figure and number is carried over from the source reels' own
> beat sheets; **nothing new is claimed.**

This reel therefore **introduces no new evidence, runs no new code, and builds
no new component.** It is an argument *about* three existing results, assembled
from the artifacts that already carry them. Every number was measured, verified
and frame-QC'd in its source reel; re-deriving any of it here could only
introduce drift.

## The act beats — carried over

| Beat | Component | Carried from | Props |
|---|---|---|---|
| B02 | `ChunkSizeTradeoff` | Ch4 reel, B03 | verbatim |
| B03 | `AnnRecallDial` | Ch5 reel, B08 | verbatim except caption self-reference |
| B04 | `RetrievalMatrix` | Ch6 reel, B07 | verbatim except caption self-reference |
| B05 | `RrfMargin` | Ch6 reel, B08 | verbatim |

**The only prop edits made, and why.** Two captions read *"measured by this
reel's own ann_search.py / hybrid_search.py"*. In a derived summary, "this reel"
points at the wrong artifact — this reel has no `code/` directory and ran
nothing. They now read *"measured by the Chapter 5 build's ann_search.py"* and
*"the Chapter 6 build's hybrid_search.py"*. **No number, label, axis, rank or
score was altered.**

## Numbers on screen, and where each was measured

| Figure | Value | Measured in |
|---|---|---|
| Chunk size has no correct setting | axis with both ends failing, middle unmarked | Ch4 reel (source: the chapter's own refusal to name a size) |
| ANN recall dial | 0.3% → 0.330 · 1.3% → 0.600 · 5.0% → 0.875 · 10.2% → 0.960 | Ch5 reel, `_run-ann.txt` |
| Retrieval matrix | sparse HIT/MISS · dense HIT/HIT · hybrid HIT/MISS | Ch6 reel, `_run-hybrid.txt` |
| RRF margin | 0.03252 vs 0.03227, 0.00025 apart | Ch6 reel, `_run-hybrid.txt` |

The verdict card (BVDT) restates only these, and the B00 output lines restate
only the three chapters' own conclusions.

## The through-line, and why it is defensible

The reel's claim is that Chapters 4, 5 and 6 share a shape: each looks like it
should have a best answer, and in each case the honest answer is a **setting you
measure**, not a default you install.

That is not a new assertion layered on top of the sources — it is what each
source already concluded:

1. **Ch4** — the chapter explicitly declines to name a correct chunk size
   ("no universally correct setting"), and the reel's axis has a deliberately
   unmarked middle to encode that.
2. **Ch5** — the recall/speed tradeoff is literally parameterised by `nprobe`,
   and the Ch5 reel measured four settings of it.
3. **Ch6** — the "safe default" (hybrid fusion) is the method that **missed**,
   by 0.00025. That result was measured, not predicted, and the Ch6 reel leads
   with it.

Point 3 is what makes the title honest rather than glib: the reel is not saying
"defaults are bad" as a slogan, it is pointing at a case where the obvious
default lost, with the arithmetic on screen.

## What this reel deliberately does NOT claim

- It does not generalise the hybrid loss into "hybrid retrieval is bad". BVDT
  says "this run was one of the times it did not [help]" — matching the Ch6
  reel's own hedge and the chapter's.
- It does not repeat the Ch6 finding that dense retrieval beat the exact-code
  query, because that result is scale-limited (12 passages) and the Ch6 reel
  already states that limit. Compressing it into a summary line would strip the
  caveat.
- It introduces no figure from a chapter that was not already rebuilt in a
  source reel.

## Components

**Zero new components.** GATE L required no search: every act beat reuses a
composition built and registered for its source reel, and every bookend reuses
the standard chassis.

Reused: `ClaudeComposerAsk` (B00, BHTF), `BrutalistHesitantWriter` (B01),
`ChunkSizeTradeoff` (B02), `AnnRecallDial` (B03), `RetrievalMatrix` (B04),
`RrfMargin` (B05), `ClaudeVerdictArtifact` (BVDT), `TitleOutroChannel` (BOUT).

`TitleOutroChannel`, not `ClaudeTitleOutro`: OUTRO-LOCK.md §Scope restricts the
locked card to `claude-liam-*` slugs; it hardcodes `@NikBearBrown` and never
renders a subline, which would drop the author signature.

## Determinism

Every beat is a pure function of its frame. `BrutalistHesitantWriter`'s seed is
pinned (`claude-rag-no-default-b01`). The four act beats carry fixed measured
props. No `Math.random` at render.

## Voice

Kokoro `am_onyx`, local, free. **$0.00 spent.** No paid API, no network call,
no code executed.
