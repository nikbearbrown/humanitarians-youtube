# BUILD-LOG — What Is a Concept Map

**Built:** 2026-08-28
**Source script:** [`script.md`](script.md)
**Toolkit:** `/Users/chaitanyam/dev/brutalist` — used **read-only**
**Voice:** Liam = Kokoro `am_onyx` ("Onyx")

## Outputs

| Cut | File | Resolution | Frames | Duration |
|---|---|---|---|---|
| 16:9 | `what-is-a-concept-map.mp4` | **3840×2160** | 5492 | 228.86 s |
| 9:16 | `vertical/what-is-a-concept-map-vertical.mp4` | **2160×3840** | 5492 | 228.86 s |

Both 24 fps, h264, yuv420p, bt709, per-beat AAC narration muxed by `compile.py`.

> **As-built state, 2026-08-28.** Revision 2 below supersedes the 9:16 row: the
> full-length `vertical/` cut was replaced by `short/`, and is not carried in
> this folder. See "Current deliverables" at the end.

## Architecture — why the visuals are out-of-tree

The human's instruction was "don't change anything in brutalist." Custom
Remotion scenes would have to be added to `runtime/remotion/src/` and
registered in `Root.tsx`, i.e. edits to the toolkit. So instead:

- **Visuals** are rendered by `scenes/render_scenes.py` (this folder), Pillow →
  frame-exact PNG state sequences → ffmpeg, natively at 3840×2160 / 2160×3840.
- They land in `media/<beat>.mp4`, which is the **top** slot precedence in
  brutalist's `compile.py:resolve_slot()` (`media/*.mp4` > `manim/*` >
  `media/*.png` > slate). No toolkit change is needed to consume them.
- **brutalist is used read-only for:** Kokoro narration
  (`generate_audio_kokoro.py`, run with an external interpreter), the
  conform/mux/assemble pass (`compile.py` via `./art final`), and its bundled
  Kokoro model files.
- **Python deps** (`kokoro-onnx`) were installed into
  `/Users/chaitanyam/medhavi-research-scripts/.venv`, never into
  `brutalist/.venv`.

Verified after the build: `git -C /Users/chaitanyam/dev/brutalist status` is
unchanged from the pre-build snapshot.

## Deviations from `ai-explainer` frame law — authorised by the human

`claude-explainer` resolves to the `ai-explainer` skill, whose laws this build
knowingly departs from. The human chose "script exact" over "skill law" when
the conflict was put to them. Each deviation:

| Law | What it requires | What was built | Why |
|---|---|---|---|
| Fidelity palette | Cream `#FAF9F5`, ink `#3D3929`, terracotta `#D97757`, EB Garamond. "Do not retint it." | Script palette: `#0A0A0A` / `#F2F0EB` / `#E8452C` / `#6B6B6B`, Helvetica Neue Bold + Menlo | The script's art-direction section is explicit and the human chose it |
| COLD OPEN LAW | B00 = `ClaudeComposerAsk`, never a brand/title card | B00 = title card carrying the requested spoken intro; B01 = the script's TOC cold open | Script has no composer beat |
| Spine | cold open → body → verdict page → HANDOFF → title-restate outro | The script's nine scenes, in order | "Follow the script exactly" |
| HANDOFF LAW | Second-to-last beat = composer with a suggested prompt, read aloud and discussed | Absent | Script has no handoff |
| OUTRO LAW | Title restate, serif, terracotta period, handle beneath | Script's four-line summary → `CONSUMERS 0` → hard cut to black | Script's own close |
| LOGO LAW | Channel brand bug on every beat | Absent | Neither `@NikBearBrown` nor `@HumanitariansAI` is this reel's channel |
| IN-FOR-BEAR LAW | B00 says "…this is Liam, in for Bear"; outro signs off the same | B00 says "Hi, I am Chaitanya…" | The human specified the intro line verbatim |

Consequence: **this is a Brutalist reel, not a Claude-branded ai-explainer.**
It should not be described as one, and it carries no Claude or channel branding.

## Judgment calls inside the script

Three places where the script under-specified or self-conflicted. Each resolved
toward the script's own hard rules, and recorded here rather than silently:

1. **SCENE 5, two reds at once.** The script asks for both "active panel Paper
   with a red top rule" *and* "the three words snap in as stacked red blocks."
   Its own hard rule says "Never two red things at once." Resolution: during the
   ACCEPT/EDIT/REMOVE moment the panel's top rule drops to Paper, so the
   verdicts own the accent. The rule returns for stage 04.

2. **SCENE 6 strikes rows FIG. 03 never showed.** Scene 6 says the record
   "returns, same position, same values" and then strikes
   `wikipedia_categories`, `confidence`, `source_url` — but the FIG. 03 listing
   in Scene 3 prints only seven rows, two of which are absent. You cannot strike
   a row that was never drawn. Resolution: FIG. 03 shows the script's seven rows
   verbatim; Scene 6 opens on the **full nine-row** record so the three
   stripped fields exist to be struck, then closes to the six-row FIG. 04.

3. **SCENE 8, three edges or one.** "Three connected node boxes … all with red
   edges pointing into a fourth box" and later "The three red edges remain."
   A first pass merged them into one bus with a single arrowhead, which read as
   one edge; corrected to three independent routes with three arrowheads, so
   three edges visibly dangle when the box is cut.

## Font substitutions

Neither family named in the script is installed on this machine.

| Script asks for | Installed | Used |
|---|---|---|
| Archivo / Inter Tight / Helvetica Now, weight 700+ | none | **Helvetica Neue Bold** — nearest available true grotesk at 700 |
| JetBrains Mono / IBM Plex Mono, 400/700 | none | **Menlo Regular + Bold** — the required 400/700 pair |

Bundled `Inter` in the toolkit ships only Regular/Medium, so it could not meet
the weight-700 display requirement. Two families total, as the script demands.

## Duration: 3:48.86, not 5:15

The script targets 5:15 and Appendix B assigns per-scene durations. Measured
Kokoro narration totals **228.86 s (3:48.86)** — 96 s under. Per-beat drift:

| Beat | Measured | Script est. | Drift |
|---|---|---|---|
| B00 | 9.75 s | 10 s | −0.25 |
| B01 | 12.25 s | 18 s | −5.75 |
| B02 | 13.03 s | 37 s | −23.97 |
| B03 | 20.29 s | 40 s | −19.71 |
| B04 | 31.78 s | 40 s | −8.22 |
| B05 | 37.56 s | 55 s | −17.44 |
| B06 | 20.31 s | 35 s | −14.69 |
| B07 | 32.83 s | 40 s | −7.17 |
| B08 | 34.23 s | 30 s | **+4.23** |
| B09 | 16.83 s | 20 s | −3.17 |

The pipeline is audio-first and `duration-planner` doctrine is "duration is an
output, never a target," so the visuals conform to the measured audio. **The gap
was not padded with holds** — that would have bought runtime with dead air.
B02 is the extreme case: 37 s of planned screen time carrying 13 s of speech.

To actually reach 5:15 the narration has to grow. Three options, in order of
preference: write more narration for the thin beats (B02 and B03 especially);
split B05 into four beats and narrate each stage properly; or re-run audio at
`--speed 0.8` (fast, but it will sound artificially slow — not recommended).

## Toolkit lints, and why they were not "fixed"

`compile.py` printed two warnings on both cuts. Both are correct observations
about a build that deliberately sits outside the scene contract:

- **`SKIN LINT: NO RENDERABLE BEATS`** — no beat carries
  `shot.remotion.pattern`, so the toolkit predicts every slot becomes a
  YOU-slate. It then reported `10/10 filled … B00:VIDEO … B09:VIDEO`, because
  `media/` was pre-filled out-of-tree. The lint assumes visuals come from
  Remotion/Manim; here they don't. Harmless, and a false positive for this
  architecture.
- **`step-reveal carries 5/10 beats (50%) — over the ~40% cap`** — MOTION.md's
  motion-diversity guard. The motion labels are read off the script's own shot
  list, which specifies step-reveals for exactly those five scenes. Relabelling
  them to satisfy the guard would be lying about the motion, so they stand.

## Reproduce

```bash
# 1. audio (the clock) — writes mp3/ + actual_duration_s back into the sheet
/Users/chaitanyam/medhavi-research-scripts/.venv/bin/python \
  /Users/chaitanyam/dev/brutalist/runtime/scripts/generate_audio_kokoro.py . --no-gate

# 2. visuals, both aspects
python3 scenes/render_scenes.py --aspect 16:9 --out media
python3 scenes/render_scenes.py --aspect 9:16 --sheet short/beat_sheet.json --out short/media

# 3. masters
cd /Users/chaitanyam/dev/brutalist
./art final <this-folder>                      # 3840x2160 (--height 2160 default)
./art final <this-folder>/short --height 3840  # 2160x3840

# The original 9:16 pass targeted vertical/, which revision 2 superseded.
# short/ is the only portrait cut carried here.
```

---

# REVISION 2 — 2026-08-28, after review

Two corrections. The human was right on both counts.

## 1. The 9:16 is now the Brutalist short, capped under 3:00

**Superseded:** `vertical/` (228.9 s, all ten beats) was built by deliberately
bypassing `shorts.py`. That was the wrong call — the 3:00 cap is a real
constraint on the 9:16, and `shorts.py`'s auto-shorten is the intended
behaviour, not an obstacle. `vertical/` was kept locally as an artefact but is
**not** the deliverable, and is not committed to this folder.

**Delivered:** `short/what-is-a-concept-map-short.mp4` — **2160×3840**,
**160.04 s (2:40.04)**, 20 s under the cap, 3840 frames @ 24 fps.

`shorts.py` planned the cut: **B05** (THE FOUR STAGES, 37.6 s) and **B08**
(THE CRACK, 34.2 s) dropped as the longest unprotected middle beats; B00 and
B09 protected; silent 4.5 s endcard appended; outro rewritten to name the cuts
and point at the long. Nine slots, all VIDEO.

It initially reported "STILL OVER at ~180.7 s" — that figure used a 20 s
*estimate* for the un-regenerated outro. Once the real outro audio existed
(15.30 s), the true total was 160.04 s and no third drop was needed. Worth
knowing: **regenerate the outro before trusting the cap arithmetic**, otherwise
you drop a beat you didn't need to.

Three overrides applied to shorts.py's output, each because the tool's default
is wrong for a non-Claude reel:

1. **Centre-cuts replaced.** `shorts.py` wrote `media/<beat>-916.mp4`
   centre-cuts of the 16:9 renders. A centre cut of 3840×2160 to 9:16 keeps
   1215 px of width and would have destroyed the bar chart, the split frame and
   the four-panel band. `short/media/` was overwritten with native 2160×3840
   portrait re-layouts from `render_scenes.py`. This is the tool's own
   documented escape hatch ("THE HUMAN IS EXPECTED TO REPLACE a centre cut that
   doesn't work").
2. **Outro narration rewritten.** The auto-rewriter spliced truncated
   mid-sentence fragments of the dropped beats and produced unspeakable text:
   *"The full video also covers Four stages. One — generate.… and One more
   thing, and it… "*. Replaced with a coherent line naming the same two dropped
   beats. Same function, per SHORTS LAW; audio regenerated.
3. **Endcard rebuilt.** `shorts.py`'s card renders in the **Claude brand** —
   ink-brown ground, EB Garamond serif, `@nikbearbrown` — at 1080×1920. Wrong
   three ways here: not this reel's palette, introduces a third type family the
   script forbids, and names a channel this reel isn't on. It would also have
   upscaled 2× into a 3840-tall frame. Replaced with a native brutalist card
   (ground, grotesk title, mono `MEDHAVY · RESEARCH LOG`, one signal rule) at
   2160×3840.

**Known cosmetic mismatch:** the short's B09 keeps the script's four-line
summary visual (ending on `CONSUMERS = 0` in signal) while the voice now reads
the rewritten "watch the long" outro. The visual still summarises and the red
hold still lands, so it was kept rather than replaced — but the step reveals
were timed to the original narration, not this one.

## 2. B04 timing defect — fixed, 16:9 master rebuilt

The human asked what was on screen at 1:16. Answer: the scripted full-frame
`THIN_CONTENT: 2`, nothing missing. But the question surfaced a genuine defect
19 s earlier that the first QC pass missed.

**Defect:** B04 (55.32–87.10 s) opened with **7.5 s of empty chart** — the
`CONFIDENCE, 25-NODE RUN` label and the HIGH/MEDIUM/LOW row labels with **no
bars**. It reads as failed media. The red `THIN_CONTENT: 2` card then held
static for another 7.5 s.

**Cause:** `allocate()` split leftover frames *equally* across elastic
segments, so the empty establishing state received the same 180-frame share as
the settled chart that carries the beat's content.

**Fix:** elastic segments now carry **weights** (`EL(w)`), and B04's empty
scaffold became a fixed 12-frame (0.5 s) establishing beat. New weighting:
settled chart 5, `THIN_CONTENT` card 2, closing mono line 2. First bar is
growing by 0.5 s; the full chart is settled by 3 s.

**Why the first QC missed it:** frames were sampled at 55% and 92% of each
beat, which landed on settled states in both cases. Sampling settled states
cannot find a bad *opening*. Beats are now spot-checked near t=0 as well.

16:9 master rebuilt: still 3840×2160, 5492 frames, 228.86 s.

## Current deliverables

| Cut | File | Resolution | Duration |
|---|---|---|---|
| 16:9 | `what-is-a-concept-map.mp4` | 3840×2160 | 228.86 s (3:48.86) |
| 9:16 | `short/what-is-a-concept-map-short.mp4` | 2160×3840 | 160.04 s (2:40.04) |
| — | `vertical/…-vertical.mp4` | 2160×3840 | 228.86 s — **superseded, not committed** |

brutalist re-verified untouched after this revision.
