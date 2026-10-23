# BUILD-PROMPT — *What The Model Would Say.*

Ep. 14 · `stellar-spectra-labels`
How to rebuild this reel from scratch, and what will bite you.

```bash
ART="E:/NEU/Jobs/Humanitarians_AI/brutalist.art"      # the DOT tree — public toolkit
PY="$ART/.venv/Scripts/python.exe"
REEL="D:/study_other/new_humanitarians/humanitarians-youtube/claude-for-astronomy/stellar-spectra-labels"
```

> `brutalist.art` (DOT) is the public toolkit. `brutalist-art/` and
> `brutalist_art/` are different trees. **Never treat a separator as a typo.**

---

## 0. The experiment

```bash
cd "$REEL" && "$PY" -I assets/gen_stars.py
```

Dependencies: numpy and Pillow. **No sklearn, no matplotlib** — the model and
every plate are written out by hand. The student is the real published form: a
quadratic polynomial in the labels fitted at every wavelength pixel and
inverted at test time by Gauss-Newton. Using the real method is the point,
because the episode's subject is *what the model is actually fitting*.

**Seed 1414.** The line bank that defines "nature" is drawn once from a frozen
seed, so the star→spectrum function is identical on every run. The script
**asserts three claims and writes nothing if any fails**. Expect:

```
  precision (repeat measurement) 0.0083 dex
  vs teacher labels  rms 0.0329
  vs truth           rms 0.1280  bias +0.0263
  error vs Teff: correlation 0.995  slope +0.178 dex/kK
  control  (unbiased teacher) 0.0129  corr -0.131
  anchored (120 stars)        0.0318  corr -0.139
  -> all three hold. writing plates.
```

Six plates, 1560 px wide. **They carry imagery only** — no text, no ticks, no
legend. Every label on screen is a Manim mobject placed *outside* the plate,
because a plate is an `ImageMobject` and GATE B is nearly blind to it.

The teacher's bias (`bias=0.18` dex per 1000 K) is **injected deliberately**
so the gap can be measured. It is not a claim about ASPCAP. Keep that
distinction in the voice and in FACTCHECK.md.

---

## 1. GATE P binds

A human signs `PEDAGOGY.md` with `VERDICT: PASS` **before** audio is
generated. It is a quality gate, not a cost gate — the audio is free.

Run the free gates *before* the signature, so a scene that fails them is not
rebuilt after a human has already approved its content:

```bash
"$PY" -I "$ART/runtime/qc/beat_lint.py" "$REEL"
for c in B01_Presenter B02_OneBreath B03_TheMethod B04_TheData B05_TheChain \
         B06_Agrees B07_TheTruth B08_Precision B09_Structure B10_TheTell; do
  "$PY" -I "$ART/runtime/qc/static_scene_check.py" "$REEL/scenes.py" --class "$c"
  "$PY" -I "$ART/runtime/qc/wcag_margin_check.py" "$REEL/scenes.py" --class "$c" --palette claude
  (cd "$REEL" && "$PY" -I "$ART/runtime/qc/manim_layout_audit.py" scenes.py --class "$c")
  (cd "$REEL" && "$PY" -I "$ART/runtime/qc/manim_layout_audit.py" scenes.py --class "$c" --portrait)
done
```

`manim_layout_audit.py` **overwrites `layout_audit.md` per class**, so read it
inside the loop or run against a scratch copy of `scenes.py` + `assets/plots/`.

**Then look at 20 frames before the signature.** It found two defects here
that every gate passed.

---

## 2. Audio is the clock

```bash
"$PY" -I "$ART/runtime/scripts/generate_audio_kokoro.py" "$REEL"
```

Kokoro `af_bella`, local, $0.00. Measured durations land in
`beat_sheet.json` as `actual_duration_s` and are **ground truth**. Never fix
timing by hand — regenerate audio and recompile.

Expect ~155.07 s. The words-only estimate has been noise of ±5–10 % with no
consistent sign across Eps. 06–14; this one came in +5.4 %.

---

## 3. Pacing, in both aspects

```bash
"$PY" -I <scratch>/nat14.py        # natural lengths, no render
"$PY" -I <scratch>/pace14.py       # solves RT/HOLD, rewrites scenes.py
"$PY" -I <scratch>/natboth14.py    # play-count parity, both aspects
"$PY" -I <scratch>/verify14.py     # the real filled length per aspect
```

**The pacing solve runs ONCE, in landscape.** A scene whose portrait branch
plays a different number of reveals will not match. Five scenes here drop
on-screen-only extras in portrait and so underfill; they carry `RT_PORTRAIT`,
a second RT kept deliberately **off** the `BEAT, RT, HOLD` line so
`pace14.py`'s regex still rewrites the canonical one.

`verify14.py` is the check that matters — `natboth14.py` measures with RT
forced to 1.0 and will keep reporting a mismatch even after `RT_PORTRAIT`
has corrected the timing. Require:

```
PASS: every scene lands UNDER its beat in BOTH aspects
```

A scene landing above −0.15 s is floored; lower its RT. **Do not reach for a
trim knob** — a per-scene TRIM override was built and tried on four scenes
across two episodes and moved the duration by exactly zero every time. At the
1.55 RT cap the remaining lever is HOLD.

---

## 4. Render

```bash
bash <scratch>/r14.sh land     # 3840x2160 -> manim/
bash <scratch>/r14.sh port     # 2160x3840 -> _portrait/
```

**ONE Manim process at a time per reel folder.** Concurrent renders corrupt
each other's ffmpeg concat (Ep. 07). ~20–30 min per aspect at 4K.

Portrait B08 will report `fps-sync=False`: 334 decodable frames against a
13.833 s container duration. It reproduces deterministically and is
**harmless** — `compile.py` retimes every clip to its beat and truncates with
`-t`. Remuxing does not fix it and an `fps` filter makes it worse.

---

## 5. Bookends and compile

```bash
"$PY" -I "$ART/runtime/scripts/remotion_scenes.py" "$REEL" --now "<iso8601>"
"$ART/art" final "$REEL"                      # clean master, --height 2160
```

**Render Remotion only via `remotion_scenes.py`, in the foreground.** Never
hand-roll `npx remotion render`.

`art final` does *not* pass `--review`, so no labels are burned in — the
`drawtext: yes` line in the summary reports the capability, not the output.

---

## 6. The 9:16

```bash
"$PY" -I "$ART/runtime/scripts/shorts.py" "$REEL" --drop --no-endcard
cp "$REEL"/_portrait/B0*.mp4 "$REEL"/_portrait/B10.mp4 "$REEL/short/manim/"
"$PY" -I "$ART/runtime/scripts/remotion_scenes.py" "$REEL/short" --now "<iso8601>"
"$PY" -I "$ART/runtime/scripts/compile.py" "$REEL/short" --height 3840
```

`--drop` with no values keeps all 14 beats — this is a full-length vertical
cut, not a short. `shorts.py` rewires the four Remotion beats to their `916`
compositions and they **must** be re-rendered; any centre-cut leftover is
stale garbage.

---

## 7. GATE V — pass `--mp4` explicitly. Always.

```bash
cd "$REEL"
"$PY" -I "$ART/runtime/qc/final_frame_check.py" . --mp4 claude-for-astronomy_OmMali_23_10_2026.mp4
mv _qc/REPORT.md _qc/REPORT-16x9.md ; mv _qc/contact_sheet.png _qc/contact_sheet-16x9.png
"$PY" -I "$ART/runtime/qc/final_frame_check.py" . --mp4 stellar-spectra-labels-9x16.mp4
mv _qc/REPORT.md _qc/REPORT-9x16.md ; mv _qc/contact_sheet.png _qc/contact_sheet-9x16.png
```

Given only a folder it takes `glob("*.mp4")[0]`, and `-9x16.mp4` sorts before
`.mp4`, so it grades the vertical file while reporting the landscape one.
A bare call after the 9:16 exists is silently wrong.

**The contact sheet only covers B00–B07.** Extract B08–B13 from the master
yourself at 85 % of each beat and look at them.

---

## 8. Deliver

16:9 → `claude-for-astronomy_OmMali_DD_MM_YYYY.mp4` (weekly: Ep. 14 =
23_10_2026). 9:16 keeps the slug → `stellar-spectra-labels-9x16.mp4`.

**Never publish.** There is no publishing machinery here; the masters stay in
this folder.

---

## The traps, condensed

1. A plate's **frame** is a curve, so GATE B catches a label crossing a
   plate's *outline* but not one in its *interior*. Read the frames.
2. **Same-colour-on-same-colour is invisible to every gate.** B08's 15× span
   was drawn on the bar it measured and no gate noticed.
3. `FadeOut` takes a plate's frame with it — give the replacement one too.
4. Never write `pat[0] ± pw * k` for a label *outside* a plate: landscape
   pw = 6.6 in a 12.3-unit frame fits, portrait pw = 3.4 in 3.6 does not.
5. Keep ≥ 0.15 units between elements. 0.04 is eleven pixels at 4K.
6. Patch scripts that `assert` out mid-run write nothing — the next command
   then cheerfully reports "syntax OK" on the unmodified file.
7. When a measurement refuses a claim, **rewrite the claim, never tune the
   experiment.**
