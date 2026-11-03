# B03 — Competitive Positioning

## Composition type
Remotion

## Layout
Dark stage. Top: three classifiers feeding into spectrum bar. Bottom: quarterly tracking timeline.

## Elements

### Top: Classifier Ensemble

#### Three classifier blocks (arranged horizontally)
- Left: "lexicon" — small card with word cloud icon. Color: #4A90D9 (blue).
  - Small example phrases: "gaining share," "defending margins."
- Center: "zero-shot (BART)" — small card with neural net icon. Color: #9B59B6 (purple).
  - Small label: "handles novel phrasing."
- Right: "stance detection" — small card with fine-tuned badge. Color: #27AE60 (green).
  - Small label: "fine-tuned on financial text."

#### Arrows converge
- Arrows from all three blocks converge downward into a single spectrum bar.

#### Spectrum bar
- A horizontal gradient bar.
- Left end: "offensive" labeled in #4A90D9 (blue). Example phrases: "gaining share," "expanding into."
- Right end: "defensive" labeled in #E74C3C (red). Example phrases: "maintaining position," "protecting margins."
- Center: "neutral" in #95A5A6 (grey).
- A marker (triangle pointer) sits at a position on the bar.
- Current score displayed above marker.

### Bottom: Quarterly Tracking

#### Timeline
- Four quarterly dots connected by a line (Q1–Q4).
- Q1, Q2, Q3: dots positioned on the blue (offensive) side of a mini spectrum.
- Q4: dot jumps to the red (defensive) side.
- A small flag icon at the Q3→Q4 transition: "directional flip detected" in #F1C40F (gold).

## Animation sequence
1. Three classifier blocks appear (1.5s).
2. Arrows converge into spectrum bar (1s).
3. Marker slides to a position on the bar (1s).
4. Quarterly timeline draws: Q1–Q3 on blue side (1.5s).
5. Q4 dot jumps to red side, flag appears (2s).
6. "directional flip detected" label (1s).

## Palette
- Lexicon: #4A90D9 (blue)
- Zero-shot: #9B59B6 (purple)
- Stance detection: #27AE60 (green)
- Offensive end: #4A90D9 (blue)
- Defensive end: #E74C3C (red)
- Neutral: #95A5A6 (grey)
- Flip flag: #F1C40F (gold)
- Timeline dots offensive: #4A90D9, defensive: #E74C3C
- Background: #1A1A2E
