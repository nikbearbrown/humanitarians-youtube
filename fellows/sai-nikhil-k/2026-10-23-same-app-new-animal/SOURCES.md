# SOURCES — Same App, New Animal

## Provenance

Sai asked (2026-10-26) for a video about extending Gavia to other wildlife,
with images from the app and of the other animals; he approved the plan and
concept and gave the screen for captures. The wildlife facts carry over from
`../2026-10-19-wildlife-beyond-loons/` (re-checked there on 2026-10-25).

## Sources

| What | Where | Used for |
|---|---|---|
| Gavia 0.3.1 (the installed app) | `/Applications/Gavia.app`, bundle `ai.humanitarians.gavia` | the six screenshots (B01, B03, B07) |
| Gavia source at v0.3.1 | github.com/nikhil-kunapareddy/gavia @ `760e465`; archived: `research/gavia_readme_v0.3.1.md`, `research/gavia_loon_v1_model_card.json`, `research/gavia_v0.3.1_preprocess.rs` | detector + tiler used in evidence; README's model-folder and tiling statements |
| NOAA Arctic Seals 2019 (Alaska Fisheries Science Center), LILA | `research/lila_noaa_arctic_seals_2019.html`; CSV + 20 frames in `evidence/data/` (not committed) | B02, B04, B05, B07 |
| NOAA seal counts | `evidence/seal_labels.py/.out` (copied from the 10-19 reel) | 14,311 seals boxed (B05) |

## Images

| Beat | File | What | Credit / licence |
|---|---|---|---|
| B01 | `app_loon.png` | result: 1 loon, 88% | Gavia 0.3.1 screenshot · photo Andrew C, CC BY 2.0 |
| B01 | `app_home.png` | home: "Is this a loon?" | Gavia 0.3.1 screenshot |
| B01 | `app_history.png` | Previous checks | Gavia 0.3.1 screenshot |
| B03 | `app_seals.png` | seals from the air: No loon detected | Gavia 0.3.1 screenshot · photo NPS, public domain |
| B03 | `app_eider.png` | Maine eider: 2 loons, 85% / 36% | Gavia 0.3.1 screenshot · photo Alan Schmierer, CC0 |
| B05 | `noaa_frame.jpg` | whole survey frame, downscaled | NOAA AFSC via LILA, CDLA-Permissive 1.0 |
| B05 | `noaa_tile_boxed.jpg` | one 960 px tile, NOAA's boxes outlined | NOAA AFSC via LILA, CDLA-Permissive 1.0 |
| B07 | `app_model.png` | Settings: Detection model row | Gavia 0.3.1 screenshot |
| B07 | `seal_parker.jpg` | harbor seals, Massachusetts | USFWS, public domain |
| B07 | `ringed_seal.jpg` | ringed seal, Finland | Estormiz, CC0 |
| B07 | `herring_gull.jpg` | herring gull, New York | Rhododendrites, CC BY-SA 4.0 |

Every file has a sidecar `images/src/<slug>.json`.

## Honesty log

- **No seal model exists.** The reel measures the current loon model and
  describes what would be built; it never shows a seal detector.
- **The eider and seal app results are single runs** on one photo each; B02's
  counts are the systematic measurement (20 random frames, 57 seals).
- **`~/Documents/gavia` hung on git** (likely iCloud-evicted files), so the source
  was cloned fresh from GitHub at the v0.3.1 tag instead.
- **Screen capture needed Screen Recording permission**; Sai switched it on
  (screenshot of System Settings, 2026-10-26 12:06).
