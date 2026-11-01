# BUILD-LOG — *Safer By Not Looking.*

Ep. 15 · `satellite-collision-avoidance` · **the series finale**
Built 2026-10-31 with `brutalist.art`, Fellow Tier, **$0.00**.

---

## Delivered

| | 16:9 | 9:16 |
|---|---|---|
| `claude-for-astronomy_OmMali_30_10_2026.mp4` | 3840 × 2160 · 158.93 s · 3814 frames · 18.0 MB | — |
| `satellite-collision-avoidance-9x16.mp4` | — | 2160 × 3840 · 158.93 s · 3814 frames · 19.9 MB |

24 fps, h264 + AAC, −21.0 LUFS integrated, both cuts sharing one audio mix.
**2:38.9** — 21 s inside the 3:00 cap. Both masters live in this folder.
**Nothing was published.**

---

## The episode

Topic 15 is "AI predicting and preventing space debris collisions in
increasingly crowded orbits". The crowding is real. The episode goes after
the quantity every downstream model is trained to predict.

**The collision probability is not the chance two satellites hit. It is the
chance they hit *given your uncertainty*** — so past a certain point, knowing
less makes the number smaller. That is probability dilution, and the integral
producing it is entirely correct.

And the second half: **a score dominated by the 99.7 % of events where
nothing was ever going to happen will prefer the forecaster that is wrong on
the 0.3 % that matter.**

This is the right finale because it closes the series' loop. Fourteen
episodes asked *where did this answer come from*. This one finds a quantity
that answers, in part, *from you*.

---

## What was measured

`assets/gen_conj.py`, seed **1515**, asserts four claims and writes no plate
if any fails. The integral is the real one — Foster's short-encounter method
in its numerically stable form, over 120,000 simulated conjunctions.

| | |
|---|---|
| Pc peaks at **σ = 212.1 m** = d/√2, matching the analytic prediction to <0.05 % | 1.635e-3 |
| Crosses the 1e-4 threshold at σ = 1397.7 m — a **6.6×** inflation | |
| At σ = 5 km: Pc = **7.99e-6**, a **205×** fall | no action |
| max-Pc at that same σ | **1.635e-3** — act |
| Population above 1e-4 | 180 of 120,000 (**0.15 %**), against ESA's 30 in 15,321 (0.20 %) |

**The reversal**, on 40,000 held-out events:

| | all events | the 124 notified |
|---|---|---|
| assume nothing changes | 0.0609 | **1.275** |
| trained ridge | **0.0152** | 4.130 |

**4× better overall. 3× worse where it matters.**

---

## Gates

| Gate | Result |
|---|---|
| F — paperwork | PASS |
| L — beat lint | PASS |
| A — render-free pre-flight | PASS, 10/10 after 1 fix |
| W — WCAG + margins | PASS, 10/10 |
| B — layout, both aspects | PASS, 20/20 **first pass** |
| Visual pre-flight, 20 frames | **3 defects found and fixed** |
| P — human signature | PASS, signed 2026-10-30 |
| V — 16:9 master | 28 frames · 0 BLOCKER · 0 MAJOR *(after 1 fix)* |
| V — 9:16 master | 28 frames · 0 BLOCKER · 0 MAJOR *(after 1 fix)* |
| Frame reading, both cuts | clean |

**GATE T and GATE SHARPNESS were not run: they are not shipped in this
toolkit**, despite SKILL.md describing GATE T as "ALWAYS RUN". Ninth
consecutive episode recording this.

---

## The six things that caught me

### 1 · The measurement refused the central claim

The hypothesis was that persistence would beat the trained model. **It does
not — it is 4× worse overall.** What is true is sharper: the ranking
*reverses* between the aggregate score and the notified events.

The claim was rewritten to what was measured. The experiment was not touched.
Standing rule since Eps. 11 and 13.

### 2 · A plate was drawn showing something that does not exist

`shrink.png` was first drawn to show alerts *breaking late* — quiet until the
last message, then jumping. The population contains **zero** such events, and
not by accident: once the covariance shrinks below the miss distance, Pc
falls, so better tracking almost always makes an alert decay. Redrawn to show
the real structure.

### 3 · The first population was 41 % high-risk

Drawing the miss distance log-uniformly made close approaches absurdly
common. Conjunctions are screened inside a box and the number below distance
*d* grows like *d²*, so *d* is now drawn uniform in **area** — which gives
0.15 % above 1e-4 without tuning anything. The rarity is a consequence of the
geometry, not a parameter.

### 4 · Three defects the 20-frame pre-flight caught that every gate passed

- **B03** — the three terracotta marks the beat asks you to find were
  **invisible** among 1,532 at `scale(1.7)`. Raised to 2.8. No gate tests
  "can a human find this".
- **B06 portrait** — name and value sat **0.02 units** apart and read as one
  run-on block. `_swatch_row` now puts them on one line.
- **B08 portrait** — the panel label ended 0.06 units above the legend.

### 5 · GATE V failed B04, and the obvious fix made the picture lie

The geometry plate shaded the Gaussian as a continuous greyscale. It failed
low-contrast at **0.23** against a 0.30 floor, because the gate averages the
colour of every pixel more than INK_DELTA from the background and this plate
is mostly soft gradient sitting just above that line.

The density ratio across the three panels is 1 : 0.056 : 1e-4. Four orders of
magnitude cannot be shown as shade without wrecking one end:

| display gamma | gate | what it did to the picture |
|---|---|---|
| 0.25 | 0.23 FAIL | the honest version |
| 0.09 | 0.34 pass | panels 2 and 3 **almost equally dark** — read as "more uncertainty, more density", the exact opposite of dilution |
| 0.70 | 0.31 marginal | panels 2 and 3 fell **below** the ink threshold and vanished |

**A gate passing is not the frame being right.** The knob was the wrong
lever, so the plate was redrawn as **1/2/3σ covariance ellipses** — crisp ink
instead of soft gradient, the way conjunction geometry is actually drawn, and
it says the same thing: the ellipse grows while the hard-body disk does not.
In the third panel the 1σ ellipse is eight times wider than the frame, so
only the disk is drawn, and that emptiness is the point.

Two further contrast wins came from removing pale ink rather than adding
dark: ghost-grey outer rings → ink/soft at descending widths, and the three
per-panel borders deleted (the gaps already separate them). Final **0.336**,
margin +0.036.

### 6 · The 9:16 then failed on a beat the 16:9 passed

B09's 85 unlit team marks were ghost-grey — just above the ink threshold.
Landscape survived because its chip and pull-quote added dark text; **portrait
drops both**, so the same scene scored 0.26. Unlit marks moved to `soft`
(still a fill, so the palette rule is untouched): portrait 0.432, landscape
0.389.

Worth recording as a general lesson: **a contrast margin that depends on
elements portrait drops is not a margin.**

---

## Also recorded

**Two results measured and deliberately NOT claimed as fixes.** B10 says the
first out loud, because "the fix I tried did not work" is the honest shape of
that beat.

- Giving the model σ/d — where the conjunction sits on the dilution curve —
  moved the notified error by **−2.7 %**. Nothing. The problem was never the
  features.
- Reweighting the tail 300× improved the notified error **2.4×**, cost **15×**
  on the aggregate, and **still lost to "assume nothing changes" by 1.4×**.

**Seven scenes needed `RT_PORTRAIT`** — the chassis mechanism added in Ep. 14.
Every landscape right-hand column becomes stacked rows in portrait, so those
branches play fewer reveals and would have frozen on a held frame. After it,
all twenty clips land exactly **+0.18 s** under their beat in both aspects.

---

## Pipeline, in order

```
research → conj.py + gen_conj.py (asserts 4 claims) → beat_sheet.json
→ paperwork → GATES F L A W B (both aspects) → 20-frame visual pre-flight
→ GATE P (human) → Kokoro audio (the clock) → nat15 → pace15
→ natboth15 → RT_PORTRAIT → verify15 (both aspects)
→ 20 Manim renders at 4K, SEQUENTIALLY → Remotion bookends (foreground)
→ compile → GATE V --mp4 → fix B04 → recompile → GATE V
→ 9:16 via shorts.py --drop --no-endcard → GATE V --mp4 → fix B09
→ re-render both aspects → recompile both → GATE V both → read frames
→ paperwork → dated delivery name
```

**Pass `--mp4` explicitly to the frame check. Always.**

---

## Cost

**$0.00.** Kokoro `af_bella` locally; Manim and Remotion for picture; no image
model, no ElevenLabs, no API keys. Fellow Tier throughout.

---

## The series

Fifteen episodes, all Fellow Tier, all $0.00, all under three minutes.

| | | the limit it found |
|---|---|---|
| 01–06 | | AI inspecting observations |
| 07 | | standing in for a calculation |
| 08 | | a division of labour |
| 09 | | an output that was never a measurement |
| 10 | | a training set produced by past decisions |
| 11 | | an objective that omitted the failure |
| 12 | | an evaluation inflated by the split |
| 13 | | a positive class that does not exist |
| 14 | | labels that were a model's output |
| **15** | | **a target that is partly a property of the observer** |
