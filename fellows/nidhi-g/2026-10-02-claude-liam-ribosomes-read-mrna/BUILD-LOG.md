# BUILD-LOG — claude-liam-ribosomes-read-mrna

## Brief
60 s · 12 beats · Kokoro am_onyx · ai-explainer · review cut only (no `./art final`).

## Decisions and justified deviations
- **Duration.** First audio pass measured 74.7 s. Narration tightened and audio regenerated with
  `--speed 1.1`, giving 65.7 s. The skill holds that duration is an output, not a target, so it stops there
  rather than cutting a mechanism step. `generate_audio_kokoro.py` has no beat-sheet speed field, so
  **always regenerate with `--speed 1.1`** (recorded in `metadata.kokoro_speed`).
- **Narration budget.** Body beats run 11–14 words against the skill's 45–70. Forced by the 60 s brief.
  The screen carries the evidence (sequence, pairing ticks, labels).
- **`lead_silence_s` on B01** is written as the skill requires, but no script in this toolkit reads it.
  B01's narration alone measures 9.94 s, which meets the ≥ 9 s rule without it.
- **Outro.** OUTRO-LOCK wins: narration is "<title>. At Nik Bear Brown." with no extra "Liam, in for Bear"
  sign-off. IN-FOR-BEAR is satisfied in B00. The 1.0 s tail hold has no script support (as above).
- **GATE A adaptation.** The static checker's simulator does not see `.animate` moves of shapes already on
  screen, so B06/B08 entrances and exits use `FadeIn/FadeOut(shift=…)`. The rendered motion is the same.
- **Colour.** Terracotta is used only on shapes, never on text (it fails AA contrast on cream).

## Gates before compile
GATE A ✓ all 7 scenes · GATE W ✓ all 7 scenes · GATE F paperwork present (FACTCHECK, SHOTLIST, PROMPTS).
