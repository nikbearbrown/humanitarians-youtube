# PROMPTS — *The Universe You Can Afford.*

GATE F expects beat-prefixed prompts for every open slot. **This reel has no open
slots** — every beat is rendered by the pipeline, and every plate is *computed*
in-repo. Nothing to hand to a generation service, nothing to spend.

What follows is the two prompt-shaped artifacts the reel *contains*, the plate
recipe, and the scene briefs that stand in for generation prompts.

---

## The two on-screen prompts (content, not requests)

**B00 — the cold-open ask** (verbatim in `ClaudeComposerAsk`):

> Cosmologists test theories by simulating whole universes, and a proper test
> needs thousands of them. What is the actual method for replacing those
> simulations with a neural network, how accurate is it, and what does the
> shortcut cost?

**B12 — the handoff prompt** (read aloud verbatim, per HANDOFF LAW):

> I want to replace an expensive simulation with a learned surrogate. Help me
> (1) choose which statistics it must reproduce and to what tolerance,
> (2) detect when an input falls outside its training set, and (3) decide what I
> would still run the slow way to keep it honest.

Rubric, on screen and spoken: are the **tolerances** named, per statistic · is
there an **out-of-distribution** check · is there a **slow-path** audit that
still runs.

That third item is the transferable lesson. A surrogate with no slow path left
running is not a speedup; it is an unverified claim that used to be a
calculation.

---

## The plate generation (in place of a stock / gen-AI request)

`assets/gen_cosmos.py` — run `python assets/gen_cosmos.py`. Deterministic, one
seed (7717), logged in `SOURCES.md`. **It is not a drawing program.** It runs the
two calculations the episode describes, in 2D at 512², and prints its own error
measurement on every run.

| Step | How |
|---|---|
| initial field | Gaussian random field with a CDM-like `P(k)`: rising as `k^ns`, turning over at `k_eq`, falling as `k^(ns-4)`. The turnover is what makes the result look like a web instead of noise |
| Zel'dovich | `psi = -i k / k² · delta_k`, then one move: `x = q + D·psi(q)`. The whole cheap answer in one line |
| N-body | particle-mesh: CIC deposit → FFT Poisson solve → kick → drift, 200 KDK leapfrog steps in the growth factor from `a = 0.10`. Equation of motion `dv/dD = -(3/2D)v + (3/2D²)g`, with the normalisation fixed by requiring the Zel'dovich growing mode to be an *exact* solution in the linear regime |
| deposit | 589,824 particles on a 512² mesh — **more particles than cells on purpose**, so the initial Lagrangian lattice does not survive as moiré in the voids. `np.bincount`, not `np.add.at`, which is the bottleneck at this count |
| display | arcsinh stretch with `gamma > 1`, bright web on near-black, warm-tinted to stay in palette. The first version used `gamma = 0.38`, which lifted the voids to a flat mid-tone and threw the picture away |
| residual | terracotta where N-body has more mass than Zel'dovich, ink where less, on cream. The first version was red/blue, which is not in the palette |
| power | the **measured** `P(k)` of both fields, first two bins dropped because they hold a handful of modes and are pure noise |
| halo zoom | the same region in both, centred on the largest *disagreement* — centring on the densest structure produced two panels that looked identical, which defeats the beat. The window wraps periodically |

**Four defects were found and fixed in this generator, all by looking at what it
produced or at the number it printed.** The worst was physics, not rendering: the
first integrator omitted the Hubble drag term, so the two calculations disagreed
by a factor of twenty on the largest scales. It was caught because the script
prints the measured `ΔP/P` and the value was 1841%. See `BUILD-LOG.md`.

**If you re-tune a plate, delete `media/videos` before re-rendering.** Manim
caches partial movie files keyed on scene *code*, and its cache key does not hash
the contents of images the scene loads.

---

## Scene briefs (in place of generation prompts)

| Beat | Scene class | Brief |
|---|---|---|
| B01 | `B01_Presenter` | Name card. `OM MALI` large, terracotta hairline, role line beneath, then a subline. Beside it a card with two rows: "six episodes / AI looks at the data", struck; and "this one / AI replaces the physics" in the accented token. Closer: Ep. 07 · there is nothing to look at. |
| B02 | `B02_OneBreath` | A computed cosmic-web plate, captioned as a 2D toy. Kinetic type in three sets on a stage beside it: NO EXPERIMENT IS POSSIBLE → SO YOU SIMULATE IT / THOUSANDS OF TIMES → NOBODY CAN AFFORD THAT in the accent. Closer: so a network learns the answer instead. |
| B03 | `B03_ParameterSpace` | A bordered 2D slice of parameter space, axes labelled generically (landscape only), with 150 seeded dots scattered in — one per cosmology. Then three counters with sublabels: 44,100 / N-body simulations, 7,000 / cosmologies, 8.5 trillion / particles. A terracotta chip: built as training data. Closer: you are searching a parameter space. |
| B04 | `B04_NoShortcut` | The starting-field plate with a caption. Beside it a ring with four chips on it — deposit, solve, kick, drift — and a terracotta arc tracing round it. The chips sit *outside* the ring: GATE B flagged all four when they sat on it. A HUNDREDS OF STEPS chip below. Closer: every particle pulls every other. |
| B05 | `B05_Zeldovich` | A schematic first: a grey dot, one terracotta arrow, a terracotta dot, labelled "one straight move, in one step". Then the Zel'dovich plate arrives framed in terracotta, with two chips beside it: RIGHT WHILE IT IS SMOOTH (quiet) / WRONG ONCE IT COLLAPSES (accented). Closer: exact, right up until it matters. |
| B06 | `B06_TheCorrection` | The terracotta-framed Zel'dovich plate, a minus sign, the ink N-body plate, an arrow, and the measured residual — each labelled beneath. A three-layer network glyph takes the residual as its target, labelled "learn this" (landscape only). Closer: it never computes a force. |
| B07 | `B07_Result` | The measured power-spectrum plate. The scene draws the axis labels and a two-line legend: N-body in ink, Zel'dovich in terracotta. Then WITHIN ~5% underlined, and "a thousandth of the time". Closer: the shortcut is not a small one. |
| B08 | `B08_DesignTell` | A card headed WHAT THE MODEL LEARNED. Row one types in and is struck: the law of gravity. Row two lands in the accent and is boxed: the map from start to finish — with "…for the universes it was shown" beneath. Beside it, the training set shown as a bordered plate. Closer: compression, not physics. |
| B09 | `B09_WhereItBreaks` | The halo zoom pair, labelled N-body (ink) and Zel'dovich (terracotta) beneath their own panels, with a terracotta ring on the core the cheap guess fails to build. Two measured figures: 4% / on large scales, 58% / on small ones, tagged as measured in this reel's own run. Closer: and haloes are where galaxies live. |
| B10 | `B10_TheBox` | A box labelled "the cosmologies it was trained on", filled with 90 seeded dots — the N-body runs already paid for — with the emulator chip inside it. The dot field is **cleared around the chip**, because an opaque chip is not enough for GATE B. An arrow leaves the box and is crossed out in terracotta; label: a cosmology it never saw. Closer: a compression of what you already paid for. |
