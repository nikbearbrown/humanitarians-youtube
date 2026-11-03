# BUILD-LOG — You Can't Escape the Fairness Impossibility — You Can Only Choose Where to Sign

## Metadata
- **Candidate**: Candidate 28 — You can't escape the fairness impossibility — you can only choose where to sign
- **Source**: `computational-skepticism-for-ai/chapters/07-fairness-metrics-choosing-a-definition-and-defending-it.md`
- **Slug**: `you-cant-escape-fairness-impossibility-you-can-only`
- **Chassis**: `course-skepticism` / `hai-simple` (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Register**: Plain (explain the mechanism clearly, then stop)
- **Voice**: Liam (`am_onyx`, in for Bear)
- **Visuals**: Manim (`morph` move, Traveling Invoice / Price-Tag across 4 stations: Group Dial, Ruler $d$, Causal DAG, $\alpha$ Slider) + Remotion (`BrutalistHesitantWriter` open, `WantQuote` carry-out, `ClaudeComposerAsk` your turn, `OutroCTA` outro)

## Beat Progression
1. **B00 (Open / Brutalist Hesitant Writer)**: Hesitant writer opens with naive question on finding a mathematically neutral fairness metric, corrected to the inevitable relocation of value choices.
2. **B01 (Stakes & The Traveling Invoice)**: Establishes the core thesis: escaping group fairness impossibility by adopting alternative frameworks does not eliminate value judgments; it relocates the invoice.
3. **B02 (Station 1: The Group Dial Tradeoff)**: Explores group fairness metrics (Demographic Parity, Equalized Odds, Predictive Parity) and shows the mutual impossibility theorem under unequal base rates.
4. **B03 (The Migration Impulse)**: The invoice detaches from Station 1 as practitioners attempt to flee group metric tensions toward individual fairness.
5. **B04 (Station 2: The Individual Ruler $d(x, y)$)**: The traveling invoice morphs into a similarity ruler. Individual fairness guarantees similar treatment for similar individuals, but the distance metric $d(x, y)$ requires choosing which differences matter.
6. **B05 (The Subjectivity of the Metric)**: Demonstrates that defining who is "similar" embeds normative human priorities directly into the metric ruler.
7. **B06 (Station 3: The Causal DAG)**: The invoice morphs into a directed acyclic graph. Causal fairness decomposes paths from sensitive attributes into resolving vs discriminatory paths.
8. **B07 (The Normative Graph Choice)**: Shows that classifying an intermediate path as "legitimate" or "discriminatory" is a social and political policy choice, not a discovery of data science.
9. **B08 (Station 4: The Continuous Inequality $\alpha$ Slider)**: The invoice morphs into an alpha slider for Generalized Entropy indices, measuring inequality across the continuous distribution of model benefits.
10. **B09 (The Price of Alpha)**: Shows the parameter tradeoff: choosing $\alpha$ specifies how heavily the system penalizes discrepancies at the bottom versus the top of the distribution.
11. **B10 (The Ledger: Four Stations, Four Invoices)**: Summary ledger showing all four stations side by side; you cannot escape the bill, you can only choose which document to sign.
12. **BCRY (Carry-Out / WantQuote)**: Liam's carry-out quote: "The math will balance any ledger you hand it. It will never tell you whose debt to forgive."
13. **BHTF (Your Turn / ClaudeComposerAsk)**: Step-by-step audit prompt instructing engineers to identify where their fairness assumptions are signed and defended in production.
14. **BOUT (Outro / OutroCTA)**: Closing card and subscribe callout for @HumanitariansAI ("Liam, in for Bear").

## Quality & Gate Verification
- **Gate T (Type Lock)**: PASS — All 14 beats verified via `type_check.py` (0 FAILs, exit code 0). Complete structural compliance across layout, title safe areas, font sizes, contrast ratios, and container boundaries.
- **Audio Synthesis**: Kokoro `am_onyx` (Liam, in for Bear); measured durations recorded in `mp3/timings.json` and synchronized in `beat_sheet.json`.
- **Manim Render**: 10 body scenes rendered at 1080p24 (B01–B10) with Gate T compliance, implementing the `morph` kinetic move tracing the Traveling Invoice across 4 analytical stations.
- **Remotion Render**: 4 custom Remotion compositions rendered at 4K/24fps: B00 (`BrutalistHesitantWriter`), BCRY (`WantQuote`), BHTF (`ClaudeComposerAsk`), BOUT (`OutroCTA`).
- **Compilation**: Conformed and compiled via `compile.py` to native 4K master (`3840×2160`), 24 fps, total runtime 231.2s. Output: `you-cant-escape-fairness-impossibility-you-can-only.mp4` and `you-cant-escape-fairness-impossibility-you-can-only-4k.mp4`.
- **Gate Audio**: PASS — Measured via `ffmpeg volumedetect`: `mean_volume: -23.9 dB` (> -40 dB audible threshold; `max_volume: -2.8 dB`).
- **Gate V**: PASS — Extracted and visually inspected full 4K frame suite (`_gate_v_frames/`). Verified brand color palette (`#FAF9F5`, `#3D3929`, `#D97757`), sharp vector math and typography, zero overlaps, clean margins, and proper visual hierarchy across all 14 beats.
- **Delivery**: Ready for packaging via `deliver.py --push`.
