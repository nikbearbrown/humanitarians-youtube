# FACTCHECK — Seals Pass, Seabirds Wait

Every claim → where → how checked. Files are under `evidence/` unless noted.

## Claims

| # | Claim | Where | Checked against | Result |
|---|---|---|---|---|
| 1 | Gavia finds loons in photos on your own computer; a person checks every box | B00 | `sources/gavia_readme.md`: "works without internet"; "Every result is meant to be reviewed by a person who knows loons" | ✅ |
| 2 | Camera traps: MegaDetector, SpeciesNet and the free AddaxAI app run on your own computer | B02 | SpeciesNet README: "AddaxAI is a popular graphical tool for running SpeciesNet on your computer"; MegaDetector README points to AddaxAI; AddaxAI repo: "Free, open source, for Windows, macOS and Linux" | ✅ |
| 3 | BirdNET's models are licensed non-commercial; Gavia's AGPL can't carry that | B02, B08 | `sources/birdnet_readme.md`: models CC BY-NC-SA 4.0; Gavia README: AGPL-3.0 (AGPL permits commercial use, so NC weights can't ship under it) | ✅ |
| 4 | Houston Audubon flew a drone over Texas waterbird colonies; going through the imagery took weeks | B03 | `sources/audubon_seebird.html` (Anna Vallery, 24 Sep 2026): Galveston Bay colonies; "But going through the imagery took weeks." | ✅ |
| 5 | Computer help: about 19% of the time; 80% cut; 89% of the birds a biologist found | B03 | same: "detected 89% of the birds identified by a biologist … while requiring only about 19% of the time"; "cuts image review time by 80%" | ✅ |
| 6 | In 2019 a survey plane photographed 268 islands; three observers went through the images | B04, B07 | `sources/sciencebase_642d7360.json`: "flew over 268 islands within the Gulf of Maine"; "Three observers reviewed the images, identified detected birds to species and behavior, and reconciled any differences." Dates 30 May – 3 Jun 2019 | ✅ |
| 7 | Herring gull 53%, eider 15%, cormorant 13% of Maine's labels | B04 captions | `maine_labels.out`: HERG 51,428; COEI 8,237 + F_COEI 6,267 (female eider, per the XML); DCCO 12,469; of 97,272 | ✅ 52.9 / 14.9 / 12.8% |
| 8 | Observers agreed on species 99% of the time (2+ observers) | B04 | `maine_labels.out`: 84,233 of 85,112 = 99.0% | ✅ |
| 9 | Maine: 97,272 birds labelled, zero images | B05, B07, B08 | `maine_labels.out`: 97,272 rows / unique ids; release files = CSV + XML, 0 image files | ✅ |
| 10 | NOAA Arctic seals: 14,311 seals boxed, on 44,185 colour images, permissive licence | B05, B06, B07, B08 | `seal_labels.out`; LILA page: CDLA-Permissive 1.0 | ✅ |
| 11 | Ringed seals ≈ 80% of NOAA's boxed seals | B06 caption | `seal_labels.out`: 11,382 / 14,311 = 79.5% | ✅ |
| 12 | On Iliamna Lake, NOAA photographed every harbor seal it saw from a plane, then counted them from the photos | B06 | `sources/inport_24457_iliamna.html`: "all seals sighted were digitally photographed …"; "The total number of seals hauled out were counted from the digital photographs" | ✅ |
| 13 | No installable offline app found that counts seals in photos | B06, B07 | research note 01 (GitHub + literature sweep, 2026-10-20); worded as "we found no…" | ⚠️ search result |
| 14 | The Maine release names a contact | B07 | ScienceBase contacts: Cyndy Loftin, Point of Contact | ✅ |

## The math (B03)

Rows, as typeset:

1. `t_assisted ≈ 0.19 t_by hand` — the article's "about 19% of the time".
2. `1 − 0.19 = 0.81 ≈ 80%` — the rounding behind "cuts image review time by 80%".
3. `N_found = 0.89 N_biologist` — "detected 89% of the birds identified by a biologist".

**Algebra check** (asserted in `build_beats.py check_figures`): 1 − 0.19 = 0.81;
|0.81 − 0.80| < 0.02, so the article's two figures are consistent. Approximation
signs where the source says "about"; equality where it states a share.

**Rendered-frame math review (2026-10-26, both aspects):** frames at each row's
reveal (6.8 / 10.0 / 13.8 s) and at 50 / 95% of the 19.58 s beat, from
`media/B03.mp4` and `vertical/media/B03.mp4` (`_qc/frames/`, `_qc/frames916/`).
- Italic t and N with upright subscripts ("assisted", "by hand", "found",
  "biologist"); true minus sign; ≈ and % render; no tofu, nothing clipped; every
  reveal ≤ 13.5 s, inside the 15 s comp.
- First cut: row 3 sat close to a 3-line conditions note at 4K. The note was cut
  to 2 lines and B03 re-rendered; the gap is now clear in both aspects.
- Portrait: the three rows span the frame width and are well above the 2% floor.

## The numeric cases (B05)

```
python3 evidence/maine_labels.py > evidence/maine_labels.out
python3 evidence/seal_labels.py  > evidence/seal_labels.out
```

Python 3.11.5, standard library only, 2026-10-25. Input sha256 values are in the
.out files. `build_beats.py` reads every on-screen number from them and asserts it.
