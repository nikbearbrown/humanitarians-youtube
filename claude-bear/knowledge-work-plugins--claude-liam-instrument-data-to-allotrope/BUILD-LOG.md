# BUILD-LOG — knowledge-work-plugins--claude-liam-instrument-data-to-allotrope

## 2026-09-04 — review cut, DONE

Redo-mode build (`mode: "redo"`) of
`anthropics/knowledge-work-plugins/youtube/claude-liam-instrument-data-to-allotrope/beat_sheet.json`
(a rendered Teardown-register `claude-liam` reel walking through the
`instrument-data-to-allotrope` Anthropic skill — converts laboratory
instrument output files to the Allotrope Simple Model). No local copy of the
skill's own SKILL.md exists on this machine (the source's `source_skill`
path lives only on Bear's machine), so the source's `beats[*].narration_text`
served as the locked script — the same situation as the `claude-liam-brief`
and other single-skill-teardown siblings in this family. Built entirely
fresh this invocation (only SUBJECT.json present on pickup).

**Register re-registered Teardown -> Plain**, matching every sibling in this
factory: the source's B03 named itself "the Teardown moment" and graded the
skill ("what it gets right… what it bites"); this redo states the same
input/output boundary as fact (no grading language) and folds the source's
"Verdict" card into a `WantQuote` carry-out beat. B00 replaced the source's
`ClaudeComposerAsk` cold open (which ran the skill live) with
`BrutalistHesitantWriter` (WRITER LAW: "read" -> "convert" — the newcomer
assumption that a skill converting lab data to Allotrope reads and
understands the results the way a scientist would, corrected to: it detects
the instrument and converts the file, nothing more). Close re-skinned to
`OutroCTA` / @HumanitariansAI with Liam's sign-off. BHTF's prompt was
rewritten clean — the source ran the actual skill against a real lab file,
which the general viewer doesn't have installed or a matching source file
for; this version asks Claude directly to convert a generic CSV export into
structured JSON, exercising the identical detect-and-convert teaching point
with no plugin dependency.

## NO-GENAI / NO-PANTRY LAW

All 7 beats are REMOTION (B00 writer, BCRY carry-out, BHTF handoff, BOUT
outro) or GRAPHIC/Manim (B01 anatomy, B02 pipeline, B03 constraint), all in
the humanitarians palette (`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`). No beat
is AI-VIDEO, pantry, or a human-drop slot. The source was already all-Remotion
(`ClaudeComposerAsk` x2, three `SkillTeardown*` cards, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so the NO-GENAI/NO-PANTRY LAW required no substitution
beyond the WRITER LAW and channel-skin row already require. B01-B03 were
rebuilt as GRAPHIC/Manim rather than reused as the source's Claude-palette
`SkillTeardown*` Remotion cards (those components hardcode `CLAUDE.*` tokens
with no color props, so they cannot be retinted to the humanitarians
palette) — matching the established practice on every sibling in this family.

## Built end to end this invocation

1. Wrote QUESTION.md, CARRY-OUT.md, SCRIPT.md, beat_sheet.json (7 beats:
   B00, B01, B02, B03, BCRY, BHTF, BOUT — matching the source's exact 7-beat
   shape), scenes.py (3 Manim scenes: B01Scene folder/anatomy, B02Scene
   three-phase pipeline, B03Scene four-input auto-detect-into-two-output
   diagram), render_scenes.py.
2. `generate_audio_kokoro.py` (7 beats, $0.00, `am_onyx`) — measured
   durations B00 10.39s, B01 17.30s, B02 9.34s, B03 19.58s, BCRY 8.64s,
   BHTF 18.24s, BOUT 4.35s. B00 clears the >=8s TIMING LAW floor with margin.
3. `render_scenes.py` (3 Manim beats) — clean on first pass, no fix
   iterations needed.
4. `remotion_scenes.py` (4 beats: B00, BCRY, BHTF, BOUT) run in the
   foreground per the one-shot COMPLETION LAW — completed within the
   default timeout, no background task needed. All 4 beats `ok`.
5. B00 verified directly: pulled frames at t=3.5s and t=8s from
   `media/B00.mp4` — the correction ("read" -> "convert") is already
   resolved and legible by t=3.5s, and the full corrected question "Can
   Claude convert my instrument files for me?" is complete and legible at
   t=8s, well inside the 10.4s clip.
6. First `compile.py` pass -> 7/7 real (no slate), master
   `knowledge-work-plugins--claude-liam-instrument-data-to-allotrope.mp4`,
   88.86s, native 3840x2160 (compile.py's 4K LAW), mean_volume -23.9 dB.
7. `type_check.py` (GATE T): **PASS on first pass, 0 FAILs** — no fix
   iterations needed.
8. Gate V: pulled 15 frames at 6s spacing across the full 88.86s runtime,
   plus targeted frames at the B03/BCRY transition (t=50/53/55/57/60/63s) to
   confirm the boundary reads clean. All 7 beats read directly at least
   once. No blockers: legible everywhere, safe inset respected, no text
   overlap, correct @HumanitariansAI branding on BHTF/BOUT, BHTF's kicker
   ("INSTRUMENT DATA TO ALLOTROPE · ANTHROPIC SKILL", wrapped to two lines)
   and the "Your Turn" segment title sit on separate lines with no
   collision (kept the topic prop to the plain skill/topic string, per the
   template pattern that avoided the exact overlap defect the
   `claude-liam-brief` sibling caught and fixed).
9. Final master independently re-verified via ffprobe/ffmpeg: h264
   3840x2160 + aac audio, duration 88.86s, mean_volume -23.9 dB max -2.7 dB,
   mp4 mtime (1788495360) newer than beat_sheet.json mtime (1788495244) —
   the COMPLETION LAW conditions are all met.

**Cosmetic note carried from every sibling in this factory:** `WantQuote`
(BCRY) and `OutroCTA` (BOUT) render on their own hardcoded off-white grounds
(`#FAF9F5` / flat white), not the humanitarians cream (`#F3EBDD`) — no color
props exist on either component. Same known seam already logged unfixed on
every sibling in this family (e.g. `knowledge-work-plugins--claude-liam-brief`,
`-friday-brief`); not fixed here for the same reason (no prop to fix it with).

## Gates

- **TIMING LAW (B00):** narration 30 words + `lead_silence_s` 0.8 ->
  measured `actual_duration_s` **10.39s**, clears the >=8s floor with
  margin. Correction ("read" -> "convert") resolved and legible by t=3.5s.
- **content-check / frame-check / lane-check:** all PASS (7/7 beats, no
  violations, canvas 3840x2160).
- **GATE T (`type_check.py`):** PASS, 0 FAILs, first pass.
- **Gate V (frame QC):** 15-frame full-runtime sweep + 6 targeted frames at
  the B03/BCRY boundary, all clean, no fixes needed.
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (ffmpeg `volumedetect`,
  independently re-verified — well above the -40 dB floor).

## Playlist resolution

`family: "knowledge-work-plugins"` matches `playlists.json` directly ->
**"Extending Claude — Skills, Plugins & Connectors"** (no fallback needed).

**Status: review cut DONE.** Passed every Phase-3 gate on the first attempt,
no fix iterations required.

## 2026-09-04 — Phase 4, DELIVERED

Master was already born native 3840x2160 (compile.py's 4K LAW), so copied
directly to `-4k.mp4` rather than re-rendering at a higher resolution.

```
python3 skills/make/hai-simple/loop/deliver.py <REEL_DIR> --push
```

Staged `DELIVERY/knowledge-work-plugins--claude-liam-instrument-data-to-allotrope/`
(4K master + description) for the Drive sync, and committed the text
artifacts (README.md, beat_sheet.json, SCRIPT.md, SUBJECT.json,
BUILD-LOG.md, CARRY-OUT.md, QUESTION.md — no mp3/mp4) to
`claude-bear/knowledge-work-plugins--claude-liam-instrument-data-to-allotrope/`
in `humanitarians-youtube`, pushed clean.

**Status: DELIVERED.**
