# SHOTLIST — Automating the YouTube Review Pipeline

Typed work order. One row per beat: what fills the slot, who owns it, current state.

| Beat | Component | Status | Owner | Notes |
|---|---|---|---|---|
| B00 | `ClaudeComposerAsk` | EXISTS | pipeline | Registered, 1920x1080. Renders 4K via `--scale=2`. |
| B01 | `BrutalistHesitantWriter` | EXISTS | pipeline | Registered, 1920x1080. |
| B02 | `HaiPipelineReviewLoop` | TO BUILD | me | Lead: `HaiBrutalistE01Pipeline` - right register, but labels hardcoded, only prop is `sparkLine`. Build a sibling in that file. |
| B03 | `HaiPixelThreshold` | TO BUILD | me | Two file cards, counting readouts, threshold line. |
| B04 | `HaiSoftFourK` | TO BUILD | me | Peel-back reveal + stretch. The one beat that shows the defect itself. |
| B05 | `HaiRenderDefaultDrift` | TO BUILD | me | Code line rewrite + surfacing comment. Cut this beat to reach 3 min. |
| B06 | `HaiStageOneSort` | TO BUILD | me | Folder watch, two-way sort, note card, deleted:0 counter. |
| B07 | `HaiOutroMismatch` | TO BUILD | me | Declared vs found handle, mismatch flag, precedent line. |
| B08 | `HaiStageTwoThree` | TO BUILD | me | Two stage chips, check jumping upstream. |
| B09 | `HaiStageFourNeeds` | TO BUILD | me | Two need-cards, one stamping LOCKED. Longest hold in the reel. |
| B10 | `ClaudeComposerAsk` | EXISTS | pipeline | Reused with `greeting: "Your turn."` |
| B11 | `OutroSeries` | EXISTS | pipeline | HAI outro. NOT `ClaudeTitleOutro`. |

## Counts

- 4 beats use existing registered components (B00, B01, B10, B11)
- 8 beats need new components (B02-B09)

The earlier estimate of "four new components" was low. The honest number is
eight. Until they exist, those beats compile as labelled request cards and the
first cut is a watchable previz - which is how the tool is designed to work.

## Build rules for the new components

1. **Author at 1920x1080.** `remotion_scenes.py:85` hardcodes `--scale=2`, so a
   1920x1080 composition renders as true supersampled 4K. Never author at
   1280x720 - 48 existing components are, and that is the defect this reel is
   about.
2. **Register both ids** if a portrait cut is ever wanted: `<Name>` at 3840x2160
   and `<Name>916` at 2160x3840. Do not add ratio-encoded legacy names.
3. **Run `./art scene-index` after adding any component** or nobody can find it.
4. **Humanitarians palette**, not the Claude skin, for the body beats.
5. **Fill the canvas.** Undersized content in the top third is a defect under
   FILL-THE-CANVAS LAW. Keep everything inside the 5% title-safe inset.
