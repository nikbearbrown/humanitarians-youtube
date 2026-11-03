# B03 — False Positives and Signal Chains

## Composition type
Remotion

## Layout
Dark stage. Left half: false positive analysis (pie chart + example card). Right half: multi-quarter signal chain timeline.

## Elements

### Left: False Positive Analysis

#### Pie chart
- Five slices labeled with root causes:
  1. "ambiguous language" — #E67E22 (orange), largest slice (~30%).
  2. "sarcasm misread" — #9B59B6 (purple), ~20%.
  3. "section misattribution" — #4A90D9 (blue), ~20%.
  4. "context-dependent" — #1ABC9C (teal), ~15%.
  5. "anomalous market" — #95A5A6 (grey), ~15%.
- Label above: "false positive root causes."

#### Example signal card
- Small card above the pie chart.
- Line 1: "confidence: 0.82" — crossed out with #E74C3C (red) strikethrough.
- Line 2: "adjusted: 0.61" — in #F1C40F (gold).
- Small tag: "ambiguous language pattern detected."

### Right: Multi-Quarter Signal Chain

#### Timeline
- Four quarterly columns: Q1, Q2, Q3, Q4.
- Three signal bars per quarter, stacked:
  - "hedging" — #E67E22 (orange). Bar height increases Q1 → Q3.
  - "confidence" — #27AE60 (green). Bar height decreases Q1 → Q3.
  - "dodge" — #E74C3C (red). Bar height stable.

#### Chain bracket
- A gold (#F1C40F) bracket spans Q1–Q3 below the bars.
- Label: "sustained deterioration — chain length 3."

#### Q4 indicator
- Q4 column highlighted with a gold border.
- Small label: "weighted signal ×1.5."

## Animation sequence
1. Pie chart draws, slices appearing clockwise (2s).
2. Example card appears above with strikethrough animation (1.5s).
3. Right: quarterly columns appear with signal bars (2s).
4. Hedging bars grow taller across Q1–Q3 (1s).
5. Confidence bars shrink across Q1–Q3 (1s).
6. Gold bracket appears with "sustained deterioration" label (1.5s).
7. Q4 highlights with weight multiplier (1s).

## Palette
- Ambiguous language: #E67E22 (orange)
- Sarcasm misread: #9B59B6 (purple)
- Section misattribution: #4A90D9 (blue)
- Context-dependent: #1ABC9C (teal)
- Anomalous market: #95A5A6 (grey)
- Strikethrough: #E74C3C (red)
- Adjusted confidence: #F1C40F (gold)
- Hedging bars: #E67E22 (orange)
- Confidence bars: #27AE60 (green)
- Dodge bars: #E74C3C (red)
- Chain bracket: #F1C40F (gold)
- Background: #1A1A2E
- Text: #EAEAEA
