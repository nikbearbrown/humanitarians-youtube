# CHECKS-REPORT — Ep. 17, *scheduling-the-night*

Ep. 17 · `scheduling-the-night` · pre-audio gate run, 2026-11-13

Gates F, L, A, W and B all run **before** GATE P, because they are free and
because a human should not be asked to sign a beat sheet whose scenes do not
yet lay out.

| gate | scope | result |
|---|---|---|
| **F** paperwork | 9 files | **complete** |
| **L** beat lint | `beat_sheet.json` | **clean** |
| **A** render-free pre-flight | 10 scenes | **10/10 clean** |
| **W** contrast + margins | 10 scenes | **10/10 clean** |
| **B** pixel layout | 10 scenes × 2 aspects, `--curve-strict` | **20/20 clean** (after 2 fixes) |
| **frames read** | 10 scenes × 2 aspects, by eye | **4 defects found that no gate could catch** |
| **P** human signature | `PEDAGOGY.md` | **AWAITING — nothing downstream has run** |

> **GATE T and GATE SHARPNESS are not shipped in this toolkit**, despite
> `ai-explainer/SKILL.md` describing GATE T as "ALWAYS RUN". There is no such
> script under `runtime/qc/`. Recorded here rather than silently skipped.

---

## GATE F — paperwork

| File | Status |
|---|---|
| `SOURCES.md` | present — verbatim ZTF and Rubin quotes; the checked **negative** result on "reinforcement/ML/neural"; an explicit "what is MINE, not theirs" |
| `FACTCHECK.md` | present — 15 entries, PUBLISHED vs COMPUTED vs MINE, the known solver jitter, and the `ideas.md` correction |
| `SHOTLIST.md` | present — 14 beats, lanes, the colour contract, aspect discipline |
| `PROMPTS.md` | present — records that **no image-generation prompts were used**; all seeds and parameters |
| `PEDAGOGY.md` | present — **awaiting signature** |
| `beat_sheet.json` | 14 beats, 430 words |
| `assets/sched.py`, `assets/gen_sched.py` | the night, the two schedulers, the plates |
| `scenes.py` | 10 aspect-aware scenes |
| `assets/plots/*.png` | 5 plates, all 1560×780 |

## GATE L — beat lint

```
[beat-lint] clean — beat mix OK (beat_sheet.json)
```

14 beats: 4 Remotion (B00, B11, B12, B13) + 10 Manim (B01–B10).

## GATE A — render-free pre-flight

10/10 clean, first pass, untouched.

## GATE W — contrast and margins

10/10 clean, first pass. `#B9B4A0` ghost appears only as strokes and fills —
never as text — and accented text is `#A44A32` throughout.

## GATE B — pixel layout, BOTH aspects, `--curve-strict`

First pass: **18/20**. Two errors, both genuine collisions:

| scene | aspect | error |
|---|---|---|
| `B10_TheTell` | landscape | `greedy 90.5/h` and `planner 90.0/h` chips straddled the plate's top frame at y 1.97 |
| `B05_RubinsMove` | portrait | `x weights` label sat on the third basis-map square |

**B10** — the plate dropped from `py 0.42` to `py 0.10` rather than raising
the chips: at the clearance the chips needed, the next thing above them is the
hairline at 2.66.
**B05** — in portrait the three maps are nearly frame-wide, so a label beside
them has nowhere to go. It moved beneath the row.

After both fixes: **20/20 clean.** Re-verified after every subsequent edit —
B03, B04, B05, B06, B07, B08 and B10 were each re-run through A, W and B.

### What GATE B structurally cannot check here

A plate's **image** is invisible to it; only the plate's **frame** is a curve.
So a label crossing a plate's outline is caught, and a label sitting *inside*
a plate — or hidden *underneath* one — never is. Both of the worst defects in
this episode were exactly that shape.

---

## Reading the frames — 4 defects every gate passed

All ten scenes were rendered to stills in both aspects and tiled into contact
sheets. This is where the real defects were.

### 1 · B06 landscape — a label rendered *behind* the plate

`16 BLOCKS, one filter each` sat at y 1.59. The plate at `pw 6.60, py 0.06`
has its top edge at y 1.71, and is drawn afterwards and opaque — so the label
was painted over and **completely invisible**. GATE B saw no collision
because nothing crossed the plate's *outline*; the label was wholly inside it.

Fixed by narrowing the plate to `pw 5.60` and dropping it to `py -0.16`,
which opens 0.24 units of clear space. `DIAL_X` moved to 1.344 to track the
narrower plate.

### 2 · B08 — the started-counts read as touching the plate frame

`401 STARTED` / `360 STARTED` spanned y 1.54–1.74 against a plate top edge at
1.55 — an overlap of 0.01, under GATE B's tolerance but plainly contact at
4K. Plate narrowed to `pw 5.80`, label row raised to `ytop 2.10`.

### 3 · B04 — "atoms in" rendered as "atomsin"

EB Garamond at 20 pt closes the space in that specific word pair. Not a
geometry error and nothing measures it. Reworded to *"the whole observable
universe holds 10⁸⁰ atoms"*, which never forms the pair.

### 4 · B03 — a legend that keyed nothing

Two of the three swatch rows carried colour chips next to text that described
**axes**, not colours — implying a colour code that did not exist. Re-keyed so
all three swatches name something actually in the plate: the field tracks, the
three highlighted fields, the shaded no-point band.

### Also corrected in portrait

- **B05** — `COVERAGE OWED` had to be scaled by `_fit()` to fit the portrait
  cell and rendered visibly smaller than `SLEW` and `DEPTH` beside it, which
  reads as a mistake. Portrait now uses the short word `COVERAGE`.
- **B07** — `= ONE REQUEST` landed on the card's top edge. The chips and card
  were re-spaced (gy 2.20, card cy −0.20).

### Verified NOT a defect

`10^2567` renders as a true typographic superscript with **no stray caret
glyph** — checked by cropping the 1920×1080 still at full resolution, because
this is precisely the Ep. 09 failure mode (a character outside the font's
coverage rendering as stray digits).

---

## One engineering defect fixed upstream of all of this

`_tsp_order()` re-walked the entire tour to score **every** candidate 2-opt
swap, giving O(passes × m³) scalar `slew_time` calls — roughly 43 million per
planner run. A convergence probe ran **7 h 38 m** before being killed, and
produced no visible output at all because it had been piped through `tail`,
which buffers until the process exits.

Rewritten to precompute the symmetric slew matrix once and score each swap by
the two edges it actually changes. `run_planner` went from hours to seconds.
The rewrite is faithful: at the same budget the plan is identical and only the
executed median airmass moved, 1.288 → 1.281.

**Lesson recorded:** never pipe a long background probe through `tail` — a
buffered pipe makes a wedged process indistinguishable from a working one.

---

## Post-GATE-P — what ran after the signature

GATE P was signed (Om Mali, 11/13/2026) and the rest of the pipeline ran.

| step | result |
|---|---|
| audio, Kokoro `af_bella` | 14 MP3s, **159.49 s** measured, $0.00 |
| pacing solve | RT/HOLD written per scene; **no `RT_PORTRAIT` needed** — `nat17.py` measured identical reveal counts in both aspects, unlike Ep. 16's six mismatches |
| GATE A re-run | 10/10 clean |
| GATE B re-run, `--curve-strict` | **20/20** clean, both aspects, after the `_swatch_row` fix |
| 4K render | 20 clips; every one lands 0.19–0.22 s under its beat |
| compile | 14/14 slots filled in both cuts, no slates |
| **frames read** | **5 defect classes found, none of which any gate caught** |
| GATE V | **exits 2 on both masters.** 0 BLOCKER; the MAJORs are characterised with measurements |

Full account in `VISUAL-QC.md`. In brief, reading frames caught:

1. **B11/B13 Remotion props that no schema defines** — zod drops unknown keys
   silently, so B11 was about to render a stranger's default verdict card.
2. **B03's third legend row welded to its swatch and scaled smaller** — a
   latent zero-gap bug in `_swatch_row` that only the reel's longest label
   exposes.
3. **B11 portrait's title truncated** to `… - one p…` while landscape was clean.
4. **`@NikBearBrown` in the composer chrome** of B00 and B12, both aspects —
   `folderLabel` was never set, so the component default rendered.
5. **B01's lower half empty for 4.6 s of an 8.4 s beat** — its chrome was
   revealed in the last play instead of the first.

### Where GATE V's own verdict is wrong

Its `low-contrast` check averages **every** non-background pixel into one ink
colour. This episode's plates are pale line-art on cream, so 61–78% of that
mean is plate. Measured properly, the type runs **5.7:1 to 7.9:1** WCAG against
the page. The two portrait `underfill` flags are an aspect mismatch: the 916
verdict card reserves platform-UI bands by design and the gate measures a
16:9-derived safe area.

Recorded, not suppressed. Nothing was run with `--lenient`.
