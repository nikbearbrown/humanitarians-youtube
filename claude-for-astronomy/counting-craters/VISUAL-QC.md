# VISUAL-QC — Ep. 18, *counting-craters*

A gate passing is not the frame being right, and a gate failing is not the
frame being wrong. Both happened here, and this file is the record of which
was which — with the measurements, not the assertions.

**Final state: 0 BLOCKER in both cuts. Nothing was passed with `--lenient`.**

---

## 1. Defects the gates caught (7)

### Portrait GATE B, strict (5) — first portrait pass failed 5 of 10

Landscape passed 10/10 on the first run. Portrait did not, which is the
standing lesson from Ep. 08: *a layout is two layouts, and only one of them
has been checked.*

| beat | what GATE B found |
|---|---|
| B03 | `label on a curve` — the numeral **14** sat on the plate's own frame |
| B04 | `text-on-text 29%` — the log-axis note landed on **7,048** |
| B06 | `outside safe area` — the 42% caption ran to x = 2.10 on a ±1.80 frame |
| B07 | `text-on-text 45%` — the x-axis caption landed on the y-axis caption |
| B08 | `text-on-text 73%` — the plate note landed on **ground 1.0 Ga old** |

All five have the same root cause and the same fix. Portrait has 4.64 units of
figure band and 3.6 of width; a landscape column of eight stacked rows does
not fit under a plate. Every fix turned stacked pairs into **side-by-side**
pairs — value beside caption, head beside sub — halving the row count. The
plates also shrank (B07 6.20→3.00, B08 6.20→2.60 units).

### The prop audit (0 found, and that is the point)

Ep. 17 nearly shipped a verdict page rendering the component's demo text
because zod silently drops unknown keys. This build audited all four Remotion
beats against the three schemas **before** rendering: 8/4/8/4 props, zero
unknown. The composer's `folderLabel` was set explicitly on B00 and B12,
because its schema default is `@NikBearBrown`.

Verified in the rendered frames at native 4K, both aspects: the footer chip
reads **@HumanitariansAI**.

### Two plates were redrawn before a single frame rendered (2)

Caught by reading the generated PNGs, not by any gate — a plate is an
`ImageMobject` and no gate can see inside one.

- **`cost.png` taught the opposite of its beat.** On an absolute time axis the
  two age windows are 0.90 and 0.56 Gyr — only 1.6× apart — so the figure read
  as "about the same" while the beat says 90% against 16%. The cost is the
  window *relative to the age being measured*, so a second panel was added:
  each window drawn over a bar running 0 → its own age. The young bar is
  swallowed whole; the old one takes a nick at the end.
- **`pile.png` read as a linear axis**, making the automation gap look like
  ~4× instead of ~78×. Decade rails were added, and B04 now lands
  "log scale — every rail is another ×10" *before* any row label.

---

## 2. Defects the gates missed, found by reading frames (2)

Both are landscape. Both passed **GATE B 20/20 strict**, GATE A 10/10, GATE W
10/10, and GATE V. Both were obvious the moment a rendered frame was opened.

### B10 — "175x tighter" overlapped the counterweight by ~1.5 units

`big` was placed at x = −2.30 and `cw` at x = +2.10 on the same line. The
counterweight is a 54-character sentence; after `_fit` to 7.60 units it ran
from −1.70 to 5.90, straight through the headline numeral. The rendered frame
shows `175x tighter` and `and the new anchor moved…` printed on top of one
another.

**Why no gate saw it:** GATE B audits sampled frames. These two land in
consecutive plays near the end of the beat, and its sample points fell either
side. Fixed by stacking them (both x = 0, y = −1.05 and −1.70).

### B06 — the "42%" numeral touched the caption above it

`n` at y = −0.70 spanned −1.05..−0.35; the 57% caption at y = −0.25 spanned
−0.38..−0.12. A gap of **0.03 units** — three pixels at 4K — which reads as
contact. The lower third of the frame was also dead space, a FILL-THE-CANVAS
defect in its own right.

Fixed by moving the row to y = −0.95, widening the horizontal separation
(x = −4.00 / +1.10), and spreading the two bars (y1 1.40→1.55, y2 0.05→0.30).

**The general lesson, again:** GATE B's overlap test needs the two mobjects to
coexist *in a sampled frame*. Elements revealed in different plays can collide
in the final composition and never be sampled together.

---

## 3. GATE V exits 2 on both cuts — and both flags were measured, not assumed

```
16:9   frames=28   BLOCKER=0   MAJOR=1
9:16   frames=28   BLOCKER=0   MAJOR=2
```

### 16:9 — one `low-contrast` on B08_50

`final_frame_check.py` builds ONE ink colour per frame as the mean of every
non-background pixel, then flags the frame if that mean sits within 0.3
luminance of the page. A pale plate therefore drags the flag, because the flag
tracks **plate area**, not legibility.

So the beat was swept at eight points and the type measured directly — the
darkest decile of non-background pixels against the modal page colour:

| sample | mean-ink sep | **type WCAG** | share of "ink" below AA |
|---|---|---|---|
| B08_15 | 0.551 | **10.7:1** | 61% |
| B08_25 | 0.328 | **8.4:1** | 86% |
| B08_40 | 0.309 | **7.0:1** | 90% |
| B08_50 | 0.312 | **6.9:1** | 89% |
| B08_60 | 0.339 | **7.2:1** | 86% |
| B08_70 | 0.353 | **7.1:1** | 85% |
| B08_85 | 0.395 | **8.3:1** | 79% |
| B08_95 | 0.404 | **8.2:1** | 80% |

AA is 4.5:1. The type never drops below **6.9:1**, while 79–90% of what the
gate averages is pale plate.

**And the frame itself explains the exact sample.** Opened at native 4K,
B08_50 is caught **mid-fade**: the numeral `90%` and its caption are at
partial opacity as they reveal. GATE V samples at a fixed 50% of the beat;
that instant falls inside the `a_val`/`a_sub` fade-in, which begins at 5.88 s
of a 12.54 s beat. Half-opacity type plus a pale plate is what pushed the
mean under the floor.

Not a defect. Making it quiet would mean darkening the plate — degrading the
design to satisfy a whole-frame average.

### 9:16 — two `underfill` on B11 (54% against a 55% floor)

The `*916` verdict card reserves bands at top and bottom for platform UI by
design, while GATE V measures a safe area derived from the 16:9 layout.
Measured on the rendered 2160×3840 frame:

```
content bbox     x 143..2017   y 519..3361
top reserve      13.5% of height
bottom reserve   12.5% of height
side reserve     6.6% / 6.6%
card area        64.2% of the full frame
```

The card is **64.2% of the frame**. The 54% is against a different box, and
the shortfall is one percentage point. The frame was read: the title is
intact, all five artifact lines are complete and legible, nothing is clipped.

Not a defect — an aspect mismatch between the component's design and the
gate's reference box.

### But the dismissal does not generalise

On Ep. 17 an `underfill` flag on B01 was **completely real** — a nine-frame
sweep showed 30% fill for 4.6 s of an 8.4 s beat because the beat's chrome was
revealed in its last play. That fix is carried forward in this reel's B01,
which lays its series line and corner bug down in the *third* play, not the
last. GATE V raised nothing on B01 in either cut here.

Sweep the beat before deciding which kind of flag you have.

---

## 4. Verified NOT defects

Each checked by opening a rendered frame at native resolution, in the aspect
named.

- **Composer footer chip** — `@HumanitariansAI` on B00 and B12, both aspects.
  The schema default is `@NikBearBrown` and Ep. 17 shipped it by accident.
- **B11 portrait title** — reads `The Clock Needs a Rock`, not truncated. The
  `- one page` tag is stripped for 9:16 only, pre-emptively, because the
  narrower 916 card truncated Ep. 17's title at exactly this spot.
- **B13 outro** — title, terracotta period, `@HumanitariansAI`,
  `Claude for Astronomy - Ep. 18`. Correct props, no defaults.
- **B00 cold open** — greeting `Ciao, HAI` (the least-recently-used short form
  in the Hi/Ola/Hej/Ciao cycle), segment, command, and all three output lines.
- **Pacing parity across aspects** — every Manim clip has an *identical frame
  count* in both cuts (B01 237, B02 321, B03 283, B04 274, B05 281, B06 303,
  B07 319, B08 296, B09 230, B10 302). Every scene plays the same reveals in
  both aspects, which is why **no `RT_PORTRAIT` was needed anywhere** in this
  reel — the landscape pacing solve is correct for portrait.
- **Masters carry no slates.** `compile.py` refuses a clean master that still
  has them; both cuts report 14/14 filled.

---

## 5. Build-process defects worth recording

- **`run.sh` renders nothing for this reel.** Its scene discovery matches
  `class X_Y(Scene)`, and every scene here subclasses `Paced`. It finds zero
  scenes, renders zero, and exits 0. Ep. 17 hit this too. Manim is rendered by
  an explicit script instead.
- **`run.sh` cannot read this `scenes.py`.** It opens the file with no
  encoding, so on this machine cp1252 raises `UnicodeDecodeError` on the
  box-drawing rules. `PYTHONUTF8=1` is set for every child process.
- **Never render Manim while Remotion is running in the same folder.** A
  four-scene re-render failed on its first scene during a concurrent Remotion
  pass and succeeded immediately afterwards, alone. The house rule "one Manim
  process at a time per reel folder" extends to the Chrome-based renderer.
- **Portrait Manim must render from the PARENT folder, not from `short/`.**
  `scenes.py` resolves plates as `HERE/assets/plots`, and `short/` has no
  `assets/`. Rendering there would fall back to blank plates — six empty
  figure boxes that every gate would pass. The aspect comes from `-r`, not
  from the working directory.

---

## 6. What was looked at

Rendered frames opened at native resolution during this build:

- 16:9 Manim: B03, B06 (×2, before and after fix), B08, B10 (×2)
- 16:9 Remotion: B00 full + footer crop, B11, B13
- 16:9 master: B08 swept at 15/25/40/50/60/70/85/95%
- 9:16 master: B03, B06, B07, B08, B11 (×2, plus a measured bounding box)
- All six plates, before any scene was written

Plus GATE B's annotated PNGs for all 20 scene/aspect pairs.
