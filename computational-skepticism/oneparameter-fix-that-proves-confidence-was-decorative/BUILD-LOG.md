# BUILD-LOG — The One-Parameter Fix That Proves the Confidence Was Decorative

## Metadata
- **Candidate**: Candidate 27 — The one-parameter fix that proves the confidence was decorative
- **Source**: `computational-skepticism-for-ai/chapters/02-probability-uncertainty-and-the-confidence-illusion.md`
- **Slug**: `oneparameter-fix-that-proves-confidence-was-decorative`
- **Chassis**: `course-skepticism` / `hai-simple` (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Register**: Plain (explain the mechanism clearly, then stop)
- **Voice**: Liam (`am_onyx`, in for Bear)
- **Visuals**: Manim (`slosh/spread` move, logit distributions, softening softmax bar chart, temperature dial, reliability curve) + Remotion (`BrutalistHesitantWriter` open, `WantQuote` carry-out, `ClaudeComposerAsk` your turn, `OutroCTA` outro)

## Six-Move Audit
1. **Open / Hesitant Writer**: B00 (Question typed and corrected: naive certainty question -> decorative confidence).
2. **Stakes First**: B01, B02 (Model outputs 99% confidence with crisp precision; empirical accuracy is only 85%; 14-point overconfidence gap).
3. **Anchor Planted**: B03 (Anchor logits: z₁=6.0, z₂=3.0, z₃=1.0 producing 94.7%, 4.7%, 0.6% softmax probabilities).
4. **Wrong Guess & Falsification**: B04 (The Inseparability Illusion: Assumed that softening probabilities must disrupt classification accuracy; falsified by monotonic scaling).
5. **Mechanism**: B05 (The Guo Discovery: class ranking is accurate and sound, but numerical probability scale is grossly inflated), B06 (Temperature scaling formula: dividing pre-softmax logits by learned constant T > 1.0).
6. **Anchor Payoff (Manim Move: `slosh/spread`)**: B07 (Softmax bar chart visibly sloshes and spreads outward as temperature dial turns from T=1.0 to T=2.0; Class A softens from 94.7% down to 85.0% while rank order remains unchanged).
7. **Mathematical Guarantee & Proof**: B08 (Strict Monotonicity: argmax(softmax(z/T)) ≡ argmax(z); zero decision flips), B09 (Separability Proof: Track 1 ranking is 100% identical, Track 2 confidence softened to empirical truth; proof that confidence was decorative all along).
8. **One Flag**: B10 (Reliability Diagram: check curve before and after T; raw output sags in the overconfident tail, calibrated curve hugs the 45° truth).
9. **Both Directions**: B11 (Direction A: In-distribution calibration delivers real probabilistic risk management), B12 (Direction B: Distribution shift caveat: calibration is set-dependent and goes stale when the world drifts).
10. **Carry-Out**: BCRY ("If dividing by one learned number fixes the probabilities without altering a single decision, the original confidence was decorative all along.")
11. **Your Turn**: BHTF (Audit prompt: measure top confidence bin accuracy, fit single temperature T on held-out logits, verify invariant ranking).
12. **Outro**: BOUT (Title restatement + @HumanitariansAI skin, "Liam, in for Bear").

## Quality & Gate Verification
- **Gate T (Type Lock)**: PASS — All 16 beats verified via `type_check.py` (0 FAILs). Refactored B02 banner fill and B05 tags fill to `MUTED_BG` with high-contrast text, eliminating glyph counter-space ink cutout artifacts and ensuring all detected text runs meet the physical height floor.
- **Audio Synthesis**: Kokoro `am_onyx` (Liam, in for Bear); measured durations synchronized into `beat_sheet.json`.
- **Manim Render**: 12 custom scenes rendered at 1080p24 (B01–B12) with Gate T compliance, implementing the `slosh/spread` kinetic move.
- **Remotion Render**: 4 custom Remotion compositions rendered at 4K/24fps: B00 (`BrutalistHesitantWriter`), BCRY (`WantQuote`), BHTF (`ClaudeComposerAsk`), BOUT (`OutroCTA`).
- **Compilation**: Conformed and compiled via `compile.py` to 4K master (`3840×2160`), 24 fps, total runtime 183.16s.
- **Gate Audio**: PASS — `mean_volume: -23.8 dB` (> -40 dB audible threshold verified; max_volume: -2.9 dB).
- **Gate V**: PASS — Visual inspection of frame sequence verified branding, typography, color palette (`#FAF9F5`, `#3D3929`, `#D97757`), title-safe margins, and bar chart dynamics.
- **Delivery**: Ready for packaging via `deliver.py --push`.
