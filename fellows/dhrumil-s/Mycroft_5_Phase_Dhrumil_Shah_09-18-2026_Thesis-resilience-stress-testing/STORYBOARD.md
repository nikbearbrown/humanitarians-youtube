# STORYBOARD — Mycroft Phase 5 (9:16)

14 scenes · **3:49 (228.86 s)** · 1080 × 1920 design canvas, mastered at 2160 × 3840 · 30 fps.

Every scene length is the **measured** length of its Kokoro narration — nothing was stretched or
padded. Times below are exact.

**Standing frame furniture:** teal progress rule at y 199 (fills n/14), `CELL Bx · SECTION · nn/14`
at y 222 left, `Dhrumil Shah` at y 222 right, scene title at y 258, content from y 420,
source line at y 1352, burned-in caption band at y 1392–1460. Nothing essential below y 1340.

**Music:** code-synthesised bed, section-mapped (intro → problem → pipeline → build → turn →
model → resolve), side-chain ducked under narration. 14 SFX cues, one per scene onset.
Mood: restrained technical ambient — pad + sparse pluck, no drums, no melody that competes.

---

| # | Scene | In → Out | Len |
|---|---|---|---|
| S01 | Opening / title card | 0:00 → 0:13.6 | 13.6 s |
| S02 | From direction to durability | 0:13.6 → 0:24.5 | 10.9 s |
| S03 | Architecture — seven stages | 0:24.5 → 0:41.9 | 17.4 s |
| S04 | Data and features | 0:41.9 → 0:59.9 | 18.0 s |
| S05 | Thesis health — seven ranked factors | 0:59.9 → 1:17.8 | 17.9 s |
| S06 | Thesis states — broken to strong | 1:17.8 → 1:33.3 | 15.5 s |
| S07 | Deterioration — change, not level | 1:33.3 → 1:46.1 | 12.8 s |
| S08 | Contradiction detection | 1:46.1 → 2:05.9 | 19.8 s |
| S09 | Stress testing — bootstrap | 2:05.9 → 2:23.6 | 17.7 s |
| S10 | VaR and CVaR | 2:23.6 → 2:39.8 | 16.2 s |
| S11 | Resilience score | 2:39.8 → 2:55.7 | 15.8 s |
| S12 | Review queue | 2:55.7 → 3:07.9 | 12.2 s |
| S13 | Honest diagnostic | 3:07.9 → 3:24.8 | 16.9 s |
| S14 | Evolution + close (incl. 2 s hold) | 3:24.8 → 3:48.9 | 24.1 s |

---

### S01 · Opening — `0:00 → 0:13.6`

**Narration (exact, as required)**
> "Hi, I am Dhrumil Shah, and this video is about Mycroft Phase 5, where I built a quantitative
> thesis-resilience, contradiction-detection, and stress-testing framework to evaluate the health
> and risk of investment theses using market data."

**On screen** — `Dhrumil Shah` / `MYCROFT PHASE 5` / `Quantitative Thesis Resilience, Contradiction
Detection & Stress Testing`, then four chips: Thesis health · Contradictions · Stress testing ·
Resilience. Source line: *Quantitative research decision support — not financial advice.*

**Editing** — chips spring in at 0.27 s intervals. No hook before the greeting.

### S02 · From direction to durability — `0:13.6 → 0:24.5`

**Narration** — "Earlier phases asked: will this stock go up or down? Phase 5 asks something else.
Is the quantitative thesis still healthy, what evidence contradicts it, and does it survive stress?"

**On screen** — the old question in a muted card, dimming to 45%; the new question below in a
teal-bordered card; then three bullets (Health / Contradiction / Stress).

**Editing** — the dim and the teal card land together on "asks something else".

### S03 · Architecture — `0:24.5 → 0:41.9`

**Narration** — the seven stages, in order.

**On screen** — the vertical pipeline, one box per stage with its sub-label, connector arrows
timed to the *next* box: Stock market data → Feature engineering → Quantitative thesis health →
Contradiction detection → Historical stress testing → Resilience score → **Human review priority**
(teal). Source: *decision support for an analyst, not an autonomous system.*

### S04 · Data and features — `0:41.9 → 0:59.9`

**On screen** — four stat cards (184,138 rows · 120 tickers · 2020-01-03 · 2026-02-11), the 11
input column chips, then 17 engineered-feature chips flying in.
**Screen-record instead:** the `load_data()` and `engineer_features()` cells.

### S05 · Thesis health — `0:59.9 → 1:17.8`

**Code card** `Cell B4 - thesis_health` — the `groupby("Date").rank(pct=True)` loop and the
weighted average, both highlighted.
**Then** — the seven weights as horizontal bars: 20 / 18 / 16 / 15 / 13 / 10 / 8 %.
Source: *cross-sectional percentile ranks, recomputed every date.*

### S06 · Thesis states — `1:17.8 → 1:33.3`

**On screen** — four state cards (broken < 35 · weakening 35–50 · stable 50–65 · strong > 65),
then **notebook figure 1** — six years of one name's thesis health crossing those lines.

### S07 · Deterioration — `1:33.3 → 1:46.1`

**Code card** `Cell B6 - deterioration` — `diff(5)`, `diff(20)`, `shift(20)`, `state_deterioration`.
**Then** — two stat cards (5-day / 20-day) and the line *"Direction of travel matters as much as
position."*

### S08 · Contradiction detection — `1:46.1 → 2:05.9`

**On screen** — supporting vs contradicting evidence cards side by side, then the
`contradiction_flag` code card with all three OR-branches highlighted, then the five reason chips.

### S09 · Stress testing — `2:05.9 → 2:23.6`

**Code card** `Cell B8 - bootstrap_stress_test` — beta, idiosyncratic split, the bootstrap draw,
the day-1 shock. **Then** four parameter cards: 3,000 simulations · 20 days · ×1.8 volatility ·
−8% day-1 shock.

### S10 · VaR and CVaR — `2:23.6 → 2:39.8`

**On screen** — a loss distribution with the worst 5% in red (shape **schematic**, stated in the
source line), then two definition cards (VaR = the threshold, CVaR = the severity), then ORCL's
real numbers: **−46.1%** VaR 95%, **−51.7%** CVaR 95%.

### S11 · Resilience score — `2:39.8 → 2:55.7`

**On screen** — the four weights (55 / 20 / 15 / 10 %) as rows, then the four bands
(fragile < 40 · watch 40–55 · resilient 55–70 · high_resilience > 70).

### S12 · Review queue — `2:55.7 → 3:07.9`

**On screen** — the queue table (Ticker · Company · Health · Resilience · Priority) with ORCL,
UNH, SPGI, EL, AMZN — all priority 9 — then **notebook figure 2** (lowest-resilience names), then
the strip *"Decision support — the analyst decides, not the system."*

### S13 · Honest diagnostic — `3:07.9 → 3:24.8`

**On screen** — two bars: flagged **21.9%** (n = 62,831) vs not flagged **19.1%** (n = 120,707),
rate of a large 5-day move. Then the amber card *"A real difference — but small. The flag fires on
about a third of all rows."* and the line **"This is a diagnostic, not a forecast."**

This scene exists so the film cannot be misread as a prediction claim. Do not cut it.

### S14 · Evolution and close — `3:24.8 → 3:48.9`

**On screen** — Phase 3 → Phase 4 → Phase 5 stack, the advisory card, then the end card:
`Dhrumil Shah` / `MYCROFT PHASE 5` / `Python · AI · Quantitative Analytics · Risk Analysis ·
Human-in-the-Loop AI` over the advisory line.

---

## Captions

Burned in, one line, white on near-black at y 1392. Cue times come from per-sentence measured
audio, character-proportional within a sentence — never a words-per-minute estimate.
0 overlaps · 0 single-word captions · longest wrapped line 29 characters.

## Which notebook cells to screen-record

| Scene | Cell / region |
|---|---|
| S04 | `load_data()` + `engineer_features()` |
| S05 | the `rank_specs` loop, `weights`, `thesis_health`, `thesis_state` |
| S07 | `health_change_5d/20d`, `prior_state_20d`, `state_deterioration` |
| S08 | `contradiction_flag` and `contradiction_reasons()` |
| S09 | `bootstrap_stress_test()` — beta, idio, bootstrap, shock |
| S10 | the `var95` / `cvar95` lines, plus the queue's VaR/CVaR columns |
| S11 | `resilience_score` and `resilience_band` |
| S12 | `review_priority`, `queue`, and the printed top-20 |
| S13 | the `evaluation` groupby and its printed table |

## Final checklist

| Requirement | Status |
|---|---|
| 9:16 vertical | ✅ |
| 2160 × 3840 (4K vertical) | ✅ rendered at `--scale=2`, not upscaled |
| 30 fps | ✅ |
| MP4 / H.264 | ✅ |
| Audio 48 kHz | ✅ AAC 48 kHz stereo |
| Synchronised captions throughout | ✅ burned in, cued from measured audio |
| Subtle background music, narration clear | ✅ ducked bed, −14 LUFS target |
| 2.5–4 minutes | ✅ 3:49 |
| Opening sentence exact | ✅ first spoken line, no hook before it |
| Mobile-safe margins | ✅ nothing essential outside x 76–1004 or y 199–1460 |
| Readable code on a phone | ✅ mono ≥ 17 px at 1080-logical width |
| No profitability / accuracy claims | ✅ audited; S13 states the limit explicitly |
| Advisory shown | ✅ S01 source line, S12 strip, S14 end card |
