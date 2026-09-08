# PEDAGOGY.md — What the Marks Weigh

Narration sign-off gate. `generate_audio_kokoro.py` refuses to run unless this
file reads **VERDICT: PASS**.

## Topic

How much information a Yoruba diacritic actually carries, measured in bits, and
why that measurement decides whether the problem needs a model at all.

## The ONE idea

The marks are not decoration, they are information, and information is
measurable. Knowing only the base letter, a mark costs 1.64 bits per character.
Knowing the whole word, 0.61 bits per word survive. That residue is precisely
what sentence context has to supply, and it is exactly the gap between a
frequency lookup table (77.1%) and a model that reads the sentence (92.4%).

Measure the problem before you model it.

## Learning objective

The viewer can state the method: before reaching for a model, quantify how much
ambiguity actually remains after the cheap baseline, and let that number decide
whether a model is warranted.

## Audience

The HAI channel audience: students and mid-career people getting proficient with
AI. No Yoruba required, no information theory required. Entropy is introduced as
"how many bits it costs to guess", which is all this video needs it to mean.

## Register check (Plain)

- Leads with method, not personality.
- States the decision trigger (B08: what the bits predicted about the baseline).
- States **where it fails** (B07: informal Yoruba, code switching, unseen names,
  tone confusions). Required by the register and present as a full beat.
- Narrated first person as Kehinde's own account of his own project.

## Teaching arc (nopunt whole-sheet checklist)

| Item | Beat | Status |
|---|---|---|
| Framework before examples | B02 the ambiguity, B03 the measurement | PASS |
| Worked example | B03/B04, real per-letter entropies from his corpus | PASS |
| Falsifiability | B06, three systems on the same held-out test split | PASS |
| Scaffolded viewer task | B09, run the same count on another writing system | PASS |
| Four bookends | B00 ask, B01 BLUF, B09 handoff, B10 outro | PASS |
| No source, no verdict | Every figure traces to SOURCES.md | PASS |

## Honesty check (DOUBLE-CHECK LAW)

Every number on screen comes from Kehinde's own repository and is reproducible
from it. The video does not claim state of the art, does not compare against
published systems it has not run, and states the licence-bound limits.

Two things the video is careful NOT to do:

- It does not present the lookup baseline as a strawman. The README records that
  an early `\w` regex bug quietly cost the baseline 16 points, that a test caught
  it, and that fixing it made the baseline *stronger*. The 77.1% quoted is the
  fixed, fair number.
- It does not claim the model understands Yoruba. B07 says plainly that it has
  learned the alphabet and that tone is still where it fails.

## Kehinde's HAI requirement

B00's first spoken words are the mandated opener, verbatim:
"Hi, I am Kehinde Obidele and this video is about ..."

## VERDICT: PASS

Signed: Kehinde Obidele, 2026-09-03
