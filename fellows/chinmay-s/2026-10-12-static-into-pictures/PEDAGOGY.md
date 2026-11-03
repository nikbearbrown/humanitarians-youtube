# PEDAGOGY.md — Static Into Pictures (GATE P)

**Reel:** `hai-static-into-pictures` · 23 beats · Bella (`af_bella`) · Humanitarians AI
**Audience:** children / complete beginners, watchable by an adult without condescension.
**Source:** a from-scratch diffusion notebook, 66 cells, NumPy and Matplotlib only.

---

## 1. This one teaches. It does not tear down.

The three previous reels in this series were critiques, because those notebooks had real
defects. **This notebook does not**, and the reel says so by treating it as a thing worth
explaining rather than hunting for faults. What makes it careful:

- **A numerical gradient check** (cell 25). The analytic backprop is verified against
  finite differences, worst relative error `1.5e-07`. Most tutorial code never does this.
- **Real baselines beside the results** (cell 53). The MMD table includes fresh real data,
  a single Gaussian and pure noise, so a reader can see what the scores mean.
- **Honesty about its own limits.** On the loss plateau: *"It does not go to zero, and it
  never will. That is not a bug."* On metrics: *"Always look at samples too."* On guidance
  at w=10: the spread stops shrinking *"but not for a good reason."*

B09, B10 and B18 carry those three points into the reel directly.

## 2. Provenance of every number

`build_beat_sheet.py` **parses the notebook's recorded outputs** — it does not transcribe
them. Figures are regexed out of the stream outputs of cells 10, 25, 30, 50, 53 and 60,
then checked:

```
signal left at T=200: 0.0782   (independently recomputed: 0.0782)
gradient check worst error: 1.5e-07
final training loss: 0.3262    (141,058 parameters)
MMD: real -0.00012 · DDPM-200 0.00025 · DDIM-50 0.00036 · DDIM-5 0.02266 · noise 0.02348
guidance: w=0 → 47.9% / 0.950   w=1 → 99.8% / 0.715   w=10 → 100.0% / 0.498
```

Eight assertions guard these, including that the DDIM degradation is monotonic and that
the five-step claim really does sit near pure noise. If the notebook is re-run and the
numbers move, the build fails rather than the narration going stale.

**The forward-process figure is independently recomputed**, not just read: a fresh
`cumprod(1 - linspace(1e-4, 0.05, 200))` gives 0.0782, matching the notebook exactly.

## 3. The animation is the mathematics

`KidSprinkle` and `KidUnsprinkle` are not illustrations of diffusion — they **run** it.
Each dot is placed by the notebook's own closed form,

```
x_t = sqrt(abar_t) * x0 + sqrt(1 - abar_t) * noise
```

with `abar` from the same linear beta schedule, and per-point noise from a deterministic
hash so dots stay coherent between frames. The on-screen "% of the drawing left" is
`sqrt(abar_t)` at that frame, so the counter and the picture cannot disagree.

## 4. How the hard ideas are carried

| Real concept | What a child sees |
|---|---|
| forward noising process | sprinkling mess on a drawing, 200 times |
| the closed-form shortcut | "we kept the recipe for the mess" |
| ε-prediction objective | "not *what is this?* but *which bit is the mess?*" |
| reverse/ancestral sampling | brushing a little mess off, over and over |
| gradient check | working the sum out by hand, then counting it a different way |
| DDIM step-skipping | taking bigger steps — until the step is too big to land |
| MMD vs baselines | a judge's scorecard, lower is better |
| classifier-free guidance | a dial for how hard to insist |
| the fidelity/diversity trade-off | "more obedient, less interesting" |

No equations appear on screen. Terms like *diffusion*, *DDIM* and *guidance scale* are
deliberately kept out of the narration except where B21 connects the dial to the
"guidance" slider a child may actually have seen in an app.

## 5. Honesty notes

- The spiral in the animation is a stand-in for the notebook's swiss-roll sample, drawn
  parametrically. The **process** applied to it is exact; the point cloud is not a replay
  of the notebook's own array.
- B14 says five-step sampling scores "about the same as pure static": 0.02266 vs 0.02348.
  That is 3.5% better, not worse — "about the same" is fair, "worse than" would not be.
- The reel does not re-run training. All model-dependent figures are the notebook's
  recorded run, stated as such in §2 rather than implied to be fresh.

## 6. Verdict

```
VERDICT: PENDING — awaiting human sign-off.
```

Generated with `--no-gate`, on the record. Two checks worth making for this cut: read it
as a child would, and confirm §1's characterisation — that this notebook is careful work —
matches your own reading, since the reel praises it by name of its methods.
