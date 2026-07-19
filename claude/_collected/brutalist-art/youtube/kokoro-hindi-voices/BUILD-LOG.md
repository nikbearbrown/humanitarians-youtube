# BUILD-LOG — Kokoro: The 4 Hindi Voices

## HUMAN FEEDBACK — 2026-07-13

Build following the same pattern as kokoro-mandarin-voices and kokoro-japanese-voices:
Hindi + English subtitle on screen on every roster card.

## BUILD LOG — 2026-07-13

### Phase A — prereq check + FACTCHECK

kokoro-onnx 0.4.7, model files already present.
`--list-voices` confirms all 4 Hindi voices: hf_alpha, hf_beta, hm_omega, hm_psi.
All 4 graded C per VOICES.md 2026-07-13. lang_for() routes h* prefix → "hi" (Hindi).

Localized lines machine-authored (not a native speaker). Verified at build:
- "मैं अल्फ़ा हूँ, हिंदी स्त्री स्वर।" → "I'm Alpha, Hindi female." ✓
- "मशीन हाथ लाती है — पसंद आप लाते हैं।" → "The machine brings the hands — you bring the taste." ✓
- पुरुष स्वर = male voice, स्त्री स्वर = female voice ✓

### Phase B — audio

- B00 (ElevenLabs): 21.58s — NikBearBrown clone, English narration
- B01 hf_alpha: 5.08s · B02 hf_beta: 4.52s · B03 hm_omega: 5.14s · B04 hm_psi: 4.89s · B99 hf_alpha: 5.08s
- Total actual duration: 46.3s (estimated was 46.29s — close match)

### Phase C — Remotion render + compile

- remotion_scenes.py (foreground): 6/6 beats rendered
- B01-B04: 8s Remotion clip center-cut to match 4-5s audio (not slow-mo; Hindi voices are brief)
- QC sheet verified: all 4 names/codes/groups/grades correct, Devanagari subtitle visible on every
  card with correct font (Noto Sans Devanagari, lang="hi"), English italic translation below ✓
- B00 terminal checklist ✓ · B99 comment CTA ✓
- Review cut: kokoro-hindi-voices-review.mp4 (46.3s)

→ GATE: human approved (visual + audio review passed).

### Phase D — publish

16:9: https://youtu.be/BZ557c_XSow — "Brutalist — Claude for Video Production" playlist (unlisted)
CC: kokoro-hindi-voices.srt uploaded (6 cues, 46.3s) ✓

9:16 Short: https://youtu.be/R25_ZNotE98 — Shorts playlist (unlisted)
Note: short SRT skipped (Shorts typically no CC).

HUMAN ACTIONS (Studio):
  1. Flip both to public when ready.
  2. Verify caption timing on 16:9.
  3. Drag ch6e to correct position in "Brutalist" playlist.
