# SOURCES — Confidently Out Of Date

Week ending 2026-11-27 · `ai-` track.

## Primary evidence — generated here

| File | What it establishes |
|---|---|
| `staleness_evidence.py` | The whole argument: two corpora an era apart, two embedding models, one index, and what a stale model does to recall and to confidence |
| `staleness_results.json` | Machine-readable output; the beat sheet is populated **from this file**, never retyped |

**Seed `20261127`**, `numpy.random.default_rng`, no wall clock.

**No gensim, no torch, no downloads.** The embeddings are PPMI over
within-document co-occurrence, reduced by SVD — about thirty lines, fully
inspectable, and reproducible on any machine with numpy. That matters here for
the same reason it did on the previous reel: when the whole claim rests on a
model, a model you can read is worth more than one you import.

### Reproduce

```bash
python staleness_evidence.py
```

Seconds to run.

## Method, stated plainly

- **Corpora.** Three topics. Documents are 60 words, 80% drawn from a topic's
  own terms and 20% shared boilerplate. Era 2 differs from era 1 in exactly
  two ways: topic C gains three terms that did not previously exist, and the
  term `pipeline` migrates from topic A to topic C.
- **Models.** `stale` is trained on era-1 documents only. `fresh` is trained
  on era-2 documents. Both then index the **same** era-2 documents.
- **Document and query vectors** are the mean of the word vectors the model
  knows. Terms the model has never seen are **dropped silently**, which is
  what production pipelines do.
- **Queries** are six words drawn from topic C's era-2 vocabulary, with the
  proportion of *new* terms swept from 0% to 100%.
- **Metrics.** recall@5 on topic-C documents, mean top-1 cosine similarity,
  and the fraction of queries for which no vector can be formed at all.

## Prior work this is consistent with

The reel re-derives the mechanism rather than citing it; no figure comes from
any of these.

- **Levy & Goldberg (2014)**, *Neural Word Embedding as Implicit Matrix
  Factorization*, NeurIPS — the result that makes PPMI + SVD a reasonable
  stand-in for a learned embedding here.
- **Hamilton, Leskovec & Jurafsky (2016)**, *Diachronic Word Embeddings
  Reveal Statistical Laws of Semantic Change*, ACL — semantic drift as a
  measurable phenomenon over time.

## Not used

No screenshots, no lifted figures, no benchmark numbers, no claim about how
often real corpora drift or how stale a typical production index is — see
`FACTCHECK.md`, "Claims considered and cut".
