# BUILD-LOG — *What The Model Would Say.*

Ep. 14 · `stellar-spectra-labels` · AI in Astronomy & Space Science
Built 2026-10-23 with `brutalist.art`, Fellow Tier, **$0.00**.

---

## Delivered

| | 16:9 | 9:16 |
|---|---|---|
| `claude-for-astronomy_OmMali_23_10_2026.mp4` | 3840 × 2160 · 155.07 s · 3721 frames · 15.8 MB | — |
| `stellar-spectra-labels-9x16.mp4` | — | 2160 × 3840 · 155.07 s · 3721 frames · 18.7 MB |

24 fps, h264 + AAC, −21.0 LUFS integrated (LRA 2.8 LU), both cuts sharing one
audio mix. **2:35.1** — 25 s inside the 3:00 cap. Both masters live in this
folder. **Nothing was published.**

---

## The episode

Topic 14 of the brief is "AI reading stellar spectra to determine
composition/age/distance faster than manual analysis". That is true, and the
reel says so. The episode is about the sentence after it: *trained on what?*

A data-driven spectral model contains no physics. Everything it knows arrives
through its reference labels — and those labels are themselves the output of a
physics pipeline. So it does not predict the star. It predicts what that
pipeline would say about the star, and it inherits that pipeline's
systematics while reporting a precision that cannot see them.

This is the first episode in the series where **the limit is in the labels
themselves** — not in how they were split, sampled, scored or defined. The
data is real, the method is sound, the evaluation is honest, every check
performed against the labels passes, and the answer is still wrong.

---

## What was measured

`assets/gen_stars.py`, seed **1414**, asserts three claims and writes no plate
if any fails. The student is the real algorithm: a quadratic polynomial in the
labels fitted at every wavelength pixel, inverted at test time by
Gauss-Newton.

| [Fe/H], 400 test stars | |
|---|---|
| repeat-measurement precision | **0.0083 dex** |
| agreement with its training labels | **0.0329 dex** |
| **against the truth** | **0.1280 dex — 15.3× the precision** |
| teacher vs truth | 0.1348 dex |
| error vs Teff | correlation **0.995**, slope **+0.178 dex/kK** |
| control, unbiased teacher | 0.0129 dex, corr −0.131 |
| anchored, 120 independent labels | 0.0318 dex, corr −0.139 |

Four times fewer labels, four times more accurate.

---

## Gates

| Gate | Result |
|---|---|
| F — paperwork | PASS |
| L — beat lint | PASS, clean |
| A — render-free pre-flight | PASS, 10/10 |
| W — WCAG + margins | PASS, 10/10 |
| B — layout, landscape | PASS, 10/10 after 2 fixes |
| B — layout, portrait | PASS, 10/10 after 1 fix |
| Visual pre-flight, 20 frames | **2 further defects found and fixed** |
| P — human signature | PASS, signed 2026-10-23 |
| V — 16:9 master | 28 frames · 0 BLOCKER · 0 MAJOR |
| V — 9:16 master | 28 frames · 0 BLOCKER · 0 MAJOR |
| Frame reading, both cuts | clean |

**GATE T and GATE SHARPNESS were not run: they are not shipped in this
toolkit**, despite SKILL.md describing GATE T as "ALWAYS RUN". Eighth
consecutive episode recording this.

---

## The five things that caught me

### 1 · GATE B can see a plate's frame, even though it cannot see the plate

The standing lesson from Eps. 11–13 is "GATE B cannot see a label printed
across a plate", because a plate is an `ImageMobject`. True of the *image* —
but `_plate()` also draws a frame **Rectangle**, which *is* a curve. So a
label crossing a plate's *outline* is caught while one in its *interior* is
not.

That edge flagged B08 and B10, whose plates sat at x = 0 (right edge 3.30)
under a right-hand column spanning 2.52…5.96. Fixed by moving both to
x = −1.10, so all five landscape plate beats share one geometry, with the rule
written into the code rather than left as a per-scene number.

### 2 · B05's portrait bracket label left the frame

Boxes 3.10 wide centred at 0 → left edge −1.55; bracket −1.77; rotated label
−2.13, in a ±1.80 frame. Shifted the portrait chain to −0.30, narrowed the
boxes to 2.60 and hung the bracket off the **right**.

### 3 · The 15× span was drawn on top of the bar it was measuring

`x3 + 0.55` put the double-arrow exactly on bar three's right edge, in the
same terracotta as the bar. The shaft vanished into it; only the arrowheads
showed, as two small ears above the bar top, and the `15x` tag floated
unconnected. **The beat's central comparison did not read.**

No gate can catch this — same-colour-on-same-colour is not an overlap any of
them test, and geometrically the arrow was exactly where it was asked to be.
Found by reading the frame. Moved to x = 1.85.

### 4 · B07 lost its plate frame at the worst possible moment

`FadeOut` takes `before`'s frame rectangle with it, and `after` was built
`frame=False`. So B06 ended framed and B07 — same geometry, one beat later,
the beat whose entire argument is *only the axis changed* — sat in a bare
axes box. The border blinked off exactly where the viewer is asked to trust
that nothing moved. Also found by reading frames.

### 5 · Five portrait branches underfilled their beats

The pacing solve runs once, in landscape. Five scenes drop on-screen-only
extras in portrait and so play fewer reveals; B08 portrait would have frozen
for ~5 s of a 14 s beat. Undershoot is safe — a short clip is freeze-padded,
where a long one is centre-cut and loses its closing line — but that is dead
air, not pacing.

Added `RT_PORTRAIT` to the chassis: a second, larger RT for that aspect, kept
off the `BEAT, RT, HOLD` line so `pace14.py`'s regex still rewrites the
canonical one. A larger RT in portrait is right on its own terms — portrait
shows fewer things, so each can afford longer to arrive. After it, **every
scene lands exactly +0.18 s under its beat in both aspects**.

---

## Also recorded

**`spectra.png` was clipping the point of its own plate.** A fixed 0.3–1.0
flux window cut the metal-rich spectrum's deepest lines — and that spectrum
having the deepest lines is the entire reason the plate exists. Normalised to
the actual range across all three.

**Portrait B08 has two duplicate-PTS frames.** Manim's partial-movie concat
produces 334 decodable frames but a container duration of 13.833 s (= 332
frames). It reproduces deterministically; remuxing and re-stamping do not fix
it, and an `fps` filter made it worse by dropping to 331. It is **harmless
here**: `compile.py` retimes every clip to its beat and truncates with `-t`,
so both aspects fill 14.10 s exactly and all 334 frames are present. Recorded
rather than papered over.

**A `folderLabel` prop was dropped by zod on B11.** `ClaudeVerdictArtifact`
has no such field and renders no handle at all, so nothing fell back to wrong
text. Removed from the sheet so it matches what rendered.

---

## Pipeline, in order

```
research → gen_stars.py (asserts 3 claims) → beat_sheet.json → paperwork
→ GATES F L A W B (both aspects) → 20-frame visual pre-flight
→ GATE P (human) → Kokoro audio (the clock) → nat14 → pace14
→ verify14 (both aspects) → 20 Manim renders at 4K, SEQUENTIALLY
→ Remotion bookends (foreground) → compile → GATE V --mp4
→ 9:16 via shorts.py --drop --no-endcard, portrait clips staged,
  916 bookends re-rendered, compile --height 3840 → GATE V --mp4
→ read frames → paperwork → dated delivery name
```

**Pass `--mp4` explicitly to the frame check. Always.** With two cuts in the
reel root, `glob("*.mp4")[0]` picks `…-9x16.mp4` before `…-cut.mp4`, and the
gate silently grades the wrong file while reporting the other.

---

## Cost

**$0.00.** Kokoro `af_bella` locally; Manim and Remotion for picture; no image
model, no ElevenLabs, no API keys. Fellow Tier throughout.
