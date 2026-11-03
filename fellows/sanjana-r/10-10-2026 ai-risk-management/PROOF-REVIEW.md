# Feedback: "The Risk Register" — Sanjana Rao (AI + Risk Management)

**Verdict:** clear-for-public. **Teaching 12/12. Production gate PASS.**
One line: *This film teaches that an AI risk register is a strong draft of the KNOWN risks —
and hands the viewer a three-step method (SCORE / OWN / WATCH) to catch the project-specific
risk no template has.*

Self-reviewed against PROOF.md after a frame-level pass on the FINAL 4K deliverable
(GATE V 0 BLOCKER / 0 MAJOR after fixes).

## Rubric
| Criterion | This cut | Score |
|---|---|---|
| Explicit framework | T03 shows SCORE / OWN / WATCH as a structure BEFORE any example | 2 |
| Reusable rubric | the three steps apply to any AI-built register; restated as a router in T07 | 2 |
| Worked example | T05 scores a register, adds the project-specific high/high risk, assigns triggers | 2 |
| Falsifiability / edge | T06: a calm all-green grid that MISSES the one high-impact risk (absence, not mis-scoring) | 2 |
| Active task | T08 hands a copyable prompt (scored register + blind-spots list), read + discussed | 2 |
| Friction | the P×I grid looks "covered," then the blind-spot dot off the grid forces the viewer to distrust the calm | 2 |
| **Total** | | **12 / 12** |

## Production gate
- **Legible at assertion** — PASS. Initial GATE V flagged T02 edge-bleed (blind-spot cluster
  past the right edge) + low-contrast on the grid scenes (faint muted labels + too-faint grid
  fills). Fixed: `fit_width` guard + inward move; darkened the `muted` token, gave grid cells
  crisp ink strokes, raised fill saturation, enlarged dots. Re-verified clean (0/0).
- **Sources on screen** — PASS. Concept explainer: example risks/scores labeled illustrative;
  no fabricated statistic; framework labeled a reusable rubric (FACTCHECK.md).
- **Side-by-side at comparison** — PASS. Template risks vs the off-grid blind spot (T02);
  the green cluster vs the MISSING high-impact corner (T06), held ≥2s.

## What works (keep)
- Framework is real, not reverse-engineered: SCORE/OWN/WATCH maps to identify→(human)
  context→respond/monitor; the falsifiability case fails by ABSENCE, a different mode than
  the worked example.
- New visual language (probability×impact heat grid, blind-spot dot, MISSING marker) distinct
  from the progress reels; one terracotta accent per beat.
- No people named; the handoff turns the lesson into a tool the viewer runs on their own plan.
