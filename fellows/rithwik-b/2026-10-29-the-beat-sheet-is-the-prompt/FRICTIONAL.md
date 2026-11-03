# FRICTIONAL — The Beat Sheet Is the Prompt

The frictional log for this piece of work: short, dated, honest entries about what was
tried, where it resisted, what was done about it and what was learned — appended as the
work goes, never rewritten. <https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-10-29 — Build, QC and fixes

> Drafted with Claude on 2026-11-02 from this folder's beat sheet, QC report and the
> series build log, which were kept during the build.

**Working on.** Name a beat's parts (narration, show, scene) and explain why Brutalist generates audio first. Research and scripting ran Weeks 3–4; the film was
narrated, rendered and checked on 2026-10-29.

**Tried, and expected.** Explain the beat sheet as the single prompt a Brutalist film is built from: narration, show events and a scene per beat, with audio generated first so narration sets the clock. I expected it to go faster than film 1 because the generator script reused film 1's spine.

**Where it resisted, and what I did next.**

- B01 was only ~10 s long, so the opening correction never landed by 75% of the beat. GATE V passed the film anyway. Typing 35 → 20 ms/char, fewer pauses.
- The correction read "the whole job." — the replacement text was split on its comma by the hesitant-writer component. Rewrote it as "a complete description" and re-rendered.
- The JSON-diff code card was labelled PYTHON. Set `language` per card.

**What Claude contributed — accepted, changed, rejected.**

- Claude generated the sheet from `build_films.py`, rendered, and found the comma split by reading the frame at 90%.
- Accepted: rewriting the replacement words rather than patching the component — the toolkit stays read-only.

**Understand now / still don't.**

- Now: A component's input format is part of the prompt. A comma in the wrong place changed what was on screen.
- Still open: Whether a viewer new to Brutalist follows the narration / show / scene split without the diagram on screen.

**Evidence:** [`QC-REPORT.md`](./QC-REPORT.md) · [`FACTCHECK-DRAFT.md`](./FACTCHECK-DRAFT.md) · [`beat_sheet.json`](./beat_sheet.json)
