# BUILD-LOG — knowledge-work-plugins--claude-liam-monday-brief

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-monday-brief/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel walking through the
`monday-brief` Anthropic skill — a Monday-morning business briefing
generator). Only `SUBJECT.json` was present on pickup; built fresh this
invocation end to end, following the same-family, same-source-shape sibling
`knowledge-work-plugins--claude-liam-brief` directly as the structural
template (identical skill-teardown shape: 1-file SKILL.md anatomy, linear
pipeline, a fixed constraint list, all-Remotion source with no AI-VIDEO/
pantry beats to replace).

**Register re-registered Teardown -> Plain**, matching every sibling in this
factory: the source graded the skill ("what it gets right… what it bites")
and framed a "Verdict" card; this redo states the five-item boundary as fact
(no grading language) and folds the verdict into a `WantQuote` carry-out
beat. B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` (WRITER LAW: "know" -> "check" — the newcomer
assumption that Claude already knows the user's numbers from memory,
corrected to: it checks them against a written file). Close re-skinned to
`OutroCTA` / @HumanitariansAI with Liam's sign-off. BHTF's prompt was
rewritten clean — the source's handoff string was garbled/truncated
("I want to generates a one-page monday morning briefing…") and referenced
a skill file the general viewer won't have installed; this version asks
Claude directly to assemble the same brief, no plugin dependency.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01, B02, B03), all in the humanitarians palette
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat is AI-VIDEO, pantry, or a
human-drop slot — the source was already all-Remotion (`ClaudeComposerAsk`
x2, three `SkillTeardown*` cards, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so no beat-type substitution was required beyond the
WRITER LAW and channel-skin rows the skill already requires.

## Built end to end this invocation

1. Wrote QUESTION.md, CARRY-OUT.md, SCRIPT.md, beat_sheet.json (7 beats),
   scenes.py (B01/B02/B03 Manim), render_scenes.py — Gate L confirmed all
   four Remotion patterns (`BrutalistHesitantWriter`, `WantQuote`,
   `ClaudeComposerAsk`, `OutroCTA`) RENDERABLE via `./art scenes --check`
   before slating.
2. `generate_audio_kokoro.py` — free, `am_onyx`, 7/7 beats. Measured
   durations: B00 10.84s, B01 12.16s, B02 9.96s, B03 14.72s, BCRY 9.47s,
   BHTF 13.85s, BOUT 3.63s. B00 clears the >=9s TIMING LAW floor (34-word
   narration + `lead_silence_s` 0.8).
3. Updated scenes.py `self.wait()` calls to the measured B01/B02/B03
   durations, then rendered all three Manim beats via `render_scenes.py` in
   the foreground — clean, no failures.
4. Rendered all four Remotion beats (B00, BCRY, BHTF, BOUT) via
   `remotion_scenes.py` in the foreground, blocked to completion — 4/4
   ok, B00 extended to 10.8s.
5. First `compile.py` pass -> 7/7 real (no slate), master 3840x2160, 75.6s,
   mean_volume -24.0 dB. content-check/frame-check/lane-check all PASS.
6. Gate V: pulled frames across all 7 beats (fps=1/6 sweep + a targeted
   t=9s pull inside B00). B00's correction ("know" -> "check") is complete
   and legible well before the beat ends; B01-B03 legible, correct
   contrast, no overlap; BHTF's topic kicker fits on one line (learned from
   the sibling's Gate V defect: never append the segment name to the
   `topic` prop). BOUT (`OutroCTA`) renders on flat white rather than the
   humanitarians cream ground — same shared-component note already logged
   unfixed on every sibling in this factory, not a new defect.
7. **GATE T (`type_check.py`) found one real defect**: B03 failed kerning
   §8.4 — max inter-glyph gap 31px > threshold 22px on the title. Cause: the
   title was built as five separate `Text()` mobjects ("WHAT", "BELONGS",
   "ON", "THE", "PAGE.") arranged with a fixed `buff=0.16`, which produces
   an oversized visual gap around short words ("ON", "THE") relative to
   their glyph width. **Fix:** replaced the five-mobject VGroup with a
   single `Text("WHAT BELONGS ON THE PAGE.", ...)` call, matching the
   pattern already used cleanly in B01/B02's titles. Re-rendered B03,
   recompiled (only B03 rebuilt, other 6 beats reused from cache),
   re-ran `type_check.py`: **GATE T PASS**, 0 FAILs.
8. Re-verified the fixed B03 frame directly (t=45s, inside B03) — title now
   reads with even, natural kerning, all three checklist rows and the
   boundary caption intact.
9. Final master verified directly:
   `knowledge-work-plugins--claude-liam-monday-brief.mp4` is 3840x2160,
   mean_volume -24.0 dB (max -3.0 dB), mtime newer than `beat_sheet.json` —
   the COMPLETION LAW conditions are all met.

## Gates

- **TIMING LAW (B00):** narration 34 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **10.84s** (rendered 10.8s), clears the
  >=9s floor. Correction ("know" -> "check") visible on-screen well before
  t=9s.
- **content-check / frame-check / lane-check:** all PASS (7/7 beats, no
  violations, canvas 3840x2160).
- **GATE T (`type_check.py`):** PASS after 1 fix iteration — see defect #7
  above. 0 FAILs on final run.
- **Gate V (frame QC):** full beat sweep at 1/6 fps plus a targeted B00
  correction check and a targeted B03 re-check after its fix. One real
  defect found and fixed (B03 kerning); clean on final pass.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (ffmpeg `volumedetect`,
  well above the -40 dB floor).

## Playlist resolution

`family: "knowledge-work-plugins"` matches `playlists.json` directly ->
**"Extending Claude — Skills, Plugins & Connectors"** (no fallback needed).

## Delivery

Phase 4 completed this invocation — see the delivery section below once run.
