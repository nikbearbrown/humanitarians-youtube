# PROOF.md — self-assessment · rag-from-first-principles

**Reel:** RAG From First Principles (deep-explainer of VIDEO_SCRIPT.md)
**Volunteer:** Ameya Deshmukh · **Category:** AI & STEM topic video
**Persona:** Liam, in for Ameya (Kokoro `am_onyx`) · **Channel:** @HumanitariansAI
**Deliverable:** `RAGFirstPrinciples_AmeyaDeshmukh_2026-08-21.mp4` · **Resolution:** 3840×2160 (4K) · **Runtime:** ~7:55 · **25 beats, 12 acts**

## Requirements checklist
| Item | Status | Evidence |
|------|--------|----------|
| Handle @HumanitariansAI throughout (no @NikBearBrown) | ✅ | folderLabel on composer beats B00/B23; ClaudeVerdictArtifact + ClaudeTitleOutro carry it |
| 4K (3840×2160) | ✅ | 18 Manim scenes `-r 3840,2160`; Remotion `--scale=2`; compiled `--height 2160` |
| Code/source on GitHub | ⏳ | reel source ready to commit (rendered media gitignored) |
| Self-assess with PROOF.md | ✅ | this file |
| STEM-topic naming `TopicName_YourNameDate` | ✅ | RAGFirstPrinciples_AmeyaDeshmukh_2026-08-21.mp4 |

## Content integrity (DOUBLE-CHECK, sharpened for deep-explainer)
- Every on-screen number is from the script's Appendix B claims ledger, each tied to
  a generating script in this repo. Verification status stated honestly in
  [FACTCHECK.md](FACTCHECK.md): source-asserted + reproducible; internal consistency
  (0.2% latency, 320×, 4.4 MB, FLOP identity, −35.5%) arithmetic-checked; scripts not
  re-run this session.
- B03/B11/B12 show real repo code (chunk_text, cosine, the argpartition top-k bug).
- The script's honest caveat (name-driven corpus → sweep your own weight) is kept in narration.

## Genre adaptation (documented)
Deep-explainer normally wants ~20–25% VOX (documentary stills). This is a measurement
film with no archival content, so VOX = 0, no pantry / no Gate D2 — body is Manim +
code + segment cards. Rationale in [BUILD-LOG.md](BUILD-LOG.md).

## Toolkit gates
- **GATE P:** [PEDAGOGY.md](PEDAGOGY.md), VERDICT: PASS.
- **GATE V (visual QC):** **0 BLOCKER** after review — fixed frame-edge bleed on the
  cold-open kicker (B01) and the scale table (B21) found in the first pass. Remaining
  advisories: B04 canvas fill 44%, and the ClaudeVerdictArtifact (B22) + ClaudeTitleOutro
  (B24) Remotion templates (inherently sparse). Contact sheet: `qc-sheet.png`.
- **Audio-first:** 25 beats measured (Kokoro, ~7:55); Manim scenes auto-fill to the clock.

## Weekly-report content
- **Worked on:** a full first-principles RAG explainer — chunking, tokenization,
  embedding/batching, indexing, retrieval, pooling loss, evaluation, and three
  counterintuitive measured results — from the fin-disclosure-rag repo.
- **Completed:** 12-act, ~8-min 4K deep-explainer with real code and real measurements.
- **Next:** the "deep cut" extensions (live retrieval.py / hybrid.py walkthroughs, a trace).

**Self-verdict: PASS** (0 blockers; advisories are one sparse teaching frame + two
inherent Remotion templates). Ready to upload.
