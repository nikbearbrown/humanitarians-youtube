# Feedback: "Two-Week Progress Review: 172 Videos, One Cadence" — Sanjana Rao, film 3

**Verdict:** clear-for-public. **Teaching 11/12. Production gate PASS.**
One line: This film sets out to turn a two-week review log into a stakeholder
dashboard — and it delivers, because the system (weekly cadence + review pipeline)
is shown before the numbers, and every figure is computed from the tracker by code
the film itself displays.

Reviewed from: sampled frames of the compiled 4K master (one+ per beat) + the full
narration. Self-review against PROOF.md by the builder. This is a progress REPORT,
so the rubric is applied in that register (the "reusable method" is the reporting
workflow a stakeholder/PM can re-run, not a scientific framework).

## Rubric
| Criterion | What it means | This cut |
|---|---|---|
| Explicit framework | Structure shown *before* the data | **2** — B02 shows the weekly-cadence toggle + the REVIEW → upload/changes/block → GitHub pipeline before any number. |
| Reusable rubric | A viewer could re-run it on a new case | **2** — B10 hands the exact prompt (tracker → totals, week/project split, GitHub rate, three stakeholder sentences); any PM can run it. |
| Worked example | A case walked through live | **2** — B03–B08 read the real tracker, compute 172/119/50/3, then revise to the Week1/Week2 + project split; numbers reproduced by the shown pandas. |
| Falsifiability / honesty | Stress-test / stated limits | **1** — B09 states the method's limits on screen (counts videos not hours; "changes requested" keeps converting to "changes made"). Honest, but a report has no true counter-case, so this is gestured rather than a hard falsifier. |
| Active task | CTA requires structured doing | **2** — B10 is a copyable scaffold with good-vs-bad answers named, not "ask Claude". |
| Friction | Viewer must resolve a tension | **2** — the "119 clean vs 50 sent back" and "is my cadence real?" tensions drive the build; the viewer must supply their own tracker to use it. |
| **Total** | | **11 / 12** |

## Production gate
- **Evidence legible at the moment of assertion — PASS.** Counters/waffle (B01),
  diagram (B02), code (B04/B07), KPI cards + funnel (B05), week bars + donut (B08),
  scorecard + gauge (B09) are all readable when named (frames checked B00–B11;
  type ≥ ~24px on 4K; warm-ink/cream contrast well above AA).
- **NO overlapping text/graphics — PASS (explicit creator requirement).** Every
  dashboard scene was frame-checked; two overlaps were caught and fixed before the
  final (B01 waffle caption clipped; B05 tiny "blocked" label colliding with
  "changes"). Re-verified clean in the final master.
- **Sources on screen, not just voiced — PASS.** Every number is computed from the
  tracker; the generating pandas is shown (B04 v1, B07 v2); scenes.py constants
  equal the code's printed outputs (172 = 119+50+3 = 87+85 = 77+95).
- **Side-by-side at the moment of comparison — PASS.** B05 funnel and B08 (Week 1
  vs Week 2 + project donut) show the splits together, held ≥ 2s.

## The problem (biggest honest weakness)
As a status report, it has no genuine falsifiability case — the honest-caveat beat
(B09) substitutes for it and is the right call, but it caps teaching at 11/12. If a
future report wanted the 12th point, it could show a target/threshold the numbers
are graded against (e.g., an SLA on turnaround) so the data can "fail," not just
describe.

## Do next (punch list)
1. [EDIT] B05 (2.13x) and B08 (2.34x) run slightly slow to fill their narration;
   fine (mostly fades/holds) but a touch more late-beat motion would use the time.
   B09's earlier 3.2x extreme slow-mo was already fixed (→1.42x) by lengthening.
2. [EDIT] Consider a turnaround-time metric (days from review → approved) in a
   future cut to add a gradable target and lift falsifiability to 2.
3. [KEEP] The different-graphics requirement is met: counters, waffle, flow diagram,
   KPI cards, funnel, week bars, donut, gauge — a distinct visual language from the
   histogram/range-band reels, same Claude palette + identical intro/outro.

## What works (keep)
- System-before-numbers structure (B02) — the spine that makes a report teach.
- Real tracker → real pandas → dashboard as one receipt (B03→B08); every figure sourced.
- Honest, aggregate-only reporting (no fellow named/ranked); the on-screen caveat.
- Legible, restrained Claude-skin dashboards; cream cross-dissolves; @HumanitariansAI
  throughout; identical Claude intro/outro; first-person Sanjana; af_bella voice.

## Series note
Film 3 keeps the framework-first + source-on-screen template from films 1–2 and
adds a dashboard visual language on request. Carry the "show the system before the
numbers" discipline forward for future stakeholder updates.
