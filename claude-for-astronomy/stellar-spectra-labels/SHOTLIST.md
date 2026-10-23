# SHOTLIST — *What The Model Would Say.*

Ep. 14 · `stellar-spectra-labels` · 14 beats · 437 words
Predicted 2:27 against Ep. 13's measured 0.3369 s/word — **under 3:00 by design**,
with ~33 s of margin for the ±5–10 % words-only error.

Both cuts render from one `scenes.py`. 16:9 at 3840×2160, 9:16 at 2160×3840.

---

## Lanes

| Lane | Beats | Engine |
|---|---|---|
| Claude UI | B00, B11, B12, B13 | Remotion (`ClaudeComposerAsk`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`) |
| Illustrated | B01–B10 | reel-local `scenes.py` (Manim CE) |

The ILLUSTRATE LAW: the Claude desktop UI appears only where the reel is
actually addressing Claude. Everything in between is drawn.

---

## Beat by beat

### B00 · COLD OPEN · 9.8 s · `ClaudeComposerAsk`
Greeting **"Ciao, HAI"** — the hello lexicon cycles least-recently-used, and
Ciao was last seen at Ep. 10. The composer types the ask, the send button
arms in terracotta, the runner reads *fitting 160 pixels against 500 labelled
stars*, and three result lines land in order. Those three lines are the reel's
own findings, in the order the reel proves them.

> Opens on the required line: "Hi, I'm Om Mali. This video is about…"

### B01 · FRAME · 7.4 s · `B01_Presenter`
Name writes in under a terracotta rule; role line; a card beside it. Row one
— *thirteen episodes / is the answer right* — lands and is **struck**. Row two
— *this one / where the answers came from* — lands and is **boxed**. Series
line: *Ep. 14 · the labels are a model's output*.

Portrait stacks name above card. Same play count in both aspects.

### B02 · FRAME · 13.5 s · `B02_OneBreath`
One card, three rows, no plate. The argument before any evidence:

1. **NOBODY MEASURES A STAR DIRECTLY** — *the labels come from a physics model*
2. **THE AI LEARNS THE LABELS** — *and nothing else*
3. **SO IT PREDICTS THE MODEL** (accent, underlined)

Closer: *not the star*.

### B03 · THE METHOD · 10.8 s · `B03_TheMethod`
The published result, as an **isotype at honest scale**. One mark = 100 stars
in both blocks: five terracotta marks for the 542 reference stars, a 24×24
field of 560 ink marks for the 56,000 labelled. The caption states the rate.
A card names what the method does *not* contain — no stellar models, no line
list. Closer: *only the labels*.

Landscape carries a `PUBLISHED · The Cannon, ApJ 2015` chip; **portrait drops
it**, because the 4.64-unit band has to carry a label, five marks, a label, a
grid, a card and the closer, and the chip is the one item the narration does
not speak. The citation line still names the paper.

### B04 · THE MECHANISM · 10.4 s · `B04_TheData`
`spectra.png` — three spectra at the same Teff and log g, different metals.
Rows named *fewest metals* / *in between* / *most metals* (terracotta). A
dashed terracotta guide drops through **pixel 47**, the most metal-sensitive
line in the frozen bank, visibly deeper in each spectrum down the stack.
Closer: *it never learns why*.

Landscape names the rows in the left margin at their measured plate heights;
portrait stacks the names beneath the plate.

### B05 · THE MECHANISM · 11.5 s · `B05_TheChain`
**Where the colour contract is taught.** Four boxes draw one at a time —
*the star*, *the spectrum*, **a physics model** (terracotta), *the AI* — with
arrows between. A terracotta bracket closes under links 2–4: *not nature*.
Closer: *only the first one is nature*.

Landscape runs the chain left to right; portrait runs it top to bottom with
the bracket turned to the side. Play counts match.

### B06 · THE RESULT · 13.5 s · `B06_Agrees`
`agree.png` — predictions against the training labels. The one-to-one line is
**traced** over the plate. Axes named in the right-hand column, then the chip
**0.033 dex**, then *agreement with its own labels*. Closer: *this is the plot
a paper shows*.

### B07 · THE RESULT · 10.8 s · `B07_TheTruth`
**The load-bearing beat.** B06 and B07 are both scatter plots, so this one
does not *present* a second scatter — it opens on B06's closing composition
and changes exactly one thing. The horizontal axis label transforms from
*what the labels say* to **what the TRUTH says**, the points cross-dissolve in
place and visibly leave the diagonal, and the chip rolls **0.033 → 0.128**.
A note lands: *nothing about the model changed*. Closer: *four times worse
than it looked*.

The dissolve is FadeOut+FadeIn of two plates at identical width and position,
not a Transform — an ImageMobject is not a VMobject and cannot be interpolated.

### B08 · THE RESULT · 13.8 s · `B08_Precision`
`bars.png` — three numbers you could quote, named **under their own bars**:

| bar | name | value |
|---|---|---|
| 1 (ink) | measure the same star twice | 0.008 dex |
| 2 (ink) | agrees with its own labels | 0.033 dex |
| 3 (terracotta) | the real error | 0.128 dex |

A dashed rule runs across at bar one's height and a terracotta double-arrow
spans up to bar three, labelled **15×** outside the plate. Closer: *the error
bars describe neither*.

Portrait has no right-hand column at 3.60 units, so the three names become
legend rows beneath the plate and the 15× becomes a chip. Nothing is dropped.

### B09 · THE TELL · 10.4 s · `B09_Structure`
`structure.png` — the [Fe/H] error against temperature. Zero is named beside
the plate (landscape) or in a note beneath it (portrait, where a label beside
a 3.40-unit plate in a 3.60-unit frame would leave the frame). The terracotta
fit is already drawn in the plate. Chip: **correlation 0.995**; then the slope,
then *a trend survives every check that compares averages*. Closer: *a line,
not a cloud*.

### B10 · THE TELL · 11.1 s · `B10_TheTell`
`anchor.png` — error against the truth, three ways:

| bar | name | value |
|---|---|---|
| 1 (terracotta) | 500 precise, inherited labels | 0.128 dex |
| 2 (ink) | 120 independent, noisier ones | 0.032 dex |
| 3 (soft) | an unbiased teacher · control | 0.013 dex |

**The only beat where the terracotta bar is the one you do not want** — and
the contract still holds, because terracotta is what the labels brought with
them. Ep. 11 shipped a bar chart whose winning design had the shorter bar and
it read as a failure, so here the names carry the verdict, not the length:
*four times fewer. four times more accurate.* Closer: *fewer, noisier, and
right*.

### B11 · VERDICT · 9.4 s · `ClaudeVerdictArtifact`
A five-line artefact page. Five, not four: GATE V's bbox-fill floor is 0.55
and a four-line card sits exactly on it, so the verdict flips on encoder
noise. The fifth line is the anchored result, which is also the line the
episode most wants to leave behind.

### B12 · HANDOFF · 10.8 s · `ClaudeComposerAsk`
The viewer's prompt, with three grading lines: does the answer trace the
labels back to *their* source, name a check that shares no assumptions, and
distinguish precision from accuracy.

### B13 · OUTRO · 4.0 s · `ClaudeTitleOutro`
Title poster-style with the terracotta period, rule, handle, series position.

---

## Aspect discipline

`scenes.py` is aspect-aware. `frame_height` stays 8.0 in both cuts, so the
vertical band plan is identical; only x changes (±6.15 landscape, ±1.80
portrait). Portrait is **not a crop** — it carries fewer elements, larger.

**The reduction rule: anything the narration speaks stays on screen.** What
portrait loses is on-screen-only extras — B03's PUBLISHED chip, B09's
margin label for zero — each replaced or already carried by the citation line.

**Play-count parity is checked in both aspects**, because the pacing solve
runs once, in landscape. Ep. 11's B04 overshot by +0.92 s precisely because
its portrait branch played more animations than its landscape branch.
