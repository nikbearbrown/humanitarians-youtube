# Look at the Frames

Read a QC report and contact sheet and classify a defect as blocker, major, or fine.

| | |
|---|---|
| **Runtime** | 2:48 (167.71 s) |
| **Format** | 30 fps · 16:9 · 3840×2160 |
| **Voice** | Kokoro `af_bella` — the series voice |
| **Beats** | 13 (B00–B12) · `ai-explainer` spine intact |
| **Brand** | `claude` · `@HumanitariansAI` |
| **Presenter** | Rithwik B. |
| **Series** | AI Fluency × Brutalist (film 3 of 6) |
| **Audience** | Humanitarians AI fellows who use Claude daily but have never built with the Brutalist toolkit |
| **Built** | 2026-10-29 · research and scripting Weeks 5–6 (see [HOURS.md](../HOURS.md)) |
| **GATE V** | 26 frames sampled · 0 BLOCKER · 0 MAJOR (1 → 0 MAJOR) |
| **Status** | Built · QC'd · fact-check drafted, **not signed** · review cut · **not published** |
| **Renders** | local review cut `ai-fluency/youtube/hai-look-at-the-frames/hai-look-at-the-frames-slate.mp4`; goes to the shared Drive with the final master |

## Through-line

Look at the frames — a passing gate is not a finished film.

## Beats

| Beat | Act | Scene | Opens with | Measured |
|---|---|---|---|---:|
| B00 | cold open | ClaudeComposerAsk | Hej, I'm Bella, for Humanitarians A I | 12.63 s |
| B01 | overview | BrutalistHesitantWriter | Here's the whole idea | 11.22 s |
| B02 | body | ShowTellCard · player | A rendered video feels finished | 14.29 s |
| B03 | body | ShowTellCard · focus | So the toolkit looks first | 16.81 s |
| B04 | body | ShowTellCard · chart | Film one's first cut failed | 15.02 s |
| B05 | body | ShowTellCard · tabs | But the gate isn't the whole review | 13.97 s |
| B06 | body | ShowTellCard · paths | And when the machine honestly can't make a visual, Brutalist doesn't… | 14.78 s |
| B07 | worked example | ClaudeComposerAsk | Here's the receipt | 11.35 s |
| B08 | worked example | ClaudeCodeBeat | It took four compiles to get to zero | 13.85 s |
| B09 | when not to | ShowTellCard · search | Where this bites | 12.50 s |
| B10 | verdict | ShowTellCard · elastic | So, the verdict | 8.38 s |
| B11 | your turn | ClaudeComposerAsk | Your turn | 20.16 s |
| B12 | outro | ShowTellCard · layout | Look at the Frames | 2.75 s |

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
.gitignore                   renders out, build inputs in
```

**Not here** — the renders: review cut, narration `mp3/`, beat `clips/`, `media/`.

## Open before publication

1. Sign [`FACTCHECK-DRAFT.md`](FACTCHECK-DRAFT.md), then `./art final` for the clean master.
2. Watch and listen to the whole cut once, end to end — frame QC so far was on stills.
3. Channel — `@HumanitariansAI`; confirm before upload.
