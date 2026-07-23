# SHOTLIST — vox-more-data-more-confident

**Why More Data Makes the Wrong Answer More Confident** · 16:9 · ~100s est. (11 beats)
Accents: dusty blue `#5B7B9C` = the truth · terracotta `#D35F43` = the biased cluster · ink = unbiased darts · gold `#F5D061` = editor's pen.
Facts verified (FACTCHECK.md): Literary Digest 1936 — 10M mailed to auto/telephone owners, ~2.4M returned, Landon 57%/370 EV predicted; FDR won ~61%, 46 of 48 states; the Digest folded within 18 months.
Card exclusions: no bias-variance decomposition · ONE plain-language "the bias" label, no E[θ̂] notation · no ten-mechanism taxonomy · Literary Digest = the hook + one causal line.

Shot-type histogram: CARD 2 · STILL 1 · COMPOSITE 3 · DOCUMENT 1 · GRAPHIC 4 — max consecutive same-type: 2 (B05–B06). Motion histogram: hold 2 · kenburns 1 · annotate 3 · highlight 1 · drawon 2 · isotype 2 — max 27%. Lint: pass.

---

## B01 — CARD (title) · own · ~9.2s
Cue: "The biggest poll in American history…"
Copy: **Why more data makes the wrong answer more confident** / sub: *bias is not noise*

## B02 — STILL · archive · kenburns · ~9.6s  ← MEDIA SLOT
Cue: "Nineteen thirty-six. The Literary Digest mails out ten million ballots…"
Slot: `media/B02.png` + `media/B02.source.txt` (required — archive slot; STAND-IN X until sidecar exists)
Archive queries:
- https://chroniclingamerica.loc.gov/search/pages/results/?andtext=literary+digest+poll+landon&date1=1936&date2=1936
- https://www.loc.gov/search/?q=literary+digest+1936+poll
- https://commons.wikimedia.org/w/index.php?search=Literary+Digest+1936+poll&title=Special:MediaSearch&type=image
1936 press is public domain — Chronicling America is the richest source here.

## B03 — COMPOSITE · archive · annotate · ~8.0s  ← derives from B02
Cue: "Franklin Roosevelt then won forty-six of the forty-eight states."
Slot: `media/B03.png` — re-crop of B02's plate, smaller. Annotation (assembly plane): terracotta strike-X through the prediction + serif label "Roosevelt: 46 of 48 states," timed to "wrong."

## B04 — DOCUMENT · own · highlight · ~10.4s
Cue: "Two point four million people. Surely a sample that big can't lie?"
Quote card: **"A sample that big can't lie."** — *— the instinct this story breaks*. Gold sweep on "can't."

## B05 — GRAPHIC · own · drawon · ~9.6s
Cue: "Here's the machine underneath."
Manim: `TheTarget` — hairline target draws itself; solid blue center dot labeled "the truth"; three ink darts land.

## B06 — GRAPHIC · own · isotype · ~9.2s
Cue: "An unbiased poll scatters its darts around the truth."
Manim: `UnbiasedTightens` — ink darts in waves of shrinking spread, centered on the blue dot. Honest convergence, seeded.

## B07 — COMPOSITE · own · annotate · ~8.8s
Cue: "But the Digest's darts weren't aimed at the truth."
Manim: `BadAim` — terracotta crosshair drifts from the truth to an offset aim-point; chip: "who got ballots: car & telephone owners." (The one history line.)

## B08 — GRAPHIC · own · isotype · ~10.4s — THE CORE IMAGE
Cue: "Now add data. The scatter tightens beautifully — around the wrong point."
Manim: `TightenWrong` — terracotta waves of shrinking spread around the OFFSET point; mono counter ticks n = 100 → 10,000 → 2,400,000; the blue truth dot sits alone outside.

## B09 — COMPOSITE · own · annotate · ~9.6s
Cue: "Scale bought precision. It never bought correction."
Manim: `TheGap` — dumbbell line from cluster center to truth dot; the film's ONE label: "the bias"; the film's ONE HandRing on the gap, timed to "name."

## B10 — GRAPHIC · own · drawon · ~9.6s
Cue: "…Precision is how tightly the darts cluster. Truth is where."
Manim: `PreciselyWrong` — two small targets: tight terracotta cluster off-center ("precisely wrong") vs loose ink cloud on-center ("roughly right").

## B11 — CARD (endcard) · own · ~8.4s
Cue: "The Literary Digest folded within two years…"
Copy: **Scale buys precision — never correction.** / sub: *from Computational Skepticism for AI — chapter 3*

---

## Slot inventory

| Slot | Need | From |
|---|---|---|
| `media/B02.png` + `B02.source.txt` | 1936 poll/headline plate | Chronicling America links above (PD) |
| `media/B03.png` | re-crop of B02 | derive locally, no spend |

Nine of eleven beats render now.
