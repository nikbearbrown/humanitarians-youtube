# BUILD-LOG — Kokoro: All 28 English Voices (The Full Roster)

## HUMAN FEEDBACK — 2026-07-13

Read youtube/kokoro-all-28-english-voices/BUILD-PROMPT.md and execute it.
Standing rules #1–#4 in EXAMPLES-CAMPAIGN.md apply. Sheet and GATE P already authored
— do not re-author. FACTCHECK the 28 against --list-voices first; only B00 spends money.
Stop at the gate with the review cut; wait for human approval before publishing.

## BUILD LOG — 2026-07-13

### Phase A — prereq check

kokoro-onnx 0.4.7 already installed (from kokoro-free-voices Phase A).
Model files already present: runtime/models/kokoro/kokoro-v1.0.onnx + voices-v1.0.bin.

### FACTCHECK — grade corrections

Cross-referenced beat_sheet grades against kokoro-free-voices FACTCHECK.md (same
VOICES.md 2026-07-13 source). 19 grades were wrong in the authored sheet; all
corrected via script — grades and narration texts updated atomically. See FACTCHECK.md.

B00: Engine = ElevenLabs (ELEVENLABS_VOICE_NIKBEARBROWN), all others = Kokoro.

### Phase B — audio

- B00 (ElevenLabs): 22.65s (~$0.02) — actual was longer than 17s estimate
- B01–B28 (Kokoro): 28 beats × $0.00 = $0.00
- B99 (Kokoro, af_heart): 17.98s = $0.00
- All 30 mp3s generated; beat_sheet.json updated with actual durations

Audio listen notes (for human review — rough voices are by design):
- am_adam (F+) B12: F-grade voice, narrates its own grade. Rough by design.
- am_santa (D-) B20: D-grade voice, 6.4s clip. Choppy by design.
- af_aoede B03: "Aoede" is an unusual name — verify pronunciation sounds correct.
- am_fenrir B15: "Fenrir" is Norse — verify pronunciation sounds correct.
- af_jessica B05: "Jessica" is graded B+ but not used in the short film; verify quality
  matches the grade (should sound decent, not rough).

### Phase C — Remotion component + compile

- KokoroRosterCard authored: runtime/remotion/src/scenes/KokoroRosterCard.tsx
  - Props: name, code, group, grade, index, topic (zod schema)
  - Grade chip: teal (A/B) · slate (C) · crimson (D/F)
  - KokoroRosterCard916 registered in Root.tsx (same component, 1080×1920)
- remotion_scenes.py (foreground): 30/30 beats rendered
- compile.py: 30/30 filled — all VIDEO beats (Remotion)
- Review cut: kokoro-all-28-english-voices-review.mp4 (196.5s)
- QC sheet verified by looking: all 28 names correct, all grades correct,
  chip colors correct (teal A/B, slate C, crimson D/F), B00/B99 correct.

## HUMAN FEEDBACK — 2026-07-13

those can be final cut and posted to YouTube 16:9 and 9:16
