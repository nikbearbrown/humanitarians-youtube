# Friction Log: Week 15 (Phase 15)

**Project:** Mycroft — ECIS + Decision Scorecard
**Week:** October 4 – October 10, 2026

---

## 1. Focus of the week

- **Management behavior analytics:** guidance language tracker; CEO vs. CFO tone divergence.
- **Signal-to-market mapping:**
  - signal-to-price impact correlation
  - three-way surprise analytics
  - reaction window analysis
- **Dashboard:** company-level analytics report view; sector summary view (mood index, cross-sector heatmap).
- **Research:** sector aggregation and benchmarking; management behavior analysis; architecture review.
- **Outputs:**
  - two Claude artifacts
  - one Substack article
  - two videos

## 2. What was tried, and what was expected

- **Tone divergence:** CEO and CFO tone on the same call was expected to move together, with divergence as occasional noise.
- **Speaker roles:** existing speaker role matching was expected to identify the CEO and CFO cleanly on every call.
- **Sector mapping:** an open-source ticker-to-GICS sector mapping was expected to be available.
- **Mood index:** a single cross-sector index was expected to compare sectors fairly.
- **Consensus:** analyst consensus was expected to add information beyond the NLP signals.

## 3. Points of resistance, and next steps taken

### CEO–CFO divergence is not noise (load-bearing)
- **What happened:** on some calls, CEO sentiment ran around +0.15 while CFO sentiment ran around −0.08.
- **What resisted:** interpreting the gap. Three explanations compete:
  - genuine disagreement
  - role-constrained language: the CFO role constrains language toward numerical precision, while the CEO role permits narrative management
  - strategic narrative management
- **Next step:** divergence is flagged against historical norms rather than treated as noise. The CFO's hedging is read as a possible sign that the numbers don't fully support the CEO's narrative.
- **Lesson:** detecting the divergence is feature engineering. Interpreting it means reasoning about people through the language they produce.

### Consensus may not add value
- **What happened:** NLP-vs-actual surprise outperformed consensus-vs-actual surprise.
- **What resisted:** whether traditional analyst consensus adds value over purely language-based signals at all.
- **Next step:** reported as a preliminary finding, not a conclusion. It also raises the question of whether the Week 12 FMP consensus integration is overhead.

### CEO–CFO speaker matching (dual titles)
- **What happened:** regex-based speaker identification broke on calls where the CFO also held the COO title.
- **Next step:** fuzzy role matching that handles title combinations.
- **Lesson:** the regex assumed one person, one title. C-suite roles overlap, especially at smaller companies. Speaker identification in transcripts is a parsing problem, not a lookup.

### GICS sector classification mapping
- **What happened:** no clean open-source ticker-to-GICS mapping was available.
- **Next step:** scraped and reconciled two partial sources, which conflicted for about 12% of tickers. About 45 minutes were consumed.
- **Lesson:** the financial data ecosystem assumes Bloomberg terminal access. Building on free-tier data means reconciliation work that institutional users skip.

### Mood index normalization
- **What happened:** the first cross-sector mood index let one high-volatility sector dominate the comparison.
- **Next step:** two-stage normalization. Standardize within each sector first, then z-score between sectors.
- **Lesson:** the Week 12 pattern again. A naive aggregation produces a number that looks meaningful but is dominated by one component.

## 4. AI and other contributions: accepted, changed, rejected

### Claude + Humanitarians AI video generation tool
- **Original work:** the concept, ideas, narration, and direction for both videos.
- **Claude's part:** assembled the videos using the video generation tool created by Humanitarians AI.

### Claude (artifacts)
- **Management Confidence Tracker:** per-company confidence trends, with drill-down into hedging ratio, numerical specificity, and qualifier density.
- **Feature Importance Ranker:** ranks NLP features by correlation with price movement across time horizons.

### Gru (SDD session)
- Documented the architecture.

### Eddy
- Reviewed "Turning Earnings Calls into Competitive Intelligence" before publication.

## 5. Understood now, and still unresolved

### Understood
- **Executive language:** it carries organizational dynamics. Who says what, and with how much precision, is a signal in its own right.
- **Information sources:** comparing them directly (NLP vs. consensus vs. actual) shows which ones actually add information.
- **Speaker roles:** C-suite titles overlap, so role matching has to handle combinations.
- **Aggregation:** standardize within groups before comparing between them, or one component dominates.
- **Free-tier data:** building on it carries hidden reconciliation costs.
- **Long-running items:** three were closed this week:
  - routing complexity (from Week 11)
  - signal decay horizon weighting (from Week 10)
  - sector ETF mapping for multi-sector tickers (from Week 12)

### Unresolved
- **NLP vs. consensus value:** does the FMP consensus integration add value or noise?
- **Power analysis:** at n≈45, the sample is still insufficient for subtle model comparisons. Carried from Week 14.
- **ChromaDB versioning and operational tooling:** carried from Weeks 13–14.
- **GICS reconciliation:** the remaining classification conflicts and their sources still need documenting.
