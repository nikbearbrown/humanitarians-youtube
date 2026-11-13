# BUILD-LOG — Claude, Reviewed.

## Decisions

- **Topic → 4 acts:** why a model can't fully grade itself (the grading
  ladder, judge gaming, never self-grade), where humans sit in the loop
  (the two sign-off gates, RLHF, disagreement as data), where human
  attention actually gets spent (triage sampling vs. blanket review),
  and calibration as the real deliverable (earning the right to run
  unsupervised, recalibration).
- **No book source** — a general, research-centric topic per the human's
  explicit request.
- **Skill trigger fired and was honored**: the task names Claude/Anthropic
  and is LLM-judge-shaped, so the `claude-api` skill was loaded before
  any content was written, and its `shared/evals/build-eval.md` guide
  grounds the grading-ladder taxonomy, the self-grading rule, and the
  two sign-off gates — current, sourced content rather than recalled
  from training. See `FACTCHECK.md`.
- **General HITL industry concepts kept qualitative**: RLHF, inter-
  annotator disagreement, and triage sampling are stated at the level of
  stable, well-documented mechanism, with no specific paper's numbers or
  benchmark percentages attached.
- **No Manim** (same `pangocairo` gap as every prior build) — absorbed
  into REMOTION.
- **Signed for Divyank from the start** — `@DivyankSingh` / "in for
  Divyank" throughout, including the outro card.
- **A3-1's VOX image could not be sourced**: a "triage/sampling" photo
  was attempted across many search terms (sorting lines, conveyor belts,
  airport screening, spotlight staging, card selection) with no usable
  real-photo result; converted that beat to REMOTION instead of forcing
  a weak image, landing at 4 VOX images total (14.3%) rather than the
  usual 5.
- **9:16 portrait coverage planned at authoring time**: `BinaryBranch`/
  `DivergentFates` assigned to A1-5, A2-4, A3-4, A4-4.
- **Location**: `humanitarians-youtube/fellows/divyank-s/2026-08-14-HITL/`
  — folder name given explicitly by the human.
- **Two-deliverable plan**: one 16:9 master (this folder) and one 9:16
  Short (`short/`, via `shorts.py`), both at 4K (16:9: 3840x2160; 9:16:
  2160x3840), matching the standing spec from all prior builds this
  session.
- **File-integrity note, carried forward**: the `humanitarians-youtube`
  folder under `Documents` has split into duplicate directories via an
  apparent cloud-sync conflict on multiple builds this session. Renders
  will be spot-checked with `ffprobe` immediately after each compile,
  cross-checked against the beat sheet's own summed duration, and the
  directory listing checked for a stray duplicate before considering a
  build finished.
