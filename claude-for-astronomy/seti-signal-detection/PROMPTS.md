# PROMPTS — *The Signal We Imagined.*

Ep. 13 · `seti-signal-detection`

**No image-generation prompts exist for this reel, and that is not an
omission.** REBUILD LAW requires every figure to be a native animated
graphic; nothing here is a generated still, a stock image, a telescope
photograph, or a redrawn published spectrogram. There is no FLUX prompt, no
nano-banana prompt, no pantry request, and no step that could spend money.

| Beat | Visual | Where it comes from |
|---|---|---|
| B01, B02 | kinetic type, cards, rules | drawn in `scenes.py` |
| B03 | a frequency axis, one tone, 26 look-alikes | drawn in `scenes.py`; the counts and the verdict are Sheikh et al.'s |
| B04 | `waterfall.png` | `assets/gen_seti.py` |
| B05 | the fan of trial tracks | drawn natively in `scenes.py`, so it sweeps on the spoken phrase |
| B06 | `three.png` / `three_v.png` | the same field under three hypotheses |
| B07 | `recall.png` | measured recall, 80 trials per hypothesis |
| B08 | `edge.png` | the control sweep |
| B09 | `cadence.png` | six integrated spectra at the candidate's own drift rate |
| B10 | `compare.png` | morphology against cadence |
| B00, B11, B12, B13 | Claude UI | shipped Remotion compositions, props in `beat_sheet.json` |

**BLC1 is an isotype, never a spectrogram.** One terracotta tone on a
frequency axis, then twenty-six ink tones around it. Reproducing the paper's
own figure would be a lifted image, and a photograph of Parkes would be
decoration — the beat is about the *population*, which is what the drawing
shows.

---

## The two prompts that ARE in the reel

### B00 — the cold-open ask

> SETI pipelines sift radio data for narrowband signals and now use deep
> learning to do it. What exactly are they trained to recognise, given that
> nobody has ever detected one?

`runningText`: `sweeping 49 drift rates across 512 channels...`

Result lines, which land answered (COLD OPEN LAW):

- the search assumes a form - the range of drift rates is the assumption
- a transmitter that corrects its own drift: found 0 times in 80
- the test that catches it asks WHERE, not WHAT

### B12 — the handoff (HANDOFF LAW)

Greeting fixed to `Your turn.`, `runningText`: `paste this into Claude...`

> Here is exactly what my detector was trained to recognise. Tell me what it
> would miss, and design a test that would catch that without me having to
> guess the right form first.

Grading lines on screen:

- grade it: does it name something OUTSIDE the training form
- grade it: is the test independent of appearance
- grade it: could you run it with the data you already have

**The prompt is read aloud verbatim and then discussed**, per HANDOFF LAW.

Why this prompt: the transferable move is not "be sceptical of your model",
it is **asking for a test that does not reference your hypothesis**. The
second grading line is the one that bites — an answer that proposes a better
classifier has not understood the question, because a better classifier is
still a guess about form. The cadence test works because it asks where a
signal came from, and that question has the same answer whatever the signal
looks like.

---

## Verdict artefact lines (B11, on screen)

Five lines, not four. A four-line `ClaudeVerdictArtifact` card sits almost
exactly on GATE V's bbox-fill floor and the verdict flips on encoder noise
(logged in Ep. 10).

1. Nobody has ever detected a radio technosignature, so the positive class
   is hypothetical.
2. To build a search you assume a form — and the range of drift rates you
   sweep IS that assumption.
3. A transmitter that corrects its own Doppler, which is what we do for
   spacecraft, was found 0 times in 80.
4. Widen the search by one number and it is found 80 times in 80. The blind
   spot was the parameter.
5. The test that escapes this asks where a signal came from, not what it
   looks like.

---

## Greeting

`Hej, HAI` — SKILL.md limits the HAI persona to the shortest forms (Hi · Ola ·
Hej · Ciao). The lexicon cycles least-recently-used first: Hej (03), Ciao
(04), Ola (05), Hi (08), Hej (09), Ciao (10), Ola (11), Hi (12). Least
recently used is Hej, last seen at Ep. 09.
