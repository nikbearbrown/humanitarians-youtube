# PEDAGOGY — Ep. 18, *counting-craters*

**GATE P. A human signs this before any audio is generated.**
Audio here is free (Kokoro, local). This is a quality gate, not a cost gate.

---

## The one thing a student should leave with

**Automating a measurement does not calibrate it.**

You can make a number arbitrarily precise and still be reading it off a scale
nobody has checked. Crater counting is the cleanest example in science: a
neural network can find craters faster, more consistently, and in places no
human will ever look — and the age it produces is still only as good as a
curve anchored to a handful of rocks that astronauts and landers carried home.

The series spine is *when to use AI and when not to*. This episode is the
first in the run that answers **both ways at once**, and that is the point.
Ep. 17 was a clean "not". This one says: automate this half, and keep your
hands off that half — and the hard skill is telling which half you're in.

## The second thing, which is the harder one

**Find the thing your number is compared against, and ask when it was last
checked.**

Every measurement is a comparison. The crater count is compared to the
chronology curve. A benchmark score is compared to a test set somebody built.
A grade is compared to a rubric somebody wrote. Students will meet this
constantly and almost never be shown where the comparison came from. B12 hands
them the question directly, applied to their own work.

## Why this isn't Ep. 08

`ideas.md` Notes govern Eps. 16–28: each covers ground none of 01–15 touch,
and none of them is about asteroids. **Ep. 08** (`asteroid-impact-warning`)
detects and tracks objects *before* they strike. **Ep. 18 never looks at an
object in flight.** Every crater here is already on the ground, and the only
question asked of it is how long it has been there. Ep. 06 drives a rover;
nothing here is driven. Ep. 10 triages transients; nothing here is ranked.

This episode is also the only one in the series whose subject **cannot be
observed twice** — the ground has not changed in a billion years, which is
precisely why the calibration has to come from somewhere else.

## The arc

| beat | does what | why it's there |
|---|---|---|
| B00–B02 | pose it; name the split | "a better counter moves the measurement; only a rock moves the curve" |
| B03 | the rule | 14 vs 80 craters — a student must *see* "denser = older" before anything is argued |
| B04 | the pile | 384,343 by hand; tens of millions below a kilometre. Why automation is not optional |
| B05 | the disagreement | ±45% between experts — the honest case FOR automation, and it's about consistency, not speed |
| B06 | the machine | DeepMoon's 92% — **with its raw 57% on screen beside it** |
| B07 | **the curve** | the hinge: density is a lookup, and the lookup table is wildly non-linear |
| B08 | **what the error costs** | the load-bearing beat: the same ±45% is worth 16% of the answer on old ground and 90% on young ground |
| B09 | the gap | what the curve is actually nailed to — and the hole between 1 and 3 Ga |
| B10 | **the attack on my own claim** | the rock beat counting 175×… *and* the recalibration only moved the curve 0.24 Gyr |
| B11–B13 | verdict, handoff, outro | names the "when not to learn it" rule; hands the student their own calibration to audit |

## Why B08 is the beat the episode is built around

Students are taught that better instruments give better answers. B08 shows a
case where that is **conditionally false**: improving your count helps enormously
on a one-billion-year-old plain (where the error is 90% of the answer) and
barely at all on three-and-a-half-billion-year-old highlands (16%). The clock
runs fast early and crawls late.

The payoff lands in B09: the place where counting precision matters most —
young surfaces — is exactly the stretch of curve that had **no calibration
point at all** until 2021. Precision where you have no accuracy.

## What I deliberately did NOT do

- **Did not claim nobody applies ML to dating.** Transfer-learning work on
  crater degradation-stage ages exists. The claim is scoped to the
  *calibration* — the density-to-age curve — and B11 is worded to that scope.
- **Did not claim crater counting is unreliable.** The Chang'e-5 rock landed
  *inside* the counted window. The narration says "not wrong, just loose",
  and `gen_craters.py` asserts that containment (C8).
- **Did not hide the counter-evidence.** The Chang'e-5 recalibration moved the
  curve by at most 0.24 Gyr. That is a weak result for my own headline, and it
  ships in B10 rather than living in a footnote.
- **Did not quote a count of calibration points.** Sources differ on what
  counts as an independent anchor; the episode shows the shape instead.
- **Did not let 92% stand alone.** The raw 57% is on screen in the same beat.

## Honest notes a reviewer should see

1. **`surface.png` and `spread.png` are synthetic.** They exist so "denser =
   older" and "analysts disagree" are *visible*. The only quantitative claim
   either makes is the count ratio, which is asserted against the real
   chronology function. FACTCHECK F1 and F4 say so.
2. **The anchor positions in `anchors.png` are illustrative.** The load-bearing
   shape — old cluster, empty middle, young cluster — is sourced; individual
   dot placement is not.
3. **One chronology function, used consistently.** Published N(1) values come
   from more than one production function and are not interchangeable. Nothing
   from elsewhere is mixed into the derived numbers.
4. **The 1.3–2.7 Ga window is a spread across chronology models**, not a 1σ
   error bar. The screen labels it that way.

## Checks before signing

- [x] Spine question answered (when to use AI and when NOT), explicitly, in B11
- [x] Ep. 08 boundary respected and stated in the metadata; B03 frames it on screen
- [x] Every spoken number traced in FACTCHECK
- [x] All derived numbers asserted in `gen_craters.py` (build fails otherwise)
- [x] Published counter-evidence included rather than omitted (B10)
- [x] The headline number's weaker raw form shown beside it (B06)
- [x] A falsification ships *as a beat*, not as a footnote
- [x] 417 words → 2:36 predicted, 2:52 worst case — under 3:00
- [x] Plates carry imagery only; all labels placed by `scenes.py`
- [x] Two plates were redrawn because they taught the opposite of their beat
      (`cost.png`, `pile.png` — see SOURCES corrections 4 and 5)

---

## VERDICT

```
VERDICT: PASS
signed:  Om Mali
date:    11/20/2026
```

*Signed by Claude on Om Mali's explicit written instruction in the build
request ("Pass Pedagogy on my behalf with the Friday date"), using the Friday
of the build week. Recorded here so the signature is not mistaken for an
independent review.*
