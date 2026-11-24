# BUILD-LOG — Gradient Descent, One Step at a Time

## 2026-11-22 — planning
- **Choices:** topic, skill (ai-explainer) and branding (default claude-liam / @NikBearBrown) were chosen by the human.
- **Greeting:** "Ciao, Liam", one word from the lexicon. Liam never takes "Wagwan".
- **Title and slug:** "Gradient Descent, One Step at a Time", slug `claude-liam-gradient-descent`.
- **Evidence:** `demo/gd_demo.py` was executed and its output is the only source of on-screen numbers.
- **DOUBLE-CHECK corrections:** two, recorded in FACTCHECK #2 and #14.
- **Duration:** about 4.3 min estimated at 2.6 words/s. That is longer than the typical 1–3 min ai-explainer. Duration is an output, not a target. The candidate trim, if one is wanted, is B07 (scale).
- **ASK→RESULT:** applied at the cold open only. Body graphics are teaching illustrations of the B00 ask, not separately generated artifacts. This follows the house precedent (`claude-liam-brutalist-runtime-align`).
- **Logo bug:** none yet; to be checked at visual QC.
- **Gates passed:** `bookend_check` PASS; `beat_lint` clean.
- **Status:** waiting for narration approval (GATE P), then audio (GATE 0).

## 2026-11-22 — GATE P: narration approved
- The human approved the narration as drafted, all 11 beats and B07 kept, in chat with "Approve, build it".
- Next: Kokoro audio (GATE 0), then a whisper pronunciation check.

## 2026-11-22 — audio, scenes, 4K review cut
- **GATE 0 (audio):** Kokoro am_onyx, 11 beats, 3:12 total.
  - A whisper check found that "eta" was phonemized /ˈiːɾə/ and heard as "either". It is now pinned via `metadata.pronounce` to /ˈeɪtə/, and B03 was regenerated.
  - Every other difference whisper reported was digit normalization (it wrote "2 4" for "two point four"), not a mispronunciation.
- **Word clock:** `align.py` aligned 11/11 beats with no fallback. Manim reveals are keyed to spoken words in `mp3/words.json`.
- **scenes.py:** six Manim scenes; every number comes from `demo/evidence.json`. B06 asserts that its descent path matches the evidence.
  - The clock counts whole frames, because Manim renders ceil(run_time·fps) frames.
  - Each scene lands within ±3% of its audio.
- **Gate fixes on the way to a clean build:**
  - **GATE A:** stub-safe points and isolated-copy data fallback; B03 arrow centers made explicit.
  - **GATE A (run.sh):** a docstring containing a fake class line had been picked up as a scene, so it was removed.
  - **GATE B:** the B02 "setting θ" label was below the safe area and was moved up.
  - **GATE V underfill:** B01 now uses type 160 with spacing 3.1. B03's equation is 132 pt with labels spread. BVDT went from five to six lines.
- **BVDT change after GATE P:** added "Where you start decides which valley you end in." This restates B06, which was already approved. It was needed for canvas fill and matches the 4-or-6 line verdict rule. Only BVDT audio was regenerated. **Flagged for the human reviewer.**
- **Hand QC** (frames read at 15/50/85% of every beat, `_qc/sheet_1-3.png`):
  - B03's spotlight changed from an underline to a box with a minimum height. An underlined "−" read as "=", and an underlined "=" read as "≡".
  - B02 labels were de-collided, B04 table columns widened, B05's runaway arrow redirected, and B06/B07 now draw from t=0 (no empty open).
- **Result:** `./art run` exit 0. GATE V: 0 BLOCKER / 0 MAJOR. GATE T: PASS, 0 FAILs. bookend PASS.
- **Known cosmetic issue, not fixed:** the locked `ClaudeTitleOutro` wraps the title as "…One Step at a / Time.". The component has no layout props, and the outro lock forbids altering the title.
- **Not done:** `./art final` (the 4K master), which waits for the human watch. The Remotion version is 4.0.535; 4.0.545 is available, and the upgrade was not run.

## 2026-11-22 — final master exported (after the human watched the review cut)
- `./art final --out exports/landscape` exited 0. GATE T PASS.
  - One §8.10 ADVISORY: the BVDT narration recites the card verbatim, at 0.90 similarity. This is not a FAIL.
- **Master:** `exports/landscape/claude-liam-gradient-descent.mp4`, 3840×2160, 24 fps, yuv420p, h264 + aac, 192.5 s.
  - SHA-256 `7000bed2b3849c51…`. It matches `.verified.json`, whose status is `ready`.
- **Extra checks:**
  - `master_check` PASS.
  - `loudness_check` PASS: −24.7 LUFS integrated, −2.96 dBTP true peak.
  - A sampled frame has no review labels.
- Not published. "ready" means the automated export checks passed; publishing is a human decision.
