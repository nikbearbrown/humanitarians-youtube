# FACTCHECK — Same App, New Plants

| # | Claim | Where | Checked against | Result |
|---|---|---|---|---|
| 1 | Last week Gavia learned to listen | B00 | CHANGELOG 0.4.0 (2026-10-30), the 10-30 reel | ✅ |
| 2 | Vegnet: a model for four invasive lake plants | B00, B01 | veg_v1.json `classes`; CHANGELOG 0.5.0 | ✅ |
| 3 | The box names the species: purple loosestrife, 97% | B01 | screenshot `app_loosestrife.png`; `lookalike_check.out` loosestrife_250894884 0.97 | ✅ observed |
| 4 | Check an image has a Model menu; Loonet for loons, Vegnet for the four | B01 | screenshot `app_model_menu.png` | ✅ |
| 5 | It's the model slot from two weeks ago, second model in it | B01 | 10-23 reel B07 (Settings → Detection model, "the app loads a retrained one"); README 0.5.0: Model menu + Settings → Detection model | ✅ |
| 6 | Headline mean AP@0.5 = 0.72 | B02, B00, B07 | README / CHANGELOG 0.5.0 0.72; `evaluate_vegnet.out` mean 0.7195 | ✅ measured |
| 7 | A hit = IoU with the reviewed box ≥ ½ | B02 | `examples/evaluate.rs` `IOU_MATCH = 0.5`, greedy match per class | ✅ |
| 8 | Each species gets an AP; the four are averaged | B02 | evaluate.rs: per-class rows and their mean ("the counterpart of Ultralytics' mAP50") | ✅ |
| 9 | Water chestnut 0.96; purple loosestrife 0.54 (reed 0.80, iris 0.59) | B02, B03, B07 | `evaluate_vegnet.out`: 0.9594, 0.5361, 0.7959, 0.5868 | ✅ measured |
| 10 | 26 training photos and 7 checked per species | B03 | train.txt / val.txt counts by species: 26 / 7 each | ✅ counted |
| 11 | Boxes drafted by another model, reviewed by a person | B03 | loonet README ("Grounding DINO drafted them and a person reviewed contact sheets"); README 0.5.0 | ✅ |
| 12 | Water chestnut has floating rosettes; loosestrife magenta spikes | B03 | the B03 photos themselves | ✅ visible |
| 13 | On its own invasive photos it boxes 25 of 28 | B04 | `lookalike_check.out` "vegnet val (invasive) 28 25" | ✅ measured |
| 14 | 40 iNaturalist photos of native look-alikes: 25 boxed; reed 5/8; watershield 7/8 | B04, B00, B07 | `lookalike_check.out` | ✅ measured |
| 15 | The rest were fireweed, blue vervain, blue flag iris; none of the 40 invasive | B04 | `lookalike_fetch.out` taxa; iNaturalist research-grade IDs (sidecars) | ✅ (IDs per iNaturalist) |
| 16 | Fireweed → purple loosestrife 97; watershield → water chestnut 95; American reed → common reed 98 | B05 | screenshots; `lookalike_check.out` 0.97 / 0.95 / 0.98 | ✅ observed + measured |
| 17 | The eider from two weeks ago: the loon model called it two loons | B05 | 10-23 reel B03 (app: "2 loons detected", 85%) | ✅ |
| 18 | All 132 of Vegnet's photos had an invasive in it | B05, B07 | label files: 132 images, 0 without boxes; all four-species folders | ✅ counted |
| 19 | The roadmap names the fixes (hand-checked boxes, more photos, natives, submerged e.g. Eurasian watermilfoil, place + date for mapping) | B06, B07 | ROADMAP v0.5.0 item 6 "It still needs"; "Later: GPS and date from EXIF … mapping invasive vegetation" | ✅ |
| 20 | Offline | B07 | README: "works without internet … your photos never leave your machine" | ✅ |

## The math (B02)

1. `IoU = |A ∩ B| / |A ∪ B| ≥ 0.5`
2. `mAP = (AP₁ + AP₂ + AP₃ + AP₄) / 4`
3. `(0.959 + 0.796 + 0.587 + 0.536) / 4 ≈ 0.720`

Read from Gavia's `examples/evaluate.rs` (IoU match 0.5; a box only matches a
label of its own class; per-class AP by the monotone envelope; mean over
classes). Row 3 uses the measured APs rounded to 3 places: sum 2.878, ÷ 4 =
0.7195, which rounds to 0.720 and equals the unrounded mean 0.7195 to 4 places.
Asserted in `build_beats.py`.

**Reproducible numeric case:** `cargo run --release --example evaluate -- --split
~/Documents/loonet/data/annotated/vegnet_v1/val.txt --model resources/models/veg_v1.onnx`
at v0.5.0 → the four rows above (`evaluate_vegnet.out`).

**Rendered-frame math review (2026-11-09, both aspects):** frames at each row's
reveal + 1 s (5.0 / 11.2 / 14.6 s) and at 15/50/85/95% of the 19.46 s beat, in
`media/B02.mp4` and `vertical/media/B02.mp4`. Upright IoU, mAP and AP with numeric
subscripts; |A ∩ B| / |A ∪ B| with bars and set symbols; ≥ and ≈ render; no tofu,
no clipping; reveals inside the 15 s comp. **Fixed on review:** the first render
typeset row 2 as `\frac{1}{4}\sum_{c=1}^{4} AP_c`, whose text-size ¼ and tall sum
shrank the row to ~2% of frame height; it is now one flat fraction and renders at
full size. 9:16: row 3 (the four APs) is the widest and renders small — digits
≈ 2.2% of frame height, above the 2% floor.
