# PROMPTS — *What The Model Would Say.*

Ep. 14 · `stellar-spectra-labels`

---

## No image-generation prompts were used. $0.00.

Every visual in this reel is either **computed** or **drawn**:

| Visual | Where it comes from |
|---|---|
| The six plates | `assets/gen_stars.py` — matplotlib-free PIL drawing over the real experiment's output arrays |
| Everything else in B01–B10 | `scenes.py` — Manim CE primitives (text, rules, cards, dots, arrows, brackets) |
| B00, B11, B12, B13 | Remotion compositions from `proven-core` (`ClaudeComposerAsk`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`) |
| Narration | Kokoro TTS `af_bella`, local |

There is no FLUX, nano-banana, DALL·E, Midjourney or any other image model in
this reel's build, and no ElevenLabs. **Fellow Tier: no API keys, no spend.**

This is not an accident of this episode — it is the toolkit rule. If a Fellow
Tier step ever appears to need a key or a paid service, that is a bug in the
toolkit, not a missing credential.

---

## The prompts that DO appear — as reel content

Two beats put a prompt on screen. They are content, not build inputs: nothing
was sent to any model to produce them, and the "output" lines beneath them are
the reel's own findings, typeset to look like a session.

### B00 — the opening ask

> Data-driven models read stellar spectra and return temperature, gravity and
> composition, far faster than fitting physics. What are they actually trained
> on, and does the quoted precision mean the answer is right?

Runner line: `fitting 160 pixels against 500 labelled stars...`

Result lines:
- `it has no physics in it - only the labels it was given`
- `it agrees with those labels to 0.03 dex`
- `against the truth: 0.13 dex, and the error is a straight line`

### B12 — the handoff, for the viewer to actually run

> Here is where my training labels came from. Tell me what systematics they
> inherit from whatever produced them, and what I could measure in a
> completely different way to check the scale.

Grading lines shown beneath it:
- `grade it: does it trace the labels back to THEIR source`
- `grade it: does it name a check that shares no assumptions`
- `grade it: does it distinguish precision from accuracy`

This is the one prompt in the reel meant to leave the reel. It is written to
be pasted into Claude alongside a real project's label provenance, and the
three grading lines are what a good answer has to do.

---

## Reproducing the visuals

```bash
# the plates — runs the real experiment, asserts all three claims,
# writes nothing if any of them fails
.venv/Scripts/python.exe -I assets/gen_stars.py

# the scenes — never hand-roll npx remotion render
.venv/Scripts/python.exe -I <art>/runtime/scripts/remotion_scenes.py <reel>
```

Seed **1414**, fixed and logged in SOURCES.md. The line bank that defines
"nature" is drawn once from a frozen seed, so the star-to-spectrum function is
identical on every run.
