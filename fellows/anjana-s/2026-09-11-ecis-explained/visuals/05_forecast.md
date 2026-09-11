# Beat 5 — The Forecast View

**Visual type:** Remotion
**Duration:** ~8 seconds

## What the viewer sees

**Forecast cards (0-4s):**
Three company forecast cards appear in a row, each in gold-bordered style:

Card 1 (Company A):
- "Predicted: raised" (green up arrow)
- Confidence: 0.73
- Top driver: "3 consecutive raises"
- Small indicator: "Agrees with sector" (green dot)

Card 2 (Company B):
- "Predicted: maintained" (blue horizontal arrow)
- Confidence: 0.68
- Top driver: "sector mixed"
- Small indicator: "Mixed sector signal" (amber dot)

Card 3 (Company C):
- "Predicted: lowered" (red down arrow)
- Confidence: 0.61
- Top driver: "stock momentum -6%"
- Small indicator: "Disagrees with sector" (red dot)

Each card appears with a slight stagger.

**Prediction timeline (4-8s):**
Below the cards, a horizontal timeline for Company A appears. Past quarters plotted:
- Q1: predicted raised, actual raised (green dot)
- Q2: predicted raised, actual raised (green dot)
- Q3: predicted raised, actual maintained (red dot)
- Q4: predicted raised (gold dot, pending, no actual yet)

The Q4 dot is open/unfilled, conveying that this prediction is still waiting. The track record is visible: mostly right, sometimes wrong.

The dashboard feels alive and forward-looking.

## Technical notes

- Forecast cards use gold border to distinguish from extraction signal cards (blue)
- Each card is compact, one prediction per card with minimal stats
- The sector agreement indicator (green/amber/red dot) adds a layer without complexity
- The timeline at the bottom connects past performance to the current open prediction
- Company A, B, C only
