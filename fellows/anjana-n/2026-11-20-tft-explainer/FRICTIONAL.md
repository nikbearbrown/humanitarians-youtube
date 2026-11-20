# Friction Log: What a Temporal Fusion Transformer Actually Does

**Week:** Week 21, November 15 – 21, 2026

## 1. Date and focus
A video on the Temporal Fusion Transformer (TFT):
- variable selection
- gated residual networks
- interpretable attention
- why it does better than LSTMs over longer horizons

## 2. What was tried, and what was expected
- The brief's examples were expected to be correct as written.
- Its claims were expected to be easy to show on screen.
- The narration was expected to fit 45 to 70 words per section.

## 3. Where things got stuck, and what was done next
- **Wrong lookback in the attention scene:** the brief said the t+5 prediction looks back to t-5, "the same quarter last year". In quarters, t-5 is ten steps back, two and a half years, and the same quarter a year before t+5 is t+1, which is still in the future. The lookback points are now calculated: t+1 looks at t-1, and t+5 looks at t-3, exactly two years earlier.
- **Ending:** the video ends on the title card
- **Length:** all five sections ran long, and they were kept as written.

## 4. What Claude contributed, and what was kept or changed
- **Original work:** concept, brief and main narration.
- **Claude:**
  - assembled the video using the video generation tool created by Humanitarians AI
  - wrote the opening, summary, viewer prompt and outro
  - spotted the lookback issue
- **Accepted:** the calculated lookback points
- **Kept as written:** all narration.

## 5. What is understood now, and what is still open
**Understood:**
- The concepts: variable selection networks, gated residual networks and skip connections, interpretable attention, and multi-horizon forecasting.

**Open:**
- None