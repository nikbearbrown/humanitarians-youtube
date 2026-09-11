# PEDAGOGY — *The Number Went Up.*

**GATE P.** A human reads the narration below and signs. Audio is not generated
until the verdict line below is changed from PENDING to a pass. Kokoro is local
and free, so this gate protects quality, never spend.

> Note for anyone editing this file: `generate_audio_kokoro.py` opens GATE P on
> a plain substring match anywhere in this document, so do **not** write the
> passing verdict string in prose — spelling it out in an explanatory sentence
> silently unlocks the gate. That is why this paragraph describes it instead of
> quoting it.

**VERDICT: PASSED**

Signed: Om Mali  Date: 11/09/26

---

## Written to a length, again

Ep. 06 was first cut at 5:23 and the human asked for under three minutes. Ep. 07
fixed that by sizing the script *before* writing it, and landed 2:50.2 against a
2:50.8 prediction. Ep. 08 does the same, with one extra margin:

| | words | predicted | measured |
|---|---|---|---|
| Ep. 07 | 443 | 2:50.8 | **2:50.2** |
| Ep. 08 | 434 | **2:46.8** | — |

The extra 3½ seconds of margin is deliberate. The words-only model
**under-predicts spoken numerals**, which is how Ep. 06 predicted 2:50 and
measured 3:07.7. This script is numeral-heavy. A first draft came in at 454
words (2:54.5 predicted); six lines were cut **before this gate**, which moved
four figures off the voice and onto the screen — where SHOW-DON'T-TELL wanted
them anyway.

If the measured total still lands over 3:00, the fix is `--speed`, not a
rewrite of signed narration. Ep. 06 needed 1.13 (Kokoro's speed is not linear:
1.08 requested gave 1.05 effective).

## What this episode teaches, and why it is worth an episode

Topic 08 in the brief is "asteroid/comet tracking — automated detection and
orbit prediction for planetary defense". The lazy version of that is a hazard
episode: big rock, small odds, look at the crater. This is not that.

The honest mechanism has **two halves that do not resemble each other**, and
the interesting thing is the seam:

1. **The learned half** is narrow and unglamorous. A CNN sorts eight kinds of
   dot; a second network scores whether four detections in a row lie on a
   straight line. It never learns an orbit. Its measured contribution is
   99.6% accuracy on real asteroids, a 0.4% false-negative rate, and a **90%
   reduction in what humans must screen**. The paper's own stated goal is
   reducing the *delay* to the Minor Planet Center — speed, not insight.
2. **The computed half** is two centuries old and does the frightening part.
   Fit a trajectory, sample every orbit the data still permits, count how many
   of them hit. No neural network is anywhere near Sentry, Aegis or NEODyS.

And then the payoff, which is the reason to make this at all: **in December
2024 an object's impact odds climbed to a record 3.1%, and five days later they
were essentially zero — and nothing went wrong.** A probability rises while the
Earth sits inside a *shrinking* uncertainty region. It collapses when the
region shrinks past us. The rise was evidence that the measurement was
improving.

That is a transferable idea. Every viewer meets moving risk numbers, and almost
everyone reads a rising one as a worsening situation. B12 hands them the
question that separates the two cases.

The series pivot is stated out loud at B01, as it was at Ep. 07: seven episodes
of AI reading the sky; this one is about where the reading stops.

## The narration, beat by beat

**B00 — cold open** (32 words)
> Hi, I'm Om Mali. This video is about how sky surveys and a neural network
> find asteroids headed for Earth, and why a rising chance of impact is usually
> the system working.

**B01 — presenter** (20 words)
> Seven episodes of AI reading the sky. This one is about the moment the
> reading stops and the arithmetic starts.

**B02 — the whole idea in one breath** (36 words)
> Telescopes sweep the whole sky every night. A network throws out the junk so
> people only look at plausible rocks. Then celestial mechanics decides whether
> to worry, and that number can rise for a good reason.

**B03 — the haystack** (34 words)
> Four telescopes photograph the same field four times a night, then subtract
> last night's picture. What is left is anything that moved, plus cosmic rays,
> satellites, and every star the subtraction got slightly wrong.

**B04 — eight kinds of dot** (34 words)
> The first stage is a convolutional network, and its whole job is telling
> eight kinds of dot apart. A cosmic ray is one pixel. A bad subtraction is two
> lobes. Only two are real.

**B05 — the tracklet** (33 words)
> Then a second network reads four detections in a row. A real rock walks a
> straight line at a steady rate; junk does not. That cut what humans must
> screen by ninety percent.

**B06 — where the learning stops** (33 words)
> Now the network is done. It never learned an orbit. What happens next is much
> older arithmetic: fit a trajectory, then sample every orbit the data still
> allows. That cloud is the answer.

**B07 — the number went up** (31 words)
> In December, a survey telescope in Chile caught a sixty-metre rock. Its odds
> of hitting Earth climbed past three percent, the highest ever recorded. Five
> days later they were essentially zero.

**B08 — why it had to** (36 words)
> Here is why. The uncertainty is a long thin cloud with Earth inside it. More
> observations shrink the cloud, so while Earth is still inside, the odds climb.
> They collapse once the cloud shrinks past us.

**B09 — then the Moon** (25 words)
> Then the same thing happened to the Moon. Its odds climbed for months, to the
> highest value yet. Webb finally ruled it out in March.

**B10 — the design tell** (32 words)
> The tell is this: the learned part answers whether a dot is real. Nothing
> learned decides whether you should move. And the gap is real — eleven
> impactors ever caught in advance.

**B11 — verdict** (30 words)
> So: the sky is subtracted, the junk is learned away, and the odds come from
> arithmetic. A rising probability means the cloud is shrinking while we are
> still inside it.

**B12 — your turn** (47 words)
> Your turn. Read it: help me tell apart a number that rose because things got
> worse, from one that rose because the uncertainty shrank, and what to ask
> before reacting to either. Run that on a forecast you actually track. Watch
> whether it asks what is shrinking.

**B13 — outro** (11 words)
> The Number Went Up. Humanitarians AI. AI in Astronomy, episode eight.

## Things a reader should push back on

Five places where I made a judgement call, so the signer can overrule me rather
than discover them later:

1. **"Four telescopes."** ATLAS's count has grown and is variously described as
   two, four or five. The line describes the *observing pattern*, not a total,
   and no count appears on screen. If that still reads as a claim, it can
   become "survey telescopes photograph the same field four times a night" at
   no cost.
2. **B09 no longer speaks the 4.3% figure.** It is on screen as a counter. This
   was one of the six trims; the alternative was going over three minutes. If
   you want it spoken, something else has to go.
3. **"Much older arithmetic"** instead of naming Gauss or a number of years.
   Least-squares orbit determination dates to 1801; "two hundred years" was in
   the first draft and was cut as both loose and expensive to speak.
4. **The computed peak is 3.86% and the published peak is 3.1%.** They are
   close because I chose the illustration scale (nominal miss = 8 capture
   radii) to put the curve's maximum in a plausible range. The *shape* and the
   peak's location are forced by geometry and checked analytically; the
   absolute height is a display choice. B08's chip says "computed in this reel,
   not redrawn" and its axis is a width, not a date. If that separation still
   feels thin, the chip can read "the shape, not the values".
5. **No hazard language.** The sources say "city killer" freely; the narration
   never does, and there are no casualty or blast comparisons. I think
   sensationalising it would be the dishonest version of this episode, but that
   is an editorial call and it is yours to reverse.

## What the visuals do that the words do not

Per SHOW-DON'T-TELL, the evidence is on screen and the voice carries the
judgement. Specifically, these are shown and never spoken: the alert volume
chip; the names of all eight artefact classes; the 0.4% false-negative rate
(landscape); the six plotted points of the published probability record; the
Torino-3 comparison with Apophis; the ruling-out date; the completeness bars
and the 90% mandate rule. **A viewer who only listens gets the argument; a
viewer who watches gets the receipts.**

## Audience check — `claude-hai` is for STUDENTS

The channel's spine question is when to use AI and when not to. This episode
answers it with a case where the boundary is already drawn correctly by the
professionals: the network is used where it is cheap and checkable (is this dot
real?) and kept out of where it would be unaccountable (should you move?). The
lesson a student can take is not "AI is limited" but "notice which half of a
pipeline produced the number you are reacting to."

No jargon is used before it is earned. "Tracklet", "line of variations" and
"target plane" appear nowhere in the narration — the pictures carry those ideas
and the citation lines name them for anyone who wants to look them up.
