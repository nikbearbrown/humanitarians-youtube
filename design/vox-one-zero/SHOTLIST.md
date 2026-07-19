# SHOTLIST — vox-one-zero

**Why One Zero Beats Four Nines** · 16:9 · ~104s est. (11 beats)
Accents: dusty navy `#3D5A80` = the flow / healthy factor / Apply · crimson `#BF3339` = the closed valve / the zero / Skip · gold `#F5D061` = editor's pen (once per graphic).
Source: chapter 11. Hero object: a score pipeline — two votes sum into a flow that must pass two inline valves (is-it-real, can-you-start) before Apply/Skip (manim move: collapse).
Card exclusions honored: **no full composite formula or weight values** (no 0.35/0.30) · **no Bayesian terminology** · no threshold-tuning (a cutoff line, no number) · no Eightfold-lawsuit · **no visa-law specifics** (universal framing). The gate-vs-vote arithmetic is the whole film.
On-screen contrast numbers (0.9s + a 0; averaged ~0.68 vs multiplied 0) are **illustrative**, not the scorer's real weights.

Shot-type histogram: CARD 2 · STILL 1 · GRAPHIC 4 · COMPOSITE 3 · DOCUMENT 1 — max consecutive same-type: 2 (B03–B04). Lint: pass.

---

## B01 — CARD (title) · own · ~10.0s
Cue: "A job can score ninety-five percent… and still be worth exactly zero."
Copy: **Why one zero beats four nines** / sub: *gates, not votes*

## B02 — STILL · ai · kenburns · ~9.5s  ← MEDIA SLOT (the only generated plate)
Cue: "Here's a role that looks perfect…"
Slot: `media/B02.png`
t2i prompt: printed screenshot of a polished corporate job posting at a prestigious company, a prominent green '95% match' badge, clean UI, pinned like a clipping to aged newsprint, desaturated flat print reproduction, editorial collage
Synthetic — disclosure line in credits. `shot.focus` on the badge.

## B03 — GRAPHIC · own · manim · ~9.5s
Cue: "Some are votes — how well you fit, whether they can even hire you."
Manim: `B03_Votes` — two navy vote bars ("fit", "can they hire you") grow, a plus between, merge into one navy flow arrow. Votes = addends. No weight values.

## B04 — GRAPHIC · own · manim · ~10.0s
Cue: "But two of the parts aren't votes at all. They're gates."
Manim: `B04_Valves` — the navy flow passes through two inline valve rings ("is it real?", "can you start?"), both open, reaching an "Apply" node. Universal framing.

## B05 — COMPOSITE · own · manim · ~10.0s — THE COLLAPSE
Cue: "A gate doesn't subtract — it multiplies… It collapses to zero."
Manim: `B05_Collapse` — full navy flow hits the "can you start?" valve; valve turns crimson and shuts; downstream flow drops to a flat zero; crimson "x0" stamp; node flips Apply → Skip. The heart of the film.

## B06 — GRAPHIC · own · manim · ~10.0s
Cue: "Average everything instead… it barely dents the score."
Manim: `B06_AverageDilutes` — four navy ~0.9 bars + one crimson zero; an "average" arrow collapses them to one bar staying high (~0.68) ABOVE a dashed apply line; label "still looks like apply." Illustrative numbers.

## B07 — COMPOSITE · own · manim · ~9.5s
Cue: "Same zero, two different fates…"
Manim: `B07_TwoFates` — left "averaged" bar high above the apply line (crimson HandRing — "hides"); right "multiplied" bar flat at zero (navy — honest); labels "go" vs "stop."

## B08 — DOCUMENT · own · highlight · ~9.0s
Cue: "A perfect job you can't start is worth nothing at all."
Quote card: **"A job you can't start is worth nothing."** — *— what the gate knows and the average forgets*. Gold sweep on "nothing."

## B09 — COMPOSITE · own · manim · ~10.0s
Cue: "…jobs the calendar already killed."
Manim: `B09_CalendarKilled` — a calendar with a crimson X on a passed date; navy envelopes fly at a shut crimson door and pile unopened; label "already closed."

## B10 — GRAPHIC · own · manim · ~9.5s
Cue: "So never average a gate… One stays shut, and the answer is zero."
Manim: `B10_TheRule` — two mini pipelines: top both valves open → navy flow → "Apply"; bottom one valve shut crimson → flat zero → "Skip"; label "every valve, or zero."

## B11 — CARD (endcard) · own · ~8.0s
Cue: "Nines and a zero. Multiply, and the zero always wins."
Copy: **Nines and a zero — multiply, and zero wins.** / sub: *from The Reallocation Engine — chapter 11*

---

## Slot inventory (fill later, any order; rerun vox_run after each drop)

| Slot | Need | From |
|---|---|---|
| `media/B02.png` | the perfect-looking "95% match" job posting | t2i prompt above (ai — disclosure) |

Everything else is CARD / DOCUMENT / GRAPHIC / COMPOSITE-manim — no media generation needed for the slate cut.
