# Vedanshu Daxesh Patel.

**Role:** Software Engineer, Humanitarians AI
**Project:** AI+1
**Project Manager:** Shourya Verma
**Tenure:** 2026-07-22 to 2026-10-02 (two contracts, Weeks 1–11)
**Kokoro voice:** `am_onyx` (used for the whole series)
**Last updated:** 2026-09-29

## Executive Summary

Vedanshu Daxesh Patel spent the tenure learning the AI+1 pipeline and then building out the retrieval layer of a RAG system, one component at a time. Weeks 1–3 covered ramp-up and debugging: generating a sample book, converting it through Brutalist into a beat sheet and video, and diagnosing pipeline output. From Week 4 the work moved to RAG: the problem RAG solves, embeddings, chunking, vector databases, retrieval methods, end-to-end assembly, prompt construction, and reranking with query rewriting. Each topic was produced as an explainer reel, and most as a CLI demo reel with runnable Python and captured run output. Two summary reels condense Chapters 1–3 and 4–6. Documented hours total 242 across 11 weeks. Each week falls in the 20–40h OPT range. The main open item is that no final retrieval-design decision for AI+1 is recorded (see Open Items).

## Quick Review

- **Weekly hours:** table below, taken from the completion report
- **Work evidence:** one dated folder per reel, each with a beat sheet, sources, pedagogy notes, and a checks report. CLI reels also include `code/` and `_run-*.txt` output.



## Hours by Week

| Week | Dates | Hours | Focus | Folders in this repo |
|---|---|---|---|---|
| 1 | Jul 22–28 | 23 | Book generation and research (ramp-up) |  |
| 2 | Jul 29–Aug 4 | 25 | Beat sheet and video via Brutalist (ramp-up) |  |
| 3 | Aug 5–11 | 22 | First debugging of pipeline stages |  |
| 4 | Aug 12–18 | 22.5 | RAG book, first RAG work | `2026-08-12-*`  |
| 5 | Aug 19–25 | 21 | Assigned 9:16 task; caught a factual error and a code error | `2026-08-19-*`  |
| 6 | Aug 26–31 | 22 | 4K/QC feedback, LangChain integration R&D | `2026-08-26-*` , `2026-08-31-*`  |
| 7 | Sep 1–7 | 21 | RAG embeddings and summary video | `2026-09-01-*` |
| 8 | Sep 8–14 | 21 | Chunking and vector-DB experiments | `2026-09-08-*` |
| 9 | Sep 15–21 | 21 | Retrieval methods and summary video | `2026-09-15-*`  |
| 10 | Sep 22–28 | 22 | End-to-end RAG pipeline and prompt construction | `2026-09-22-*` |
| 11 | Sep 29–Oct 2 | 21.5 | Reranking, query rewriting, summary video (final week) | `2026-09-29-*` |
| **Total** | | **242** | First contract 135.5h (W1–6), renewed 106.5h (W7–11) | |

## Folder Guide

| Folder | Reel title | What it shows |
|---|---|---|
| `2026-08-12-claude-rag-introduction/` | The Model Never Saw The Document. | Why a model can't answer from a document it never saw |
| `2026-08-12-claude-rag-deep-explainer/` | Two Kinds Of Memory. | Parametric vs. retrieved memory, long form |
| `2026-08-19-claude-rag-the-problem/` | Confident, Frozen, Or Buried. | Three failure modes RAG addresses |
| `2026-08-19-claude-rag-the-problem-deep-explainer/` | Three Ways To Be Wrong. | Long-form version of the same three failures |
| `2026-08-26-claude-rag-embeddings/` | Meaning, As A Number. | What an embedding is |
| `2026-08-26-claude-rag-embeddings-deep-explainer/` | The Geometry Of Meaning. | Embedding space, long form |
| `2026-08-26-claude-cli-rag-embeddings/` | Watch Embeddings Beat The Wrong Words. | CLI demo: semantic match beats keyword overlap |
| `2026-08-31-claude-cli-rag-introduction/` | Watch Retrieval Fix A Stale Answer. | CLI demo: retrieval corrects an outdated answer |
| `2026-08-31-claude-cli-rag-the-problem/` | Watch The Obvious Fix Fail. | CLI demo: why the naive fix doesn't work |
| `2026-09-01-claude-rag-embeddings/` | Meaning, As A Number. | Revised embeddings reel, with 9:16 short |
| `2026-09-01-claude-summary/` | The Right Text. | Summary of Chapters 1–3 |
| `2026-09-08-claude-rag-chunking/` | Where You Cut The Page. | Chapter 4: chunking strategies |
| `2026-09-08-claude-cli-rag-vector-databases/` | Watch Exact Search Hit A Wall. | Chapter 5: brute-force vs. ANN search (`code/`, `_run-*.txt`) |
| `2026-09-15-claude-cli-rag-retrieval-methods/` | Watch The Right Answer Get Outvoted. | Chapter 6: BM25, dense, and hybrid retrieval |
| `2026-09-15-claude-summary/` | There Is No Default. | Summary of Chapters 4–6 |
| `2026-09-22-claude-cli-rag-pipeline/` | Watch A Bug Name Its Own Stage. | End-to-end pipeline with per-stage diagnosis |
| `2026-09-22-claude-rag-prompt-construction/` | Labels Are Not Decoration. | How retrieved context is labeled in the prompt |
| `2026-09-29-claude-cli-rag-reranking/` | Reorder Is Not Retrieve. | Chapter 9: cross-encoder reranking and query rewriting |

Folders from `2026-08-31` on include a `short/` 9:16 cut. Several include a `short/QC-REPORT.md`.

## Open Items

1. **Retrieval decision not recorded.** Weeks 7–11 implemented and compared several chunking, retrieval, and reranking approaches. No record says which approach AI+1 should use or why.

## Source Attribution

All reels are adapted from *RAG Foundations*, the volunteer's own AI+1-generated book (`source_book` in each `beat_sheet.json`). The volunteer's contribution covers the book, the beat sheets, the Python demos under `code/`, the fact checks, and the renders. Source figures are rebuilt natively, not embedded; the details are in each folder's `SOURCES.md`. Summary reels reuse figures and numbers from their source reels and add no new claims. Rendering uses the Brutalist toolkit (`nikbearbrown/brutalist.art`).


