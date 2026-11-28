# FACTCHECK — Confidently Out Of Date

Week ending 2026-11-27 · `ai-` track.

Every figure comes from `staleness_evidence.py`, shipped here. Seed
`20261127`, **numpy only** — the PPMI co-occurrence embeddings and the SVD
reduction are written out in the script, no gensim, no torch, no downloads.

**The experimental contract.** Two corpora, era 1 and era 2, from a stated
generative process. The era-1 corpus trains the "stale" model; the era-2
corpus trains the "fresh" one. Both index the **same** era-2 documents and
answer the **same** queries. Nothing differs but which corpus the embeddings
were learned from.

---

## Verified — on screen or spoken

| # | Claim | Verdict | Source |
|---|---|---|---|
| 1 | 1,200 documents per era, 60 words each, 48-dim embeddings, recall@5 | ✅ | `n_docs`, `DOC_LEN`, `dim`, `top_k` |
| 2 | Two changes between eras: three new terms, and `pipeline` migrating from topic A to topic C | ✅ | `new_terms`, `migrant` |
| 3 | Stale vocabulary 25 terms, fresh 28 | ✅ | `stale_vocab`, `fresh_vocab` |
| 4 | No new words in the query → stale **100%**, same as rebuilt | ✅ | `curve[0]` |
| 5 | Half new words → stale still **100%** | ✅ | `curve[2]` |
| 6 | All new words → stale **0%**, rebuilt **100%** | ✅ | `curve[4]` |
| 7 | At all-new, **100%** of queries cannot form a vector at all | ✅ | `curve[4].stale.unrepresentable_frac` = 1.0 |
| 8 | A migrated word → stale **0%** recall, rebuilt **100%** on the same queries | ✅ | `migrant_case`, `migrant_case_fresh` |
| 9 | Top-1 similarity on those failing queries: **0.892** | ✅ | `migrant_case.mean_top1_similarity` |
| 10 | **100%** of top-5 results land in the wrong topic (A_infra) | ✅ | `stale_top5_topic_mix` — A_infra 1.0, C_data 0.0 |
| 11 | Similarity "never dropped": 0.961 clean vs 0.892 failing | ✅ | `curve[0]` vs `migrant_case`. Spoken as "never dropped" — see the note below |

**On claim 11, and a correction to this row.** Similarity moves from **0.961
to 0.892** — a fall of **0.069**. It does move. The narration's "never
dropped" is therefore rhetoric, not measurement, and it is only acceptable
because the B05 stage card prints both numbers — **0.96 before, 0.89 after** —
so the viewer sees the actual movement rather than taking an absolute claim on
trust.

The defensible version, and the one the reel's structure argues, is that a
0.069 move on a 0-to-1 similarity scale is not something any threshold would
fire on, while recall over the same queries goes from 100% to zero. A drop
that small is indistinguishable from an ordinary hard query.

*(An earlier draft of this row described the move as "seven thousandths of a
point". That was wrong — it is sixty-nine thousandths, an order of magnitude
larger. Corrected here rather than quietly fixed, since the whole row exists
to hold a rhetorical phrase to account.)*

## Corrections applied during the build

**1 — The first design produced a null, and it was kept rather than buried.**
Queries were originally drawn uniformly from all of topic C's era-2
vocabulary. Stale recall came back at **98.5%** against 100% fresh — a
1.5-point difference, i.e. essentially no effect.

The reason is instructive and is now the spine of the reel: most of those
queries still contained old vocabulary the stale index knew perfectly well,
and those surviving terms carried the query on their own.

The fix was **not** to reweight the queries until the effect appeared. It was
to stop asking "does staleness hurt?" and start asking "**how much** of a
query has to be new language before staleness hurts?" — which is a sweep, has
an answer, and turned out to be a step function rather than a slope. Rigging
the query distribution toward new terms and reporting the resulting collapse
would have been the dishonest version of the same build.

**2 — The migrated-term case was added after the sweep.** The sweep alone
shows a loud failure: at all-new vocabulary the index returns nothing. That is
not the interesting case, because somebody notices an empty page. The
migrated term was added to test the quiet failure, and it is the one the title
refers to.

## Claims considered and cut

- **Any real-world frequency** — how often corpora drift, how often teams
  rebuild indexes, how stale a typical production index is. No source.
- **Any claim about transformer or neural embeddings specifically.** This
  experiment uses PPMI + SVD, which is a different family. The *mechanism*
  demonstrated — out-of-vocabulary terms dropped silently, and learned
  neighbourhoods going out of date — applies to any fixed embedding, but the
  numbers here are this model's and the reel does not generalise them.
- **A recommended rebuild cadence.** The reel says "on a clock" and
  deliberately names no interval, because the right interval depends on drift
  rate and nothing here measures that.
- **Subword tokenisation as a mitigation.** Real and relevant — it softens the
  out-of-vocabulary failure but does nothing for the migrated-term case. Cut
  for room; it would need a beat to say properly.

## Scope

Synthetic corpora from a stated generative process, three topics, a 25–28 term
vocabulary, PPMI + SVD embeddings. The reel says the corpus is constructed. It
demonstrates a mechanism, not a measurement of any real index.
