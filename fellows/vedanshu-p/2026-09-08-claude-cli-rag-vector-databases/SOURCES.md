# SOURCES — claude-cli-rag-vector-databases

*"Watch Exact Search Hit A Wall." · RAG Foundations, Chapter 5 — Vector
Databases and Approximate Nearest-Neighbor Search*
*DOUBLE-CHECK LAW record: what the source says, what the reel says, what was
measured, and every correction applied in between.*

---

## Primary source

| Field | Value |
|---|---|
| Book | *RAG Foundations* — Vedanshu Daxesh Patel |
| Repo | `D:\ai1-cli-main` |
| Chapter | `chapters/05-vector-databases-ann.md` |
| Fact-check record | `chapters/05-vector-databases-ann.md.verified.json` |

## The demo is real, and that is the point

ACTUAL-CODE LAW requires the CODE beat to show the source that actually produced
the OUTPUT. This reel goes the whole way: `code/` holds three runnable scripts,
they were executed on this machine, and **every number in every output beat is
their real stdout**. Nothing on screen is illustrative.

| File | Role |
|---|---|
| `code/corpus.py` | The synthetic embedding collection both benchmarks search |
| `code/brute_force_search.py` | Cycle 1 — exact search, timed at three collection sizes |
| `code/ann_search.py` | Cycle 2 — an inverted-file (IVF) index, with recall measured |

Captured transcripts, verbatim:

| File | Feeds |
|---|---|
| `_run-brute.txt` | B04 (`CliRunOutput` lines) |
| `_run-ann.txt` | B07 (scaling series) and B08 (the recall dial) |

Re-run either script and the numbers reproduce — the seed is fixed (`SEED = 5`
in `corpus.py`). Wall-clock milliseconds are machine-specific; the comparison
counts and recall figures are not.

### What was measured

**B04 — brute force (`_run-brute.txt`):**

```
  vectors   ms/query   compared/query
    1,000       0.08            1,000
   10,000       1.16           10,000
  100,000      10.87          100,000
```

**B07 — how cost grows (`_run-ann.txt`, table 1):** exact comparisons per query
1,000 → 10,000 → 100,000; IVF comparisons 121 → 396 → 1,271. A hundredfold
increase in data costs the index about **ten and a half times** the comparisons,
because cells are sized ~√n and a fixed `nprobe` is probed.

**B08 — the dial (`_run-ann.txt`, table 2), 100,000 vectors, 316 cells:**

| nprobe | compared | of total | recall@10 |
|---|---|---|---|
| 1 | 315 | 0.3% | 0.330 |
| 4 | 1,261 | 1.3% | 0.600 |
| 16 | 5,042 | 5.0% | 0.875 |
| 32 | 10,180 | 10.2% | 0.960 |

## The synthetic corpus — a modelling decision worth declaring

The vectors are generated, not embedded, because the chapter's claim is about how
search **cost** behaves as a collection grows, which depends on the count and the
geometry rather than on what any text said.

**The generator is not uniform noise, and it took four attempts to get right.**
This is logged because a reader who did not know it would reasonably suspect the
data of being tuned to flatter the method:

1. **Uniform Gaussian vectors in 384 dimensions → IVF recall 0.015–0.465.**
   Correct behaviour, useless demo: uniformly random high-dimensional points sit
   at roughly equal distances from one another, so there is no neighbourhood
   structure for any index to exploit. That run measures the curse of
   dimensionality, not the method, and would have badly misrepresented ANN.
2. **Adding cluster centres with per-coordinate noise σ=0.4 → no better.** In 384
   dimensions the noise norm is σ·√384 ≈ 7.8 against a unit-norm centre, so the
   noise swamped the structure and the data was still effectively uniform. (A
   second bug was caught here too: queries were being drawn from a *fresh* set of
   random centres, so they were not near the corpus at all.)
3. **Correctly scaled noise (σ ≈ α/√D) → recall 1.000 at every setting.** Now the
   clusters were so clean that probing one cell already found everything — a
   tradeoff curve with no tradeoff in it.
4. **Low intrinsic dimensionality → the curve in B08.** Real sentence embeddings
   have a high *ambient* dimension but a much lower *intrinsic* one: they lie near
   a low-dimensional manifold, because the texts they encode vary along far fewer
   degrees of freedom than the model has output units. `corpus.py` samples a
   latent vector in 16 dimensions, maps it into 384 with a fixed random linear
   map, and adds small ambient jitter. That has genuine local neighbourhood
   structure — the property an index exploits — and yields the recall curve above.

The reasoning is documented in `corpus.py` itself, not just here, so the
assumption travels with the code.

## Sources the chapter cites, and how the reel uses them

| # | Source | Used in | How |
|---|---|---|---|
| 1 | Malkov & Yashunin (2018), *HNSW* — arXiv 1603.09320 | B01, B07 citation, B09 | Cited for the linear cost of exact search and for HNSW as the chapter's walkthrough index. The reel does **not** claim to implement HNSW |
| 2 | Aumüller, Bernhardsson & Faithfull (2018/2020), *ANN-Benchmarks* — arXiv 1807.05614 | **B08, cited on screen** | The recall-vs-throughput curve is exactly what this benchmark plots; B08 is that shape, measured locally |
| 3 | Indyk & Motwani (1998) | B01 (background) | Classical exact indexes degrade toward linear scan past a few dozen dimensions. Not named on screen |
| 4 | Jégou, Douze & Schmid (2011), *Product Quantization* | — | Named in the chapter as another ANN family; not demonstrated here |
| 5 | Johnson, Douze & Jégou (2019/2021), *Billion-Scale Similarity Search* | — | Same |
| 6 | Pan, Wang & Li (2023/2024), *Survey of Vector DBMS* | B09 (background) | What a vector database is as a category. No vendor named, per the chapter |

## Corrections and editorial decisions applied

1. **The reel builds IVF; the chapter walks through HNSW. This is stated out
   loud.** B09's narration names it: *"the chapter walks through HNSW, a graph
   index. We built an inverted file. Different mechanism, same bargain."* The
   chapter itself licenses this — it presents HNSW as "a single illustrative
   example" and notes that "a different index family would support the same
   reasoning," and it lists inverted-file indexes as a real, distinct family. But
   the viewer is told, not left to assume.

2. **Figure 02 was deliberately NOT rebuilt.** The chapter's second figure is the
   multi-layer HNSW graph. Drawing that hierarchy in a reel whose code builds
   flat IVF cells would imply the demo does something it does not. Omitting it is
   the honest choice; the SUMMARY beat carries the distinction in words instead.

3. **Wall-clock is reported but the argument rests on comparison counts.** B07
   plots *comparisons per query*, not milliseconds, because comparison counts are
   machine-independent and are what the chapter's cost argument is actually about.
   The measured milliseconds are shown in B04 where the point is the felt cost of
   exact search.

4. **No claim that the index is uniformly faster.** At high `nprobe` this
   pure-numpy IVF is not faster in wall-clock than a single BLAS matmul, because
   fancy-indexing copies memory that the dense path never touches. The reel
   therefore never says "the index is always faster"; it says the *work* stops
   tracking the collection, which is what was measured and what the chapter
   claims.

5. **The recall cost is shown before the win is celebrated.** B08 opens on the
   cheapest setting recovering only 33% of true neighbours. An explainer that
   showed only the 96% row would be selling the method rather than teaching it.

6. **No vendor named**, per the chapter's explicit note that the concept matters
   and not which company implemented it.

7. **Nothing version-dated introduced** — no model versions, no drifting counts.

## Components

New this reel (GATE L: four searches, both genuine misses, built rather than
slated):

| Composition | Beat | 9:16 twin |
|---|---|---|
| `AnnScalingChart` | B07 | `AnnScalingChart916` |
| `AnnRecallDial` | B08 | `AnnRecallDial916` |

The closest library lead was `BarChart` (score 9.0). **Rejected on inspection:**
it imports `../tokens/vox` and accents in TEAL, which would break this reel's
Claude fidelity palette and its one-terracotta-accent law. A hit is a lead, not a
verdict — reading the file is what settled it.

Both new components sit on the existing `EmbedChrome` `FigureFrame` and reuse
`ChunkChrome`'s `useBeatClock`, both built for earlier reels in this series — so
Chapters 3, 4 and 5 share one chrome and one clock.

Reused unmodified (props only): `ClaudeComposerAsk` (B00, B02, B05, B10),
`RagExecutiveSummary` (B01, B09), `ClaudeCodeBeat` (B03, B06),
`CliRunOutput` (B04), `TitleOutroChannel` (B11).

`TitleOutroChannel`, not `ClaudeTitleOutro`: OUTRO-LOCK.md §Scope restricts the
locked card to `claude-liam-*` slugs; it hardcodes `@NikBearBrown` and never
renders a subline, which would drop the author signature.

## Determinism

`corpus.py` fixes `SEED = 5`, so both scripts build an identical collection and
re-running reproduces the tables. Every Remotion beat is a pure function of its
frame. No `Math.random` at render.

## Voice

Kokoro `am_onyx`, local, free. **$0.00 spent.** No paid API was called.
