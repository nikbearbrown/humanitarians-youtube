# Beat 2 — The Feature Vector

**Visual type:** Remotion
**Duration:** ~15 seconds

## What the viewer sees

**The decision log (0-5s):**
The append-only signal log from Beat 1 glows on the left side. Rows of past signals scroll vertically, each showing a ticker, direction arrow, and date:

- Company A: raised Q1, raised Q2, raised Q3
- Company B: maintained Q1, maintained Q2, lowered Q3
- Company C: lowered Q1, maintained Q2, maintained Q3

The log is full of history. It pulses, signaling that patterns are hidden inside.

**Feature extraction (5-10s):**
From the log, individual features animate out and arrange themselves horizontally in the "future" region on the right side. Each feature appears in its own labeled box:

1. "Prior direction: raised" (green up arrow)
2. "Trend length: 3 quarters" (number: 3)
3. "Stock momentum: +4.2%" (small upward chart line)
4. "Sector aggregate: 60% raised" (small cluster of arrows, mostly green)
5. "Days since last call: 87" (calendar icon)
6. "Prior confidence: 0.84" (number badge)

The boxes snap together into a single horizontal feature vector strip with a gold border (prediction color).

**Prediction output (10-15s):**
The feature vector feeds into a simple model node labeled "Logistic Regression" (small, clean, not complex). The model processes and outputs: "Prediction: raised" with confidence 0.73 in a gold prediction card.

Label: "No new data. Just the patterns in what it already knows."

## Technical notes

- The feature extraction animation should feel like insights pulling themselves out of raw data
- Each feature box should be readable at a glance, one value per box
- The feature vector strip with gold border distinguishes predictions from extractions (blue)
- The logistic regression node should look simple on purpose, the sophistication is in the features not the model
- Company A, B, C only, no real tickers
