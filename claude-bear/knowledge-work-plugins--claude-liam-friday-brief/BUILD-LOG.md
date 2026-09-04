# BUILD-LOG — knowledge-work-plugins--claude-liam-friday-brief

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-friday-brief/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel walking through the
`friday-brief` Anthropic skill — a small-business end-of-week pulse
generator). This invocation found only `SUBJECT.json` on disk; every other
artifact (QUESTION.md, CARRY-OUT.md, SCRIPT.md, beat_sheet.json, audio,
Manim, Remotion, compiled master, GATE T) was authored and built fresh in
this pass.

**Register re-registered Teardown -> Plain**, matching every sibling in this
factory (e.g. `knowledge-work-plugins--claude-liam-brief`, the exact same
family, redone 2026-09-02): the source graded the skill ("what it gets
right… what it bites") and framed a "Verdict" card; this redo states the
skill's four-field boundary as fact (no grading language) and folds the
verdict into a `WantQuote` carry-out beat. B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` (WRITER LAW:
"news" -> "numbers" — the newcomer assumption that a Friday brief means
outside market news on a schedule, corrected to the business's own sales
numbers). Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's
sign-off. BHTF's prompt was rewritten clean — the source's handoff string
was truncated/garbled ("I want to delivers the friday end-of-week pulse —
revenue vs prior week, top sellers, wins. Read the friday-brief skill…")
and referenced a skill file the general viewer won't have installed; this
version asks Claude directly to run the same weekly check, no plugin
dependency.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat is AI-VIDEO, pantry, or a
human-drop slot. The source was already all-Remotion (`ClaudeComposerAsk` x
2, three `SkillTeardown*` cards, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`),
so no substitution beyond the WRITER LAW and channel-skin row was required.

## Built end to end this invocation

1. Read the source sheet + the `claude-liam-brief` sibling (same family,
   already DONE) as the concrete redo template — its structure, prop
   shapes, and BUILD-LOG were used to keep this redo consistent with the
   rest of the factory.
2. Wrote `QUESTION.md`, `CARRY-OUT.md`, `SCRIPT.md` (Step 0/0.5 equivalents
   for hai-simple — no host prompt, since B00 is Remotion), then
   `beat_sheet.json` (7 beats matching the source's beat count), `scenes.py`
   (B01/B02/B03 Manim, adapted from the sibling's helpers), and
   `render_scenes.py`.
3. Generated audio: `generate_audio_kokoro.py`, free, local, `am_onyx`.
   Measured durations: B00 11.63s, B01 14.85s, B02 9.34s, B03 16.79s, BCRY
   10.62s, BHTF 16.92s, BOUT 4.05s.
4. Rendered the three Manim beats (`render_scenes.py`, foreground) — clean,
   0 failures.
5. Rendered the four Remotion beats (`remotion_scenes.py`, foreground). The
   render exceeded the tool's default inline timeout and was moved to a
   tracked background task by the harness; per the COMPLETION LAW (never end
   a turn on an unsupervised render), blocked on it directly via
   `TaskOutput(block=true)` until the task-completion notification confirmed
   exit code 0 — all 4 beats rendered clean (B00 extended to 11.6s, BCRY to
   10.6s, BHTF to 16.9s, BOUT to 4.0s).
6. `compile.py` — first pass, 7/7 real (no slate). content-check PASS,
   frame-check PASS (canvas 3840x2160), lane-check PASS. Master
   `knowledge-work-plugins--claude-liam-friday-brief.mp4`, 85.2s,
   GATE AUDIO PASS mean_volume -24.0 dB.
7. **GATE T (`type_check.py`)**: PASS on first run, 0 FAILs across all 9
   checks (min-size, overflow, contrast, contrast-local, bbox-overlap,
   card-clip, kerning, no-wordy-card, redundancy-advisory). No fix
   iterations needed — see `TYPECHECK.md`.
8. **Gate V (frame QC)**: pulled and read a frame from every beat, plus a
   late frame (t=8s) from B00 specifically to confirm the TIMING LAW
   correction. All 7 read clean: B00's writer types "Can Claude send me
   Friday news every week?", "news" visibly corrects to "numbers" by t=8s
   (well inside the >=8s floor); B01 folder/SKILL.md anatomy legible; B02
   three-phase pipeline legible, arrows clear; B03's four checkmarked
   fields (revenue, top sellers, wins, watches) plus the "nothing outside
   this list" boundary caption all legible with no overlap; BCRY carry-out
   sentence alone, serif, large; BHTF's `ClaudeComposerAsk` kicker
   ("FRIDAY BRIEF · ANTHROPIC SKILL") and "Your Turn" segment title sit on
   separate lines with no collision (the sibling's B_HTF kicker/segment
   overlap defect, avoided here by keeping the topic prop short per the
   template pattern); BOUT reads the title + "Liam, in for Bear." + Subscribe
   + @HumanitariansAI. No legibility, safe-inset, or text-overlap defects
   found — zero fix iterations needed on this pass. (BOUT/`OutroCTA` renders
   on flat white, not the humanitarians cream ground — same shared-component
   note already logged unfixed on every sibling in this factory, e.g.
   `knowledge-work-plugins--claude-liam-brief`.)
9. Final master verified directly: `ffprobe` confirms 3840x2160, 85.208s,
   audio + video streams present; `ffmpeg volumedetect` confirms mean_volume
   **-24.0 dB** / max -2.7 dB (well above the -40 dB floor); mtime newer than
   `beat_sheet.json` (22:30:19 vs 22:28:39). COMPLETION LAW conditions all
   met.

## Gates

- **TIMING LAW (B00):** narration 34 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **11.63s**, clears the >=8s floor by a wide
  margin. Correction ("news" -> "numbers") visible on-screen well before
  t=8s.
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840x2160).
- **GATE T (`type_check.py`):** PASS, 0 FAILs, first run — no fix
  iterations required.
- **Gate V (frame QC):** full beat sweep, all 7 beats read directly, plus a
  targeted late-frame check on B00. Zero defects found on this pass.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg `volumedetect` via
  `compile.py`, independently re-verified via direct `ffprobe`/`ffmpeg`
  call — well above the -40 dB floor).

## Playlist resolution

`family: "knowledge-work-plugins"` matches `playlists.json` directly ->
**"Extending Claude — Skills, Plugins & Connectors"** (no fallback needed).

## Delivery

Phase 4 completed this invocation. The master is born natively at 3840x2160
via `compile.py`'s 4K LAW, so no separate 4K re-render was needed — copied
directly to `knowledge-work-plugins--claude-liam-friday-brief-4k.mp4`.
`deliver.py --push` staged
`DELIVERY/knowledge-work-plugins--claude-liam-friday-brief/` (4K master +
description) for the Drive sync, and committed the text artifacts
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no media) to `humanitarians-youtube` under
`claude-bear/knowledge-work-plugins--claude-liam-friday-brief/`.
`HAILOOP-LOG.md` updated with the matching entry.
