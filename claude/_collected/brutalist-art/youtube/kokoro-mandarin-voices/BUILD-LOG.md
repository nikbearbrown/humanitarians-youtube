# BUILD-LOG — Kokoro: The 8 Mandarin Voices

## HUMAN FEEDBACK — 2026-07-13

Mandarin should have the Mandarin AND English subtitle on screen (not just in SRT captions).
KokoroRosterCard extended with optional `subtitle` (Mandarin spoken text) and `subtitleEn`
(English translation) props — rendered below the grade chip on every roster card.

## BUILD LOG — 2026-07-13

### Phase A — prereq check + FACTCHECK

kokoro-onnx 0.4.7 already installed (from prior phase).
Model files already present: runtime/models/kokoro/kokoro-v1.0.onnx + voices-v1.0.bin.
`--list-voices` confirms all 8 Mandarin voices present: zf_xiaobei, zf_xiaoni, zf_xiaoxiao,
zf_xiaoyi, zm_yunjian, zm_yunxi, zm_yunxia, zm_yunyang. All 8 graded D per VOICES.md.

### Component changes

KokoroRosterCard extended:
- Added optional `subtitle` (native text) and `subtitleEn` (English translation) to schema
- Removed hardcoded " English" suffix from group label (group is now fully self-contained)
- Subtitle block renders below grade chip: native text in body weight, English in italic slate
- `contentTop` shifted up (portrait 0.28→0.24, landscape 0.20→0.18) to accommodate two extra lines

### Phase B — audio

- B00 (ElevenLabs): 33.85s (~$0.02) — NikBearBrown clone, longer than 20s estimate (dense narration)
- B01–B08 (Kokoro, cmn lang): 8 beats × $0.00 = $0.00
- B99 (Kokoro, zf_xiaoxiao): 4.76s = $0.00
- Total actual duration: 77.6s

Audio listen notes (for human review — D-grade voices are rough by design):
- All 8 voices graded D: thin non-English support per VOICES.md; rough quality expected
- B01 Xiaobei (6.3s) — longest Mandarin clip; verify tone sounds like a named intro
- B05 Yunjian / B07 Yunxia — male voices; verify gender distinction audible

### Phase C — Remotion render + compile

- KokoroRosterCard updated (subtitle/subtitleEn support) — re-rendered all 8 roster beats
- remotion_scenes.py (foreground): 10/10 beats rendered
- compile.py: 10/10 filled — all VIDEO beats (Remotion)
- Review cut: kokoro-mandarin-voices-review.mp4 (77.6s)
- QC sheet verified: all 8 names correct, all grades D crimson chip, Mandarin subtitle +
  English translation visible on every roster card, B00/B99 correct.

## HUMAN FEEDBACK — 2026-07-13

Perfect final cut, post to YouTube — create a 9:16 and same idea for Japanese (show
Japanese and English subtitle on screen).

## BUILD LOG — FINAL + SHORT — 2026-07-13
