# BUILD-PROMPT — rebuild *What We Chased Before.* from this folder

Ep. 10 · `classifying-supernovae`. Everything below is free and local. **No API
keys.** If any step appears to want one, stop — that is a toolkit bug, not a
missing credential (CLAUDE.md rule 7).

## Paths

```
TOOLKIT=E:/NEU/Jobs/Humanitarians_AI/brutalist.art          # brutalist.art — the DOT tree
REEL=D:/study_other/new_humanitarians/humanitarians-youtube/claude-for-astronomy/classifying-supernovae
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
cd "$REEL" && "$PY" assets/gen_triage.py     # seed 1017 → assets/plots/
rm -rf media/videos                          # REQUIRED — see the note at the end
```

numpy, scipy and Pillow. **No matplotlib** — the venv does not ship it.

numpy and Pillow. **No sklearn** — the classifier is a hand-written Gaussian
naive Bayes, chosen deliberately: a class with no labelled examples cannot be
predicted at all, so the feedback mechanism this episode is about is visible
in the model rather than buried inside an ensemble.

It runs 60 repeats × 12 seasons × 20 spectra across three follow-up
strategies. **The self-check asserts three things and writes nothing if any
fails**: greedy accuracy rises; greedy's median rare-class recall stays under
0.02 *and* at least half the runs end at zero; uncertainty sampling ends at
≥ 0.40 with at most 5% of runs at zero. Expect:

```
greedy       acc 0.883 -> 0.897 | rare recall median 0.000 | 48/60 runs at zero
canonical    rare recall median 0.000                      | 53/60 runs at zero
uncertainty  acc 0.920           | rare recall median 0.638 |  0/60 runs at zero
labelled-set rare fraction @ season 12: greedy 0.19%  uncertainty 16.8%
boundary enrichment 3.6x (season 1) -> 8.4x (season 8)
P(ever finding the rare class): 35% at 0% exploration -> 92% at 10%
```

**If an assertion fails, rewrite the claim — do not tune the experiment until
it agrees with you.** It refused three times and every refusal was my error.
Three traps worth knowing before you touch it:

- **The outcome is bimodal.** A greedy run either stumbles on a rare object
  early or never sees one. A 12-repeat *mean* read 0.088 where the median is
  0.000 and 48 of 60 runs end with no recall whatsoever. Report medians and
  the count at zero, never a mean.
- **Rare-class recall does not "collapse" — it starts at zero.** A
  brightness-biased seed set contains no rare objects. The loop inherits the
  blind spot and preserves it; it does not create it.
- **Record metrics at the BOTTOM of each season, not the top.** The first
  version logged before each query, so its last point reflected eleven rounds
  and not twelve, and two plates disagreed about the same configuration.

### 1. GATE P — the human signs

`PEDAGOGY.md` must contain `VERDICT: PASS` (as a substring) with a signature.
**Do not write that string anywhere else in the file**, including in prose
explaining the gate: `generate_audio_kokoro.py` opens on a plain substring
match anywhere in the document.

### 2. Audio — the master clock

```bash
cd "$TOOLKIT" && "$PY" runtime/scripts/generate_audio_kokoro.py "$REEL"
```

Kokoro `af_bella`, local, $0.00. Expect **147.7 s** (2:27.7). No `--speed`
needed — 32.3 s of headroom under the cap.

Budget margin under the 3:00 cap because **the words-only prediction is noise of
order ±5–10% with no consistent sign**: Ep. 06 +10.4%, Ep. 07 −0.4%, Ep. 08
−5.0%, Ep. 09 +2.7%, Ep. 10 −8.2%. Do not assume a direction.

### 3. Pacing (only if the narration changed)

```bash
"$PY" $SCRATCH/nat10.py    # per-scene natural length, no render
"$PY" $SCRATCH/pace10.py   # solves RT/HOLD and writes them into scenes.py
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
  its body is too long: lower its `RT` instead. That was Ep. 09's B10. **No
  scene needed it here** — all 20 clips landed −0.13 to −0.22 s under their
  beats and none reached the 0.35 s floor.

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
landscape figure band is 4.30 units. The six plates are `selection` 1500×760
(0.507), `deadline` 1560×780 (0.500), `loop` 1720×740 (0.430), `composition`
1720×620 (0.360), `boundary` 1720×700 (0.407), `budget` 1560×780 (0.500). At
ratio 0.50 a plate 8.0 wide is 4.00 tall and leaves nothing for labels, which
is why B03 and B04 are 6.40 wide. Ep. 08's B04 plate covered its own title for
exactly this reason.

### 7. 16:9 — Remotion bookends, then compile

```bash
cd "$TOOLKIT"
"$PY" runtime/scripts/remotion_scenes.py "$REEL"        # FOREGROUND (rule 5)
"$PY" runtime/scripts/compile.py "$REEL" --height 2160  # → claude-for-astronomy_OmMali_25_09_2026.mp4
"$PY" runtime/qc/final_frame_check.py "$REEL" \\
      --mp4 "$REEL/claude-for-astronomy_OmMali_25_09_2026.mp4"          # GATE V — ALWAYS --mp4
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
      --mp4 "$REEL/short/classifying-supernovae-short.mp4"
cp "$REEL"/short/classifying-supernovae-short.mp4 "$REEL"/classifying-supernovae-9x16.mp4
```

**`final_frame_check.py` given only a folder takes `glob("*.mp4")[0]`**, and
`classifying-supernovae-9x16.mp4` sorts *before* the landscape master --
before the build-time `classifying-supernovae.mp4` (`-` precedes `.`) and
before the delivered `claude-for-astronomy_OmMali_25_09_2026.mp4` (`clas`
precedes `clau`). Once the vertical copy exists in the reel root, every
bare call silently re-checks the vertical file while reporting as though it
were the landscape one. **Always pass `--mp4`**, and keep the two reports apart
(`_qc/REPORT-16x9.md`, `_qc/REPORT-9x16.md`) — the gate overwrites
`_qc/REPORT.md` and `_qc/contact_sheet.png` on every run.

Two expected SKIN LINT warnings (`B00 … wants ClaudeComposerAsk`, `B13 … wants
ClaudeTitleOutro`): the linter checks composition *names* and does not know
`shorts.py`'s ONDA CHECK rewired them to the `916` variants.

### 9. Look at the frames — this is where the real defects are

Read `_qc/contact_sheet.png` and `short/_qc/contact_sheet.png`, then **sample
the tail yourself** — the sheet carries only 16 of 28 frames, and B08–B13 is the
whole verdict / handoff / outro run. Sample *late* in each beat: a pale element
mid-`FadeIn` looks exactly like a rendering defect.

And read the finished frame of **every** Manim scene at 480p in **both** aspects
before committing to 4K. **Two defects in this build were invisible to every
gate**: B04's chip sitting eleven pixels under the axis labels (GATE B passes
it — the shapes do not intersect), and the one-page recap omitting the cost of
the fix. Ep. 09 had eleven such. Two specific habits:

- **Never use a glyph outside the font's coverage.** `✓` is absent from EB
  Garamond and Ep. 09 shipped it as stray digits. Draw marks from `Line`s;
  this reel uses no glyph outside the font.
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

**A note on `ClaudeVerdictArtifact` and GATE V's underfill floor.** The gate
measures the content *bounding box* against the title-safe area and wants
≥ 55%. A four-line artifact card sits almost exactly on that line, so encoder
noise alone can flip the verdict. Ep. 10's card carries five lines and clears
it — but the fifth line was added because the recap should state the cost of
the fix, not to satisfy a heuristic. If you write a shorter card, expect the
flag and look at the frame before changing anything.

## Still unpatched upstream

- `run.sh` does not export UTF-8 and crashes on cp1252.
- `run.sh`'s scene-discovery regex matches `(Scene)` only, so it silently skips
  GATE F, A and W on any reel whose scenes subclass a base class.
- **`scripts/type_check.py` (GATE T) does not exist.** SKILL.md calls it
  "ALWAYS RUN" and a hard block on `./art final`. §8.1/§8.3 are covered by
  GATE W and §8.2/§8.5 by GATE B; **§8.4 (kerning / font coverage) and §8.6
  (golden strings) are covered by nothing** — and Ep. 09's missing `✓` glyph
  was exactly a §8.4 defect that reached a rendered frame.
- `generate_audio_kokoro.py` opens GATE P on a plain substring match.

## Never

- Never publish. The masters stay in this folder.
- Never hand-roll `npx remotion render` — go through `remotion_scenes.py`.
- Never fix timing by hand. Regenerate audio and recompile.
- Never re-render a plate without `rm -rf media/videos` first: Manim's cache key
  hashes scene *code*, not the contents of images a scene loads.
