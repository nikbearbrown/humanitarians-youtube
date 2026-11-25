# Trust, Then Verify

Decide which claims in a script need a source before the final cut, and who signs for them.

| | |
|---|---|
| **Runtime** | 2:47 (167.24 s) |
| **Format** | 30 fps · 16:9 · 3840×2160 |
| **Voice** | Kokoro `af_bella` — the series voice |
| **Beats** | 13 (B00–B12) · `ai-explainer` spine intact |
| **Brand** | `claude` · `@HumanitariansAI` |
| **Presenter** | Rithwik B. |
| **Series** | AI Fluency × Brutalist (film 4 of 6) |
| **Audience** | Humanitarians AI fellows who use Claude daily but have never built with the Brutalist toolkit |
| **Built** | 2026-10-29 · research and scripting Weeks 7–8 (see [HOURS.md](../HOURS.md)) |
| **GATE V** | 26 frames sampled · 0 BLOCKER · 0 MAJOR (1 → 0 MAJOR) |
| **Status** | Built · QC'd · fact-check drafted, **not signed** · review cut · **not published** |
| **Renders** | local review cut `ai-fluency/youtube/hai-trust-then-verify/hai-trust-then-verify-slate.mp4`; goes to the shared Drive with the final master |

## Through-line

Trust, then verify — decide which claims need a source before the final cut, and who signs.

## Beats

| Beat | Act | Scene | Opens with | Measured |
|---|---|---|---|---:|
| B00 | cold open | ClaudeComposerAsk | Ciao, I'm Bella, for Humanitarians A I | 14.04 s |
| B01 | overview | BrutalistHesitantWriter | Here's the whole idea | 10.92 s |
| B02 | body | ShowTellCard · masked | Fluent text is persuasive | 14.29 s |
| B03 | body | ShowTellCard · focus | Here's the brief, claim by claim | 16.98 s |
| B04 | body | ShowTellCard · tabs | So they split | 14.83 s |
| B05 | body | ShowTellCard · paths | Every film ships with a fact check file | 13.14 s |
| B06 | body | ClaudeCodeBeat | But look at what the gate actually checks | 14.31 s |
| B07 | worked example | ClaudeComposerAsk | So here's what Claude did instead | 11.41 s |
| B08 | worked example | ClaudeCodeBeat | This is the real file, right now | 14.49 s |
| B09 | when not to | ShowTellCard · search | Where this bites | 12.22 s |
| B10 | verdict | ShowTellCard · elastic | So, the verdict | 9.64 s |
| B11 | your turn | ClaudeComposerAsk | Your turn | 17.79 s |
| B12 | outro | ShowTellCard · layout | Trust, Then Verify | 3.18 s |

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
