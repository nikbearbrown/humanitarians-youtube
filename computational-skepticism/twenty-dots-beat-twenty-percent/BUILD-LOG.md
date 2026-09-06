# BUILD-LOG — Twenty dots beat twenty percent

## Metadata
- **Candidate**: Candidate 30 — Twenty dots beat twenty percent
- **Source**: `computational-skepticism-for-ai/chapters/10-visualization-under-validation-honest-misleading-and-the-choices-between.md`
- **Slug**: `twenty-dots-beat-twenty-percent`
- **Chassis**: `course-skepticism` / `hai-simple` (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Register**: Plain (explain the mechanism clearly, then stop)
- **Voice**: Liam (`am_onyx`, in for Bear)
- **Visuals**: Manim (split move: 1000-dot population split, natural frequency branch, Cleveland-McGill hierarchy, 20-dot quantile dotplot, direction cards) + Remotion (hesitant writer open, quote, your turn, outro)

## Six-Move Audit
1. **Stakes First**: B01, B02 (Physicians given 80% sensitivity and 9.6% false-positive rate estimate 80% to 90% cancer risk; actual probability is under 8%).
2. **Wrong Guess & Falsification**: B03 (The intuitive assumption that medical professionals need remedial statistical formula drills; falsified by cognitive evidence showing it is an interface defect caused by normalized percentages).
3. **Epistemic Mechanism**: B04, B05, B06 (Gerd Gigerenzer's natural frequencies: 1,000 women baseline yielding 8 true positives and 99 false positives. Cleveland & McGill perception hierarchy: position and count rank at the top with near-zero perceptual error, whereas area, volume, and color saturation have high error).
4. **Anchor Planted & Payoff**: B01, B04 -> B07 (`split` Manim move splits 1,000-person cohort into positive test cases, culminating in Kay & Hullman's 20-dot quantile dotplot where 4 filled circles represent a 20% risk).
5. **Both Directions**: B08 (Direction A: A dotplot will not calculate the probability for you; calibration, priors, and sampling must still be rigorous), B09 (Direction B: A mathematically flawless probability is epistemic malpractice if presented in an interface guaranteed to mislead).
6. **Carry-Out**: BCRY ("Position and count replace mental arithmetic with direct perception.")
7. **One Flag**: B07 (Quantile dotplots discretize into quantiles — e.g. 5% per dot — so extreme tail risks require explicit labeling or higher dot densities).
8. **Your Turn**: BHTF (Prompt for practitioners to translate their system's headline percentage into 20 discrete dots).
9. **Outro**: BOUT (Title restatement + @HumanitariansAI skin).

## Quality & Gate Verification
- **Gate T (Type Lock)**: PASS — All 13 beats conform to type specifications (0 FAILs in TYPECHECK.md).
- **Audio Synthesis**: Synthesized with Kokoro `am_onyx` (Liam, in for Bear); measured durations conformed in `mp3/timings.json` (13 beats, 197.5s runtime).
- **Manim Render**: 9 custom scenes rendered at 24fps (B01–B09) implementing the `split` move across 1000-dot population grids, natural frequencies, Cleveland-McGill ranking, 20-dot quantile dotplot, and direction cards.
- **Remotion Render**: 4 custom Remotion compositions rendered at 4K/24fps: B00 (`BrutalistHesitantWriter`), BCRY (`WantQuote`), BHTF (`ClaudeComposerAsk`), BOUT (`OutroCTA`).
- **Compilation**: Assembled via `compile.py` to 4K (`3840×2160`), 24 fps, total runtime 197.5s.
- **Gate Audio**: PASS — `mean_volume: -23.8 dB`, `max_volume: -2.7 dB` (audible threshold > -40 dB verified via ffmpeg).
- **Gate V**: PASS — Visual inspection of full frame sequence verified palette (`#FAF9F5`, `#3D3929`, `#D97757`), safe insets, typography (EB Garamond / UI Sans), no text collisions, and complete element containment.
- **Delivery**: Staged and delivered to Google Drive outbox (`DELIVERY-course/twenty-dots-beat-twenty-percent`) and pushed to `humanitarians-youtube` GitHub repository.
