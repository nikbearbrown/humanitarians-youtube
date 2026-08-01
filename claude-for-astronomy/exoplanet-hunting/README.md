<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# Exoplanet Hunting: Teaching AI to Show Its Work

## What this video is about

**Topic:** AI IN ASTRONOMY & SPACE SCIENCE

This is Humanitarians.

The current plan contains **19 beats**. Estimated runtime is **~2:28**, computed from word counts
only — no audio has been generated yet, so this is not a measured duration (see `STATUS.md`).
The source is `SHOTLIST.md` and `FACTCHECK.md` in this folder.

Episode 02 of the planned weekly series covering AI applications across astronomy and space
science (see `weekly_stem_videos/ideas.md`). Episode 01, `ai-vs-the-data-deluge`, told the story
of AstroNet's two-view CNN finding Kepler-90i. That episode's own README asked for a follow-up that
goes deeper into false-positive types and a different confirmed case rather than repeating the
same anecdote — this episode is that follow-up: it names the three signal types that fake a
transit (eclipsing binary, stellar variability, instrumental artifact), then walks through NASA
Ames's ExoMiner (2021), a classifier built from separate, explainable diagnostic-test branches
(centroid offset, odd/even transit depth, secondary eclipse) rather than a black box, and its
301-planet Kepler batch validation and 2026 TESS extension (ExoMiner++).

**This project has not been built yet** — it is at the "beat sheet authored" stage (see
`STATUS.md`). No audio or video exists for it in this repo copy.

## Make your own version

Download the free local toolkit:

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

The toolkit uses local Kokoro narration and does not require an API key. The beat sheet is the
source of truth: one beat per moment, with narration, visual intent, and shot instructions. For
this project, start with `beat_sheet.json`. Preserve it before experimenting; make a copy or a
branded variant rather than overwriting the plan.

Recommended builder: **`ai-explainer`** — one tight insight, single mechanism, single worked
example, same shape as Ep.01 (one system, one architecture detail, one takeaway) rather than a
multi-act documentary.

## Research prompt

Paste this into your research workflow before rewriting the video:

> Research **"Exoplanet Hunting: Teaching AI to Show Its Work"** for an educational explainer
> about **AI IN ASTRONOMY**, specifically NASA's ExoMiner classifier and the three false-positive
> types it's built to catch. Start from the source links already logged in `FACTCHECK.md` in this
> folder, then locate primary sources, official documentation, peer-reviewed research, or original
> datasets. Identify the central question, one concrete key case, the mechanism that resolves it,
> important terminology, dated or version-sensitive claims, credible disagreements, limitations,
> and visual evidence suitable for animation. Return a claim table with: claim, exact source URL or
> citation, publication date, quoted or pinpoint evidence, confidence, and what must still be
> verified. Do not invent statistics, quotations, people, results, or historical details.

## Fact-check prompt

Run this after editing the narration:

> Audit `beat_sheet.json` beat by beat. Extract every factual, numerical, historical, and
> technical claim. Check each against the strongest available primary source. Produce a table
> with beat ID, claim, verdict (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source,
> and required correction. Flag examples that must be labeled illustrative, claims that may date
> quickly, missing citations, causal language supported only by correlation, and any visual that
> implies more than the evidence establishes. Do not silently repair the script: list every
> proposed change for human review.

## Build and review loop

You are the conductor; the machine performs the build. Claude cannot judge whether the finished
film works for an audience, so human review is a required part of the method. This project is
currently paused after step 3 below — steps 4 onward are outstanding.

1. **Research and scope:** one insight, one motivating mechanism (here: ExoMiner's explainable
   diagnostic branches, not AstroNet's dual-view split — a deliberately different mechanism from
   Ep.01, see `FACTCHECK.md`).
2. **Write the beat sheet:** open with the unresolved backlog problem, name the three impostor
   signal types, show the diagnostic-branch mechanism in real depth (three named tests, not a
   generic "AI classified it" gloss), close on the 301-planet result and its 2026 TESS extension.
3. **Fact-check:** `FACTCHECK.md` — every claim sourced against primary/official material; three
   explicit resolved decisions logged (no likeness photos, no real-archive stills by design, and
   which system's stats attach to which beat).
4. **Gate P — narration review:** see `PEDAGOGY.md`. **Not yet cleared** — outstanding human
   pedagogy pass required before audio generation.
5. **Generate local audio:** not yet run. Planned voice: Kokoro `af_heart` (series consistency
   with Ep.01).
6. **Compile the previz → final cut:** not yet run.
7. **Fill the pantry:** not applicable — no real-archive assets planned for this episode (see
   `FACTCHECK.md` "Resolved decisions" #2).
8. **Watch, refine, and repeat:** not yet reached.
9. **Final QC:** not yet reached.
10. **Publish only by human decision:** not applicable yet — nothing has been rendered.

## Beat-sheet and visual rules

- Audio is the clock. Once Kokoro audio exists, regenerate and remeasure it whenever narration
  changes; `estimated_duration_s` values in `beat_sheet.json` are pre-audio placeholders only.
- Prefer concept visuals over decorative interface footage.
- Keep each beat visually legible.
- This episode uses zero real-archive assets and zero paid generation by design (see
  `FACTCHECK.md` and `PROMPTS.md`) — every beat is an original Manim diagram or Remotion card.
- Keep the source project intact. Create a new folder for a substantially different version.

## Voice and persona

- **Heart — `af_heart`:** planned narration voice for this episode (matches Ep.01).

## Useful project files

- `beat_sheet.json` — narrative and visual plan; pre-audio estimated durations only, not yet built
- `SHOTLIST.md` — beat-by-beat breakdown, shot type per beat, approval checklist (unchecked)
- `FACTCHECK.md` — claim-level evidence, verdicts, and resolved wording/scope decisions
- `PROMPTS.md` — record that no Higgsfield stills were drafted for this episode, and why
- `PEDAGOGY.md`, `STATUS.md` — narration gate note (currently PENDING) and current build state
- `scenes.py` — Manim scene source for the 11 GRAPHIC beats; written but not yet executed/rendered

## Final human checklist

- [ ] Can a new viewer state the question after the opening? (Why do thousands of Kepler
      candidates still need proof?)
- [ ] Does motion carry the explanation rather than merely decorate it? (The three diagnostic-
      branch beats should carry the actual mechanism, not just illustrate "AI checked it.")
- [ ] Is every important claim supported and every hypothetical labeled? (See `FACTCHECK.md`.)
- [ ] Does the payoff visibly resolve the opening case? (301 planets validated; ExoMiner++ scaling
      to TESS.)
- [ ] Has a human watched a complete draft and requested at least one refinement pass? **Not yet —
      this hasn't been built or watched by anyone.**

<!-- END BRUTALIST REBUILD GUIDE -->
