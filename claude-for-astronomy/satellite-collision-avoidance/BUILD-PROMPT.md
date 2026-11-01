# BUILD-PROMPT — *Safer By Not Looking.*

Ep. 15 · `satellite-collision-avoidance` · the series finale
How to rebuild this reel from scratch, and what will bite you.

```bash
ART="E:/NEU/Jobs/Humanitarians_AI/brutalist.art"      # the DOT tree — public toolkit
PY="$ART/.venv/Scripts/python.exe"
REEL="D:/study_other/new_humanitarians/humanitarians-youtube/claude-for-astronomy/satellite-collision-avoidance"
```

> `brutalist.art` (DOT) is the public toolkit. `brutalist-art/` and
> `brutalist_art/` are different trees. **Never treat a separator as a typo.**

---

## 0. The experiment

```bash
cd "$REEL" && "$PY" -I assets/gen_conj.py
```

Dependencies: numpy, scipy (`i0e`) and Pillow. The integral is the real
short-encounter one, in its **numerically stable** form — the naive version
overflows for d/σ ≳ 30, which is exactly the well-tracked regime the episode
is about.

**Seed 1515.** Four claims are ASSERTED; nothing is written if any fails:

```
  Pc peaks at sigma 212.1 m  (d/sqrt(2) = 212.1)   Pc = 1.635e-03
  Pc crosses 1e-04 at sigma 1397.7 m on the dilution branch
  degraded sigma 5000.0 m -> Pc 7.986e-06
  max-Pc (scale-free)     -> 1.635e-03
  final risk >= 1e-4 : 180 of 120,000 (0.15%)
                        all MSE   notified MSE
  persistence            0.0609          1.275
  ridge                  0.0152          4.130
  -> all four hold. writing plates.
```

**Draw the miss distance uniform in AREA, not log-uniform.** Conjunctions are
screened in a box and the count below distance *d* grows like *d²*.
Log-uniform gives a 41 % high-risk population; uniform-in-area gives 0.15 %,
the order ESA reports. The rarity must come from the geometry.

**Clip the risk at the 1e-6 floor**, as ESA's own baseline does. Without it
the squared error is dominated by the gap between 1e-25 and 1e-12, both of
which mean "will not happen".

Plates carry **imagery only**. Every label is placed by `scenes.py` outside
the plate.

---

## 1. GATE P binds

A human signs `PEDAGOGY.md` with `VERDICT: PASS` **before** audio. Run the
free gates first — L, A, W, and B in **both** aspects — and then **look at 20
frames**. On this reel the frames found three defects the gates passed,
including an isotype whose entire point was invisible.

`manim_layout_audit.py` overwrites `layout_audit.md` per class, so read it
inside the loop or audit a scratch copy.

---

## 2. Audio is the clock

```bash
"$PY" -I "$ART/runtime/scripts/generate_audio_kokoro.py" "$REEL"
```

Expect ~158.9 s. The words-only estimate has been ±5–10 % with no consistent
sign across Eps. 06–15.

---

## 3. Pacing, in both aspects

```bash
"$PY" -I <scratch>/nat15.py       # natural lengths, no render
"$PY" -I <scratch>/pace15.py      # solves RT/HOLD, rewrites scenes.py
"$PY" -I <scratch>/natboth15.py   # play-count parity
"$PY" -I <scratch>/verify15.py    # the real filled length per aspect
```

**Seven of ten scenes need `RT_PORTRAIT` here.** Every landscape right-hand
column becomes stacked rows in portrait, and B03/B09 drop chips and quotes
entirely, so those branches play fewer reveals and would freeze on a held
frame. Keep `RT_PORTRAIT` **off** the `BEAT, RT, HOLD` line so `pace15.py`'s
regex still rewrites the canonical one.

`verify15.py` is the check that matters — `natboth15.py` measures with RT
forced to 1.0 and keeps reporting a mismatch after the fix. Require:

```
PASS: every scene lands UNDER its beat in BOTH aspects
```

---

## 4. Render

```bash
bash <scratch>/r15.sh land     # 3840x2160 -> manim/
bash <scratch>/r15.sh port     # 2160x3840 -> _portrait/
```

**ONE Manim process at a time per reel folder.**

---

## 5. Bookends, compile, GATE V

```bash
"$PY" -I "$ART/runtime/scripts/remotion_scenes.py" "$REEL" --now "<iso8601>"
"$ART/art" final "$REEL"
cd "$REEL" && "$PY" -I "$ART/runtime/qc/final_frame_check.py" . \
    --mp4 claude-for-astronomy_OmMali_30_10_2026.mp4
```

**Render Remotion only via `remotion_scenes.py`, in the foreground.**

**Pass `--mp4` explicitly. Always.** Given only a folder the gate takes
`glob("*.mp4")[0]`, and `-9x16.mp4` sorts before `.mp4`.

---

## 6. The 9:16

```bash
"$PY" -I "$ART/runtime/scripts/shorts.py" "$REEL" --drop --no-endcard
cp "$REEL"/_portrait/B*.mp4 "$REEL/short/manim/"
"$PY" -I "$ART/runtime/scripts/remotion_scenes.py" "$REEL/short" --now "<iso8601>"
"$PY" -I "$ART/runtime/scripts/compile.py" "$REEL/short" --height 3840
```

`--drop` with no values keeps all 14 beats. The four Remotion beats are
rewired to their `916` compositions and **must** be re-rendered.

---

## 7. Deliver

16:9 → `claude-for-astronomy_OmMali_DD_MM_YYYY.mp4` (Ep. 15 = 30_10_2026).
9:16 keeps the slug. **Never publish.**

---

## The traps, condensed

1. **A gate passing is not the frame being right.** B04's display gamma 0.09
   passed GATE V at 0.34 and rendered a picture arguing the *opposite* of the
   episode's thesis. Render it, look at it, reject it.
2. **When a knob can't satisfy both the gate and the meaning, the knob is the
   wrong lever.** Redraw. Here: a shaded density field became covariance
   ellipses, which are higher-contrast *and* more standard.
3. **Buy contrast by removing pale ink, not by adding dark.** Ghost-grey
   strokes sit just above GATE V's ink threshold and drag the mean hard —
   deleting three per-panel borders was worth +0.025.
4. **A contrast margin that depends on elements portrait drops is not a
   margin.** B09 passed 16:9 and failed 9:16 on exactly that.
5. **A plate's frame is a curve; its image is not.** GATE B catches a label
   crossing a plate's outline, never one inside it.
6. Never write `pat[0] ± pw * k` for a label *outside* a plate.
7. Keep ≥ 0.15 units between elements; 0.04 is eleven pixels at 4K.
8. **When a measurement refuses a claim, rewrite the claim, never tune the
   experiment.** It happened again here, and the rewritten claim was better.
9. **Don't draw the picture you expected.** `shrink.png` was drawn to show
   late-breaking alerts; there are zero in 120,000.
