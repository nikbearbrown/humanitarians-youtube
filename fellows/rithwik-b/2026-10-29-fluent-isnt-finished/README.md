# Fluent Isn't Finished

State the asymmetry (Claude builds, cannot watch) and sort build steps into Claude-owned vs human-owned.

| | |
|---|---|
| **Runtime** | 2:52 (171.82 s) |
| **Format** | 30 fps · 16:9 · 3840×2160 |
| **Voice** | Kokoro `af_bella` — the series voice |
| **Beats** | 13 (B00–B12) · `ai-explainer` spine intact |
| **Brand** | `claude` · `@HumanitariansAI` |
| **Presenter** | Rithwik B. |
| **Series** | AI Fluency × Brutalist (film 1 of 6) |
| **Audience** | Humanitarians AI fellows who use Claude daily but have never built with the Brutalist toolkit |
| **Built** | 2026-10-29 · research and scripting Weeks 1–2 (see [HOURS.md](../HOURS.md)) |
| **GATE V** | 26 frames sampled · 0 BLOCKER · 0 MAJOR (8 → 1 → 2 → 0 MAJOR across four compiles) |
| **Status** | Built · QC'd · fact-check drafted, **not signed** · review cut · **not published** |
| **Renders** | local review cut `ai-fluency/youtube/hai-fluent-isnt-finished/hai-fluent-isnt-finished-slate.mp4`; goes to the shared Drive with the final master |

## Through-line

Claude can build the video but can't watch it — fluency is knowing which calls stay yours.

## Beats

| Beat | Act | Scene | Opens with | Measured |
|---|---|---|---|---:|
| B00 | cold open | cold open | Hi, I'm Bella, for Humanitarians A I | 13.50 s |
| B01 | overview | BLUF | Here's the whole idea | 13.33 s |
| B02 | body | body | Start with what the machine is great at | 15.72 s |
| B03 | body | body | But the whole toolkit rests on one asymmetry | 15.10 s |
| B04 | body | body | So Brutalist splits the work along that line | 15.51 s |
| B05 | body | body | Sort the steps and the split gets obvious | 13.82 s |
| B06 | body | body | That's how the two ideas fit | 15.98 s |
| B07 | worked example | worked example (ask) | Here's a real receipt, from building this series | 14.44 s |
| B08 | worked example | worked example (result) | And then the toolkit stopped it | 13.65 s |
| B09 | when not to | when not to | Where this bites: the gates slow you down | 11.07 s |
| B10 | verdict | verdict | So, the verdict | 8.79 s |
| B11 | your turn | your turn | Your turn | 18.03 s |
| B12 | outro | outro | Fluent isn't finished | 2.88 s |

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
SERIES-PLAN.md               audience, outcome and spine for the whole series
.gitignore                   renders out, build inputs in
```

**Not here** — the renders: review cut, narration `mp3/`, beat `clips/`, `media/`.

## Open before publication

1. Sign [`FACTCHECK-DRAFT.md`](FACTCHECK-DRAFT.md), then `./art final` for the clean master.
2. Watch and listen to the whole cut once, end to end — frame QC so far was on stills.
3. Channel — `@HumanitariansAI`; confirm before upload.
