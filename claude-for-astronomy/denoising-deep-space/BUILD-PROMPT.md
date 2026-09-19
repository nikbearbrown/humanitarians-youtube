# BUILD-PROMPT — rebuild *The Sharpest Guess.* from this folder

Ep. 09 · `denoising-deep-space`. Everything below is free and local. **No API
keys.** If any step appears to want one, stop — that is a toolkit bug, not a
missing credential (CLAUDE.md rule 7).

## Paths

```
TOOLKIT=E:/NEU/Jobs/Humanitarians_AI/brutalist.art          # brutalist.art — the DOT tree
REEL=D:/study_other/new_humanitarians/humanitarians-youtube/claude-for-astronomy/denoising-deep-space
PY="$TOOLKIT/.venv/Scripts/python.exe"
```

`brutalist.art` (dot) is **not** `brutalist-art/` or `brutalist_art/`.

## Two Windows preambles — both required, every invocation

```bash
export PYTHONUTF8=1 PYTHONIOENCODING=utf-8
```

Without these the Python scripts die on cp1252 as soon as narration carries
typographic punctuation.

**And call `$PY` explicitly — never `python3`.** A Windows venv ships
`python.exe` but no `python3.exe`, so `python3` falls through to the system
Python, which has none of the toolkit's dependencies. That is what made Ep. 08's
first audio run fail with `pip install kokoro-onnx`.

## Hard rule: render one Manim process at a time

**Two Manim processes writing into one reel folder corrupt each other's
output** — the concat step silently drops frames (Ep. 07: a 7.51 s beat came out
7.083 s with all fourteen partial files summing to exactly the right count). Do
not parallelise the aspects. After killing a render job, **check mtimes for
monotonicity**: `TaskStop` kills the shell, not the Manim child.

## Rebuild

### 0. Plates (only if you change the physics or the seed)

```bash
cd "$REEL" && "$PY" assets/gen_deconv.py     # seed 9109 → assets/plots/
rm -rf media/videos                          # REQUIRED — see the note at the end
```

numpy, scipy and Pillow. **No matplotlib** — the venv does not ship it.

The script **asserts two claims** and writes nothing if either fails. Expect:

```
striping: pattern recovered to 3.58%          -> REMOVABLE
information above cutoff: 19.2% of the truth, and 1.3x the noise
truths differ by 52.4%  |  their images differ by 0.0000 noise sigma  -> PASS
chi2/N: smooth=1.008  matched=1.007  rough=1.008 ... differ by 35.9%
above the cutoff the posterior variance equals the PRIOR variance to 1.0000
variance ratio 0.0006 at SNR~1000 -> 0.0306 at SNR~3  (53x)
```

**If an assertion fails, the physics is wrong — fix it, do not loosen the
tolerance.** It has already refused to run five times, four of them for real
errors. Two traps worth knowing before you touch it:

- **numpy's FFT is unnormalised.** `std(field) = sqrt(Σspec)/N`. Getting this
  wrong by a factor of N gives a prior ~255× too weak, which **does not
  crash** — it just stops contributing, and every plate still looks plausible.
  `prior_power()` derives the factor and asserts it over 24 draws (one draw of
  a steep spectrum scatters by tens of per cent, so one-draw checks are
  meaningless).
- **Do not average anything over all Fourier modes.** Only 1,153 of 65,536 lie
  below the cutoff; everything else is where `H = 0` and `var/P = 1` regardless
  of the data, so whole-frame averages go flat and stop responding.

### 1. GATE P — the human signs

`PEDAGOGY.md` must contain `VERDICT: PASS` (as a substring) with a signature.
**Do not write that string anywhere else in the file**, including in prose
explaining the gate: `generate_audio_kokoro.py` opens on a plain substring
match anywhere in the document.

### 2. Audio — the master clock

```bash
cd "$TOOLKIT" && "$PY" runtime/scripts/generate_audio_kokoro.py "$REEL"
```

Kokoro `af_bella`, local, $0.00. Expect **163.6 s**. No `--speed` needed.

Budget margin under the 3:00 cap because **the words-only prediction is noise of
order ±5–10% with no consistent sign**: Ep. 06 +10.4%, Ep. 07 −0.4%, Ep. 08
−5.0%, Ep. 09 +2.7%. Do not assume a direction.

### 3. Pacing (only if the narration changed)

```bash
"$PY" $SCRATCH/nat9.py     # per-scene natural length, no render
"$PY" $SCRATCH/pace9.py    # solves RT/HOLD and writes them into scenes.py
```

Then verify at **24 fps** — the real frame rate — in **both aspects**:

```bash
cd "$REEL"
for S in B01_Presenter … B10_TheTell; do
  "$PY" -m manim -ql --fps 24 --disable_caching scenes.py "$S"
  "$PY" -m manim -ql --fps 24 --disable_caching -r 480,854 scenes.py "$S"
done
```

Accept `−0.25 s … +0.05 s`. The asymmetry is the point: a short clip is padded
with a held frame (invisible), a long one is **centre-cut** and loses the
closing line off both ends.

Three things to know:

- `hold_to_beat` subtracts a module-level **`TAIL_TRIM = 0.18`**, because
  `renderer.time` under-reports the true rendered length (each play's frame
  count rounds up, and the error grows with the number of reveals).
- A residual undershoot **cannot** be fixed by lowering `RT` or `HOLD` — a
  smaller body raises `target − now` by the same amount and the total does not
  move. Only the trim, or a scene short enough to hit the 0.35 s floor, changes
  it.
- If a scene does **not** respond to the trim, it is already on the floor and
  its body is too long: lower its `RT` instead. That is B10 (20 reveals,
  `RT = 1.278`).

### 4. Gates F · L · A · W

**`run.sh` skips F, A and W on this reel** — all three are guarded on
`[ -n "$PENDING" ]`, and `PENDING` is empty because `run.sh` finds scenes with
`class (\w+)\(Scene\)` while every scene here subclasses `Paced`.

```bash
cd "$REEL"
for f in FACTCHECK.md SHOTLIST.md PROMPTS.md; do test -f "$f" || echo "GATE F: missing $f"; done
"$PY" $TOOLKIT/runtime/qc/beat_lint.py beat_sheet.json
for S in B01_Presenter … B10_TheTell; do
  "$PY" $TOOLKIT/runtime/qc/static_scene_check.py scenes.py --class "$S" --quiet
  "$PY" $TOOLKIT/runtime/qc/wcag_margin_check.py  scenes.py --class "$S" --quiet
done
```

### 5. Manim, 4K, both aspects — sequentially

```bash
cd "$REEL"; mkdir -p manim _portrait
for S in B01_Presenter … B10_TheTell; do
  BID="${S%%_*}"
  "$PY" -m manim -qk --fps 24 --disable_caching -r 3840,2160 scenes.py "$S"
  cp "media/videos/scenes/2160p24/$S.mp4" "manim/$BID.mp4"
done
for S in B01_Presenter … B10_TheTell; do
  BID="${S%%_*}"
  "$PY" -m manim -qk --fps 24 --disable_caching -r 2160,3840 scenes.py "$S"
  cp "media/videos/scenes/3840p24/$S.mp4" "_portrait/$BID.mp4"
done
```

**Verify every render before slotting it:**

```
-0.25 s <= (duration - actual_duration_s) <= +0.05 s   else re-render
frames / 24 == duration                                else the concat dropped frames
```

### 6. GATE B — pixel-true layout, both aspects

```bash
for S in B01_Presenter … B10_TheTell; do
  "$PY" $TOOLKIT/runtime/qc/manim_layout_audit.py scenes.py --class "$S" --png --curve-strict
  "$PY" $TOOLKIT/runtime/qc/manim_layout_audit.py scenes.py --class "$S" --png --curve-strict --portrait
done
```

Expect 20 × `rc=0`. **`layout_audit.md` is overwritten by every run** — copy it
per scene to read more than the last.

**Size every plate to its band before rendering.** `ph = pw × (ih/iw)`, the
landscape figure band is 4.30 units, and `varratio.png` is 2:1 — the tallest
plate here, which is why it is 5.80 wide and not 7.2. Ep. 08's B04 plate covered
the title for exactly this reason.

### 7. 16:9 — Remotion bookends, then compile

```bash
cd "$TOOLKIT"
"$PY" runtime/scripts/remotion_scenes.py "$REEL"        # FOREGROUND (rule 5)
"$PY" runtime/scripts/compile.py "$REEL" --height 2160  # → denoising-deep-space.mp4
"$PY" runtime/qc/final_frame_check.py "$REEL"           # GATE V
```

The four Remotion renders are the slow, memory-hungry step (~15 min). On Ep. 07
they left 1.1 GB free of 31.7 GB and the harness killed `run.sh`'s wrapper; the
child `compile.py` usually survives, so check mtimes and carry on from there.

### 8. 9:16 — full length, no beats cut

```bash
cd "$TOOLKIT"
"$PY" runtime/scripts/shorts.py "$REEL" --drop --no-endcard --handle "@HumanitariansAI"
cp "$REEL"/_portrait/B*.mp4 "$REEL"/short/manim/
cp "$REEL"/scenes.py "$REEL"/short/scenes.py
"$PY" runtime/scripts/remotion_scenes.py "$REEL/short"
"$PY" runtime/scripts/compile.py "$REEL/short" --height 3840
"$PY" runtime/qc/final_frame_check.py "$REEL/short"
cp "$REEL"/short/denoising-deep-space-short.mp4 "$REEL"/denoising-deep-space-9x16.mp4
```

Two expected SKIN LINT warnings (`B00 … wants ClaudeComposerAsk`, `B13 … wants
ClaudeTitleOutro`): the linter checks composition *names* and does not know
`shorts.py`'s ONDA CHECK rewired them to the `916` variants.

### 9. Look at the frames — this is where the real defects are

Read `_qc/contact_sheet.png` and `short/_qc/contact_sheet.png`, then **sample
the tail yourself** — the sheet carries only 16 of 28 frames, and B08–B13 is the
whole verdict / handoff / outro run. Sample *late* in each beat: a pale element
mid-`FadeIn` looks exactly like a rendering defect.

And read the finished frame of **every** Manim scene at 480p in **both** aspects
before committing to 4K. **Eleven defects in this build were invisible to every
gate**, including a font glyph that rendered as stray digits and a tile grid
that drew as vertical bars. Two specific habits:

- **Never use a glyph outside the font's coverage.** `✓` is absent from EB
  Garamond. Draw marks from `Line`s.
- **Measure anything placed with `next_to()`** — its y depends on its
  neighbour's rendered height, and guessing is what put a caption under a chip
  here and in Ep. 08.

## Toolkit patches this reel depends on

Already applied, needed by any reel:

1. `runtime/scripts/shorts.py` — `link_or_copy()` falls back to `shutil.copy2`
   when `Path.symlink_to` raises `OSError 1314`. Without it `shorts.py` cannot
   run on Windows.
2. `ClaudeVerdictArtifact916.tsx` / `ClaudeTitleOutro916.tsx` — rescaled from
   42% and 19% canvas fill to ~79% (Ep. 07). No further work needed.

## Still unpatched upstream

- `run.sh` does not export UTF-8 and crashes on cp1252.
- `run.sh`'s scene-discovery regex matches `(Scene)` only, so it silently skips
  GATE F, A and W on any reel whose scenes subclass a base class.
- **`scripts/type_check.py` (GATE T) does not exist.** SKILL.md calls it
  "ALWAYS RUN" and a hard block on `./art final`. §8.1/§8.3 are covered by
  GATE W and §8.2/§8.5 by GATE B; **§8.4 (kerning / font coverage) and §8.6
  (golden strings) are covered by nothing** — and this reel's missing `✓` glyph
  is exactly a §8.4 defect that reached a rendered frame.
- `generate_audio_kokoro.py` opens GATE P on a plain substring match.

## Never

- Never publish. The masters stay in this folder.
- Never hand-roll `npx remotion render` — go through `remotion_scenes.py`.
- Never fix timing by hand. Regenerate audio and recompile.
- Never re-render a plate without `rm -rf media/videos` first: Manim's cache key
  hashes scene *code*, not the contents of images a scene loads.
