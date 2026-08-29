# SOURCES — Watch Embeddings Beat The Wrong Words.

## Book source

- Book: *RAG Foundations* (author: Vedanshu Daxesh Patel)
- Chapter: `chapters/03-representing-text-embeddings.md` — "Representing Text:
  Embeddings"
- Same source as the sibling ai-explainer reel `2026-08-26-claude-rag-embeddings`;
  full citation list (Mikolov et al. 2013 word2vec, Devlin et al. 2019 BERT,
  Reimers & Gurevych 2019 Sentence-BERT, Manning/Raghavan/Schütze 2008 vector
  space model + cosine similarity) carries over unchanged — see that reel's
  `SOURCES.md` for the complete bibliography. This reel makes no new citation
  claims; it demonstrates the chapter's own worked example as runnable code
  instead of narrating it.
- Directly targets the chapter's own worked example (`## Worked example: two
  phrasings, one meaning — and a false match`, Figure 02): "how much vacation
  do I get" / "what's the PTO policy" should land close together; "how do I
  request time off" / "how do I request a new laptop" should land farther
  apart *despite sharing the phrase "how do I request."*

## Code (THE ACTUAL-CODE LAW — real, run, not fabricated)

- `code/naive_similarity.py` — six hardcoded FAQ passages (three HR: vacation/
  PTO, sick leave, parental leave; three IT: laptop request, password reset,
  software install), one query ("How do I request time off?"), ranked by
  literal word overlap (Jaccard-style set intersection/union). Pure standard
  library, no dependencies. Run for real via `python code/naive_similarity.py`.
  Verbatim captured stdout:
  ```
  query: 'How do I request time off?'

  ranked by word overlap:
    0.148  IT-01
    0.030  HR-01
    0.000  IT-03
    0.000  IT-02
    0.000  HR-03
    0.000  HR-02

  top match: IT-01 (score 0.148)
  ```
  Trimmed subset (top 2 rows + verdict) used in beat B04.
- `code/embedding_similarity.py` — same six passages, same query. The only
  change: passages and query are encoded with `sentence-transformers`'
  `all-MiniLM-L6-v2` (a real, small, local Sentence-BERT model — the exact
  family of model cited in the chapter via Reimers & Gurevych 2019), ranked
  by cosine similarity. Run for real via `python code/embedding_similarity.py`.
  Verbatim captured stdout:
  ```
  query: 'How do I request time off?'

  ranked by cosine similarity (all-MiniLM-L6-v2 embeddings):
    0.334  HR-01
    0.277  HR-03
    0.229  IT-01
    0.154  HR-02
    0.113  IT-02
    0.093  IT-03

  top match: HR-01 (score 0.334)
  ```
  Trimmed subset (top 3 rows + verdict) used in beat B07.
- `sentence-transformers` + `all-MiniLM-L6-v2` are free and require no API
  key — the model weights (~90MB) download once from Hugging Face's public
  model hub and run entirely locally afterward. Consistent with Fellow-tier
  "no money, ever."
- **Build-environment note**: `sentence-transformers` was installed and run
  inside an isolated Python venv, not the toolkit's shared system Python.
  Installing it system-wide pulled in `numpy<2`, which broke `kokoro_onnx`'s
  own `numpy>=2.0.2` requirement (confirmed by a failed import) until
  reverted. This is disclosed here so nobody re-runs `pip install
  sentence-transformers` directly into the toolkit's environment and breaks
  audio generation for every other reel in this book.
- IT-01's wrong-answer ranking in `naive_similarity.py` was predicted before
  running the script (it literally shares the phrase "how do i request" with
  the query, once function words are ignored it's the only exact multi-word
  match), then confirmed by actually executing it — not a cherry-picked run.
  Both scripts were run more than once during development with identical
  results (co-occurrence counts are deterministic).

## An honest dead end (disclosed, per DOUBLE-CHECK LAW)

- Before landing on the FAQ-retrieval framing above, two other approaches
  were tried and abandoned because they didn't actually work:
  1. A hand-rolled co-occurrence ("distributional") word-vector model built
     from a small 12-sentence hardcoded corpus, with and without stopword
     filtering and IDF weighting. It produced the WRONG ordering (the
     intended-close pair scored lower than the intended-far pair) in every
     variant tried — a small hardcoded corpus is too sparse for a shared
     pivot word like "request" not to dominate the sentence vectors. Not
     used; would have been dishonest to present as "the fix."
  2. Literally reproducing the chapter's own four short quoted phrases
     ("how much vacation do I get" / "what's the PTO policy" / "how do I
     request time off" / "how do I request a new laptop") as an isolated
     pairwise cosine-similarity comparison, using four different real
     Sentence-BERT models (`all-MiniLM-L6-v2`, `paraphrase-MiniLM-L6-v2`,
     `all-mpnet-base-v2`, `paraphrase-mpnet-base-v2`). None of the four
     cleanly reproduced the chapter's intended separation on those exact
     bare fragments — short, context-free questions are genuinely difficult
     for general-purpose sentence embeddings, a real and interesting
     limitation, but not the demo this reel needed. The chapter's own
     Figure 02 caption calls this "a 2-dimensional embedding-space *sketch*"
     — a teaching simplification, not a claim that any specific real model
     reproduces it on contact.
- What DOES reproduce honestly and robustly is the retrieval framing this
  reel actually uses: a realistic small set of FAQ passages plus one
  question, where naive word-overlap is fooled by a literally shared phrase
  and returns the wrong passage, while `all-MiniLM-L6-v2` embeddings
  correctly rank the semantically right passage first. This is truer to the
  chapter's own larger point anyway — retrieval means picking the right
  passage out of several candidates, not just scoring one isolated pair.

## Invented specifics (disclosed, per DOUBLE-CHECK LAW)

- The six FAQ passages (leave policy numbers, sick-day counts, parental-leave
  weeks, IT turnaround times) are an original toy example built for this
  reel — the chapter itself gives no HR/IT policy figures. Chosen to be
  plausible and internally consistent, not to match any real company policy.
- No model version number, parameter count, or training-corpus size is
  spoken anywhere in this reel beyond what's already sourced in the sibling
  ai-explainer reel's SOURCES.md (word2vec's 1.6B-word corpus, BERT vs.
  Sentence-BERT's ~65 hours / ~5 seconds figure).

## What this reel does NOT claim

- It does not claim `all-MiniLM-L6-v2` (or any specific embedding model)
  perfectly solves retrieval in general — only that, on this one real,
  reproducible example, comparing meaning outperforms counting words. The
  chapter's own next sections (and this book's later chapters) are where
  the limits of retrieval get their own treatment.
- It does not re-litigate word2vec's vector-arithmetic example (king − man +
  woman ≈ queen) or the BERT/Sentence-BERT timing figures — those are the
  sibling ai-explainer reel's territory; this reel is the worked-example
  half of the chapter, made runnable.
