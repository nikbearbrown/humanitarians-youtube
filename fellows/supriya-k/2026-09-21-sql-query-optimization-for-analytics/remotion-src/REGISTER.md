# remotion-src/ — reel-local scenes and how to register them

Two beats in this reel use scenes that do not exist in the shared library. Both
gaps are logged in `brutalist.art/TEMPLATE-MISSES.md` with a proposed upstream fix.

| File | Composition id | Beat | Why it is reel-local |
|---|---|---|---|
| `sqlDeckKit.tsx` | *(not a composition)* | — | Shared palette + deterministic helpers for the three forks below. `deckPatterns.tsx` keeps its constants and helpers **module-private** (only components and data types are exported), so a fork cannot import them and must carry a verbatim copy. |
| `SqlPlanBeat.tsx` | `SqlPlanBeat` | B03 | `ClaudeCodeBeat` hard-codes its language chip to `'python'` and renders ONE card. This beat is SQL and its whole point is two captures side by side. |
| `SqlPredictCard.tsx` | `SqlPredictCard` | B05 | The library `PredictCard` is registered only as `Illu-PredictCard`, whose props are baked into the Studio preview wrapper and cannot be set per beat. `ILLUSTRATIONS.md` names copying the props block into the reel as the intended path. |
| `SqlAttritionChain.tsx` | `SqlAttritionChain` | B01 | **Fork.** Fixes `_qc/REPORT.md` #3 (counter card painted over `slideMeta`, deleting the isotype scale declaration) and #4 (beat ended mid-migration). |
| `SqlScaleComparison.tsx` | `SqlScaleComparison` | B04 | **Fork.** Fixes `_qc/REPORT.md` #2 (BLOCKER — item labels overflowed off the left frame edge; two clipped, one missing). |
| `SqlDivergentFates.tsx` | `SqlDivergentFates` | B06 | **Fork.** Fixes `_qc/REPORT.md` #1 (BLOCKER — endpoint badges gated at `p≥0.82` were unreachable after truncation, so track labels and outcomes never rendered). |

## The 9:16 portrait variants (the vertical companion)

Five more reel-local scenes, for `vertical/`. **No library `916` exists for any
deck pattern** — `AttritionChain916`, `ScaleComparison916`, `DivergentFates916`
and `PredictCard916` are all absent from `Root.tsx` — which is exactly the gap
`shorts.py`'s ONDA CHECK reports:

```
[short] B01  ONDA CHECK ⚠ no SqlAttritionChain916 composition in Root.tsx — add one, or drop pantry/B01-916.mp4
```

| File | Composition id | Beat | Registered | Re-band |
|---|---|---|---|---|
| `SqlAttritionChain916.tsx` | `SqlAttritionChain916` | B01 | 1080×1920 · 620f | 3 panels side-by-side → **stacked**; losses drift RIGHT (down would collide with the next panel) |
| `SqlPlanBeat916.tsx` | `SqlPlanBeat916` | B03 | 1080×1920 · 610f | 2 cards side-by-side → **stacked**. A portrait column is WIDER in characters than a landscape half-column, so the captures get more room |
| `SqlScaleComparison916.tsx` | `SqlScaleComparison916` | B04 | 1080×1920 · 555f | axis stays horizontal (a magnitude axis must read as one continuous line); each row gains ~2.5× vertical space, label above / value below |
| `SqlPredictCard916.tsx` | `SqlPredictCard916` | B05 | 1080×1920 · 305f | spark top, question filling the middle third at ~2× the type size, rule + commit beneath |
| `SqlDivergentFates916.tsx` | `SqlDivergentFates916` | B06 | 1080×1920 · 640f | L→R fork → **top-down fork**; badges are full-width blocks beneath their own endpoint |

**The five library beats need no new scenes.** B00/B02/B08 rewire to
`ClaudeComposerAsk916`, B07 to `ClaudeVerdictArtifact916`, B09 to
`ClaudeTitleOutro916` — and those 916 zod schemas are **literal aliases**:

```tsx
export const claudeComposerAsk916Schema = claudeComposerAskSchema;
```

so the 16:9 props carry over verbatim. Standing rule #4 satisfied for free.

### Portrait scale basis — do not reuse `sc(H)`

`sc(H) = H/720` is a **landscape-height** basis. In portrait `H = 1920`, so it
returns 2.67× and blows the type up against a 1080-wide frame. Portrait forks use
**`scW(W) = W/1080`** (added to `sqlDeckKit.tsx` alongside `wrapText`). Both
helpers keep the design resolution-independent: 1080×1920 is the design size,
2160×3840 the `--scale=2` render.

### Copy step covers all eleven files

`BUILD-PROMPT.md` step 1's `cp "$REEL"/remotion-src/sqlDeckKit.tsx
"$REEL"/remotion-src/Sql*.tsx …` already globs the portrait scenes — no change
needed.

### The three forks — what changed, and what deliberately did not

The shared library components in `runtime/remotion/src/deckPatterns.tsx` are
**not edited**. Toolkit-level fixes for the underlying bugs are written up in
`brutalist.art/TEMPLATE-MISSES.md` **#5 (truncation), #6 (ScaleComparison label
budget), #7 (AttritionChain z-order)** — those are the fixes that would help every
other reel; these forks only rescue this one.

Each fork keeps the library's motion math, palette, easing and geometry
**verbatim**. Three things change:

1. **`durationInFrames` matches the beat's MEASURED audio** (620 / 555 / 640
   frames vs the library's uniform 900), so `remotion_scenes.py` has no tail to
   truncate and each authored timeline plays in full.
2. **Author-supplied text gets a real width budget** — shrink-to-fit, wrap, or
   relocation — because these patterns were designed for ~10-character labels and
   this reel's are 27–44.
3. **Every hardcoded pixel is multiplied by `sc(H) = H / 720`**, so the forks can
   register at **1920×1080** and render at a true **3840×2160** under the existing
   global `--scale=2`. This is why re-registering the *originals* at 1080 would be
   wrong (their constants are 720p-tuned) but re-registering the *forks* is
   correct — and it resolves QC item Q6 without touching `remotion_scenes.py`.

> ⚠ **If narration is ever regenerated, re-check these three `durationInFrames`
> against the new `actual_duration_s`.** They track the current measured audio
> (20.57 s / 18.41 s / 21.33 s). The badge reveal at `p=0.55` gives headroom, but a
> large shift should be re-verified by QC.

## Why registration is a manual step

`runtime/scripts/remotion_scenes.py` renders `shot.remotion.pattern` as a
**composition id** inside the shared project:

```
npx remotion render src/index.ts <pattern> media/<BID>.mp4 --props=<props.json> \
    --scale=2 --image-format=png --crf=16
```

There is no reel-local scene autoloader. A composition that is not registered in
`runtime/remotion/src/Root.tsx` cannot be rendered, so B03 and B05 will fail until
the two steps below are done. (This is the same arrangement the `claude-debunked`
exemplar used — its `remotion-src/Debunked.tsx` + `Wheel.tsx` were registered the
same way.)

## Step 1 — place the files (COPY — do not symlink)

Copy both files into the shared project's scenes tree:

```bash
TOOLKIT=/Users/supriyakushwaha/Documents/ai1-cli/brutalist.art
REEL=/Users/supriyakushwaha/Documents/humanitarians-youtube/fellows/supriya-k/2026-09-16-sql-query-optimization-for-analytics

cp "$REEL"/remotion-src/sqlDeckKit.tsx "$REEL"/remotion-src/Sql*.tsx \
   "$TOOLKIT"/runtime/remotion/src/scenes/
```

That copies six files: `sqlDeckKit.tsx` plus the five `Sql*` scenes. The kit must
travel with them — the three forks import it as `./sqlDeckKit`.

**This reel's `remotion-src/` stays the source of truth.** The copies under
`runtime/remotion/src/scenes/` are disposable build artifacts — regenerate them
with the `cp` above on every build (`BUILD-PROMPT.md` step 1 does exactly this).
Edit the scene *here*, never there; if the two diverge, the reel folder wins.

### Why not a symlink (learned the hard way, 2026-09-16)

An earlier version of this file recommended `ln -sf`. **That does not work**, and
it fails in a way designed to waste your afternoon:

- **`tsc` passes.** TypeScript follows the symlink and resolves `../tokens/claude`
  relative to the *symlink's* directory (`src/scenes/`), where it exists.
- **Webpack fails.** Remotion's bundler resolves the symlink to its **realpath**
  first, then resolves relative imports from the *real* directory
  (`…/<reel>/remotion-src/`), producing:

  ```
  Error: Module not found: Error: Can't resolve '../tokens/claude' in
  '…/2026-09-16-sql-query-optimization-for-analytics/remotion-src'
  ```

So a symlink typechecks clean and then dies at bundle time. Copies avoid it
entirely. (The alternative — `resolve.symlinks: false` in a `remotion.config.ts`
webpack override — was rejected: no config file exists in this project, and
introducing one changes bundling for all ~580 compositions to suit one reel.)

Both files import from `../tokens/claude`, `../tokens/layout`,
`../illustrations/kit` and `../illustrations/structural`. Those resolve correctly
from a **real file** at `src/scenes/`, which is why that is the placement.

## Step 2 — register the compositions

Add to `runtime/remotion/src/Root.tsx` (this edits the toolkit, so it is a
tracked change to review — the reel folder stays the source of the scene code):

```tsx
import { SqlPlanBeat,    sqlPlanBeatSchema }    from './scenes/SqlPlanBeat';
import { SqlPredictCard, sqlPredictCardSchema } from './scenes/SqlPredictCard';

<Composition
  id="SqlPlanBeat"
  component={SqlPlanBeat}
  durationInFrames={630}
  fps={30}
  width={1920}
  height={1080}
  schema={sqlPlanBeatSchema}
  defaultProps={{
    title: 'demo/explain_a_non_sargable.txt  →  demo/explain_b_sargable.txt',
    lang: 'sql',
    left:  { heading: 'A — non-sargable', code: '-- see beat_sheet.json', verdict: 'SCAN · 400,000 rows read',  tone: 'warn' },
    right: { heading: 'B — sargable',     code: '-- see beat_sheet.json', verdict: 'SEARCH · 11,369 rows read', tone: 'good' },
    sparkLine: 'SCAN means every row.',
    citation: 'Captured from SQLite 3.45.3 — demo/RESULTS.md',
    highlightLeft: 'SCAN',
    highlightRight: 'SEARCH',
  }}
/>

<Composition
  id="SqlPredictCard"
  component={SqlPredictCard}
  durationInFrames={390}
  fps={30}
  width={1920}
  height={1080}
  schema={sqlPredictCardSchema}
  defaultProps={{
    sparkLine: 'Commit before the reveal.',
    question: "Both filter the same indexed column. What does A's WHERE clause do that costs it the index?",
    commit: 'commit — the answer is one beat away',
  }}
/>
```

`durationInFrames` here only sets the Studio preview length. The real clock is the
beat's measured audio: `remotion_scenes.py` freeze-extends each render to
`actual_duration_s`, and `compile.py` conforms it.

## Step 3 — verify before rendering

```bash
cd $TOOLKIT/runtime/remotion
npx tsc --noEmit
npx remotion compositions src/index.ts | grep -iE '^Sql'
```

Expected output:

```
SqlPlanBeat                           30      1920x1080      630 (21.00 sec)
SqlPredictCard                        30      1920x1080      390 (13.00 sec)
SqlAttritionChain                     30      1920x1080      620 (20.67 sec)
SqlScaleComparison                    30      1920x1080      555 (18.50 sec)
SqlDivergentFates                     30      1920x1080      640 (21.33 sec)
```

All **five** ids must print, and `bundle errors: 0`.

`npx tsc --noEmit` shows **2 pre-existing errors** at `Root.tsx` (`LabelChip`
missing `pairs`/`footer`, `QuoteCard` missing `before`/`after`). Those come from
untracked scene work unrelated to this reel and were present before these two
compositions were added — verified by typechecking the pre-edit `Root.tsx`, which
produced the same 2 errors. **Any error naming `SqlPlanBeat` or `SqlPredictCard`
is ours and must be fixed.**

### ⚠ The webpack cache pitfall

If the bundle error names a path that no longer exists — a file you just moved,
renamed, or converted from a symlink — **it is the cache, not your code**:

```bash
rm -rf $TOOLKIT/runtime/remotion/node_modules/.cache/webpack/remotion-production-*
```

This bit once already: after replacing the symlinks with real copies, the
identical `Can't resolve '../tokens/claude' in …/remotion-src` error kept
appearing even though nothing referenced `remotion-src` any more. Clearing
`node_modules/.cache/webpack/remotion-production-4.0.486` fixed it instantly.
**Clear this cache after any scene file move, before you debug anything else.**

Then, and only then, render via
`python3 runtime/scripts/remotion_scenes.py <REEL>` — never hand-roll
`npx remotion render` (brutalist `CLAUDE.md` rule 5).

## Design constraints these two scenes respect

- Pure functions of the audio clock: `useCurrentFrame()` / `useVideoConfig()` only.
  No timers, no CSS transitions, no `Math.random()` — same seed in, same frames out.
- Positioned from the shared `SAFE` constant (`tokens/layout.ts`), never by
  hand-nudged pixels.
- Every variable-length text node has `maxWidth`/`minWidth: 0` plus wrap or
  ellipsis — never a bare fixed width (the standing fix from
  `CLAUDE-CODE-VISUAL-QC-CHECK.md`).
- ONE terracotta moment at a time: in `SqlPlanBeat` the accent hands off from card
  A to card B rather than lighting both.
- `SqlPredictCard` changes props only. The motion math inside `PredictCard` is not
  touched, per the starter-template contract in `ILLUSTRATIONS.md`.

## Known open item

Neither scene renders the `@HumanitariansAI` logo bug (LOGO LAW). Nor do the three
library patterns this reel uses. See `TEMPLATE-MISSES.md` #3 — the right fix is a
shared `<BrandBug channel="hai" />` overlay, not five copies of the same div.

## v2 changes (2026-10-17)

These copies are kept byte-identical to `runtime/remotion/src/scenes/` (verified after the
rebuild). New opt-in props — every one is a no-op when omitted:

| Composition | New props |
|---|---|
| all ten `Sql*` | `handle` — lower-right author chip (library `HandleChip`, same size/position as QuoteCard etc.) |
| `SqlAttritionChain`, `SqlAttritionChain916` | `data.panelCounts` — exact figure per panel; `handleTop` (916 only) |
| `SqlScaleComparison916` | `handleTop` — chip top-right (bottom-right holds the axis title) |
| `SqlPredictCard` | `scale`, `shiftY` — grow/centre the question block |

Layout changes: `SqlPlanBeat` / `SqlPlanBeat916` size the plan text to the largest mono size that
fits the card width (longest line) and height, and centre it — no clipping possible.
`SqlAttritionChain` counter, `SqlDivergentFates` badges and all four portrait headers now sit
inside the 5% title-safe inset (Gate V).

Registered lengths in `Root.tsx` now match the rev 3 audio (30 fps): AttritionChain 551f ·
PlanBeat 572f · ScaleComparison 476f · PredictCard 303f · DivergentFates 571f (landscape and
916 alike). The figures in the tables above are the Sep 16 values.

The `vertical/` folder named above no longer exists — the 9:16 is built in `short/`.
