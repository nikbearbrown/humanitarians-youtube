# ToDo — banking-domain-star-method-behavioral

Done. 0 slots outstanding.

- [x] **Human: sign `PEDAGOGY.md`** — `VERDICT: PASS`, signed 2026-08-10.
- [x] **Human: approve `beat_sheet.json` + `scenes.py`** (Gate 2).
- [x] Machine: `generate_audio_kokoro.py` — 22 mp3s + `mp3/timings.json`, `actual_duration_s`
      locked into `beat_sheet.json`.
- [x] Machine: `run.sh` full chain — GATE F/L/A/W → Manim render (11 beats) → GATE B → Remotion
      render (11 beats) → GATE V → compile. Several real defects found and fixed along the way
      (see `STATUS.md`); Gate V's underfill/low-contrast findings across 14 beats were reviewed in
      full and accepted by the human rather than fixed further — 7 are shared-component
      limitations with no override lever, 7 are the agent's own scenes already substantially
      enlarged this pass.
- [ ] **Human: watch the compiled cut** — the one gate that's never automated. Not yet confirmed.

Outputs: `banking-domain-star-method-behavioral-slate.mp4` (review) and
`banking-domain-star-method-behavioral.mp4` (clean master), both 262.7s, 3840×2160.
