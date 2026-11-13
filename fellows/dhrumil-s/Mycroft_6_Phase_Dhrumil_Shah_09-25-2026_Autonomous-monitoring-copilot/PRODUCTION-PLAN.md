# PRODUCTION PLAN — Mycroft Project, Phase 6 (9:16, 4K)

14 scenes · **3:51 (231.33 s)** · 1080 × 1920 design canvas, mastered at 2160 × 3840 · 30 fps.

Every scene length is the **measured** length of its Kokoro narration — nothing stretched or
padded. All figures quoted are from the executed notebook; provenance in `docs/FACTCHECK.md`.

---

## Title and description

**Title (YouTube / LinkedIn):**
*Mycroft Phase 6 — I Built an Explainable AI Monitoring Copilot (5 Agents, One Queue)*

Alternates: *Five AI Agents Watch the Market. Every Alert Explains Itself.* ·
*Mycroft Phase 6 — Explainable Autonomous Monitoring in Python*

**Description:**
> Phase 6 of my Mycroft project integrates five independent research agents into one auditable
> monitoring pass over 120 tickers. A robust anomaly detector, a peer-weakness ranker, a risk
> scorer, a thesis-deterioration watcher and an isolation forest each raise their own flag. A
> transparent review-priority score — plain integer weights, no learned model — combines them into
> a ranked human review queue, and every alert carries the number that caused it. Outputs include a
> JSON event log with `human_decision` and `human_rationale` left deliberately empty.
>
> Built in Python with pandas, scikit-learn and Google Colab.
>
> Research decision-support only. Agents prioritize evidence and anomalies; the human reviewer
> makes the final decision. Not financial advice.
>
> #Python #MachineLearning #ExplainableAI #ScikitLearn #DataScience #AIEngineering

---

## Production table

| Timestamp | Scene | Visuals | On-Screen Text | Voice-Over | Animation / Transition |
|---|---|---|---|---|---|
| 0:00–0:14 | S01 Introduction | Title card over the dark-navy grid; four capability chips | `Dhrumil Shah` · `MYCROFT PROJECT PHASE 6` · `Explainable Autonomous Monitoring Copilot` · chips: 5 agents / Transparent score / Written reasons / Human decides | "Hi, I am Dhrumil Shah, and this video is about Mycroft Phase 6, where I built an explainable autonomous monitoring copilot that runs five research agents over the market every day, scores what deserves a human look, and writes down exactly why." | Title springs in; chips land 0.27 s apart |
| 0:14–0:27 | S02 Problem | Three stacked cards with down-arrows | `PROBLEM` One analyst, 120 names, every single day. · `CHALLENGE` Automate it and you get a black box: "review this", with no reason. · `PROPOSED` Automate the search — but make every alert explain itself. | "Here is the problem. One analyst cannot watch a hundred and twenty names every day. Automate it and you get the opposite problem: a black box that says review this, with no reason attached. Neither one is usable." | Cards cue to their own sentence |
| 0:27–0:42 | S03 Objective | Previous phases → NEW IN PHASE 6 → Final capability | `Previous phases` each built one kind of signal · `NEW IN PHASE 6` Five agents run together / Weights you can read / A written reason on every alert · `Final capability` an auditable daily monitoring pass | "Phase 6 is the integration phase. Earlier phases each built one kind of signal. Phase 6 runs five of them together, combines them with weights you can read, and attaches a written reason to every single alert. Nothing is a black box." | Teal card expands on "runs five of them together" |
| 0:42–0:57 | S04 Architecture | Market panel → five agent rows → priority → three outputs | `Market panel` 184,138 rows · 120 tickers → `Agent A..E` → `Transparent review priority` → `Review queue` / `JSON event log` / `Human fields` | "The shape is simple. The same market panel feeds five independent agents. Each raises its own flag. A transparent score adds those flags up. That produces a ranked review queue, an auditable event log, and two empty fields waiting for a human." | Agents cascade in 0.23 s apart; arrows fade with the next block |
| 0:57–1:12 | S05 Agent A | `rolling_modified_z` code card + three z-chips + threshold card | `anomaly_severity = max(\|z\|)` · `flag when ≥ 4.0` | "Agent A watches for abnormal days. It computes a rolling modified z-score on returns, volume and intraday range, built on medians rather than means, so a few wild days cannot hide the rest. Anything past four standard-equivalents is flagged." | Median/MAD lines highlighted amber |
| 1:12–1:27 | S06 Agents B + C | Two weight cards | `Agent B · peer weakness` 50% weak 20-day return / 25% high volatility / 25% deep drawdown · `Agent C · risk score` 40% volatility / 35% drawdown / 25% intraday range | "Agent B ranks each name inside its own industry… Agent C scores risk across the whole market on the same day. Both fire in the worst twenty percent." | Second card lands on "Agent C" |
| 1:27–1:41 | S07 Agent D | Five weight rows + trigger card | `THESIS HEALTH · 0–100` 25/20/20/20/15 % · `thesis_change_20d <= -20` | "Agent D carries the thesis-health idea forward from Phase 5… It is watching the change, not the level." | Trigger card on "falls twenty points" |
| 1:41–1:57 | S08 Agent E | IsolationForest code card + eight feature chips | `n_estimators=250, contamination=.03` · `iso.fit(train[ISO_FEATURES]) # train dates only` | "Agent E is the only machine-learning model here. An isolation forest, two hundred and fifty trees, fit on the training dates only…" | The `fit` line highlighted; chips fly in |
| 1:57–2:14 | S09 Priority | Five weight rows + max card | `+2 anomaly_flag` `+1 peer_outlier_flag` `+2 high_risk_flag` `+2 thesis_deterioration_flag` `+2 multivariate_anomaly_flag` · `max 9` | "Now the part that makes it auditable. The priority is a plain sum… No learned weights, no hidden model. Nine is the maximum." | Rows stack; `max 9` card lands last |
| 2:14–2:27 | S10 Explanation | "not: review this" → the real explanation block | `SPGI · S&P Global Inc. · priority 8` · `robust_anomaly(z=7.5)` `risk_score=0.92` `thesis_change20d=-74.0` `isolation_score=0.025` | "And every flag writes its own reason, with the number that caused it…" | Reasons type in one per line |
| 2:27–2:44 | S11 Summary | Three stat cards + five agent-count bars | `120` tickers monitored · `43` flagged for review · `3` priority 5 or above · 29 / 15 / 11 / 4 / 3 | "That produces a daily monitoring summary. On the eleventh of February…" | Bars grow proportional to count |
| 2:44–3:00 | S12 Queue + log | Queue rows + JSON event-log card | `SPGI 8` `SCHW 6` `UNH 5` `EMR 4` `GD 4` · `"human_decision": null` `"human_rationale": null` · `Left empty by design` | "The queue itself is short… two fields left deliberately empty: human decision, and human rationale." | JSON card reveals; null fields in teal |
| 3:00–3:23 | S13 Diagnostic | Notebook figure 2 + four priority cards + caveat | `priority 0 → 17.8%` `4 → 34.4%` `6 → 39.4%` `8 → 40.6%` · "The trend is real — but noisy. It dips at 3, 5 and 7, and the high scores are rare (n = 64 at priority 9)." · **"A historical diagnostic, not a forecast."** | "So does the priority score actually mean anything? Measured over six years…" | Figure holds; caveat card lands on "But it is noisy" |
| 3:23–3:51 | S14 Close | "What I built" list → NEXT list → end card | 5 accomplishments · NEXT: Schedule a daily run / Calibrate weights against outcomes / A reviewer interface · `Mycroft Project Phase 6` `Developed by Dhrumil Shah` | "So, Phase 6… Mycroft Project, Phase 6. Developed by Dhrumil Shah. Thank you for watching." | List builds, then crossfades to the end card |

---

## Which notebook cells to screen-record

| Scene | Cell / region |
|---|---|
| S04 | `load_data()` + the `# PHASE 6` header block |
| S05 | `rolling_modified_z()`, `anomaly_severity`, `anomaly_flag` |
| S06 | the `peer_pct_*` loop, `peer_weakness`, `risk_score` |
| S07 | `health_parts`, `thesis_health`, `thesis_change_20d` |
| S08 | `ISO_FEATURES`, the `iso` Pipeline, `iso.fit(train[...])` |
| S09 | `review_priority` |
| S10 | `explain_row()` and the `explanation` column in the printed queue |
| S11 | the `report` dict and the printed monitoring summary JSON |
| S12 | the `events` loop, `latest_event_log.json`, `latest_queue.head(20)` |
| S13 | `priority_eval` and its printed table, plus figure 2 |

## Animation and transition guidance

Hard cuts between scenes; a 7-frame cross-dissolve only on the figure scene. Springs at 12–16 px
rise, 0.2–0.3 s apart. Code reveals line-by-line, highlighted lines carrying an amber left bar.
Highlighting is subtractive — dim the rest rather than flashing the target. No spins, no parallax,
no stock footage.

## Background music guidance

Restrained technical ambient: low pad plus sparse pluck, no drums and no melody that competes with
speech. Section-mapped — intro, problem, turn, build, model, resolve — and side-chain ducked under
narration. Bed sits roughly 20 dB below the voice; the mix is normalised to −14 LUFS with a
−1.5 dBFS peak.

## Caption policy

Burned in, one line, white on near-black at y 1392, 30 px semibold. Cue times come from
per-sentence measured audio, character-proportional within a sentence. 0 overlaps, 0 single-word
captions, longest wrapped line 29 characters. Full cue list: `captions/captions.json`.

## 9:16 layout

| Element | Value (design canvas 1080 × 1920) |
|---|---|
| Safe margins | left/right 76 px → content width 928 px |
| Progress rule | y 199, teal fill = n/14 |
| Cell header | y 222 — `CELL Cx · SECTION · nn/14` left, `Dhrumil Shah` right |
| Scene title | y 258, 46 px semibold |
| Content column | y 420 → y 1340 |
| Source line | y 1352, mono 15 px |
| Captions | y 1392–1460 |
| Code | mono ≥ 17 px, ≤ 56 characters per line |

## Export checklist

| Requirement | Status |
|---|---|
| 9:16 vertical | ✅ |
| 2160 × 3840 (4K vertical) | ✅ rendered at `--scale=2`, not upscaled |
| 30 fps | ✅ |
| MP4 / H.264 | ✅ |
| Audio 48 kHz, clear voice-over | ✅ AAC 48 kHz stereo, −14 LUFS |
| Synchronised captions throughout | ✅ burned in, cued from measured audio |
| Subtle background music | ✅ ducked bed |
| 2–4 minutes | ✅ 3:51 |
| Opening sentence exact | ✅ first spoken line, no hook before it |
| Mobile-safe area | ✅ nothing essential outside x 76–1004 or y 199–1460 |
| Readable code on a phone | ✅ verified at 540 px review width |
| No fabricated metrics | ✅ audited; S13 states the limits explicitly |
| Advisory boundary shown | ✅ S01 source line, S12 strip, S14 end card |
