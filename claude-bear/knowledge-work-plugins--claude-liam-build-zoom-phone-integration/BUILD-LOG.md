# BUILD-LOG — knowledge-work-plugins--claude-liam-build-zoom-phone-integration

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-phone-integration/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel walking through the
`build-zoom-phone-integration` Anthropic skill — a reference skill for
Zoom Phone covering OAuth, the Phone APIs, webhooks, Smart Embed events,
URI schemes, CRM or CTI dialer wiring, and call handling automation).
This invocation started from a bare `SUBJECT.json` (no prior-pass
artifacts) and built the reel end to end, using the
`knowledge-work-plugins--claude-liam-build-zoom-bot` sibling (built
earlier the same day, same source shape) as the exact structural
precedent.

**Register re-registered Teardown -> Plain**, matching every sibling in
this factory: the source graded the skill ("what it gets right… what it
bites") and framed a "Verdict" card; this redo states the same
seven-area boundary as fact (no grading language) and folds the verdict
into a `WantQuote` carry-out beat. B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` (WRITER LAW:
"be" -> "build" — the newcomer assumption that Claude itself personally
becomes/handles the Zoom phone integration, answering calls, corrected to
Claude building the integration's code). Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. BHTF's prompt was rewritten clean —
the source's handoff string was truncated/garbled ("...reference skill
for zoom phone. use after routing to a phone workflow when imple. Read
the build-zoom-phone-integration skill...") and referenced a skill file
the general viewer won't have installed; this version asks Claude
directly to walk through a real CRM/Zoom-Phone wiring task, no plugin
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

1. Read the source sheet in full (locked facts: build-zoom-phone-integration
   is a reference skill for Zoom Phone, used after a request has already
   routed to a phone workflow; it covers OAuth, the Phone APIs, webhooks,
   Smart Embed events, URI schemes, CRM or CTI dialer wiring, and call
   handling automation; a skill = a folder Claude reads before acting;
   execution is linear — read SKILL.md, execute steps in order, return
   result). No SCRIPT.md existed on the source; its `beats[*].narration_text`
   served as the locked script. Read the structure template
   (`claude-liam-simple-delve`) and the nearest built precedent in this
   exact family (`knowledge-work-plugins--claude-liam-build-zoom-bot`, a
   same-day redo of a sibling skill-teardown reel with an identical 7-beat
   shape) to match conventions exactly.
2. Wrote `QUESTION.md` and `CARRY-OUT.md` before any narration (Step 0):
   carry-out line is "Build Zoom Phone Integration doesn't make Claude
   answer your calls — it makes Claude wire the connection: the OAuth,
   the webhooks, and the CRM or CTI dialer code that handles the call for
   you," defeating the wrong guess that Claude personally answers or
   routes the call.
3. Authored `SCRIPT.md` (Plain register, 7 beats matching the source's
   beat count) and `beat_sheet.json` — B00 `BrutalistHesitantWriter`
   (humanitarians palette, trigger "be" -> replacement "build", 35-word
   narration + `lead_silence_s` 0.8 per TIMING LAW), B01/B02/B03 as
   GRAPHIC/Manim (anatomy, pipeline, seven-area reference-not-one-build
   constraint), BCRY `WantQuote` carry-out, BHTF `ClaudeComposerAsk`
   your-turn with a freshly written runnable prompt (CRM caller-ID lookup
   via Zoom Phone), BOUT `OutroCTA`. Confirmed via `./art scenes --check`
   that `BrutalistHesitantWriter`, `WantQuote`, `ClaudeComposerAsk`, and
   `OutroCTA` are all RENDERABLE before slating (GATE L).
4. Wrote `scenes.py` (three custom Manim scenes: B01 "a skill is a
   folder", B02 "how it runs" pipeline, B03 "a reference, not one build"
   seven-item checklist) and `render_scenes.py`, adapted directly from the
   `build-zoom-bot` precedent's pattern with content rewritten for this
   topic (B03 restructured from three fixed build-target rows to a
   compact seven-row checklist reflecting the source's actual scope list).
5. Generated audio: `generate_audio_kokoro.py`, free, local, `am_onyx`,
   first pass clean, $0.00. Measured durations became the clock: B00
   12.16s, B01 18.15s, B02 9.34s, B03 18.97s, BCRY 10.84s, BHTF 16.70s,
   BOUT 5.10s.
6. Rendered the three Manim beats via `render_scenes.py` in the
   foreground — all 3 succeeded on first attempt.
7. Rendered the four Remotion beats via `remotion_scenes.py`. The command
   exceeded the tool's inline timeout and was moved to a tracked
   background task by the harness; per the COMPLETION LAW, blocked on it
   directly via `TaskOutput(block=true)` until the completion
   notification confirmed exit code 0 — all 4 beats rendered clean
   (B00 extended to 12.2s, BCRY to 10.8s, BHTF to 16.7s, BOUT to 5.1s).
8. Verified B00 directly before compiling: pulled a frame at t=11.0s —
   the correction ("be" -> "build") is complete and legible, full
   question reads "Can Claude build my Zoom phone integration?" `ffprobe`
   confirms `media/B00.mp4` = 12.17s with an audio track, clearing the
   >=8s TIMING LAW floor.
9. First `compile.py` pass -> 7/7 real (no slate), master
   `knowledge-work-plugins--claude-liam-build-zoom-phone-integration.mp4`,
   92.3s, mean_volume -24.0 dB. content-check/frame-check/lane-check all
   PASS, canvas 3840x2160 (4K LAW — clean master forced from 720p
   directly).
10. **GATE T (`type_check.py`): PASS on first run**, 0 FAILs.
11. **Gate V (frame QC):** pulled frames from all 7 beats (representative
    frame per beat across the full 92.3s runtime) and read each directly.
    All legible, correct contrast, no text overlap, no clipping, safe
    inset respected, correct @HumanitariansAI branding throughout. No
    defects found this pass — clean on the first sweep. (BOUT/`OutroCTA`
    renders on flat white, not the humanitarians cream ground — the same
    shared-component quirk already logged unfixed on every sibling in
    this factory, e.g. `knowledge-work-plugins--claude-liam-build-zoom-bot`
    and `knowledge-work-plugins--claude-liam-build-zoom-meeting-app`; not
    a new defect.)
12. Final master verified directly, independent of `compile.py`'s
    self-report: `ffmpeg -af volumedetect` confirms mean_volume -24.0 dB
    / max -2.9 dB; `ffprobe` confirms one video stream (3840x2160) and
    one audio stream; `stat` confirms the `.mp4` (16:21:21) is newer than
    `beat_sheet.json` (16:19:51) — all COMPLETION LAW conditions met.

## Gates

- **TIMING LAW (B00):** narration 35 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **12.16s** (rendered 12.17s), clears the
  >=8s floor. Correction ("be" -> "build") visible on-screen by t=11.0s.
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840x2160).
- **GATE T (`type_check.py`):** PASS on first run, 0 FAILs.
- **Gate V (frame QC):** full beat sweep, all 7 beats read directly. No
  defects found.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg `volumedetect`
  via `compile.py`, independently re-verified via direct `ffmpeg`/`ffprobe`
  call — well above the -40 dB floor).

## Playlist resolution

`family: "knowledge-work-plugins"` matches `playlists.json` directly ->
**"Extending Claude — Skills, Plugins & Connectors"** (no fallback
needed).

## Delivery

Phase 4 completed this invocation. The master is born natively at
3840x2160 via `compile.py`'s 4K LAW, so no separate 4K re-render was
needed — copied directly to
`knowledge-work-plugins--claude-liam-build-zoom-phone-integration-4k.mp4`.
`deliver.py --push` staged
`DELIVERY/knowledge-work-plugins--claude-liam-build-zoom-phone-integration/`
(4K master + description) for the Drive sync, and committed + pushed
`claude-bear/knowledge-work-plugins--claude-liam-build-zoom-phone-integration/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no media) to `humanitarians-youtube`.
`HAILOOP-LOG.md` updated with the matching entry.
