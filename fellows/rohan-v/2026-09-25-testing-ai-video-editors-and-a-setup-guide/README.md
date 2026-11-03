# Testing AI Video Editors, and a Setup Guide for New Fellows — Rohan V.

Progress video, week of 2026-09-25 · Humanitarians AI · Lyrical Literacy ·
GitHub `rohanvijaykumar`

## This week's contribution

**Question.** Can an AI agent take on the editing of our Lyrical Literacy
tutorials, and what does a new fellow need, in what order, to get started?

**Prediction.** That an agent editor could handle finishing work (captions,
titles) on footage we already have.

**What I built/tried.** Looked at four ways to let an agent edit: Remotion,
HyperFrames, OpenReel and a DaVinci Resolve MCP connector. Tested one hands-on:
HyperFrames re-edited the finished Suno Part 1 footage and narration with
word-by-word captions and a new intro (2026-09-16). Started the setup guide:
Discord, Suno, Midjourney and Canva, with account access and how to use each.

**Observed result.** A 4:05 cut with 94 caption lines and 0 overlaps, but at
1920×1080, not 4K. The glass style vanished on our cream footage, the captions
copied the phonetic spelling from the voice script until fixed, and the render
needed ~61 GB of scratch. Good at packaging existing footage; no new teaching
visuals.

**Next experiment.** Write the setup guide (in progress). _Proposed, not yet
decided:_ run OpenReel and DaVinci Resolve on the same footage, so the comparison is fair.

## Human and AI work

**My decisions, implementation and verification:** chose the four tools to look
at, set up and directed the HyperFrames test, stopped it writing to C:, and
defined the guide's scope.

**AI tools/voices used and what they generated:** Claude (Claude Code) ran the
HyperFrames install and test edit, and this week built this video (four new
scenes, three reused), traced every claim, rendered and drafted these docs.
Narration: Kokoro `af_bella`, my persistent voice for the series (AI voice,
disclosed on screen).

**What I rejected or corrected:** installing anything onto C:; the test's
phonetic captions; a draft line that counted Remotion as untested.

**What remains unverified or failed:** OpenReel and DaVinci Resolve are not yet
tested; the guide is not yet written; YouTube 4K playback not yet checked.

## Reproduce

**Brutalist version/commit and date checked:** `26894b5` (main, merged
with origin/main `6a8380a` on 2026-09-25) plus this week's scenes — checked
2026-09-25.

**Source commit used for this export:** see the commit that adds this folder.

**Beat sheet and custom scene files:** [`beat_sheet.json`](./beat_sheet.json),
[`cues.json`](./cues.json), [`vertical/beat_sheet.json`](./vertical/beat_sheet.json);
scenes `HaiProgressTwoFronts`, `HaiToolField`, `HaiFootageShowcase`,
`HaiVerdictSplit` (+ `916` siblings) in the Brutalist toolkit.

**Commands, dependencies, inputs:**

```bash
./art final path/to/2026-09-25-testing-ai-video-editors-and-a-setup-guide
./art vertical path/to/2026-09-25-testing-ai-video-editors-and-a-setup-guide
```

Inputs: [`pantry/`](./pantry/) — four frames of the HyperFrames output (my own
footage). The 6 s caption excerpt and the full test render are renders and stay
out of git.

**Approvals and checks:** GATE F, GATE T and Gate V on both cuts — results in
[`BUILD-LOG.md`](./BUILD-LOG.md). No human approval record is required for this
reel type; none is claimed.

## Watch and review

Landscape — [`landscape/AgenticEditingUpdate_RohanV.mp4`](https://drive.google.com/drive/folders/1TYRVlCh91t0EzFt3ZYOAGAzgzXeNDHah) — 3840×2160 — 2:20 (140.79 s) — SHA-256 `346e8fcdc0f26a6b2e2b973487bc214289f9f29f7ab71496a62604dc33fea20a`

Vertical — [`vertical/AgenticEditingUpdate_RohanV.mp4`](https://drive.google.com/drive/folders/1cNSkXK6U4DmUPhBRF8HIortJicGE8kCk) — 2160×3840 — 2:20 (140.79 s) — SHA-256 `151bdaed017955e234730a2cf868b2b7dcbab7082538484c4e782e6306236f74`

Sources/large assets: the full HyperFrames test render is on my machine
(`HyperFrames/videos/suno-part-1-glass/out/`, SHA-256 in `pantry/hf-source.sha256`).

PM review status: pending
YouTube 4K processing check: pending upload
Professors' publication decision: pending

## Files

| | |
|---|---|
| [`beat_sheet.json`](./beat_sheet.json) · [`cues.json`](./cues.json) | the build contract and the word-clock anchors |
| [`FACTCHECK.md`](./FACTCHECK.md) · [`SOURCES.md`](./SOURCES.md) | every claim and the session record line it rests on |
| [`SOURCE-brief.md`](./SOURCE-brief.md) · [`PROMPT.md`](./PROMPT.md) · [`PEDAGOGY.md`](./PEDAGOGY.md) · [`PROMPTS.md`](./PROMPTS.md) · [`SHOTLIST.md`](./SHOTLIST.md) | the brief, design and per-beat plan |
| [`BUILD-LOG.md`](./BUILD-LOG.md) · [`FEEDBACK.md`](./FEEDBACK.md) · [`FRICTIONAL.md`](./FRICTIONAL.md) | what broke, reviewer notes, the frictional log |
| [`description.txt`](./description.txt) | the YouTube description |
| `qc-sheet-16x9.png` · `qc-sheet-9x16.png` | contact sheets of both masters |
