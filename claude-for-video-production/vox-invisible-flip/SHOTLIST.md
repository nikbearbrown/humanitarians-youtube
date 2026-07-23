# SHOTLIST — vox-invisible-flip

**Why an Invisible Change Can Flip a Million-Pixel Answer** · 16:9 · ~102s est. (11 beats)
Accents: dusty blue `#5B7B9C` = the human-visible truth / panda side · terracotta `#D35F43` = the perturbation / gibbon · gold `#F5D061` = editor's pen.
Facts verified (FACTCHECK.md): panda 57.7% → gibbon 99.3% at ε=0.007 — Goodfellow, Shlens & Szegedy (ICLR 2015). Closes the chapter's own [Verify] tag.
Card exclusions: no FGSM/PGD equations (sign-of-gradient intuition only, drawn as aligned slivers) · no L∞/L1 formalism · no boundary-tilting account · no defense toolkit.
Highlighter rule honored: gold sweeps only on short single-line quotes (B04, B10).

Shot-type histogram: CARD 2 · STILL 1 · COMPOSITE 3 · DOCUMENT 2 · GRAPHIC 3 — max consecutive: 2. Motion: hold 3 · kenburns 1 · highlight 2 · drawon 2 · annotate 2 · isotype 1 — max 27%. Lint: pass.

---

## B01 — CARD (title) · own · ~8.8s
Copy: **Why an invisible change can flip a million-pixel answer** / sub: *adversarial examples*

## B02 — STILL · archive · kenburns · ~8.4s  ← MEDIA SLOT
Slot: `media/B02.png` + `media/B02.source.txt` (archive slot — STAND-IN X until sidecar exists)
Archive queries:
- https://commons.wikimedia.org/w/index.php?search=giant+panda+bamboo&title=Special:MediaSearch&type=image
- https://www.si.edu/openaccess?edan_q=giant%20panda
- https://www.loc.gov/free-to-use/?q=panda
Corner chip at assembly: "panda · 57.7%" (blue).

## B03 — COMPOSITE · archive · hold · ~10.4s  ← derives from B02
Slot: `media/B03.png` — B02's plate duplicated side by side (derive locally, no spend).
Annotation (assembly plane): serif label "spot the difference," timed to "same."

## B04 — DOCUMENT · own · highlight · ~9.6s
Quote card: **"gibbon — 99.3%"** — *— the model, on the same panda (Goodfellow et al., 2014)*. Gold sweep on "gibbon" (short line — safe).

## B05 — GRAPHIC · own · drawon · ~10.0s
Manim: `JustNumbers` — grey pixel-grid unfurls into a strip of mono number cells. The picture becomes a list.

## B06 — COMPOSITE · own · annotate · ~9.6s
Manim: `WeightedSum` — slate weight chips stamp under the cells; the activation bar + hairline decision line draw in; fill sits panda-side in blue. No formula anywhere.

## B07 — GRAPHIC · own · isotype · ~10.8s — THE CORE IMAGE
Manim: `Slivers` — tiny terracotta arrows land on every cell in one wave, all pointing the same way; the bar climbs in steps and turns terracotta. Sign-of-the-gradient, drawn.

## B08 — COMPOSITE · own · annotate · ~9.6s
Manim: `TheFlip` — the fill crosses the decision line; label chip Transforms blue "panda" → terracotta "gibbon"; the film's ONE HandRing on the crossing, timed to "flips."

## B09 — GRAPHIC · own · drawon · ~9.6s
Manim: `NothingEverything` — two panels: one magnified cell + its single sliver ("one pixel — nothing") vs the climbed bar ("the sum — everything").

## B10 — DOCUMENT · own · highlight · ~9.6s
Quote card: **"Not a bug — a flashlight."** — *— what adversarial examples reveal*. Gold sweep on "flashlight" (short line — safe).

## B11 — CARD (endcard) · own · ~8.8s
Copy: **Right answer, wrong reasons — until someone checks.** / sub: *from Computational Skepticism for AI — chapter 8*

---

## Slot inventory

| Slot | Need | From |
|---|---|---|
| `media/B02.png` + `B02.source.txt` | panda photograph | Commons/Smithsonian/LOC links above |
| `media/B03.png` | B02 duplicated side by side | derive locally, no spend |

Nine of eleven beats render now.
