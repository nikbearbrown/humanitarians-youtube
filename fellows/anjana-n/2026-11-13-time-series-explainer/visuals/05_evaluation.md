# B05 — The Evaluation Trap

## Composition type
Remotion

## Layout
Dark stage. Top: wrong way (random split with future leakage). Bottom: right way (temporal split). Title card at end.

## Elements

### Timeline (shared)
- A horizontal timeline with ~20 data points spaced evenly.
- Each point is a small circle.

### Top: Random split (wrong)
- Points colored randomly: some blue (#3498DB, train) and some red (#E74C3C, test) scattered throughout.
- A blue training point sits to the RIGHT of a red test point — future information in training.
- Arrows highlight the problem: "this training point is from the future of this test point."
- Large red X icon.
- Label: "random split — future leakage."

### Bottom: Temporal split (correct)
- A vertical cutoff line at roughly the 70% mark of the timeline.
- All points left of the line: blue (#3498DB) — train.
- All points right of the line: red (#E74C3C) — test.
- No overlap.
- Large green (#27AE60) checkmark.
- Label: "temporal split — train on the past, test on the future."

### Title card
- Both splits fade.
- Centered text: "Time Series — When Order Is the Signal."
- Color: #EAEAEA.
- Fade to dark.

## Animation sequence
1. Timeline appears with data points (1s).
2. Random coloring scatters blue and red points (1.5s).
3. Problem arrows highlight future leakage (1.5s).
4. Red X and "future leakage" label (1s).
5. Scene shifts to bottom: same timeline, cutoff line appears (1s).
6. Points color cleanly — blue left, red right (1.5s).
7. Green checkmark and "temporal split" label (1s).
8. Fade to title card (2s).
9. Fade to dark (0.5s).

## Palette
- Train points: #3498DB (blue)
- Test points: #E74C3C (red)
- Cutoff line: #F1C40F (gold)
- Wrong: #E74C3C (red X)
- Correct: #27AE60 (green checkmark)
- Title: #EAEAEA
- Background: #1A1A2E
