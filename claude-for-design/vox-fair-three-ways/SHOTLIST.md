# SHOTLIST — vox-fair-three-ways

**Why No Algorithm Can Be Fair Three Ways at Once** · 16:9 · ~110s est. (12 beats)
Accents: dusty blue `#5B7B9C` = group A · terracotta `#D35F43` = group B — **group identity, morally neutral here** · gold `#F5D061` = editor's pen + the EQUAL/check chips.
All numbers computation-verified via Chouldechova's relation (FACTCHECK.md). The calibration-state numbers are CORRECTED from the chapter's inconsistent table — erratum filed.
Card exclusions: no algebra on screen · no COMPAS · no individual/counterfactual fairness · no GE index · no debiasing toolkit.

Shot-type histogram: CARD 2 · STILL 1 · GRAPHIC 5 · COMPOSITE 2 · DOCUMENT 2 — max consecutive: 2 (B07–B08). Motion: hold 2 · kenburns 1 · isotype 2 · annotate 2 · highlight 2 · drawon 2 · kinetic 1 — max 17%. Lint: pass.

---

## B01 — CARD (title) · own · ~10.4s
Copy: **Why no algorithm can be fair three ways at once** / sub: *the impossibility theorem*

## B02 — STILL · ai · kenburns · ~10.0s  ← MEDIA SLOT (the only one)
Slot: `media/B02.png`
t2i prompt: printed application decision form with two large checkboxes labeled yes and no, anonymous and clinical, pinned like a clipping to aged newsprint, desaturated flat print reproduction, editorial collage, no names or faces
Synthetic — disclosure in credits.

## B03 — GRAPHIC · own · isotype · ~7.2s
Definition 1, equal yes-rates: two rows of 10 outline squares (blue/terra); 4 fill in each. Countable.

## B04 — COMPOSITE · own · annotate · ~7.6s
Definition 2, equal errors: rows persist; slate chips land — "false alarms — equal" / "misses — equal."

## B05 — GRAPHIC · own · isotype · ~8.4s
Definition 3, the honest score: chip "the model says: 70%"; exactly 7 of 10 fill in each row.

## B06 — DOCUMENT · own · highlight · ~9.6s
Quote card: **"You can have any two. Not three."** — *— Kleinberg, Mullainathan & Raghavan · Chouldechova, 2016*. Gold sweep on "two."

## B07 — GRAPHIC · own · drawon · ~10.4s
Manim: `TheMachine` — two score-distribution panels (A massed right, B massed left), threshold lines, and the dial table in the HONEST-SCORE state:
| | A | B |
|---|---|---|
| misses caught | .83 | .50 |
| false alarms | .20 | .04 |
| a "yes" is right | .86 | .86 |

## B08 — GRAPHIC · own · kinetic · ~10.4s — THE CORE MOVE
Manim: `EqualizeErrors` — B's threshold slides (.5 → .6); table Transforms to the equalized-odds state: TPR .70/.70, FPR .15/.15 (gold EQUAL chips), PPV **.88 vs .67**. Fix the errors, break the score.

## B09 — COMPOSITE · own · annotate · ~9.6s
Manim: `HonestAgain` — threshold slides back; table returns to honest state; the film's ONE HandRing lands around the split error rows, timed to "tear."

## B10 — GRAPHIC · own · drawon · ~10.0s
Manim: `TheTriangle` — three nodes (equal yeses · equal errors · honest score); gold checks land on two, the edge to the third snaps with a terracotta X; the checks rotate to another pair, another edge snaps. Fig 7.1 in motion.

## B11 — DOCUMENT · own · highlight · ~10.0s
Quote card: **"Which fairness should win?"** — *— not a technical question*. (The COMPAS lesson, carried generically — the case itself is excluded.)

## B12 — CARD (endcard) · own · ~9.2s
Copy: **Fairness is a choice. The theorem just makes it honest.** / sub: *from Computational Skepticism for AI — chapter 7*

---

## Slot inventory

| Slot | Need | From |
|---|---|---|
| `media/B02.png` | yes/no decision form still | t2i prompt above (ai — disclosure) |

Eleven of twelve beats render now.
