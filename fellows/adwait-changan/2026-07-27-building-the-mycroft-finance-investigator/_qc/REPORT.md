# Visual QC report — Building the Mycroft Finance Investigator

Method: sampled frames with ffmpeg and read the PNGs (VISUAL QC LAW), across two render
passes. 13/13 beats render as real visuals — **zero slates**.

## Defects found and fixed

| # | Beat(s) | Defect | Root cause | Fix | Status |
|---|---|---|---|---|---|
| 1 | B02, B03, B08 | Illustration reveal truncated — only the first chips/layers appeared; caption missing | The `ClaudeScience*` compositions are registered at 900 frames (30s); their staggered reveal was cut to our shorter beats by the audio-length freeze/trim | Shortened those three comps to 360 frames (12s) in the local `brutalist.art` `Root.tsx` so the animation completes inside each beat, then freeze-holds | FIXED |
| 2 | B05 | A meta-comment ("REPRESENTATIVE excerpt… see FACTCHECK.md") was burned into the on-screen code | Placeholder text left in the `code` prop | Removed; later replaced the whole excerpt with the real `finance.py:162 ebitda_variance()` | FIXED |
| 3 | B06 | Variance shown as "120,000 (budget minus actual)" — wrong sign/definition | Authoring error | Now "Variance (actual − budget) — −$120,000", matching the code's `variance = actual - budget` | FIXED |

## Accuracy pass (fellow-confirmed, 2026-07-27)

- "43 data rows across six synthetic datasets" (not "records").
- Investigator described as "local, evidence-driven agent — no external model in the loop."
- Verdict carries the synthetic-sample / DRAFT-workflow / named-human-reviewer disclosure
  (spoken + on-screen).

## Result

Zero BLOCKER, zero MAJOR defects remaining. Clean master compiled with no review burn-ins.
Note: this reel is 100% Remotion by design (all patterns render locally); the deep-explainer
VOX/Manim quota warning from `compile.py` is expected and accepted for this build.
