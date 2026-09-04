<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# Wrong, Safely.

## What this video is about

**Topic:** IRREDUCIBLY HUMAN · AGENT SYSTEM DESIGN

Made by Mubin Modi. Published on **@HumanitariansAI**.

An explainer on how agentic systems work in production, taught through one worked
example: a rescheduling agent asked to move a Tuesday appointment to Thursday
afternoon. The single insight the video lands is that **an agent fails because the
model acted and no one checked — so the engineering job is oversight, not a smarter
model.**

**9 beats · 2:40 runtime · 4K (3840×2160) · Kokoro `am_onyx`, free and local.**

The body walks four layers (agent proposes → code validates → human approves → tool
runs), sends one real sentence through them, shows the typed tool contract that makes
validation possible, and closes on the failure that survives all of it: a trace where
every step returns clean, the final message reads correctly, and a policy check was
never evaluated.

Source: `agent-storyboard-production-package.md` — "The Reschedule", an 8:10 storyboard
by Mubin Modi. This reel is the `ai-explainer` compression of it to one insight; the
full 13-scene arc remains a `deep-explainer` candidate.

## Make your own version

Download the free local toolkit:

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

The toolkit uses local Kokoro narration and does not require an API key. The beat
sheet is the source of truth: one beat per moment, with narration, visual intent, and
shot instructions. For this project, start with `beat_sheet.json`. Preserve it before
experimenting; make a copy or a branded variant rather than overwriting a finished
plan.

Recommended builder: **`ai-explainer`**. Use `ai-explainer` for one tight insight,
`cli-explainer` when the prompt → real code → moving output → revision loop is the
subject, and `deep-explainer` for a multi-act 5–10 minute documentary.

## Research prompt

Paste this into your research workflow before rewriting the video:

> Research **"Wrong, Safely."** for an educational explainer about **agent system
> design in production**. Start from the storyboard noted in this folder, then locate
> primary sources: vendor agent-design documentation, published post-mortems of agent
> failures in production, human-in-the-loop and approval-gate literature, tool-calling
> and structured-output specifications, and work on trace-level versus final-answer
> evaluation. Identify the central question, one concrete key case, the mechanism that
> resolves it, important terminology, dated or version-sensitive claims, credible
> disagreements, limitations, and visual evidence suitable for animation. Return a
> claim table with: claim, exact source URL or citation, publication date, quoted or
> pinpoint evidence, confidence, and what must still be verified. Do not invent
> statistics, quotations, people, results, or historical details.

## Fact-check prompt

Run this after editing the narration:

> Audit `beat_sheet.json` beat by beat. Extract every factual, numerical, historical,
> legal, medical, scientific, and product/version claim. Check each against the
> strongest available primary source. Produce a table with beat ID, claim, verdict
> (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, and required
> correction. Flag examples that must be labeled illustrative, claims that may date
> quickly, missing citations, causal language supported only by correlation, and any
> visual that implies more than the evidence establishes. Do not silently repair the
> script: list every proposed change for human review.

Note for this reel: it asserts no external empirical facts. Its claims are design
claims drawn from the author's own worked example, and the one figure on screen (a
24-hour rescheduling policy) is presented as an illustration, not an industry
statistic. See `SOURCES.md`.

## Build and review loop

You are the conductor; the machine performs the build. Claude cannot judge whether the
finished film works for an audience, so human review is a required part of the method.

1. **Research and scope:** choose one insight and one motivating case. Split unrelated
   insights into separate videos.
2. **Write or revise the beat sheet:** open with the unresolved case; show at least two
   concrete moving instances before abstraction; return to the opening object in the
   payoff; end with a boundary and one viewer exercise.
3. **Fact-check:** create or update `FACTCHECK.md`. Mark unresolved claims with
   `[VERIFY: …]`; never fill gaps by guessing.
4. **Gate P — narration review:** read every line aloud and review it on an animated
   slate. Record the human verdict in `PEDAGOGY.md`.
5. **Generate local audio:** measured audio durations become the master clock; never
   repair timing by hand.
6. **Compile the previz:** render what can be generated locally. Missing stills or
   footage should remain honest labeled slates.
7. **Fill the pantry:** this reel needs none — all nine beats are code-rendered.
8. **Watch, refine, and repeat:** check pacing, comprehension, typography, captions,
   transitions, factual implications, and whether each visual teaches the spoken point.
9. **Final QC:** verify type size, overflow, contrast, caption timing, audio levels,
   credits, and that the clean master contains no review burn-ins.
10. **Publish only by human decision:** the toolkit builds locally and never treats a
    successful render as authorization to upload.

Typical commands from the toolkit root:

```bash
./art ai-explainer --help
python3 runtime/scripts/generate_audio_kokoro.py "/absolute/path/to/this/project"
./art run   "/absolute/path/to/this/project"
./art todo  "/absolute/path/to/this/project"
./art final "/absolute/path/to/this/project"
```

`./art run` burns per-beat markers (`B03 REMOTION VIDEO 45.9s +17.1s`) into the footer
— that is the review cut. `./art final` is the clean master and carries none.

## Beat-sheet and visual rules

- Audio is the clock. Regenerate and remeasure audio when narration changes.
- Prefer concept visuals over decorative interface footage. The Claude UI appears only
  at the cold open, the handoff, the verdict page and the outro (ILLUSTRATE LAW).
- Keep each beat visually legible — roughly six or fewer simultaneous elements.
- The first complete compile is a previz, not a finished video.
- Keep the source project intact. Create a new folder for a substantially different
  version or persona.

### Two timing traps this reel hit — read before reusing these components

- **A composition registered longer than its beat loses its tail.** The renderer emits
  the composition's registered length and the clip is then trimmed to the measured
  audio. On a 20s beat against a 30s composition, only the first two-thirds survive —
  here that silently deleted the failure flip that the whole falsifiability beat exists
  to show. Fixed upstream: `remotion_scenes.py` now passes `__beatDurationS` and
  `illustrations/kit.tsx` `useP()` normalizes progress against the beat.
- **`BrutalistHesitantWriter` matches `triggerWords` per whitespace token**, so a
  multi-word phrase never matches and the correction never fires. It also builds its own
  timeline from `charMs` and does not read the beat clock — tune `charMs` so the whole
  performance, corrections included, fits inside the measured audio.

## Voice and persona

- **Onyx — `am_onyx`:** the voice used here. Free, local, no account.
- **Bella — `af_bella`** and **Kore — `af_kore`** are the other Humanitarians AI
  registers.

This reel is narrated in the **Teardown** register for practitioners rather than the
Pragmatist/student register `ai-explainer` assigns the HAI channel by default. That is a
recorded deviation, not an oversight — see `metadata.deviations_from_house_default` in
`beat_sheet.json`. Converting it is a narration rewrite across all nine beats.

## Useful project files

- `beat_sheet.json` — narrative and visual plan (the source of truth)
- `mubin-wrong-safely-data.json` — flattened player manifest: per-beat kind, frame
  count at 30fps, audio path and props
- `mp3/` — measured narration, one file per beat, plus `timings.json`
- `BUILD-PROMPT.md` — the paste-ready prompt that rebuilds this end to end
- `CHECKS-REPORT.md` — PROOF GATE record and frame-law compliance
- `DESIGN-CARDS.md` — the one GATE L punt and the component built to close it
- `SOURCES.md` — source, what was rewritten, what was cut, determinism record
- `_qc/AUTHORING-QC.md` — human QC log: eight defects found, all fixed
- `_qc/REPORT.md` — machine GATE V output (regenerated every run)
- `media/` — per-beat rendered video

## Known open item

GATE V reports 0 BLOCKER and 10 MAJOR `underfill` warnings. The check requires ink to
cover ≥55% of the title-safe area measured as a *bounding-box area*, which no
text-centric house component can reach — the title outro scores 4%, the hesitant writer
6%, the verdict card 54%. The cuts in this folder were produced with `ART_STRICT=0`,
which downgrades those to warnings. That is disclosed, not silently passed; see
`_qc/AUTHORING-QC.md` for the three ways to resolve it.

## Final human checklist

- Can a new viewer state the question after the opening?
- Does motion carry the explanation rather than merely decorate it?
- Is every important claim supported and every hypothetical labeled?
- Does the payoff visibly resolve the opening case?
- Is the "Your Turn" prompt concrete enough to use immediately?
- Did a human watch the complete output and request at least one refinement pass?

<!-- END BRUTALIST REBUILD GUIDE -->
