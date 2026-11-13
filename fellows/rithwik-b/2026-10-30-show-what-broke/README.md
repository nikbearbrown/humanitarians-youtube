# Show What Broke

Write a four-line failure-log entry (broke, noticed, changed, checked) and explain why it is stronger evidence than a polished demo.

| | |
|---|---|
| **Runtime** | 2:48 (167.99 s) |
| **Format** | 30 fps · 16:9 · 3840×2160 |
| **Voice** | Kokoro `af_bella` — the series voice |
| **Beats** | 13 (B00–B12) · `ai-explainer` spine intact |
| **Brand** | `claude` · `@HumanitariansAI` |
| **Presenter** | Rithwik B. |
| **Series** | AI Fluency × Brutalist (film 5 of 6) |
| **Audience** | Humanitarians AI fellows who use Claude daily but have never built with the Brutalist toolkit |
| **Built** | 2026-10-30 · research and scripting Weeks 9–10 (see [HOURS.md](../HOURS.md)) |
| **GATE V** | 26 frames sampled · 0 BLOCKER · 0 MAJOR (1 → 0 MAJOR) |
| **Status** | Built · QC'd · fact-check drafted, **not signed** · review cut · **not published** |
| **Renders** | local review cut `ai-fluency/youtube/hai-show-what-broke/hai-show-what-broke-slate.mp4`; goes to the shared Drive with the final master |

## Through-line

Show what broke — a failure log proves understanding in a way a polished demo can't.

## Beats

| Beat | Act | Scene | Opens with | Measured |
|---|---|---|---|---:|
| B00 | cold open | ClaudeComposerAsk | Hola, I'm Bella, for Humanitarians A I | 14.98 s |
| B01 | overview | BrutalistHesitantWriter | Here's the whole idea | 12.97 s |
| B02 | body | ShowTellCard · masked | Anyone can post a polished demo | 11.73 s |
| B03 | body | ShowTellCard · tabs | Put them side by side | 13.06 s |
| B04 | body | ShowTellCard · chart | Here's this series' actual log, by stage | 14.02 s |
| B05 | body | ShowTellCard · focus | And look at who caught them | 15.81 s |
| B06 | body | ShowTellCard · paths | Every entry has the same shape | 11.07 s |
| B07 | worked example | ClaudeComposerAsk | Here's one real entry | 16.81 s |
| B08 | worked example | ClaudeCodeBeat | So it went in the log | 12.78 s |
| B09 | when not to | ShowTellCard · search | Where this bites | 12.22 s |
| B10 | verdict | ShowTellCard · elastic | So, the verdict | 9.41 s |
| B11 | your turn | ClaudeComposerAsk | Your turn | 20.44 s |
| B12 | outro | ShowTellCard · layout | Show What Broke | 2.69 s |

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
SERIES-BUILD-LOG.md          the full 12-entry series failure log this film quotes
.gitignore                   renders out, build inputs in
```

**Not here** — the renders: review cut, narration `mp3/`, beat `clips/`, `media/`.

## Open before publication

1. Sign [`FACTCHECK-DRAFT.md`](FACTCHECK-DRAFT.md), then `./art final` for the clean master.
2. Watch and listen to the whole cut once, end to end — frame QC so far was on stills.
3. Channel — `@HumanitariansAI`; confirm before upload.
