# FACTCHECK — vox-invisible-flip

Source of record: `books/computational-skepticism-for-ai/chapters/08-robustness-what-understanding-means-when-a-pixel-can-break-the-model.md` ("The panda becomes a gibbon" + the linearity hypothesis section).
Primary source verified 2026-07-06 via web search — **this closes the chapter's own [Verify] tag on the panda-gibbon citation.**

## The panda-gibbon case — verified

| Beat | Claim | Verdict | Source / derivation |
|---|---|---|---|
| B02 | "panda, 57.7% confident" | ✓ | Goodfellow, Shlens & Szegedy, "Explaining and Harnessing Adversarial Examples" (arXiv 1412.6572, Dec 2014; ICLR 2015), §3 figure: GoogLeNet classifies the clean panda at 57.7%. |
| B03 | "pixel by pixel, the differences are fractions of a percent" | ✓ | The FGSM perturbation uses ε = 0.007 on [0,1]-scaled pixels — 0.7% of the brightness range per coordinate, below perceptual threshold at print scale. Chapter says the same. |
| B04 | "gibbon — 99.3%… more sure of the gibbon than it ever was of the panda" | ✓ | Same figure: the perturbed image classifies as gibbon at 99.3% — higher than the clean panda confidence (57.7%). The film's comparative phrasing is exactly the figure's punchline. |
| B01/title | "million-pixel answer" | flourish, labeled | Evocative scale in the candidate title. The narration is the honest one: "hundreds of thousands of numbers" (224×224×3 = 150,528 input values for the ImageNet-era pipeline). The title's "million-pixel" reads as a register of scale, not a count; narration never says "million." |

## The mechanism — the linearity hypothesis, drawn not written

| Beat | Claim | Verdict | Basis |
|---|---|---|---|
| B05 | "the image is a long list of numbers… each one a pixel's brightness" | ✓ | Standard input representation; the chapter's framing. Cell values on screen are dressing, not data claims. |
| B06 | "multiplies each number by a weight… one enormous weighted sum" | ✓ simplification, defended | The linear-classifier core of the chapter's own exposition (f(x) = wᵀx). Deep networks are locally-linear enough for the intuition — which is precisely Goodfellow's linearity hypothesis. No formula on screen (card exclusion). |
| B07 | "nudge every pixel by a sliver… each in the direction that pixel's weight prefers. The pushes never cancel. They only add." | ✓ | δ = ε·sign(w) in words — the sign-of-the-gradient intuition the card permits. The alignment (never canceling) is the mechanism's crux. FACTCHECK holds the math: Δf = wᵀδ = ε·Σ|wᵢ| = ε‖w‖₁, growing with dimension count. |
| B08 | "a hundred thousand invisible slivers… add up to a shove… the label flips" | ✓ | ε‖w‖₁ with d ≈ 150k coordinates: per-coordinate invisibility, decisive aggregate. "A hundred thousand" matches the honest input count. |
| B09 | "per pixel, nothing… across hundreds of thousands, everything" | ✓ | Restatement of the same accumulation; the chapter: "invisibly small in any one coordinate can accumulate into a decisive activation shift across thousands of coordinates." |
| B10 | "the perturbation isn't noise — it's a flashlight pointed at what the model really learned" | ✓ chapter's framing, labeled | The chapter's proxy thesis ("adversarial perturbations are not bugs, they are features," citing Ilyas et al. 2019 — which carries the chapter's other [Verify] tag, not closed here). The quote card is the FILM'S OWN line, attributed descriptively. Note: the deeper proxy/texture story is candidate 17's film — this one stays on the accumulation mechanism, one closing reading only. |

## Exclusions honored

No FGSM/PGD equations on screen (the ε‖w‖₁ math lives HERE) · sign-of-the-gradient appears only as "the direction that pixel's weight prefers" · no L∞/L1 vocabulary · no boundary-tilting second account · no defense toolkit · no Ilyas experimental detail (candidate 17's territory).

## Rendering honesty checks

- B03's twin plates must be pixel-identical copies of B02 — the film should NOT fabricate a visible perturbation pattern; invisibility is the claim.
- B06/B07/B08 are one persistent machine: same cells, same bar, same decision line — the fill climbs continuously across beats, never teleports.
- B07's arrows: identical size, identical direction, one per cell — alignment is the argument; varied arrows would say "noise," which is the opposite claim.
- The bar's fill turns terracotta only as it climbs under the perturbation — blue at rest (panda side), terracotta in motion toward the flip.
- The decision-line label sits clear of the line itself (Gate B rule); the "panda"/"gibbon" chips never overlap the tube.
- B02 archive slot needs its `.source.txt` sidecar (STAND-IN X until then); if a suitable PD panda photo isn't found, flip B02/B03 to `ai` with disclosure — the argument doesn't depend on the photo's provenance, only its constancy.
- Confidence numbers appear exactly twice: 57.7 (B02 chip) and 99.3 (B04 card) — both verified; no other numbers on screen except the honest "hundreds of thousands" in narration.

## Chapter errata (feed back to the book)

- The [Verify] tag on the panda-gibbon citation can be closed: Goodfellow, Shlens & Szegedy, arXiv:1412.6572 (ICLR 2015), §3 — 57.7% panda → 99.3% gibbon, ε=0.007, GoogLeNet. The chapter's "high confidence panda" slightly overstates 57.7% — suggest "middling confidence" or the exact figure; the 99.3% flip is the stronger fact and the chapter already leans on it correctly.

Sources: [Goodfellow et al. summary (OpenGenus)](https://iq.opengenus.org/explaining-and-harnessing-adversarial-examples/) · [PyTorch FGSM tutorial](https://docs.pytorch.org/tutorials/beginner/fgsm_tutorial.html) · [Interpretable ML — Adversarial Examples](https://f0nzie.github.io/interpretable_ml-rsuite/adversarial.html)
