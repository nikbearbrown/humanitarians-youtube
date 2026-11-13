# Mycroft Phase 4 — Production Plan (9:16, 4K)

Everything below is derived from `Mycroft_Phase4_Regime_Aware.ipynb` and its executed outputs.
No metric, library, API or capability appears here that is not in that notebook.
Provenance for every number: `docs/FACTCHECK.md`.

---

## 1. Video title

**Primary:** *Mycroft Phase 4 — Teaching a Forecasting Model Where It Is Wrong*

Alternates:
- *Mycroft Phase 4 — Regime-Aware Adaptive Forecasting*
- *One AUC Score Hides Four Different Markets — Mycroft Phase 4*
- *Why My Model Is Worst When the Market Is Calm*

## 2. Mandatory opening sentence (final)

> "Hi, I am Dhrumil Shah, and this video is about Mycroft Phase 4, where I added market-regime
> discovery and regime-aware thresholds so the system reports **where** its forecasts hold up,
> instead of one score for every market."

## 3. What Phase 4 accomplishes — summary

Phase 3 ended with a single honest verdict: five-day price direction was close to a coin flip.
Phase 4 asks whether that weakness is **uniform**, and answers it: it is not.

Phase 4 adds five things to the pipeline:

1. **Market-regime discovery** — 7 market-level features per day, K-means into 4 regimes, the
   clustering fit on training dates only, then applied forward.
2. **Named regimes** — `calm_bull`, `sideways_mixed`, `high_volatility`, `stressed_bear`,
   labelled from cluster centroid behaviour rather than left as anonymous IDs.
3. **A regime-aware classifier** — ExtraTrees over 19 price/volume features **plus the regime id**.
4. **Per-regime diagnostics** — the model is scored separately inside each regime.
5. **Adaptive thresholds and a research queue** — each regime gets its own decision cut-off,
   tuned on validation for balanced accuracy; only names that clear it by 0.08 are queued.

**The finding.** Overall test ROC-AUC is **0.5178** — still weak. But by regime:
**high_volatility 0.5359**, **sideways_mixed 0.5239**, **calm_bull 0.4909** (below chance).
And permutation importance puts **`regime_id` first by an order of magnitude** over every
technical indicator. Phase 4's deliverable is not a better score — it is a system that localises
its own weakness and reports it.

## 4. Recommended duration

**3:16 (196 s)** — the sum of the 14 scene durations below. The reference film runs 3:00; Phase 4
has one extra act (per-regime results), so 180–200 s is the right envelope. No scene runs longer
than 16 s. If you need to land under 3:00, the two cuts that cost least are S03 (−4 s, fold the
question into S02) and S12 (−3 s, tighten to the top bar only).

## 5–8. Scene-by-scene storyboard, narration, visuals, on-screen text

Style follows the reference film: warm cream ground, serif headline + italic sub-line, chip
stacks with arrows, bordered figure cards, 2-column stat cards, terracotta reserved for the
honest/negative finding. Header on every scene: `DHRUMIL SHAH` left, `nn / 14` right.
Footer source line at the bottom of the content column.

---

### S01 · Opening — `0:00 → 0:15` (15 s)

**Narration**
> "Hi, I am Dhrumil Shah, and this video is about Mycroft Phase 4, where I added market-regime
> discovery and regime-aware thresholds so the system reports where its forecasts hold up,
> instead of one score for every market."

**Visual** — Title card. Large serif "Hi, I am Dhrumil Shah." with an italic sub-line. Beneath it,
a four-chip vertical stack fading in one at a time: `Market regimes` → `Regime-aware model` →
`Adaptive thresholds` → `Research queue`, the last in terracotta.

**On-screen text** — `MYCROFT · PHASE 4` (kicker) · "Regime-Aware Adaptive Forecasting" (sub-line)

**Editing** — Chips spring in at 0.35 s intervals, 12 px rise. No hook before the greeting.

---

### S02 · Where Phase 3 left off — `0:15 → 0:28` (13 s)

**Narration**
> "Phase 3 ended with an honest result. Across a hundred and twenty tickers, five-day direction
> came out close to a coin flip. One number — for every market condition."

**Visual** — A single wide card holding the Phase 3 verdict, then a dimmed copy of it splitting
into four faint ghost cards (the coming regimes) to foreshadow the question.

**On-screen text** — Headline: "One score for every market." · Card: `≈ 0.52 ROC-AUC · 5-day direction`
· Footer: `Phase 3 result — carried forward as context`

**Editing** — The single card splits into four on the word "every"; ghosts stay at 25% opacity.

---

### S03 · The Phase 4 question — `0:28 → 0:40` (12 s)

**Narration**
> "That single number hides something. A calm market and a crash are not the same problem.
> Phase 4 asks whether the model's weakness depends on the regime it is predicting in."

**Visual** — Two side-by-side sparkline cards drawn from the regime map: a flat calm stretch and
the early-2020 drop. A large question mark sits between them.

**On-screen text** — Headline: "Is the weakness the same everywhere?" · Labels: `calm` / `crash`

**Editing** — Question mark scales in from 1.5× with a spring on "depends".

---

### S04 · The data — `0:40 → 0:51` (11 s)

**Narration**
> "The input is unchanged — one hundred and eighty-four thousand rows, one hundred and twenty
> tickers, January twenty-twenty to February twenty-twenty-six. Same data, new question."

**Visual** — 2 × 2 stat-card grid.

**On-screen text**
| card | value | label |
|---|---|---|
| 1 | `184,138` | rows |
| 2 | `120` | tickers |
| 3 | `2020-01-03` | first date |
| 4 | `2026-02-11` | last date |

Footer: `load_data() — schema check, duplicate drop, tz-normalised dates`

**Editing** — Cards land in reading order, 0.25 s apart. Values count up over 0.6 s.

---

### S05 · Architecture — `0:51 → 1:06` (15 s)

**Narration**
> "The pipeline gains a layer. Daily prices become a market table; the market table becomes
> regimes; the regime label joins the features; and the model learns a separate decision
> threshold for each regime."

**Visual** — The vertical workflow diagram, revealed top to bottom in step with the narration:

```
Daily prices  (184,138 rows · 120 tickers)
        ↓
Feature engineering  (19 model features)
        ↓
Market table  (1 row per day · 7 regime features)
        ↓
K-means, k = 4  — fit on training dates only
        ↓
Named regimes  calm_bull · sideways_mixed · high_volatility · stressed_bear
        ↓
ExtraTrees classifier  (19 features + regime_id)
        ↓
Per-regime thresholds  (tuned on validation)
        ↓
Research queue  (|p − threshold| ≥ 0.08)
```

**On-screen text** — Headline: "One new layer, top to bottom." · The boxes marked **NEW IN PHASE 4**
are the market table, K-means, named regimes, and per-regime thresholds — badge them in terracotta.

**Editing** — Each box springs in with its connector arrow; the four NEW badges pulse once.

---

### S06 · Building the market table — `1:06 → 1:19` (13 s)

**Narration**
> "First, I collapse every ticker into one row per day — market return, cross-sectional
> volatility, median twenty-day return and volatility, advance rate, and rolling twenty-day
> volatility and momentum. Seven numbers that describe the whole market."

**Visual** — Code card (see §9, segment A) with the `groupby("Date").agg(...)` block, then seven
chips flying out of it into a row: the seven regime features.

**On-screen text** — Headline: "120 tickers → 1 row per day." · Chip row: the 7 feature names
· Footer: `REGIME_FEATURES — market-level, not per-ticker`

**Editing** — Highlight the `.agg(` lines; chips emit on the word "seven".

---

### S07 · Discovering the regimes — `1:19 → 1:34` (15 s)

**Narration**
> "Then K-means splits those days into four regimes. The clustering is fit only on the training
> dates and then applied forward, so no future day shapes the clusters. Each cluster gets a
> readable name from its centroid."

**Visual** — Code card (segment B): the `Pipeline([StandardScaler, KMeans(n_clusters=4)])`, the
`fit(regime_train[...])` line highlighted, then `predict(market[...])`.
Beside it, a small timeline bar showing train / validate / test split with the clustering arrow
pointing only at the train portion.

**On-screen text** — Headline: "Fit on the past. Applied forward." ·
Callout: `no future day shapes the clusters` · Footer: `date_split(market) — 70 / 15 / 15 by date`

**Editing** — The `fit` line highlights amber; an arrow animates from it to the train segment only.

---

### S08 · The regime map — `1:34 → 1:49` (15 s)

**Narration**
> "Here is the map. Stressed bear is almost entirely the early twenty-twenty crash — twenty-four
> days. High volatility, ninety-seven. The market spends most of its life in calm bull, eight
> hundred twenty-one days, or sideways mixed, five hundred fifty-four."

**Visual** — **`assets/figures/fig1_regime_map.png`** (the notebook's own figure) in a bordered
card, full content width. Under it, four count chips coloured to match the plot's legend.

**On-screen text** — Headline: "Four regimes, very unevenly sized." ·
Chips: `calm_bull 821` · `sideways_mixed 554` · `high_volatility 97` · `stressed_bear 24`
· Footer: `Notebook figure — Mycroft Phase 4 Regime Map`

**Editing** — Ken-Burns 1.00 → 1.04 across the scene. Chips land one per named regime.
When "twenty-four days" is said, dim everything except the red cluster at the left of the plot.

---

### S09 · The regime-aware model — `1:49 → 2:03` (14 s)

**Narration**
> "The model is an Extra Trees classifier over nineteen price and volume features, plus the
> regime identifier itself. Train, validation and test are split by date, and missing values are
> filled with training medians only."

**Visual** — Code card (segment C): the `ExtraTreesClassifier(...)` constructor and the
`X_train = train[MODEL_FEATURES + ["regime_id"]]` line, with `+ ["regime_id"]` highlighted.

**On-screen text** — Headline: "Nineteen features — plus the regime." ·
Chips: `n_estimators 350` · `max_depth 14` · `min_samples_leaf 8` · `class_weight balanced`
· Footer: `fillna(X_train.median()) — training statistics only`

**Editing** — `+ ["regime_id"]` gets a terracotta underline that draws left-to-right.

---

### S10 · The honest headline — `2:03 → 2:16` (13 s)

**Narration**
> "The headline is still honest. Test ROC-AUC is point five one eight, and the Brier score is
> point two five — what a coin flip gives you. Regime awareness did not make the model predictive."

**Visual** — Two stat cards (test AUC, Brier) and a full-width terracotta verdict card.

**On-screen text**
- `0.5178` — test ROC-AUC (n = 26,760)
- `0.2501` — Brier score
- Verdict card: **"Regime awareness did not make the model predictive."**
- Footer: `Test = final 15% of dates · chance ROC-AUC = 0.50 · chance Brier ≈ 0.25`

**Editing** — The verdict card slides up last and stays for the remainder of the scene.
Do **not** animate these numbers upward as if they were a win — fade them in flat.

---

### S11 · The real finding — `2:16 → 2:32` (16 s)

**Narration**
> "But split it by regime and something shows up. In high volatility, AUC is point five four.
> Sideways mixed, point five two. In calm bull — the most common regime — it is point four nine,
> below chance. The model is least useful exactly when the market is quiet."

**Visual** — A three-row table, each row a horizontal bar centred on 0.50 so `calm_bull` visibly
extends to the **left** of the line. The 0.50 line is labelled `chance`.

**On-screen text**
| regime | n | ROC-AUC |
|---|---|---|
| `high_volatility` | 1,080 | **0.5359** |
| `sideways_mixed` | 9,600 | **0.5239** |
| `calm_bull` | 16,080 | **0.4909** |

Callout under the table: `stressed_bear had too few test rows to score (< 100) — not shown`
Footer: `Per-regime metrics on the held-out test split`

**Editing** — Bars grow from the 0.50 line; the calm_bull bar grows leftward in terracotta.
This is the emotional centre of the film — hold the finished frame 2 s before cutting.

---

### S12 · What the model actually uses — `2:32 → 2:45` (13 s)

**Narration**
> "Permutation importance agrees. The regime identifier is the single most useful feature, by an
> order of magnitude. Most technical indicators contribute nothing, or slightly hurt."

**Visual** — **`assets/figures/fig2_feature_importance.png`** (the notebook's own figure) in a
bordered card. Highlight the `regime_id` bar with a terracotta outline.

**On-screen text** — Headline: "The regime is the feature." ·
Callout: `regime_id ≫ every price indicator` · Footer: `Permutation importance · ≤ 8,000 test rows · 3 repeats · scored on ROC-AUC`

**Editing** — Outline draws around the top bar as it is named. Note the negative bars are real —
do not crop them out.

---

### S13 · Adaptive thresholds and the queue — `2:45 → 3:00` (15 s)

**Narration**
> "So the thresholds adapt. Each regime gets its own cut-off, tuned on validation for balanced
> accuracy, and only names that clear it by eight points enter the research queue. On the latest
> day — a calm bull day — two names qualified."

**Visual** — Left: the threshold rule as a compact formula card. Right: the queue as two rows.

**On-screen text**
- Rule: `research_signal = positive_watch if p ≥ t + 0.08 · negative_watch if p ≤ t − 0.08 · else neutral`
- `2026-02-11 · regime: calm_bull · threshold 0.50`
- `INTU · Intuit Inc. · p = 0.6315 · +0.1315 · positive_watch`
- `SPGI · S&P Global Inc. · p = 0.5830 · +0.0830 · positive_watch`
- Advisory strip (always on screen in this scene):
  **"Research queue for human review. Educational research output — not financial advice."**

**Editing** — Threshold line animates to 0.50; the two qualifying dots cross it and turn terracotta.
Every other name stays grey below the line.

---

### S14 · Accomplishment, next steps, close — `3:00 → 3:16` (16 s)

**Narration**
> "Phase 4's accomplishment is not a better score. It is a system that knows where it is weak and
> says so. Next: more history behind the rare regimes, calibration measured per regime, and a
> stressed-bear sample large enough to actually test. I'm Dhrumil Shah. Thank you for watching."

**Visual** — Two short lists side by side — **Shipped in Phase 4** and **Still open** — then the
end card.

**On-screen text**
| Shipped in Phase 4 | Still open |
|---|---|
| Market-regime discovery (k = 4) | `stressed_bear`: 24 days — too few to test |
| Regime-aware classifier | Per-regime calibration not yet measured |
| Per-regime diagnostics | Regime labels named from full-period centroids |
| Adaptive per-regime thresholds | Thresholds tuned on one validation window |
| Latest research-signal queue | |

End card: `Mycroft Phase 4` / *Regime-aware. Honest about where it fails.* / `Dhrumil Shah`
Advisory line: `Educational research output. Not financial advice.`

**Editing** — The two lists build alternately, left then right. End card crossfades at "I'm Dhrumil Shah."

---

## 9. Python / Colab segments to demonstrate

Four segments only. Each is trimmed to what fits a 9:16 frame at ≥ 30 px mono, ≤ 46 characters
per line. Full listings in `docs/CODE-SEGMENTS.md`.

**A · S06 — the market table** (what turns 120 tickers into one row per day)
```python
market = features.groupby("Date").agg(
    market_return=("return_1d", "mean"),
    cross_section_vol=("return_1d", "std"),
    median_20d_return=("return_20d", "median"),
    median_20d_vol=("volatility_20d", "median"),
    advance_rate=("return_1d",
        lambda s: float((s > 0).mean()))
).dropna().reset_index()
```
*Why it matters:* every regime decision rests on these seven daily numbers. Highlight `advance_rate`
— the share of names that rose — because it separates a broad rally from a narrow one.

**B · S07 — fitting the regimes without looking ahead**
```python
regime_train, _, _, regime_cut, _ = date_split(market)

regime_pipeline = Pipeline([
    ("scale", StandardScaler()),
    ("cluster", KMeans(n_clusters=4,
                       random_state=42, n_init=20))
])
regime_pipeline.fit(regime_train[REGIME_FEATURES])   # train dates only
market["regime_id"] = regime_pipeline.predict(market[REGIME_FEATURES])
```
*Why it matters:* the single most important correctness line in Phase 4. Scaling and clustering are
learned on the training window and then applied forward. Highlight the `.fit(` line.

**C · S09 — the regime becomes a feature**
```python
X_train = train[MODEL_FEATURES + ["regime_id"]]

model = ExtraTreesClassifier(
    n_estimators=350, max_depth=14,
    min_samples_leaf=8, max_features="sqrt",
    class_weight="balanced",
    random_state=42, n_jobs=-1
)
model.fit(X_train.fillna(X_train.median()), y_train)
```
*Why it matters:* `+ ["regime_id"]` is the whole thesis of Phase 4 in five characters, and §S12
shows it is the feature the model leans on hardest.

**D · S13 — adaptive thresholds and the signal rule**
```python
for regime, group in valid_scored.groupby("regime"):
    best = {"threshold": .50, "balanced_accuracy": -np.inf}
    for threshold in np.arange(.40, .66, .02):
        m = classification_metrics(
            group["target_up_5d"],
            group["prob_up_5d"], threshold)
        if m["balanced_accuracy"] > best["balanced_accuracy"]:
            best = {"threshold": float(threshold), ...}

latest["research_signal"] = np.select(
    [latest["prob_up_5d"] >= latest["adaptive_threshold"] + .08,
     latest["prob_up_5d"] <= latest["adaptive_threshold"] - .08],
    ["positive_watch", "negative_watch"], default="neutral")
```
*Why it matters:* it closes the loop — a per-regime cut-off chosen on validation, and a margin
requirement that keeps borderline names out of the queue.

**Demonstration pattern used throughout:**
`Input → Python processing → Mycroft Phase 4 component → Output`
e.g. S07: *daily market table → StandardScaler + KMeans → regime label per day → the regime map.*

## 10. Diagrams and animations

| # | Diagram | Scene | Notes |
|---|---|---|---|
| D1 | Vertical pipeline (9 boxes, 4 badged NEW) | S05 | The spine of the film; reuse its boxes as section markers |
| D2 | Train / validate / test timeline with the clustering arrow on train only | S07 | Makes the no-lookahead claim visible |
| D3 | Regime map (notebook figure) | S08 | Real output — do not redraw |
| D4 | AUC-vs-0.50 diverging bars | S11 | The one chart that carries the finding |
| D5 | Feature importance (notebook figure) | S12 | Real output — keep the negative bars |
| D6 | Threshold line with two qualifying dots crossing it | S13 | Ties the rule to the queue |

Animation discipline: one idea per scene, springs at 12–16 px rise, no spins, no parallax.
Figures get a slow 4% Ken-Burns only.

## 11. Editing and transitions

- Hard cut between scenes, 7-frame cross-dissolve on the two figure scenes only.
- Code: reveal line-by-line at ~2 frames per line; highlighted lines get an amber left bar and a
  lifted background, matching the reference film's code cards.
- Highlighting is subtractive — dim the rest of the card to 45% rather than flashing the target.
- Terracotta appears **only** on honest-limitation content (S02 verdict, S10 verdict, the
  `calm_bull` bar in S11, the `regime_id` outline in S12, the two queue rows in S13).
- Counters count up only for descriptive counts (S04, S08). Metrics never count up.
- Audio: one voice, no music bed under the S10–S11 verdicts; if a bed is used elsewhere, duck it
  to −22 dB under narration.

## 12. 9:16 layout recommendations

| Element | Value (design canvas 1080 × 1920) |
|---|---|
| Safe margins | left/right 76 px → content width 928 px |
| Header | `DHRUMIL SHAH` + section left, `nn / 14` right, at y 200 |
| Headline | serif, 56–64 px, from y 270 |
| Italic sub-line | 26 px, directly under the headline |
| Content column | y 420 → y 1340 |
| Source/footer line | y 1360, mono 15 px |
| Captions | burned in, y 1390–1460, 30 px semibold, one line, 4–8 words |
| Code | mono ≥ 30 px, ≤ 46 characters per line, cards ≤ 928 px wide |
| Figures | full content width, bordered card, caption underneath at 15 px |
| Nothing essential | above y 200 or below y 1470 |

Test every code frame at 1080-logical width before rendering at 4K — if it is unreadable at
540 px wide it is unreadable on a phone.

## 13. 4K export specifications

| Setting | Value |
|---|---|
| Resolution | **2160 × 3840** (9:16 vertical UHD) |
| Method | design at 1080 × 1920, render at `--scale=2` — re-rasterised, never upscaled |
| Frame rate | 30 fps (the reference is 24 fps; 30 is smoother for code reveals — pick one and keep it) |
| Video codec | H.264 High, CRF 16, `yuv420p`, `+faststart` |
| Audio | AAC 48 kHz stereo, 320 kbps master |
| Loudness | −14 LUFS integrated, −1.5 dBTP |
| Derived masters | 1080 × 1920 (CRF 17) · 720 × 1280 (CRF 20) · 540 × 960 proxy (CRF 24), Lanczos |
| Naming | `Mycroft-Phase-4-4k(9x16)_Dhrumil_Shah.mp4` |

## 14. Closing statement

> "Phase 4's accomplishment is not a better score — the model is still close to a coin flip, and
> the film says so twice. What Phase 4 built is a system that knows *where* it is weak: it
> discovers market regimes without looking ahead, scores itself separately inside each one, and
> finds that its worst performance comes in the calmest, most common market. Its most useful
> feature turns out to be the regime label itself. That turns a flat, unusable result into a map
> of where to look next — and that map is what Phase 5 will build on: more history behind the
> rare regimes, calibration measured per regime, and enough stressed-bear data to finally test
> the case the model was built for."

---

## Accuracy notes for the editor

Things that are **true and must stay true** in the cut:

1. The overall result is **weak** — 0.5178 test ROC-AUC. Never frame Phase 4 as a accuracy win.
2. `calm_bull` is **below chance** (0.4909). Show it below the 0.50 line.
3. `stressed_bear` is **not** in the per-regime table — only 24 regime days, and under 100 test
   rows, so the notebook skips it. Say so on screen.
4. The per-regime threshold table is computed for every regime, but only `calm_bull`'s value
   (0.50) is visible in the executed output. Do not put invented numbers on the other regimes.
5. Feature importances are **small in absolute terms** (`regime_id` ≈ 0.017 AUC). "An order of
   magnitude above the others" is accurate; "large" is not.
6. Exactly **two** names qualified on 2026-02-11, both `positive_watch`. There were no
   `negative_watch` names that day.
7. Work in progress, not achievements: per-regime calibration, the regime-label naming step
   (centroids computed over the full period), and anything about Phase 5.
