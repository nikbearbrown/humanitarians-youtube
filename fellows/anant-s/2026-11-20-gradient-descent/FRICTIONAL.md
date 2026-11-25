# Frictional log — Gradient Descent, One Step at a Time

## 2026-11-22 — the first film: one rule, and the gates that shaped every later scene

- **Drive:** https://drive.google.com/drive/folders/1zudlUZG4n6vUShgp1M1VU1pwPly0YjMR
- **Video:** `exports/landscape/claude-liam-gradient-descent.mp4` (3:12)

**What I was working on.** The first film of the STEM series, and the first one built with the brutalist.art toolkit on this Windows machine. I chose the topic, the ai-explainer skill and the default claude-liam / @NikBearBrown branding from the options Claude proposed. I directed the work in Claude Code; Claude wrote, built and checked the film.

**What I tried, and what I expected.**

- I expected about 4.3 min of narration, estimated at 2.6 words/s. That is longer than the typical 1–3 min ai-explainer, and Claude named B07 (scale) as the trim if one was wanted.
- I expected Kokoro to say "eta" correctly.
- I expected the six Manim scenes to clear the gates on the first pass.
- I expected an underline to be a clean way to spotlight each symbol in the update rule.

**Where it resisted, and what I did next.**

- **"eta" was heard as "either".** A whisper check found Kokoro phonemized it /ˈiːɾə/. Claude pinned it to /ˈeɪtə/ via `metadata.pronounce` and regenerated B03. Every other whisper difference was digit normalization ("2 4" for "two point four").
- **GATE A pre-flights the scenes in an isolated copy.** Claude made the code stub-safe (point helpers and an isolated-copy data fallback) and made B03's arrow centres explicit. A docstring containing a fake class line had been picked up by `run.sh` as a scene; Claude removed it.
- **Manim renders ceil(run_time·fps) frames.** Claude made the clock count whole frames; each scene now lands within ±3% of its audio.
- **GATE B:** B02's "setting θ" label sat below the safe area. Claude moved it up.
- **GATE V underfill.** Claude set B01 to type 160 with spacing 3.1, set B03's equation at 132 pt with the labels spread, and took BVDT from five to six lines. The new line, "Where you start decides which valley you end in.", came after GATE P. It restates B06, only BVDT audio was regenerated, and Claude flagged it for me.
- **Hand QC at 15/50/85% of every beat:** an underlined "−" read as "=", and an underlined "=" read as "≡". Claude switched B03 to box spotlights with a minimum height, de-collided B02's labels, widened B04's table columns, redirected B05's runaway arrow, and made B06/B07 draw from t = 0.

**What Claude contributed, and what I did with it.**

- **Script and evidence:** Claude wrote the 11-beat narration and `demo/gd_demo.py`, ran it, and used its output as the only source of on-screen numbers. Its fact check corrected two draft claims before I saw the script.
- **Build and QC:** Claude wrote the six Manim scenes, generated the Kokoro audio, rendered, fixed every gate failure above, and checked the master: GATE V 0 BLOCKER / 0 MAJOR, GATE T PASS, `master_check` PASS, loudness −24.70 LUFS / −2.96 dBTP, a sampled frame with no review labels.
- **Rebuild prompt:** Claude wrote `BUILD-PROMPT.md`, which rebuilds the film end to end with free tools only and never publishes.
- **My part:** I approved the narration, watched the 4K review cut, and only then had Claude run `./art final`. I set the rule that no delivered video carries a "B0x REMOTION" footer or bottom strip.
- Accepted:
    - **The narration as drafted, all 11 beats and B07 kept.** I approved it at GATE P in chat with "Approve, build it". It already carried the two corrections: "millions of times" → "step after step", and "this same rule" → "a version of this same rule".
    - **The final export after my watch of the review cut.** `./art final --out exports/landscape` exited 0.
- Rejected:
    - **Trimming B07 to shorten the film.** I kept all 11 beats. The measured narration came to 3:12, not the estimated 4.3 min.

**What I understand now, and what I still do not.**

- Understood:
    - On L = θ² each step multiplies θ by (1 − 2η): 0.8 at η = 0.1, so 3 → 2.4 → 1.92. It converges only when |1 − 2η| < 1; η = 0.9 flips sign every step and still lands, and η = 1.1 runs away to 18.5752 in ten steps.
    - Gradient descent stops in whichever valley it starts above: from θ = 2 it rests at loss −1.0702, next to a deeper valley at −3.5139.
    - An underline on a math operator can change what it reads as. A box spotlight does not.
    - Manim counts frames, not seconds, so the scene clock has to as well.
    - The word-rate estimate overstated the length: 4.3 min estimated, 3:12 measured.
    - "ready" in `.verified.json` means the automated export checks passed. Publishing is a separate human decision.
- Not understood / not verified:
    - The no-label check on this master is recorded only as one sampled frame; no full `check_no_labels` run is logged in this folder.
    - The locked `ClaudeTitleOutro` wraps the title as "…One Step at a / Time.". The component has no layout props and the outro lock forbids altering the title, so it is not fixed.
    - Remotion is 4.0.535; 4.0.545 is available and the upgrade was not run.
    - `master_check` skipped its clock check because `clock_check.py` is missing from the toolkit.
    - FACTCHECK #16 is only "minor": the 1/25 cost per step ignores fixed overhead.
    - Not published. The Drive copy is still the labelled review cut.
