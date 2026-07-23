# SHOTLIST — vox-ghost-jobs

**Why You Can Spot a Fake Job Without Reading It** · 16:9 · ~95s est. (11 beats)
Accents: dusty blue `#5B7B9C` = live/real · terracotta `#D35F43` = ghost/fake · gold `#F5D061` = editor's pen (once per graphic).
Hook stat: **81% of recruiters admit their employer posts ghost jobs** (MyPerfectResume, n=753 — verified; replaced the card's unverifiable "up to 42%", see FACTCHECK.md). Three fingerprints max on screen (card exclusion): stale clock · frozen siblings · cloned text.

Shot-type histogram: CARD 2 · STILL 1 · COMPOSITE 3 · DOCUMENT 1 · GRAPHIC 4 — max consecutive same-type: 2 (B05–B06). Lint: pass.

---

## B01 — CARD (title) · own · ~10.8s
Cue: "Eighty-one percent of recruiters admit it…"
Copy: **Why you can spot a fake job without reading it** / sub: *ghost postings, scored like spam*

## B02 — STILL · ai · kenburns · ~10.8s  ← MEDIA SLOT
Cue: "A ghost posting isn't a job that fell through…"
Slot: `media/B02.png`
t2i prompt: printed screenshot of a polished corporate job posting page with a prominent apply button, pinned like a clipping to aged newsprint, desaturated flat print reproduction, editorial collage
Synthetic — disclosure line in credits.

## B03 — COMPOSITE · ai · hold · ~8.0s  ← MEDIA SLOT (derive from B02, no new gen)
Cue: "From the outside it reads exactly like a real one."
Slot: `media/B03.png` — duplicate/crop B02's clipping into two identical pinned twins.
Annotation (assembly plane): charcoal serif label "one of these is real" timed to "exactly."

## B04 — DOCUMENT · own · highlight · ~8.8s
Cue: "…a machine you already trust… your spam filter."
Quote card: **"Sent at 3 a.m. Ten thousand copies. No replies."** — *— what a spam filter actually reads*. Gold sweep on "reads."

## B05 — GRAPHIC · own · manim · ~8.4s
Cue: "It doesn't judge what the mail says."
Manim: `SpamMeter` — envelope + vertical meter; three terracotta ticks land, fill steps down into the spam zone, SPAM chip. No probabilities printed.

## B06 — GRAPHIC · own · manim · ~6.0s — fingerprint 1/3
Cue: "A stale clock: up eleven weeks, never once updated."
Manim: `StaleClock` — posting card + liveness meter (high, blue); STALE CLOCK stamp slaps on; meter drops one step.

## B07 — COMPOSITE · own · manim · ~6.0s — fingerprint 2/3
Cue: "Frozen siblings: ten other roles…"
Manim: `FrozenSiblings` — greyed sibling mini-cards fade in beneath; FROZEN SIBLINGS stamp; meter crosses the midline and turns terracotta.

## B08 — GRAPHIC · own · manim · ~6.4s — fingerprint 3/3
Cue: "Cloned text: the same description, word for word…"
Manim: `ClonedText` — carbon-copy duplicate slides out from behind the card; CLONED TEXT stamp; meter deep in ghost zone. No fourth signal (card exclusion).

## B09 — COMPOSITE · own · manim · ~10.0s
Cue: "No single stamp is decisive… but the stamps accumulate…"
Manim: `AccumulateRing` — B08 end-state rebuilt; HandRing (terracotta) around the METER on "accumulate." One ring only.

## B10 — GRAPHIC · own · manim · ~8.8s
Cue: "The same company, the same title, can score opposite ways."
Manim: `TwoDoors` — two cards, same title chip; left meter fills blue → LIVE chip; right drains terracotta → GHOST chip.

## B11 — CARD (endcard) · own · ~8.0s
Cue: "The score is a probability, not a verdict…" (the ONE closing caveat line — card exclusion)
Copy: **A posting is a signal — signals can lie.** / sub: *from The Reallocation Engine — chapter 8*

---

## Slot inventory (fill later, any order; rerun vox_run after each drop)

| Slot | Need | From |
|---|---|---|
| `media/B02.png` | pristine posting clipping | t2i prompt above (ai — disclosure) |
| `media/B03.png` | two identical twins of B02 | derive locally from B02.png, no spend |

Everything else is CARD / DOCUMENT / GRAPHIC — no media generation needed for the slate cut.
