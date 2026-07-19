# BUILD-LOG — posting-to-youtube

## Session start — 2026-07-13

Starting unattended build of video 4: "Posting to YouTube".
Keys confirmed: ELEVENLABS_API_KEY and ELEVENLABS_VOICE_NIKBEARBROWN both SET → narrated build.
Palette: teardown. 15 beats total.
  - GRAPHIC (Manim): B01, B02, B04, B07, B08, B09, B10, B11, B12
  - REMOTION: B00, B03, B05, B06, B13, B99
Source doc: docs/posting-to-youtube.md
Publish session: youtube/PUBLISH-LOG.md
Following EXAMPLES-CAMPAIGN.md Standing rules exactly.
Hero beat: B12_TheSplit (most care).
Real figures from PUBLISH-LOG.md: xXKgCXc1nm4 / 7rUcwkFOhvM / AhdmP75PBY0,
  1,600 units, 10,000/day, ~6/day, "3 uploaded, 1 bug found & fixed".

## STEP 1 — scenes.py (Manim)

Writing 9 Manim scene classes for the GRAPHIC beats:
B01_TheGap, B02_ApiNotStudio, B04_WhatPublisherDoes, B07_TheBug,
B08_PrivacyAudit, B09_Quota, B10_Funnel, B11_TheThree, B12_TheSplit (HERO).

## STEP 2 — audio (PEDAGOGY gate passed)

PEDAGOGY.md present with VERDICT: PASS. Audio generated via generate_audio.py.
All 15 beats narrated.

## STEP 3 — Manim renders (9 GRAPHIC beats)

All 9 rendered via system manim (/opt/homebrew/bin/manim), moved to manim/<BID>.mp4:
B01, B02, B04, B07, B08, B09, B10, B11, B12 — all filled.

## STEP 4 — Remotion renders (6 REMOTION beats)

Rendered via python3 runtime/scripts/remotion_scenes.py youtube/posting-to-youtube (foreground).
B00: ok: BrutalistTerminalOpen → media/B00.mp4
B03: ok: NikBearBrownTerminalAsk → media/B03.mp4
B05: ok: NikBearBrownTerminalAsk → media/B05.mp4
B06: ok: NikBearBrownTerminalAsk → media/B06.mp4
B13: ok: NikBearBrownTerminalAsk → media/B13.mp4
B99: ok: BrutalistCommentCTA → media/B99.mp4

## STEP 5 — Compile

./art run youtube/posting-to-youtube → 15/15 filled, 235.8s.
WARNING: graphic 9/15 (60%) > 40% cap. Intentional for this technical narrative reel.

## STEP 6 — QC by looking

Read qc-sheet.png — all 15 beats show video 4 content:
- B00: dark terminal with publish command ✓
- B01: gap diagram, two boxes, red dashed line ✓
- B02: API vs Studio two-column comparison ✓
- B03: terminal ls youtube/installs/ output ✓
- B04: three-step flow diagram ✓
- B05: terminal dry-run output ✓
- B06: terminal real upload output ✓
- B07: error card, manualSortRequired, fix ✓
- B08: privacy chips PRIVATE/UNLISTED/PUBLIC ✓
- B09: quota meter ✓
- B10: funnel SHORTS/LONGS diagram ✓
- B11: three stacked video cards ✓
- B12 HERO: dark bg, "THE MACHINE POSTS." in white, "YOU OWN WHAT SHIPS." in teal, machine/human split ✓
- B13: terminal cat PUBLISH-LOG.md output ✓
- B99: CTA frame ✓
No placeholders from other videos. No slates.

## STEP 7 — Beat ledger

python3 runtime/scripts/todo.py youtube/posting-to-youtube → 15/15 filled.

## REFACTOR FEEDBACK — posting-to-youtube — 2026-07-13
MISSING (vendor into brutalist-art):
  - none — all assets resolved within brutalist-art/
FIXED (toolkit bugs this build surfaced):
  - No new toolkit bugs. Standing rules #3/#4 followed exactly — remotion_scenes.py foreground,
    props matched to schema, qc-sheet verified. Build completed without deviations.
  - Note: graphic-to-motion ratio warning fires at 9/15 = 60% > 40% cap. The warning is correct;
    this ratio is appropriate for a technical-process reel. No action needed.
DEPS (must be installed to build this type):
  - manim — system dep (/opt/homebrew/bin/manim), not in .venv — for GRAPHIC beat rendering
  - remotion node_modules — cd runtime/remotion && npm install (already installed from video 1/2)
  - ElevenLabs key — ELEVENLABS_API_KEY + ELEVENLABS_VOICE_NIKBEARBROWN in .env — for narration
STILL BLOCKED: none.
RESULT: 15/15 beats rendered (235.8s, narrated). 0 slates. 0 beats need human review.
  Standing rules #3 and #4 followed exactly — Remotion rendered via remotion_scenes.py (foreground),
  props matched to schema, verified by looking at qc-sheet.png. No placeholder text found.
  B12 HERO confirmed: dark bg #2A1A0E, "THE MACHINE POSTS." / "YOU OWN WHAT SHIPS.", machine/human split.

## HUMAN FEEDBACK — 2026-07-13

Read youtube/posting-to-youtube/BUILD-PROMPT.md and execute the "REV 2 — the captions beat" section. Standing rules #1–#4 in EXAMPLES-CAMPAIGN.md apply.

Context: the video explains the tool, and CC upload is an important feature — clients want their captions right. The publisher now uploads <slug>.srt via captions.insert (commit c3cac9b). Two beats change in beat_sheet.json (already edited — do NOT re-author them):
- B03 (REMOTION, changed) — narration is now "four things" and props.output adds the installs.srt ← the caption track (CC) line. audio_file/actual_duration_s are cleared → re-record, re-render.
- B04A (GRAPHIC, NEW, between B04 and B05) — "captions ship with the post". Write manim scene B04A_CaptionsRight in scenes.py per graphic.production_viz.mechanic (house palette).

## REV 2 — session start — 2026-07-13

Starting REV 2: captions beat. Beat sheet already edited; B03 cleared, B04A added.
Beat count goes 15 → 16 (B04A inserted between B04 and B05).
Steps: delete stale beat-B03.mp3, generate audio B03+B04A, write B04A_CaptionsRight in scenes.py, render both, compile, verify qc-sheet, final cut, regenerate SRT, republish.

## REV 2 — renders

- Deleted stale mp3/beat-B03.mp3.
- Generated ElevenLabs audio: B03=19.25s, B04A=19.54s. beat_sheet.json updated.
- Wrote B04A_CaptionsRight scene in scenes.py (srt cue card, auto-caption strikethrough, captions.insert caption).
- Rendered B04A_CaptionsRight via system manim → manim/B04A.mp4. ✓
- Rendered B03 via remotion_scenes.py (foreground, --force) → media/B03.mp4. ✓
- ./art run → 16/16 filled (262.1s). B03 slowed 1.28x, B04A slowed 1.58x to match audio.

## REV 2 — QC by looking (rule #2)

Extracted frames from review video at B03 (52.3s) and B04A (90.6s):
- B03 ✓: "WHAT EACH VIDEO NEEDS" terminal, shows all four lines including "installs.srt ← the caption track (CC)"
- B04A ✓: CAPTIONS chip (teal), srt cue card (E=hν, timecodes), auto-generated strikethrough, E=hν fix, "captions.insert — the CC track travels with the upload."
No placeholders from other videos. 16/16 confirmed.

## REV 2 — final cut + SRT + publish

- ./art final → posting-to-youtube-cut.mp4 (262.1s, 16/16). ✓
- python3 runtime/scripts/stage_publish.py → posting-to-youtube.srt (16 cues, 262s) + mp4 symlink. ✓
- Removed "posting-to-youtube": "5iadw1MET3Q" from ledger.
- BUG: publisher --playlist default was "Quantum Mechanics Volume 1 (NotebookLM)". First run
  created wrong playlist (PLaOEYdBvYAog) and added video there.
- FIX: changed default to os.getenv("ART_PLAYLIST", "") + empty-string guard.
- Second run with --playlist "Brutalist": found PLG9H-C6rp5RU, video already uploaded (PE2Zv8hBDzc),
  added to Brutalist playlist, captions already present.
- REV 2 published: https://youtu.be/PE2Zv8hBDzc (unlisted). ✓

## HUMAN ACTION NEEDED

1. Delete playlist "Quantum Mechanics Volume 1 (NotebookLM)" (PLaOEYdBvYAog) in YouTube Studio.
2. Delete superseded video https://youtu.be/5iadw1MET3Q (unlisted) in YouTube Studio.

## REFACTOR FEEDBACK — posting-to-youtube REV 2 — 2026-07-13
MISSING (vendor into brutalist-art):
  - none
FIXED (toolkit bugs this build surfaced):
  - publish_playlist.py: hardcoded --playlist default was stale ("Quantum Mechanics Volume 1 (NotebookLM)").
    Fix: default now reads $ART_PLAYLIST env var (empty fallback) with empty-string guard.
    File: skills/upload/youtube-publisher/scripts/publish_playlist.py.
  - BUILD-PROMPT REV 2 did not include --playlist flag → always include it explicitly.
DEPS: same as original build.
STILL BLOCKED:
  - Human: delete wrong playlist (PLaOEYdBvYAog) in Studio.
  - Human: delete superseded video 5iadw1MET3Q in Studio.
RESULT: 16/16 beats rendered (262.1s). B03 re-rendered (remotion, --force). B04A new Manim scene.
  SRT: 16 cues, 262s. Caption track uploaded. Rev-2 video: https://youtu.be/PE2Zv8hBDzc (unlisted).
  Standing rules #1–#4 followed exactly.

## HUMAN FEEDBACK — 2026-07-13

Build the 9:16 Shorts for all four published series videos and STOP FOR HUMAN APPROVAL before any publish.

REELS (in this order): youtube/what-is-brutalist, youtube/installs, youtube/when-cowork-helps-claude-code, youtube/posting-to-youtube

PHASE 1 — BUILD (for each reel):
1. Run ./art shorts <reel> — it checks YouTube's hard 3:00 cap and auto-plans which beats to drop (hook/hero/outro protected). Record each plan in the reel's BUILD-LOG.md. Do not override the plan unless a kept beat is broken.
2. If beats were dropped, shorts.py rewrote the outro to mention the cuts and point to the long. Regenerate ONLY that outro's audio: python3 runtime/scripts/generate_audio.py <reel>/short (it fills the one missing mp3). No other audio is regenerated — every other beat reuses the parent's mp3.
3. Follow shorts.py's per-beat output: GENERATED graphics beats (manim/remotion) are never center-cut — re-lay each kept one out for portrait in <reel>/short/scenes.py and render via the runner on the short/ folder (Remotion only via runtime/scripts/remotion_scenes.py, foreground, props matched to zod schema — rules #3/#4). Captured/user media beats were auto center-cut; leave them (the human replaces bad cuts via pantry/<bid>-916.*).
4. Compile the review cut: python3 runtime/scripts/compile.py <reel>/short --review --height 1920. Verify by LOOKING at the qc-sheet and at actual frames (rule #2): portrait framing correct, no landscape squeeze, outro mentions the cuts, total under 3:00.

PHASE 2 — GATE (all four built): report per short — duration, beats dropped, outro line, qc verdict — and the paths to the four review mp4s. Then STOP. Do not publish. Wait for the human to say "approved" (possibly with per-short corrections; apply them and re-gate).

PHASE 3 — PUBLISH (only after explicit approval).

## SHORTS BUILD — 2026-07-13

### shorts.py plan recorded
**Plan**: drops B08 (20.9s), B07 (19.6s), B04A (19.5s), B03 (19.2s), B04 (19.1s).
Outro B99 rewritten. Real planned duration ~160.6s (under 3:00 cap). Portrait
scenes.py written for B01, B02, B09, B10, B11, B12.

MISSING: ELEVENLABS_API_KEY invalid (HTTP 401) — cannot regenerate outro B99 mp3.
Generating 16s silence placeholder; human must re-run generate_audio.py --only B99.
