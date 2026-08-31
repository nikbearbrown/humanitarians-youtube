# PROMPTS — *Nobody Is Coming to Approve It.*

GATE F expects beat-prefixed prompts for every open slot. **This reel has no
open slots** — every beat is rendered by the pipeline, and every terrain plate
is generated in-repo. Nothing to hand to a generation service, nothing to spend.

What follows is the two prompt-shaped artifacts the reel *contains*, the plate
recipe, and the scene briefs that stand in for generation prompts.

---

## The two on-screen prompts (content, not requests)

**B00 — the cold-open ask** (verbatim in `ClaudeComposerAsk`):

> A Mars rover gets one plan a sol and the round trip to Earth can be 44
> minutes. What is the actual method it uses to choose a route and a science
> target on its own, how good is it, and what does that autonomy cost?

**B12 — the handoff prompt** (read aloud verbatim, per HANDOFF LAW):

> I am designing a system that must make a judgement call before any human can
> review it, because review arrives too late to matter. Help me (1) write down
> the criteria it should apply, (2) decide how conservative it should be when
> the cost of being wrong is asymmetric, and (3) design how I would update those
> criteria once the system is deployed and hard to reach.

Rubric, on screen and spoken: are the **criteria** written down where a person
can argue with them · is the **conservatism** priced · is there a **route** to
change its mind after deployment.

That third item is the transferable lesson of the episode. A deployed judgement
that cannot be revised is not a finished system; it is a frozen one.

---

## The plate generation (in place of a stock / gen-AI request)

`assets/gen_mars.py` — run `python assets/gen_mars.py`. Deterministic; seeds are
listed in `SOURCES.md`. Every plate is built from a seeded procedural height
field and rendered as a monochrome camera frame under a low sun.

| Recipe | How |
|---|---|
| `_terrain` | fractal value noise for the ground, plus a second high-frequency octave for visible grit, plus irregular embossed caps for rocks (per-rock lobe noise, so they are not hemispheres) |
| `_shadow` | hard cast shadows, marched along the sun vector over the height field. This is what makes a rock read as an obstacle rather than a smudge — the first pass had no shadow term and every plate looked like grey bubbles in fog |
| `_to_plate` | maps luminance into a wide value range with real blacks. Deliberately **not** a flat mid-grey: GATE V measures the separation between mean ink luminance and the page, and Ep. 05 lost two passes to exactly that |
| `_cost_grid` | reduces the terrain to 40-px cells scored on step height + mean slope — the two quantities a traversability map actually carries |
| `_draw_cost` | paints the grid: cells under the traversable floor stay page-white, and darken with cost. A traversability map is mostly empty, and that emptiness is the point |
| `pathfan` | 96 drawn candidate arcs over a ~6 m horizon. **Feasible** = no cell crossed exceeds the clearance limit; among feasible, the winner is the one that reaches furthest forward. The rejected arcs run straight through obstacles on purpose — candidates are generated blind and the scoring is what throws them out |
| `rockfield` | one scene, three plates: the picture, the closed contours, the ranking. Detections are limited to rocks that are big, well separated, and far enough from the frame edge that their contour cannot be clipped |
| `route` | top-down boulder field with the straight line and the driven detour |

Three rendering passes were needed before these read (logged in `BUILD-LOG.md`):
the plates were shadowless and flat, the contours were drawn near-white and
vanished, and the path fan's first scoring rule picked a route that hugged
obstacles instead of threading the gap.

---

## Scene briefs (in place of generation prompts)

| Beat | Scene class | Brief |
|---|---|---|
| B01 | `B01_Presenter` | Name card. `OM MALI` large, terracotta hairline under it, role line beneath. Beside it two rows: "every episode so far: too much data" with a stack glyph, the row then **struck**; and "this one: too much distance" with a long gap glyph in the accented token. |
| B02 | `B02_OneBreath` | Kinetic type in three sets over a faint navcam plate. Set 1: ONE PLAN A DAY. Set 2: two chips — WHERE TO DRIVE, WHAT TO LOOK AT. Set 3: SCORED, NOT ASKED. Closer: nobody is coming to approve it. |
| B03 | `B03_LightTime` | Earth disc left, Mars disc right, a long channel between. A terracotta pulse crosses it under a bracket reading 3–22 MINUTES, ONE WAY; the return doubles the bracket to UP TO 44 FOR AN ANSWER. A struck joystick chip: NO REAL-TIME CONTROL. A sol bar: ONE COMMAND BLOCK, UPLINKED BEFORE THE ROVER WAKES. |
| B04 | `B04_WhatItSees` | The navcam plate left, captioned SYNTHETIC, with its stereo partner offset behind it. An arrow crosses to the cost grid, which draws on cell by cell. One cell is ringed terracotta and labelled STEP HEIGHT and SLOPE. Closer: one number per cell is the whole world. |
| B05 | `B05_TheFan` | The cost grid across the figure band, rover mark bottom-centre. The fan draws on under a ~1,700 PATHS chip and a 6 m horizon bracket. Rejected arcs stay grey under a REJECTED label; the survivors darken under a CLEARANCE CHECK chip; one arc turns terracotta with a ring on its waypoint. A closing chip: IT LOOKS WHILE IT DRIVES. |
| B06 | `B06_Aegis` | The rockfield plate, captioned SYNTHETIC, cross-fading to the contour version as six outlines close. Three measurement chips stagger beside it: SIZE, BRIGHTNESS, RANGE. A SCENE PROFILE card slides in. The ranked plate replaces the contour one; exactly one contour is terracotta. Closer: the laser fires without asking. |
| B07 | `B07_Snowdrift` | The route map, framed, captioned SCHEMATIC. The grey straight line labelled 520 m STRAIGHT ACROSS; the terracotta route labelled 759 m ACTUALLY DRIVEN. Two counters: 6 SOLS, ~12 SOLS SAVED. Closer: it went further to get there sooner. |
| B08 | `B08_TheProfile` | A document card centre: SCENE PROFILE, four rule lines typing in — prefer LARGE, prefer BRIGHT, prefer NEAR, prefer THIS OUTLINE. A signature line at the foot in the accented token: WRITTEN ON EARTH, BEFORE LAUNCH. An arrow carries the card across the light-time gap to the rover mark. Closer: the taste is a document, and it has an author. |
| B09 | `B09_Result` | Two autonomy bars — CURIOSITY 6.2%, PERSEVERANCE ~90% — with the sol condition. A distance rule beneath: 699.9 m, LONGEST DRIVE WITH NO HUMAN REVIEW. Then two AEGIS bars: >93% and ~20%, each labelled with its condition. The citation names both sources and says the two AEGIS figures come from different evaluations. |
| B10 | `B10_TwoLimits` | Left: the route map reduced; a terracotta bracket over the difference, labelled 239 m, and beneath it CAUTION, PAID IN METRES. Right: a sol axis with two ticks, SOL 442 and SOL 697, the span between them filled terracotta and reading 255 SOLS, labelled ONE DEFINITION OF INTERESTING, THEN THE NEXT. Closer: you can only change its mind on a mission clock. |
