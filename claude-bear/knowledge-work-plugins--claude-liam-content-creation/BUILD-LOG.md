# BUILD-LOG — knowledge-work-plugins--claude-liam-content-creation

## 2026-09-03 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-content-creation/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel walking through the
`content-creation` Anthropic skill — a marketing-content drafting tool).
Only `SUBJECT.json` existed on pickup; everything below was built fresh
this invocation, using the same-family, already-delivered
`knowledge-work-plugins--claude-liam-brief` sibling as the exact
structural precedent (identical source shape: skill-teardown, 7 beats,
source already all-Remotion).

**Register re-registered Teardown -> Plain**: the source graded the skill
("what it gets right… what it bites") and framed a "Verdict" card; this
redo states the six-format boundary as fact (no grading language) and
folds the verdict into a `WantQuote` carry-out beat. B00 replaced the
source's `ClaudeComposerAsk` cold open with `BrutalistHesitantWriter`
(WRITER LAW: "blog"->"marketing", "post"->"content" — the newcomer
assumption that this is a blog-writing tool, corrected to a multi-channel
marketing-content system). Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off. BHTF's prompt was rewritten
clean — the source's handoff string was truncated/garbled and referenced a
skill file the general viewer won't have installed; this version asks
Claude directly to draft the same announcement across three channels and
compare the shapes, which doubles as a live test of the reel's own claim.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat is AI-VIDEO, pantry, or a
human-drop slot — the source was already all-Remotion (`ClaudeComposerAsk`
x2, three `SkillTeardown*` cards, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so the law required no substitution beyond the WRITER
LAW and channel-skin row it already mandates.

## Built end to end this invocation

1. Wrote `QUESTION.md` and `CARRY-OUT.md` before any narration (Plain
   register: carry-out written first, then the reel reverse-engineered to
   land it). Wrong guess: "content creation" means one universal piece of
   copy pasted everywhere. Correction: six distinct channel formats (blog,
   social, email, landing page, press release, case study), each with its
   own shape, from one instruction file.
2. Wrote `SCRIPT.md` (7-beat table, redo audit, register audit, deliberately
   -not-claimed section) and `beat_sheet.json`, matching the source's exact
   7-beat count (B00, B01, B02, B03, BVDT->BCRY, BHTF, BOUT). GATE L
   checked all four reused Remotion components before slating —
   `BrutalistHesitantWriter`, `ClaudeComposerAsk`, `WantQuote`, `OutroCTA`
   all RENDERABLE with matching props (`./art scenes --check`).
3. Generated audio: `generate_audio_kokoro.py`, free, `am_onyx`. Measured
   durations: B00 12.10s, B01 15.51s, B02 11.63s, B03 18.09s, BCRY 8.64s,
   BHTF 17.19s, BOUT 4.74s.
4. Wrote `scenes.py` / `render_scenes.py` for the three GRAPHIC beats
   (B01 anatomy, B02 pipeline, B03 constraint — six-format list), Manim,
   humanitarians palette, durations matched to measured audio. Rendered
   all three in the foreground — clean on first pass.
5. Rendered the four REMOTION beats via `remotion_scenes.py`. The render
   exceeded the tool's 120s inline timeout and was moved to a tracked
   background task by the harness; per the COMPLETION LAW (never end a
   turn on an unsupervised render), blocked on it directly via
   `TaskOutput(block=true)` until the task-completion notification
   confirmed exit code 0 — 4/4 beats rendered clean (B00, BCRY, BHTF,
   BOUT). Verified `media/B00.mp4` directly: `ffprobe` confirms 12.10s
   with audio+video tracks, clearing the >=8s TIMING LAW floor; a frame
   pull at t=10s shows both corrections complete and legible — "Can Claude
   write my marketing content?".
6. First `compile.py` pass -> 7/7 real (no slate), master
   `knowledge-work-plugins--claude-liam-content-creation.mp4`, 88.9s,
   mean_volume -24.0 dB.
7. **GATE T (`type_check.py`) found a real defect on first run**: B03's
   min-size check (§8.1) failed at 18px < the 20px floor (a lowercase
   substring in one of the six item rows, same defect class already logged
   on the `claude-liam-brief` sibling). **Fix:** bumped B03's item-row,
   "nothing outside this list", and footer font sizes (26->32, 28->32,
   24->30) in `scenes.py`, re-rendered B03, recompiled. Re-ran
   `type_check.py`: **GATE T PASS**, 0 FAILs.
8. Gate V: pulled a frame from all 7 beats (B00 mid-typing + t=10s
   settled, B01, B02, B03 post-fix, BCRY, BHTF, BOUT) and read each
   directly. All legible, correct contrast, no text overlap, no clipping,
   safe inset respected, correct @HumanitariansAI branding throughout.
   (BOUT/`OutroCTA` renders on flat white, not the humanitarians cream
   ground — same shared-component note already logged unfixed on every
   sibling in this factory, e.g. `knowledge-work-plugins--claude-liam-brief`.)
9. Final master verified directly: 3840x2160 (born natively via
   compile.py's 4K LAW), 88.9s, mean_volume -24.0 dB (max -3.0 dB), mtime
   newer than `beat_sheet.json` — the COMPLETION LAW conditions are all
   met.

## Gates

- **TIMING LAW (B00):** narration 32 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **12.10s**, clears the >=8s floor. Both
  corrections ("blog"->"marketing", "post"->"content") visible and settled
  on-screen by t=10s.
- **content-check / frame-check / lane-check:** all PASS per `compile.py`
  output (7/7 beats, no violations, canvas 3840x2160).
- **GATE T (`type_check.py`):** PASS after 1 fix iteration — B03 min-size
  (§8.1), see defect #7 above. 0 FAILs on final run.
- **Gate V (frame QC):** full beat sweep, all 7 beats read directly, B03
  re-checked after its fix. One real defect found and fixed; clean on
  final pass.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg `volumedetect` via
  `compile.py`, independently re-verified via direct `ffprobe`/`ffmpeg`
  call — well above the -40 dB floor).

## Playlist resolution

`family: "knowledge-work-plugins"` matches `playlists.json` directly ->
**"Extending Claude — Skills, Plugins & Connectors"** (no fallback needed).

## Delivery

Phase 4 pending as of this log entry — the review cut is DONE and passes
every gate; 4K master + `deliver.py --push` to follow in this same
invocation.
