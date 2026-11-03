# PROOF.md — self-assessment · rag-pdf-pytorch

**Reel:** RAG in PyTorch: Answer Questions From a PDF
**Volunteer:** Ameya Deshmukh · **Category:** AI & STEM topic video
**Persona:** Liam, in for Ameya (Kokoro `am_onyx`) · **Channel:** @HumanitariansAI
**Deliverable:** `RAGPipelinePyTorch_AmeyaDeshmukh_2026-08-14.mp4` · **Resolution:** 3840×2160 (4K) · **Runtime:** ~3:03

Self-assessment against the reviewer requirements and the toolkit gates.

## Requirements checklist
| Item | Status | Evidence |
|------|--------|----------|
| Handle @HumanitariansAI throughout (no @NikBearBrown) | ✅ | `folderLabel` on all composer beats (B00/B02/B05/B09); outro handle B10 |
| 4K (3840×2160) | ✅ | Manim scenes `-r 3840,2160`; Remotion `--scale=2`; compiled `--height 2160` |
| Code/source on GitHub | ✅ | reel source committed (rendered media gitignored, regenerates) |
| Self-assess with PROOF.md | ✅ | this file |
| STEM-topic naming `TopicName_YourNameDate` | ✅ | RAGPipelinePyTorch_AmeyaDeshmukh_2026-08-14.mp4 |

## Content integrity (ACTUAL-CODE + DOUBLE-CHECK LAW)
- B03 and B06 show **real, runnable PyTorch** (sentence-transformers `model.encode`
  → tensor; `torch.nn.functional.normalize`; `q @ emb.T`; `torch.topk`; a grounded
  prompt). Technical claims verified in [FACTCHECK.md](FACTCHECK.md) / [SOURCES.md](SOURCES.md).
- The 2D vector space is captioned as a simplification of the real 384-dim space;
  `llm(...)` is labelled as the viewer's own model call (not a product placement).

## Toolkit gates
- **GATE P:** [PEDAGOGY.md](PEDAGOGY.md), VERDICT: PASS.
- **GATE V (visual QC):** 0 BLOCKER after review — fixed frame-edge bleed on the
  concept beats (B01, B08) found in earlier passes. Remaining advisories are
  canvas-fill / contrast on the sparse concept cards and the outro title-card
  template (`ClaudeTitleOutro`). Contact sheet: `qc-sheet.png`.
- **Revision cycle (cli-explainer):** present — B02→B03→B04 (index) then
  B05→B06→B07 (retrieval).
- **Audio-first:** 11 beats measured (Kokoro); Manim scenes auto-fill to the clock.

## Weekly-report content
- **Worked on:** a build-along explainer of a Retrieval-Augmented Generation
  pipeline over PDFs, in PyTorch.
- **Completed:** chunk → embed (sentence-transformers) → retrieve
  (`q @ emb.T` + `topk`) → grounded, cited answer — as a 4K cli-explainer with
  real code on screen.
- **Next:** a follow-up on chunking strategies / re-ranking to cut retrieval noise.

**Self-verdict: PASS** (0 blockers; advisories are inherent-outro + near-threshold
fill/contrast on concept cards). Ready to upload.
