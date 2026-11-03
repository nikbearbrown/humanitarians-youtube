# PEDAGOGY — "16-bit or 24-bit: What Bit Depth Does"

How this reel is built to teach, and the two corrections that shaped it.

## The brief that set the register

Rohan, after watching the first cut:

> I checked out the bit depth video. It starts out very abruptly. what is a
> person who knows nothing about audio going to understand? I want you to give
> some background. Explain it as if the viewer is new to the topic completely.
> Keep everything at a high level.

then, after the rewrite over-corrected:

> Okay. and dont make the video too high level either. it has to be a good
> balance. at the end of the day the viewer has to learn somthing

Both are load-bearing. The first says *no assumed knowledge*; the second says
*no empty reel*. The structure below is the attempt to hold both.

## The shape

| Beat | Job | What the viewer can do after it |
|---|---|---|
| B00 ASK | name the situation | recognise the question when a dialog asks it |
| B01 BACKGROUND | what sound is, how a computer stores it, the two questions | tell sample rate and bit depth apart |
| B02 ANALOGY → IDEA | a ruler, then that ruler on a wave | say what bit depth *is* in their own words |
| B03 MECHANISM | the leftover gap is a hiss; coarser ruler, louder hiss | explain *why* a lower depth is noisier |
| B04 THE NUMBERS | −53 vs −101 dB, and what 100 dB means in a room | judge whether 16-bit is enough |
| B05 WHAT TO DO | 24 to work in, 16 to ship, never step down then up | make the decision |
| B06 OUTRO | the through-line | repeat it to someone else |

Background → everyday analogy → the idea → why it matters → what to do. The
subject of the video is not reached until B02, and its first hard number does not
arrive until B04, at 1:20 of 2:07.

## Vocabulary: what is never said

The audience note rules out the words a professional would reach for first. Every
one of these has a plain replacement that is used consistently:

| Not used | Used instead |
|---|---|
| quantisation, quantisation error | *pushed to the nearest marking*, *the leftover gap* |
| noise floor | *the hiss the file itself adds* |
| dynamic range | *how quiet a sound can get before the hiss takes over* |
| dBFS, full scale | *how far below full volume* |
| resolution, precision (as jargon) | *how many markings your ruler has* |
| LSB, least significant bit | not needed at all |
| dither | **deliberately absent** — see below |
| sample rate | said **once**, named only so it can be set aside |
| headroom | *room to work in* |

"Decibel" is the one technical word kept, because B04 cannot work without a unit
and the frame immediately anchors it to a whisper and a rock concert.

## Why a ruler

Every analogy for bit depth is either a staircase or a ladder, and both have the
same defect: they are already *pictures of the answer*. A viewer who does not yet
know what is being measured cannot see why a staircase matters.

A ruler is different in three useful ways:

1. **It is an object, not a diagram.** Everyone has used one.
2. **Its two variables are already familiar** — how long it is, and how finely it
   is marked. Those are full scale and step size, with no new words.
3. **Its failure mode is already familiar too.** Everyone has had to round to the
   nearest marking and knows it is a small lie. That is the whole mechanism, and
   it arrives for free.

The rulers stay on screen while the wave snaps to them. The analogy is not a
stepping stone to be kicked away once the "real" explanation arrives — it *is*
the explanation, and a viewer who loses the thread can look back at it.

## Why the hiss is shown moving

B03's claim is that thousands of tiny errors add up to *a sound*. A still trace
of noise does not make that claim — it looks like a decorative squiggle. The
trace is reseeded every two frames, so it is visibly alive, and the two
comparison cards at the end run their traces at 4× different amplitudes so
"louder hiss" is something you see rather than read.

## Why exactly two numbers

The first version of B04 compared 8-, 16- and 24-bit with per-bit brackets
(+47.7 dB, +48.8 dB) and step sizes in scientific notation. Rohan cut it:

> These are too detailed. Keep it high level. Use details only where necessary.

Three columns is a table; two is a decision. What survived is the pair that
answers the export dialog — and, more importantly, the **room line**: a dashed
rule across the plot labelled THE ROOM YOU ARE SITTING IN, with the 16-bit floor
below it. Two numbers are abstract; a line that says *your room is noisier than
this* is a conclusion the viewer can act on tonight.

## What was deliberately left out

- **Dither.** The honest treatment of quantisation noise includes dither, and
  dither is genuinely interesting. It is also a second mechanism layered on the
  first, and a viewer who has just met "rounding" cannot hold "and now we add
  deliberate noise to make the rounding sound better". The measurement was taken
  *without* dither and MEASUREMENTS.txt says so.
- **Sample rate, beyond naming it.** It is the other half of the same dialog and
  deserves its own reel.
- **Fixed vs floating point.** The reason 32-bit float exists is a better answer
  to B05's question than 24-bit is, and it needs its own five minutes.
- **The 24-bit floor.** Measured, logged, not shown. See
  [FACTCHECK.md](./FACTCHECK.md).
- **Any claim that 24-bit sounds better to a listener.** It does not, and B05
  says so plainly: *"Your listener gains nothing from more."*

## The one thing a viewer should remember

> Bit depth isn't quality. It's room to work in.

If they remember only that and the export rule that follows from it, the reel has
done its job.
