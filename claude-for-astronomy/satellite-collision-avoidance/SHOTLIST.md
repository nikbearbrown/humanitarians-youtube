# SHOTLIST — *Safer By Not Looking.*

Ep. 15 · `satellite-collision-avoidance` · 14 beats · 426 words
**The series finale.**
Predicted 2:31 against Ep. 14's measured 0.3548 s/word — **under 3:00 by
design**, with ~29 s of margin for the ±5–10 % words-only error.

Both cuts render from one `scenes.py`. 16:9 at 3840×2160, 9:16 at 2160×3840.

---

## Lanes

| Lane | Beats | Engine |
|---|---|---|
| Claude UI | B00, B11, B12, B13 | Remotion (`ClaudeComposerAsk`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`) |
| Illustrated | B01–B10 | reel-local `scenes.py` (Manim CE) |

The ILLUSTRATE LAW: the Claude desktop UI appears only where the reel is
actually addressing Claude. Everything between is drawn.

---

## Beat by beat

### B00 · COLD OPEN · 9.6 s · `ClaudeComposerAsk`
Greeting **"Ola, HAI"** — the hello lexicon cycles least-recently-used, and
Ola was last seen at Ep. 11. The composer types the ask, the send button arms
in terracotta, the runner reads *integrating the encounter plane over 120,000
conjunctions*, and three result lines land in order.

> Opens on the required line: "Hi, I'm Om Mali. This video is about…"

### B01 · FRAME · 8.5 s · `B01_Presenter`
Name writes in under a terracotta rule; role line; a card beside it. Row one
— *fourteen episodes / where the answer came from* — lands and is **struck**.
Row two — *this one / it moves when you do* — lands and is **boxed**. Series
line: *Ep. 15 · the last one*.

### B02 · FRAME · 11.7 s · `B02_OneBreath`
One card, three rows, no plate. The argument before any evidence:

1. **NOT THE CHANCE THEY HIT** — *that is what everyone hears*
2. **GIVEN YOUR OWN UNCERTAINTY** — *that is what is computed*
3. **SO IT IS PARTLY ABOUT YOU** (accent, underlined)

Closer: *know less, look safer*.

### B03 · THE TASK · 12.1 s · `B03_TheBenchmark`
The published benchmark as an **isotype at honest scale**. One mark = 10
close approaches: a field of **1,532 ink marks**, of which **3 are
terracotta** — the thirty that were ever dangerous, scattered through the
field so the eye has to find them.

15,321 against 30 is 511:1, which cannot be drawn as two blocks side by side
— at any mark size that makes the small block visible, the large one does not
fit. Putting the thirty *inside* the field makes the ratio the picture rather
than a caption on it.

Landscape adds a `PUBLISHED · ESA, 2015-2019` chip and the 199,082-message
note; **portrait drops both** — the citation line still names the paper.

### B04 · THE MECHANISM · 12.4 s · `B04_TheNumber`
`geometry.png` — the same encounter at three tracking qualities, on **one
shared density scale**. Panels named *tracked well* / *in between* /
*tracked badly*; the terracotta hard-body disk is ringed, identical in all
three. Closer: *less on the disk*.

**The one plate beat with no right-hand column**, so its plate centres rather
than sitting at x = −1.10.

### B05 · THE MECHANISM · 12.1 s · `B05_Dilution`
`dilution.png` — Pc against your own uncertainty. The ends are named (*you
know exactly* / *you know almost nothing*), the action threshold chipped at
1 in 10,000, and the **summit** dot called out. Closer: *the curve has a
summit*.

### B06 · THE TELL · 10.6 s · `B06_TheFlip`
**The load-bearing beat.** `flip.png` — two bars for the *same conjunction*
straddling the action threshold:

| bar | | value |
|---|---|---|
| ink | tracked well | 1.6 in a thousand |
| terracotta | uncertainty 7× larger | 8 in a million |

The right column says it plainly: *nothing about the two objects is
different — only how well one of them was tracked*. Closer: *the alert goes
away*.

### B07 · THE TASK · 11.0 s · `B07_TheTask`
`shrink.png` — risk against time to closest approach. Ghost traces fade
toward the floor; three terracotta traces climb from it. A vertical rule
marks where the forecast is made, two days out.

**This plate was redrawn after being measured** — see FACTCHECK. Closer:
*they announce themselves early*.

### B08 · THE RESULT · 11.4 s · `B08_TheReversal`
`bars.png` — **two panels that cannot share an axis**, which is the beat. The
errors differ by two orders of magnitude; forcing one axis would flatten the
right-hand panel to nothing, and the right-hand panel is the only one an
operator cares about.

| | all 40,000 | the 124 notified |
|---|---|---|
| assume nothing changes (ink) | 0.061 | **1.275** |
| the trained model (terracotta) | **0.015** | 4.130 |

Right column: **4× better**, then **3× worse** in the accent, underlined, and
*on the only ones anybody saw*. Closer: *same model, opposite verdict*.

### B09 · THE RESULT · 9.9 s · `B09_NinetySeven`
The published confirmation, as a second isotype: **97 ghost marks, 12 filled
terracotta**. The organisers' own phrase types in the right column —
*"surprisingly effective"* — for a forecast that says nothing will change.
Closer: *twelve of ninety-seven*.

### B10 · THE TELL · 12.8 s · `B10_TheTell`
`maxpc.png` — the diluting terracotta curve and the flat ink bound, with two
dots **at the same uncertainty** giving opposite decisions. The right column
also carries the fix that failed: *I gave it the geometry too — it moved the
error three percent*. Closer: *it stops depending on you*.

### B11 · VERDICT · 12.4 s · `ClaudeVerdictArtifact`
A five-line artefact page. Five, not four: GATE V's bbox-fill floor is 0.55
and a four-line card sits exactly on it, so the verdict flips on encoder
noise.

### B12 · HANDOFF · 11.4 s · `ClaudeComposerAsk`
The viewer's prompt — *what could I do to the inputs to make this number look
better without making anything safer* — with three grading lines.

### B13 · OUTRO · 5.3 s · `ClaudeTitleOutro`
Title poster-style with the terracotta period, rule, handle, series position.
Ends on *"That is the series."*

---

## Aspect discipline

`scenes.py` is aspect-aware. `frame_height` stays 8.0 in both cuts, so the
vertical band plan is identical; only x changes (±6.15 landscape, ±1.80
portrait). Portrait is **not a crop** — it carries fewer elements, larger.

**The reduction rule: anything the narration speaks stays on screen.** What
portrait loses is on-screen-only extras — B03's PUBLISHED chip and message
note, B09's chip and pull-quote, and the right-hand columns, which become
stacked legend rows beneath each plate.

**Play-count parity is checked in both aspects** with `natboth15.py`, and the
real filled length with `verify15.py`. Scenes whose portrait branch plays
fewer reveals carry `RT_PORTRAIT` — the Ep. 14 lesson, now part of the
chassis.
