# FACTCHECK — Same App, New Animal

| # | Claim | Where | Checked against | Result |
|---|---|---|---|---|
| 1 | Gavia asks "is this a loon?" | B00, B01 | home screenshot: "Is this a loon?" | ✅ |
| 2 | Boxes every loon with a confidence; a person keeps or rejects it; history stays local | B01 | result screenshot (1 loon, 88%; Save result; Yes/No); README v0.3.1 ("your photos never leave your machine") | ✅ |
| 3 | 20 random NOAA frames, 57 seals | B02 | `seal_split.out` (seed 20261026) | ✅ measured |
| 4 | It found none; 4 "loon" boxes whole, 86 tiled | B02, B08 | `seal_check.out` at 0.25; Gavia's `evaluate` P = R = AP = 0 both ways | ✅ measured |
| 5 | Seal photo → "No loon detected"; Maine eider → "2 loons", 85% | B03, B00, B08 | app screenshots, 2026-10-26 | ✅ observed |
| 6 | The model has only ever seen loons | B03 | model card: `"classes": ["common loon"]`, dataset loonnet_v1 | ✅ |
| 7 | The model looks at 640 px | B04 | model card input shape [1, 3, 640, 640] | ✅ |
| 8 | Typical seal 64 px; ~6 px whole; ~43 px per tile | B04, B08 | `seal_scale.out` (median of 57; plan_tiles copy: 54 tiles of 960 px) | ✅ measured |
| 9 | Tiling hurts close-up loon photos | B06 | README v0.3.1: precision 0.906 → 0.074 with tiling on | ✅ |
| 10 | Seven seals in one tile | B05 | `make_survey_crops.py`: tile (1722, 3140, 2682, 4100) holds 7 of 7 | ✅ |
| 11 | 14,311 seals boxed; licence lets a trained model ship | B05, B08 | `seal_labels.out`; LILA page: CDLA-Permissive 1.0 (results not restricted) | ✅ |
| 12 | The app loads a retrained model dropped into its models folder | B07, B08 | README v0.3.1: "put its .onnx and .json files in the models folder … A choice of model then appears in Settings → Detection model" | ✅ |
| 13 | Ringed seals are most of NOAA's set | B07 | `seal_labels.out`: 11,382 / 14,311 = 79.5% | ✅ |
| 14 | Maine's seabird labels are public, photos not released | B07 | 10-19 reel `maine_labels.out`: 97,272 labels, 0 image files | ✅ |

## The math (B04)

1. `s_model = s × 640 / L`
2. `64 × 640 / 6576 ≈ 6.2 px (whole frame)`
3. `64 × 640 / 960 ≈ 42.7 px (one tile)`

Asserted in `build_beats.py` from `seal_scale.out`. Letterboxing scales the
longer side to 640, and these frames are landscape (6576 > 4384), so L = 6576
for the whole frame; tiles are square, L = 960. 64·640/6576 = 6.229;
64·640/960 = 42.667.

**Rendered-frame math review (2026-10-26, both aspects):** frames at each row's
reveal (≈ 1.5 / 8.3 / 12.2 s) and at 95% of the 19.27 s beat (`media/B04.mp4`,
`vertical/media/B04.mp4`). Italic s and L with upright "model" subscript; true
×, ≈ and slash; units "px" upright; no tofu or clipping; reveals inside the
15 s comp. 9:16 ink heights: rows 5.3% / 2.7% / 3.0% of frame height (floor 2%).
