**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 15 — Business Analytics

**Timeline:** October 4, 2026 – October 10, 2026

**Scope:** Sector-level sentiment analytics, management behaviour metrics, signal-to-price attribution, surprise analytics, and multi-horizon reaction analysis.

---

## Sector Sentiment Aggregator
- **Inputs:** per-company tone, hedging index, and forward-looking density
- **Aggregation:**
  - Mean, median, and standard deviation per sector
  - Weighted by market cap
- **Sector definition:** GICS classification across the 25-ticker universe
- **Storage:** timestamped aggregates in PostgreSQL
- Exposed as sector composite scores in the dashboard

## Sector Mood Index
- **Composite of:**
  - Mean FinBERT polarity
  - Hedging ratio
  - Forward-looking density
- Computed per sector per quarter
- Rendered as a time series, with highlights where the index crosses the sector's historical mean
- Flags sector-level sentiment regime changes

## Cross-Sector Comparison
- Z-scores of sentiment, hedging, and confidence relative to the cross-sector distribution
- Identifies sectors that are unusually optimistic or pessimistic relative to the market
- Comparative heatmap across sectors and quarters

## Management Confidence Score
- **Scale:** 0–100, computed per call and per speaker
- **Components:**
  - Inverse hedging index
  - Forward-looking density
  - Definitive-statement ratio
  - Numerical specificity: concrete numbers, dates, and targets vs. vague qualifiers
- Tracked quarter over quarter per company

## Guidance Language Tracker
- **Compares each quarter's guidance language with the prior quarter's:**
  - **Numerical specificity:** concrete targets vs. directional language
  - **Time-horizon references:** near-term vs. long-term
  - **Qualifier density**
- Flags significant moves toward vagueness or specificity, with a directional change score

## CEO vs. CFO Tone Divergence
- Uses normalized speaker labels to isolate CEO and CFO segments
- **Per-speaker metrics:**
  - FinBERT sentiment
  - Hedging index
  - Confidence score
- **Divergence:** absolute CEO–CFO difference
- Flags calls that exceed the company's historical divergence norm, a possible indicator of internal disagreement or a messaging split

## Signal-to-Price Impact Correlation
- **Features evaluated:**
  - Direction and confidence level
  - Hedging index
  - Tone-shift magnitude
- **Statistics:** Pearson and Spearman correlation with excess returns at 1, 5, and 30 days
- Features ranked by predictive informativeness
- Persisted in PostgreSQL and shown as a feature-importance table

## Surprise Score Analytics
- **Three surprise dimensions:**

| Dimension | Question answered |
|---|---|
| NLP vs. consensus | Did the model detect something analysts missed? |
| Consensus vs. actual | Standard earnings surprise |
| NLP vs. actual | Model accuracy |

- Cross-tabulation isolates the scenarios where the NLP pipeline adds value beyond consensus
- Surprise distributions visualized per quarter

## Reaction Window Analysis
- **Excess return windows:** same day, 1, 2, 5, 10, and 30 days
- Cumulative abnormal return (CAR) curves per signal
- **Classification:**
  - Immediate reaction
  - Delayed reaction (continued drift / underreaction)
  - Reverting reaction (overreaction)
- Curves grouped by confidence tier

## Dashboard
- **Sector:** sentiment overview, mood-index time series, cross-sector heatmap
- **Management:**
  - Confidence trend lines
  - Guidance specificity change flags
  - CEO–CFO divergence alerts
- **Market:**
  - Signal-to-price feature importance ranking
  - Surprise distributions
  - Reaction window curves
- **Global filters:** sector, quarter, confidence tier

## Validation
- Full pipeline re-run with business analytics enabled
- Sector aggregation validated across the 25-ticker set
- Management confidence scores confirmed to correlate with historical guidance accuracy
- Surprise analytics verified to cross-reference consensus, NLP predictions, and actual outcomes correctly
- Signal-to-price correlations benchmarked to identify the features with the most predictive weight
