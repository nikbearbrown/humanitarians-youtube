<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# AI vs. the Data Deluge

## What this video is about

**Topic:** AI IN ASTRONOMY & SPACE SCIENCE

This is Humanitarians.

The current plan contains **18 beats**. Its runtime is measured from per-beat narration audio
(~1:47 of speech; full render with holds/transitions runs a little longer — see `STATUS.md`).
The source is: `SHOTLIST.md` and `FACTCHECK.md` in this folder.

Episode 01 of a planned weekly series covering AI applications across astronomy and space
science — chosen because it had zero overlap with any existing collection in this repository.
14 further topic ideas are scoped (exoplanet hunting deep-dive, gravitational wave detection,
galaxy classification, fast radio bursts, Mars rover autonomy, cosmological simulation, asteroid
tracking, image denoising, supernova classification, generative spacecraft design, solar storm
prediction, SETI signal detection, stellar spectra classification, satellite collision
avoidance) but not yet built.

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
branded variant rather than overwriting a finished plan.

Recommended builder: **`ai-explainer`** — one tight insight, single mechanism, single worked
example. That's exactly this video's shape (one discovery, one architecture detail, one
takeaway), not a multi-act documentary.

## Research prompt

Paste this into your research workflow before rewriting the video:

> Research **"AI vs. the Data Deluge"** for an educational explainer about **AI IN ASTRONOMY**.
> Start from the source links already logged in `FACTCHECK.md` in this folder, then locate primary sources, official documentation,
> peer-reviewed research, or original datasets. Identify the central question, one concrete key
> case, the mechanism that resolves it, important terminology, dated or version-sensitive claims,
> credible disagreements, limitations, and visual evidence suitable for animation. Return a claim
> table with: claim, exact source URL or citation, publication date, quoted or pinpoint evidence,
> confidence, and what must still be verified. Do not invent statistics, quotations, people,
> results, or historical details.

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
film works for an audience, so human review is a required part of the method.

1. **Research and scope:** one insight, one motivating case (here: Kepler-90i, discovered by a
   neural network in data every human reviewer had already passed over).
2. **Write or revise the beat sheet:** open with the unresolved case; show the mechanism in
   enough depth to be genuinely instructive (this build's second pass added the AstroNet
   dual-view CNN architecture specifically because the first cut was too generic — "there was a
   classification problem, ML solved it" isn't an insight); return to the opening case in the
   payoff.
3. **Fact-check:** `FACTCHECK.md` — every claim sourced, wording judgment calls (e.g. Rubin
   Observatory's 10TB-vs-20TB and 7M-vs-10M figures) resolved and explained, not silently picked.
4. **Gate P — narration review:** see `PEDAGOGY.md`. Content was human-approved upstream in
   `SHOTLIST.md`/`FACTCHECK.md` before audio generation.
5. **Generate local audio:** Kokoro voice `af_heart`. Measured audio durations became the master
   clock.
6. **Compile the previz → final cut:** all 18 beats filled (8 Manim, 7 Remotion, 3 real archive
   imagery/video) — no open slots, no Higgsfield spend (4 originally-approved paid stills were
   reassigned to free in-house builds before generation; see `FACTCHECK.md` "Resolved decisions").
7. **Fill the pantry:** rights-cleared real assets (NASA Kepler-90 image, NOIRLab Rubin photo and
   video) added with provenance logged in `FACTCHECK.md`.
8. **Watch, refine, and repeat.**
9. **Final QC:** verify captions, audio levels, credits (the two real-archive assets require
   exact, unaltered CC BY 4.0 credit lines — see `FACTCHECK.md`), and source disclosures.
10. **Publish only by human decision:** the toolkit builds locally and never treats a successful
    render as authorization to upload.

## Beat-sheet and visual rules

- Audio is the clock. Regenerate and remeasure audio when narration changes.
- Prefer concept visuals over decorative interface footage.
- Keep each beat visually legible.
- Generated or archival media needs provenance; this build uses two real, credited archive
  assets (NASA, NOIRLab) rather than generating stand-ins for things that already have a real,
  free, correctly-licensed source.
- Keep the source project intact. Create a new folder for a substantially different version.

## Voice and persona

- **Heart — `af_heart`:** narration voice for this episode.

## Useful project files

- `beat_sheet.json` — narrative and visual plan, the source of truth for the final render
- `SHOTLIST.md` — beat-by-beat breakdown, ≤28 words of VO per beat, shot type per beat
- `FACTCHECK.md` — claim-level evidence, verdicts, resolved wording decisions, and the required
  credit lines/rights info for every non-original asset (NASA, NOIRLab)
- `PROMPTS.md` — record of the Higgsfield stills that were approved, then never used
- `PEDAGOGY.md`, `STATUS.md` — narration gate note and current build state
- `scenes.py`, `media/`, `clips/`, `mp3/` — derived build/render artifacts (audio and video
  masters themselves are gitignored per repo policy; only manifests, timings, and small
  reconstructable assets are tracked)

## Final human checklist

- Can a new viewer state the question after the opening? (Why did every human reviewer miss
  Kepler-90i?)
- Does motion carry the explanation rather than merely decorate it? (The dual-view Manim beats
  carry the actual mechanism, not just illustrate a generic "AI" concept.)
- Is every important claim supported and every hypothetical labeled? (See `FACTCHECK.md`.)
- Does the payoff visibly resolve the opening case? (Kepler-90i confirmed, 8-planet system.)
- Did a human watch the complete output and request at least one refinement pass? (Yes — the
  first cut was flagged as too generic and the dual-view architecture depth was added as a
  direct result.)

<!-- END BRUTALIST REBUILD GUIDE -->
