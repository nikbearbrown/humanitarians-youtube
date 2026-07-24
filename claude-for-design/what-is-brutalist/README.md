# What is Brutalist? — the intro video

The first video in the **"Brutalist — Claude for Video Production"** playlist on
[@HumanitariansAI](https://www.youtube.com/@HumanitariansAI). It argues the conductor idea — *you decide,
the machine plays* — and shows the real terminal workflow. Meta by design: it's made **by** the
toolkit, **about** the toolkit. The narration is the repo `README.md` in spoken form.

## What's here

- `beat_sheet.json` — the heart. 16 beats, ~2.8 min, audio-first (narration is the clock). Intercuts
  concept animations (Manim) with live terminal scenes (Remotion): `art fill-in`, `./setup`,
  `art --list / todo / run`. Validated against `runtime/schema/beat_sheet.schema.json`.

## A self-contained folder

Everything for this video lives in this one folder — the beat sheet, the rendered scenes
(`manim/`, `media/`), the audio (`mp3/`), the compiled cut, and the derived ledger (`todo.json`,
`STATUS.md`). You can copy the folder, point the pipeline at it, and it builds in place; nothing
reaches outside it except the shared `runtime/`. One folder = one video.

## Rebuild it

Claude Code runs the whole build — you don't render scenes by hand. Point it at this folder:

```bash
# from the repo root
./art todo    youtube/what-is-brutalist          # the beat ledger — what each beat needs
./art fill-in youtube/what-is-brutalist           # render every pipeline beat (all 16 here)
./art run     youtube/what-is-brutalist           # compile the cut
```

Then swap the narration and beats for your own and run again.

## The render contract (retry, then hand back to you)

When Claude Code renders a scene it **retries up to five times**, fixing its own errors between
attempts. If a scene still won't render after five tries, it **leaves that beat unrendered and moves
on to the next one** rather than stalling the whole build — the beat shows up as a slate in the cut
and stays flagged in `todo.json`/`STATUS.md`. So a finished pass can legitimately contain a few
missing or rough beats.

That's by design: **the human is expected to look at the result and redo some scenes.** Watch the
cut, find the beats that came out unrendered or just bad, and rebuild only those — adjust the beat's
spec in `beat_sheet.json` (the heart) and re-run `fill-in` on it, or fix the scene and re-render.
Running unattended (e.g. `claude --dangerously-skip-permissions`) is fine and fast, but it means
exactly this: the machine gets you a full draft with a few beats left for your judgment, and you
finish the ones only a human should. That review-and-redo pass *is* the human's job — see
`runtime/README.md` for the general contract.

## A note on the labor split (this video proves it)

Run `./art todo` and every beat reports `pipeline` — **zero human beats.** This explainer is
entirely machine-buildable: concept animations and terminal scenes are exactly what Manim and
Remotion are superhuman at. So `fill-in` renders all of it and leaves no request cards.

Which means the human's entire contribution to *this* video is the part only a human can do:
writing and approving the narration (the script), judging the pacing, and watching the finished cut
to decide whether it lands. The score is yours; the playing is the machine's. That is the video's
whole argument, demonstrated by how the video itself gets made.

*Narration needs `ELEVENLABS_API_KEY` + the NikBearBrown voice (`ELEVENLABS_VOICE_NIKBEARBROWN`).
The silent cut (slates/terminal scenes, no VO) builds with no keys.*

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# What is Brutalist?

## What this video is about

**Topic:** CLAUDE FOR VIDEO PRODUCTION

This is Kore for Humanitarians AI.

The current plan contains **20 beats**. Its runtime is 214.96. The source recorded by the project is: See the local source and fact-check files.

## Make your own version

Download the free local toolkit:

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

The toolkit uses local Kokoro narration and does not require an API key. The beat sheet is the source of truth: one beat per moment, with narration, visual intent, and shot instructions. For this project, start with `beat_sheet.json`. Preserve it before experimenting; make a copy or a branded variant rather than overwriting a finished plan.

Recommended builder: **`ai-explainer`**. Use `ai-explainer` for one tight insight, `cli-explainer` when the prompt → real code → moving output → revision loop is the subject, and `deep-explainer` for a multi-act 5–10 minute documentary.

## Research prompt

Paste this into your research workflow before rewriting the video:

> Research **“What is Brutalist?”** for an educational explainer about **CLAUDE FOR VIDEO PRODUCTION**. Start from the source noted in this folder, then locate primary sources, official documentation, peer-reviewed research, standards, or original datasets. Identify the central question, one concrete key case, the mechanism that resolves it, important terminology, dated or version-sensitive claims, credible disagreements, limitations, and visual evidence suitable for animation. Return a claim table with: claim, exact source URL or citation, publication date, quoted or pinpoint evidence, confidence, and what must still be verified. Do not invent statistics, quotations, people, results, or historical details.

## Fact-check prompt

Run this after editing the narration:

> Audit `beat_sheet.json` beat by beat. Extract every factual, numerical, historical, legal, medical, scientific, and product/version claim. Check each against the strongest available primary source. Produce a table with beat ID, claim, verdict (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, and required correction. Flag examples that must be labeled illustrative, claims that may date quickly, missing citations, causal language supported only by correlation, and any visual that implies more than the evidence establishes. Do not silently repair the script: list every proposed change for human review.

## Build and review loop

You are the conductor; the machine performs the build. Claude cannot judge whether the finished film works for an audience, so human review is a required part of the method.

1. **Research and scope:** choose one insight and one motivating case. Split unrelated insights into separate videos.
2. **Write or revise the beat sheet:** open with the unresolved case; show at least two concrete moving instances before abstraction; return to the opening object in the payoff; end with a boundary and one viewer exercise.
3. **Fact-check:** create or update `FACTCHECK.md`. Mark unresolved claims with `[VERIFY: …]`; never fill gaps by guessing.
4. **Gate P — narration review:** read every line aloud and review it on an animated slate. Record the human verdict in `PEDAGOGY.md`. Do not generate final audio until the narration passes.
5. **Generate local audio:** use Kokoro voice `af_kore` in the Pragmatist register. Measured audio durations become the master clock; never repair timing by hand.
6. **Compile the previz:** render what can be generated locally. Missing stills or footage should remain honest labeled slates.
7. **Fill the pantry:** add rights-cleared images or footage to `pantry/`, include source/provenance sidecars, then rebuild only changed slots.
8. **Watch, refine, and repeat:** check pacing, comprehension, joke timing, typography, captions, transitions, factual implications, and whether each visual teaches the spoken point.
9. **Final QC:** verify type size, overflow, contrast, caption timing, audio levels, credits, source disclosures, and that the clean master contains no review burn-ins.
10. **Publish only by human decision:** the toolkit builds locally and never treats a successful render as authorization to upload.

Typical commands from the toolkit root:

```bash
# Review the relevant skill before editing the plan
./art ai-explainer --help

# After the human signs Gate P
python3 runtime/scripts/generate_audio_kokoro.py "/absolute/path/to/this/project"

# Review cut, missing-asset list, then clean master
./art run "/absolute/path/to/this/project"
./art todo "/absolute/path/to/this/project"
./art final "/absolute/path/to/this/project"
```

## Beat-sheet and visual rules

- Audio is the clock. Regenerate and remeasure audio when narration changes.
- Prefer concept visuals over decorative interface footage.
- Use actual code in CLI videos; never substitute pseudocode while claiming it is the generated program.
- Keep each beat visually legible—roughly six or fewer simultaneous elements.
- Generated or archival media needs provenance; real people and events should use appropriately licensed archives where possible.
- Deep explainers should mix Vox-style still beats, Manim, and Remotion rather than becoming an all-slide or all-stock-footage cut.
- Consecutive Vox stills may share a short continuity run; do not force continuity across the entire film.
- The first complete compile is a previz, not a finished video.
- Keep the source project intact. Create a new folder for a substantially different version or persona.

## Voice and persona options

- **Kore — `af_kore`:** Humanitarians AI presenter register; analytical, design-critical, concise.
- **Bella — `af_bella`:** Humanitarians AI pragmatist register; method, use cases, and explicit boundaries.

For Humanitarians AI productions, Kore is the default presenter and the opening and closing should identify Kore as “in for Humanitarians AI.” Persona variants belong in new `nbb-` or `hai-` folders and must not overwrite the source reel.

## Useful project files

- `beat_sheet.json` — narrative and visual plan
- `PEDAGOGY.md` — narration gate and human approval
- `FACTCHECK.md` — claim-level evidence and corrections
- `BUILD-PROMPT.md` / `BUILD-LOG.md` — reproducible build instructions and decisions
- `SHOPPING.md` — duration-locked pantry needs for deep explainers
- `SOURCES.md` — research, rights, licenses, and credits
- `pantry/` — human-supplied source assets
- `media/`, `manim/`, `clips/`, `mp3/` — derived build artifacts

## Final human checklist

- Can a new viewer state the question after the opening?
- Does motion carry the explanation rather than merely decorate it?
- Is every important claim supported and every hypothetical labeled?
- Can the viewer distinguish evidence, interpretation, and opinion?
- Does the payoff visibly resolve the opening case?
- Is the “Your Turn” prompt concrete enough to use immediately?
- Did a human watch the complete output and request at least one refinement pass?

<!-- END BRUTALIST REBUILD GUIDE -->
