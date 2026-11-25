# The Workflow Is the Lesson

Map an AI-assisted workflow as steps and mark which the machine runs and where a person must check.

| | |
|---|---|
| **Runtime** | 2:55 (175.21 s) |
| **Format** | 30 fps · 16:9 · 3840×2160 |
| **Voice** | Kokoro `af_bella` — the series voice |
| **Beats** | 13 (B00–B12) · `ai-explainer` spine intact |
| **Brand** | `claude` · `@HumanitariansAI` |
| **Presenter** | Rithwik B. |
| **Series** | AI Fluency × Brutalist (film 6 of 6) |
| **Audience** | Humanitarians AI fellows who use Claude daily but have never built with the Brutalist toolkit |
| **Built** | 2026-10-30 · research and scripting Weeks 11–12 (see [HOURS.md](../HOURS.md)) |
| **GATE V** | 26 frames sampled · 0 BLOCKER · 0 MAJOR (0 MAJOR) |
| **Status** | Built · QC'd · fact-check drafted, **not signed** · review cut · **not published** |
| **Renders** | local review cut `ai-fluency/youtube/hai-workflow-is-the-lesson/hai-workflow-is-the-lesson-slate.mp4`; goes to the shared Drive with the final master |

## Through-line

The workflow is the lesson — the machine runs the steps, you stand at the checks.

## Beats

| Beat | Act | Scene | Opens with | Measured |
|---|---|---|---|---:|
| B00 | cold open | ClaudeComposerAsk | Jambo, I'm Bella, for Humanitarians A I | 14.25 s |
| B01 | overview | BrutalistHesitantWriter | Here's the whole idea | 11.99 s |
| B02 | body | ShowTellCard · masked | This A I fluency skill isn't about any single prompt | 13.82 s |
| B03 | body | ShowTellCard · paths | Here's the Brutalist loop | 14.74 s |
| B04 | body | ShowTellCard · tabs | Sort them | 16.13 s |
| B05 | body | ShowTellCard · focus | What made it repeatable? | 15.23 s |
| B06 | body | ShowTellCard · chart | And the workflow got cheaper | 15.19 s |
| B07 | worked example | ClaudeComposerAsk | Here's the real run | 14.55 s |
| B08 | worked example | ClaudeCodeBeat | Here's the script itself | 15.32 s |
| B09 | when not to | ShowTellCard · search | Where this bites | 11.48 s |
| B10 | verdict | ShowTellCard · elastic | So, the verdict | 9.56 s |
| B11 | your turn | ClaudeComposerAsk | Your turn | 19.71 s |
| B12 | outro | ShowTellCard · layout | The Workflow Is the Lesson | 3.24 s |

## Fact-check

Drafted, not signed — see [`FACTCHECK-DRAFT.md`](FACTCHECK-DRAFT.md). Every factual row
traces to the series build log or a file in the toolkit; judgment rows are framed as
advice on camera. The final master compiles only after the draft is checked and renamed
`FACTCHECK.md` (GATE F).

## What is in this folder

```
beat_sheet.json              every beat: narration, show events, scene, measured duration
timings.json                 the measured clock, per beat
README.md                    this file
FACTCHECK-DRAFT.md           every claim, its source, its verdict — awaiting sign-off
SOURCES.md                   provenance and toolchain
SHOTLIST.md                  scene per beat
PROMPTS.md                   the viewer handoff prompt read aloud in the film
QC-REPORT.md                 gate result + the defects found by frame review
qc-contact-sheet.png         GATE V contact sheet
BUILD-PROMPT.md              paste-ready rebuild
FRICTIONAL.md                the process log for this piece of work
description.txt              YouTube description + validated chapters
scripts/build_films.py       generator for films 2–4 (the film's worked example)
scripts/build_films_5_6.py   generator for films 5–6
.gitignore                   renders out, build inputs in
```

**Not here** — the renders: review cut, narration `mp3/`, beat `clips/`, `media/`.

## Open before publication

1. Sign [`FACTCHECK-DRAFT.md`](FACTCHECK-DRAFT.md), then `./art final` for the clean master.
2. Watch and listen to the whole cut once, end to end — frame QC so far was on stills.
3. Channel — `@HumanitariansAI`; confirm before upload.
