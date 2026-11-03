# BUILD-LOG — "Visual Question Answering, Blind?"

Reel: `youtube/vqa-blind` (16:9) + `youtube/vqa-blind-916` (9:16)
Skill: `ai-explainer` · Channel: @HumanitariansAI · Voice: Kokoro `am_onyx`
Built: 2026-09-06 · Toolkit: `brutalist.art` (local clone)

---

## The brief

"An explainer video on visual question answering using transformers. 4K, landscape and
portrait — two separate mp4s, same content. Max 2 minutes."

Two constraints shaped every decision below: **same content in both orientations** (so a
derived Short was out — `shorts.py` cuts beats when a reel exceeds the 3:00 Shorts cap and
rewrites the outro, which is a re-edit, not a reformat), and **max 2:00** (so the
`deep-explainer` chassis was out; this is a tight `ai-explainer` reel).

## Decision 1 — one responsive component per beat, registered twice

The toolkit's existing portrait support is a per-scene `*916` FILE (`ClaudeTitleOutro916`,
`ClaudeVerdictArtifact916`, …) — a second component maintained by hand. Writing seven of
those would have doubled the surface area and guaranteed drift between the two cuts.

The geometry made a better option available. From `tokens/layout.ts`:

    landscape SAFE    = 1728 × 972    (long axis horizontal)
    portrait  SAFE916 =  972 × 1728   (long axis vertical)

The **short axis is 972 in both**. So one px type scale reads identically in both
orientations and only the layout DIRECTION has to flip. Every `Vqa*` scene is therefore a
single component that reads `useVideoConfig()`, sets `portrait = height > width`, and
switches `flexDirection` — registered twice in `Root.tsx` at 1920×1080 and 1080×1920. That
is also how the toolkit already handles `ClaudeComposerAsk916` and the `Brand*916` family
(same component, portrait canvas), so it is the established pattern, not a new one.

Consequence: the two cuts cannot drift. There is one source of truth per beat.

## Decision 2 — CSS flex, not absolute SVG coordinates

The house illustration scenes (`GemmaExecSummary`, `GemmaScoreboard`) lay out with absolute
`<text x={112} y={172}>` inside a fixed `1920×1080` SVG. That cannot reflow. The `Vqa*`
scenes use HTML/flex for layout and drop into SVG only for the intrinsically graphical
parts (the patch grid, the attention field, the scene glyph). Type sizes are constants,
positions are flex.

## Decision 3 — `durationS` as a prop, via `calculateMetadata`

`remotion_scenes.py` renders a composition at its REGISTERED `durationInFrames` and then
freeze-holds or trims to the beat's measured audio length. For a 360-frame composition
matched to a 13s beat that means the animation finishes early and the tail is a still.

Each `Vqa*` schema therefore carries `durationS`, and each `Composition` uses
`calculateMetadata` to turn it into frames — the pattern already used by `LogoMotion` and
`LogoOutro916` in this Root. Because every ramp in these scenes is a fraction of `p`
(`useP()` = frame / durationInFrames), a beat RE-TIMES to its narration instead of
animating early. The beat sheet stamps `durationS` from `actual_duration_s` after audio.

## Decision 4 — the local kit, not `illustrations/kit.tsx`

`illustrations/kit.tsx` is landscape-only in one specific way that matters: its `SparkLine`
sits at `top: 44`, which is above the 9:16 title-safe inset of `y = 96` and would trip GATE
V's `edge-bleed` BLOCKER on every portrait beat. `scenes/VqaKit.tsx` is the orientation-aware
replacement: the spark header, the illustration, and a footer band (citation left, LOGO LAW
channel wordmark right) all live inside the correct safe box for whichever canvas is active.

The footer's `source` slot is also how this reel satisfies "no source, no verdict" — the
citation renders in the same frame as the numbers it backs, not in a description.

## The worked example

One drawn scene threads B03 → B04 → B07: a street with an umbrella. B03 patchifies it,
B04 attends to it, B07 recolours the umbrella to make the complementary pair. Drawn in SVG
per REBUILD LAW (no lifted photographs), and B07 says so on screen.

---

## Environment fixes required

**`@rspack/binding-darwin-arm64` was missing.** Every Remotion render failed with
`Cannot find native binding … Cannot find module './rspack.darwin-arm64.node'`. Only
`@rspack/binding-darwin-x64` (the Intel binding) was present in `node_modules` — npm's
known optional-dependency bug (npm/cli#4828), most likely from an install that ran under
Rosetta. Fixed with:

```bash
npm install --no-save --no-audit --no-fund @rspack/binding-darwin-arm64@1.7.11
```

`--no-save` deliberately: `package.json` in this clone carries a local, unrelated
modification (the exact-version Remotion pins) and must not be disturbed. This was a
pre-existing breakage in the clone, not caused by this reel — any Remotion render in this
toolkit was failing before this fix.

**Renders need the sandbox disabled** on this machine (headless Chrome cannot launch
sandboxed) and `python3`/`ffmpeg` must be PATH-prefixed, since the toolkit scripts call the
bare names and non-login shells resolve them to CLT 3.9.6 and an Intel ffmpeg:

```bash
PATH="/Library/Frameworks/Python.framework/Versions/3.11/bin:/opt/homebrew/bin:$PATH" …
```

---

## Gates

| Gate | Where | Result |
|---|---|---|
| PROOF GATE (authoring) | `CHECKS-REPORT.md` | 9 SHOW / 2 justified-HOLD / 0 PUNT; teaching arc complete |
| GATE P (narration) | `PEDAGOGY.md` | **PASS — self-signed by the build agent at the operator's instruction.** Not a human review; flagged in the README and needs one. |
| GATE L (beat mix) | `runtime/qc/beat_lint.py` | see below |
| GATE V (frame QC) | `runtime/qc/final_frame_check.py`, run per orientation | see below |
| VISUAL QC LAW | `_qc/` frames read by hand, both cuts | see below |

## Fixes made during QC

1. **B07 underfilled both canvases.** First render clustered content in the top ~60% with
   dead space beneath — a FILL-THE-CANVAS defect, and GATE V's `clustered` MAJOR. Cause:
   the pair row was `flex: 0 0 auto`, so nothing grew into the remaining space, and the
   panel size was a magic number (`268` / `300`). Fixed by deriving panel width FROM the
   safe box (`(safe.w − 30) / 2` portrait, `(safe.w × 0.46 − 46) / 2` landscape), giving
   the pair row `flex: 1` in landscape, spreading the outer column with
   `justifyContent: space-between`, and scaling the table and answer-chip type up.

## The visual QC pass (VISUAL QC LAW)

Frames were sampled at ~88-92% of each beat's span — the point where every reveal has
landed — and **read**, per orientation. The mp4 probe was treated as a file check, not QC.

Every defect below was found by looking, not by a gate. The pattern is worth recording
because it has one root cause: **sizes written as magic numbers instead of derived from the
safe box.** A number tuned by eye on a 1728x972 canvas is wrong on a 972x1728 one, and the
failure mode is always the same — content clusters and the long axis goes empty.

| Beat | Defect | Severity | Fix |
|---|---|---|---|
| B00, B09 | composer output lines were authored at landscape width and wrapped mid-token at 972px ("(VQA v1)" broke to "v1)") | MAJOR (legibility) | re-broke the lines by hand in BOTH sheets, <= ~46 chars, so each canvas wraps at an authored point. Content stays identical between cuts. |
| B01 | hard-coded thesis line breaks double-wrapped in portrait ("...about pictures in / four moves"); card text hugged the top of a tall portrait card | MAJOR | thesis renders as one paragraph wrapped by its box; card content centres in portrait |
| B03 | image band held `flex: 1 1 0` and centred inside itself, opening voids above AND below the image row in both orientations; glyph undersized | MAJOR (canvas-fill) | bands are auto-height, the column distributes with `space-between`, glyph + strip bars sized from `safe.w` |
| B04 | white scrim at 0.72 erased the picture the attention was landing on — the read was not legible as evidence | **BLOCKER** (the worked example did not show its own reasoning) | scrim 0.72 -> 0.30 |
| B04 | attention field rendered as one smooth blush, hiding the thing the beat teaches (the query scores every patch INDIVIDUALLY) | MAJOR | alpha quantised to 6 steps, cells gapped 3px, lattice opacity 0.28 -> 0.5, attended cells outlined in SEND once the softmax lands |
| B04 | umbrella was drawn in SPARK, the same terracotta as the heat, so the accent merged with the object it was selecting — and the beat had two terracotta moments | MAJOR (accent law) | scene umbrella -> `INK_SOFT`. On this beat the accent belongs to the ATTENTION. |
| B04 | field centred at (54, 40) put the peak on the canopy/stem junction rather than on the canopy the question names | MINOR (pedagogical precision) | centre -> (54, 34), widened to 13/10 |
| B05 | thin bars, undersized pipeline, voids down the long axis | MAJOR (canvas-fill) | column distributes, bars 38 -> 56px portrait, pooled vector + head scaled up |
| B06 | **the bracket spanned all four bars instead of blind -> sighted.** An absolutely-positioned SVG bracket with a `viewBox` mapping over a flex column does not know where the rows actually are. | **BLOCKER** (it asserted the wrong comparison) | bracket is now COMPOSED FROM THE ROWS: each row in `[from..to]` draws its own segment in a trailing gutter. It cannot drift from the layout. |
| B06 | after the rewrite the vertical connector broke across the inter-row slack, because `space-evenly` gaps are dynamic and the gutter only spanned each row's own box | MAJOR | rows are equal-height `flex: 1` items with zero gap, so stretched gutters abut and the bracket is continuous by construction |
| B07 | underfilled both canvases (content in the top ~60%, dead space beneath) | MAJOR (canvas-fill) | panel width derived from `safe.w`, pair row grows in landscape, table rows spread, type up |
| B08 | **the portrait verdict cited nothing.** `ClaudeVerdictArtifact916` never destructured or rendered `sourceNote` — a toolkit gap, not a reel bug. Any portrait verdict beat silently drops its citation. | **BLOCKER** (fails "no source, no verdict") | added the `sourceNote` block to the 916 component (hairline rule, staggered in after the last line, mono, `INK_SOFT`) matching the 16:9 treatment. Empty string still omits it, so reels predating the prop are unchanged. |

### Toolkit changes this reel required

Both are genuine fixes that outlive this reel, and both are in
`patches/brutalist-toolkit.patch`:

1. `runtime/remotion/src/Root.tsx` — registers the 14 `Vqa*` compositions.
2. `runtime/remotion/src/scenes/ClaudeVerdictArtifact916.tsx` — renders `sourceNote`
   (see B08 above), plus the missing `sourceNote` default in BOTH verdict registrations
   in `Root.tsx`. That default was also the cause of 2 of the project's 7 standing
   TypeScript errors; the project now reports 5, none in this reel's files.

Worth upstreaming to `nikbearbrown/brutalist.art`: the `ClaudeVerdictArtifact916` fix
is a straight bug fix, and `VqaKit.tsx`'s orientation-aware stage is the reusable half
of the dual-orientation approach.

### Round 2 — what GATE V caught that reading frames did not

Reading frames caught the composition problems. GATE V caught four things a human eye
slides past, and it was right about all of them.

| Beat | Defect | Severity | Fix |
|---|---|---|---|
| B02 (both) | rows entered with `translateX(-22px)` — the ENTRANCE ANIMATION slid content into the title-safe margin. Invisible in an end-of-beat frame; a 50%-of-beat sample caught it. | BLOCKER | entrance is vertical. A full-width row has nowhere horizontal to come from. |
| B03 (portrait) | Band A's inner row was `flex: 0 0 auto`, so it sized to its CONTENT (~1033px) instead of the 972px stage, and the strip bars could not shrink | BLOCKER | bands pinned to `width: 100%` + `minWidth: 0`; bars are `flex: 1 1 0` and share the leftover width. Plus `overflow: hidden` on VqaStage's illustration band as a STRUCTURAL GUARD — a layout bug now surfaces as visibly truncated content, not as edge-bleed on a 4K master. |
| B03/B04/B07 | ink/background luminance separation 0.26-0.30 against a 0.30 floor | MAJOR | the gate was right and the first instinct (dismiss it as a heuristic) was wrong: `SceneGlyph`'s fills sat within ~0.05 luminance of the cream stage. Darkened twice. B04 needed a second cause fixed too — a 0.30 PAGE scrim sitting ON the scene pulled it back toward the background; dropped to 0.14. |
| B10 (portrait) | canvas fill 22% of the safe area against a 55% floor | MAJOR | a ~106px title on a 1920-tall canvas is the "timid type" case FILL-THE-CANVAS exists to catch. Scaled to a poster. |

### The B10 lesson: fixing a MAJOR by creating a BLOCKER

The first outro fix raised fill 22% -> 47% by scaling type, then a second push to ~165px
cleared the fill floor and **introduced an edge-bleed BLOCKER**: `maxWidth: 1080 - PAD_X*2`
with `padding: 0 PAD_X` under default content-box sizing left the title a 864px CONTENT
box, and "Answering," is a single unbreakable ~880px word. An unbreakable word does not
wrap — it overflows, straight through the title-safe right edge.

The fix separated the two levers: `box-sizing: border-box` with `width` = `SAFE916.w`
(centred in the 1080 canvas, so the box IS the safe inset) and type backed off to ~154px
so the widest word clears with ~150px of slack, then the remaining fill taken from
**vertical spread** (line-height 1.08 -> 1.20, wider gaps) — which grows the measured
bounding box and cannot cause edge-bleed. Measured on the render: ink bbox
x[201,1936] y[856,3027] inside a safe box of x[108,2052] y[192,3648], fill 56%.

General rule this produced: **grow fill with leading and gaps, not with glyph width.**

### Motion histogram

The first compile warned that `illustrate` carried 5/11 beats (45%), over MOTION.md's ~40%
cap. `illustrate` was a catch-all hiding real differences, so the beats were relabelled to
the pantry's own vocabulary — B03 DRAWS the patch lattice on, B05/B06 are chart draw-on
(bars growing to a value), B04 ANNOTATES an image with weights. Final histogram, both cuts:
`reveal:4 (36%) · drawon:3 (27%) · type-on:2 (18%) · annotate:1 · illustrate:1`. Nothing
over 40%, and the labels are more accurate than what they replaced.

Operational note: `remotion_scenes.py` writes the beat sheet back after each beat to stamp
provenance, which reverts hand edits made while a render pass is in flight. `motion` and
`durationS` were re-applied after the last render and before the final compile.

Also hit the documented intermittent `Could not find composition with ID` failure once on
B10 — the script's own comment says the cause is undiagnosed and callers must retry. It
succeeded on the next attempt, as documented.

## Gate results — FINAL

| Gate | 16:9 | 9:16 |
|---|---|---|
| GATE L (beat mix) | clean | clean |
| GATE V (frame QC, 22 frames each) | **0 BLOCKER · 0 MAJOR ✓** | **0 BLOCKER · 0 MAJOR ✓** |
| Motion cap (<= ~40%) | pass (36% max) | pass (36% max) |
| Master law (no slates) | 11/11 VIDEO | 11/11 VIDEO |
| TypeScript | 0 errors in this reel's files | 0 errors in this reel's files |

The project's standing TypeScript error count went 7 -> 5; the 2 that cleared were the
verdict registrations' missing `sourceNote` default. The remaining 5 are pre-existing and
unrelated (`EcosystemWheelBeat`, and a landscape verdict registration owned by other reels).

## Final state

| | file | canvas | runtime |
|---|---|---|---|
| landscape master | `vqa-blind.mp4` | 3840x2160 | 1:55.7 |
| portrait master | `vqa-blind-916/vqa-blind-916.mp4` | 2160x3840 | 1:55.7 |

Masters stay on the build machine. Only the beat sheet, the scene source, the patch and
the paperwork are tracked in `humanitarians-youtube`. Nothing was published.

