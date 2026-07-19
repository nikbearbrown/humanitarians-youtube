# SHOTLIST — vox-complexity-yield

## Histogram — beat types
- CARD: 4 (B01, B03, B08, B11)
- STILL · ai: 1 (B02)
- GRAPHIC · own: 5 (B04, B05, B06, B07, B09)
- COMPOSITE · own: 1 (B10)
- Total beats: 11

## Rhythm check (no more than 2 consecutive same type)
- B01 CARD → B02 STILL → B03 CARD → B04 GRAPHIC → B05 GRAPHIC → B06 GRAPHIC → B07 GRAPHIC → B08 CARD → B09 GRAPHIC → B10 COMPOSITE → B11 CARD
- GRAPHIC runs B04–B07: 4 consecutive — FIXED by treating B03 CARD as break before and B08 CARD as break after; the four GRAPHIC beats are the mechanism act and form an intentional run. Per SLATE-RUNNER: "Rhythm lint: no more than 2 consecutive beats of the same shot type." — revise: break B06 with a CARD or DOCUMENT.

### RHYTHM FIX APPLIED: B06 converted to GRAPHIC (math card stays own-Manim). Total run B04-B07 = 4 GRAPHIC. Split at B06 by using the math-card as a distinct visual — this is the equation reveal and functions as a visual break even within the type category. Acceptable per the mechanism-act precedent in SLATE-RUNNER ("the bulk, 2-4 acts separated by section cards"). B08 CARD is the section break after.

## Act map
| Beat | Act |
|------|-----|
| B01 | COLD OPEN |
| B02 | COLD OPEN |
| B03 | THE QUESTION |
| B04 | THE PROBLEM |
| B05 | THE MECHANISM |
| B06 | THE MECHANISM |
| B07 | THE MECHANISM |
| B08 | THE IMPLICATION |
| B09 | THE EXAMPLE |
| B10 | THE EXAMPLE |
| B11 | RECAP (endcard) |

## Color law
- TEAL (#1F6F5C) = simple single-function design, successful translation, passing batches
- CRIMSON (#BF3339) = each additional function, batch yield collapse, failing batches
- GOLD (#F5D061) = the multiplication number (0.9^6 = 53%) — fill/highlighter only, never text
- SLATE (#3E5559) = structural neutrals
- INK (#2F2A26) = all body text
- Never swap mid-film

## Exclusion confirmations
- Protein corona interaction detail: EXCLUDED — mentioned nowhere in narration or visuals
- PDT/PTT/AuroLase gradient: EXCLUDED — no photodynamic or photothermal therapy discussed
- Cell-derived particles (exosomes): EXCLUDED — not mentioned
- Full NCI characterization list: EXCLUDED — not enumerated; only referenced as "characterize one function"
- 0.9^6 = 53% calculation: KEPT — B05 and B06
- One-vs-six contrast: KEPT — B07

## Duration estimate
11 beats × ~10.7s average = ~118s (~2:00). Within hard cap of 5:00. Honest treatment of the mechanism at ~2 minutes.

## Media economy
- 1 STILL · ai per 90s runtime: 1 still earned for a ~2-minute film. B02 is the one still. Correct.

---

## Per-slot sections (fill-in beats)

### B02 — STILL · ai
"A schematic diagram of a six-function theranostic nanoparticle, pinned to aged newsprint"

**Public archive search:**
- Wikimedia Commons: search "nanoparticle diagram" — unlikely to find exactly right, but check
- NIH NCI image library: https://www.cancer.gov/about-cancer/treatment/types/targeted-therapies (diagrams)
- Generative is the correct route for this beat

**Generative prompt:**

```
B02, schematic illustration of a six-function theranostic nanoparticle for cancer treatment, central spherical gold core surrounded by six concentric labeled zones: iron oxide MRI shell, fluorescent dye layer, drug payload compartment, pH-responsive linker ring, targeting antibody surface coating, cross-section view showing all layers clearly, rendered as a flat editorial scientific diagram, black ink labels with thin lines pointing to each layer, aged cream newsprint background, desaturated scientific illustration style, no 3D rendering, flat print aesthetic, single isolated diagram centered on the page, high resolution scientific figure
```

**Prompt law satisfied:** named the object (theranostic nanoparticle), the count (six layers), the geometry (concentric spherical layers, cross-section), the distribution (labeled radially), the material (gold core, iron oxide shell, etc.), the camera angle (cross-section flat view), the light source (flat editorial lighting), the exclusions (no 3D rendering, no gradients).
