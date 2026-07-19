# SHOTLIST — vox-99-percent-test

**Why a 99%-Accurate Test Is Almost Always Wrong When It Says Yes** · 16:9 · ~104s est. (12 beats)
Accents: dusty blue `#5B7B9C` = the one true positive / truth · terracotta `#D35F43` = false alarms / noise · gold `#F5D061` = editor's pen.
All numbers computation-verified (FACTCHECK.md). Countable-true law: 10,000 marks exactly, 1 blue exactly, 100 terracotta exactly, 101 in the pool.
Card exclusions: no Bayes formula on screen, no sensitivity/specificity vocabulary, no odds shortcut, no second domain example.

Shot-type histogram: CARD 2 · STILL 1 · DOCUMENT 2 · GRAPHIC 5 · COMPOSITE 2 — max consecutive same-type: 2 (B06–B07, B10–B11). Lint: pass.

---

## B01 — CARD (title) · own · ~9.5s
Cue: "A test that is ninety-nine percent accurate just came back positive…"
Copy: **Why a 99% accurate test is almost always wrong when it says yes** / sub: *base rates and the confidence illusion*

## B02 — STILL · ai · kenburns · ~10.0s  ← MEDIA SLOT (the only one)
Cue: "The disease is rare — one person in ten thousand…"
Slot: `media/B02.png`
t2i prompt: printed medical lab test result slip with a bold POSITIVE result line, pinned like a clipping to aged newsprint, desaturated flat print reproduction, editorial collage, no brand names
Synthetic — disclosure line in credits.

## B03 — DOCUMENT · own · highlight · ~8.5s
Cue: "Lock in a number before we count."
Quote card: **"Pick a number. Lock it in."** — *— before the counting starts*. Gold sweep on "Lock."

## B04 — GRAPHIC · own · manim · ~9.0s
Cue: "…take ten thousand people and simply count."
Manim: `TheCrowd` — 125×80 grid of 10,000 pale dots fills in row-chunks; exactly ONE turns blue and pulses.

## B05 — COMPOSITE · own · manim · ~6.5s
Cue: "…it catches that one person."
Manim: `OneCaught` — thin scan line sweeps once; blue flag chip "TRUE POSITIVE" plants by the blue dot. (No ring — the film's single ring is saved for B09.)

## B06 — GRAPHIC · own · manim · ~10.0s
Cue: "…wrong about one percent of the nine thousand nine hundred ninety-nine…"
Manim: `FalseAlarms` — exactly 100 scattered dots flip terracotta in one wave. 9,999 × 0.01 = 99.99 ≈ 100.

## B07 — GRAPHIC · own · manim · ~8.5s
Cue: "Now pull out everyone who tested positive."
Manim: `ThePool` — grid fades back; the 101 flagged dots migrate into a bucket and settle in tidy rows: 100 terracotta, 1 blue on top.

## B08 — DOCUMENT · own · ~8.0s
Cue: "…one in a hundred and one. About one percent."
Claim card: **≈1%** set enormous; attribution line: *1 true positive among 101 positive results*. No formula (card exclusion).

## B09 — COMPOSITE · own · manim · ~9.5s
Cue: "…nothing is broken."
Manim: `NothingBroken` — chips "99% accurate" (the box) and "≈1% sick" (the count); the film's ONE HandRing lands on the gap, timed to "orders."

## B10 — GRAPHIC · own · manim · ~9.5s
Cue: "Because you answered the wrong question."
Manim: `TwoQuestions` — two question cards: "right about the sick?" → 99 (blue) · "positive actually sick?" → ~1 (terracotta).

## B11 — GRAPHIC · own · manim · ~8.5s
Cue: "The bridge between them is the ingredient intuition always forgets…"
Manim: `TheBaseRate` — the 10,000 grid ghosts back at low opacity behind the chip "1 in 10,000 — the base rate"; the blue dot still burns through.

## B12 — CARD (endcard) · own · ~8.5s
Cue: "An honest test and a rare disease add up to a pile of false alarms…"
Copy: **The test is honest. Your intuition forgot the prior.** / sub: *from Computational Skepticism for AI — chapter 2*

---

## Slot inventory

| Slot | Need | From |
|---|---|---|
| `media/B02.png` | lab-result slip still | t2i prompt above (ai — disclosure) |

Eleven of twelve beats render now — this is the most Manim-native reel yet.
