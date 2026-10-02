# PROMPTS — *Nothing Left To Remove.*

Ep. 11 · `generative-spacecraft-design`

**No image-generation prompts exist for this reel, and that is not an
omission.** REBUILD LAW requires every figure to be a native animated
graphic; nothing here is a generated still, a stock image, a photograph, or a
traced outline of a real part. There is no FLUX prompt, no nano-banana prompt,
no pantry request, and no step that could spend money.

What stands in place of image prompts:

| Beat | Visual | Where it comes from |
|---|---|---|
| B01, B02 | kinetic type, cards, rules | drawn in `scenes.py` |
| B03 | bracket silhouette + mass bar | isotype drawn in `scenes.py`; the two masses are ESA's published figures |
| B04 | `domain.png` | `assets/gen_struct.py` |
| B05 | `evolve.png` | real SIMP iterates, `assets/topo.py` |
| B06 | `shapes.png` / `shapes_v.png` | the optimiser's output and an equal-mass plate |
| B07 | `paths.png` | elastic strain-energy density from the FE solve |
| B08 | `damage.png` / `damage_v.png` | the same design with an 8×8 void punched at the worst location |
| B10 | `price.png` | measured compliance against mass budget |
| B00, B11, B12, B13 | Claude UI | shipped Remotion compositions, props in `beat_sheet.json` |

---

## The two prompts that ARE in the reel

These are on screen, spoken, and are the point of their beats.

### B00 — the cold-open ask

> Generative design software is given a volume, some loads and a mass budget,
> and it returns a part lighter and stiffer than a person would draw. What is
> it actually optimising, and what does that leave out?

`runningText`: `solving 7,200 elements, 90 iterations...`

Result lines, which land answered (COLD OPEN LAW — the ask is never left
hanging):

- it works - same mass, 23% stiffer than a machined plate
- the catch - the optimum keeps no spare load path
- one small void in the worst place: 31x softer

### B12 — the handoff (HANDOFF LAW)

Greeting fixed to `Your turn.`, `runningText`: `paste this into Claude...`

> Here is exactly what I asked my model to optimise. Tell me what I left out
> of the objective, what failure that omission makes invisible, and the
> cheapest change to the objective that would catch it.

Grading lines on screen:

- grade it: does it name a failure the metric cannot see
- grade it: does it price the fix, not just demand it
- grade it: would the fix have changed your last decision

**The prompt is read aloud verbatim and then discussed**, per HANDOFF LAW —
B12's narration reads it, then tells the viewer to run it on something they
have already shipped. A handoff where the prompt only appears on screen is a
defect.

Why this prompt and not "learn more about generative design": the episode's
transferable habit is reading your own objective for what it omits, and that
only lands if the viewer applies it to an objective they actually own. The
third grading line is the one that makes it bite — an omission that would not
have changed any decision is not worth the mass.

---

## Verdict artefact lines (B11, on screen)

Five lines, not four. A four-line `ClaudeVerdictArtifact` card sits almost
exactly on GATE V's bbox-fill floor and the verdict flips on encoder noise
(logged in Ep. 10). Five also lets the card carry the price, which the recap
should: an episode whose honesty rests on quantifying the cost must quantify
it on the page a viewer can pause.

1. Give it a volume, the loads and a mass budget and it returns a shape no
   engineer would draw.
2. It is genuinely better: at the same mass, 23% stiffer than a plate
   machined to fit.
3. It got there by deleting everything that was not carrying the load you
   specified — including the second load path.
4. One void in the worst place costs the plate 20% and the optimised bracket
   31 times.
5. Ask for damage tolerance and you get it back, for a third of the mass you
   just saved.

---

## Greeting

`Ola, HAI` — SKILL.md limits the HAI persona to the shortest forms (Hi · Ola ·
Hej · Ciao). All four are in use, so the lexicon cycles least-recently-used
first: Hej (03), Ciao (04), Ola (05), Hi (08), Hej (09), Ciao (10). Least
recently used is Ola, last seen at Ep. 05.
