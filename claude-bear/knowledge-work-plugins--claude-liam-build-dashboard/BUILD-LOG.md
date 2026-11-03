# BUILD-LOG — knowledge-work-plugins--claude-liam-build-dashboard

## 2026-09-02 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-build-dashboard/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel walking through the
`build-dashboard` Anthropic skill — builds an interactive HTML dashboard
with charts, filters, and tables). Started from a bare `SUBJECT.json` — no
prior-pass artifacts existed — and built the reel end to end this
invocation.

**Register re-registered Teardown -> Plain**, matching every sibling in
this factory: the source graded the skill ("what it gets right… what it
bites") and framed a "Verdict" card; this redo states the four-situation
boundary as fact (no grading language) and folds the verdict into a
`WantQuote` carry-out beat. B00 replaced the source's `ClaudeComposerAsk`
cold open with `BrutalistHesitantWriter` (WRITER LAW: "app" -> "file" —
the newcomer assumption that "build a dashboard" means a live, hosted app,
corrected to a single self-contained file). Close re-skinned to `OutroCTA`
/ @HumanitariansAI with Liam's sign-off. BHTF's prompt was rewritten
clean — the source's handoff string named the internal `build-dashboard`
skill file (which the general viewer won't have installed) and truncated
its own use-case list mid-sentence; this version asks Claude directly to
build a dashboard from data the viewer already has, no plugin dependency.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat is AI-VIDEO, pantry, or a
human-drop slot. (The source was already all-Remotion — no ai-video-prompt
or pantry beat existed to replace beyond the WRITER LAW and channel-skin
substitutions the skill requires regardless.)

## Built end to end this invocation

1. Wrote `QUESTION.md`, `CARRY-OUT.md`, `SCRIPT.md`, `beat_sheet.json`
   (Phase 1/2) following the immediate sibling
   `knowledge-work-plugins--claude-liam-brief` as the structure template
   (same family, same source shape: anatomy -> pipeline -> constraint ->
   verdict, 7 beats).
2. `generate_audio_kokoro.py` — free, local, `am_onyx`, all 7 beats in one
   pass, no gate. Measured durations: B00 11.93s, B01 14.55s, B02 9.34s,
   B03 15.62s, BCRY 10.26s, BHTF 14.76s, BOUT 3.52s. **TIMING LAW check:**
   B00 narration (34 words) + `lead_silence_s` 0.8 measured at **11.93s**,
   clearing the >=8s floor with room for the writer to reach its
   correction.
3. Wrote `scenes.py` (B01Scene/B02Scene/B03Scene, Manim) with `wait()`
   calls hand-tuned to the measured durations above, and `render_scenes.py`
   to drive them. Rendered all three in the foreground — clean, no
   failures.
4. Rendered the four REMOTION beats (B00, BCRY, BHTF, BOUT) via
   `remotion_scenes.py` in the foreground. The render exceeded the tool's
   120s inline timeout and was moved to a tracked background task by the
   harness; per the COMPLETION LAW (never end a turn on an unsupervised
   render), blocked on it directly via `TaskOutput(block=true)` until the
   task-completion notification confirmed exit code 0 — all 4 beats
   rendered clean on the first pass (`extended to` the audio-clock
   durations: B00 11.9s, BCRY 10.3s, BHTF 14.8s, BOUT 3.5s).
5. `compile.py` — 7/7 real (no slate) on the first pass. **4K LAW** forced
   the master natively to 2160p. content-check, frame-check, and
   lane-check all PASS. Master: 80.96s, mean_volume -24.1 dB.
6. **GATE T (`type_check.py`)**: PASS on the first run, 0 FAILs. B03's
   four-checkmark list came in at exactly the 20px min-size floor (vs.
   brief's three-item list at 22px) — passing but tight, logged here in
   case a future pass on this beat needs the item font bumped.
7. **Gate V (frame QC)**: pulled and read a frame from all 7 beats
   directly. B00 (late frame): correction "app" -> "file" fully complete
   and legible, question reads "Can Claude build me a live dashboard
   file?". B01: folder/SKILL.md anatomy card, clean. B02: three-card
   pipeline, clean. B03: four checkmarked situations + boundary line +
   "nothing outside this list", all legible, no overlap. BCRY: carry-out
   quote, clean. BHTF: `ClaudeComposerAsk` — kicker ("BUILD DASHBOARD ·
   ANTHROPIC SKILL") and "Your Turn" segment title sit on separate lines
   with no collision (kept the topic string short per the lesson logged on
   `claude-liam-brief`'s Gate V defect). BOUT: outro card + subscribe CTA,
   clean (renders on flat white, not the humanitarians cream ground — same
   shared-`OutroCTA`-component note already logged unfixed on multiple
   siblings in this factory, e.g. `claude-for-legal--claude-liam-nda-review`
   and `knowledge-work-plugins--claude-liam-brief`). **No defects found —
   clean on first pass, no fix iteration needed.**
8. Final master verified directly: `knowledge-work-plugins--claude-liam-build-dashboard.mp4`
   is 3840x2160, 80.96s, has an `aac` audio stream, mean_volume -24.1 dB
   (max -2.9 dB), mtime newer than `beat_sheet.json` (14:17:35 vs
   14:16:22) — the COMPLETION LAW conditions are all met.

## Gates

- **TIMING LAW (B00):** narration 34 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **11.93s** (rendered 11.9s), clears the
  >=8s floor. Correction ("app" -> "file") visible on-screen by the late
  frame.
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840x2160).
- **GATE T (`type_check.py`):** PASS, 0 FAILs, first run.
- **Gate V (frame QC):** full beat sweep, all 7 beats read directly. No
  defects found.
- **GATE AUDIO:** PASS, mean_volume **-24.1 dB** (ffmpeg `volumedetect` via
  `compile.py`, independently re-verified via direct `ffprobe`/`ffmpeg`
  call — well above the -40 dB floor).

## Playlist resolution

`family: "knowledge-work-plugins"` matches `playlists.json` directly ->
**"Extending Claude — Skills, Plugins & Connectors"** (no fallback
needed).

## Delivery

Phase 4 completed this invocation. The master is born natively at
3840x2160 via `compile.py`'s 4K LAW, so no separate 4K re-render was
needed — copied directly to
`knowledge-work-plugins--claude-liam-build-dashboard-4k.mp4`.
`deliver.py --push` staged
`DELIVERY/knowledge-work-plugins--claude-liam-build-dashboard/` (4K master
+ description) for the Drive sync, and committed + pushed
`claude-bear/knowledge-work-plugins--claude-liam-build-dashboard/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no media) to `humanitarians-youtube`.
`HAILOOP-LOG.md` updated with the matching entry.
