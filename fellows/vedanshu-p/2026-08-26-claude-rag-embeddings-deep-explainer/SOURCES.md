# SOURCES — The Geometry Of Meaning.

## Book source

- Book: *RAG Foundations* (author: Vedanshu Daxesh Patel)
- Chapter: `chapters/03-representing-text-embeddings.md` — "Chapter 3 — Representing
  Text: Embeddings and Semantic Similarity"
- Same source as the sibling ai-explainer reel (`2026-08-26-claude-rag-embeddings`) and
  cli-explainer reel (`2026-08-26-claude-cli-rag-embeddings`). This deep-explainer cut
  makes no new factual claims beyond those two — it re-presents the same five citations
  across a 6-act documentary structure, with its own set of Manim/Remotion/VOX treatments.

## Citations (identical bibliography to the sibling ai-explainer reel's SOURCES.md)

- Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient Estimation of
  Word Representations in Vector Space. https://arxiv.org/abs/1301.3781 — the
  1.6-billion-word training corpus and "learned, not assigned" framing (B02–B05).
- Mikolov, T., Yih, W., & Zweig, G. (2013). Linguistic Regularities in
  Continuous Space Word Representations. *NAACL-HLT 2013*, pp. 746–751.
  https://aclanthology.org/N13-1090/ — king − man + woman ≈ queen (B07, B08).
- Devlin, J., Chang, M., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of
  Deep Bidirectional Transformers for Language Understanding. *NAACL-HLT 2019*.
  https://arxiv.org/abs/1810.04805 — deep contextual representations, poor
  direct use for sentence comparison (B11–B13).
- Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using
  Siamese BERT-Networks. *EMNLP-IJCNLP 2019*. https://arxiv.org/abs/1908.10084
  — the restructuring that makes whole-passage comparison work, the ~65-hours-
  to-~5-seconds efficiency figure (B13, B14), and the paraphrase-placement
  training objective behind the worked example (B21–B26).
- Manning, C. D., Raghavan, P., & Schütze, H. (2008). *Introduction to
  Information Retrieval*, Chapter 6: Scoring, Term Weighting, and the Vector
  Space Model. Cambridge University Press. https://nlp.stanford.edu/IR-book/ —
  cosine similarity's pedigree, predating embeddings (B17–B20).

## Figures (REBUILD LAW — rebuilt natively, never screenshotted)

- `images/representing-text-embeddings-fig-01.png` — the chapter's 2D scatter
  teaching-simplification (vacation/PTO/leave clustered, printer far). Rebuilt
  natively as B04 (`B04_VocabularyToVectors`, new Manim scene) — captioned as
  a teaching simplification, real embeddings use hundreds of dimensions. The
  original PNG remains reference-only; never embedded.
- `images/representing-text-embeddings-fig-02.png` — the chapter's embedding-
  space sketch (paraphrase pair close, shared-phrase-trap pair far). Rebuilt
  natively as B26 (`B26_ParaphraseVsTrap`, new Manim scene, callback to B19's
  cosine geometry) — captioned as a rebuild, qualitative placement only, no
  computed score. The original PNG remains reference-only; never embedded.

## VOX stills — all Tier 1 (generic/illustrative, no rights escalation)

None of the seven VOX beats depict a real, named person, object, or event —
all are generic documentary-style scenes invented for this reel, so all are
Tier 1 per Gate D2 (`reference/shopping-list.md`): real stock photography or
AI-generate, no rights clearance required. Full sourcing (real licensed stock
photos, same method used for this book's Chapter 1/2 deep-explainer pantry
fills) lives in `SHOPPING.md` (written after audio lock, per Gate D2 — not
yet written as of this authoring pass). Subjects, by beat:

- **B02/B03 (run R1)** — a wide shot of library shelves, then a tight shot on
  an open book's printed text. Grounds "a vocabulary learned from an enormous
  amount of ordinary text" (word2vec's training corpus) in something visible.
- **B12** — a research desk, monitor showing dense text/diagrams, notebook
  open. A documentary-era marker for "2019, transformer models" — no specific
  lab, person, or paper is depicted.
- **B17/B18 (run R2)** — a wide shot of an old library card-catalog wall, then
  a tight shot on one open drawer, index cards fanned. Grounds "information
  retrieval represented documents as vectors, decades before neural
  embeddings" in a real documentary object (the vector space model's own
  historical instrument, generically depicted).
- **B23** — two desks, two people typing two different questions into a chat
  window. Grounds the worked example (vacation/PTO vs. time-off/laptop) in
  something concrete, matching this book's own help-desk framing precedent
  (Chapter 1/2 deep-explainer siblings).
- **B29** — a stack of printed pages on a desk. Visual bridge toward Chapter
  4's "chunk" question, without depicting or asserting an answer to it.

## What this reel does NOT claim

- It does not assert that any embedding model was actually run to produce a
  precise similarity score for the worked example (B22–B26) — the chapter's
  own text explicitly declines to give one, and this reel matches that
  caveat exactly: every worked-example beat is qualitative ("similar
  meaning," "different meaning," "same region," "different regions"), never
  a computed number.
- It does not assert a specific mechanism for how Chapter 4 resolves the
  "what counts as one chunk" question (B30, BVDT) — only that the question
  exists and matters, per the chapter's own bridge.
- It does not re-litigate Chapter 2's three-failure argument or the
  cli-explainer's retrieval demo — those are the sibling reels' territory;
  this reel is the full documentary treatment of Chapter 3 alone.
