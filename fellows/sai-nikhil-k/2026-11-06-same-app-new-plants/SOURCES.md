# SOURCES — Same App, New Plants

## Provenance

Sai asked (2026-11-09) for two backlog videos, one feature each, from his repo
<https://github.com/nikhil-kunapareddy/gavia>: November 6 = "Invasive vegetation
detection". He chose the angle and title, said nothing is to be left out, and
gave a hands-off window for the app screenshots.

## Sources

| What | Where | Used for |
|---|---|---|
| Gavia v0.5.0 release + source | github.com/nikhil-kunapareddy/gavia @ `5dd8471` (tag v0.5.0); archived: `research/gavia_CHANGELOG_v0.5.0.md`, `research/gavia_README_v0.5.0.md`, `research/gavia_ROADMAP_v0.5.0.md`, `research/gavia_veg_v1_card.json`, `research/gavia_commit_e329602.txt` | the feature, the four species, the README's 0.720, the roadmap's to-do list |
| Gavia v0.5.0 (built + run) | scratch clone at the tag; `/Applications/Gavia.app` 0.5.0 | evaluate + look-alike runs; screenshots |
| loonet vegnet v1 | `~/Documents/loonet` (local; commit `8664322`); archived: `research/loonet_vegnet_v1_README.md` | 132 iNaturalist photos, 33 per species, Grounding DINO drafts, a box = a stand |
| vegnet_v1 split | `data/annotated/vegnet_v1/{train,val}.txt` + labels (not committed) | B02 re-run; 26 + 7 per species; every photo has a box |
| Native look-alikes | iNaturalist API, fixed sample (`evidence/lookalike_fetch.py`); photos + sidecars in `evidence/data/lookalikes/` (not committed) | B04, B05 |
| Releases | `evidence/releases.out` | dates only (0.5.0 published 2026-11-02 UTC) |

## Week-scope commits (Gavia, after 0.4.0)

| Commit | Date | Author | What |
|---|---|---|---|
| `e329602` | 2026-11-01 | Sai Nikhil Kunapareddy | Add Vegnet, an invasive plant model, with a Model menu on the Check page |
| `4ac6248` | 2026-11-01 | Sai Nikhil Kunapareddy | Release 0.5.0 |

loonet: `8664322` "vegnet: detect invasive lake plants; v1 trained on drafted
boxes" (Sai, 2026-10-30). No other authors in the window.

## Images

| Beat | File | What | Credit / licence |
|---|---|---|---|
| B01 | `app_loosestrife.png` | result: Purple loosestrife 97% | Gavia 0.5.0 screenshot · photo Brian Finzel, CC BY-SA |
| B01 | `app_model_menu.png` | Model menu open | Gavia 0.5.0 screenshot |
| B01 | `app_veg_home.png` | "Is this an invasive plant?" | Gavia 0.5.0 screenshot |
| B03 | `sp_chestnut.jpg` | water chestnut, Kingfisher Pond, MA | Jasmine Ganter, CC BY (iNaturalist) |
| B03 | `sp_reed.jpg` | common reed, Milwaukee, WI | Eric Schmidt, CC BY (iNaturalist) |
| B03 | `sp_iris.jpg` | yellow flag iris, Millbrook, AL | Rob John, CC BY (iNaturalist) |
| B03 | `sp_loosestrife.jpg` | purple loosestrife, Jamesville, NY | Douglas Goldman, CC BY-SA (iNaturalist) |
| B05 | `app_fireweed.png` | native fireweed → Purple loosestrife 97% | Gavia 0.5.0 screenshot · photo CC0 (Grayson County, VA) |
| B05 | `app_watershield_crop.png` | native watershield → Water chestnut 95% | Gavia 0.5.0 screenshot · Steven Lamonde, CC BY |
| B05 | `app_american_reed_crop.png` | native American reed → Common reed 98% | Gavia 0.5.0 screenshot · Brandon Corder, CC BY |
| — | `app_model_setting.png` | Settings: Detection model row (cropped) | Gavia 0.5.0 screenshot (not used on screen) |

Every file has a sidecar `images/src/<slug>.json`.

## Honesty log

- **Four scores for one set of weights.** veg_v1.json `metrics`: mAP50 0.798
  (Ultralytics, recorded in the checkpoint during training); loonet README: 0.77
  (Ultralytics val); Gavia commit `e329602`: 0.731 "through Ultralytics' own square
  pipeline"; Gavia README / CHANGELOG: 0.720 (Gavia's `evaluate`, letterboxed like
  the app). Re-measured: 0.7195 with Gavia's evaluator. The reel shows only the
  app's number and says what it's made of.
- **The look-alike sample is unfiltered**: first 8 qualifying observations per
  taxon below a fixed id; 40 photos, all kept (some are seed heads or leaves only).
- **"Not one of the forty is invasive"** rests on iNaturalist research-grade IDs.
  The American reed subspecies is the weakest of those; flagged in PEDAGOGY.
- **The species photos in B03 are from Vegnet's own dataset** (loonet's
  manifest), credited; they illustrate the species, not a result.
