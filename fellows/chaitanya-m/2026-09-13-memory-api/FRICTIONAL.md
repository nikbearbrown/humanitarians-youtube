# FRICTIONAL — Memory API

The frictional log for this piece of work: short, dated, honest entries about
what was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-09-28 — Retrospective entry for the 2026-09-13 reel

> **Written 2026-09-28, after the work it describes.** The frictional-log rule
> arrived 2026-09-22, after this reel was built and merged, so no
> contemporaneous log exists. Reconstructed from this folder's `BUILD-LOG.md`,
> `SOURCES.md`, `FACTCHECK.md` and the commit history — then drafted with Claude
> from that record. **Sections marked `[NOT RECORDED]` are gaps only I can
> fill.**

**Working on.** The Memory API subsystem — how the hub carries learner memory
across textbooks — built from a presentation deck rather than a written script.

**Tried, and expected.** The constraint was "don't change anything in
brutalist." I expected that to force a re-implementation of the deck as Remotion
scenes. It didn't: rendering the real deck headless turned out to be both easier
and more honest, because the visuals are then the actual artifact rather than a
copy of it.

**Where it resisted, and what I did next.**

- `--virtual-time-budget` is not a clock. Page load consumes the budget, so a
  nominal 200ms landed after an animation with a 450ms delay had already
  finished. Replaced with explicit seeking — freeze animations in CSS from frame
  one, then rewrite `animation-delay` to `(original − t)`.
- The deck declares its delays with `!important`, so an inline style loses and
  the `.rise` elements never appeared at all. The seek has to use
  `setProperty(..., 'important')`. Found by inspection, not by reading docs.
- Freezing from frame one also killed a race that had produced non-monotonic
  output — t=0.6s showed *more* than t=1.3s.
- The narration did not fit the deck's `data-dur` windows: three scenes overrun,
  three undershoot. Holding to the windows would cut Bella off mid-sentence
  three times. Cut the beats to measured narration, which the script explicitly
  permits.
- `shorts.py`'s default centre-cut destroyed every two-column slide — on scene 2
  the headline vanished and `LEARNER_PROFI` was truncated mid-word. Fixed with
  the tool's own `pantry/` override rather than an out-of-tree crop.
- `shorts.py` first reported "STILL OVER" using a 20s *estimate* for the
  un-regenerated outro. The real audio was 15.30s and no beat needed dropping.
- Scene 5 carried a claim flagged as possibly stale. I kept the primary
  narration rather than substituting the alternate, because the primary states
  its own uncertainty aloud. At port time it was confirmed — and harder than the
  narration put it: no textbook calls the hub at all.
- At review, a chapter-list defect surfaced that the build had not caught: the
  7.98s sign-in beat would have silently disabled the entire YouTube chapter
  list, because one sub-10s chapter kills the whole list with no warning. Wrote
  `chapters.py` to generate and *validate* the list rather than fix it by hand.

**What Claude contributed — accepted, changed, rejected.**

- Claude wrote the deck capture, ran the build, wrote the build log, did the
  fact-check against `medhavi-hub`, and wrote `chapters.py`.
- Accepted: rendering the deck as-is instead of re-implementing it. Accepted:
  regenerating the outro before trusting the cap arithmetic.
- Changed: the auto-rewritten short outro spliced unspeakable mid-sentence
  fragments; replaced with a coherent line. The auto-generated endcard was in
  the wrong brand and named the wrong channel; rebuilt.
- Rejected: substituting the alternate Scene 5 on an unconfirmed claim.
- `[NOT RECORDED]` — what I rejected in the deck's own design, and whether the
  four-value palette was mine or inherited.

**Understand now / still don't.**

- Now: a tool's default can be wrong for your reel without the tool being wrong.
  `shorts.py` documents `pantry/` as the human's override precisely because
  centre-cuts fail on some layouts — using it is the intended path, not a
  workaround.
- Now: a validator that refuses to emit bad output beats a checklist. The
  chapter rule is invisible until it silently costs you the feature.
- Still open: the fact-check found the 24-turn window is a caller-supplied
  default clamped to [2,100], not a fixed limit, and that the shared-secret auth
  is skipped entirely in non-production. Both are stated in `description.txt`
  but neither is corrected in the video.
- Still open: no frame-level QC report was written for this reel, unlike the
  others. The `_qc/` frames exist; the written rubric pass does not.

**Evidence:** [`BUILD-LOG.md`](./BUILD-LOG.md) · [`FACTCHECK.md`](./FACTCHECK.md) ·
[`PEDAGOGY.md`](./PEDAGOGY.md) (GATE P, signed 2026-09-17) ·
[`chapters.py`](./chapters.py) · PR [#122](https://github.com/nikbearbrown/humanitarians-youtube/pull/122)
