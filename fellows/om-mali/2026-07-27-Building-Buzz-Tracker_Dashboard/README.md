# Weekly Research Report: Building the Buzz Tracker Dashboard

**Fellow:** Om Mali
**Week ending:** July 26, 2026
**Video title:** "Turning Hacker News Talk Into an AI Attention Signal"
**Project:** Mycroft — an experiment in using AI to invest in AI
**Source:** the author's own n8n workflow, Postgres database, and dashboard (own project, no
external source — see `SOURCES.md`)

This is a real fellow's real progress showcase, not a fictional demonstration (contrast with the
`fellows/maya-r/` example series, which is explicitly fictional). It documents week 8 of Mycroft:
an n8n agent that turns free public Hacker News discussion into a 0–100 Buzz Score per AI
company, plus a Groq-generated, comment-grounded Community Opinion read — and this week's
specific addition, the AI Buzz Tracker dashboard.

The beat sheet contains 19 beats (B00–B18): a cold open, the motivating hypothesis, one
architecture map, a six-beat pipeline walkthrough (fetch → score → comments), a sector-narrative
safety check, four dashboard/status beats, a two-beat honest limitation ("the misattribution
finding"), and an outro naming the next fix. All 19 beats are filled — 4 Remotion
cards/graphics, 15 real screenshot stills of the author's own workflow and dashboard.

## Production state

- Build: complete — 19/19 beats filled, Kokoro voice `am_onyx`, cut = master (see `BUILD-LOG.md`)
- Gate P (narration/pedagogy structure): PASS (see `PEDAGOGY.md`)
- Fact-check gate: **author confirmation still needed** — every claim describes the author's own
  private system and can only be verified by Om Mali, not by an external source (see
  `FACTCHECK.md`)
- Publishing: not authorized

## What's not in this repo copy, and why

The rendered MP4 (`hn-buzz-signal.mp4`), the per-beat narration `mp3` files, and the per-beat
rendered `clips/B*.mp4`/`media/*.mp4` files were left out of this checked-in copy. They're large,
regenerable from `beat_sheet.json` plus the assets that *are* here, and every other project in
this repository keeps the same kind of files out for the same reason (this repo's `.gitignore`
excludes `*.mp3`/`*.mp4`). The original full build, including the rendered video, still exists at
the source production location outside this repository.

`TYPECHECK.md` (a typography/kerning gate from the original build) was also left out — it isn't
part of any established convention seen elsewhere in this repository (not in `claude-for-*`
projects, not in the other `fellows/` reports). It's available in the original build folder if a
future reviewer wants it restored.

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

# Weekly Research Report: Building the Buzz Tracker Dashboard

## What this video is about

**Topic:** Om Mali — Mycroft (AI Sector Attention Signal)

This is a progress showcase for a professor/project review audience: what does it take to turn
free, public Hacker News discussion into a structured, comment-grounded attention signal for the
AI sector — and what does the dashboard built on top of it actually show?

The current plan contains **19 beats**. Its runtime is measured from per-beat narration audio
(~5:32 summed from `actual_duration_s` across all 19 beats). The source recorded by the project
is the author's own system — see `SOURCES.md` and `FACTCHECK.md`.

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

Recommended builder: **`cli-explainer`** — the subject is a real pipeline (prompt/workflow → real
code and data → a real bug, a real fix, a real limitation), not an abstract single insight or a
multi-act documentary.

## Research prompt

Paste this into your research workflow before rewriting the video:

> Research **"Turning Hacker News Talk Into an AI Attention Signal"** for a progress-showcase
> explainer about **Om Mali's Mycroft project**. Start from `SOURCES.md` in this folder — the
> only source is the author's own system. Identify the central question, the mechanism, the real
> bug/fix pair, the real limitation found in production, and what still needs the author's
> confirmation before publishing. Do not invent statistics, run counts, or outcomes beyond what
> `beat_sheet.json` and `FACTCHECK.md` already state.

## Fact-check prompt

Run this after editing the narration:

> Audit `beat_sheet.json` beat by beat against `FACTCHECK.md`. This project has no external
> source — every claim describes a private system, so verification means confirming each
> author-asserted claim with Om Mali directly, not searching for a public citation. Flag any
> claim that reads as more certain or more impressive than what the author has actually
> confirmed.

## Build and review loop

1. **Research and scope:** one system (Mycroft), one week's addition (the dashboard), framed
   against the pipeline that came before it.
2. **Write or revise the beat sheet:** open with what the system does today; show the real
   architecture; walk the pipeline concretely (named nodes, named example); end with an honest,
   unresolved limitation and a named next fix — not a tidy "it's solved" ending.
3. **Fact-check:** `FACTCHECK.md` — every claim listed individually for the author to confirm,
   since nobody else has access to the private system being described.
4. **Gate P — narration review:** see `PEDAGOGY.md` (PASS — carried over from the original
   build).
5. **Generate local audio:** Kokoro voice `am_onyx`. Measured audio durations are the master
   clock.
6. **Compile the previz → final cut:** all 19 beats filled, no open slots.
7. **Fill the pantry:** all 15 STILL beats use the author's own screenshots (`pantry/`), which
   need no external rights clearance — see `SOURCES.md`.
8. **Watch, refine, and repeat.**
9. **Final QC:** confirm every author-asserted claim in `FACTCHECK.md` before authorizing a
   render for review.
10. **Publish only by human decision:** not authorized yet.

## Voice

- **Onyx — `am_onyx`:** Om Mali's chosen Kokoro voice for this report series, per the
  male-coded-name default described in `fellows/README.md` (the fellow's stated preference always
  overrides the name-based suggestion; this is the fellow's actual choice, already reflected in
  `beat_sheet.json`).

## Useful project files

- `beat_sheet.json` — narrative and visual plan, the source of truth for the render
- `FACTCHECK.md` — every claim listed for the author's confirmation (not externally sourced —
  see why at the top of that file)
- `SOURCES.md` — asset provenance (own-work screenshots, no external licensing needed)
- `BUILD-PROMPT.md` / `BUILD-LOG.md` — build instructions and what's already been done
- `PEDAGOGY.md` — narration-structure gate (PASS)
- `pantry/` — the author's own source screenshots
- `media/`, `clips/`, `mp3/` — derived build artifacts (manifests, timings, small stills;
  audio/video masters themselves are gitignored per repo policy)

## Final human checklist

- Can a new viewer state the question after the opening? (Does argument volume on Hacker News
  lead attention on AI companies?)
- Does motion carry the explanation rather than merely decorate it? (Each pipeline beat shows the
  actual workflow screenshot with the actual nodes named in narration.)
- Is every important claim supported and every hypothetical labeled? (See `FACTCHECK.md` — all 12
  rows need the author's own confirmation.)
- Does the payoff visibly resolve the opening case? (The dashboard, shown in B12–B15, is the
  concrete result of the pipeline walked through in B02–B11.)
- Is the limitation honestly presented, not smoothed over? (B16–B17 present a real
  misattribution bug and an unresolved gap, not a solved problem.)
- Did a human (Om Mali specifically) confirm every author-asserted claim before this is cleared
  to publish?

<!-- END BRUTALIST REBUILD GUIDE -->
