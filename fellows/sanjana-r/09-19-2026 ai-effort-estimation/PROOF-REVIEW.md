# Feedback: "AI Effort Estimation: Stop Guessing How Long Tasks Take" — Sanjana Rao, film 2

**Verdict:** clear-for-public. **Teaching 12/12. Production gate PASS.**
One line: This film sets out to teach a reusable way to turn a gut estimate into an
honest, evidence-based range — and it delivers, because the method (reference-class
forecasting) is shown as a structure before the worked build, and every number on
screen comes from code the film itself displays.

Reviewed from: sampled frames of the compiled 4K master (one+ per beat) + the full
narration. Self-review against PROOF.md by the builder.

## Where it improved vs film 1 (Monte Carlo Schedule Risk)
| Criterion | Film 1 | Film 2 |
|---|---|---|
| Effect legibility | v1→v2 P80 shift small (29.3→29.8), visually subtle — the film's one noted weakness | v1→v2 shown as a large, explicit NUMBER: gut 10 → honest ~19 days, side by side (B08) |
| Falsifiability | folded into the revision (parallel merge) | revision PLUS the method's own limit shown on screen — a no-reference-class task flagged "spike it, don't fake it" (B08) |
| Framework-first | 4-step method before the build | carried forward: 4-step reference-class method (B02) before any example |
| Source-on-screen | numbers from shown code | carried forward: scenes.py dataset === estimate.py v2 HISTORY/VELOCITY shown in B07 |

## Rubric
| Criterion | What it means | This cut |
|---|---|---|
| Explicit framework | Structure shown *before* examples | **2** — B02 lays out reference-class forecasting (DESCRIBE → MATCH → DISTRIBUTION → CALIBRATE) as a labelled pipeline before any build. |
| Reusable rubric | Viewer can apply the axes to a new case | **2** — B09 states the three questions (reference class / what it actually took / velocity) explicitly; B10 hands the copyable prompt. Transfers to any backlog. |
| Worked example | A case walked through live | **2** — B03–B08 build a real `estimate.py`, run it (10 days), revise it, re-run (ranges; ~19). Real numbers throughout, each gut point shown on the optimistic edge of its class. |
| Falsifiability / edge | Framework stress-tested | **2** — two levels: (1) v1 single-point model exposed as systematically optimistic; (2) B08 shows the method's OWN boundary — a task with no reference class is flagged to spike, not estimated. |
| Active task | CTA requires structured doing | **2** — B10 is a scaffold (backlog + last 15 completed tasks with ACTUAL durations → grouped classes, matched ranges, no-match flags) and names good-vs-bad answers, not "ask Claude". |
| Friction | Viewer must resolve a tension | **2** — the film forces the "10 days looks certain but reality is ~19" tension and the "what do you do with no history?" edge; the viewer must supply their own completed-task durations to use it. |
| **Total** | | **12 / 12** |

## Production gate
- **Evidence legible at the moment of assertion — PASS.** Histogram (B01), code (B04/B07),
  point plan (B05), and range bands with P50-P80 labels (B08) are on screen and readable when
  the narration names them (frames checked B00–B11; type ~24px+; warm-ink/cream contrast well
  above AA; the one initial B01 overlap was caught in QC and re-rendered clean).
- **Sources on screen, not just voiced — PASS.** Every figure is produced by the reel's own
  seed-locked estimator; the generating code is shown (B04 v1, B07 v2), and the B07 HISTORY /
  VELOCITY dataset is identical to scenes.py — the film passes its own "no source, no verdict" rule.
- **Side-by-side at the moment of comparison — PASS.** B08 shows each gut point ON its P50-P80
  band (optimism made visible) and the totals gut 10 → honest ~19 together, held > 2s.

## The problem (biggest honest weakness)
The reference-class dataset is illustrative (one sample team's history), so the specific
numbers (8-12, 2-3, 3-5) are a worked example, not a claim about any real project. This is
correct and clearly framed, but a viewer must bring their OWN completed-task history for the
method to produce trustworthy numbers — which is exactly what B10's scaffold asks for. Not a
gate failure; a property of the method, stated in the film.

## Do next (punch list)
1. [EDIT] B05 has generous right-side negative space; a faint "no error bars" cue on each row
   could sharpen the false-precision read. Deferred — the "how sure are we?" line already lands it.
2. [EDIT/NEW SOURCE] For a film 3, a second worked example on a *different* class shape (e.g. a
   bimodal reference class) would stress the "read the spread" step harder. Future film.
3. [EDIT] B08 runs slowed ~2x to fill its 40s narration; motion stays smooth but a touch more
   late-beat animation (e.g. the totals counting up) would use the time even better. Minor.

## What works (keep)
- Framework-first structure (B02 before the build) — the spine that makes it teach.
- Prompt → real code → moving output as one receipt (B03→B04→B05, B06→B07→B08), Claude skin.
- The falsifiability case shown ON SCREEN (no-reference-class → spike it), not just voiced.
- Legible, restrained Claude-skin design; cream cross-dissolve transitions read as one
  continuous piece; @HumanitariansAI on every composer chip + the outro; first-person Sanjana
  cold open exactly as requested; af_bella (female) voice throughout.
- Honesty: numbers are runnable code, effect is not exaggerated, nothing dates the video.

## Series note
Film 2 self-applied film 1's punch list: the "make the effect legible as a number" fix is done
(gut 10 → honest ~19 shown explicitly), and falsifiability is strengthened from a revision-only
case to an on-screen method-limit. Carry the framework-first + source-on-screen template forward.
