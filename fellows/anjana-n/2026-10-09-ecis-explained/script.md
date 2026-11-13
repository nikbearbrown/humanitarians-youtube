# ECIS Episode 10 — The Business Layer: Full Script

**Skill:** ai-explainer
**Voice:** af_bella (Anjana) — source `beats.json` says `am_onyx`; overridden per
the series convention set in Episode 1 (Anjana narrates, no channel handle)
**Target length:** ~3:45 (16:9 master) / ~2:40 (9:16 short)
**Series:** Sequel to Episodes 1–9. Episode 9 turned the instruments on the
system itself. Episode 10 turns them outward: the same signals, rolled up into
something a desk could actually act on.

---

## B00 — The Ask (cold open)

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~13s

**Narration:**

Nine episodes of building a thing that reads earnings calls one company at a
time. The question a desk would actually ask is a different one: so what? I'm
Anjana — this week ECIS learns to answer it.

**Composer ask:**

> ECIS produces a graded signal per company per call. But nobody trades one
> signal. Which sectors are shifting, which executives are hedging, and which
> of these features actually moves a price — and over what horizon?

**Output lines (resolved on screen):**
- company signals rolled up to sector mood
- confidence scored per speaker, CEO against CFO
- features ranked by what actually moves price

---

## B01 — Recap (20s)

### Narration
ECIS extracts financial guidance signals from earnings call transcripts using four readers — keyword, FinBERT, NER, and LLM — triangulated with dynamic weights across reader, model, speaker, chunk quality, and section type. A prediction layer forecasts next-quarter direction from signal features and market data, with every prediction pre-registered and graded at 30, 90, and 180 days. Episode 9 added statistical rigor — bootstrap confidence intervals, permutation tests, concept drift detection — plus data lineage tracking, ChromaDB optimization, and Grafana monitoring dashboards. Now in Episode 10: the business analytics layer that turns raw signals into sector-level intelligence.

### Visual direction
Compressed pipeline schematic: four reader icons feed into the triangulator, which feeds the prediction layer (scorecard icon), then monitoring (Grafana panels). Each stage lights up as narrated. The pipeline then extends rightward to a new glowing section labeled "business analytics" with a gold outline, pulsing to signal the new addition.

---

## B02 — Sector Intelligence (12s)

### Narration
The system now rolls individual company signals up to the sector level. A sector sentiment aggregator computes market-cap-weighted composites of tone, hedging, and forward-looking density across every company in a GICS sector. The mood index tracks how that composite shifts quarter over quarter, flagging regime changes. And a cross-sector heatmap benchmarks each sector's language metrics against all others using z-scores — showing which sectors are unusually optimistic or pessimistic relative to the market.

### Visual direction
Three panels. Left: a funnel showing individual company signal dots rolling up into a single sector bar, labeled "sector sentiment aggregator." Center: a time-series line chart showing the mood index across quarters — the line crosses a dashed historical mean, with the crossing point highlighted and labeled "regime change." Right: a heatmap grid — rows are sectors (Tech, Healthcare, Finance, Energy), columns are metrics (sentiment, hedging, confidence). Cells are colored by z-score: green for positive, red for negative, grey for neutral. Label: "cross-sector heatmap."

---

## B03 — Management Behavior (10s)

### Narration
Two new modules watch how executives actually talk. A management confidence score combines hedging ratio, forward-looking density, definitive statement ratio, and numerical specificity into a zero-to-hundred scale per speaker, per call. And a CEO-versus-CFO tone divergence detector flags calls where the two executives score differently on sentiment and confidence — potential signals of internal disagreement or strategic messaging.

### Visual direction
Split view. Left: a vertical gauge (0–100) labeled "management confidence." The needle sits at 72. Four small input arrows feed into the gauge, labeled "hedging (inv)," "fwd-looking," "definitive," "specificity." Below, a small trend sparkline shows the score across four quarters. Right: two speaker icons — one labeled "CEO," one "CFO." Below each, a horizontal bar: CEO bar at 78 (green), CFO bar at 51 (orange). The gap between them is highlighted with a red bracket and a small alert icon. Label: "divergence: 27 points — flagged."

---

## B04 — Signal Value (12s)

### Narration
Which signals actually move prices? A signal-to-price correlation module computes Pearson and Spearman correlations between every extracted feature — direction, confidence, hedging, tone shift — and excess returns at one-day, five-day, and thirty-day horizons. It ranks features by predictive informativeness. Alongside that, a surprise score module cross-tabulates three dimensions: what the NLP model predicted, what consensus expected, and what actually happened. The most valuable quadrant: signals where the model saw something analysts missed.

### Visual direction
Two panels. Left: a ranked horizontal bar chart showing feature importance. Bars sorted by correlation strength: "tone shift magnitude" (longest bar, gold), "confidence level" (medium, blue), "hedging index" (medium, green), "direction signal" (shorter, purple). Each bar has a small correlation value (e.g., r=0.34). Three sub-labels per bar: "1d," "5d," "30d" as small dot indicators. Right: a 2x2 matrix. Rows: "NLP predicted raised / lowered." Columns: "consensus expected raised / lowered." Cells show counts. The top-right cell (NLP raised, consensus lowered) glows gold with label: "model saw it first." A small badge: "surprise score analytics."

---

## B05 — Reaction Windows (12s)

### Narration
The final piece: how does the market actually respond over time? A reaction window module plots cumulative abnormal returns at same-day, one-day, two, five, ten, and thirty days after an earnings call. Some signals show immediate pricing — the market reacts within hours. Others show continued drift — the market underreacted and keeps moving. And some show mean reversion — the initial reaction was an overreaction that fades. The dashboard groups these curves by signal confidence tier, showing exactly where the pipeline's high-confidence calls carry the most lasting impact.

### Visual direction
Three cumulative abnormal return curves, each starting at time zero (earnings call) and extending to day 30 on the x-axis. Top curve (blue): labeled "immediate pricing" — sharp jump at day 0, then flat. Middle curve (green): labeled "continued drift" — moderate jump, then steady upward slope continuing through day 30. Bottom curve (red): labeled "mean reversion" — sharp jump at day 0, then curves back toward zero. X-axis: "days after earnings call" (0, 1, 2, 5, 10, 30). Y-axis: "cumulative abnormal return (%)." A small filter toggle at top-right: "confidence tier: high." Label below: "reaction window analysis."

---

## B06 — Your Turn (7s)

### Narration
Sector intelligence. Management behavior. Signal value. Reaction timing. The business layer makes ECIS answer not just what was said, but what it means for the market. ECIS Episode 10: The Business Layer.

### Visual direction
Wide pullback of the full ECIS architecture with Ep10 additions glowing. New additions glow gold in sequence: sector aggregation funnel, mood index line, cross-sector heatmap, confidence gauge, CEO-CFO divergence bars, feature importance ranking, surprise matrix, reaction window curves. Each pulses gold briefly then settles. Architecture fades. Centered text: "ECIS Episode 10: The Business Layer."

---

## B07 — Verdict

**Pattern:** `ClaudeVerdictArtifact` · **Duration:** ~26s

**Narration:**

Let's recap with Claude. Nine episodes produced a signal per company per call,
and this one turns that into something you could put in front of a desk.
Individual signals aggregate into sector mood, benchmarked against every other
sector. How executives talk becomes a score, and a gap between the CEO and the
CFO becomes a flag. Every extracted feature gets ranked by how well it actually
correlates with excess return. And the reaction curves say not just whether the
market moved, but when, and whether it stayed moved.

**Artifact lines:**
- Company signals roll up to market-cap-weighted sector composites, with a mood
  index and a cross-sector z-score benchmark.
- Management confidence is scored 0–100 per speaker; CEO-versus-CFO divergence
  is flagged.
- Every feature is ranked by correlation with excess return at 1, 5 and 30 days.
- Reaction windows separate immediate pricing from continued drift and mean
  reversion, grouped by confidence tier.

---

## B08 — Your Turn

**Pattern:** `ClaudeComposerAsk` · **Duration:** ~34s

**Narration:**

Your turn. Take the signals you already produce and ask what the aggregate of
them says that no single one does. Then ask which of the things you measure has
ever actually been checked against an outcome, rather than assumed to matter.
And whether you know how long the effect lasts — because something that moves
and then reverts is a very different finding from something that keeps moving.

**Composer ask:**

> I produce lots of individual signals or scores — per customer, per ticket, per
> account, per case. Can you help me: one, work out what the aggregate of them
> would say that no single one does, and at what grouping that becomes useful;
> two, name which of the things I measure has ever actually been tested against
> a real outcome rather than assumed to matter; and three, tell me honestly how
> I'd find out whether an effect I see persists or reverts — and why that
> distinction changes what I should do about it?

---

## B09 — Title outro

**Pattern:** `ClaudeTitleOutro` · **Duration:** ~5s

**Narration:**

Anjana here, thanks for watching.

**Title:** ECIS — Episode 10
**Subline:** the business layer · episode ten
**Handle:** (none)
