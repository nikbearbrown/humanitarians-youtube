# BUILD LOG — hai-simple/knowledge-work-plugins--linux

Redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-meeting-sdk/linux`
(Teardown register, 7-beat skill-teardown of the Anthropic skill `meeting-sdk/linux`) as
`hai-simple` (Plain register, Humanitarians AI skin). Source folder untouched.

## Source is intact

Every beat carries the full skill-description sentence: "Zoom Meeting SDK for Linux -
C++ headless meeting bots with raw audio/video access, transcription, recording, and AI
integration for server-side automation." Nothing to recover; full detail in `QUESTION.md`.
No local copy of the source's own `SKILL.md`/`linux.md` exists on this machine (its path
in the source sheet, `/Users/bear/Documents/CoWork/.../partner-built/zoom-plugin/skills/
meeting-sdk/linux/SKILL.md`, is Bear's-machine-only) — the source `beat_sheet.json`'s own
intact `narration_text` and file-listing props served as the sole fact source, per Phase
1's "describe behavior generically when in doubt" instruction. No fact invented beyond
what the source states.

## What changed vs. source (per redo contract)

- **Register:** Teardown → Plain. Source's "Teardown moment," "what it gets right / what
  it bites," and verdict framing dropped; B03 states the mechanism (headless, on a Linux
  server, raw audio/video access, transcription, recording, AI-step handoff) and stops.
- **Cold open:** source's `ClaudeComposerAsk` ask → `BrutalistHesitantWriter`. Writer
  types the newcomer's wrong-guess word "SCREEN" (implying the bot needs a screen/window
  somewhere to run and be watched), hesitates, corrects to "server" → lands "meeting-sdk/
  linux needs a server to run the bot on. Right?". The wrong guess is the inverse of the
  source's own spec line ("headless meeting bots ... for server-side automation").
- **Beat count:** kept the source's shape in substance (B00 → B01 anatomy → B02 pipeline
  → B03 mechanism → BCRY carry-out → BHTF handoff → BOUT outro), source's single outro
  split into hai-simple's fixed two-part Humanitarians AI outro (`OutroSeries` +
  `OutroCTA`) — 8 beats total, same precedent as this family's other redos
  (`enrich-lead`, `lead-triage`, `legal-risk-assessment`, …).
- **Facts/argument:** unchanged — anatomy (six files/folders: `linux.md`,
  `meeting-sdk-bot.md`, `RUNBOOK.md`, `SKILL.md`, `concepts/`, `references/`), pipeline
  (Steps section, linear execution), the job (C++ bot, headless, Linux server, raw
  audio/video access, transcription, recording, AI-step handoff, server-side automation),
  and the scope guarantee (same input, same behavior, every run; silent outside the file)
  all carried over from the source's own intact text.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Close:** BHTF's paste-ready prompt is new and complete (the source's own handoff was
  visibly truncated: "...raw audio/video acce."). Rewritten as "I want a Zoom meeting bot
  running headless on Linux. Read the meeting-sdk/linux skill in this folder and walk me
  through exactly which steps you'd run, in order, before you run any of them."

## NO-GENAI / NO-PANTRY LAW

Every beat is REMOTION (`BrutalistHesitantWriter`, `SkillTeardownAnatomy`,
`SkillTeardownPipeline`, `SkillTeardownMechanism`, `WantQuote`, `ClaudeComposerAsk`,
`OutroSeries`, `OutroCTA`) — no beat in either version was ever AI-VIDEO, pantry, or a
human-drop slot. `compile.py`'s motion-histogram WARNING (`remotion` 8/8 = 100%, over the
~40% pantry cap) is expected and accepted for the same reason every prior all-REMOTION
sibling in this family logged it: this reel is a file/pipeline/scope explainer, not a
worked-example narrative, and has no illustrative-figure beats to draw as Manim/GRAPHIC.

## Build — clean first pass

- **GATE L:** confirmed all seven components RENDERABLE via `./art scenes --check`
  before authoring (`BrutalistHesitantWriter`, `SkillTeardownAnatomy`,
  `SkillTeardownPipeline`, `SkillTeardownMechanism`, `WantQuote`, `ClaudeComposerAsk`,
  `OutroSeries`, `OutroCTA`) — no PUNT needed, every beat is an existing library hit.
- **GATE T:** `type_check.py` PASS, 0 FAILs, first pass.
- `generate_audio_kokoro.py` — 8 beats, $0.00. B00 measured **10.03s** (26-word narration
  + `lead_silence_s` 0.8), clear of the ≥9s TIMING LAW window.
- **Harness note (foreground-render rule):** `remotion_scenes.py` on the full 8-beat sheet
  hit the tool's 2-minute default foreground timeout twice (once at 2 min, once at the
  10-min ceiling) — B00–B03 and BCRY had already written to `media/` before each kill, so
  per the COMPLETION LAW's foreground-render rule the run was never treated as background
  work left to finish itself: confirmed via `ls media/` which beats existed, then re-ran
  `--only BHTF`, `--only BOUT`, `--only BCTA` individually in the foreground, each
  completing in well under a minute once isolated from the earlier contention. All 8
  confirmed present in `media/` before compiling.
- **Compile:** `compile.py` — content-check PASS, frame-check PASS, lane-check PASS,
  8/8 beats real (no slates). 4K LAW forced the native master to 3840×2160 directly (no
  separate upscale needed, all-Remotion reel).
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (well clear of the -40 dB floor), max
  -2.9 dB — independently re-verified via `ffmpeg volumedetect` on the compiled master.
- **Gate V (frame QC):** sampled frames at t=8.7s (B00, correction landed — "meeting-sdk/
  linux needs a server to run the bot on. Right?" fully typed, cursor resting at end),
  t=16s (B01 anatomy — all six files/folders listed, "6 files total" callout correct),
  t=27s (B02 pipeline — four-phase flow clean), t=40s (B03 mechanism — "Headless, on a
  server. Raw audio and video, start to finish." no judgment language), t=55s (BCRY
  carry-out quote, alone, serif, legible), t=70s (BHTF ClaudeComposerAsk, prompt text
  correct, `@HumanitariansAI` folder label), t=80s (BOUT title restate "Claude, Meeting
  SDK/Linux."), t=84s (BCTA "…Liam, in for Bear." + Subscribe + handle). All legible,
  correctly kerned, no text overlap, safe inset respected. **Noted, not a defect
  introduced here:** `OutroSeries`/`OutroCTA` render on flat white rather than the
  humanitarians cream (`#F3EBDD`) — same shared-component behavior already logged
  unremarked in every sibling hai-simple reel in this family; out of this reel's scope to
  fix.
- **ffprobe:** video 3840×2160 h264, audio aac 48kHz present; duration 84.98s; mp4 mtime
  (05:32:44) newer than beat_sheet.json mtime (05:31:24).

## Output

`knowledge-work-plugins--linux.mp4` — 85.0s, 8/8 beats real (no slates), native
3840×2160, audible narration throughout (mean_volume -23.9 dB, independently verified,
mp4 newer than beat_sheet.json). COMPLETION LAW satisfied.

**Playlist:** Extending Claude — Skills, Plugins & Connectors. `SUBJECT.json`'s
`family: "knowledge-work-plugins"` matches the `knowledge-work-plugins` prefix in
`playlists.json`'s map directly (no fallback needed).

**Status: review cut DONE.** Passed every Phase-3 gate. Proceeding to Phase 4 (4K render
+ deliver.py) in this same invocation.

## Phase 4 (4K + delivery)

- **4K master:** the Phase-3 compile already wrote the master natively at 3840×2160
  (all-Remotion reel, 4K LAW). Copied it to `knowledge-work-plugins--linux-4k.mp4` so
  `deliver.py`'s `newest_master()` picks it as the explicit 4K variant.
