# SHOTLIST — vox-panda-proxy

**Title:** The Model Isn't Broken — It's Honest About What It Learned
**Total beats:** 13 | **Est. duration:** ~3:22 | **Slug:** vox-panda-proxy

---

## Rhythm check

13 beats | ~202s ≈ 3:22 | under 5:00 cap ✓
CARD · GRAPHIC · CARD · GRAPHIC · GRAPHIC · STILL · GRAPHIC · DOCUMENT · GRAPHIC · DOCUMENT · GRAPHIC · GRAPHIC · CARD
Max run: 2 consecutive same type ✓

## Act map

| Beat | Act | Type | Source | Motion | Notes |
|------|-----|------|--------|--------|-------|
| B01 | COLD OPEN | CARD | own | title | "COMPUTATIONAL SKEPTICISM" eyebrow; B01_Title |
| B02 | COLD OPEN | GRAPHIC | own | split | Panda → gibbon: 94% → 99.3% after invisible perturbation |
| B03 | THE QUESTION | CARD | own | question | On screen + in narration ✓ |
| B04 | THE PROBLEM | GRAPHIC | own | compare | Two reactions: brittle (wrong) vs. proxy-learner (right) |
| B05 | THE PROBLEM | GRAPHIC | own | split | Shape channel vs. texture channel — perturbation moved texture only |
| B06 | THE MECHANISM | STILL | ai | kenburns | Pixel noise / static — hidden structure |
| B07 | THE MECHANISM | GRAPHIC | own | trace | Proxy feature: correlated on training, flies apart under perturbation |
| B08 | THE MECHANISM | DOCUMENT | own | highlight | Quote: "statistical signature of pixel arrangements" |
| B09 | THE IMPLICATION | GRAPHIC | own | compare | Wrong diagnosis: patch / harden. Right: interrogate representation |
| B10 | THE IMPLICATION | DOCUMENT | own | highlight | Quote: "not bugs, they are features" |
| B11 | THE IMPLICATION | GRAPHIC | own | trace | 94% accuracy ≠ robust ≠ learned intended features |
| B12 | THE EXAMPLE | GRAPHIC | own | accumulate | Skin lesion: ruler = cancer proxy; 92% → 62% without rulers |
| B13 | RECAP | CARD | own | endcard | "The panda never moved. What the model was looking at did." |

---

## Color semantics
- TEAL = correct diagnosis / proxy-learner framing / representation interrogation
- CRIMSON = wrong diagnosis / fragile framing / patching
- SLATE = the panda / shape channel / what humans see
- GOLD = the flip moment / adversarial perturbation / the reveal
- Never swapped mid-film ✓

## STILL economy
~202s → 2 stills allowed (1 per 90s); used: 1 (B06, THE MECHANISM entry) ✓

## Exclusions honored
- No Ilyas et al. experimental details ✓
- No robust-dataset debate ✓
- No defense toolkit ✓
- No gradient math ✓

---

## Slots YOU fill (prompts in PROMPTS.md, beat-id-prefixed)

### B06 — STILL · ai · kenburns (THE MECHANISM entry)
The content IS close-up digital pixel noise or static pattern, black and white, abstract and grainy, suggesting hidden structure.
Wrong = a clean graph, a normal image, anything that looks orderly.
Real-asset alternatives (check first):
- https://commons.wikimedia.org/w/index.php?search=pixel+noise+static+pattern&title=Special:MediaSearch&type=image
Drop the result in `pantry/` as `B06-<anything>.jpg`.
