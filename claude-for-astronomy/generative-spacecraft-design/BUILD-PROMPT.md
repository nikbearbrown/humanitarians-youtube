# BUILD-PROMPT — rebuild *Nothing Left To Remove.* from this folder

Ep. 11 · `generative-spacecraft-design`. Everything below is free and local. **No API
keys.** If any step appears to want one, stop — that is a toolkit bug, not a
missing credential (CLAUDE.md rule 7).

## Paths

```
TOOLKIT=E:/NEU/Jobs/Humanitarians_AI/brutalist.art          # brutalist.art — the DOT tree
REEL=D:/study_other/new_humanitarians/humanitarians-youtube/claude-for-astronomy/generative-spacecraft-design
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
cd "$REEL" && "$PY" assets/gen_struct.py --force   # → assets/plots/
rm -rf media/videos                          # REQUIRED — see the note at the end
```

numpy, scipy and Pillow. **No matplotlib** — the venv does not ship it, so
every chart is drawn with the small `Axes` helper in the generator.

**There is no seed.** SIMP from a uniform start is deterministic given the
problem, so the same source produces the same plates on every machine.
`SOURCES.md` records the mesh and the parameters instead.

**`--force` matters.** The optimisations and the 398-location damage sweep take
about four minutes, so they are cached in `assets/.cache_struct.npz`. The cache
does not know the physics changed — after editing `topo.py` or the load cases,
pass `--force` or you will restyle plates computed from the old model.

The script **asserts three claims** and writes nothing if any fails. Expect:

```
symmetry of the optimum: max|x - mirror(x)| = 2.12e-11
plate  @ 0.40  undamaged  100.03  worst    121.41 (1.21x)
bracket@ 0.40  undamaged   81.31  worst   2536.90 (31.20x)
bracket@ 0.60  undamaged   55.65  worst     90.79 (1.63x)
1. undamaged, at 40% mass: bracket 81.31 vs plate 100.03  -> 1.23x stiffer
2. worst-case damage:      bracket 2536.9 vs plate 121.4  -> 20.90x SOFTER
3. bracket at 60% mass:    sensitivity 1.63x (was 31.2x, a factor of 19.1)
```

**If an assertion fails, rewrite the CLAIM — do not loosen the tolerance.** It
refused once already, on a threshold I had chosen before measuring: claim 3
asserted the 60%-mass sensitivity would fall below 1.5x and it reads 1.63x.
Four traps worth knowing before you touch it:

- **A load point in void reports your density floor, not a load path.** The
  first version put three load cases at three heights on the free edge; two sit
  in void, the solve returned ~8.5e9, and the "ratio" came out at 89 million.
  That is EMIN restated. The bracket has a solid, non-design **mounting lug**
  for this reason, and damage patches overlapping it are excluded from the
  sweep — severing the fitting is a different failure from cracking a web.
- **Straight down is already the worst direction** on a short cantilever, so
  optimising for it is nearly robust against other directions: one lug and
  three load *directions* measured a 1.07x penalty. Real, and not an episode.
  The large effect is damage tolerance, which is what the literature names.
- **Validate the FE core before trusting anything.** A wrong stiffness matrix
  is still symmetric and still solves. `scratchpad/fecheck.py` checks exactly
  3 zero eigenvalues, all three rigid-body motions in the nullspace, the
  uniaxial patch test against 1/2 E/(1-nu^2) eps^2, and the solid cantilever
  against Euler-Bernoulli (expect FE 1.4-1.9% SOFTER, never stiffer).
- **The symmetry assertion is a dof-ordering check.** Domain, support and load
  are symmetric about mid-height, so the optimum must be. Get the element dof
  order wrong and the matrix is still symmetric, still solves, and quietly
  describes a different structure.

### 1. GATE P — the human signs

`PEDAGOGY.md` must contain `VERDICT: PASS` (as a substring) with a signature.
**Do not write that string anywhere else in the file**, including in prose
explaining the gate: `generate_audio_kokoro.py` opens on a plain substring
match anywhere in the document.

### 2. Audio — the master clock

```bash
cd "$TOOLKIT" && "$PY" runtime/scripts/generate_audio_kokoro.py "$REEL"
```

Kokoro `af_bella`, local, $0.00. Expect **149.0 s** (2:29.0). No `--speed`
needed — 31 s of headroom under the cap.

Budget margin under the 3:00 cap because **the words-only prediction is noise of
order ±5–10% with no consistent sign**: Ep. 06 +10.4%, Ep. 07 −0.4%, Ep. 08
−5.0%, Ep. 09 +2.7%, Ep. 10 −8.2%, Ep. 11 +3.3%. Do not assume a direction.

### 3. Pacing (only if the narration changed)

```bash
"$PY" $SCRATCH/nat11.py     # per-scene natural length, no render
"$PY" $SCRATCH/pace11.py    # solves RT/HOLD and writes them into scenes.py
"$PY" $SCRATCH/natboth11.py # natural length in BOTH aspects - see below
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
  its body is too long: **lower its `RT`**. A per-scene trim override was
  tried on B01 first and changed nothing, because `target - trim - now` was
  already below the 0.35 s floor. B01 went 0.837 -> 0.803, B07 1.299 -> 1.286.
- **The solve runs ONCE, in landscape.** Any scene whose portrait branch does
  a different number of plays inherits an RT fitted to the wrong body.
  `natboth11.py` measures both aspects and flags the mismatches: **8 of 10
  scenes differ here.** Seven are SHORTER in portrait, which `hold_to_beat`
  pads safely; **B04 is LONGER** (its portrait branch calls `closer()`, two
  plays and 1.15 s, where landscape adds one FadeIn) and overshot by +0.92 s
  until it was given its own multiplier:

  ```python
  BEAT, RT, HOLD = "B04", 1.539, 0.000
  if PORTRAIT:
      RT = 1.347
  ```

  On a separate line, so `pace11.py`'s regex still rewrites the landscape
  value on a re-solve.

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
landscape figure band is 4.30 units. The eight plates are `domain` 1560x720
(0.462), `evolve` 1464x744 (0.508), `shapes` 1554x380 (0.245), `paths`
1560x780 (0.500), `damage` 1554x380 (0.245), `price` 1560x780 (0.500), and the
stacked portrait variants `shapes_v` / `damage_v` 980x1010 (1.031). A
0.50-ratio plate at pw = 8.0 is 4.00 tall and leaves nothing for labels, so
`paths` and `price` run at 6.6 and `domain` at 7.2. Ep. 08's B04 plate covered
its own title for exactly this reason.

**The two-panel comparisons ship in BOTH arrangements.** A 4:1 image squeezed
into portrait's 3.44 units is 0.84 tall and the truss is unreadable, so
portrait loads the stacked variant instead. Portrait is not a crop.

### 7. 16:9 — Remotion bookends, then compile

```bash
cd "$TOOLKIT"
"$PY" runtime/scripts/remotion_scenes.py "$REEL"        # FOREGROUND (rule 5)
"$PY" runtime/scripts/compile.py "$REEL" --height 2160  # → generative-spacecraft-design.mp4
"$PY" runtime/qc/final_frame_check.py "$REEL" \\
      --mp4 "$REEL/claude-for-astronomy_OmMali_02_10_2026.mp4"   # ALWAYS --mp4
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
      --mp4 "$REEL/short/generative-spacecraft-design-short.mp4"
cp "$REEL"/short/generative-spacecraft-design-short.mp4 "$REEL"/generative-spacecraft-design-9x16.mp4
```

**`final_frame_check.py` given only a folder takes `glob("*.mp4")[0]`**, which
is whichever filename happens to sort first. Against the build-time name it
picks the WRONG one: `generative-spacecraft-design-9x16.mp4` beats
`generative-spacecraft-design.mp4` because `-` precedes `.`, which is how
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
