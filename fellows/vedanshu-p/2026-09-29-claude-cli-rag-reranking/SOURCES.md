# SOURCES — claude-cli-rag-reranking

*"Reorder Is Not Retrieve." · RAG Foundations, Chapter 9 — Re-ranking and Query
Rewriting (Basics)*
*DOUBLE-CHECK LAW record.*

---

## Primary source

| Field | Value |
|---|---|
| Book | *RAG Foundations* — Vedanshu Daxesh Patel |
| Repo | `D:\ai1-cli-main` |
| Chapter | `chapters/09-reranking-query-rewriting.md` |
| Fact-check record | `chapters/09-reranking-query-rewriting.md.verified.json` |

Folder dated **2026-09-29** per explicit instruction.

## The demo is real — with two components declared as stand-ins

| File | Role | Real? |
|---|---|---|
| `code/encoder.py` | `all-MiniLM-L6-v2` embeddings, numpy BERT forward pass, extended with `encode_tokens` | **real model weights** |
| `code/corpus.py` | 14 help-desk policy documents + the chapter's own question and rewrite | synthetic, written |
| `code/rerank.py` | two-stage cascade, joint re-scoring, timings, the query-independence proof | **real** — with a declared stand-in for stage 2 |
| `code/rewrite.py` | literal vs rewritten query over the same index | **real** — with hand-written rewrites |

Captured transcripts, verbatim: `_run-encoder.txt`, `_run-rerank.txt` (feeds
B04 and B05), `_run-rewrite.txt` (feeds B08).

`encoder.py` is carried from the Chapter 7 reel — same hand-rolled safetensors
parser, same 6-layer numpy forward pass — and re-validated here
(`_run-encoder.txt`: identical 1.000 / paraphrase 0.555 / unrelated 0.100). It
gains one method, `encode_tokens`, which stops the same forward pass one step
before mean pooling.

### Stage 2 is NOT a cross-encoder — the reel's largest declaration

Chapter 9's re-ranking section is specifically about **cross-encoders**: a model
that encodes the query and one document *together* through a network fine-tuned
to emit a relevance score.

**This reel cannot run one.** The machine's HuggingFace cache holds only
bi-encoders (`all-MiniLM-L6-v2`, `all-mpnet-base-v2`,
`multi-qa-mpnet-base-dot-v1`, two paraphrase variants);
`transformers` and `sentence-transformers` are not installed; there is no
network access. Downloading a cross-encoder was not an option.

Rather than fake one, stage 2 uses **late interaction (MaxSim)**: keep the
per-token vectors for the query and each candidate, and for every query token
take its best-matching document token, summed. The query and the document
genuinely do look at each other, token by token — so it is a real joint
interaction, and it is **weaker than the mechanism the chapter describes**:

* a cross-encoder runs full attention *across* the pair, in a network trained on
  relevance labels;
* MaxSim compares two independently-encoded token sequences after the fact.

It is also **not ColBERT**, even though MaxSim is ColBERT's scoring function
(Khattab & Zaharia, 2020). ColBERT *trains* a model to produce token vectors
suited to that comparison; here the function is applied off-label to a model
trained for mean-pooled sentence similarity.

**Where this is declared to the viewer:** B04's caption ("Stage 2 here is late
interaction, not a cross-encoder"), and B09's narration, which names it as one
of three limits on the result.

**Consequence for the finding, stated plainly:** the reel measured that *this*
re-ranker moved nothing. A real cross-encoder might well have moved things. The
reel's claim is about what it ran, not about cross-encoders in general.

### The rewrites are hand-written

Chapter 9 names two methods for producing a rewrite — HyDE (generate a
hypothetical answer, embed that) and Rewrite-Retrieve-Read (a trained model
rewrites the query). **Both require a language model, and this machine has
none.**

So the rewrites in `corpus.REWRITES` were written by hand, in the style
Rewrite-Retrieve-Read describes. The first is the chapter's own, verbatim.

What is therefore measured is real: the effect of a better query on a real
retriever, same index, same encoder, only the query text differing. What is
**not** demonstrated is a model producing the rewrite. The caveat is in the
source file shown on screen in B07, not only in the narration.

## What was measured

**B04 — the cascade and its cost (`_run-rerank.txt`):**

| quantity | measured |
|---|---|
| corpus | 28 chunks from 14 documents |
| stage 1, index built once | 2448 ms |
| stage 2, joint pass | 86 ms per query-document pair |
| stage 2 on a 5-chunk shortlist | 428 ms |
| stage 2 on all 28 chunks | 2398 ms |
| stage 2 on 1,000,000 chunks | 23.8 hours per query |

The million-chunk figure is **arithmetic on the measured per-pair time**, not a
measured run, and is presented as such ("86 ms per pair is … 23.8 hours per
query across a million chunks").

**B05 — the re-ranking result, over six questions:**

| | |
|---|---|
| answer already first before re-ranking | 5/6 |
| answer first after re-ranking | 5/6 |
| promoted | **0** |
| demoted | **0** |

The shortlist shown in B05 is the one question where the answering document
(`OE-300`) was **not in the top-5 at all**, so no re-ranker could reach it. The
re-scorer did reorder that shortlist — the connectors cross — but it reordered
five documents none of which answer the question.

**B08 — literal vs rewritten query, same six questions (`_run-rewrite.txt`):**

| | literal | rewritten |
|---|---|---|
| answer present in top-5 | 5/6 | **6/6** |
| answer ranked first | 5/6 | 5/6 |

One rescue (`OE-300`), zero losses.

## The structural claim, checked rather than asserted

`prove_query_independence` encodes the same document twice, in two batches
alongside two different queries, and compares the vectors elementwise.

**Result: 0.00e+00.** Byte-identical. A bi-encoder's document vector cannot
depend on the query — that is the whole speed trick and the whole blind spot,
and it is the reason a second pass exists at all. This is a check that could
have failed and did not.

## Corrections and editorial decisions applied

1. **A chunking artifact was found and fixed before any narration was written.**
   The first splitter cut on blank lines only, which made every document's
   *title* its own 20-to-50 character chunk. Those title chunks then competed
   with real passages, and "Retired Benefit Plans" — a heading containing no
   policy at all — outranked the paragraph that answers the question. Titles are
   now attached to the passage beneath them (structure-aware chunking, the
   Chapter 4 lesson arriving one chapter later). Logged rather than silently
   corrected because it changed the numbers.

2. **The corpus was expanded because the first test was too easy, not because
   the result was unwelcome.** Six well-separated documents gave every question
   exactly one plausible home, so the first pass could not realistically err.
   Eight confusable neighbours were added — documents that each talk about
   enrolment, coverage, eligibility or "your plan" without being the one you
   want. The re-ranking result did not change (0 promoted, 0 demoted both
   before and after the expansion); what changed is that one question's answer
   fell out of the top-5, which is what made the ceiling visible.

3. **The null result is reported as the finding.** Re-ranking moved nothing on
   this corpus. The reel does not go looking for a corpus where it would, and
   does not imply the chapter is wrong — it reports what this run showed and
   names the three reasons the test is limited.

4. **No accuracy or benchmark number is claimed.** Six questions, one corpus.

5. **The chapter's cited improvements belong to their authors.** Nogueira &
   Cho's 27% relative gain and Reimers & Gurevych's 65-hours-to-5-seconds
   speedup are the chapter's citations of other people's measurements. The 27%
   figure does not appear on screen anywhere in this reel. The speedup is
   referenced only in B04's citation line as the origin of the bi-encoder
   framing, never as something this reel measured.

6. **Nothing version-dated.** No model version claims beyond the specific
   checkpoint used; no drifting counts.

## Sources the chapter cites, and how the reel uses them

| # | Source | Used in | How |
|---|---|---|---|
| 1 | Gao, Y. et al. (2023/2024) — *RAG for LLMs: A Survey* | B05, B08 citations | The pre-retrieval / post-retrieval framing that places both refinements inside the retrieve stage |
| 2 | Reimers & Gurevych (2019) — *Sentence-BERT* | B04 citation | Origin of the bi-encoder architecture whose cost profile B04 measures |
| 3 | Nogueira & Cho (2019) — *Passage Re-ranking with BERT* | background | The cross-encoder re-ranking result. Deliberately NOT shown on screen — this reel did not run a cross-encoder and will not borrow its number |
| 4 | Ma, X. et al. (2023) — *Query Rewriting for/in RAG* | B08 citation | The rewrite-then-retrieve shape the hand-written rewrites follow |
| 5 | Gao, L. et al. (2022/2023) — *HyDE* | background | Named in the narration as a method requiring an LLM; not run |
| 6 | Manning, Raghavan & Schütze (2008) | background | Relevance feedback as the pre-LLM ancestor of rewriting. Not on screen |
| 7 | Khattab & Zaharia (2020) — *ColBERT* | `rerank.py` docstring | Origin of MaxSim, cited where the stand-in is declared |

Khattab & Zaharia is **not** in the chapter's reference list — it is cited here
because this reel's stand-in borrows its scoring function, and using a technique
without naming its source would be the wrong kind of quiet.

## Figures

| Source figure | Treatment |
|---|---|
| `images/reranking-query-rewriting-fig-01.png` — two-stage diagram, fast bi-encoder shortlist feeding a slower cross-encoder re-ranker | **Rebuilt natively** as B04 (`TwoStageCascade`), carrying this reel's own measured timings instead of illustrative labels. REBUILD LAW |
| `images/reranking-query-rewriting-fig-02.png` — before/after of a vague question rewritten | **Rebuilt natively** across B06 (the rewrite itself, typed into the composer) and B08 (`RetrievalMatrix` — the measured outcome of both phrasings). The source figure asserts the rewrite is better; the rebuild measures it |

No source image is embedded anywhere.

## Components

New this reel (GATE L: six searches, both genuine misses):

| Composition | Beat | 9:16 twin |
|---|---|---|
| `TwoStageCascade` | B04 | `TwoStageCascade916` |
| `ShortlistReorder` | B05 | `ShortlistReorder916` |

**Reused after inspection — a GATE L hit that survived:** `RetrievalMatrix`
(B08), built for the Chapter 6 reel. Its contract is rows × columns of HIT/MISS
cells with exactly one accent and a derived all-hits column, which is precisely
the shape of the literal-vs-rewritten sweep. The derived column is suppressed
(`bothLabel: ""`) because the story is the single flipped cell. Props only; the
component is unmodified.

Rejected leads, opened and read: `RetrievalTwoQueries` (9.0) — Chapter 6's
two-phrasings premise, props hardcoded to that argument; `RrfMargin` (5.5) —
RRF arithmetic, not a shortlist reorder; `CwcEvalScoring` (13.0) and
`SleeperAgentsResult` (4.5) — both expose only `sparkLine`, with content fixed
to their own reels.

Both new components sit on the existing `EmbedChrome` `FigureFrame` and reuse
`ChunkChrome`'s `useBeatClock`, so Chapters 3–9 share one chrome and one clock.

Reused unmodified (props only): `ClaudeComposerAsk` (B00, B02, B06, B10),
`ClaudeCodeBeat` (B03, B07), `RagExecutiveSummary` (B01, B09),
`TitleOutroChannel` (B11).

`TitleOutroChannel`, not `ClaudeTitleOutro`: OUTRO-LOCK.md §Scope restricts the
locked card to `claude-liam-*` slugs; it hardcodes `@NikBearBrown` and never
renders a subline, which would drop the author signature.

## VOX LAW — zero pantry stills, and that is the correct number

No photographic stills, and none were fetched. VOX LAW holds that a still is
evidence, never texture. This chapter's evidence is architecture, code, timings
and ranks — there is no beat whose evidence is an image, so a pantry still could
only be decoration. Both source figures were rebuilt natively, so no image file
enters the render at all.

## Determinism

The encoder is a fixed pretrained checkpoint with no sampling; retrieval,
re-scoring and rewriting are deterministic by construction. Re-running either
script reproduces every rank in this reel exactly. **Timings are the one
exception** — they vary by a few percent between runs, which is why the reel
quotes them as measured figures rather than constants, and why the shipped
numbers come from the captured transcripts rather than from memory.

Every Remotion beat is a pure function of its frame; no `Math.random` at render.

## Voice

Kokoro `am_onyx`, local, free. **$0.00 spent.** No paid API, no network call.
