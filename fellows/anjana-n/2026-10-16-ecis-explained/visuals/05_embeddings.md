# B05 — Embedding Upgrades

## Composition type
Remotion

## Layout
Dark stage. Split view: Sentence-BERT fine-tuning (left), FinBERT ensemble (right).

## Elements

### Left side: Fine-Tuned Sentence-BERT

#### Before embedding space
- A scatter plot of dots in a bounded box labeled "before."
- Dots in two colors: #4A90D9 (blue, questions) and #27AE60 (green, answers).
- Dots are scattered with poor clustering — intermixed, no clear grouping.

#### After embedding space
- A second scatter plot labeled "after."
- Same colored dots, but now clustered — blue-green pairs sit close together.
- Clear clusters visible, with separation between unrelated pairs.

#### Connecting arrow
- An arrow from "before" to "after" labeled "financial Q&A training data."

#### Label
- Below: "fine-tuned Sentence-BERT."

### Right side: FinBERT Ensemble

#### Three model icons
- Three FinBERT blocks stacked vertically, each labeled "checkpoint 1/2/3."
- Each produces a slightly different score displayed to its right:
  - Checkpoint 1: "0.72."
  - Checkpoint 2: "0.68."
  - Checkpoint 3: "0.74."
- Color: #4A90D9 (blue) for each.

#### Convergence
- Three arrows converge into a single averaged output: "ensemble: 0.71."
- Output highlighted in #27AE60 (green).

#### Variance comparison
- Two small text lines below:
  - "single checkpoint variance: 0.09" — struck through, #E74C3C (red).
  - "ensemble variance: 0.03" — highlighted, #27AE60 (green).

#### Label
- Below: "FinBERT ensemble."

## Animation sequence
1. Left "before" scatter appears (1.5s).
2. Arrow draws, "after" scatter appears with tight clusters (2s).
3. "fine-tuned Sentence-BERT" label fades in (0.5s).
4. Right: three checkpoint blocks appear with scores (2s).
5. Arrows converge, ensemble score appears (1.5s).
6. Variance comparison lines fade in (2s).
7. "FinBERT ensemble" label fades in (0.5s).

## Palette
- Question dots: #4A90D9 (blue)
- Answer dots: #27AE60 (green)
- Training arrow: #F1C40F (gold)
- Checkpoint blocks: #4A90D9 (blue)
- Ensemble output: #27AE60 (green)
- High variance: #E74C3C (red, struck through)
- Low variance: #27AE60 (green)
- Background: #1A1A2E
