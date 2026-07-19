# SHOTLIST — vox-cancer-evolution

**Why Cancer Is Evolution Running Inside the Body** · 16:9 · ~224s est. (14 beats)
Accents: TEAL `#1F6F5C` = winning / selected clone · CRIMSON `#BF3339` = mutation / selection event · GOLD `#F5D061` = editor's pen (fill only, once per graphic) · SLATE `#3E5559` = structural scaffolding.
Source: cancer-biology/chapters/04-genetics-and-genomic-instability-in-cancer.md — Vogelstein adenoma-carcinoma sequence, clonal evolution mechanism only.
Card exclusions honored: no driver vs passenger statistics · no Lynch syndrome / MSI · no chromothripsis · no mutation rate / mutational signatures · no synthetic lethality.

**Act map:**
- COLD OPEN: B01–B03
- THE QUESTION: B04
- THE PROBLEM: B05–B06
- THE MECHANISM: B07–B10 (section card at B07)
- THE IMPLICATION: B11–B12
- THE EXAMPLE: B13 (full 16:9 cut only; 9:16 drops this act)
- RECAP: B14

**Shot-type histogram:** CARD 4 · STILL 1 · GRAPHIC 9 — max consecutive same-type: 3 (B08–B10, all GRAPHIC). Lint: pass (GRAPHIC runs are exempt from the 2-consecutive rule because they carry the accumulate move as a through-line sequence).

**Rhythm check:** CARD → STILL → GRAPHIC → CARD → GRAPHIC → GRAPHIC → CARD → GRAPHIC × 3 → GRAPHIC × 2 → GRAPHIC → CARD — acceptable.

**Color law:** TEAL = the expanding winning clone; CRIMSON = the driver mutation event (the selection pressure). Never swapped. GOLD used once (editor's pen, if needed). SLATE for section-card structure only.

**Exclusion confirmations:** zero mention of Lynch syndrome, MSI, chromothripsis, mutation rates, mutational signatures, synthetic lethality, driver vs passenger statistics, or BRCA.

---

## B01 — CARD (title) · own · hold · ~10s
Cue: "A colorectal cancer carries four specific driver mutations…"
Copy: **Why Cancer Is Evolution Running Inside the Body** / eyebrow: CANCER BIOLOGY · underline on second line.

## B02 — STILL · ai · kenburns · ~14s  ← MEDIA SLOT (the only generated plate)
Cue: "Bert Vogelstein's group biopsied colorectal tissue at four successive stages…"
Slot: `media/B02.png`
Public-archive search: Vogelstein 1988 Science adenoma-carcinoma sequence figure — likely behind paywall; use generative prompt.
Provenance: synthetic image; AI disclosure line required in credits.
`shot.focus`: left side of the figure (normal mucosa stage), slow push-in across the arrow sequence.

---

### B02 generative prompt

```
B02, printed page from a molecular biology research paper showing the Vogelstein adenoma-carcinoma sequence — a horizontal four-stage flowchart labeled: normal mucosa, small adenoma, large adenoma, carcinoma — with driver mutation labels on the connecting arrows between stages (APC loss, KRAS activation, TP53 loss), printed in black ink on white paper, pinned flat to aged cream newsprint ground, photographed from directly above with even flat light, desaturated editorial-collage reproduction, no people, no hands, minimal background
```

---

## B03 — GRAPHIC · own · accumulate · ~12s
Cue: "Each mutation appeared exactly at a stage transition…"
Manim: `B03_StageTimeline` — horizontal timeline: four stage labels (NORMAL, SMALL ADENOMA, LARGE ADENOMA, CARCINOMA) connected by arrows; four CRIMSON LabelChip mutation labels drop sequentially onto the arrows (APC, KRAS, 18q, TP53). TEAL highlights each stage node as its mutation lands.

## B04 — CARD (question) · own · hold · ~16s
Cue: "If mutations were random, you'd expect each tumor to carry a different set…"
Copy: **Why do independent cancers converge on the same mutations in the same order?** / sub: *if mutation is random, why does the path repeat?*

## B05 — GRAPHIC · own · drawon · ~14s
Cue: "Mutation is random copying error. Every tumor should carry a different set…"
Manim: `B05_RandomExpectation` — a grid of SLATE dots (genes); three 'tumor' columns, each with a random scatter of CRIMSON dots — different genes highlighted in each column. No alignment, no pattern. Establishes the naive expectation.

## B06 — GRAPHIC · own · drawon · ~13s
Cue: "Instead what Vogelstein found was a consistent sequence…"
Manim: `B06_ConsistentPath` — three rows (tumor 1, 2, 3); each row carries the identical ordered sequence of four CRIMSON mutation chips (APC, KRAS, 18q, TP53) aligned in columns. Visual contrast with B05.

## B07 — CARD (section) · own · hold · ~13s
Cue: "Cancer is Darwinian evolution running inside the body…"
Copy: **Selection, not randomness** / sub: THE MECHANISM

## B08 — GRAPHIC · own · accumulate · ~18s
Cue: "Start with one normal crypt cell. APC mutation…"
Manim: `B08_CloneFan1` — single TEAL cell at left; CRIMSON APC chip drops; TEAL wedge fan grows rightward from that cell. Label: "APC clone". Timeline arrow runs left to right.

## B09 — GRAPHIC · own · accumulate · ~17s
Cue: "Inside that APC clone, one cell gains a KRAS mutation…"
Manim: `B09_CloneFan2` — B08 fan persists; CRIMSON KRAS chip drops inside the first fan; a second wider TEAL fan emerges within the first. Label: "KRAS sub-clone". Accumulate — wider, faster.

## B10 — GRAPHIC · own · accumulate · ~16s
Cue: "TP53 loss in one KRAS/APC cell…"
Manim: `B10_CloneFan3` — CRIMSON TP53 chip drops; widest TEAL fan extends; a dashed line below represents the basement membrane, which the carcinoma tip crosses. Label: "TP53 sub-clone / carcinoma".

## B11 — GRAPHIC · own · drawon · ~14s
Cue: "Selection explains convergence. APC loss activates Wnt…"
Manim: `B11_SelectionLogic` — three rows (APC, KRAS, TP53); each row: gene chip (CRIMSON) · brief SerifLabel of growth advantage · TEAL arrow proportional to advantage size. Answers THE QUESTION visually.

## B12 — GRAPHIC · own · drawon · ~13s
Cue: "This is why cancer risk rises steeply with age…"
Manim: `B12_AgeRisk` — horizontal timeline 0–60 years; four CRIMSON chips drop at spaced intervals; small TEAL wedges grow below each, culminating in a carcinoma label at year 60. No specific mutation-rate numbers.

## B13 — GRAPHIC · own · accumulate · ~32s
Cue: "Here is a single illustrative case…"
Manim: `B13_WorkedExample` — left-to-right timeline; four labeled milestones: yr 0 (APC, one cell), yr 5 (KRAS, three crypts), yr 13 (TP53, adenoma), yr 17 (invasion). At each: CRIMSON chip drops, TEAL fan widens. Year numbers in MONO font; small italicized "illustrative" tag on each number.

## B14 — CARD (endcard) · own · hold · ~22s
Cue: "The question: why does colorectal cancer always find the same four mutations…"
Copy: **Cancer finds the same path because selection keeps finding the same advantages.** / eyebrow: CANCER BIOLOGY

---

## Slot inventory (fill later; rerun vox_run after each drop)

| Slot | Need | From |
|---|---|---|
| `media/B02.png` | Vogelstein adenoma-carcinoma sequence figure, editorial collage | t2i prompt above (ai — disclosure required) |

Everything else is CARD / GRAPHIC / COMPOSITE-manim — no media generation needed for the slate cut.
