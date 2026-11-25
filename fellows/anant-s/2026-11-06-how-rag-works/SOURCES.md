# SOURCES — How RAG Works

This is a concept film. There is one primary paper; every other number is executed locally.

## Primary reference
- P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Küttler, M. Lewis, W. Yih, T. Rocktäschel, S. Riedel, D. Kiela (2020). **"Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks."** *Advances in Neural Information Processing Systems 33 (NeurIPS 2020).* arXiv:2005.11401. <https://arxiv.org/abs/2005.11401>
  - §1: names the method "retrieval-augmented generation (RAG)"; the non-parametric memory "can be replaced to update the models' knowledge as the world changes".
  - §2.2: retriever is DPR, a bi-encoder with BERT-base query and document encoders; top-k retrieval is maximum inner product search.
  - §2.3: generator is BART-large (about 400M parameters).
  - §3: Wikipedia, December 2018 dump; "Each Wikipedia article is split into disjoint 100-word chunks, to make a total of 21M documents"; FAISS index with an HNSW approximation.
  - §4.5 "Index hot-swapping": December 2016 vs December 2018 indexes on 82 world leaders; 70% and 68% accuracy when index and leaders match, 12% and 4% when they don't.
  - Read 2026-11-22 via arxiv.org (abstract page) and ar5iv (full text). The full-text fetch was truncated after about half the paper; every item used in the film is from §1–§4.5, which were read verbatim. Appendix details (exact embedding width, exact parameter count) were not verified and are not used.

## Supporting (background only; no on-screen claim depends on them)
- V. Karpukhin et al. (2020), "Dense Passage Retrieval for Open-Domain Question Answering", EMNLP 2020 (the DPR retriever).
- K. Spärck Jones (1972), "A statistical interpretation of term specificity and its application in retrieval", *Journal of Documentation* 28(1): the idea behind idf, used by the toy embedding.

## Executable evidence
- `demo/rag_demo.py`: pure Python + numpy. Deterministic; no seed is needed because nothing is random.
- Outputs: `demo/evidence.json` (all values, both runs, the prompts) and `demo/RUN-LOG.txt` (human-readable log).
- Environment: Python 3.12.13, numpy 2.5.5, Windows 11 (`Windows-11-10.0.26300-SP0`).
- Script sha256 `ef0b674237a9a11b3df5fb50f5eed3e1ba0f1805fcd71458ea9139e9d66226be`.
- Inputs sha256 `caf5a186dd1c63996296b980b26b664a86fcdb6d948a4dc66d31920a25d1c073` (documents, stale page, question, stop-words, top-k).
- `make_sheet.py` reads every on-screen and spoken number from `evidence.json` and asserts the ranking IDs, so a changed demo cannot silently change the film.

### What is constructed, and labelled so
- The shop handbook (three documents, six sentences) and the stale `faq-2019.txt` page are written for the film.
- The **answer step is illustrated, not executed**. No language model runs. The demo's "reader" is a regex that copies the `<n> days` figure from the rank-1 chunk, to show that the answer follows whatever was retrieved. B08 and B10 carry an on-screen "illustrated" tag.
- The toy embedding is TF-IDF word counting, not a learned model; the narration says so in B03.

## Corrections applied (DOUBLE-CHECK law)
See FACTCHECK rows 9, 20, 21 and 25.

## Seeds
- Hesitant writer: seed = slug `show-tell-how-rag-works`.
- Outro mascot and polarity: seeded by slug (OUTRO-LOCK).
- Demo: none needed (deterministic).
