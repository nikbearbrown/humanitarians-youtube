# Research 2 — open labelled wildlife datasets (accessed 2026-10-20)

Source: each dataset's own page on lila.science/datasets/<slug>, fetched with curl 2026-10-20.
Quotes are the page's text. CDLA-Permissive = Community Data License Agreement (permissive variant):
allows sharing results (e.g. trained weights) — compatible with shipping weights in an AGPL app.

| dataset (lila slug) | taxa | input | labels | size (as stated) | licence |
|---|---|---|---|---|---|
| izembek-lagoon-waterfowl | brant, Canada goose, emperor goose, gull | aerial, 8688×5792 | boxes (point-derived, fixed size) | 9,267 images; 521,270 boxes (brant 424,790; Canada goose 47,561; gull 5,631; emperor goose 2,013; other 5,631) | LILA page states none; source is USGS data release doi:10.5066/P9UHP1LE (Weiser et al. 2022) — USGS releases are usually public domain, CONFIRM at DOI |
| noaa-arctic-seals-2019 | ice seals | aerial colour + thermal | boxes | "around 28,000 bounding boxes (14,000 on color images, 14,000 on thermal images)" | CDLA-Permissive |
| aerial-seabirds-west-africa | royal tern, Caspian tern, gray-headed gull | UAV orthomosaic | points | 21,516 point annotations | CDLA-Permissive |
| big-bird | 102 bird species | UAV, global | boxes + polygons | 4,284 images (3,209 empty); 49,990 annotations (41,337 boxes, 8,653 polygons) | "University of Queensland Permitted Re-Use with Acknowledgement License" — check terms |
| uas-imagery-of-migratory-waterfowl-at-new-mexico-wildlife-refuges | waterfowl | UAS | boxes (DBSCAN consensus of volunteer boxes) | not captured | **CC BY-NC 4.0** — NC risk |
| duck-pictures-in-wetlands | wetland birds + mammals, Finland | camera trap | species tags, adult/juvenile, counts (COCO Camera Traps) | 674,426 images | CDLA-Permissive |
| boxes-on-bees-and-pollen | bees + pollen | close-up | boxes | ~5,000 images; ~50,000 annotations | CDLA-Permissive |
| mit-sea-grant-river-herring | river herring (~80%) + trout, bass, perch, eel, sunfish, lamprey | underwater fish-ladder cameras, MA (Coonamessett, Ipswich, Santuit) | COCO-format annotations | not captured | CDLA-Permissive |
| beluga-id-2022 | beluga whale, Cook Inlet AK | boat + drone | full-image boxes, viewpoint, individual ID | 5,902 photos; 1,617 encounters | CDLA-Permissive |
| conservationdrones | humans + animals | aerial thermal video | boxes + tracks | 48 real + 124 synthetic videos (62k + 100k frames) | CDLA-Permissive |
| new-zealand-wildlife-thermal-imaging | invasive predators: possum, rodents, cats, hedgehogs, mustelids | thermal video (Cacophony Project) | track labels | 121,190 videos | CDLA-Permissive |
| community-fish-detection-dataset | fish | aggregate of ~17 sets | boxes | ">935,000 bounding boxes"; per-set licences, "some licenses include an NC restriction" | mixed |

Other LILA sets with individual IDs + boxes (CDLA unless noted, not re-checked): leopard-id-2022, hyena-id-2022, great-zebra-giraffe-id, whale-shark-id. Camera-trap sets omitted — that input type is already served (research 1).

## Outside LILA
- **SeaTurtleID2022** (Kaggle wildlifedatasets/seaturtleid2022; arXiv 2211.10307, Adam et al., WACV 2024): "8729 photographs of 438 unique individuals collected within 13 years"; identities, timestamps, body-part segmentation masks. Kaggle licence field: "Other (specified in description)" — terms not found in the description excerpt; UNVERIFIED. Individual re-ID, not counting.
- **Weinstein et al. 2022**, "A general deep learning model for bird detection in high-resolution airborne imagery", Ecological Applications (weecology.org/publication/weinstein-2022-general). Data/licence location UNVERIFIED; the model ships in DeepForest (MIT).
- **UQ "Permitted Re-Use with Acknowledgement"** (Big Bird's licence): UQ Library lists it as one of four standard eSpace licences; operative wording not found — CONFIRM before training weights on Big Bird.

## BY TAXON (synthesis)
- **Waterfowl / geese:** strongest. Izembek (521k boxes, USGS) + NM refuges (NC — avoid) + DuckNet code.
- **Colonial seabirds / terns / gulls:** West Africa (21.5k points, CDLA) + Big Bird (102 spp, UQ licence to confirm).
- **Seals:** NOAA Arctic ice seals (~28k boxes colour+thermal, CDLA). Harbor/grey seal haul-outs: no LILA set found.
- **Whales:** individual ID (beluga, CDLA; Flukebook data server-side). Not counting.
- **Sea turtles:** SeaTurtleID2022 = individual ID only; no nest/track box set found.
- **Fish:** river herring at MA fish ladders (CDLA, COCO) — a New England analog of loon monitoring.
- **Pollinators:** bees + pollen boxes (~50k, CDLA).
- **Invasive predators (NZ):** thermal video tracks, 121,190 videos (CDLA).
- **Amphibians / reptiles:** no permissive box set found in this sweep.
