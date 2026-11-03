# I Built Lemonade's Claims Bot — Here's What Production Would Actually Need

A **6:10** teaching walkthrough at **3840×2160**, built for Week 17's Lemonade
case study and its companion reference implementation.

Lemonade discloses claims *outcomes* richly (96% of first notice of loss taken
with no human, ~55% closed end to end) and claims *mechanism* thinly. So the
workflow got built anyway. The film walks that build one stage at a time —
Intake → Verification → Authorization Gate — and at each stage answers what
production would actually demand of it.

The teach isn't Lemonade's numbers. It's **four questions** the viewer can run
on anything they've built: what's mocked, what did I invent and does the code
admit it, what happens when it says no, and could I prove afterwards what
happened. Shown as a structure before any stage opens, visibly applied three
times, then handed over.

## Files

- **`lemonade-claims-bot.mp4`** — the final cut. Every beat holds on its
  finished frame for a full second before a hard cut into the next, giving the
  viewer time to read it. No crossfades.
- **`beat_sheet.json`** — the complete beat-by-beat build: narration, measured
  audio durations, and every Remotion component and prop used.
- **`FACTCHECK.md`** — the claim-by-claim audit: verdict, evidence, source and
  any correction applied, for every beat.
- **`07-lemonade-agentic-ai-insurtech-CASE-STUDY.md`** — the primary-sourced
  case study the film is built from. Every Lemonade figure traces here.
- **`PEDAGOGY.md`** — thesis, method, act structure, evidence discipline, the
  PROOF rubric score, and the GATE P sign-off.
- **`QC-REPORT.md`** — the full build log: every defect found by looking at
  frames, the PROOF checkpoint that sent the film back for rework, and the
  final verification.

This is a **deliverables-only** folder, matching the file set used across this
fellow's episodes. The working folder — the full narration script, the PROOF
review, 18 approved 4K frames, the reference implementation, the pacing script,
and ~144MB of per-beat renders, mp3s and conformed clips — is kept outside the
repo and deliberately not shipped here.

## The four questions

| # | Question | Answered at |
|---|---|---|
| 1 | **Dependencies** — what's mocked? | B04, B06 |
| 2 | **Invented values** — what did I make up, and does the code admit it? | B06, B07B, B08 |
| 3 | **Failure paths** — what happens when it says no? | B04 |
| 4 | **Accountability** — could you prove, afterwards, what happened and why? | B08 |

B09 lands the point: 43 green tests prove **none** of the four.

## Note on the pacing pass

The 1.0s hold before every cut is **not** part of the Brutalist toolkit's
`compile.py`, which is a hard-cut concat with no transition or pause mechanism
at all. It's a separate `ffmpeg` pass over `compile.py`'s own per-beat
conformed clips, and it must be re-run after any recompile — `compile.py`
overwrites the unpaced master and knows nothing about it.

The script itself lives with the working folder rather than here.

## Note before pushing

The `humanitarians-youtube` repo's `.gitignore` excludes `*.mp4` and `*.mp3`,
so **`git add` will silently skip the video.** Check with `git status` or
`git check-ignore -v lemonade-claims-bot.mp4` before assuming it was staged;
force it with `git add -f` if the video is meant to travel with the repo.

Never run a broad `git add .` here, and confirm the branch first — this is a
shared repo.

## Sourcing

Every factual claim is audited beat by beat in `FACTCHECK.md`. The confirmed
figures come from Lemonade's FY2025 Form 10-K (filed 25 February 2026); the
undisclosed settlement boundary is stated as an audited *absence* rather than
filled with a plausible number. Sofia is introduced — in narration and on
screen — as the case study's illustrative scenario, not a real customer.

Not depicted anywhere: computer-vision video analysis, any fraud-algorithm
count, or any dollar threshold attributed to Lemonade. None is confirmed as
current mechanism, and the video-analysis claim was retracted by Lemonade
itself in 2021.

Built with the [Brutalist](https://github.com/nikbearbrown/brutalist.art) free,
local video toolkit (Kokoro TTS + Remotion) — no paid APIs, no keys.
