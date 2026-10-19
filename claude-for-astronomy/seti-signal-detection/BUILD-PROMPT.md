# BUILD-PROMPT — rebuild *The Signal We Imagined.* from this folder

Ep. 13 · `seti-signal-detection`. Everything below is free and local. **No API
keys.** If any step appears to want one, stop — that is a toolkit bug, not a
missing credential (CLAUDE.md rule 7).

## Paths

```
TOOLKIT=E:/NEU/Jobs/Humanitarians_AI/brutalist.art          # brutalist.art — the DOT tree
REEL=D:/study_other/new_humanitarians/humanitarians-youtube/claude-for-astronomy/seti-signal-detection
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
cd "$REEL" && "$PY" assets/gen_seti.py --force   # → assets/plots/
rm -rf media/videos                          # REQUIRED — see the note at the end
```

numpy and Pillow only. **The detector is the real algorithm**, not a
stand-in: `dedoppler_map` computes the statistic a radio technosignature
pipeline computes, swept over trial drift rates. That is the point -- it puts
the episode's subject, the assumption, in plain sight as one number.

**Seed 1313.** The experiment is cached in `assets/.cache_seti.npz`; pass
`--force` after editing `seti.py` or the cache will restyle plates computed
from the old physics.

The script **asserts three claims** and writes nothing if any fails. Expect:

```
threshold 4.46  (noise-only map max, 95th pct)
hypothesis    excludes zero  includes zero
assumed                1.00           1.00
corrected              0.00           1.00
pulsed                 0.70           0.60
edge sweep: 1.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
cadence recall: assumed 0.98  corrected 0.76  pulsed 0.70
```

**If an assertion fails, rewrite the CLAIM -- do not loosen the tolerance.**
Four traps, every one of which cost a rebuild:

- **Return a HIT LIST, not a maximum.** The interference is brighter than the
  signal, so a single maximum over the field is always an interference line
  and the injected signal never moves it. Every recall came out at 0.03-0.10.
- **Calibrate the threshold on NOISE, not on interference.** Otherwise it
  tracks the brightest line (22.6) and nothing can ever exceed it. The
  interference is not meant to be under the threshold; it is the pile of hits
  a human sifts.
- **Stay in the resolved regime.** De-Doppler only separates a drifting
  signal from a stationary one when the signal moves MANY linewidths across
  the integration. At 16 rows and 0.15-0.60 Hz/s that is 2-10 channels
  against a 1-2 channel linewidth, and the separation does not exist. 32 rows
  at 0.6-2.0 Hz/s matches what real surveys do.
- **Watch the sign.** Drift drawn with a random sign while the search covers
  only positive rates means half of every "assumed" signal is never searched
  for -- it shows up as recall 0.45 on the hypothesis that should work.

**A fourth claim was measured and CUT.** An earlier version argued zero drift
is too crowded to search; the measurement said 6 look-alikes for a drifting
candidate against 5 for a stationary one. `seti.lookalikes` still runs and is
still printed; it is simply not claimed.

### 1. GATE P — the human signs

`PEDAGOGY.md` must contain `VERDICT: PASS` (as a substring) with a signature.
**Do not write that string anywhere else in the file**, including in prose
explaining the gate: `generate_audio_kokoro.py` opens on a plain substring
match anywhere in the document.

### 2. Audio — the master clock

```bash
cd "$TOOLKIT" && "$PY" runtime/scripts/generate_audio_kokoro.py "$REEL"
```

Kokoro `af_bella`, local, $0.00. Expect **141.5 s** (2:21.5). No `--speed`
needed — 38 s of headroom under the cap.

Budget margin under the 3:00 cap because **the words-only prediction is noise of
order ±5–10% with no consistent sign**: Ep. 06 +10.4%, Ep. 07 −0.4%, Ep. 08
−5.0%, Ep. 09 +2.7%, Ep. 10 −8.2%, Ep. 11 +3.3%, Ep. 12 −0.1%, Ep. 13 −5.1%. Do not assume a direction.

### 3. Pacing (only if the narration changed)

```bash
"$PY" $SCRATCH/nat13.py     # per-scene natural length, no render
"$PY" $SCRATCH/pace13.py    # solves RT/HOLD and writes them into scenes.py
"$PY" $SCRATCH/natboth13.py # natural length in BOTH aspects - see below
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
- **The lever is always RT.** A per-scene trim override was built and tried
  on FOUR scenes across two episodes -- Ep. 11's B01 and B07, Ep. 13's B07 and
  B09 -- and moved the measured duration by exactly zero every time, because
  `target - trim - now` was already below the 0.35 s floor in all four. Once
  the wait is floored the total is just `body + floor`, and only a smaller
  body changes it. A scene landing above -0.15 s is floored: lower its RT.
- **If RT is already at the 1.55 cap**, raise HOLD instead; that also grows
  the body. Ep. 13's B06 needed exactly this: -0.30 s with RT capped and the
  tail floored, fixed by HOLD 0.034 -> 0.043.
- **The solve runs ONCE, in landscape.** `natboth13.py` measures both aspects
  and flags scenes whose portrait branch does a different number of plays.
  Scenes that are SHORTER in portrait are safe -- the tail pads them. Only a
  scene that is LONGER in portrait needs its own multiplier, as Ep. 11's B04
  did.

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

**Size every plate to its band before rendering.** `ph = pw × (ih/iw)` and
the landscape figure band is 4.30 units. The seven plates are `waterfall`
1500×700 (0.467), `three` 1552×420 (0.271), `recall` / `edge` / `compare`
1560×780 (0.500), `cadence` 1150×478 (0.416), and the stacked portrait
variant `three_v` 760×940 (1.237).

**SIX of this reel's seven GATE B failures were one mistake**: a label at
`pat[0] ± pw * k`. In landscape `pw` is 7 units and that lands inside a
12.3-unit frame; in portrait `pw` is 3.4 and the SAME expression lands
outside a 3.6-unit frame. An offset scaled to the plate is not an offset
scaled to the safe area.

**Watch the spectrogram display gamma.** GATE V failed this reel four times
on low contrast because the noise was lifted toward ink and the structure was
no more contrasty than the background. The metric averages EVERY pixel
differing from the background by more than `INK_DELTA`, so a field of
marginally-grey noise drags it to cream. Gamma 2.80 puts the noise below the
threshold; 1.55 was measured and was not enough.

### 7. 16:9 — Remotion bookends, then compile

```bash
cd "$TOOLKIT"
"$PY" runtime/scripts/remotion_scenes.py "$REEL"        # FOREGROUND (rule 5)
"$PY" runtime/scripts/compile.py "$REEL" --height 2160  # → seti-signal-detection.mp4
"$PY" runtime/qc/final_frame_check.py "$REEL" \\
      --mp4 "$REEL/claude-for-astronomy_OmMali_16_10_2026.mp4"   # ALWAYS --mp4
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
"$PY" runtime/qc/final_frame_check.py "$REEL/short" \\
      --mp4 "$REEL/short/seti-signal-detection-short.mp4"
cp "$REEL"/short/seti-signal-detection-short.mp4 "$REEL"/seti-signal-detection-9x16.mp4
```

**`final_frame_check.py` given only a folder takes `glob("*.mp4")[0]`**, which
is whichever filename happens to sort first. Against the build-time name it
picks the WRONG one: `seti-signal-detection-9x16.mp4` beats
`seti-signal-detection.mp4` because `-` precedes `.`, which is how
Ep. 10 lost a re-render to a phantom regression. Against the delivered name it
happens to pick the right one, because `claude-` beats `generative-`. **Do not
rely on either: always pass `--mp4`**, and copy the reports to aspect-suffixed
names, because the gate overwrites `_qc/REPORT.md` and
`_qc/contact_sheet.png` on every run.

**The 16:9 master is renamed on delivery** to
`claude-for-astronomy_OmMali_DD_MM_YYYY.mp4` with that week's release date;
the 9:16 keeps the slug. `compile.py` writes `<slug>.mp4`, so the rename is a
manual step.

Two expected SKIN LINT warnings (`B00 … wants ClaudeComposerAsk`, `B13 … wants
ClaudeTitleOutro`): the linter checks composition *names* and does not know
`shorts.py`'s ONDA CHECK rewired them to the `916` variants.

### 9. Look at the frames — this is where the real defects are

Read `_qc/contact_sheet.png` and `short/_qc/contact_sheet.png`, then **sample
the tail yourself** — the sheet carries only 16 of 28 frames, and B08–B13 is the
whole verdict / handoff / outro run. Sample *late* in each beat: a pale element
mid-`FadeIn` looks exactly like a rendering defect.

And read the finished frame of **every** Manim scene at 480p in **both** aspects
before committing to 4K. **Twelve defects in this build were invisible to
every gate**, plus one GATE V caught only after the compile. Three specific
habits:

- **Ask whether the picture says what the beat says.** B06's comparison bars
  were drawn from compliance, where shorter means stiffer — so the winning
  design had the SHORTER bar and the chart argued the opposite of the
  narration. B10's legend named the wrong curve. No geometric check reaches
  either.
- **A gap of 0.04 units is eleven pixels at 4K, and eleven pixels reads as
  contact.** Four of the twelve were sub-0.08-unit gaps that GATE B scores as
  non-intersecting. Leave >= 0.15 between any two elements.
- **A plate is an `ImageMobject`, not a curve**, so GATE B will not flag a
  label printed across it. B06 portrait shipped "the optimiser's answer"
  straight over the bracket until the frame was read.
- **Never use a glyph outside the font's coverage.** `✓` is absent from EB
  Garamond and Ep. 09 shipped it as stray digits. Draw marks from `Line`s.
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

**Write the verdict card with FIVE lines, not four.** GATE V measures the
content bounding box against the title-safe area and wants >= 55%; a four-line
`ClaudeVerdictArtifact` sits almost exactly on that line and the verdict flips
on encoder noise (Ep. 10). Five clears it, and gives the recap room to state
the cost — which an episode about quantifying a cost ought to do on the page a
viewer can pause.

**Give every scene its footer EARLY.** GATE V samples each beat at 50% and
85% of its span. B01 is the one scene that does not call `chrome()`, and with
its citation and brand bug landing last, the content bbox covered only the top
half of the frame for most of the beat — 44% fill, a MAJOR. Moving the footer
into the header fixed it without changing the play count or the duration.

## Still unpatched upstream

- `run.sh` does not export UTF-8 and crashes on cp1252.
- `run.sh`'s scene-discovery regex matches `(Scene)` only, so it silently skips
  GATE F, A and W on any reel whose scenes subclass a base class.
- **`scripts/type_check.py` (GATE T) does not exist.** SKILL.md calls it
  "ALWAYS RUN" and a hard block on `./art final`. §8.1/§8.3 are covered by
  GATE W and §8.2/§8.5 by GATE B; **§8.4 (kerning / font coverage) and §8.6
  (golden strings) are covered by nothing** — Ep. 09's missing `✓` glyph was
  exactly a §8.4 defect that reached a rendered frame.
- `generate_audio_kokoro.py` opens GATE P on a plain substring match.

## Never

- Never publish. The masters stay in this folder.
- Never hand-roll `npx remotion render` — go through `remotion_scenes.py`.
- Never fix timing by hand. Regenerate audio and recompile.
- Never re-render a plate without `rm -rf media/videos` first: Manim's cache key
  hashes scene *code*, not the contents of images a scene loads.
