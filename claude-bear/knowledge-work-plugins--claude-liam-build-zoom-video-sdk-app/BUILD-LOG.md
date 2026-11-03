# BUILD-LOG — knowledge-work-plugins--claude-liam-build-zoom-video-sdk-app

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-video-sdk-app/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel walking through the
`build-zoom-video-sdk-app` Anthropic skill — a reference for Zoom's Video
SDK across six client platforms). This invocation started from a bare
`SUBJECT.json` (no prior-pass artifacts) and built the reel end to end.

**Register re-registered Teardown -> Plain**, matching every sibling in
this factory: the source graded the skill ("what it gets right… what it
bites") and framed a "Verdict" card; this redo states the same
one-condition boundary as fact (no grading language) and folds the
verdict into a `WantQuote` carry-out beat. B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` (WRITER LAW:
"meeting" -> "video" — the newcomer assumption that "build a Zoom video
SDK app" produces an app that joins an actual Zoom meeting, corrected to
a custom video session built on Zoom's SDK). Close re-skinned to
`OutroCTA` / @HumanitariansAI with Liam's sign-off. BHTF's prompt was
rewritten clean — the source's handoff string was truncated/garbled
("...use after routing to a custom-session workfl. Read the
build-zoom-video-sdk-app skill...") and referenced a skill file the
general viewer won't have installed; this version asks Claude directly
to walk through the meeting-vs-custom-session distinction, no plugin
dependency.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat is AI-VIDEO, pantry, or
a human-drop slot — the source was already all-Remotion (`ClaudeComposerAsk`
x2, three `SkillTeardown*` cards, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so no substitution was required beyond the WRITER LAW
and channel-skin row hai-simple already mandates.

## Built end to end this invocation

1. Read the source sheet in full (locked facts: build-zoom-video-sdk-app
   is a reference skill for Zoom's Video SDK; applies after the work is
   routed to a custom-session workflow, when full control over the video
   experience is needed rather than an actual Zoom meeting; platform
   surface is android/flutter/ios/linux/macos/react-native, 8 files total
   incl. RUNBOOK.md and SKILL.md; a skill = a folder Claude reads before
   acting; execution is linear — read SKILL.md, execute steps in order,
   return result). No SCRIPT.md existed in the source dir (batch-built,
   PEDAGOGY.md VERDICT: PASS only). Read the structure template
   (`claude-liam-simple-delve`) and the nearest built precedent in this
   exact family (`knowledge-work-plugins--claude-liam-build-zoom-bot`,
   built the same day, also a redo of a skill-teardown reel with the same
   7-beat shape) to match conventions exactly.
2. Wrote `QUESTION.md` and `CARRY-OUT.md` before any narration (Step 0):
   carry-out line is "Build Zoom Video SDK App doesn't build you a Zoom
   meeting — it builds a custom video session, full control over the
   experience, on whichever of six platforms your app runs," defeating
   the wrong guess that the skill produces an actual Zoom meeting client.
3. Authored `SCRIPT.md` (Plain register, 7 beats matching the source's
   beat count) and `beat_sheet.json` — B00 `BrutalistHesitantWriter`
   (humanitarians palette, trigger "meeting" -> replacement "video",
   34-word narration + `lead_silence_s` 0.8 per TIMING LAW), B01/B02/B03
   as GRAPHIC/Manim (anatomy, pipeline, one-condition-six-platforms
   constraint), BCRY `WantQuote` carry-out, BHTF `ClaudeComposerAsk`
   your-turn with a freshly written runnable prompt, BOUT `OutroCTA`.
   Confirmed via `./art scenes --check` that `BrutalistHesitantWriter`,
   `ClaudeComposerAsk`, `WantQuote`, and `OutroCTA` are all RENDERABLE
   before slating (GATE L).
4. Wrote `scenes.py` (three custom Manim scenes: B01 "a skill is a
   folder" with six platform chips, B02 "how it runs" pipeline, B03
   "one condition" — a request splitting into a struck-through "Zoom
   meeting" path and a checked "custom video session" path, six platform
   chips beneath) and `render_scenes.py`, adapted from the
   `claude-liam-build-zoom-bot` precedent's pattern with content
   rewritten for this topic.
5. Generated audio: `generate_audio_kokoro.py`, free, local, `am_onyx`.
   Measured durations became the clock: B00 11.67s, B01 20.35s, B02
   9.34s, B03 17.49s, BCRY 10.07s, BHTF 15.27s, BOUT 5.42s.
6. Rendered the three Manim beats via `render_scenes.py` in the
   foreground — all 3 succeeded on first attempt.
7. Rendered the four Remotion beats via `remotion_scenes.py` in the
   foreground (`--timeout` on the Bash tool raised past the harness's
   2-minute default per the COMPLETION LAW — no background task,
   blocked on it directly until exit).
8. Verified B00 directly before compiling: pulled a frame at t=9.5s —
   the correction ("meeting" -> "video") is complete and legible, full
   question reads "Can Claude build my Zoom video app?" `ffprobe`
   confirms `media/B00.mp4` = 11.7s with an audio track, clearing the
   >=8s TIMING LAW floor.
9. First `compile.py` pass -> 7/7 real (no slate), master 90.6s,
   mean_volume -24.0 dB, canvas 3840x2160 (4K LAW — clean master forced
   from 720p directly). content-check/frame-check/lane-check all PASS.
10. **GATE T (`type_check.py`), first run: FAIL** — B03 min-size §8.1:
    smallest text run 15px < floor 20px (the six platform chips'
    `font_size=16` labels). Fixed by measuring each label's rendered
    width and sizing the card to fit + bumping `font_size` to 22 in both
    B01's and B03's platform-chip loops (B01 had the same undersized
    `font_size=17`, bumped preemptively). Re-rendered B01/B03, recompiled,
    **GATE T PASS** on second run.
11. **Gate V (frame QC):** pulled frames from all 7 beats (representative
    frame per beat) and read each directly. Found two visual defects on
    the first sweep, both in the newly rewritten B01/B03 Manim scenes:
    (a) B01 — the "react-native" chip text overflowed its fixed-width
    card, spilling past both edges with no visible border; (b) B03 — the
    crimson strike mark over "Zoom meeting" was a small X centered on the
    label rather than a full-width strikethrough, obscuring the "m" in
    "meeting" and reading as a legibility defect rather than a clean
    struck-through state. Fixed root cause: replaced fixed chip card
    widths with widths measured from the rendered text (`max text width +
    padding`) so no label can overflow regardless of length; replaced the
    `_cross` glyph with a `_strike` helper that draws a full-width
    horizontal line across the target label. Re-rendered B01/B03,
    recompiled, re-pulled frames — both defects confirmed fixed on the
    re-check, zero blockers on the second sweep. BOUT/`OutroCTA` renders
    on flat white, not the humanitarians cream ground — the same
    shared-component quirk already logged unfixed on every sibling in
    this factory (e.g. `knowledge-work-plugins--claude-liam-build-zoom-bot`);
    not a new defect.
12. Final master verified directly, independent of `compile.py`'s
    self-report: `ffmpeg -af volumedetect` confirms mean_volume -24.0 dB
    / max -2.8 dB; `ffprobe` confirms one video stream (3840x2160) and
    one audio stream; `stat` confirms the `.mp4` (16:53:55) is newer than
    `beat_sheet.json` (16:46:05) — all COMPLETION LAW conditions met.

## Gates

- **TIMING LAW (B00):** narration 34 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **11.67s** (rendered 11.7s), clears the
  >=8s floor. Correction ("meeting" -> "video") visible on-screen by
  t=9.5s.
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840x2160).
- **GATE T (`type_check.py`):** FAIL on first run (B03 min-size, six
  platform-chip labels below the 20px floor) -> fixed (dynamic chip
  width + font_size 22 in B01 and B03) -> **PASS** on second run.
- **Gate V (frame QC):** full beat sweep, all 7 beats read directly.
  First sweep found 2 defects (B01 chip text overflow, B03 strike-mark
  obscuring a letter) -> both fixed at the root (dynamic card sizing;
  full-width strikethrough helper) -> re-render, recompile, re-sweep:
  zero defects on the second pass.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg `volumedetect`
  via `compile.py`, independently re-verified via direct `ffmpeg`/`ffprobe`
  call — well above the -40 dB floor).

## Playlist resolution

`family: "knowledge-work-plugins"` matches `playlists.json` directly ->
**"Extending Claude — Skills, Plugins & Connectors"** (no fallback
needed).

## Delivery

Phase 4 not yet run this invocation — see the standing task below for
the next step, or the supervisor's own delivery pass. The master is born
natively at 3840x2160 via `compile.py`'s 4K LAW (no separate 4K re-render
needed once triggered).
