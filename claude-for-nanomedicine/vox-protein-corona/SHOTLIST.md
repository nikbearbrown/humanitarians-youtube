# SHOTLIST — vox-protein-corona

**The Instant a Nanoparticle Hits Blood, It Vanishes Under a Coat of Protein** · 16:9 · ~107s est. (11 beats)
Accents: teal `#1F6F5C` = engineered particle surface / targeting ligands · crimson `#BF3339` = protein corona / masking / liver clearance · gold `#F5D061` = the moment of corona formation (editor's pen, once per graphic).
Source: cancer-nanomedicine/chapters/04-targeting-epr-protein-corona-and-active-ligands.md — protein corona masking mechanism only.

Card exclusions honored: no passive vs active targeting mechanics · no EPR debate · no engineer-the-corona angle · no patient-to-patient variability. One STILL ai: proteins swarm the particle.

---

## Shot-type histogram

CARD 4 · STILL 1 · GRAPHIC 5 · COMPOSITE 1 — max consecutive same-type: 2 (B05–B06). Rhythm lint: pass.

## Act map

| Act | Beats |
|---|---|
| COLD OPEN | B01 |
| THE QUESTION | B02 |
| THE PROBLEM | B03–B04 |
| THE MECHANISM | B05–B06 |
| THE IMPLICATION | B07–B08 |
| THE EXAMPLE | B09 |
| RECAP / OUTRO | B10–B11 |

## Color law

TEAL = the engineered thing (ligands, the particle's designed surface) — the value being lost.
CRIMSON = the corona, the masking, the clearance — the obstacle.
GOLD = one-time editor's-pen highlight; fill only, never text color.
Never swapped mid-film.

## Exclusion confirmations

- EPR debate: not mentioned, zero appearances.
- Passive vs active targeting mechanics (own video): not introduced.
- Engineer-the-corona-as-feature: not mentioned.
- Patient-to-patient corona variability: excluded.
- No equations (none in chapter for this mechanism).

---

## B01 — CARD (title) · own · hold · ~7.5s

Cue: "You spend months engineering a nanoparticle's surface…"
Copy: **The Instant a Nanoparticle Hits Blood, It Vanishes Under a Coat of Protein** / sub: *why targeting that works in culture fails in blood*
Topic eyebrow: CANCER NANOMEDICINE

---

## B02 — CARD (question) · own · hold · ~9.0s

Cue: "A nanoparticle is decorated with targeting antibodies…"
Gap formula on screen: **The antibodies are still attached. Why does the particle end up in the liver?**
No verdict, no answer yet.

---

## B03 — STILL · ai · kenburns · ~9.5s  ← MEDIA SLOT (the one generated plate)

Cue: "The moment a nanoparticle enters blood, plasma proteins begin adsorbing…"
Slot: `media/B03.png`
Shot focus: centered on the teal particle with crimson proteins swarming; push-in during kenburns.

### B03 — Generative prompt

```
B03, editorial scientific diagram of a single spherical nanoparticle (teal-colored, 80nm diameter, clean engineered surface with small protruding antibody shapes) being surrounded by plasma proteins in blood — large oval albumin molecules, Y-shaped immunoglobulin antibodies, elongated fibrinogen — adsorbing onto and covering the particle surface, proteins shown in crimson and dark red tones, flat schematic illustration pinned to aged cream newsprint, desaturated editorial style, no gradients no glow, direct overhead view, proteins accumulating densely on the lower two-thirds of the particle, upper third still teal-exposed, scientific diagram aesthetic, Okabe-Ito colorblind-safe palette
```

Synthetic/AI — disclosure line in credits. `shot.focus` toward the particle center.

---

## B04 — GRAPHIC · own · manim · accumulate · ~11.0s

Cue: "This coating is called the protein corona…"
Manim: `B04_CoronaForms` — teal Circle particle with teal Dot ligands on perimeter; crimson protein Dots appear one by one (AnimationGroup lag_ratio) and pile on until ligands are buried; gold label "protein corona forms within seconds". The core visual.

---

## B05 — GRAPHIC · own · manim · drawon · ~10.0s

Cue: "First consequence: the corona physically masks targeting ligands…"
Manim: `B05_LigandMasked` — particle with extended teal ligand arm; crimson rectangle slides over the ligand; cell-surface receptor sits unreachable; annotation "ligand masked — cannot bind".

---

## B06 — GRAPHIC · own · manim · drawon · ~10.0s

Cue: "Second consequence: certain proteins in the corona are recognition signals…"
Manim: `B06_OpsominClearance` — fully-coated crimson particle; LabelChip "OPSONIN" on corona; crimson arrow points toward liver shape; serif label "flagged for clearance".

---

## B07 — GRAPHIC · own · manim · drawon · ~9.0s

Cue: "This is why culture medium and blood are not the same experimental environment…"
Manim: `B07_TwoEnvironments` — two panels left/right divided by a gold vertical line: left "CULTURE MEDIUM" shows clean teal particle with ligand binding a receptor; right "BLOOD" shows same particle coated crimson, ligand buried, arrow to liver. The environmental contrast.

---

## B08 — CARD (section) · own · hold · ~9.5s

Cue: "Any targeting strategy validated only in protein-free culture is incomplete…"
Copy: **Testing in culture medium is not testing in blood.** / sub: *the corona is not optional — it is the experimental condition*

---

## B09 — GRAPHIC · own · manim · drawon · ~11.0s

Cue: "Consider a specific case. A folate-targeted nanoparticle…"
Manim: `B09_FolateExample` — two-column bar chart: "IN CULTURE" teal bar 87%; "IN BLOOD" two bars — crimson 72% liver, teal 3% tumor; serif label "illustrative numbers" beneath both columns; annotation "ligands buried" with crimson arrow pointing to the blood column.

---

## B10 — COMPOSITE · own · manim · annotate · ~11.0s

Cue: "The protein corona is why targeting that works in a dish fails in a body…"
Manim: `B10_CoronaSummary` — the fully-coated particle end-state; a HandRing lands around the crimson corona layer; two SerifLabels: "targeting ligands — buried" (teal underline) and "protein corona — seconds" (crimson underline). One ring only.

---

## B11 — CARD (endcard) · own · hold · ~9.5s

Cue: "The corona forms. The ligand is buried…"
Copy: **The protein corona buries the targeting ligand. The body sees the corona, not the particle you designed.** / sub: CANCER NANOMEDICINE

---

## Slot inventory (fill later; rerun vox_run after each drop)

| Slot | Need | From |
|---|---|---|
| `media/B03.png` | nanoparticle surrounded by plasma proteins swarming | generative prompt above (ai — disclosure) |

Everything else is CARD / GRAPHIC / COMPOSITE-manim — no media generation needed for the slate cut.
