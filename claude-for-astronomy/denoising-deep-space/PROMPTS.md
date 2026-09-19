# PROMPTS — *The Sharpest Guess.*

GATE F expects beat-prefixed prompts for every open slot. **This reel has no
open slots** — every beat is rendered by the pipeline, and every plate is
*computed* in-repo. Nothing to hand to a generation service, nothing to spend.

What follows is the two prompt-shaped artifacts the reel *contains*, the plate
recipe, and the scene briefs that stand in for generation prompts.

---

## The two on-screen prompts (content, not requests)

**B00 — the cold-open ask** (verbatim in `ClaudeComposerAsk`):

> AI can turn a blurry telescope image into a sharp one. Where does the new
> detail come from, how would I know if it were invented, and what should a
> reconstruction actually report?

**B12 — the handoff prompt** (read aloud, per HANDOFF LAW):

> When a model sharpens, upscales or fills in my data, help me work out which
> parts are measured and which are the model's assumption — and what I should
> report alongside the result.

Rubric, on screen and spoken: does it separate **measured** from **assumed** ·
does it ask what the model was **trained on** · does it offer a **range**
rather than one answer.

That third item is the transferable lesson. Any restoration that returns one
picture has thrown away the only thing that told you which parts of it to
trust.

---

## The plate generation (in place of a stock / gen-AI request)

`assets/gen_deconv.py` — run `python assets/gen_deconv.py`. Deterministic, one
seed (9109), logged in `SOURCES.md`. Needs numpy, scipy and Pillow — **no
matplotlib**, which the toolkit venv does not ship.

**It is not a drawing program.** It runs the calculations the episode
describes, and two of its claims are assertions rather than pictures.

| Step | How |
|---|---|
| optics | the incoherent OTF of a circular pupil in closed form, `H(k) = (2/π)[arccos u − u√(1−u²)]` with `u = k/k_c`, and **identically zero above `k_c`**. That hard zero is the episode: frequencies above the cutoff are not attenuated, they are annihilated |
| the sky | an inclined exponential disc with a steep bulge, a bar, log-spiral arms and 14 seeded knots — structure across a wide range of scales, so the cutoff has something to destroy |
| observation | PSF convolution → Poisson photons → Gaussian read noise. Every step real; the "integrated SNR 364" is measured from it |
| striping | a 1/f profile along the slow-read axis, constant per row, estimated from 96 known-dark columns and subtracted — the same move NSClean makes in Fourier space |
| three answers | for each candidate prior, the regularisation strength is **bisected until χ²/N = 1**, so all three are equally consistent with the data by construction. Then a *sample* is drawn from each posterior, because the posterior MEAN is identically zero above the cutoff for every prior and therefore cannot differ — a fact that itself took a rewrite to notice |
| the posterior | exact. A linear-Gaussian problem with a circulant PSF is diagonal in Fourier space, so `var(k) = 1/(|H|²/σ² + 1/P)` and the samples are drawn from the true posterior rather than an approximation to it |
| the variance ratio | closed form, over the **observable band** only. Averaged over all modes it is pinned near the fraction lying above the cutoff, where `var/P = 1` whatever the data does, and the curve goes flat — which is why the paper it comes from takes its ratio inside an aperture around the galaxy |

### Five defects found in this generator — four of them errors of mine

1. **The stripe residual measured the wrong quantity**, comparing the cleaned
   frame against the noiseless scene and so folding in read noise that stripe
   removal never claimed to remove. It reported 22% for a method recovering
   the pattern to 3.6%.
2. **An arbitrary threshold.** ">20% of the truth" was picked before any
   measurement and then read 19.2%. The honest move was not to retune the
   threshold but to assert something meaningful: that the destroyed
   information exceeds the noise, and therefore dominates rather than
   rounds away.
3. **The wrong comparison region.** That noise comparison was first made over
   the whole frame, where the noise fills 65,536 pixels and the galaxy occupies
   a few thousand, so empty sky dominated the ratio and it read 0.5×.
4. **A prior 255× too weak** — numpy's unnormalised-FFT factor wrong by N.
   Nothing crashed. A too-weak prior simply stops contributing, so the
   posterior samples collapsed onto the mean, the "three answers" plate showed
   three nearly identical pictures (2.8% apart instead of 35.9%), and the
   variance ratio was computed against a mis-scaled prior. **This is the
   dangerous class: a silent numerical error that produces a plausible
   picture.** The normalisation is now derived (`std = √(Σspec)/N`) and
   asserted over 24 draws.
5. **A self-check noisier than the effect it checked.** The checks were first
   Monte Carlo; at the smallest disc the target probability is ~10⁻⁵, so
   800,000 samples left about eight hits per point and `argmax` returned noise.
   Replaced with exact quadrature.

**If you re-tune a plate, delete `media/videos` before re-rendering.** Manim
caches partial movie files keyed on scene *code*, and its cache key does not
hash the contents of images the scene loads.

---

## Scene briefs (in place of generation prompts)

| Beat | Scene class | Brief |
|---|---|---|
| B01 | `B01_Presenter` | Name card. `OM MALI` large, terracotta hairline, role line beneath. Beside it a card with two rows: "eight episodes / AI reads the sky", struck; and "this one / AI draws it" in the accented token. Closer: Ep. 09 · the detail is not a measurement. |
| B02 | `B02_OneBreath` | The BLUF. **No exhibit** — EXECUTIVE-SUMMARY LAW makes beat 2 a text/kinetic beat, never the first exhibit. Three sets of kinetic type on a card, the third accented and underlined. Closer: the gap gets filled either way. |
| B03 | `B03_TwoKinds` | The four computed panels, named left to right with the last two in the accent. A quiet chip for the removable pair and a terracotta chip for the irrecoverable one. Captioned as a synthetic field. Closer: one is a pattern, one is a loss. |
| B04 | `B04_TheChain` | The forward chain in four panels, each named beneath, with a LOSSY chip under the blurred step and a 98% counter with its subline. Closer: multiplied by zero, and gone. |
| B05 | `B05_SameData` | Two skies, the terracotta difference, the single shared observation. Two counters — 52% apart, 0.0000 noise σ, the second underlined. Nothing here is cited; the generator proves it. Closer: the data cannot tell them apart. |
| B06 | `B06_ThreeAnswers` | Three samples in a row, a χ² value typed under each, a line saying they match equally well, and a terracotta chip for the 36% spread. No rule between them — one sat 0.10 units from the line beneath and GATE B read the line as a label on a curve. Closer: sharpness is a choice. |
| B07 | `B07_WhereItComesFrom` | An ink card headed "the training set" with a grid of 66 tiles beneath it (the heading goes ABOVE: under the grid it landed on the bottom row of tiles, and a Square has a stroke). An arrow to a terracotta THE PRIOR box. A 17,852 counter, and the cost pair in landscape only. Closer: the most likely galaxy it was ever shown. |
| B08 | `B08_ManyAnswers` | Five panels, then two single-line rows — the second accented and bold — then a chip carrying the 1.0000 identity. Portrait drops the panel labels. Closer: the spread is the answer. |
| B09 | `B09_WhenItInvents` | The varratio plate, sized to 5.80 wide because at 2:1 it is the tallest plate in the reel, with **both** axis labels below it and a terracotta ring on the weak-data end. The two published figures sit in a column beside it under a "published, not measured here" tag. Closer: the ratio is the alarm. |
| B10 | `B10_TheTell` | A card: "removes the noise" struck, "adds an assumption" boxed in terracotta. Beside it two schematic cards — a soft blob and a tighter shape with dots — a **drawn** tick (the `✓` character is absent from EB Garamond and rendered as stray digits), and QUALITATIVELY in ink. Portrait drops the cards and the tick. Closer: report the range, not the picture. |
