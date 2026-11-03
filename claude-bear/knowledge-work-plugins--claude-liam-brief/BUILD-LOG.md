# BUILD-LOG — knowledge-work-plugins--claude-liam-brief

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-brief/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel walking through the `brief`
Anthropic skill — a legal-work briefing generator). This invocation found
Phase 1 and Phase 2 already complete (QUESTION.md, CARRY-OUT.md, SCRIPT.md,
beat_sheet.json, audio, and B01–B03 Manim renders all present on disk from a
prior pass) and continued from there rather than re-authoring.

**Register re-registered Teardown -> Plain**, matching every sibling in this
factory: the source graded the skill ("what it gets right… what it bites")
and framed a "Verdict" card; this redo states the three-mode boundary as
fact (no grading language) and folds the verdict into a `WantQuote`
carry-out beat. B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "news" -> "briefings" — the newcomer
assumption that a legal briefing means outside news on a schedule, corrected
to a scan of the user's own materials). Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. BHTF's prompt was rewritten clean —
the source's handoff string was truncated/garbled and referenced a skill
file the general viewer won't have installed; this version asks Claude
directly to run the same triage, no plugin dependency.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat is AI-VIDEO, pantry, or a
human-drop slot.

## Built end to end this invocation

1. Verified prior-pass state: audio already generated for all 7 beats
   (`generate_audio_kokoro.py`, free, `am_onyx`) — measured durations B00
   10.75s, B01 14.89s, B02 9.34s, B03 19.56s, BCRY 9.81s, BHTF 15.81s, BOUT
   4.33s. B01–B03 Manim already rendered. `media/B00.mp4` already rendered
   and verified directly: pulled a frame at t=8s — the correction ("news" ->
   "briefings") is complete and legible, full question reads "Can Claude
   email me legal briefings every morning?" `ffprobe` confirms
   `media/B00.mp4` = 10.77s with an audio track, clearing the >=8s TIMING
   LAW floor.
2. Rendered the three remaining REMOTION beats (BCRY, BHTF, BOUT) via
   `remotion_scenes.py` in the foreground. The render exceeded the tool's
   default inline timeout and was moved to a tracked background task by the
   harness; per the COMPLETION LAW (never end a turn on an unsupervised
   render), blocked on it directly via `TaskOutput(block=true)` until the
   task-completion notification confirmed exit code 0 — 2/2 new beats
   rendered clean (B00/BOUT were already filled from the prior pass).
3. First `compile.py` pass -> 7/7 real (no slate), master
   `knowledge-work-plugins--claude-liam-brief.mp4`, 85.5s, mean_volume
   -23.9 dB.
4. **Gate V found a real defect on first sweep**: BHTF's `ClaudeComposerAsk`
   topic prop was authored as `"LEGAL BRIEFING · ANTHROPIC SKILL · YOUR
   TURN"` — the template sibling (`claude-liam-simple-delve`) never appends
   the segment name to the topic kicker (the `segment` prop already carries
   "Your Turn" on its own line). At 44 chars with the kicker's uppercase
   letter-spacing, this wrapped the topic to two lines and overlapped the
   "Your Turn" segment title beneath it. **Fix:** trimmed `topic` back to
   `"LEGAL BRIEFING · ANTHROPIC SKILL"` (matching the template's pattern),
   re-rendered BHTF, recompiled. Frame re-pull confirmed the kicker and
   segment title now sit on separate lines with no collision.
5. **GATE T (`type_check.py`) found a second real defect**: B03's min-size
   check (§8.1) failed at 18px < the 20px floor. Two blind fix attempts
   (raising the "nothing outside this list" caption's font_size/opacity)
   left the reported number unchanged — a strong signal the flagged text run
   wasn't the caption at all. Diagnosed directly by running the checker's
   own blob-detection functions (`ink_mask`/`labeled_blobs`/`text_run_bboxes`)
   against the raw frame: the 18px blob was an isolated x-height-only
   fragment of the word "own" in row 2 ("...your own sources") — an
   all-lowercase substring with no ascenders or descenders naturally
   measures shorter than mixed-case text at the same font_size, and this
   particular row happened to isolate one. Separately discovered along the
   way: fading text via Manim `set_opacity()` pushes the blended pixel color
   outside the checker's ink/mute detection tolerance entirely, so a
   low-opacity caption is measured as a scatter of disconnected fragments
   rather than one glyph run — the correct pattern (per the checker's own
   source comments) is full-opacity `MUTE` (`#5D584F`) for de-emphasized
   annotations, not opacity-faded `INK`. Applied both fixes: item rows
   25px -> 30px font_size (clears the x-height floor with margin), and the
   "nothing outside this list" caption recolored to full-opacity MUTE.
   Re-rendered B03, recompiled, re-ran `type_check.py`: **GATE T PASS**, 0
   FAILs.
6. Gate V re-verified after both fixes: pulled a frame from each of the 7
   beats plus targeted re-checks of BHTF and B03. All legible, correct
   contrast, no text overlap, no clipping, safe inset respected, correct
   @HumanitariansAI branding throughout. (BOUT/`OutroCTA` renders on flat
   white, not the humanitarians cream ground — same shared-component note
   already logged unfixed on every sibling in this factory, e.g.
   `claude-for-legal--claude-liam-nda-review`.)
7. Final master verified directly: `knowledge-work-plugins--claude-liam-brief.mp4`
   is 3840x2160, 85.5s, mean_volume -23.9 dB (max -2.8 dB), mtime newer than
   `beat_sheet.json` (13:59:19 vs 13:47:43) — the COMPLETION LAW conditions
   are all met.

## Gates

- **TIMING LAW (B00):** narration ~34 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **10.75s** (rendered 10.77s), clears the
  >=8s floor. Correction ("news" -> "briefings") visible on-screen by t=8s.
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840x2160).
- **GATE T (`type_check.py`):** PASS after 2 fix iterations — see defect #2
  above. 0 FAILs on final run.
- **Gate V (frame QC):** full beat sweep, all 7 beats read directly at
  least once, BHTF and B03 re-checked after their respective fixes. Two
  real defects found and fixed (BHTF kicker/segment overlap, B03 min-size);
  clean on final pass.
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (ffmpeg `volumedetect` via
  `compile.py`, independently re-verified via direct `ffprobe`/`ffmpeg`
  call — well above the -40 dB floor).

## Playlist resolution

`family: "knowledge-work-plugins"` matches `playlists.json` directly ->
**"Extending Claude — Skills, Plugins & Connectors"** (no fallback needed).

## Delivery

Phase 4 completed this invocation. The master is born natively at
3840x2160 via `compile.py`'s 4K LAW, so no separate 4K re-render was
needed — copied directly to `knowledge-work-plugins--claude-liam-brief-4k.mp4`.
`deliver.py --push` staged `DELIVERY/knowledge-work-plugins--claude-liam-brief/`
(4K master + description) for the Drive sync, and committed + pushed
`claude-bear/knowledge-work-plugins--claude-liam-brief/` (README.md,
beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md, CARRY-OUT.md,
QUESTION.md — no media) to `humanitarians-youtube` (commit `f42a1e5a`),
clean, no conflicts. `HAILOOP-LOG.md` updated with the matching entry.
