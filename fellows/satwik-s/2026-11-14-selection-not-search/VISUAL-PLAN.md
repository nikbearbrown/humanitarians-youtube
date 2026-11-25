# VISUAL-PLAN — Week 16: Selection, Not Search

4K 16:9 (3840×2160 at scale=2 from 1920×1080). Two-skin palette: claude skin on UI beats (B00/B09); humanitarians tokens on body beats (B01–B08). Accent roles: **CRIMSON = similarity-only / rejected, TEAL = selection / shared vocabulary, SLATE = role structure / scale, GOLD = the "similarity is not relevance" finding, SAGE = robust across K.**

| Beat | Component | Visual |
|------|-----------|--------|
| B00 | ClaudeComposerAsk | composer ask + folder summary (shared claude scene) |
| B01 | W16TwoArms | two cards (retrieval = crimson, selection = teal) + "only difference" rule band |
| B02 | W16TwoSignals | two cards (similarity = crimson/imprecise, shared vocab = teal/precise) + gold rule band |
| B03 | W16SimNotRel | two tall crimson bars — 85% (17/20), 60% (12/20) share no project vocabulary |
| B04 | W16RobustK | K-sweep table (K=10/20/30) × 2 project rows, crimson percentages |
| B05 | W16Structure | two project panels (32 / 26 selected) with 4 role rows each |
| B06 | W16Weights | two cards (role = structure/slate, weights = order/teal) + slate rule band |
| B07 | W16Exclusion | two project panels: total excluded 864/559 + highlighted 109/63 high-sim-no-vocab + example id |
| B08 | W16Boundary | two columns MEASURED (sage) / THE LIMITS (crimson) + falsifiability stamp |
| B09 | ClaudeTitleOutro | title restate + handle + sign-off (shared claude scene) |

Shared helper block identical to Week14Reorder.tsx / Week15Parser.tsx. CW=1920, CH=1080, SAFE=100. Each body beat: SparkLine top, CornerBug bottom-right. durationInFrames = round(actual_duration_s × 30) after audio measured.
