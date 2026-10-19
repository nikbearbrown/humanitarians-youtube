/ PEDAGOGY — *The Signal We Imagined.*

**GATE P.** A human reads the narration below and signs. Audio is not
generated until the verdict line below is changed from PENDING to a pass.
Kokoro is local and free, so this gate protects quality, never spend.

> Note for anyone editing this file: `generate_audio_kokoro.py` opens GATE P on
> a plain substring match anywhere in this document, so do **not** write the
> passing verdict string in prose — spelling it out in an explanatory sentence
> silently unlocks the gate. That is why this paragraph describes it instead of
> quoting it.

**VERDICT: PASSED**

Signed: Om Mali  Date: 10/16/26

---

## Written to a length

| | words | predicted | measured |
|---|---|---|---|
| Ep. 10 | 429 | 2:41.0 | 2:27.7 |
| Ep. 11 | 419 | 2:24.3 | 2:29.0 |
| Ep. 12 | 400 | 2:22.2 | 2:22.1 |
| **Ep. 13** | **420** | **2:29.2** | **2:21.5** |

Margin ~31 s. The words-only model is noise of order ±5–10% **with no
consistent sign** — Ep. 06 +10.4%, 07 −0.4%, 08 −5.0%, 09 +2.7%, 10 −8.2%,
11 +3.3%, 12 −0.1%. The rate used is Ep. 12's measured 0.3553 s/word. Even at
the slowest rate in the series this lands at 2:37. If the measured total
somehow exceeds 3:00 the fix is `--speed`, not a rewrite of signed narration.

**Measured after the gate: 2:21.5**, 38 s under the cap, so no `--speed` was
needed. Model error **−5.1%**. The eight-episode range is now +10.4% to
−8.2%, still with no consistent sign.

## What this episode teaches, and why it is worth an episode

Topic 13 in the brief is "how AI separates potential alien signals from human
radio interference". The obvious version is a detective story: here is the
noise, here is the clever filter, here is the candidate. That version is true
and it skips the only hard part.

The hard part is that **this is the first episode in the series where the
positive class does not exist.** Every earlier limit lived in something you
could in principle inspect: a biased training set, an under-specified
objective, a leaky split. Here there is no training set to be biased, no test
set to leak, and nothing to validate against, because **nobody has ever
observed the thing being searched for.** That is not my framing. It is the
stated motivation of the field's own simulation toolkit:

> "Given that we have not yet detected a radio SETI signal, we must make
> assumptions about their form"
> — Brzycki et al. 2022, *AJ*

So I built the real search and measured what the assumption costs.

The detector is not a stand-in: it computes the de-Doppler statistic a radio
technosignature pipeline actually computes — sum the dynamic spectrum along a
straight track, once per trial drift rate, keep the best. That matters,
because it makes the assumption a single visible number: **the range of drift
rates you sweep.**

- A signal drifting the way searches assume: found **80 times in 80**.
- A signal from a transmitter that **corrects its own Doppler** — which is
  exactly what we do for our own spacecraft — found **0 times in 80**. Not
  rarely. Never. It is not missed; it is never looked for.
- Widen the sweep by one number so it includes zero drift, and the same
  signal is found **80 times in 80**.
- A pulsed beacon, whose drift *is* searched, is found **0.70** of the time,
  because the search also assumes it is on continuously. A second assumption,
  a different mechanism.
- The control locates the blind spot exactly: sweep the search's lower limit
  and recall falls from 1.00 to 0.00 between **0.06 and 0.12 Hz/s**. A cliff,
  not a slope.

And the escape is the test the field already uses, and the one that actually
settled BLC1: point at the star, look away, point back. A source on the sky
comes and goes with the telescope; interference does not care where you
point. That test scores **0.76** on the signal the morphology search scores
**zero** on, because it asks *where a signal came from*, not what it looks
like.

The series pivot is stated at B01: twelve episodes of AI looking at things
that exist; this one is about looking for something nobody has ever found.

## The narration, beat by beat

**B00 — cold open** (28 words)
> Hi, I'm Om Mali. This video is about how we search for alien radio signals,
> and why the thing we are searching for is something we made up.

**B01 — presenter** (20 words)
> Twelve episodes of AI looking at things that exist. This one is about
> looking for something nobody has ever found.

**B02 — the whole idea in one breath** (29 words)
> Here is the problem. We have never detected one. So to build a search, you
> have to assume what it looks like. And then you find what you assumed.

**B03 — the one that got a name** (36 words)
> Two thousand nineteen. Parkes, pointed at Proxima Centauri. A narrow tone
> at nine eighty-two megahertz survives every cut and gets a name. Then they
> find dozens more just like it, from broken electronics on the ground.

**B04 — what the data is** (42 words)
> This is what the data looks like. Time down, frequency across. The dark
> vertical lines are us, transmitters on the ground. A signal from the sky
> leans, because the planet moves. A faint one is invisible here, which is
> why you integrate.

**B05 — the assumption, as a number** (35 words)
> So that is the search. Try every lean, keep the best. The range of leans
> you try is the assumption, written as a number. Anything outside it is not
> missed. It is never looked for.

**B06 — three transmitters** (29 words)
> Here are three transmitters. One leans, like we assume. One corrects its
> own drift, which is what we do. One blinks. All three are things a
> transmitter can do.

**B07 — the blind spot** (35 words)
> Run the search. The one that leans, found every time. The one that corrects
> its drift, found never — zero out of eighty. Widen the search by one
> number, and it is found every time.

**B08 — the edge** (26 words)
> And you can watch the blind spot appear. Move the edge of the search
> outward, and recall falls off a cliff exactly where it crosses zero.

**B09 — the other test** (33 words)
> So use a different test. Point at the star. Look away. Point back. Look
> away. A signal from the sky comes and goes with the telescope. Interference
> does not care where you point.

**B10 — the design tell** (35 words)
> So the tell. That test does not care what the signal looks like. The one
> our search scores zero on, it finds three times in four. Ask where it came
> from, not what it resembles.

**B11 — verdict** (29 words)
> So: we have never seen one. Every search is a guess about form. The only
> test that escapes the guess is the one that asks where it came from.

**B12 — your turn** (32 words)
> Your turn. Read it. Here is what my detector was trained to recognise. Tell
> me what it would miss, and what test would catch that without me having to
> guess right first.

**B13 — outro** (11 words)
> The Signal We Imagined. Humanitarians AI. AI in Astronomy, episode thirteen.

## Things a reader should push back on

Eight judgement calls, so the signer can overrule me rather than discover them:

1. **The centrepiece is a simulation and the voice says "run the search" in
   the first person.** A viewer could hear B04–B10 as a measurement of real
   Breakthrough Listen data. Every one of those beats carries "computed in
   this reel". If you want the voice to say "I simulated it", one word.
2. **Hypothesis B — the drift-corrected transmitter — is my choice, not a
   prediction.** I picked it because it is what *we* do for spacecraft, which
   makes it the most defensible "equally plausible alternative" I can name.
   But it is still a choice, and the episode's whole argument is about the
   danger of choosing. That is a tension the reel does not resolve, and I
   think it should not pretend to.
3. **Real pipelines do sweep through zero drift.** They then discard
   zero-drift hits, because in practice almost all of them are local. My
   simulation models the exclusion as a search-range limit, which is cleaner
   to demonstrate but is not exactly how every pipeline is built. The reel
   says "the range you try"; a SETI practitioner may object that the real
   mechanism is a post-hoc cut rather than a sweep limit. The consequence is
   the same, but the mechanism is simplified.
4. **I tried to argue that zero drift is too crowded to search, and my own
   measurement refused.** 6 look-alikes for a drifting candidate against 5
   for a stationary one. I removed the claim rather than raise the
   interference count until it came true — but that means the episode does
   not explain *why* pipelines exclude zero drift, only that excluding it has
   this cost. That is a real gap in the argument and I would rather leave it
   open than fill it with a tuned number.
5. **"0.70 for the pulsed beacon" is a sensitivity effect, not a drift-range
   effect.** Two different assumptions fail in two different ways, and the
   reel treats them as one family. Defensible, but it is a compression.
6. **BLC1's "dozens of look-alikes" is published, mine is not.** The reel
   must not let those blur, and B03's citation line says published, not
   measured here. Check that it reads that way to you.
7. **"We have never detected one"** is true as of this build and is the
   foundation of everything. If that ever changes the episode is obsolete in
   the best possible way.
8. **Ma et al.'s deep-learning search (820 targets, 480 hours, 8 candidates)
   is in SOURCES and not in the reel.** I judged that a second system's
   numbers would blur the one case being measured. You may think a modern ML
   example belongs on screen given the brief says "how AI separates" — that
   is a fair objection and it would cost a beat.

## What the visuals do that the words do not

Shown and never spoken: the 982 MHz tone turning from terracotta to ink as
the look-alikes arrive; the traced track in a field the viewer is told they
cannot see; the fan of trial tracks and the bracket closing around it; the
zero bar drawn as a *visible zero* rather than omitted; the 0.06 Hz/s chip at
the foot of the cliff; all six cadence traces; the ink/terracotta key.
**A viewer who only listens gets the argument; a viewer who watches gets the
receipts.**

## Audience check — `claude-hai` is for STUDENTS

The channel's spine question is when to use AI and when not to. This episode
answers with the case that has no good answer yet: **what do you do when you
cannot validate?** You cannot cross-validate against a class with no
examples. You cannot measure recall on something never observed. Every
number a SETI pipeline reports about its own sensitivity is a number about
synthetic injections — about the thing we imagined.

The transferable habit is the one B12 asks for: when you cannot validate
against truth, **look for a test that does not reference your hypothesis at
all.** Provenance instead of appearance. Where did this come from, rather
than what does it look like. It generalises far beyond radio astronomy — to
fraud, to anomaly detection, to anything where the positive class is rare,
expensive, or hypothetical.

No jargon before it is earned. "Technosignature", "de-Doppler", "drift rate",
"narrowband" and "cadence" appear nowhere in the narration — the pictures
carry those ideas and the citation lines name them. The voice says "lean",
"the range you try", "point at it, look away".
