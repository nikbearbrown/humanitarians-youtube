/ PEDAGOGY — *What We Chased Before.*

**GATE P.** A human reads the narration below and signs. Audio is not generated
until the verdict line below is changed from PENDING to a pass. Kokoro is local
and free, so this gate protects quality, never spend.

> Note for anyone editing this file: `generate_audio_kokoro.py` opens GATE P on
> a plain substring match anywhere in this document, so do **not** write the
> passing verdict string in prose — spelling it out in an explanatory sentence
> silently unlocks the gate. That is why this paragraph describes it instead of
> quoting it.

**VERDICT: PASSED**

Signed: Om Mali  Date: 25/09/26

---

## Written to a length

| | words | predicted | measured |
|---|---|---|---|
| Ep. 08 | 434 | 2:46.8 | 2:38.5 |
| Ep. 09 | 436 | 2:39.2 | 2:43.6 |
| **Ep. 10** | **429** | **2:41.0** | **2:27.7** |

Margin ~19 s. The words-only model is noise of order ±5–10% **with no
consistent sign** — Ep. 06 +10.4%, Ep. 07 −0.4%, Ep. 08 −5.0%, Ep. 09 +2.7% —
so the margin is for noise, not for a predicted direction. If the measured
total lands over 3:00 the fix is `--speed`, not a rewrite of signed narration.

**Measured after the gate: 2:27.7**, 32.3 s under the cap, so no `--speed` was
needed. Model error **−8.2%**, the largest under-run of the five and now the
low end of the range (+10.4% … −8.2%).

## What this episode teaches, and why it is worth an episode

Topic 10 in the brief is "AI triaging which transient sky events astronomers
should chase before they fade". The obvious version is a speed story: too many
alerts, not enough humans, here comes the classifier. That version is true and
it is also the least interesting thing about the problem.

The interesting thing is that **the training set is the output of the system's
own past decisions**. Spectroscopy is the scarce resource. What got a spectrum
became what got a label; what got a label became what the model can recognise;
what the model recognises decides what gets a spectrum next. The loop runs
through human hands and a telescope queue, and it was closed long before any
machine learning arrived — the historical sample is bright and Ia-heavy
because that is what people chose to chase.

So I built the loop and ran it. Twelve seasons, twenty spectra each, sixty
repeats, three strategies. The result is sharper than I expected and I had to
rewrite my own claim to match it:

- Spending the budget on **confidence** makes overall accuracy rise — 0.883 to
  0.897 — while the rare class's median recall stays at **exactly zero**. In
  **48 runs out of 60** it is never recognised once, after 240 spectra.
- Spending it on the **brightest** objects, which is what the field actually
  did, is worse: 53 of 60 at zero.
- Spending it where the model is **least sure** reaches a median recall of
  **0.638**, never fails in 60 runs — and ends with *higher* overall accuracy
  too, 0.920.

That last point matters: this is not a trade of accuracy for diversity. Greedy
loses on both. The real cost lands on the count of confirmed Ia, and the
episode says so and quantifies it.

The payoff is a number, not a warning. **One night in ten** spent on doubt
takes the chance of ever recognising the rare class from 35% to 92%, and costs
18% of the confirmations.

The series pivot is stated at B01: nine episodes of AI looking at the sky;
this one is about AI choosing what we look at.

## The narration, beat by beat

**B00 — cold open** (33 words)
> Hi, I'm Om Mali. This video is about how AI decides which exploding stars are
> worth pointing a telescope at tonight, and why the ones it skips are the ones
> nobody ever finds.

**B01 — presenter** (19 words)
> Nine episodes of AI looking at the sky. This one is about AI deciding what we
> look at next.

**B02 — the whole idea in one breath** (33 words)
> A supernova fades in days. There are far more of them than there are
> telescopes, so something has to choose. And the thing doing the choosing
> learned from what we chose last time.

**B03 — the deadline** (33 words)
> A transient peaks and fades within about two weeks, so a spectrum is only
> useful early. Rubin will report up to ten million changes a night. About one
> in ten ever gets one.

**B04 — which ones** (30 words)
> And which ones? The bright ones. Almost every transient brighter than
> magnitude eighteen gets confirmed. Down at twenty and fainter, closer to one
> in seven. Nobody wrote that rule down.

**B05 — the loop** (38 words)
> So the labelled set is not a sample of the sky. It is a record of what we
> chased. Train on it and you get a model that is best at exactly the things we
> already looked at.

**B06 — twelve seasons** (32 words)
> I ran that loop. Twelve seasons, twenty spectra each, spent where the model
> is most confident. Accuracy climbs. The rare class? In forty-eight runs out
> of sixty it is never recognised once.

**B07 — what got labelled** (30 words)
> You can see why. After two hundred and forty spectra, the rare class is two
> tenths of one percent of everything labelled. The loop kept confirming what
> it already knew.

**B08 — spend it on doubt** (35 words)
> Now change one thing. Spend the budget where the model is least sure, nearest
> the line it cannot draw. That is a real deployed rule. And doubt moves —
> toward the thing nobody has labelled.

**B09 — the receipt** (33 words)
> In a real run on a real telescope, that strategy reached the same performance
> with a quarter fewer spectra, and turned up microlensing and flaring stars
> that were never in anyone's training set.

**B10 — the design tell** (33 words)
> So the tell. A classifier trained on past choices repeats them, and accuracy
> never warns you. Spend one night in ten on what you do not understand: a
> third becomes nine in ten.

**B11 — verdict** (30 words)
> So: the sample is the decision. Confidence buys more of what you have. Doubt
> is the only thing that buys something new, and it costs less than you would
> think.

**B12 — your turn** (39 words)
> Your turn. Read it: my model was trained on data that earlier decisions
> produced. Help me work out what it can never learn, and the cheapest
> experiment that would show me. Run it on a model you rely on.

**B13 — outro** (11 words)
> What We Chased Before. Humanitarians AI. AI in Astronomy, episode ten.

## Things a reader should push back on

Six judgement calls, so the signer can overrule me rather than discover them:

1. **The centrepiece is a simulation, and the episode says "I ran that loop"
   in the first person.** That is accurate — I did — but a viewer could hear it
   as "this is what ZTF does". Every one of those beats carries "computed in
   this reel" on its citation line, and the class fractions and budget are
   invented to be illustrative. If you want the voice to say "I simulated it",
   that is a one-word change.
2. **"Nobody wrote that rule down"** is editorial. The selection function is
   emergent, not anyone's policy, and I think that is exactly why it is worth
   naming — but it is the most opinionated line in the reel.
3. **B04's faint-band figure.** The source gives 10–20% for 20 < V < 22; the
   plate draws 15% and the voice says "one in seven". If you would rather the
   voice say "one in five to one in ten", it fits.
4. **The episode does not name ZTF, ALeRCE or Fink in the voice** — only in the
   citation lines. That keeps the narration about the mechanism, but it means a
   viewer who only listens does not learn that these are real systems with
   names. B09 says "a real run on a real telescope", which I think carries it.
5. **The rare class is never given a name.** In reality it would be a specific
   transient type. I kept it abstract because naming one would imply a claim
   about that class that the simulation does not support.
6. **The 18% cost is quoted from one point on a noisy curve.** At 10%
   exploration the confirmed-Ia count is 82% of its peak across 40 repeats; the
   curve wobbles by a few percent either side. "About a fifth" would be safer
   if you want it softer.

## What the visuals do that the words do not

Shown and never spoken: the shaded decision window; all four confirmation
bars; the "published, not measured here" tag; the closed ring in B05; both
curves in B06 and the fact that all three accuracy lines rise; the 0.19% and
16.8% pair; the 3.6× and 8.4× enrichment; the "92 spectra, not 127" card; the
whole trade-off curve. **A viewer who only listens gets the argument; a viewer
who watches gets the receipts.**

## Audience check — `claude-hai` is for STUDENTS

The channel's spine question is when to use AI and when not to. This episode
answers with a case where the model is useful, the pipeline works, the accuracy
number is genuinely improving — and the whole thing is quietly narrowing. The
transferable habit is one question a student can ask of any trained system:
*where did the labels come from, and what could never have been in them?*

No jargon before it is earned. "Active learning", "uncertainty sampling",
"selection function" and "feedback loop" appear nowhere in the narration — the
pictures carry those ideas and the citation lines name them for anyone who
wants to look them up.
