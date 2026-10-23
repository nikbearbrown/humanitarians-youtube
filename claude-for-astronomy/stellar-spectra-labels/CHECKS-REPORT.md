# CHECKS-REPORT — *What The Model Would Say.*

Ep. 14 · `stellar-spectra-labels` · pre-audio gate run, 2026-10-23

Gates F, L, A, W and B all run **before** GATE P, because they are free and
because a scene that fails them would have to be rebuilt after the human had
already signed off on its content. Audio, pacing, render, GATE V and the 9:16
derivative all come **after** the signature.

---

## Summary

| Gate | What it checks | Result |
|---|---|---|
| **F** | paperwork complete | **PASS** |
| **L** | beat mix / ledger | **PASS** — clean |
| **A** | render-free scene pre-flight | **PASS** — 10/10 clean |
| **W** | WCAG contrast + safe margins | **PASS** — 10/10 clean |
| **B** | pixel layout, landscape | **PASS** — 10/10, 0 errors 0 warnings |
| **B** | pixel layout, portrait | **PASS** — 10/10, 0 errors 0 warnings |
| **pre-flight** | 20 frames read by eye | **2 defects found and fixed** — see below |
| **P** | human signature | **PASS** — signed 2026-10-23 |
| **V** | 16:9 master, explicit `--mp4` | **PASS** — 28 frames, 0 BLOCKER, 0 MAJOR |
| **V** | 9:16 master, explicit `--mp4` | **PASS** — 28 frames, 0 BLOCKER, 0 MAJOR |
| frame reading | both cuts, B08-B13 extracted separately | clean — see `VISUAL-QC.md` |

> **GATE T and GATE SHARPNESS are not shipped in this toolkit**, despite
> `ai-explainer/SKILL.md` describing GATE T as "ALWAYS RUN". Noted here for the
> eighth consecutive episode rather than silently skipped.

---

## GATE F — paperwork

| File | Status |
|---|---|
| `SOURCES.md` | present — verbatim DR14 and Ness et al. quotes, anchor caveats, deliberately-unused list |
| `FACTCHECK.md` | present — every on-screen claim, PUBLISHED vs COMPUTED, plus five refused claims |
| `SHOTLIST.md` | present — 14 beats, lanes, aspect discipline |
| `PROMPTS.md` | present — records that **no image-generation prompts were used** |
| `PEDAGOGY.md` | present — awaiting signature |
| `beat_sheet.json` | 14 beats, 437 words |
| `assets/spectra.py`, `assets/gen_stars.py` | the experiment and the plates |
| `scenes.py` | 10 aspect-aware scenes |

## GATE L — beat lint

```
[beat-lint] clean — beat mix OK (beat_sheet.json)
```

14 beats: 4 Remotion (B00, B11, B12, B13) + 10 Manim (B01–B10). The ledger
agrees: `[todo] 0/14 filled`, every Manim beat routed to `manim/B0*.mp4` and
every Remotion beat to `media/B*.mp4`.

## GATE A — render-free pre-flight

All ten scenes execute `construct()` start to finish against the geometry stub
with no Python error and no out-of-frame coordinate:

```
B01_Presenter  B02_OneBreath  B03_TheMethod  B04_TheData   B05_TheChain
B06_Agrees     B07_TheTruth   B08_Precision  B09_Structure B10_TheTell
→ 10 scene(s): 10 clean · 0 warn · 0 error
```

## GATE W — contrast and margins

All ten clean against the `claude` palette. The palette rule that matters:
`#B9B4A0` (ghost) is **2.0:1 on cream and fails WCAG**, so it is used for
strokes and fills only, never for text. Accented text uses `#A44A32` (4.7:1),
never the `#D97757` mark colour.

## GATE B — pixel layout, BOTH aspects

**Final: 20/20 clean, 0 errors, 0 warnings.**

| Scene | landscape | portrait |
|---|---|---|
| B01_Presenter | 0 / 0 | 0 / 0 |
| B02_OneBreath | 0 / 0 | 0 / 0 |
| B03_TheMethod | 0 / 0 | 0 / 0 |
| B04_TheData | 0 / 0 | 0 / 0 |
| B05_TheChain | 0 / 0 | 0 / 0 |
| B06_Agrees | 0 / 0 | 0 / 0 |
| B07_TheTruth | 0 / 0 | 0 / 0 |
| B08_Precision | 0 / 0 | 0 / 0 |
| B09_Structure | 0 / 0 | 0 / 0 |
| B10_TheTell | 0 / 0 | 0 / 0 |

### The three defects it caught on the first pass

**1 · B08 and B10 — the right-hand column crossed the plate.** (landscape,
3 warnings)

```
WARN · label on a curve/line: `thegapbetweenwhatyou`      box=[2.82, -0.41, 5.66, -0.11]
WARN · label on a curve/line: `wouldquoteandwhatistrue`   box=[2.66, -0.81, 5.82, -0.51]
WARN · label on a curve/line: `fourtimesmoreaccurate.`    box=[2.61,  0.03, 5.87,  0.29]
```

The right-hand column spans x 2.52…5.96. B06, B07 and B09 place their plate at
x = −1.10, so its right edge is 2.20 and the column clears it by 0.32. B08 and
B10 placed theirs at x = 0, reaching 3.30 — straight through the column.

**Why this one was visible at all is worth recording.** The standing lesson
from Eps. 11–13 is that *GATE B cannot see a label printed across a plate*,
because a plate is an `ImageMobject` and the gate only reasons about curves.
That is still true of the image. But `_plate()` also draws a **frame
Rectangle**, which *is* a curve — so a label crossing the plate's outline gets
caught even though one sitting in the middle of the image would not. The gate
found the edge case; it would not have found the interior.

Fixed by moving both plates to x = −1.10, so all five landscape plate beats now
share one geometry, with the rule written into the `RCOL_W` comment rather than
left as a per-scene number.

**2 · B05 — the portrait bracket label left the frame.** (portrait, 1 warning)

```
WARN · outside safe area: `notnature`  box=[-2.21, -0.72, -2.05, 0.44]
```

Portrait boxes 3.10 wide centred at x = 0 put their left edge at −1.55; the
bracket went 0.22 further and its rotated label 0.36 beyond that, landing at
x = −2.13 in a ±1.80 frame. Fixed by shifting the portrait chain to x = −0.30,
narrowing the boxes to 2.60 and hanging the bracket off the **right**, where
the label lands at 1.46 with an extent of 1.35…1.57.

**3 · Not a gate finding, but caught in the same pass:** `spectra.png` was
clipping the metal-rich spectrum's deepest lines against a fixed 0.3–1.0 flux
window — and that spectrum having the deepest lines is the entire point of the
plate. Fixed in `gen_stars.py` by normalising to the actual range across all
three spectra, and the plate was re-read by eye afterwards.

### What GATE B structurally cannot check here

Five of ten scenes are plate beats. The gate sees each plate's frame and
nothing inside it. So the following were verified **by arithmetic and by
reading frames**, not by the gate:

- every label is placed *outside* the plate rectangle, except two deliberate
  marks (B04's wavelength guide, B06/B07's traced diagonal), which carry
  `_qc_intentional`;
- bar-label columns derive from `BAR_FX`, the **measured** plate-internal bar
  positions (offsets of ∓0.309 × pw, safely inside the plate) rather than a
  guessed `pw × k`;
- B04's row labels sit at `SPEC_FY`, the measured row centres;
- B08's 15× span uses `_bar_fy()` to convert a value to a height fraction.

## Visual pre-flight — 20 frames, read before the signature

All ten scenes rendered at low resolution in both aspects and read as contact
sheets. This is the check CLAUDE.md rule 5 exists for, and on this reel it
matters more than usual: five of ten scenes are plate beats, and a gate that
only reasons about curves is close to blind on them.

**It found two defects that every gate passed.**

### 1 · B08 — the 15× span was drawn on top of the bar it was measuring

`x3 + 0.55` put the double-arrow exactly on bar three's right edge (the bar
spans x 0.38…1.50 in landscape). The arrow is the same terracotta as the bar,
so the shaft disappeared into it and only the two arrowheads showed, as small
ears above the bar top — while the `15x` tag floated in the right-hand column
with nothing connecting it to anything. The beat's central comparison did not
read at all.

**No gate can catch this.** Same-colour-on-same-colour is not an overlap that
GATE B, W or A tests; geometrically the arrow was exactly where it was asked
to be. Moved to x = 1.85 — 0.35 clear of the bar, 0.35 inside the plate's
right edge — and the span now reads as a span.

### 2 · B07 — the plate lost its frame mid-argument

`before` carries `frame=True`, but `FadeOut` takes its frame rectangle with
it, and `after` had been built with `frame=False`. So B06 ended with a framed
plate and B07 — the same plate geometry, one beat later, the beat whose whole
point is that *only the axis changed* — sat in a bare axes box. Side by side
in the sheet the border blinked off at precisely the moment the viewer is
being asked to trust that nothing moved. `after` now carries a frame too.

### What the frames confirmed as correct

- **B04** — the terracotta guide genuinely cuts a line that deepens down the
  stack: shallow in the metal-poor spectrum, deepest in the terracotta one.
  The measured pixel-47 position was right.
- **B03** — the isotype reads as a ratio. Five marks against a dense 24×24
  field is visibly ~100×, and the caption carries the rate.
- **B05** — the chain and its bracket read cleanly in both aspects, with the
  portrait bracket now on the right after the GATE B fix.
- **B06 → B07** — the points visibly leave the diagonal across the dissolve.
- **B08 / B10** — bar names sit under their own bars in landscape and become
  legend rows in portrait; no label touches a plate.
- **B09** — the zero rule, the terracotta fit and the trend all read; portrait
  names the rule in a note rather than in the margin it cannot reach.
- Every scene carries its footer, citation and wordmark bug.

Re-verified after both fixes: GATE A, W and B all still clean on B07 and B08
in both aspects.

## Pacing and play-count parity

**Solved and verified.** Measured narration totals **155.07 s (2:35.1)**,
+5.4 % against the words-only estimate — inside the usual +-5-10 % band.

Nine of ten scenes hit the RT 1.55 cap with HOLD taking the remainder; B01,
the shortest beat, solved at RT 0.906.

`natboth14.py` then found **five scenes whose portrait branch plays fewer
reveals** (B03, B06, B08, B09, B10), because portrait drops on-screen-only
extras. That underfills the beat: B08 portrait would have frozen on its last
frame for ~5 s of a 14 s beat. Undershoot is the SAFE direction -- a short
clip is freeze-padded, where a long one is centre-cut and loses its closing
line -- but it is dead air, not pacing.

Fixed with a new `RT_PORTRAIT` class attribute, kept deliberately OFF the
`BEAT, RT, HOLD` line so `pace14.py`'s regex still rewrites the canonical one.
`verify14.py` then computed the real filled length per aspect:

```
worst headroom +0.00 s
PASS: every scene lands UNDER its beat in BOTH aspects
```

Every one of the twenty clips lands exactly **+0.18 s** under its beat -- the
`TAIL_TRIM` -- so nothing was centre-cut in either cut.

`natboth14.py` compares play counts and animation totals in **both** aspects,
because the pacing solve runs once, in landscape. Ep. 11's B04 overshot its
beat by +0.92 s precisely because its portrait branch played more animations
than its landscape branch. Every scene in this reel was written so the two
branches differ in *placement* but not in *play count* — B03 and B09 are the
two that drop an element in portrait, and both drop it before any animation,
so the counts still match. `natboth14.py` will confirm that rather than
assume it.

## Numerical self-check

`assets/gen_stars.py` **asserts all three central claims and writes no plate if
any fails.** Re-verified reproducing on seed 1414, 2026-10-23:

```
  precision (repeat measurement) 0.0083 dex
  vs teacher labels  rms 0.0329
  vs truth           rms 0.1280  bias +0.0263
  error vs Teff: correlation 0.995  slope +0.178 dex/kK
  control  (unbiased teacher) 0.0129  corr -0.131
  anchored (120 stars)        0.0318  corr -0.139
  -> all three hold. writing plates.
```

## Remotion patterns

All four registered in `runtime/remotion/src/Root.tsx`, with dedicated 9:16
variants where the layout needs one:

| Pattern | 16:9 | 9:16 |
|---|---|---|
| `ClaudeComposerAsk` | ✔ | `ClaudeComposerAsk916` (same component) |
| `ClaudeVerdictArtifact` | ✔ | `ClaudeVerdictArtifact916` |
| `ClaudeTitleOutro` | ✔ | `ClaudeTitleOutro916` |

Rendered only via `runtime/scripts/remotion_scenes.py`, in the foreground.
Never `npx remotion render` by hand.

## Cost

**$0.00.** Kokoro `af_bella` locally for narration; Manim and Remotion for
picture; no image model; no ElevenLabs; no API keys. Fellow Tier throughout.
