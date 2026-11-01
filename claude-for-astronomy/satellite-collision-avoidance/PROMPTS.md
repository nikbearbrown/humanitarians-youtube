# PROMPTS — *Safer By Not Looking.*

Ep. 15 · `satellite-collision-avoidance` · the series finale

---

## No image-generation prompts were used. $0.00.

Every visual in this reel is either **computed** or **drawn**:

| Visual | Where it comes from |
|---|---|
| The six plates | `assets/gen_conj.py` — matplotlib-free PIL drawing over the real experiment's output arrays |
| Everything else in B01–B10 | `scenes.py` — Manim CE primitives (text, rules, cards, dot fields, bars) |
| B00, B11, B12, B13 | Remotion compositions from `proven-core` |
| Narration | Kokoro TTS `af_bella`, local |

No FLUX, no nano-banana, no DALL·E, no Midjourney, no ElevenLabs.
**Fellow Tier: no API keys, no spend.**

This is the toolkit rule, not an accident of this episode. If a Fellow Tier
step ever appears to need a key or a paid service, that is a bug in the
toolkit, not a missing credential.

---

## The prompts that DO appear — as reel content

Two beats put a prompt on screen. They are content, not build inputs: nothing
was sent to any model to produce them, and the "output" lines beneath them
are the reel's own findings, typeset to look like a session.

### B00 — the opening ask

> Operators screen thousands of close approaches a week and act when the
> collision probability crosses a threshold. What is that probability
> actually a probability of, and can it be moved without moving the
> satellites?

Runner line: `integrating the encounter plane over 120,000 conjunctions...`

Result lines:
- `it is not P(collision) - it is P(collision | your covariance)`
- `inflate the covariance 7x and the alert drops below threshold`
- `and the score prefers the model that misses the dangerous ones`

### B12 — the handoff, for the viewer to actually run

> Here is my risk metric and the set I evaluate it on. Tell me what I could
> do to the INPUTS to make the number look better without making anything
> safer — and what I should score instead.

Grading lines shown beneath it:
- `grade it: does it find a way to game the metric`
- `grade it: does it separate the aggregate from what matters`
- `grade it: does it name a quantity you cannot flatter`

This is the one prompt meant to leave the reel. It is written to be pasted
into Claude alongside a real project's risk metric and evaluation set, and
the three grading lines are what a good answer has to do.

It is also the series' closing question. Fifteen episodes asked *where did
this answer come from*; this one asks the version you can run on your own
work tomorrow.

---

## Reproducing the visuals

```bash
# the plates — runs the real collision-probability integral, asserts four
# claims, writes nothing if any of them fails
.venv/Scripts/python.exe -I assets/gen_conj.py

# the scenes — never hand-roll npx remotion render
.venv/Scripts/python.exe -I <art>/runtime/scripts/remotion_scenes.py <reel>
```

Seed **1515**, fixed and logged in SOURCES.md.
