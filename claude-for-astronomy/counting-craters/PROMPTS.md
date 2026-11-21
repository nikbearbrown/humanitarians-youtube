# PROMPTS — Ep. 18, *counting-craters*

Beat-prefixed prompts for every slot that a human or a generator fills. This
reel has **no open slots**: every beat is generated deterministically by this
repo. The prompts below are therefore the *generation* prompts — what each
asset was asked to be — kept so the reel can be rebuilt from scratch.

No paid API is involved anywhere in this list. Spend: **$0.00**.

---

## B00 — cold open, `ClaudeComposerAsk`

> Composer on the cream stage. Greeting `Ciao, HAI`. Type the ask:
> *"Nobody has visited most of the Moon or Mars. We still quote their surface
> ages in billions of years. Where does that number actually come from?"*
> Running text `counting craters on ground nobody has sampled...`. Three
> output lines, landing in order, the third carrying the whole episode:
> *"AI can do the counting. It cannot move the curve."*
> Footer chip `@HumanitariansAI` — **set explicitly; the schema default is
> `@NikBearBrown`.**

## B01 — `B01_Presenter`

> Name card. OM MALI writes in with a terracotta hairline beneath; role line
> *Humanitarians AI — presenter*. **Reveal the series line and the corner bug
> early**, not last, so the lower band is never empty mid-beat. Then a card
> draws and splits down a centre rule: left half terracotta, *COUNTING / AI
> owns this*; right half ink, *THE NUMBER / it does not*.

## B02 — `B02_OneBreath`

> The BLUF card. Three lines type on: *MORE CRATERS MEANS OLDER GROUND* (sub:
> density is the measurement) · *YEARS NEED A CURVE* (sub: and the curve needs
> dated rocks) · *ONLY A ROCK MOVES THE CURVE*, accented and underlined.
> Closer: *a better counter only moves the measurement*.

## B03 — `B03_TheRule` + `surface.png`

> Two patches of synthetic ground, side by side, same area and same
> instrument. Fade both up together, then label: *1.0 Ga* with a counter
> running to **14**, then *3.5 Ga* with a counter running to **80** — and let
> the second counter visibly take longer to climb. Closer frames the episode
> against Ep. 08: *every crater here is already on the ground*.

## B04 — `B04_ThePile` + `pile.png`

> Three populations as bars on a **log** axis. Place a *×10 per rail* note
> under the axis immediately — without it the bars read as linear and the
> automation gap looks like 4× instead of 78×. Label rows: *7,048 — the
> training set*; *384,343 — catalogued BY HAND*; *~10 million+ — 10 m to 1 km
> on Mars*. Accent the third on "hands stop here".

## B05 — `B05_TheDisagreement` + `spread.png`

> One patch of ground, craters drawn two ways. Land **±45%** large beside it
> with a small citation: *Robbins et al. 2014*. Then the legend, which teaches
> the fill convention in-beat: *FILLED = every analyst marked it* /
> *OPEN = contested*. Closer: *the disagreement is all in the small ones*.

## B06 — `B06_TheMachine` (no plate — this beat is numbers)

> Two bars, no imagery. Bar one grows to **92%** and holds: *recall, AFTER
> post-processing*. Bar two grows to **57%** beneath it, ghosted but legible:
> *the raw network*. **The second bar is not optional** — the headline recall
> must not stand alone. Then **42% of what it returned was NEW**, in the
> accent. Closer: *this half is perception — and perception is AI's*.

## B07 — `B07_TheCurve` + `curve.png`

> The chronology function. Axis labels go **outside** the plate: *craters per
> km² (log)* and *age, billions of years*. Bracket the long flat middle — *a
> slow, steady clock* — then bracket the steep old end — *the early
> bombardment*. Land **96%** in the accent against the steep end, with the
> surface labelled *4.1 Ga* so the number is never floating free.

## B08 — `B08_WhatItCosts` + `cost.png`

> The money beat. Curve above with the ±45% band passing through it; the two
> relative bars below. Call out the 3.5 Ga bar: **16% of the answer**. Then
> the 1.0 Ga bar, in the accent: **90%**. Land a note beneath both: *the SAME
> counting error, both times*. Closer: *consistency buys the most on young
> ground*.

## B09 — `B09_TheGap` + `anchors.png`

> The calibration record on a time axis, labelled outside the plate. Label the
> old cluster *Apollo + Luna*, the young cluster *a few dated craters*, then
> the empty middle in the accent: **1 – 3 Ga, NO ANCHOR**. The Chang'e-5
> marker lands in the hole last.

## B10 — `B10_TheTell` (type only)

> A wide terracotta bar draws: *the counted window, 1,400 Myr*. It **collapses**
> to a single ink tick: *the rock, 8 Myr*. The ratio lands between them:
> **175× tighter**. Then the counterweight types in beneath, ghosted but
> readable — *the new anchor moved the curve by at most 0.24 Gyr* — because
> the weaker reading of my own evidence ships as a beat. Closer, accented:
> *not wrong — loose*.

## B11 — verdict, `ClaudeVerdictArtifact`

> Artifact page, heading *When not to learn it*, five lines. **Props are
> `artifactTitle` / `artifactHeading` / `artifactLines`** — this component has
> no `title`, no `rows`, and no `folderLabel`; an unknown key is dropped by
> zod and the component renders its own demo card instead.

## B12 — handoff, `ClaudeComposerAsk`

> Greeting fixed to `Your turn.` The prompt types itself while the narration
> reads it aloud and then discusses it:
> *"Take a measurement I trust in my own work. Separate what is MEASURED from
> what it is CALIBRATED AGAINST, and tell me which of the two I have never
> checked."*
> Two output lines tell the viewer what to look for in the answer. Footer chip
> `@HumanitariansAI`, set explicitly.

## B13 — outro, `ClaudeTitleOutro`

> Poster restate: **The Clock Needs a Rock.** with the terracotta period,
> `handle: @HumanitariansAI`, `subline: Claude for Astronomy - Ep. 18`.
> **Props are `title` / `handle` / `subline`** — not `subtitle`, not
> `folderLabel`.

---

## Plate generation

> `python -I assets/gen_craters.py`
>
> Re-derive every number the narration speaks; assert nine of them; write six
> plates carrying imagery only. Seeded 1801–1804. Fail loudly and write
> nothing if any assertion breaks.
