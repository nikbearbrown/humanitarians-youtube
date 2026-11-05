# CHECKS-REPORT — hai-repo-sensei-v2

Every gate this reel was run through, with the result as the tool reported it.

## Gate A — static scene pre-flight

Every Manim class in `scenes.py` checked for shape motion and runtime errors before any
render. All clean.

## Gate B — layout audit

`manim_layout_audit.py` renders each scene headless and checks every label against the
title-safe box, against lines and curves it might sit on, and against its neighbours.
All scenes clean; annotated frames in `layout_audit_frames/`, report in `layout_audit.md`.

## Gate T — typography and contrast

Spec: `skills/make/kerning/reference/type-spec.md` §8. Floor 1.9% frame-height, contrast
4.5:1 WCAG, kern threshold 3.5x expected advance.

**Landscape** — Reel: `hai-repo-sensei-v2`  |  Checked: 2026-10-26T18:50  |  Overall: PASS  |  Beats checked: 20  |  FAILs: 0

**Vertical** — not built for this reel.

## Gate V — frame-level visual QC

# Gate V — visual QC report

Frames sampled: 40  ·  BLOCKER: 0  ·  MAJOR: 0

Clean — no BLOCKER/MAJOR defects. ✓

## Gate F — fact check

Claim-level verdicts in [FACTCHECK.md](FACTCHECK.md). SPEC-ASSERTED rows are the open
ones and that sign-off is the fellow's.

## Build gate

Full per-beat record in [BUILD-LOG.md](BUILD-LOG.md).
