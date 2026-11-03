# BUILD-LOG — knowledge-work-plugins--claude-liam-build-zoom-contact-center-app

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-build-zoom-contact-center-app/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel walking through the
`build-zoom-contact-center-app` Anthropic skill — a reference skill for Zoom
Contact Center integrations). This invocation started from a bare
`SUBJECT.json` (no prior-pass artifacts) and built the reel end to end.

**Register re-registered Teardown -> Plain**, matching every sibling in this
factory: the source graded the skill ("what it gets right… what it bites")
and framed a "Verdict" card; this redo states the same five-item scope
boundary as fact (no grading language) and folds the verdict into a
`WantQuote` carry-out beat. B00 replaced the source's `ClaudeComposerAsk`
cold open with `BrutalistHesitantWriter` (WRITER LAW: "agent" -> "app" — the
newcomer assumption that "contact center app" means a talking AI agent,
corrected to Claude building the integration app's code). Close re-skinned
to `OutroCTA` / @HumanitariansAI with Liam's sign-off. BHTF's prompt was
rewritten clean — the source's handoff string was truncated/garbled
("...use after routing to a contac. Read the build-zoom-contact-center-app
skill...") and referenced a skill file the general viewer won't have
installed; this version asks Claude directly to walk through the same scope
(engagement context, campaign callbacks, version-drift), no plugin
dependency. Built from the nearest precedent in this exact family
(`knowledge-work-plugins--claude-liam-build-zoom-bot`, also a redo of a
skill-teardown reel), matching its conventions exactly.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat is AI-VIDEO, pantry, or a
human-drop slot — the source was already all-Remotion (`ClaudeComposerAsk`
x2, three `SkillTeardown*` cards, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so no substitution was required beyond the WRITER LAW
and channel-skin row hai-simple already mandates.

## Built end to end this invocation

1. Read the source sheet + narration in full (locked facts:
   build-zoom-contact-center-app is a *reference* skill for Zoom Contact
   Center; used after routing to a contact-center workflow for app/web/native
   integrations, engagement context and state handling, campaigns,
   callbacks, or version-drift troubleshooting; a skill = a folder Claude
   reads before acting, 8 items — RUNBOOK.md, SKILL.md, android/, concepts/,
   ios/, references/, scenarios/, troubleshooting/; execution is linear —
   read SKILL.md, execute steps in order, return result). Read the structure
   template (`claude-liam-simple-delve`) and the nearest built precedent in
   this exact family (`knowledge-work-plugins--claude-liam-build-zoom-bot`)
   to match conventions exactly.
2. Wrote `QUESTION.md` and `CARRY-OUT.md` before any narration (Step 0):
   carry-out line is "Build Zoom Contact Center App doesn't hand you a
   talking AI agent — it makes Claude build the app… fitted around Zoom's
   own Contact Center platform," defeating the wrong guess that "contact
   center app" means a conversational agent.
3. Authored `SCRIPT.md` (Plain register, 7 beats matching the source's beat
   count) and `beat_sheet.json` — B00 `BrutalistHesitantWriter`
   (humanitarians palette, trigger "agent" -> replacement "app", 32-word
   narration + `lead_silence_s` 0.8 per TIMING LAW), B01/B02/B03 as
   GRAPHIC/Manim (anatomy, pipeline, five-item scope constraint), BCRY
   `WantQuote` carry-out, BHTF `ClaudeComposerAsk` your-turn with a freshly
   written runnable prompt, BOUT `OutroCTA`. Confirmed via
   `./art scenes --check` that `BrutalistHesitantWriter`, `ClaudeComposerAsk`,
   `WantQuote`, and `OutroCTA` are all RENDERABLE before slating (GATE L).
4. Wrote `scenes.py` (three custom Manim scenes: B01 "a skill is a folder"
   — eight-item file listing, B02 "how it runs" pipeline, B03 "five things
   this skill covers") and `render_scenes.py`, adapted from the
   `claude-liam-build-zoom-bot` precedent's pattern with content rewritten
   for this topic.
5. Generated audio: `generate_audio_kokoro.py`, free, local, `am_onyx`.
   Measured durations became the clock: B00 12.76s, B01 15.02s, B02 9.34s,
   B03 18.73s, BCRY 14.12s, BHTF 15.64s, BOUT 5.10s.
6. Rendered the three Manim beats via `render_scenes.py` in the foreground.
7. Rendered the four Remotion beats via `remotion_scenes.py` in the
   foreground — all 4 succeeded on first attempt (B00 extended to 12.8s,
   BCRY to 14.1s, BHTF to 15.6s, BOUT to 5.1s).
8. Verified B00 directly before compiling: pulled a frame at t=11.5s — the
   correction ("agent" -> "app") is complete and legible, full question
   reads "Build me a Zoom contact center app?" `ffprobe` confirms
   `media/B00.mp4` = 12.77s with an audio track, clearing the >=8s TIMING
   LAW floor.
9. First `compile.py` pass -> 7/7 real (no slate), 91.7s. **GATE T
   (`type_check.py`) FAILED on first run**: B03's footer text measured 16px
   < the 20px floor. Fixed by increasing B03's row/footer font sizes in
   `scenes.py` (rows 25->28, footer 22->26 with a width-safe scale guard),
   re-rendered B03, recompiled — GATE T PASS on second run.
10. **Gate V (frame QC), first sweep:** pulled a frame from every beat and
    read each directly. Found a real defect in B01: the folder-tab outline
    struck through the "RUNBOOK.md" row at the top and clipped
    "troubleshooting/" at the bottom — the 8-row file list overflowed the
    fixed-height card (a leftover 3-item-card size copied from the
    zoom-bot precedent, never resized for 8 items). Fixed by sizing the
    card dynamically to `rows.height` with real margin and positioning the
    tab and captions relative to the card's actual top/bottom instead of
    hardcoded coordinates. Also caught the fix's side effect: B01's Manim
    scene still targeted its old borrowed 18.6s internal duration against
    a 15.02s narration track, so `compile.py` was center-cropping 1.8s off
    each end of B01 (chopping into the middle of the row fade-in
    animation) — retargeted the scene's internal wait to 14.9s to match
    the measured audio, eliminating the crop. Re-rendered B01, recompiled,
    re-ran GATE T (PASS) and a full second frame sweep of all 7 beats — no
    further defects. (BOUT/`OutroCTA` renders on flat white, not the
    humanitarians cream ground — the same shared-component quirk already
    logged unfixed on every sibling in this factory, e.g.
    `knowledge-work-plugins--claude-liam-build-zoom-bot`; not a new
    defect.)
11. Final master verified directly, independent of `compile.py`'s
    self-report: `ffprobe` confirms one video stream (3840x2160, matches
    4K LAW) and one audio stream; `ffmpeg -af volumedetect` confirms
    mean_volume -24.0 dB / max -2.9 dB; `stat` confirms the `.mp4`
    (15:01:58) is newer than `beat_sheet.json` (14:52:12) — all
    COMPLETION LAW conditions met.

## Gates

- **TIMING LAW (B00):** narration 32 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **12.76s**, clears the >=8s floor.
  Correction ("agent" -> "app") visible on-screen by t=11.5s.
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840x2160).
- **GATE T (`type_check.py`):** FAILED first run (B03 min-size, 16px <
  20px floor) — fixed in `scenes.py`, **PASS on second run**, 0 FAILs.
- **Gate V (frame QC):** full beat sweep, all 7 beats read directly. First
  sweep found and fixed a real defect (B01 folder-tab/text overlap +
  center-crop mismatch, see above); second sweep clean.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg `volumedetect` via
  `compile.py`, independently re-verified via direct `ffmpeg`/`ffprobe`
  call — well above the -40 dB floor).

## Playlist resolution

`family: "knowledge-work-plugins"` matches `playlists.json` directly ->
**"Extending Claude — Skills, Plugins & Connectors"** (no fallback needed).

## Delivery

Phase 4 completed this invocation. The master is born natively at
3840x2160 via `compile.py`'s 4K LAW, so no separate 4K re-render was needed
— copied directly to
`knowledge-work-plugins--claude-liam-build-zoom-contact-center-app-4k.mp4`.
`deliver.py --push` staged
`DELIVERY/knowledge-work-plugins--claude-liam-build-zoom-contact-center-app/`
(4K master + description) for the Drive sync, and committed + pushed
`claude-bear/knowledge-work-plugins--claude-liam-build-zoom-contact-center-app/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no media) to `humanitarians-youtube`.
`HAILOOP-LOG.md` updated with the matching entry.
