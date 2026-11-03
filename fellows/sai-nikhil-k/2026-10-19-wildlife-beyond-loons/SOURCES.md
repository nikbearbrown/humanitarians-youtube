# SOURCES — Seals Pass, Seabirds Wait

## Provenance

The raw material is this folder's `research/` (four notes, 2026-10-19/20, with a
shortlist and a candidate ONE idea). On 2026-10-25 Sai was offered that angle
and replied "build it"; he then asked for the build to be finished while he
slept, so the title change and every judgement call below were made without
asking him. All on-screen figures were re-checked at source on 2026-10-25; the
research notes were treated as leads only.

## Sources (archived under `evidence/sources/` unless noted)

| What | Where | Used for |
|---|---|---|
| USGS data release, Kline, Lewis, Maher & Loftin 2023, doi:10.5066/P92SL92P | ScienceBase item 642d7360d34ee8d4add393cb (`sciencebase_642d7360.json`, `GOM2019SeabirdImageryCounts_FINAL.xml`); CSV in `evidence/data/` | 268 islands; "Three observers reviewed the images…"; release = CSV + XML only; the measured counts (B04, B05, B07, B08) |
| LILA, NOAA Arctic Seals 2019 (Alaska Fisheries Science Center) | `lila_noaa_arctic_seals_2019.html`; detections CSV + file list in `evidence/data/` | CDLA-Permissive; the measured seal counts (B05, B06, B07, B08) |
| NOAA InPort item 24457, "A Dataset of Aerial Survey Counts of Harbor Seals in Iliamna Lake, Alaska: 1984-2013" | `inport_24457_iliamna.html` | "all seals sighted were digitally photographed…"; "The total number of seals hauled out were counted from the digital photographs" (B06) |
| Anna Vallery, "We're Getting Better at Surveying Seabirds", Audubon Washington, 24 Sep 2026 | `audubon_seebird.html` | Houston Audubon + Rice; "going through the imagery took weeks"; 89% of birds, "about 19% of the time"; "cuts image review time by 80%" (B03) |
| BirdNET-Analyzer README | `birdnet_readme.md` (gh api, 2026-10-25) | code MIT; models CC BY-NC-SA 4.0 (B02, B08) |
| SpeciesNet (google/cameratrapai) and MegaDetector READMEs | `speciesnet_readme.md`, `megadetector_readme.md` | AddaxAI as the tool for running both "on your computer" (B02) |
| AddaxAI repo | `gh api repos/PetervanLunteren/AddaxAI`: "Free, open source, for Windows, macOS and Linux"; MIT | B02 |
| Gavia README (nikhil-kunapareddy/gavia) | `gavia_readme.md` | AGPL-3.0; works without internet; "Every result is meant to be reviewed by a person who knows loons" (B00, B02) |
| Repo licences | `gh api repos/<r>`, 2026-10-25: BirdNET-Analyzer MIT, MegaDetector MIT, cameratrapai Apache-2.0, AddaxAI MIT | B02 |

## Photographs (Wikimedia Commons, sidecars in `images/src/`)

| Beat | Slug | Place | Author | Licence |
|---|---|---|---|---|
| B04 | `counting_dots` | Bitter Lake, South Dakota | USFWS Mountain-Prairie | public domain |
| B04 | `herring_gull` | Quogue, New York | Rhododendrites | CC BY-SA 4.0 |
| B04 | `eider_maine` | Stonington, Maine | Alan Schmierer | CC0 |
| B04 | `cormorant_colony` | Virginia | Sarah Meadows, USFWS | public domain |
| B06 | `seal_aerial` | Glacier Bay, Alaska | National Park Service | public domain |
| B06 | `ringed_seal` | Oulu, Finland | Estormiz | CC0 |
| B06 | `seal_parker` | Parker River NWR, Massachusetts | USFWS Northeast | public domain |

`gbbg_maine` (great black-backed gull, Stonington, CC0) was fetched but not used.

## Honesty log

- **Title.** Offered as "Most Species Fail the Data Question"; built as "Seals
  Pass, Seabirds Wait" because "most" was never measured.
- **Dropped claims** (research notes marked them VERIFY, or the page was down):
  CDFW harbor-seal microscope/light-table method (map.dfg.ca.gov metadata page
  returned a maintenance page); USFWS brant YOLOv5 + 1–2% human check; river
  herring volunteer figures; Lyons 2019, Hayes, Chabot 2015 drone-count figures;
  Lindenmayer & Scheele "Do not publish". None appear in the reel.
- **Maine: 268 islands flown, 224 with a labelled bird** — both true, both shown
  where they belong (268 in narration as the survey; 224 in the evidence).
- **Seals: LILA's "around 80,000" images vs 88,228 files measured** (44,185
  colour + 44,043 thermal + 11 other files). Only the measured colour count is on
  screen. Boxes: 14,311 colour + 14,088 thermal = 28,399 (LILA: "around 28,000").
- **The seal boxes carry a `detection_score` column**, so they may be detector
  output that people reviewed; the reel says "boxed", never "hand-labelled".
- **"No installable offline app found"** for seals or Maine colonies is the result
  of research note 01's sweep (GitHub + literature), not a proof of absence.
- **Ringed seal photo** is the Baltic subspecies (*Pusa hispida botnica*); the
  caption says "Ringed seal", and NOAA's set is Alaskan ringed seals.
