# Feedback: "Monte Carlo Schedule Risk: When Will This Project Really Finish?" — Sanjana Rao, film 1

**Verdict:** clear-for-public. **Teaching 12/12. Production gate PASS.**
One line: This film sets out to teach a reusable way to turn a single-point deadline
into an honest, simulated one — and it delivers, because the method is shown as a
structure before the worked build, and every number on screen comes from code the
film itself displays.

Reviewed from: sampled frames of the compiled 4K master (one per beat) + the full
narration. Self-review against PROOF.md by the builder.

> **Revision 2 (post-feedback):** narration rewritten to be warmer and jargon-light
> for beginners (Monte Carlo, P50/P80/P90, and the "wait for the slowest path" idea
> are now explained in plain words); runtime 4:52 → 5:38. The B09 "Read three numbers"
> summary had overlapping P50/P80/P90 labels — rebuilt as a left-side legend + clean
> color-coded lines (no overlap). Chapter timestamps in description.txt updated. The
> 9:16 Short was lengthened 35s → 54s with fuller narration and a slower chart build.

## Rubric
| Criterion | What it means | This cut |
|---|---|---|
| Explicit framework | Structure shown *before* examples | **2** — B02 lays out the 4-step method (RANGE → SAMPLE ONCE → REPEAT 10,000× → COMMIT TO P80) as a labelled pipeline before any build. |
| Reusable rubric | Viewer can apply the axes to a new case | **2** — the exact procedure (three-point estimate per task → simulate → read P50/P80/P90) transfers to any plan; B10 hands the copyable prompt. |
| Worked example | A case walked through live | **2** — B03–B08 build a real `schedule_sim.py`, run it, read the distribution, then revise it; real numbers throughout (plan 19; P80 ≈ 29). |
| Falsifiability / edge | Framework stress-tested | **2** — B06–B08 expose the naive single-chain model as too optimistic and add the parallel merge (finish = max of paths), the counter-case that shifts the distribution right + wider. |
| Active task | CTA requires structured doing | **2** — B10 is a scaffold (paste tasks + three estimates + dependencies; get P80 + the driving task), not "ask Claude". |
| Friction | Viewer must resolve a tension | **2** — the film forces the "plan says 19 but the P80 says 29" tension and the merge-bias surprise; the viewer must supply their own estimates and dependencies to use it. |
| **Total** | | **12 / 12** |

## Production gate
- **Evidence legible at the moment of assertion — PASS.** Histograms, code, and the
  plan/P50/P80 markers are on screen and readable when the narration names them
  (checked B01, B04, B05, B08 frames; ~24px+ type, cream/ink contrast well above AA).
- **Sources on screen, not just voiced — PASS.** Every figure is produced by the
  reel's own simulator; the generating code is shown (B04 v1, B07 v2). The film
  passes its own "no source, no verdict" rule.
- **Side-by-side at the moment of comparison — PASS.** B08 overlays the v1 and v2
  distributions with both P80 markers, held well over 2s.

## The problem (biggest honest weakness)
The v1 → v2 P80 shift is real but **numerically small** (≈29.3 → ≈29.8 days), so the
"later and wider" claim, while true and correctly shown side-by-side, is visually
subtle. This is a fidelity choice (the numbers are not exaggerated), but a viewer
skimming B08 could miss the size of the effect.

## Do next (punch list)
1. [EDIT] In B08, add a small numeric callout of both P80 values (e.g. "29.3 → 29.8")
   so the shift is legible as a number, not only as overlapping bars. (Deferred — the
   arrow + "later + wider" caption already carries the point; low risk.)
2. [EDIT] Consider a second, more parallel example where merge bias is larger, to
   dramatize the effect — future film, not this cut.
3. [EDIT] Manim output beats freeze-hold 3–5s at their tail to match narration; fine,
   but a touch more motion under the closing narration of B05/B09 would help. Minor.

## What works (keep)
- Framework-first structure (B02 before the build) — the spine that makes it teach.
- Prompt → real code → moving output as one receipt (B03→B04→B05, B06→B07→B08).
- Legible, restrained Claude-skin design; cream cross-dissolve transitions read as one
  continuous piece; @HumanitariansAI brand bug on every beat; first-person Sanjana
  cold open exactly as requested.
- Honesty: no exaggerated numbers, no undated model claims, sources are runnable code.

## Series note
No prior film in this series to diff against. If a film 2 follows, carry the
framework-first structure and the source-on-screen discipline forward as the standing
template.
