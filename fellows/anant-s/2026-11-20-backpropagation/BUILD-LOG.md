# BUILD-LOG — Backpropagation, One Error at a Time

## 2026-11-22 — planning
- **Brief:** film 2 of the STEM series. The human chose this topic as the sequel to film 1. Skill is ai-explainer, channel claude-liam, greeting "Hola, Liam".
- **Evidence:** `demo/bp_demo.py` was executed. Its asserts check the chain-rule product and finite-difference agreement (|Δ| = 2.7e-10).
- **Pronunciation:**
  - Kokoro read "tanh" as "tan", so it is pinned to /tæntʃ/ via `metadata.pronounce`.
  - "ReLU" reads /ɹiː luː/, which is fine.
- **DOUBLE-CHECK:** two "minor" qualifiers were accepted (FACTCHECK #9 and #12), and the wording was kept honest.
- **Gates:** `bookend_check` PASS, `beat_lint` clean.
- **Duration:** about 3.0 min estimated at the film-1 Kokoro rate (3.5 words/s).
- **Status:** waiting for narration approval (GATE P).

## Plan for scenes, from film-1 lessons
- GATE A pre-flights an isolated copy of `scenes.py`, so the code must be stub-safe:
  - use the `P()`/`V()` point helpers
  - data-file fallback to the reel path
  - explicit `move_to` lists on shapes that must register as changing
  - no literal `class BXX_Name(Scene)` text in comments
- Count the clock in frames, as ceil(run_time·fps).
- Use box spotlights with a minimum height. Never underline "=" or "−".
- GATE V needs at least 55% fill. B01 uses type 130 with spacing 3.1, and BVDT has 6 lines.
- Keep text within ±6.0 x / ±3.2 y. Draw from t = 0.2 so no beat opens on an empty frame.

## 2026-11-22 — GATE P: narration approved
- The human approved the narration as drafted, all 11 beats, in chat with "Approve, build it".

## 2026-11-22 — audio, scenes, review cut, final
- **Audio and pronunciation.**
  - Kokoro, 11 beats.
  - Whisper heard "backpropagation" as "back repugation", so it is pinned to /bˌækpɹˌɑːpəɡˈeɪʃən/. "tanh" is pinned to /tæntʃ/.
  - The affected beats were regenerated.
- **Silences.** The toolkit ignores `lead_silence_s`/`tail_silence_s`, so `stem-films/tools/pad_silence.py` padded the audio directly: B01 +0.8 s lead, BVDT +0.5 s lead, BOUT +1.0 s tail. Then `align.py` ran.
- **scenes.py:** 6 Manim scenes, word-cued, with every number read from `evidence.json`. Gates A, W and B pass for all of them.
- **GATE V underfill fixes.**
  - B01's correction was shortened to "tests every weight" → "sends the error backward", at type 160. The narration is unchanged.
  - B02 now ghosts its full layout from t = 0.2.
  - B06 shows its cost-row labels early.
- **GATE T §8.3 false positive.** Terracotta arrow tips were read as low-contrast accent text in B05. The fix was to change the accent, not the gate:
  - All arrows and labels are now ink.
  - The terracotta accent is carried only by box outlines (B04's loss, B05's ∂L/∂w₁), B02's frame, B03's brace, and filled bars in B06/B07.
- **Final:** `exports/landscape/claude-liam-backpropagation.mp4`, 3840×2160, 24 fps, 196.8 s, SHA-256 `89161db107f4db3a…`, matching `.verified.json` (`ready`).
  - GATE V clean; GATE T PASS.
  - `check_no_labels` PASS: 98 samples, none with a footer strip.
  - `master_check` PASS.
  - `loudness` PASS: −24.63 LUFS, −3.12 dBTP.
- **Known cosmetic issue:** the locked `ClaudeTitleOutro` wraps the title as "…at a / Time.", as in film 1.
- **Not published.**
