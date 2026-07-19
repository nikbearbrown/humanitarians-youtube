# SHOTLIST — vox-base-rate

**Why Your 0.68 Is Really a 0.40** · 16:9 · ~96s est. (11 beats)
Accents: dusty navy `#3D5A80` = true sponsor / genuine positive · crimson `#BF3339` = false positive · pale grey `#D8D2C4` = non-sponsor not flagged · gold `#F5D061` = editor's pen (once per graphic).
Source: chapter 5, the base-rate / confidence-illusion section + Fig 5.4. Companion to vox-comma-orphan (join half of the same chapter).
Card exclusions honored: **no Bayes formula / derivation** (the dot grid + sliding marker ARE the argument) · no calibration-curve discussion · no cost-asymmetry threshold · **medical framing one beat only (B05)** · no verb taxonomy.

Shot-type histogram: CARD 2 · STILL 1 · DOCUMENT 1 · GRAPHIC 4 · COMPOSITE 3 — max consecutive same-type: 2 (B04–B05). Lint: pass.
On-screen values are ONLY the three verified markers (0.08 / 0.68 / ~0.40) + the 8-in-100 base rate + the 99% / 1-in-10,000 medical ratio. No invented false-positive tally is stamped.

---

## B01 — CARD (title) · own · ~10.0s
Cue: "A verified score. Properly calibrated…"
Copy: **Why your 0.68 is really a 0.40** / sub: *the base rate the score forgot*

## B02 — STILL · ai · kenburns · ~9.0s  ← MEDIA SLOT (the only generated plate)
Cue: "Here's what your scorer returns… Zero point six-eight."
Slot: `media/B02.png`
t2i prompt: printed screenshot of a data tool result card reading 'Sponsorship probability: 0.68 — likely sponsor', clean sans-serif UI, pinned like a clipping to aged newsprint, desaturated flat print reproduction, editorial collage
Synthetic — disclosure line in credits. `shot.focus` toward the 0.68 after the plate lands.

## B03 — DOCUMENT · own · highlight · ~8.5s
Cue: "…how rare is a sponsor here in the first place?"
Quote card: **"How rare is it, before you look?"** — *— the question the score skips*. Gold sweep on "rare."

## B04 — GRAPHIC · own · manim (isotype) · ~10.5s
Cue: "…only eight companies in a hundred have ever sponsored."
Manim: `B04_BaseRateGrid` — 10×10 isotype grid counts up; 8 navy sponsors, 92 pale grey; label "8 sponsors in 100." The base rate. (8% — verbatim from ch.5.)

## B05 — GRAPHIC · own · manim · ~9.5s — the ONE medical beat
Cue: "…ninety-nine percent accurate, for a disease one in ten thousand…"
Manim: `B05_MedicalIntuition` — a tall crimson bar (~100 false positives) beside a single navy tick (~1 true), label "per 10,000 tested." Ratio, not arithmetic. Medical framing appears here and nowhere else (card exclusion).

## B06 — COMPOSITE · own · manim · ~9.0s
Cue: "A positive signal fires… lands on rare real sponsors and common non-sponsors alike."
Manim: `B06_SignalLands` — faint base-rate grid; a signal ring sweeps; the few navy sponsors light, many grey squares flip crimson. No exact FP count.

## B07 — GRAPHIC · own · manim (isotype) · ~9.0s — the swamp
Cue: "…false positives pile up — swamping the handful of real ones."
Manim: `B07_Swamp` — flagged squares gather into a pile; a few navy at the base, crimson accumulating until navy is nearly buried. Accumulate move.

## B08 — COMPOSITE · own · manim · ~10.5s — the slide
Cue: "…the base rate drags it down, and the marker slides toward forty."
Manim: `B08_MarkerSlides` — 0→1 probability axis; grey tick at 0.08 ("base rate") tugs left; navy marker slides 0.68 → ~0.40; crimson HandRing lands on 0.40 on "forty." Three verified markers only.

## B09 — GRAPHIC · own · manim · ~9.0s
Cue: "0.68 is the signal's strength. 0.40 is what it's worth once the rarity is counted."
Manim: `B09_SignalVsWorth` — big **0.68** under navy "signal strength" vs big **0.40** under crimson "what it's worth"; arrow "count the base rate." No formula.

## B10 — COMPOSITE · own · manim · ~9.5s
Cue: "…a lead worth checking, not a promise."
Manim: `B10_LeadNotVerdict` — company card; navy "ask directly" arrow leads on; faded "apply blindly" arrow struck in crimson; label "a lead, not a verdict." No cost-ratio math.

## B11 — CARD (endcard) · own · ~8.0s
Cue: "A strong signal for a rare thing is still a long shot."
Copy: **A strong signal for a rare thing is still a long shot.** / sub: *from The Reallocation Engine — chapter 5*

---

## Slot inventory (fill later, any order; rerun vox_run after each drop)

| Slot | Need | From |
|---|---|---|
| `media/B02.png` | "Sponsorship probability: 0.68" scorer readout clipping | t2i prompt above (ai — disclosure) |

Everything else is CARD / DOCUMENT / GRAPHIC / COMPOSITE-manim — no media generation needed for the slate cut.
