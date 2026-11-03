# Research 3 — who counts wildlife by hand (accessed 2026-10-20)

## 1. Colonial waterbirds — Texas coast (Houston Audubon + Rice) → "SeeBird"
- Audubon Washington, "We're Getting Better at Surveying Seabirds", 2026-09-24
  (audubon.org/washington/news/were-getting-better-surveying-seabirds):
  - "But going through the imagery took weeks."
  - computer-assisted workflow "requir[ed] only about 19% of the time"; "cuts image review time by 80%".
  - "We're calling this growing suite of tools SeeBird." "our goal was to make the tools we developed open source"; first published 2022.
  - distinguishes "Royal and Sandwich Tern"; Texas colonies "support hundreds of thousands of nesting pelicans, terns, herons, egrets, and skimmers every single year." Built at Chester Island, Matagorda Bay.
- Paper: "Deep object detection for waterbird monitoring using aerial imagery", arXiv 2210.04868 (16 species).
- → Demand is real AND someone is already building the open tool. Gavia-style angle: offline desktop review app on top, or a different region/species.

## 2. Gull colonies — UK (Rush et al. 2018)
- "Can drones count gulls? Minimal disturbance and semiautomated image processing with an unmanned aerial vehicle for colony-nesting seabirds", Rush, Clarke, Stone, Wood, Ecology and Evolution 2018, DOI 10.1002/ece3.4495.
  - manual counting "proved to be time-consuming in our study system and more prone to errors" (§4)
  - large image volumes "become unwieldy for larger populations and may thus be subject to observer error during manual counts" (§1.3)
  - batch processing in ArcGIS, "reducing user time greatly" — no number.
- Search summary also surfaced (NOT yet verified at source): Lyons et al. 2019 "between three and eight times faster" for nests; burrow-nesting shearwaters thermal counts "approximately 5% of the time"; Hayes et al. "within 5% of human counts, about 90% of the time". VERIFY before use.

## 3. River herring — Massachusetts fish ladders (MIT Sea Grant + Woodwell + MIT CSAIL)
- MIT News, "Augmenting citizen science with computer vision for fish monitoring", 2026-03-25:
  - monitored "primarily through traditional visual counting and volunteer-based programs"
  - "Volunteer visual counts are limited to brief daytime sampling windows"
  - manual video review "is still labor-intensive and time-consuming"
  - "they labeled 1,435 video clips and annotated 59,850 frames"; "the system counted 42,510 river herring" (2024 Coonamessett)
  - counts "consistent with traditionally established estimates"; code/model open-source status not stated.
  - People: Zhongqi Chen, Linda Deegan (Woodwell); Robert Vincent, Kevin Bennett (MIT Sea Grant); Sara Beery, Timm Haucke (CSAIL).
- Association to Preserve Cape Cod volunteer program: "300+ volunteers/annually", 3 shifts/day, 10-minute sampling (mass.gov deck, search summary — VERIFY).
- Training data already public: LILA mit-sea-grant-river-herring (CDLA-Permissive) — see research 2.
- → Strong New England analog to loons: volunteer program, video already captured, open data exists. Input is video, not stills.

## 4. Fall-staging brant — Izembek Lagoon, Alaska (USGS → USFWS)
- USGS, "Optimizing surveys of fall-staging geese using aerial imagery and automated counting" (pubs.usgs.gov/publication/70239012): ML counts, manually corrected; ocular surveys at the lagoon run "more than 40 years".
- USFWS Fall Brant Survey report (sciencebase item 67a6a615d34e329fb20398c2, search summary): YOLO v5 trained on 2017–2019 photos, applied to 2022–2025, human validator checks a 1–2% subsample; Pacific Flyway Council replaced the winter survey with this photo survey. VERIFY wording.
- → Proof the agency workflow already went "detector + human check". It's the shape Gavia ships; data public (research 2).

## 5. Colonial seabirds — Maine coastal islands (USGS / UMaine Coop Unit) ← same region as loons
- Kline, Lewis, Maher & Loftin 2023, USGS data release doi:10.5066/P92SL92P — "Point locations and species and behavioral identifications of colonial nesting seabirds on Maine's coastal islands interpreted from 2019 plane-based imagery" (ScienceBase item 642d7360d34ee8d4add393cb, JSON fetched 2026-10-20):
  - plane "flew over 268 islands within the Gulf of Maine"; 100-megapixel PhaseOne camera; "ground sampling distance of 2 cm/px"
  - focal species: "Herring Gull, Great Black-backed Gull, Double-crested Cormorant, Common Eider, and Tern spp."
  - **"Three observers reviewed the images, identified detected birds to species and behavior, and reconciled any differences."**
  - "collected as part of a recurrent survey of colonial nesting birds on Maine's coastal islands."
  - Files: GOM2019SeabirdImageryCounts_FINAL.csv (16,255,217 B) + .xml. **Labels only — imagery not in the release** (would have to be requested).
- Chabot, Craik & Bird 2015, "Population Census of a Large Common Tern Colony with a Small Unmanned Aircraft", PLoS ONE 10(4): e0122588 (PMC4398491): colony ">6,000 nests" at Tern Islands, New Brunswick; whole-colony aerial counts "93.6% and 94.0%" of the ground count.
- Gulf of Maine Seabird Working Group tern census = ground-based egg/nest counts (search summary, VERIFY).

## 6. Seals — photo counts still done by eye
- California harbor seal record (CDFW BIOS ds106 metadata): seals "were identified and enumerated from processed photographs using a Nikon binocular dissecting microscope ... over a Bausch and Lomb 'corrected' light table" (historic method; later image software).
- Alaska standard: oblique photos taken in flight, reviewed after the flight to count individuals (search summary of NOAA/Springer sources, VERIFY).
- Training data: LILA noaa-arctic-seals-2019, ~28,000 boxes colour + thermal, CDLA-Permissive (research 2). No Gulf of Maine harbour-seal photo set found.

## 7. Why offline matters — sensitive locations
- Lindenmayer & Scheele 2017, "Do not publish", Science 356(6340):800–801, DOI 10.1126/science.aan1362: open species-location data can fuel poaching; example (via ANU news summary) the pink-tailed worm-lizard — after survey locations were published to an online atlas, trespassers likely linked to the pet trade appeared at study sites.
- → An app that never uploads photos (EXIF GPS included) is a feature for reptiles, raptor nests, orchids — not just for no-signal lakes.
