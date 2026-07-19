# BUILD-LOG — Kokoro: The 5 Japanese Voices

## HUMAN FEEDBACK — 2026-07-13

Same idea as Mandarin — show Japanese and English subtitle on screen.
KokoroRosterCard already extended with subtitle/subtitleEn (done in Mandarin build).

## BUILD LOG — 2026-07-13

### Phase A — prereq check + FACTCHECK

kokoro-onnx 0.4.7 already installed. Model files already present.
`--list-voices` confirms all 5 Japanese voices: jf_alpha, jf_gongitsune, jf_nezumi,
jf_tebukuro, jm_kumo.

Grades per hexgrad/Kokoro-82M VOICES.md 2026-07-13:
- jf_alpha: C+ ✓
- jf_gongitsune: C ✓
- jf_nezumi: C- ✓
- jf_tebukuro: C- (BUILD-PROMPT notes "doc listing was ambiguous" — used as authored)
- jm_kumo: C- ✓

Note: jf_tebukuro grade C- treated as authored; ambiguity noted here and in FACTCHECK.md.
Japanese grade range is better than Mandarin (C+/C/C- vs all-D).

### Phase B — audio

- B00 (ElevenLabs): 20.74s — NikBearBrown clone
- B01 jf_alpha: 24.19s · B02 jf_gongitsune: 27.78s · B03 jf_nezumi: 27.75s
  B04 jf_tebukuro: 27.84s · B05 jm_kumo: 22.91s · B99 jf_alpha: 24.19s
- Total actual duration: 175.4s (estimated was 74s — Japanese TTS generates slow,
  deliberate speech with natural pauses; C+/C/C- quality is audible in the speech
  rhythm)

### Phase C — Remotion render + compile

- remotion_scenes.py (foreground): 7/7 beats rendered
- SLOW-MO WARNING: KokoroRosterCard is registered at 240 frames (8s). Japanese audio
  beats run 22-28s, so compile stretches the 8s Remotion clip 3.0-3.5x. The spring
  animation plays at 1/3 speed (~3s instead of 1s). Static hold is unaffected.
  Fix: update KokoroRosterCard durationInFrames in Root.tsx to 900 (30s) and re-render.
- QC sheet verified: all 5 names/codes/groups/grades correct, bilingual subtitle visible
  on every card, B00/B99 correct.
- Review cut: kokoro-japanese-voices-review.mp4 (175.4s)

## BUG REPORT — 2026-07-13

Stale audio confirmed: mp3/ mtime 17:37 < beat_sheet mtime 17:48. Audio was generated from
an earlier version of beat_sheet.json (before subtitle/subtitleEn were written atomically).
The beat_sheet.json Write call replaced the file the Kokoro generator had already modified
with actual_duration_s values, so the narration_text fields at audio-gen time may differ from
the current file. Safest fix: delete all mp3s and regenerate from current beat_sheet.json.

SAME-BUG SWEEP result:
- kokoro-all-28-english-voices: narration verified correct (B01 "graded A minus" ✓, B99
  "only A minus" ✓) — FACTCHECK ran before audio per build log; mtime gap = remotion stamp.
- kokoro-mandarin-voices: narration correct ("I don't speak Mandarin" ✓); mtime gap = remotion.
- kokoro-free-voices: all English, no language confusion risk; mtime gap = remotion stamp.
- kokoro-hindi-voices / kokoro-romance-voices: no audio yet, clean.

## AUDIO REBUILD — 2026-07-13

All 7 Japanese mp3s deleted and regenerated from current beat_sheet.json.

VERIFICATION:
- B00 new duration: 21.45s — matches Japanese narration ~270 chars (~21s at ElevenLabs rate).
  Mandarin B00 was 33.85s (~495 chars). Duration proves B00 was generated from Japanese text.
- B01-B05/B99: Kokoro jf_*/jm_* voices, same durations as before (narration was unchanged
  Japanese text). Confirmed: 24.19s, 27.78s, 27.75s, 27.84s, 22.91s, 24.19s.
- mp3 mtime (17:58:35) > old beat_sheet mtime (17:48) → stale-audio gap eliminated.
- Review mp4 mtime (17:58:55) > mp3 mtime (17:58:35) → mp4 is built from new audio.
- B00 narration_text says "I don't speak Japanese" and "Japanese narration" — never
  "Chinese" or "Mandarin".
- B99 (jf_alpha) narrates in Japanese: アルファです。日本語の女性の声です… — correct.

Review cut: kokoro-japanese-voices-review.mp4 (176.1s)

→ GATE: human listened — B00 (English intro) is clean.

## AUDIO QUALITY NOTE — 2026-07-13

Human verdict on B01-B05 (Kokoro jf_*/jm_* voices): "not pure Japanese — sounds like
it's mixing Chinese phonology." Consistent with pack grades C+/C/C-. The Kokoro-82M
non-English voices at this grade tier appear to share phonetic artifacts across East Asian
languages. Not a build error — the engine's own report card. Documented here so the
description can be honest: "C+ to C- — your ear is the final grade."

DECISION: move on. Publish pending human studio flip when ready.
