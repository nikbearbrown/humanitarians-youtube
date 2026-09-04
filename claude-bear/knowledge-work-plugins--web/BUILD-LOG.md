# BUILD-LOG — knowledge-work-plugins--web

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-contact-center/web/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel walking through the
`contact-center/web` Anthropic skill — a partner-built Zoom skill for the
Zoom Contact Center Web SDK). This invocation started from a bare
`SUBJECT.json` (no prior-pass artifacts) and built the reel end to end.

**Register re-registered Teardown -> Plain**, matching every sibling in this
factory: the source graded the skill ("what it gets right: repeatable
results. what it bites: anything outside the spec") and framed a "Verdict"
card; this redo states the same scope boundary as fact (no grading
language) and folds the verdict into a `WantQuote` carry-out beat. B00
replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "widget" -> "SDK" — the newcomer
assumption that "Contact Center, web" means a ready-made, drop-in chat
widget, corrected to the actual mechanism: Claude wires the SDK's events
into the viewer's own site). Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. BHTF's prompt was rewritten clean —
the source's handoff string was truncated/garbled ("...use for web
chat/video/campaign embed. Read the contact-center/web skill and walk me
through what you will do before you do it.") and referenced a skill file
the general viewer won't have installed; this version asks Claude directly
to walk through the same scope (events, app context, postMessage), no
plugin dependency. Built from the nearest precedent in this exact family
(`knowledge-work-plugins--claude-liam-build-zoom-contact-center-app`, also
a redo of a skill-teardown reel from the same source series), matching its
conventions exactly (humanitarians palette #F3EBDD/#2F2A26/#E4572E/#1F4E5F,
chip-row / pipeline / checklist Manim scenes, `WantQuote` carry-out,
`OutroCTA` close).

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette.
No beat is AI-VIDEO, pantry, or a human-drop slot — the source was already
all-Remotion (`ClaudeComposerAsk` x2, three `SkillTeardown*` cards,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so no substitution was
required beyond the WRITER LAW and channel-skin row hai-simple already
mandates.

## Built end to end this invocation

1. Read the source sheet in full (locked facts: contact-center/web is a
   partner-built (Zoom) skill for the Zoom Contact Center SDK for Web — web
   chat/video/campaign embeds, engagement event handling, app-context
   integrations, and Smart Embed postMessage workflows; a skill = a folder
   Claude reads before acting, 6 items — RUNBOOK.md, SKILL.md, concepts/,
   examples/, references/, troubleshooting/; execution is linear — read
   SKILL.md, execute steps in order, return result; source had no
   SCRIPT.md, so `beats[*].narration_text` served as the locked script).
   Read the structure template (`claude-liam-simple-delve`) and the nearest
   built precedent in this exact family
   (`knowledge-work-plugins--claude-liam-build-zoom-contact-center-app`) to
   match conventions exactly, plus the `claude-plugins-official--claude-liam-agent-development`
   sibling for the general redo-audit format.
2. Wrote `QUESTION.md` and `CARRY-OUT.md` before any narration (Step 0):
   carry-out line is "Contact Center, web doesn't hand you a drop-in chat
   widget — it wires the Zoom Web SDK's chat, video, and campaign embeds
   into your own site through events, context, and postMessage, the same
   way every time," defeating the wrong guess that "Contact Center, web"
   means a finished, ready-made chat widget.
3. Authored `SCRIPT.md` (Plain register, 7 beats matching the source's beat
   count) and `beat_sheet.json` (via `build_beat_sheet.py`) — B00
   `BrutalistHesitantWriter` (humanitarians palette, trigger "widget" ->
   replacement "SDK", 31-word narration + `lead_silence_s` 0.8 per TIMING
   LAW), B01/B02/B03 as GRAPHIC/Manim (anatomy, pipeline, four-item scope),
   BCRY `WantQuote` carry-out, BHTF `ClaudeComposerAsk` your-turn, BOUT
   `OutroCTA`. Confirmed via `./art scenes --check` that
   `BrutalistHesitantWriter`, `WantQuote`, `ClaudeComposerAsk`, and
   `OutroCTA` are all RENDERABLE before slating (GATE L).
4. Wrote `scenes.py` (three Manim scenes: B01 "a skill is a folder" —
   six-item file listing sized dynamically to its row count, B02 "how it
   runs" pipeline, B03 "what this skill covers" four-item scope checklist)
   and `render_scenes.py`, adapted from the `build-zoom-contact-center-app`
   precedent's pattern with content rewritten for this topic.
5. Generated audio: `generate_audio_kokoro.py`, free, local, `am_onyx`.
   Measured durations became the clock: B00 10.75s, B01 14.04s, B02 9.34s,
   B03 21.44s, BCRY 12.25s, BHTF 16.94s (pre-fix), BOUT 5.38s.
6. Rendered the three Manim beats via `render_scenes.py` in the foreground
   — all 3 succeeded on first attempt.
7. Rendered the four Remotion beats via `remotion_scenes.py` — exceeded the
   tool's 120s timeout and was moved to background by the harness
   automatically; blocked on it via `TaskOutput(block=true)` per the
   one-shot COMPLETION LAW's foreground-render rule before proceeding,
   confirmed exit code 0 with all four beats reporting `ok`.
8. Verified B00 directly before compiling: pulled a frame at t=9.5s — the
   correction ("widget" -> "SDK") is complete and legible, full question
   reads "How do I add a chat SDK to my website?" `ffprobe` confirmed
   `media/B00.mp4` = 10.77s with an audio track, clearing the >=8s TIMING
   LAW floor.
9. First `compile.py` pass -> 7/7 real (no slate), 91.1s. GATE T
   (`type_check.py`) **PASS, 0 FAILs on the first run**.
10. **Gate V (frame QC), first sweep found a real defect not caught by
    GATE T**: pulled frames every ~6s across the full 91.1s runtime plus a
    targeted late-frame pull on BHTF. BHTF's on-screen composer text was
    truncated mid-sentence ("...Walk me through the", the remaining ~84
    characters never appearing) — `ClaudeComposerAsk`'s composer card caps
    the input area to 3 visible lines (`overflow: hidden`, `maxHeight:
    CMD*1.45*3`) regardless of how long the typed `command` prop is, and
    the drafted prompt (240 characters) needed ~5 lines to fully display.
    Verified this is a **pre-existing, previously-uncaught defect shared
    across the family**: pulled the same-beat frame from the
    `knowledge-work-plugins--claude-liam-build-zoom-contact-center-app`
    sibling's already-delivered `media/BHTF.mp4` and confirmed its 220-
    character prompt is truncated identically ("...where version-drift",
    the rest never appearing), despite that sibling's own BUILD-LOG.md
    recording Gate V as clean ("paste-ready prompt text legible") — the
    truncation was missed because the narration audio does read the full
    text aloud, masking the on-screen clip. Root-caused to the component,
    not the content: any `command` needing more than ~155 characters (at
    this canvas/topic-length combination) will silently clip. Fixed for
    this reel (not the sibling, which is out of scope for this build) by
    shortening BHTF's on-screen `command` AND its matching narration
    (`narration_text`) together to 153 characters, so what Liam reads
    aloud matches what's on screen exactly, and the full prompt now
    displays. Patched only the BHTF beat's two fields directly in
    `beat_sheet.json` (not a full `build_beat_sheet.py` re-run, which would
    have discarded the other 6 beats' already-measured audio durations and
    render stamps), regenerated BHTF's audio only (`--only BHTF`, 13.23s),
    re-rendered BHTF only (`remotion_scenes.py --only BHTF --force`,
    exceeded 120s timeout, backgrounded, blocked via `TaskOutput` before
    proceeding, exit 0), frame-verified the fix (full prompt "Walk me
    through adding Zoom Contact Center's web chat to my site — engagement
    events, app context, and Smart Embed postMessage — before I write any
    code." now fully legible), then recompiled (`compile.py --force`).
11. Re-ran GATE T on the recompiled master — **PASS, 0 FAILs**. Re-swept
    Gate V across the full recompiled 87.4s runtime (BHTF is now 13.2s vs.
    16.9s pre-fix): all 7 beats legible, safe-inset, single-accent, no
    overlap, correct topic/title/`@HumanitariansAI` handle throughout, zero
    further blockers.
12. Final master verified directly, independent of `compile.py`'s
    self-report: `ffprobe` confirms one video stream (3840x2160, matches 4K
    LAW) and one audio stream (aac); `ffmpeg -af volumedetect` confirms
    mean_volume -24.0 dB / max -2.8 dB; `stat` confirms the `.mp4`
    (04:21:36) is newer than `beat_sheet.json` (04:20:06) — all COMPLETION
    LAW conditions met.

## Gates

- **TIMING LAW (B00):** narration 31 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **10.75s** (10.77s in the final render),
  clears the >=8s floor. Correction ("widget" -> "SDK") visible on-screen
  by t=9.5s.
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840x2160).
- **GATE T (`type_check.py`):** PASS, 0 FAILs, both before and after the
  BHTF fix.
- **Gate V (frame QC):** full beat sweep, all 7 beats read directly. First
  sweep found and fixed a real defect (BHTF composer-card 3-line text
  clip, see above, also identified as a pre-existing unfixed defect on the
  `build-zoom-contact-center-app` sibling); second sweep clean.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg `volumedetect` via
  `compile.py`, independently re-verified via direct `ffmpeg`/`ffprobe`
  call — well above the -40 dB floor).

## Playlist resolution

`family: "knowledge-work-plugins"` matches `playlists.json` directly ->
**"Extending Claude — Skills, Plugins & Connectors"** (no fallback needed).

## Delivery

Phase 4 to be completed this invocation (see below for outcome).
