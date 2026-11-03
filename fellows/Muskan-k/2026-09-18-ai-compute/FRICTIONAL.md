# Frictional log — Explainer: AI's Four Chips (CPU · GPU · TPU · NPU)

## 2026-09-18 — claude-hai explainer, 16:9 + 9:16

- **Drive:** https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G

Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`, `PROOF-REVIEW.md`
(11/12, gate PASS), `_qc/REPORT.md`, `ai-compute.mp4`, `short/ai-compute-short.mp4`.
(YouTube / Drive: TBD.)

**What I was working on.** An explainer on AI specialized compute — CPU/GPU/TPU/NPU —
framework-first: AI is mostly parallel matrix math, so chips trade generality for
AI-speed along a spectrum; match the chip to the job, it's not a ranking. Kept it
non-dating (no FLOPs, benchmarks, or model names).

**What I tried, and what I expected.**
* I expected the existing card kinds (grid, versus) to carry the CPU → GPU → TPU → NPU
  progression.

**Where it resisted, and what I did next.**
* None of the kinds showed a *general ↔ specialized spectrum* well — a grid is a set,
  a versus is two sides, but this needed one axis with four points. Had Claude add a
  new "spectrum" kind to the generator (horizontal axis + markers in 16:9; vertical in
  9:16). Verified it reads cleanly in both aspects before committing to the full render.

**What Claude contributed, and what I did with it.**
* Mine: the topic, the framework (match chip to job / not a ranking), GATE P, review.
* Claude's: the beat sheet; the new spectrum kind; all rendering/compiling; PROOF.

**What I understand now, and what I still do not.**
* Understood: a spectrum is the right visual for a "general → specialized" axis, and
  it's now reusable in the generator.
* Not resolved: PROOF flagged the worked example walks only one chip (face-unlock →
  NPU); showing the lens *discriminate* between two jobs would be stronger.
