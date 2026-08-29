# SOURCES — Meaning, As A Number.

## Book source

- Book: *RAG Foundations* (author: Vedanshu Daxesh Patel) — confirmed via
  `D:\ai1-cli-main\metadata.yaml` (title, author, rights all match).
- Chapter: `chapters/03-representing-text-embeddings.md` — "Chapter 3 —
  Representing Text: Embeddings and Semantic Similarity"
- The chapter carries its own fact-check record:
  `chapters/03-representing-text-embeddings.md.verified.json` —
  `verified: true`, `verified_by: "Vedanshu Daxesh Patel"`,
  `verified_at: "2026-08-13"`, "fact-checked at GATE 4 (0 discrepancies)".
  This corroborates but does not replace this reel's own DOUBLE-CHECK LAW
  pass below — every claim was independently checked against its cited
  source, not taken on the chapter's word alone.

## Citations carried into narration (verbatim to the chapter's own citations)

- Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient
  Estimation of Word Representations in Vector Space.
  https://arxiv.org/abs/1301.3781 — word2vec, the 1.6-billion-word training
  corpus figure (B02), used verbatim from the paper's own description.
- Mikolov, T., Yih, W., & Zweig, G. (2013). Linguistic Regularities in
  Continuous Space Word Representations. *NAACL-HLT 2013*, pp. 746–751.
  https://aclanthology.org/N13-1090/ — king − man + woman ≈ queen (B03).
  The chapter's own caveat (the result depends on excluding the query word
  from the nearest-vector search, per later replication work) is carried
  onto the screen as text, not softened or dropped — this is the chapter's
  own DOUBLE-CHECK LAW move, preserved rather than re-simplified into a
  clean-sounding claim.
- Devlin, J., Chang, M., Lee, K., & Toutanova, K. (2019). BERT:
  Pre-training of Deep Bidirectional Transformers for Language
  Understanding. *NAACL-HLT 2019*. https://arxiv.org/abs/1810.04805 —
  referenced in B04's narration (BERT's contextual representations) but
  not quoted with a number on screen.
- Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings
  using Siamese BERT-Networks. *EMNLP-IJCNLP 2019*.
  https://arxiv.org/abs/1908.10084 — Sentence-BERT's restructuring (B04)
  and the real, cited 65-hours-to-5-seconds speed figure for finding the
  most similar pair among 10,000 sentences (B05, BVDT) — both numbers are
  the paper's own reported figures, not invented for this reel (unlike
  Chapter 2's builds, this beat states real numbers on screen because the
  chapter itself states them as the paper's actual reported result, not as
  a qualitative-only claim).
- Manning, C. D., Raghavan, P., & Schütze, H. (2008). *Introduction to
  Information Retrieval*, Chapter 6. Cambridge University Press.
  https://nlp.stanford.edu/IR-book/ — cosine similarity predating embeddings,
  from the classical vector space model (B06).

## Figures (REBUILD LAW — rebuilt natively, never screenshotted)

- `images/representing-text-embeddings-fig-01.png` / `.svg` — the
  simplified 2D word2vec scatter (vacation/PTO/leave clustered, printer far
  away). Rebuilt natively as B02 (`EmbedScatterPlot`) — captioned on screen
  "Redrawn (simplified) from the chapter's own Fig. 01 — real embeddings
  hold hundreds of dimensions, not two," matching the chapter's own caption
  note almost verbatim.
- `images/representing-text-embeddings-fig-02.png` / `.svg` — the 2D
  embedding-space sketch with two question pairs (close vs. far despite
  shared wording). Rebuilt natively as B09 (`EmbedRevealPairs`) —
  captioned "Redrawn (simplified) from the chapter's own Fig. 02."

## Honesty notes

- B03's on-screen caveat about the king/queen result is not softened —
  the chapter is explicit that this is "worth holding loosely rather than
  as a guaranteed computation," and the reel preserves that exact framing
  rather than presenting the equation as a clean, always-true fact.
- B09's worked example follows the chapter's own explicit instruction:
  "reason about this qualitatively... rather than as a specific computed
  number, since no embedding model was actually run to produce a precise
  score for this example." No invented similarity score appears on screen
  anywhere in this reel — B02's and B09's point placements are illustrative
  layout choices (which cluster is closer/farther), not a rendering of any
  real computed embedding.
- B05/BVDT's 65-hours/5-seconds figures ARE real, cited numbers from the
  Reimers & Gurevych paper's own abstract/results — distinguishing this
  from an invented statistic required checking the actual paper's claim,
  not just the chapter's restatement of it.
