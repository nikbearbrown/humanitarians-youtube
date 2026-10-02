# PROMPTS — *What We Chased Before.*

GATE F expects beat-prefixed prompts for every open slot. **This reel has no
open slots** — every beat is rendered by the pipeline, and every plate is
*computed* in-repo. Nothing to hand to a generation service, nothing to spend.

## The two on-screen prompts (content, not requests)

**B00 — the cold-open ask** (verbatim in `ClaudeComposerAsk`):

> Telescopes find far more exploding stars than anyone can follow up. How does
> a model decide which ones to chase, what does that decision do to the next
> model, and what would fix it?

**B12 — the handoff prompt** (read aloud, per HANDOFF LAW):

> My model was trained on data that earlier decisions produced. Help me work
> out what it can never learn from that data, and design the cheapest
> experiment that would show me.

Rubric, on screen and spoken: does it ask **how the data was collected**, not
just what is in it · does it name a class the data **cannot contain** · does
the experiment **cost less than the status quo**.

That last item is the transferable lesson, and the episode earns it with a
number: one night in ten takes the chance of ever seeing the rare class from
35% to 92%.

## The plate generation (in place of a stock / gen-AI request)

`assets/gen_triage.py` — run `python assets/gen_triage.py`. Deterministic, one
seed (1017). numpy + Pillow only; **no sklearn**, which the venv does not ship.

**It is not a drawing program.** It runs a closed-loop survey simulation:
three classes (65 / 30 / 5%), overlapping 2-D features, a magnitude per object,
a **brightness-biased seed set of 30 labels**, then 12 seasons × 20 spectra,
repeated **60 times**, under three follow-up strategies.

| Choice | Why |
|---|---|
| Gaussian naive Bayes, hand-written | A class with **no labelled examples cannot be predicted at all**, so the feedback mechanism is visible in the model rather than buried in an ensemble. An imported random forest would have hidden the thing the episode is about. |
| A brightness-biased seed set | This is the real historical situation, and it is what makes rare-class recall start at zero rather than degrade from something. |
| The rare class placed in the overlap between the two common ones | Genuinely ambiguous objects are the ones worth a spectrum — which is exactly why Fink's deployed rule takes the alerts nearest a 50/50 call. |
| Three strategies | canonical (brightest first), greedy (most confident), uncertainty (smallest margin). These map onto Ishida+2019's canonical / passive / active. |
| **Medians, not means** | The outcome is bimodal. See below. |

### Four errors this script caught, all mine

1. **The claim was wrong before the code was.** I asserted rare-class recall
   "collapses" under a greedy budget. It does not — it starts at zero and never
   leaves, because a brightness-biased seed contains no rare objects at all.
   The self-check failed, and the right response was to rewrite the claim to
   match the experiment rather than tune the experiment to match the claim.
2. **A mean of a bimodal outcome.** Twelve repeats gave 0.088; sixty gave a
   **median of 0.000 with 48 of 60 runs ending at zero**. The mean was being
   dragged up by a few lucky runs that stumbled on a rare object early. "Low
   recall" and "usually none at all" are different claims.
3. **Two plates measured the same configuration with different statistics**,
   so pure-greedy read 0.281 in one and 0.000 in the other.
4. **An off-by-one in when the loop was evaluated** — metrics were recorded at
   the *top* of each season, so the last point reflected eleven rounds of
   spectra, not twelve.

### Two plates that computed something true and showed it badly

- `loop.png` drew accuracy on a 0–1 axis. Every strategy sits between 0.88 and
  0.92, so all three curves collapsed into one flat line and the panel said
  nothing — while its whole job is to show accuracy *rising* beside a panel
  pinned at zero. Zoomed to 0.84–0.94.
- `budget.png` plotted the **median** rare-class recall, which for a bimodal
  outcome jumps discontinuously and drew as a jagged step. Replaced with the
  **fraction of surveys that recognise the rare class at all** — smooth,
  bounded, and the question a time-allocation committee actually asks.

**If you re-tune a plate, delete `media/videos` before re-rendering.** Manim
caches partial movie files keyed on scene *code* and does not hash the contents
of images a scene loads.

## Scene briefs (in place of generation prompts)

| Beat | Scene class | Brief |
|---|---|---|
| B01 | `B01_Presenter` | Name card, terracotta hairline, and a card with two rows: "nine episodes / AI looks at the sky" struck, "this one / AI chooses what we look at" accented. Closer: the sample is the decision. |
| B02 | `B02_OneBreath` | The BLUF. **No exhibit** — EXECUTIVE-SUMMARY LAW makes beat 2 text/kinetic. Three sets, the third accented and underlined. Closer: the loop was already closed. |
| B03 | `B03_TheDeadline` | The computed light curves with the useful window shaded, and two counters beside them. The window caption is landscape-only. Closer: the decision cannot wait. |
| B04 | `B04_WhichOnes` | Four published bars with the unconfirmed remainder ringed terracotta, a quiet *published, not measured here* tag on one side and the editorial line on the other. No axis label — it sat between them and collided with both. Closer: the bright ones, every time. |
| B05 | `B05_TheLoop` | Four chained boxes, the last filled terracotta, with a return leg routed **below** (landscape) or **beside** (portrait) every label. A closed ellipse drawn through the boxes put a stroke under all eight text objects and GATE B flagged every one. Closer: best at what we already looked at. |
| B06 | `B06_TwelveSeasons` | The two-panel result with the counter **beside** the plate in landscape — stacked, a 3.87-unit plate left 0.43 units for two labels, an axis label and a counter. Closer: accuracy never warned anyone. |
| B07 | `B07_WhatGotLabelled` | The two composition panels with the figures side by side beneath them in both aspects. Stacked, the portrait caption ended up below its own closing line. Closer: it kept confirming what it knew. |
| B08 | `B08_SpendItOnDoubt` | The two feature-space snapshots, a short key line, and the two enrichment figures as one row of chips. As figure-over-subline the sublines landed exactly on the panel labels. Closer: doubt goes where the labels are not. |
| B09 | `B09_TheReceipt` | The deployed card with the chip placed **below** the card edge rather than straddling it, and the two unexpected classes over a struck line. Closer: it found things nobody asked for. |
| B10 | `B10_TheTell` | The card, the trade-off curve, and the counter — which reads **35% → 92%**, not "one night in ten", because the closing line already says that and the phrase was appearing twice on screen. Closer: one night in ten. |
