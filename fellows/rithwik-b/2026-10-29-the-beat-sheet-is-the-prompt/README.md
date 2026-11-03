# The Beat Sheet Is the Prompt

Name a beat's parts (narration, show, scene) and explain why Brutalist generates audio first.

| | |
|---|---|
| **Runtime** | 2:50 (170.09 s) |
| **Format** | 30 fps · 16:9 · 3840×2160 |
| **Voice** | Kokoro `af_bella` — the series voice |
| **Beats** | 13 (B00–B12) · `ai-explainer` spine intact |
| **Brand** | `claude` · `@HumanitariansAI` |
| **Presenter** | Rithwik B. |
| **Series** | AI Fluency × Brutalist (film 2 of 6) |
| **Audience** | Humanitarians AI fellows who use Claude daily but have never built with the Brutalist toolkit |
| **Built** | 2026-10-29 · research and scripting Weeks 3–4 (see [HOURS.md](../HOURS.md)) |
| **GATE V** | 26 frames sampled · 0 BLOCKER · 0 MAJOR (0 MAJOR) |
| **Status** | Built · QC'd · fact-check drafted, **not signed** · review cut · **not published** |
| **Renders** | local review cut `ai-fluency/youtube/hai-beat-sheet-is-the-prompt/hai-beat-sheet-is-the-prompt-slate.mp4`; goes to the shared Drive with the final master |

## Through-line

The beat sheet is the prompt — every frame, word and second comes from one file.

## Beats

| Beat | Act | Scene | Opens with | Measured |
|---|---|---|---|---:|
| B00 | cold open | ClaudeComposerAsk | Ola, I'm Bella, for Humanitarians A I | 14.59 s |
| B01 | overview | BrutalistHesitantWriter | Here's the whole idea | 9.88 s |
| B02 | body | ShowTellCard · masked | Of all the A I fluency skills, this is the one people underrate | 14.76 s |
| B03 | body | ClaudeCodeBeat | Here's one real beat from film one | 14.49 s |
| B04 | body | ShowTellCard · focus | Read it like a spec | 14.14 s |
| B05 | body | ShowTellCard · paths | Because Brutalist is audio first | 14.51 s |
| B06 | body | ShowTellCard · chart | This is film one's actual clock | 16.83 s |
| B07 | worked example | ClaudeComposerAsk | Here's what happens when the description is incomplete | 12.12 s |
| B08 | worked example | ClaudeCodeBeat | One line fixed it | 13.91 s |
| B09 | when not to | ShowTellCard · search | Where this bites | 13.18 s |
| B10 | verdict | ShowTellCard · elastic | So, the verdict | 10.09 s |
| B11 | your turn | ClaudeComposerAsk | Your turn | 18.37 s |
| B12 | outro | ShowTellCard · layout | The Beat Sheet Is the Prompt | 3.22 s |

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
