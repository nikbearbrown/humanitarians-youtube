# BUILD-LOG — *Aim Where It's Going.*

Ep. 16 · `predictive-adaptive-optics` · toolkit `brutalist.art` · skill
`ai-explainer` · channel `claude-hai` · **$0.00**

## Deliverables

| Cut | File | Resolution | Duration | Size | Loudness |
|---|---|---|---|---|---|
| 16:9 master | `claude-for-astronomy_OmMali_06_11_2026.mp4` | 3840×2160 @ 24 | 160.82 s (2:40.8) | 15.5 MB | −21.0 LUFS |
| 9:16 master | `predictive-adaptive-optics-9x16.mp4` | 2160×3840 @ 24 | 160.82 s (2:40.8) | 17.3 MB | −21.0 LUFS |
| 9:16 in place | `short/predictive-adaptive-optics-short.mp4` | 2160×3840 | 160.82 s | 17.3 MB | — |

Both masters are **3859 frames** and carry **all 14 beats**. The 9:16 is
**not a crop**: every Manim beat is re-laid-out from the same `scenes.py` at
2160×3840, and all four Remotion bookends re-render against their `…916`
compositions at native portrait resolution.

The 16:9 filename follows the series convention (weekly Thursdays; Ep. 15 was
`30_10_2026`), which is a manual delivery step nothing in the toolkit performs.

## Gates

| Gate | What it checks | Result |
|---|---|---|
| F | paperwork set present | PASS |
| L | beat-mix lint | PASS — `clean — beat mix OK`, 14 beats |
| A | static pre-flight | PASS — 10/10 first pass; re-run twice, still clean |
| W | WCAG contrast · margins · overlap | PASS — 10/10 first pass; re-run twice |
| **B** | pixel layout, per scene, both aspects | **20/20** — landscape first pass, portrait after 2 fixes; re-run with `--curve-strict`, still 20/20 |
| **P** | human pedagogy signature | **signed VERDICT PASS, Om Mali, 11/06/2026** |
| **V** | frame QC on each compiled master | **28 frames · 0 BLOCKER · 0 MAJOR**, both cuts |
| T | type-lock | **COULD NOT RUN — not shipped in this toolkit** (see below) |

**GATE T and GATE SHARPNESS are still not shipped**, despite
`ai-explainer/SKILL.md` calling GATE T "ALWAYS RUN" and a hard block on
`./art run` and `./art final`. Searching for `type_check.py` returns nothing.
Eleventh consecutive episode recording this rather than silently skipping it.
§8.1/§8.3 are covered by GATE W and §8.2/§8.5 by GATE B; §8.4 kerning and
§8.6 golden strings are covered by nothing automated and were read by eye.

**Gates F, A and W do not run under `run.sh` on this reel** — all three are
guarded on a non-empty PENDING list, and PENDING is empty because `run.sh`
discovers scenes by matching a direct `Scene` subclass while every scene here
subclasses `Paced`. They were invoked directly. Do not read a clean `run.sh`
as evidence they ran.

## Audio is the clock

428 words, budgeted before the beat sheet was written. Kokoro `af_bella`,
local, free:

```
B00 11.84  B01  8.19  B02 13.87  B03 13.14  B04 14.87  B05 12.71  B06 11.22
B07 11.26  B08 11.35  B09 11.54  B10 12.25  B11 11.52  B12 11.41  B13  5.65
TOTAL 160.82 s = 2:40.8      margin to the 3:00 cap = 19.2 s
```

No `--speed` correction. Predicted 2:38.6 from Ep. 15's 0.3731 s/word; measured
**+1.4%**. Across Eps. 06–16 the words-only model has erred +10.4%, −0.4%,
−5.0%, …, +1.4% — **noisy in both directions with no consistent sign**, which
is why a margin is budgeted rather than the prediction trusted.

## Pacing

Solved from a no-render measurement pass, then verified at 480p in both
aspects before any 4K time was spent.

```
B01  8.042/8.19   B02 13.667/13.87  B03 12.958/13.14  B04 14.667/14.87
B05 12.500/12.71  B06 11.000/11.22  B07 11.042/11.26  B08 11.167/11.35
B09 11.333/11.54  B10 12.042/12.25
```

**Every scene lands under its beat in both aspects**, worst case −0.220 s
(B06). `compile.py` reported no stretch and no centre-cut on either aspect, so
there is no slow motion anywhere.

The residual 0.15–0.22 s is **frame quantisation inside `play()`** and is not
fixable by raising HOLD — a larger HOLD raises `renderer.time` and
`hold_to_beat()` shortens the tail by exactly the same amount. Undershoot is
the correct side to err on: a short clip is padded with a held frame, which is
invisible, while a long clip is centre-cut and would clip the closing line off
both ends.

### RT_PORTRAIT, and the one scene that was capped

Five scenes (B03, B04, B06, B07, B08) restack a landscape right-hand column
into rows and play **fewer reveals** in portrait; one RT for both aspects
would freeze them on a last frame for seconds of narration. Each carries its
own `RT_PORTRAIT`, solved to reproduce the landscape body length:

| beat | portrait / landscape plays | RT | RT_PORTRAIT |
|---|---|---|---|
| B03 | 11 / 13 | 1.550 | 1.798 |
| B04 | 8 / 11 | 1.550 | **2.000 (capped; wanted 2.190)** |
| B06 | 10 / 12 | 1.550 | 1.759 |
| B07 | 8 / 10 | 1.550 | 1.878 |
| B08 | 10 / 12 | 1.550 | 1.770 |

B04 portrait therefore holds ~0.9 s more frozen tail than its landscape twin.
Deliberate: past RT ≈ 2 a reveal stops reading as a reveal, and `hold_to_beat`
absorbs the difference into a held closing frame.

**The pre-audio paperwork said six scenes restack and play fewer reveals; the
measured pass says five.** B05 restacks but plays the same twelve reveals in
both aspects. Corrected in `CHECKS-REPORT.md`.

## Defects found and fixed in this build

### 1. A strikethrough that struck the heads of the letters, not their middles

`_strike()` centred on the glyph **bounding box**, which rises with ascenders
and falls with descenders — so the rule's position depended on which letters
the sentence happened to contain. B01's "where the answer came from" has
ascenders and **no descenders at all**, putting the rule at **0.831** of the
x-height band. B10's "a messier sky should break it" measured **0.505** and
looked correct **by accident**, because "sky" descends.

That is why twenty pre-flight frames did not catch it: B10's strike was among
them and it was fine. Now centred on the **median** glyph top and bottom,
which recovers the x-height band itself; both measure 0.500. Full account in
`_qc/VISUAL-QC.md`.

No gate could have caught this: `_strike` sets `_qc_intentional`, which is the
hook that exempts a deliberate strikethrough from GATE B's TEXT-ON-CURVE rule.
The gate cannot tell a strike through the middle from a strike through the
heads — **both are the intentional case.**

### 2. GATE B had been run without `--curve-strict`

The Ep. 08 recipe specifies `--png --curve-strict`; the gate script written
for this episode omitted both. Re-run with the flag across all ten scenes in
both aspects: **20/20 CLEAN**, so nothing else was behind it. Flag added to the
script.

### 3. Three props that silently did nothing

`remotion_scenes.py` warned that B11 passed `effortLabel`, `folderLabel` and
`modelLabel` to `ClaudeVerdictArtifact`, which has no such fields — zod drops
unknown keys. Checked the component: it renders **no** model/folder/effort
chrome at all, so nothing was replaced by default text and the frame was
correct either way. The props were surplus in the beat sheet and were removed,
which also cleared the warning from the 9:16 pass.

### Carried in from the pre-audio build

Five defects that every gate passed were found by reading 20 pre-flight frames
and fixed before the signature: B05 occupying only the top half of the frame
in both aspects, B09's 0.10-unit joiner line rendering as a stray tick with a
label floating beside nothing, B09 carrying three terracotta elements in one
beat, and dead bottom-right quadrants in B03 and B04. Detail in
`CHECKS-REPORT.md`.

## Known deviation, not fixed

`compile.py` warns on both cuts:

```
motion histogram: reveal:7  type-on:3  build:3  kinetic:1
WARNING: 'reveal' carries 7/14 beats (50%) — over the ~40% pantry cap
```

The warning is real and MOTION.md's reasoning behind the cap is sound — a
language-heavy sheet usually means that language was *easiest*, not best. Here
it reflects a genuine structure: ten of fourteen beats are computed-evidence
Manim plates, and a plate's honest motion is a staged reveal. Converting the
excess would mean re-authoring beats whose content a human has already signed,
so it is **recorded rather than silently cleared**. Worth revisiting at the
beat-sheet stage of the next episode, which is the only place it is cheap.

## The physics, and two expectations that were refused

`assets/gen_ao.py` **asserts eight claims and writes no plate if any fails**
(seed 1616). Both of these were my working hypotheses, and both were wrong:

1. **"More atmospheric layers break the predictor."** False in clean air —
   three layers still gave 183×, because a sum of frozen translations is still
   a linear time-invariant process and a linear filter eats any number of them.
   Layers only cost once the sensor is noisy. **Noise, not complexity, is the
   ceiling**, and B10 says so on screen.
2. **"Prediction beats a faster loop."** False here by 4× against 11×. The
   draft verdict line was rewritten before it reached the beat sheet.

Two bugs were caught by the asserts, not by eye: a spurious √2 that made every
structure function exactly **2× too large**, and a sign error in the sub-pixel
shift that made the pupil's track zigzag rather than translate, so odd delays
looked better than even ones.

## Cost

**$0.00.** Kokoro `af_bella` locally for narration; Manim and Remotion for
picture; numpy/scipy/Pillow for the experiment. No image model, no ElevenLabs,
no API keys, no paid step anywhere. Fellow Tier throughout.

## Not published

There is no publishing machinery in this toolkit and nothing was uploaded
anywhere. Both masters stay in this folder.
