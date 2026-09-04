# BUILD-LOG — knowledge-work-plugins--claude-liam-data-context-extractor

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-data-context-extractor/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel walking through the
`data-context-extractor` Anthropic skill). Started from a bare
`SUBJECT.json` — no prior-pass artifacts existed — and built the reel end
to end this invocation.

### Source defect, disclosed up front

The source sheet's narration is generated from a template that substitutes
the skill's one-line description into four beats (B00, B03, BVDT, BHTF).
Comparing against the sibling `claude-liam-build-dashboard` (same family,
same template, substitution present and correct there — "Build an
interactive HTML dashboard with charts, filters, and tables. Use when
creating an executive overview...") confirmed this: in
`claude-liam-data-context-extractor`'s source, that substitution never ran.
All four occurrences read as a bare `>` where the description belongs. The
one fragment that IS genuine text in the source, not a placeholder, is the
lead-in clause itself — **"Generate or improve a company-specific data
analysis skill by"** — repeated verbatim across all four beats before the
`>`.

Per the REDO LAW ("keep its question, its facts... the source is a LOCKED
SCRIPT"), this build carries that confirmed fragment forward as the skill's
stated job and does **not** invent a completion for the missing clause, and
does **not** fabricate an enumerated use-case list the way `build-dashboard`
legitimately preserved a real one (four situations, actually present in
that source). Where `build-dashboard` had facts to lock, this source
genuinely has none beyond the generic skill mechanics (folder, SKILL.md,
linear execution, same-input-same-output boundary) that are also stated,
intact, elsewhere in the same source and are true of every Claude skill.
This reasoning is written out in full in `QUESTION.md`.

**Register re-registered Teardown -> Plain**, matching every sibling in
this factory: the source graded the skill ("what it gets right… what it
bites") and framed a "Verdict" card; this redo states the definitions-only
boundary as fact (no grading language) and folds the verdict into a
`WantQuote` carry-out beat. B00 replaced the source's `ClaudeComposerAsk`
cold open with `BrutalistHesitantWriter` (WRITER LAW: "automatically" ->
"once I write it down" — the newcomer assumption that Claude reads company
data on its own, corrected to a written, one-time context file). Close
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off. BHTF's
prompt was rewritten clean — the source's handoff string named the
internal `data-context-extractor` skill file (which the general viewer
won't have installed) and carried the same broken `>` fragment mid-sentence
("I want to >. Read the data-context-extractor skill..."); this version
asks Claude directly to turn a plain rundown of the viewer's own data into
a written skill file, no plugin dependency.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat is AI-VIDEO, pantry, or a
human-drop slot. (The source was already all-Remotion — no ai-video-prompt
or pantry beat existed to replace beyond the WRITER LAW and channel-skin
substitutions the skill requires regardless.)

## Built end to end this invocation

1. Wrote `QUESTION.md`, `CARRY-OUT.md`, `SCRIPT.md`, `beat_sheet.json`
   (Phase 1/2), using the immediate sibling
   `knowledge-work-plugins--claude-liam-build-dashboard` as the structure
   template (same family, same source shape: anatomy -> pipeline ->
   constraint -> verdict, 7 beats) — and its BUILD-LOG as the model for how
   to disclose a source-content gap honestly instead of inventing facts.
2. `generate_audio_kokoro.py` — free, local, `am_onyx`, all 7 beats in one
   pass, no gate. Measured durations: B00 10.5s, B01 16.45s, B02 9.34s, B03
   15.62s, BCRY 9.83s, BHTF 15.08s, BOUT 3.99s. **TIMING LAW check:** B00
   narration (31 words) + `lead_silence_s` 0.8 measured at **10.5s**,
   clearing the >=8s floor with room for the writer to reach its
   correction.
3. Wrote `scenes.py` (B01Scene/B02Scene/B03Scene, Manim) with `wait()`
   calls hand-tuned to the measured durations above, and `render_scenes.py`
   to drive them. Rendered all three in the foreground — clean, no
   failures.
4. Rendered the four REMOTION beats (B00, BCRY, BHTF, BOUT) via
   `remotion_scenes.py` in the foreground (no `--concurrency` flag — this
   checkout's version doesn't accept one; ran to completion in-process,
   never backgrounded, per the COMPLETION LAW). All 4 beats rendered clean
   on the first pass, extended to the audio-clock durations (B00 10.5s,
   BCRY 9.8s, BHTF 15.1s, BOUT 4.0s).
5. `compile.py` — 7/7 real (no slate) on the first pass. **4K LAW** forced
   the master natively to 2160p. content-check, frame-check, and
   lane-check all PASS. GATE AUDIO: PASS, mean_volume -24.0 dB.
6. **GATE T (`type_check.py`)**: FAIL on the first run — B01's overflow
   §8.2, 2 text runs outside the title-safe box (a third caption line I'd
   added pushed the block too low). Fixed by trimming B01's caption back to
   two lines matching the sibling's proven layout, re-rendered B01 only,
   recompiled, reran GATE T: **PASS, 0 FAILs**.
7. **Gate V (frame QC)**: pulled and read a frame from all 7 beats
   directly (mid/late in each beat's window). B00 (late frame): correction
   "automatically" -> "once I write it down" fully complete and legible,
   question reads "Does Claude read my company's data once I write it
   down?". B01: folder/SKILL.md anatomy card with the two-line caption,
   clean, no overflow. B02: three-card pipeline, clean. B03: three
   definition rows + boundary line + "outside the file's context" +
   footer, all legible, no overlap. BCRY: carry-out quote, clean. BHTF:
   `ClaudeComposerAsk` — topic line and "Your Turn" segment title on
   separate lines, no collision; prompt text fully readable. BOUT: outro
   card + subscribe CTA, clean (renders on flat white, not the
   humanitarians cream ground — the same shared-`OutroCTA`-component note
   already logged unfixed on multiple siblings in this factory, e.g.
   `claude-for-legal--claude-liam-nda-review` and this family's own
   `knowledge-work-plugins--claude-liam-build-dashboard`). No other
   defects found.
8. Final master verified directly:
   `knowledge-work-plugins--claude-liam-data-context-extractor.mp4` is
   3840x2160, 81.82s, has an `aac` audio stream, mean_volume -24.0 dB (max
   -2.8 dB), mtime newer than `beat_sheet.json` — the COMPLETION LAW
   conditions are all met.

## Gates

- **TIMING LAW (B00):** narration 31 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **10.5s**, clears the >=8s floor. Correction
  ("automatically" -> "once I write it down") visible on-screen by the
  late frame.
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840x2160).
- **GATE T (`type_check.py`):** FAIL -> fixed (B01 overflow) -> PASS, 0
  FAILs on the second run.
- **Gate V (frame QC):** full beat sweep, all 7 beats read directly. No
  defects found beyond the pre-existing, already-logged OutroCTA
  background note.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg `volumedetect` via
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
`knowledge-work-plugins--claude-liam-data-context-extractor-4k.mp4`.
`deliver.py --push` staged
`DELIVERY/knowledge-work-plugins--claude-liam-data-context-extractor/` (4K
master + description) for the Drive sync, and committed + pushed
`claude-bear/knowledge-work-plugins--claude-liam-data-context-extractor/`
(README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md,
CARRY-OUT.md, QUESTION.md — no media) to `humanitarians-youtube`.
`HAILOOP-LOG.md` updated with the matching entry.
