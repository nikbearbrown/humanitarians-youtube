# BUILD-LOG — The average that hides the patient

## Metadata
- **Candidate**: Candidate 23 — The average that hides the patient
- **Source**: `computational-skepticism-for-ai/chapters/11-communicating-uncertainty-calibrating-claims-to-evidence.md`
- **Slug**: `average-that-hides-patient`
- **Chassis**: `course-skepticism` / `hai-simple` (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Register**: Plain (explain the mechanism clearly, then stop)
- **Voice**: Liam (`am_onyx`, in for Bear)
- **Visuals**: Manim (12 scenes: distributions, formulas, cohort splits, tables) + Remotion (4 scenes: hesitant writer open, quote, your turn prompt, outro)

## Six-Move Audit
1. **Stakes First**: B01, B02 (Proprietary bedside sepsis early-warning AI deployed across hundreds of hospitals nationwide with developer-reported AUC 0.76–0.83 and acceptable aggregate calibration).
2. **Anchor Planted**: B03 (A pooled cohort of 12,955 admissions under a single headline metric: Expected Calibration Error = 0.018).
3. **Wrong Guess & Falsification**: B04, B05 (The intuitive assumption that low global ECE guarantees calibrated predictions for any individual patient; falsified because calibration error is a sample-weighted sum across bins).
4. **Epistemic Mechanism**: B06, B07 (The 90/10 cohort breakdown: 90% routine floor patients vs 10% ICU shock patients. When routine ECE is 0.005 and ICU ECE is 0.135, the weighted average is 0.018—the routine majority completely masks double-digit clinical miscalibration).
5. **Anchor Payoff**: B08, B09 (Independent validation by Wong et al. 2021 across 27,697 admissions: external AUC dropped to 0.63, positive predictive value was only 12%, and 67% of sepsis cases were missed).
6. **One Flag**: B10 (Homogeneous cohorts where population averages represent individuals vs Heterogeneous clinical cohorts where sickest patients have distinct risk dynamics).
7. **Both Directions**: B11 (Direction A: A clean global calibration score does not guarantee safety for any individual patient or subgroup), B12 (Direction B: The stratified toolkit—subgroup-specific calibration curves, slice ECE audits, worst-case error bounds).
8. **Carry-Out**: BCRY ("An aggregate calibration metric does not measure how well a model serves any specific patient; it measures how well the majority drowns out the margins.")
9. **Your Turn**: BHTF (Audit production classifier calibration curves by clinical subgroup, demographic slice, or operational context to detect masked high-stakes error).
10. **Outro**: BOUT (Title restatement + @HumanitariansAI skin).

## Exclusions Audit
- **No Brier score decomposition**: Verified — absent from script and visual assets.
- **No temperature scaling**: Verified — absent from script and visual assets.
- **No conformal prediction**: Verified — absent from script and visual assets.
- **No ECE formula derivation**: Verified — only operational weighted-sum definition used.
- **Epic Sepsis numbers strictly as cited**: Verified — Wong et al. (2021) external AUC 0.63 vs internal 0.76–0.83, PPV 12%, missed 67% sepsis cases.
- **Subgroup ECE table values**: Verified — explicitly flagged as an illustrative demonstration of weighting arithmetic.

## Quality & Gate Verification
- **Gate T (Type Lock)**: PASS — All 16 beats checked against type specifications via `type_check.py` (0 fails).
- **Audio Synthesis**: Synthesized with Kokoro `am_onyx` (Liam, in for Bear); all durations measured and synchronized in `beat_sheet.json` (186.2s total runtime).
- **Manim Render**: 12 custom scenes rendered at 24fps (B01–B12) implementing dot clouds, weighted sum mechanics, and cohort breakdowns. Text padding and card margins verified.
- **Remotion Render**: 4 custom Remotion compositions rendered at 4K/24fps: B00 (`BrutalistHesitantWriter`), BCRY (`WantQuote`), BHTF (`ClaudeComposerAsk`), BOUT (`OutroCTA`).
- **Compilation**: Assembled via `compile.py` to native 4K (`3840×2160`), 24 fps, 0 slates (16/16 filled). Total runtime 186.22s.
- **Gate Audio**: PASS — `mean_volume: -23.9 dB`, `max_volume: -2.9 dB` (threshold > -40 dB verified via `volumedetect`).
- **Gate V**: PASS — Visual inspection of frame sequence verified branding, typography (EB Garamond + UI Sans), color palette (`#FAF9F5`, `#3D3929`, `#D97757`), margins, safe-insets, mathematical notation, and readability.
- **Delivery**: Ready for packaging and delivery via `deliver.py --push`.
