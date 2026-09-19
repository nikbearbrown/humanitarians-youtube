# PEDAGOGY — *The Sharpest Guess.*

**GATE P.** A human reads the narration below and signs. Audio is not generated
until the verdict line below is changed from PENDING to a pass. Kokoro is local
and free, so this gate protects quality, never spend.

> Note for anyone editing this file: `generate_audio_kokoro.py` opens GATE P on
> a plain substring match anywhere in this document, so do **not** write the
> passing verdict string in prose — spelling it out in an explanatory sentence
> silently unlocks the gate. That is why this paragraph describes it instead of
> quoting it.

**VERDICT: PASS**

Signed: Om Mali  Date: 18/09/2026

---

## Written to a length

| | words | predicted | measured |
|---|---|---|---|
| Ep. 07 | 443 | 2:50.8 | 2:50.2 |
| Ep. 08 | 434 | 2:46.8 | 2:38.5 |
| **Ep. 09** | **436** | **2:39.2** | — |

The margin is ~21 s. It is wide because **the words-only model is noisy in both
directions** — Ep. 06 ran 10.4% long, Ep. 07 0.4% short, Ep. 08 5.0% short —
not because any particular kind of word runs long. Ep. 08's build log justified
its margin by claiming spoken numerals under-predict; they did not, and that
reasoning is retracted here.

If the measured total lands over 3:00 the fix is `--speed`, not a rewrite of
signed narration.

## What this episode teaches, and why it is worth an episode

Topic 09 in the brief is "denoising deep space images — how AI reconstructs
sharper JWST/Hubble images from noisy raw sensor data". The lazy version is a
before-and-after reel: blurry blob, crisp galaxy, look how clever. This is not
that, because the before-and-after framing hides the only interesting question,
which is **where the new detail came from**.

The episode makes three moves:

1. **Two different operations are both called denoising, and only one of them
   is arithmetic.** JWST's 1/f detector striping is a *pattern*: you measure it
   in blank sky and subtract it. NSClean does this in Fourier space in a few
   seconds on a laptop, with no network anywhere. Blur is not a pattern. It is
   missing information.

2. **The missing information is missing exactly, not approximately.** The
   transfer function of a circular aperture is *identically zero* above its
   cutoff. Numbers multiplied by zero do not come back. In this reel's optics
   only 1.8% of the grid's spatial frequencies survive at all.

3. **So the problem has many right answers, and a sharp picture is a choice
   among them.** B05 proves it rather than asserting it: two skies that differ
   by half their structure, blurred, produce observations differing by
   **0.0000 noise σ**. B06 then gives the same single image to three different
   assumptions, forces all three to fit the data *identically* (χ²/N = 1.008,
   1.007, 1.008), and gets three visibly different galaxies — 36% apart.

The payoff is a practice, not a warning. The honest output of a restoration is
**a range**, and where the range is wide, nothing was measured. That is
directly checkable, it is what the current literature actually does (256 and
450 posterior samples in the two papers cited), and it hands the viewer a
question they can ask of any enhanced image they meet.

The series pivot is stated out loud at B01, as in Eps. 07 and 08: eight
episodes of AI reading the sky; this one is about AI drawing it.

## The narration, beat by beat

**B00 — cold open** (30 words)
> Hi, I'm Om Mali. This video is about how AI sharpens telescope images, and
> why the sharpest picture is a guess, one of many that fit the data equally
> well.

**B01 — presenter** (20 words)
> Eight episodes of AI reading the sky. This one is about AI drawing it, and
> where the detail comes from.

**B02 — the whole idea in one breath** (37 words)
> Every telescope image is blurred and noisy. Some of that is fixable
> arithmetic. But the blur destroys information outright, and getting a sharp
> picture back means filling the gap with an assumption about what galaxies
> look like.

**B03 — two kinds of denoising** (35 words)
> Two different things get called denoising. Detector striping is a pattern you
> can measure in blank sky and subtract — seconds on a laptop, no network. Blur
> is not a pattern. It is missing information.

**B04 — the chain** (30 words)
> Here is the chain: real sky, blurred by the aperture, counted as photons,
> plus read noise. The aperture is the killer. Above its cutoff the transfer
> function is exactly zero.

**B05 — two skies, one image** (35 words)
> So watch this. I built two skies that differ by half their structure. Blur
> them both and the images are identical — not close, identical to four decimal
> places. The data cannot tell them apart.

**B06 — three answers** (32 words)
> Give one image to three different assumptions and you get three different
> sharp galaxies. All three match the data equally well. Sharpness is not
> something you recovered. It is something you chose.

**B07 — where the detail comes from** (33 words)
> A real system makes that choice by training on simulated galaxies, tens of
> thousands of them. It returns the most likely galaxy given what it was shown.
> That assumption is doing real work.

**B08 — return the range** (31 words)
> The honest version returns hundreds of answers instead of one. Where they
> agree, the photons decided. Where they disagree, the prior did. Above the
> cutoff the spread is exactly the prior.

**B09 — the detector** (34 words)
> That gives you a detector. Compare the spread of the answers against the
> spread of the assumption. Strong data, tiny ratio. Weak data, and the ratio
> climbs while features appear that were never observed.

**B10 — the design tell** (32 words)
> So the tell is this: a denoiser does not remove noise, it adds an assumption.
> Checked against Webb, one method's guesses held up. Qualitatively. Nobody has
> measured how often they do not.

**B11 — verdict** (31 words)
> So: striping subtracts, blur does not. One sharp picture is a choice among
> many. The only honest output is a range, and the range tells you which
> details you actually measured.

**B12 — your turn** (46 words)
> Your turn. Read it: when a model sharpens, upscales or fills in my data, help
> me work out which parts are measured and which are the model's assumption,
> and what to report. Run it on something you have enhanced. Watch whether it
> asks for a range.

**B13 — outro** (10 words)
> The Sharpest Guess. Humanitarians AI. AI in Astronomy, episode nine.

## Things a reader should push back on

Six judgement calls, so the signer can overrule me rather than discover them
later:

1. **"Identical to four decimal places" is literally what the script prints
   (0.0000), but the true value is exactly zero.** I chose the weaker phrasing
   because "exactly zero" invites the objection "nothing is exactly zero in a
   real telescope" — which is fair, since a real system has scattered light,
   finite sampling and imperfect flat-fielding. If you would rather the
   narration claim the stronger, mathematically correct thing, it is a one-line
   change.
2. **The episode never shows a real telescope image.** No HST, JWST or HSC
   frame appears anywhere; B10's Hubble/Webb panels are schematic cards. This
   is deliberate under REBUILD LAW, but it does mean a viewer never sees the
   actual thing being discussed. The alternative was licensing questions and an
   implication that the computed plates are data.
3. **"Tens of thousands"** is spoken while **17,852** is on screen. If you want
   the exact figure spoken, something else in B07 has to go.
4. **B10 leans hard on one caveat.** "Qualitatively" is a one-word sentence and
   is on screen at 22 pt. I think the emphasis is earned — the paper says it in
   those terms — but it is the most opinionated moment in the reel.
5. **"Nobody has measured how often they do not"** is an absence claim. I
   checked both primary papers and neither reports a quantitative error rate
   against independent truth. If you know of one, this line is wrong and should
   go.
6. **The variance-ratio curve is mine, the two figures beside it are theirs.**
   They are different measurements — mine over Fourier modes in a
   linear-Gaussian model, theirs over an image aperture with a diffusion prior.
   They appear together because the beat is about that distinction, and a tag
   separates them. If that still reads as conflation, the tag can become a
   full sentence.

## What the visuals do that the words do not

Per SHOW-DON'T-TELL, the evidence is on screen and the voice carries the
judgement. Shown and never spoken: the 3.6% stripe residual; the 98% of grid
frequencies that carry nothing; the 52% / 0.0000 pair; the three χ² values;
17,852 and the training cost; the 1.0000 identity above the cutoff; the two
published variance ratios; "no published rate for how often it is wrong".
**A viewer who only listens gets the argument; a viewer who watches gets the
receipts.**

## Audience check — `claude-hai` is for STUDENTS

The channel's spine question is when to use AI and when not to. This episode
answers with a case where the tool is genuinely useful *and* its output is not
a measurement — which is the harder, more useful lesson than "AI is
unreliable". A student can take away one transferable habit: when a model fills
something in, ask what it was trained on and ask for a range.

No jargon is used before it is earned. "Null space", "posterior",
"deconvolution" and "regularisation" appear nowhere in the narration — the
pictures carry those ideas and the citation lines name them for anyone who
wants to look them up. The one technical token on screen is χ², which is
labelled by what it means ("all three match the data equally well") in the
same breath.
