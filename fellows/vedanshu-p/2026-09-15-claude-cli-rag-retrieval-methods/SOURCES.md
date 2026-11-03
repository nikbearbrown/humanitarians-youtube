# SOURCES — claude-cli-rag-retrieval-methods

*"Watch The Right Answer Get Outvoted." · RAG Foundations, Chapter 6 —
Retrieval Methods: Sparse, Dense, and Hybrid*
*DOUBLE-CHECK LAW record: what the source says, what was measured, and where
the measurement disagreed with the expectation.*

---

## Primary source

| Field | Value |
|---|---|
| Book | *RAG Foundations* — Vedanshu Daxesh Patel |
| Repo | `D:\ai1-cli-main` |
| Chapter | `chapters/06-retrieval-methods.md` |
| Fact-check record | `chapters/06-retrieval-methods.md.verified.json` |

## The demo is real — including the dense side

ACTUAL-CODE LAW requires the CODE beat to show the source that produced the
OUTPUT. The harder requirement for *this* chapter is that dense retrieval be
real: a chapter comparing sparse against dense is worthless if the dense
similarity scores were invented or tuned.

| File | Role |
|---|---|
| `code/corpus.py` | 12 help-desk policy passages + the chapter's two queries |
| `code/encoder.py` | **Real `all-MiniLM-L6-v2` embeddings**, in numpy |
| `code/bm25_search.py` | Cycle 1 — BM25 from scratch |
| `code/hybrid_search.py` | Cycle 2 — dense retrieval + Reciprocal Rank Fusion |

Captured transcripts, verbatim:

| File | Feeds |
|---|---|
| `_run-bm25.txt` | B04 |
| `_run-hybrid.txt` | B07 and B08 |

### How the embeddings are real without `sentence-transformers`

Neither `sentence-transformers` nor `transformers` is installed on this machine,
but the genuine model weights were already in the local HuggingFace cache and
`tokenizers` is available. So `encoder.py`:

1. **Parses `model.safetensors` by hand** — the container is an 8-byte
   little-endian header length, a JSON header, then raw tensor bytes. That is
   the entire format, so no `safetensors` dependency is needed.
2. **Runs the 6-layer BERT forward pass in numpy** — embeddings → 6 ×
   (multi-head self-attention, GELU feed-forward, residual + LayerNorm) →
   mean-pool over the attention mask → L2 normalise. That is exactly what
   sentence-transformers does for `all-MiniLM-L6-v2`.

**Validation.** `python encoder.py` prints a behavioural check, because a wrong
forward pass yields noise and cannot hold this ordering:

```
identical   1.000   (expect 1.000)
paraphrase  0.555   (expect clearly high)
unrelated   0.100   (expect clearly low)
```

Those magnitudes are what real `all-MiniLM-L6-v2` produces. No similarity score
anywhere in this reel is hand-set.

No network access was used and no paid API was called.

### The corpus is written, not generated — and deliberately adversarial

This chapter's claim is about *which kind of match* succeeds, which depends on
the actual words, so the passages are real prose. They are stacked against the
demo in both directions on purpose:

* **TE-330** (travel) and **PD-207** (professional development) both contain the
  word "reimbursement", so query 1 cannot be won by that word alone — only the
  code `TR-114` identifies the right chunk.
* **PD-207** and **CE-118** are both about the company paying for employee
  education, so query 2 has near-miss neighbours *in meaning*, not just in
  wording. CE-118 additionally contains the literal words "company pays".

`GOLD` is `TR-114` for **both** queries, because Chapter 6's example is two
employees asking about the same policy in different words.

## What was measured

**B04 — sparse only (`_run-bm25.txt`):**

| query | top-1 | gold rank | verdict |
|---|---|---|---|
| exact code | TR-114 (3.488) | 1 | **HIT** |
| paraphrase | CE-118 (3.819) | 3 (1.943) | **MISS** |

**B07 — all three methods (`_run-hybrid.txt`):**

| method | exact code | paraphrase | both |
|---|---|---|---|
| sparse (BM25) | HIT | MISS | no |
| dense (all-MiniLM-L6-v2) | HIT | HIT | **YES** |
| hybrid (RRF, k=60) | HIT | **MISS** | no |

**B08 — the fusion arithmetic on the paraphrase:**

```
CE-118: sparse #1 + dense #2  ->  1/61 + 1/62 = 0.03252   (wins)
TR-114: sparse #3 + dense #1  ->  1/63 + 1/61 = 0.03227   (gold, loses)
margin 0.00025
```

## Corrections and editorial decisions applied

These are the important ones, because **the run did not produce the expected
result and the reel was rewritten around what it did produce.**

1. **Hybrid LOST the paraphrase, and the reel leads with that.** The tidy,
   expected story — sparse wins one, dense wins the other, hybrid wins both —
   is not what happened. RRF fuses *ranks*, so CE-118 being sparse's confident
   #1 and dense's #2 narrowly outvoted the correct TR-114 at dense #1 and sparse
   #3. B08 shows the arithmetic rather than asserting the conclusion.
   This independently reproduces the chapter's own refusal to over-claim:
   *"It would be convenient to claim that hybrid retrieval simply always wins.
   The evidence doesn't fully support that."*

2. **Dense did NOT fail the exact-code query, so the reel does not say it did.**
   The chapter warns (via Sciavolino et al., 2021) that dense retrievers can
   smear a specific code into "something about policies". Here dense ranked
   TR-114 first at 0.600. B09's narration states the limit out loud: twelve
   passages is far too small to reproduce an effect documented over rare
   entities at scale. Claiming a failure that did not occur would have been the
   easy way to make the chapter's point.

3. **The corpus was NOT re-tuned to force the expected outcome.** Adding more
   code-like decoys or lengthening the gold passage until dense failed would
   have been engineering the data to match a claim. The measured result stands.

4. **One fusion loss is not a verdict on fusion, and B09 says so.** The reel
   claims only what the run supports: fusion counts ranks rather than reasoning,
   so a confidently wrong retriever can outvote a correct one. It does not
   generalise to "hybrid is bad".

5. **The DPR margin is not quoted on screen.** The chapter cites DPR
   outperforming BM25 by 9–19 points absolute on top-20 accuracy, but explicitly
   warns against over-generalising it, since it was measured on paraphrase-style
   questions. Quoting it beside this reel's 12-passage run would invite exactly
   that over-generalisation.

6. **No vendor or product is named** beyond the model actually used, per the
   chapter's practice of treating named tools as examples of a category.

7. **Nothing version-dated was introduced** — no drifting counts, no model
   version claims beyond the specific checkpoint used.

## Sources the chapter cites, and how the reel uses them

| # | Source | Used in | How |
|---|---|---|---|
| 1 | Spärck Jones (1972) — term specificity / IDF | B03 | The `idf()` function is this idea; narration credits rare terms carrying the weight |
| 2 | Robertson & Zaragoza (2009) — BM25 | B02, B03 | Length normalisation and TF saturation, named as BM25's two corrections over TF-IDF |
| 3 | Manning, Raghavan & Schütze (2008) | background | "Sparse" as a representation over the whole vocabulary |
| 4 | Karpukhin et al. (2020) — DPR | B04, B09 | The paraphrase gap that motivates dense retrieval. Margin deliberately not quoted (see §5) |
| 5 | Sciavolino et al. (2021) — entity-centric questions | B09 | The dense weakness the reel looked for and did NOT reproduce at this scale |
| 6 | **Cormack, Clarke & Buettcher (2009) — RRF** | **B07, B08, cited on screen** | The fusion formula, implemented exactly: sum of 1/(k + rank), k=60, no weight tuning |
| 7 | Kamalloo et al. (2023/2024) — BEIR reproduction | B09 | Hybrid improves "in general" but with named exceptions — the hedge this run lands on |
| 8 | Mandikal & Mooney (2024) — sparse meets dense | B09 | A peer-reviewed case where dense performed comparably or marginally worse than sparse |

## Figures

| Source figure | Treatment |
|---|---|
| `images/retrieval-methods-fig-01` — sparse vector (long, mostly zeros) vs dense embedding (short, populated) | **Not used.** The reel argues about which kind of match wins, not about vector geometry; no beat's claim rests on the shape. Including it would be decoration, so it was omitted rather than padded in |
| `images/retrieval-methods-fig-02` — query → sparse + dense in parallel → fusion | **Rebuilt natively** inside B08 (`RrfMargin`) — and rebuilt at the moment the merge goes *wrong*, using the reel's own measured ranks, rather than as a neutral architecture diagram. REBUILD LAW |

No source image is embedded anywhere.

## Components

New this reel (GATE L: four searches, all genuine misses, built rather than
slated):

| Composition | Beat | 9:16 twin |
|---|---|---|
| `RetrievalTwoQueries` | B01 | `RetrievalTwoQueries916` |
| `RetrievalMatrix` | B07 | `RetrievalMatrix916` |
| `RrfMargin` | B08 | `RrfMargin916` |

Close leads, all read and rejected: `BrandDriftCaseStudy` (props:
`activeColumn` only), `CwcEvalScoring` and `CadencesFig3Artifacts` (props:
`sparkLine` only) — each has its content hardcoded to another reel, so none is
reusable. A hit is a lead, not a verdict; opening the files is what settled it.

All three sit on the existing `EmbedChrome` `FigureFrame` and reuse
`ChunkChrome`'s `useBeatClock`, both built for earlier reels in this series —
so Chapters 3–6 share one chrome and one clock.

Reused unmodified (props only): `ClaudeComposerAsk` (B00, B02, B05, B10),
`ClaudeCodeBeat` (B03, B06), `CliRunOutput` (B04),
`RagExecutiveSummary` (B09), `TitleOutroChannel` (B11).

`TitleOutroChannel`, not `ClaudeTitleOutro`: OUTRO-LOCK.md §Scope restricts the
locked card to `claude-liam-*` slugs; it hardcodes `@NikBearBrown` and never
renders a subline, which would drop the author signature.

## Determinism

BM25 is deterministic. The embeddings are a fixed pretrained checkpoint with no
sampling. Re-running either script reproduces every number in this reel exactly
— including the 0.00025 margin. Every Remotion beat is a pure function of its
frame; no `Math.random` at render.

## Voice

Kokoro `am_onyx`, local, free. **$0.00 spent.**
