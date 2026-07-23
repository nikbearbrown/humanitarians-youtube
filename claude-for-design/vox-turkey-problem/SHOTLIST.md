# SHOTLIST — vox-turkey-problem

**Why the Turkey's Model Was Perfect Until Thanksgiving** · 16:9 · ~103s est. (11 beats)
Accents: terracotta `#D35F43` = confidence, the model's picture built from its data · dusty blue `#5B7B9C` = the world / the true risk · gold `#F5D061` unused this film (both quotes wrap — no sweeps, Gate B lesson).
Source: *Computational Skepticism for AI*, ch. 14 (Limit 3: the data-world gap; Taleb's turkey problem, *The Black Swan* 2007).
Card exclusions: no Mediocristan/Extremistan taxonomy · no Hume/induction history · no distribution-shift formalism · no medical-AI second example — one turkey, one curve, one cliff.
One HandRing: B05, on the confidence peak.

Shot-type histogram: CARD 2 · STILL 1 · GRAPHIC 5 · DOCUMENT 2 · COMPOSITE 1 — max consecutive: 2. Motion: hold 4 · kenburns 1 · isotype 2 · drawon 3 · annotate 1 — max 36%. Lint: pass.

---

## B01 — CARD (title) · own · ~8.0s
Copy: **The turkey's model was perfect — until Thanksgiving** / sub: *the limits of AI*

## B02 — STILL · ai · kenburns · ~9.5s  ← MEDIA SLOT (the only one)
Slot: `media/B02.png`
t2i prompt: archival farm photograph, a single turkey in a farmyard at morning feeding time, scattered grain on the ground, a hand offering feed at the frame edge, desaturated flat print reproduction pinned like a clipping to aged newsprint, editorial paper collage, no readable text
Synthetic — disclosure in credits. (Archive alternative, free: LOC Free-to-Use / Smithsonian Open Access / Wikimedia Commons — queries: "turkey farm feeding photograph", "poultry farm 1930s", "Thanksgiving turkey farm historic". Drop as `media/B02.png` + `B02.source.txt`.)

## B03 — GRAPHIC · own · isotype · ~10.0s
Manim: `FeedingDays` — square day-marks fill in reading order, mono counter climbs to 1,000; declared unit chip "■ = 10 mornings" (100 marks); serif model-card above: "the model: the human cares about my welfare."

## B04 — GRAPHIC · own · drawon · ~10.0s
Manim: `ConfidenceCurve` — zero-based axes (days 0–1,000 × confidence); terracotta curve draws on, rising monotonically. Labels float clear of strokes with tick connectors.

## B05 — COMPOSITE · own · annotate · ~9.5s
Manim: `DayThousand` — the curve persists; the film's ONE HandRing lands on the peak at day 1,000, timed to "maximum"; LabelChip beneath: "day 1,000 — the day before Thanksgiving."

## B06 — GRAPHIC · own · drawon · ~9.5s
Manim: `TheCliff` — the curve extends one day past the ringed peak and drops vertically to zero. Label "day 1,001" floated clear of the drop. Drawn fast — an event, not a decay.

## B07 — DOCUMENT · own · hold · ~9.0s
Quote card: **"the feeling of safety reached its maximum when the risk was at the highest"** — *Nassim Nicholas Taleb, The Black Swan (2007)*. Wrapped lines → no gold sweep. Fragment of "Consider that the feeling of safety reached its maximum when the risk was at the highest!" — verified via secondary sources (FACTCHECK.md); confirm against print before publication.

## B08 — GRAPHIC · own · isotype · ~10.0s
Manim: `RoutineCases` — dusty-blue case grid, declared unit chip "■ = 100 cases" (100 marks = 10,000); chip "99.7% accurate"; one empty outlined slot OUTSIDE the grid frame: "the case that ends the regime — not in the data."

## B09 — GRAPHIC · own · drawon · ~10.0s
Manim: `TheGap` — terracotta confidence line climbs; flat dusty-blue line above it, "the world's risk — never moved." The gap closes as belief climbs toward a risk it cannot see. Labels clear of both strokes.

## B10 — DOCUMENT · own · hold · ~9.0s
Quote card: **"The system's competence is over the data, not the world."** — *Computational Skepticism for AI, chapter 14*. Wraps to two lines → no gold sweep.

## B11 — CARD (endcard) · own · ~8.4s
Copy: **The data is always less than the world.** / sub: *from Computational Skepticism for AI — chapter 14*

---

## Slot inventory

| Slot | Need | From |
|---|---|---|
| `media/B02.png` | farmyard turkey still | t2i prompt above (ai — disclosure) or archive queries above (free) |

Ten of eleven beats render now.
