# BUILD-LOG — knowledge-work-plugins--claude-liam-build-zoom-team-chat-app

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-team-chat-app/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel walking through the
`build-zoom-team-chat-app` Anthropic skill — a reference skill for Zoom
Team Chat integrations). This invocation started from a bare
`SUBJECT.json` (no prior-pass artifacts) and built the reel end to end.

**Register re-registered Teardown -> Plain**, matching every sibling in
this factory: the source graded the skill ("what it gets right… what it
bites") and framed a "Verdict" card; this redo states the same six-item
coverage boundary as fact (no grading language) and folds the verdict
into a `WantQuote` carry-out beat. B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` (WRITER LAW:
"design" -> "assemble" — the newcomer assumption that Claude freely
designs a brand-new chat app from imagination, corrected to Claude
assembling a bounded set of pieces from a fixed instruction file). Close
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off. BHTF's
prompt was rewritten clean — the source's handoff string was
truncated/garbled ("...reference skill for zoom team chat. use after
routing to a chat workfl. Read the build-zoom-team-chat-app skill and
walk me through what you will do before you do it.") and referenced a
skill file the general viewer won't have installed; this version asks
Claude directly to walk through a bot/card/webhook example, no plugin
dependency.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat is AI-VIDEO, pantry, or
a human-drop slot — the source was already all-Remotion (`ClaudeComposerAsk`
x2, three `SkillTeardown*` cards, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`),
so no substitution was required beyond the WRITER LAW and channel-skin row
hai-simple already mandates.

## Built end to end this invocation

1. Read the source sheet + narration in full (locked facts:
   build-zoom-team-chat-app is a reference skill for Zoom Team Chat, used
   after routing to a chat workflow, covering user-scoped messaging
   integrations, chatbot experiences, rich cards, buttons, slash
   commands, or chat webhooks; a skill = a folder Claude reads before
   acting; execution is linear — read SKILL.md, execute steps in order,
   return result). Read the structure template (`claude-liam-simple-delve`)
   and the nearest built precedent in this exact family
   (`knowledge-work-plugins--claude-liam-build-zoom-bot`, also a redo of a
   skill-teardown reel from the same source series) to match conventions
   exactly.
2. Wrote `QUESTION.md` and `CARRY-OUT.md` before any narration (Step 0):
   carry-out line is "Build Zoom Team Chat App doesn't give Claude a
   blank page… it gives Claude one instruction file, and Claude assembles
   exactly what that file lists… into the Zoom chat you already have,"
   defeating the wrong guess that Claude freely designs a new chat app.
3. Authored `SCRIPT.md` (Plain register, 7 beats matching the source's
   beat count) and `beat_sheet.json` — B00 `BrutalistHesitantWriter`
   (humanitarians palette, trigger "design" -> replacement "assemble",
   31-word narration + `lead_silence_s` 0.8 per TIMING LAW), B01/B02/B03
   as GRAPHIC/Manim (anatomy, pipeline, six-item coverage constraint),
   BCRY `WantQuote` carry-out, BHTF `ClaudeComposerAsk` your-turn with a
   freshly written runnable prompt, BOUT `OutroCTA`. Confirmed via
   `./art scenes --check` that `BrutalistHesitantWriter`,
   `ClaudeComposerAsk`, `WantQuote`, and `OutroCTA` are all RENDERABLE
   before slating (GATE L).
4. Wrote `scenes.py` (three custom Manim scenes: B01 "a skill is a
   folder", B02 "how it runs" pipeline, B03 "one chat lane, six pieces")
   and `render_scenes.py`, adapted from the `claude-liam-build-zoom-bot`
   precedent's pattern with content rewritten for this topic's six-item
   coverage list (two columns of three, vs. the precedent's three-row
   single column).
5. Generated audio: `generate_audio_kokoro.py`, free, local, `am_onyx`.
   Measured durations became the clock: B00 10.99s, B01 18.45s, B02
   9.34s, B03 17.96s, BCRY 12.44s, BHTF 15.25s, BOUT 5.59s.
6. Rendered the three Manim beats via `render_scenes.py` in the
   foreground — all 3 succeeded on first attempt.
7. Rendered the four Remotion beats via `remotion_scenes.py`. The command
   exceeded the tool's inline timeout and was moved to a tracked
   background task by the harness; per the COMPLETION LAW, blocked on it
   directly via `TaskOutput(block=true)` until the completion
   notification confirmed exit code 0 — all 4 beats rendered clean
   (B00 extended to 11.0s, BCRY to 12.4s, BHTF to 15.2s, BOUT to 5.6s).
8. Verified B00 directly before compiling: pulled a frame at t=9.5s —
   the correction ("design" -> "assemble") is complete and legible, full
   question reads "Does Claude assemble a new team chat app?" `ffprobe`
   confirms `media/B00.mp4` = 11.0s with an audio track, clearing the
   >=8s TIMING LAW floor.
9. First `compile.py` pass -> 7/7 real (no slate), master
   `knowledge-work-plugins--claude-liam-build-zoom-team-chat-app.mp4`,
   91.0s, mean_volume -24.0 dB. content-check/frame-check/lane-check all
   PASS, canvas 3840x2160 (4K LAW — clean master forced from 720p
   directly).
10. **Gate V (frame QC), first pass:** pulled frames across all 7 beats
    and read each directly. B00/B01/B02/B03/BCRY/BOUT clean. Found one
    real defect on **BHTF**: the longer on-screen topic string ("BUILD
    ZOOM TEAM CHAT APP · ANTHROPIC SKILL") wrapped to two lines in
    `ClaudeComposerAsk` and crowded the "Your Turn" segment label directly
    beneath it — a legibility issue this reel's longer title introduced
    that the shorter-titled `build-zoom-bot` precedent didn't hit.
    **Fixed:** shortened the on-screen `topic` prop to "ZOOM TEAM CHAT ·
    ANTHROPIC SKILL" (32 chars, matching the precedent's working length)
    — fits on one line, no overlap. Per COMPLETION LAW, edited
    `beat_sheet.json`, re-rendered BHTF only (`remotion_scenes.py --only
    BHTF --force`), and recompiled (never left a post-compile sheet edit
    unreconciled with the master).
11. **GATE T (`type_check.py`) — first run after the BHTF fix and
    recompile: FAIL** (1 pixel beat) — B03's footer/row text measured
    18px, under the 20px (1.9% frame-height) floor at the actual rendered
    size, once GATE T inspected real pixels post-render rather than the
    pre-render text-only pass that had shown PASS earlier. **Fixed:**
    bumped `scenes.py` B03Scene row font_size 25->27 and footer font_size
    23->26, deleted the stale `manim/B03.mp4`, re-rendered B03, and
    recompiled. **Re-run: GATE T PASS, 0 FAILs.**
12. **Gate V, final pass:** re-pulled the BHTF and B03 frames after both
    fixes — BHTF's topic now renders on one line with clean spacing above
    "Your Turn"; B03's six-item list and footer are legible at the larger
    size, correct contrast, no overlap, safe inset respected, correct
    @HumanitariansAI branding throughout. (BOUT/`OutroCTA` renders on flat
    white, not the humanitarians cream ground — the same shared-component
    quirk already logged unfixed on every sibling in this factory, e.g.
    `knowledge-work-plugins--claude-liam-build-zoom-bot`; not a new
    defect.)
13. Final master verified directly, independent of `compile.py`'s
    self-report: `ffmpeg -af volumedetect` confirms mean_volume -24.0 dB
    / max -2.9 dB; `ffprobe` confirms one video stream (3840x2160) and
    one audio stream; `stat` confirms the `.mp4` (17:29:20) is newer than
    `beat_sheet.json` (17:25:38) — all COMPLETION LAW conditions met.

## Gates

- **TIMING LAW (B00):** narration 31 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **10.99s** (rendered 11.0s), clears the
  >=8s floor. Correction ("design" -> "assemble") visible on-screen by
  t=9.5s.
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840x2160).
- **GATE T (`type_check.py`):** FAIL on first post-render run (B03 text
  18px < 20px floor) -> fixed (font_size bumps in `scenes.py`) -> **PASS**
  on re-run, 0 FAILs.
- **Gate V (frame QC):** full beat sweep, two passes. First pass found
  and fixed a BHTF topic-string wrap/crowd defect; second pass (post-fix,
  post-GATE-T-fix) found no further defects.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg `volumedetect`
  via `compile.py`, independently re-verified via direct `ffmpeg`/`ffprobe`
  call — well above the -40 dB floor).

## Playlist resolution

`family: "knowledge-work-plugins"` matches `playlists.json` directly ->
**"Extending Claude — Skills, Plugins & Connectors"** (no fallback
needed).

## Delivery

The master is born natively at 3840x2160 via `compile.py`'s 4K LAW, so no
separate 4K re-render is needed — copied directly to
`knowledge-work-plugins--claude-liam-build-zoom-team-chat-app-4k.mp4`.
`deliver.py --push` stages
`DELIVERY/knowledge-work-plugins--claude-liam-build-zoom-team-chat-app/`
(4K master + description) for the Drive sync, and commits + pushes
`claude-bear/knowledge-work-plugins--claude-liam-build-zoom-team-chat-app/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no media) to `humanitarians-youtube`.
`HAILOOP-LOG.md` updated with the matching entry.
