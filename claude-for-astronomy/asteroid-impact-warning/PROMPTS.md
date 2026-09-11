# PROMPTS — *The Number Went Up.*

GATE F expects beat-prefixed prompts for every open slot. **This reel has no
open slots** — every beat is rendered by the pipeline, and every plate is
*computed* in-repo. Nothing to hand to a generation service, nothing to spend.

What follows is the two prompt-shaped artifacts the reel *contains*, the plate
recipe, and the scene briefs that stand in for generation prompts.

---

## The two on-screen prompts (content, not requests)

**B00 — the cold-open ask** (verbatim in `ClaudeComposerAsk`):

> An asteroid's impact odds climbed to three percent, then fell to zero. What
> actually finds these objects, which part of that is machine learning, and why
> did the number rise before it collapsed?

**B12 — the handoff prompt** (read aloud, per HANDOFF LAW):

> Help me tell apart a number that rose because the situation got worse, from
> one that rose because the uncertainty shrank — and tell me what to ask before
> I react to either.

Rubric, on screen and spoken: does it separate the **estimate** from the
**uncertainty** · does it ask **what new data arrived** · does it name what
would make the number **fall**.

That third item is the transferable lesson. A risk number with no stated
condition for falling is not a measurement; it is a mood.

---

## The plate generation (in place of a stock / gen-AI request)

`assets/gen_neo.py` — run `python assets/gen_neo.py`. Deterministic, one seed
(8801), logged in `SOURCES.md`. Needs only numpy, scipy and Pillow — **no
matplotlib**, because the toolkit venv does not ship it and Ep. 07 established
that PIL draws these plots perfectly well.

**It is not a drawing program.** It runs the calculations the episode
describes and prints its own diagnostics on every run.

| Step | How |
|---|---|
| star field | analytic Gaussian PSFs on a Poisson sky, with a Pareto flux distribution so a few stars are bright and most are faint |
| the mover | a PSF *smeared along a segment*, summed over 24 sub-exposures — a 30 s exposure of a fast NEO is a short streak, not a dot, and convolving a line with a Gaussian by hand gets the end caps wrong |
| differencing | the reference frame is deliberately misregistered by 0.35 px before subtraction, so bright stars leave dipole residuals. **That is where the artefact classes come from** — a perfect subtraction would make the whole episode unnecessary |
| detection | threshold at 5σ of the difference's own MAD-estimated noise, then a 4-connectivity flood fill to count blobs. Prints 4 blobs: 1 real, 3 artefacts |
| the eight classes | each **synthesised from its own physical model**: a trailed NEO, a point source, a 1–2 px cosmic ray with *no PSF at all*, a subtraction dipole, a diffraction spike, a satellite trail, a saturated-column bleed, and pure noise |
| stamp stretch | one PHYSICAL stretch shared by all eight panels — zero at the sky level, full scale 26 noise-σ above it, on a 0.20 grey pedestal so the dipole's negative lobe is visible |
| tracklet | a least-squares straight-line fit through four timed positions; prints the RMS residual for the real mover (0.040) and for four unrelated artefacts (1.456) |
| capture radius | `b_cap = R⊕·√(1 + (v_esc/v∞)²)`, with v∞ recovered from the published impact speed first. Using the impact speed directly understates b_cap by ~12%, and the code says so |
| impact probability | exact quadrature of the target-plane Gaussian over the capture disc — the inner integral done in closed form with `erf` |
| the b-plane | the actual 2-D Gaussian density rendered as a raster, at three widths, with Earth's disc and its offset **to scale** |

### Four defects were found and fixed in this generator — three by looking at what it produced, one by the number it printed

1. **The self-check refuted my own derivation.** The script asserts that the
   probability curve's peak sits where geometry says it must. The first
   version predicted σ_peak = d from a one-dimensional argument; the numbers
   said 0.67 d. The numbers were right — the uncertainty shrinks in *both*
   target-plane directions, so the correct answer is **σ_peak → d/√2 =
   0.7071**. The script now asserts that and raises `SystemExit` on failure.
2. **The self-check then broke on Monte Carlo noise.** With the corrected
   prediction, sampling still failed at `b_cap/d = 0.001`, where the peak
   probability is ~10⁻⁵: 800,000 samples leave about eight hits per point and
   `argmax` returns noise. Replaced with exact quadrature. **A self-check that
   is noisier than the effect it checks is not a check.**
3. **The mover was invisible.** At 5200 flux, spread along a trail, the one
   real object sat inside the difference image's noise — a picture of nothing.
   Raised to 34,000 and gave the difference frame its own signed stretch.
4. **The dipole rendered as a single dot**, and the bleed class as two black
   rectangles. Both came from per-panel percentile stretching, which rescales
   each cut-out against its own brightest pixels — so a stamp containing one
   saturated column maps everything else to black, and the eight classes stop
   being comparable, which is the exact comparison the beat is making. One
   shared physical stretch on a grey pedestal fixed both.

**If you re-tune a plate, delete `media/videos` before re-rendering.** Manim
caches partial movie files keyed on scene *code*, and its cache key does not
hash the contents of images the scene loads.

---

## Scene briefs (in place of generation prompts)

| Beat | Scene class | Brief |
|---|---|---|
| B01 | `B01_Presenter` | Name card. `OM MALI` large, terracotta hairline, role line beneath. Beside it a card with two rows: "seven episodes / AI reads the sky", struck; and "this one / the reading ends, the arithmetic begins" in the accented token. Closer: Ep. 08 · the number is not the news. |
| B02 | `B02_OneBreath` | The BLUF. **No exhibit** — EXECUTIVE-SUMMARY LAW makes beat 2 a text/kinetic beat, never the first exhibit. Three sets of kinetic type on a card, the third in the accent and underlined. Closer: finding it is learned. fearing it is not. |
| B03 | `B03_TheHaystack` | The computed difference triplet, panels named left to right with "the difference" in the accent. A terracotta ring on the one real mover. Captioned as a synthetic field. A chip for the alert volume, then a line naming the three artefact families. Closer: most of what moves is not a rock. |
| B04 | `B04_EightKinds` | The eight-class grid, with terracotta rings on cosmic ray and dipole — the two the narration names. Two legend lines name all eight (per-panel labels do not fit the sheet's 0.22-unit gutter in either aspect). Beside it ONE PIXEL and TWO LOBES with glosses, then the chip. Closer: it learns what the camera lies about. |
| B05 | `B05_Tracklet` | Four terracotta dots with the fitted line drawn through them; four hollow ghost dots that no line fits. A two-line legend, then three counters, the last underlined. Closer: the point was speed, not cleverness. |
| B06 | `B06_WhereLearningStops` | Two boxes: LEARNED filled terracotta, COMPUTED outlined in ink, an arrow between, and the label "the terracotta stops here" at the boundary. Beneath, one ink track and a 22-line terracotta fan — `_kclip` truncates the normal, because an unbounded fan put a line through the title. Closer: it never computes a risk. |
| B07 | `B07_TheNumberWentUp` | The published record rebuilt: axes, six plotted points, the climb in terracotta and the collapse in ink, 3.1% underlined, and the Torino chip placed clear of the plot's right edge (on it, GATE B calls it a label on a curve). Closer: nobody made a mistake. |
| B08 | `B08_WhyItHadTo` | The three b-plane panels with their tags and a scale key, beside the computed probability curve with "the region shrinks →" beneath and its peak named. The chip insists the plate is computed, not redrawn. Closer: a rising number was never bad news. |
| B09 | `B09_Again` | An ink Moon, a truncated terracotta fan crossing it, the 4.3% figure struck through, and the ruling-out line with its date. Closer: the shape repeats because the geometry does. |
| B10 | `B10_TheTell` | A card headed WHAT IS ACTUALLY AUTOMATED: row one boxed in terracotta, row two struck. Beside it the completeness bars with size-class labels and a caption naming the 90% rule. A counter for the eleven. Closer: the search is the unfinished part. |
