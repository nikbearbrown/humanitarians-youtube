# Confidently Out Of Date

**Track:** educational (STEM / AI) · **Week ending:** 2026-11-27

> A stale index fails quietly. It does not throw and it does not come back
> empty — it returns five confident results from the wrong neighbourhood, with
> a similarity score that looks like a good day.

Two cuts delivered separately: a 16:9 master at 3840×2160 and a 9:16 Short at
2160×3840, both 2:13. **No video files are in this repo** — this is the record
of how they were built and why each claim holds.

## The argument

You build a search index over your documents once. A year passes. New words
appear, and a few old words quietly change which conversation they belong to.
Nobody rebuilds the index.

Two corpora an era apart. Between them, exactly two changes: topic C gains
three terms that did not previously exist, and the term `pipeline` migrates
from infrastructure to data. The stale model learns era 1; the fresh model
learns era 2. **Both index the same documents and answer the same queries.**

| How much of the query is new language | Rebuilt | Stale |
|---|---|---|
| None | 100% | **100%** |
| Half | 100% | **100%** |
| All of it | 100% | **0%** |
| A word that moved | 100% | **0%** |

**Staleness is harmless right up until it isn't.** While any of the query
uses vocabulary the index knows, the surviving terms carry it and recall is
perfect. That is the honest headline, and it is why this failure survives in
production for so long.

**Then there are two completely different failures wearing the same label.**

A word the index *never learned* fails **loudly**: no vector, no result, 100%
of those queries answer nothing, and somebody sees an empty page.

A word that *moved* fails **quietly**. The index has a vector for `pipeline`.
It is confident about it. It is simply pointing at where that word used to
live:

- recall@5: **0%**
- top-1 similarity: **0.892**
- share of results from the wrong topic: **100%**

**So the fix is not a bigger model — it is a clock and a canary.** Re-embed on
a cadence, because text drifts whether or not anyone is watching. And monitor
the out-of-vocabulary rate on live queries, because that is the number that
moves when the language moves. Similarity does not: it goes from 0.961 to
0.892 — a move of 0.069 — while recall goes from everything to nothing.

## Reproduce it

```bash
python staleness_evidence.py
```

Seed `20261127`, **numpy only**. The PPMI co-occurrence embeddings and the SVD
reduction are written out in the script — no gensim, no torch, no downloads.
Seconds to run.

## Beats

| # | Act | Scene | What it does |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | A year-old index, scores still high — is it fine? |
| B01 | BLUF | `BrutalistHesitantWriter` | types **loudly**, deletes it, types **quietly** |
| B02 | SETUP | `StageRail` | Index built → language moves → index does not |
| B03 | BODY | `PairedBars` | Recall by how much of the query is new language |
| B04 | BODY | `CardSet` | The loud failure and the quiet one |
| B05 | LAND | `StageRail` | Clock, canary, and the metric that will not help |
| B06 | HANDOFF | `ClaudeComposerAsk` | Measure OOV rate and drift on your own queries |
| B07 | OUTRO | `HaiTitleOutro` | Title restate · @HumanitariansAI |

## Built for this reel

**Nothing.** `PairedBars` carries its third different argument in three weeks,
`StageRail` and `CardSet` are long-standing library.

## Honesty notes

- **The first experiment produced a null, and it is in the record.** Queries
  drawn uniformly from topic C gave stale recall of 98.5% against 100% fresh —
  no effect. The reason is the finding: most of those queries still contained
  old vocabulary that worked perfectly. The fix was to change the **question**
  — how much of a query has to be new before staleness bites? — not to
  reweight queries until a collapse appeared. The second version is the reel.
- **A line was corrected before compile.** B05 originally said similarity
  "never dropped at all". It drops by 0.069. The narration now states the
  figure and the stage card prints both numbers.
- **Staleness is reported as harmless where it is harmless.** The reel leads
  with 100% recall at half-new vocabulary. A video claiming constant
  catastrophe would be easy to disprove and would deserve to be.
- **This is PPMI + SVD, not a transformer.** The mechanism — OOV terms dropped
  silently, learned neighbourhoods going out of date — applies to any fixed
  embedding, but the numbers are this model's and the reel does not generalise
  them.
- **No rebuild cadence is recommended.** The right interval depends on drift
  rate, and nothing here measures that.
- **Subword tokenisation** softens the OOV failure and does nothing for the
  migrated-word case. Cut for room, noted in `FACTCHECK.md`.

Full ledger in `FACTCHECK.md`, method in `SOURCES.md`, build record in
`FRICTIONAL.md`.
