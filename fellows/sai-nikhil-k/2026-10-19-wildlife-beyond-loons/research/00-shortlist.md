# Shortlist — which wildlife gets the next Gavia? (2026-10-20)

Synthesis of research 01–03. Every figure below is cited in those files; items marked
VERIFY there are not used here.

## The test (four questions per candidate)
1. **Demand** — is someone counting it by hand today, on the record?
2. **Data** — is there a labelled set we may train on and ship weights from (no NC clause)?
3. **Gap** — is there no installable, offline, review-first app for it already?
4. **Fit** — still photos or drone frames → boxes or points, like Gavia?

## Ranked

| # | target | demand | data | gap | fit |
|---|---|---|---|---|---|
| 1 | **Colonial seabirds on Maine's coast** (gulls, cormorants, eiders, terns) | USGS: 268 islands, "Three observers reviewed the images" | USGS point labels per observer (doi:10.5066/P92SL92P); **imagery not released** | SeeBird (Texas) aims to be open; nothing offline for Gulf of Maine species | ✅ aerial stills → points |
| 2 | **Seals at haul-outs** | photo counts done by eye (CDFW: microscope + light table) | NOAA Arctic seals, ~28,000 boxes, colour + thermal, CDLA-Permissive | no offline tool found | ✅ aerial stills → boxes |
| 3 | **Geese / brant** | USFWS replaced ocular surveys with photos | Izembek: 9,267 images, 521,270 boxes (USGS; licence to confirm) | agency already runs YOLOv5 + human check | ✅ — but already built in-house |
| 4 | **River herring** (MA fish ladders) | volunteer visual counts, "limited to brief daytime sampling windows" | LILA river herring, COCO, CDLA-Permissive | MIT/Woodwell system exists; open status not stated | ⚠️ video, not stills |
| 5 | **Sensitive species** (reptiles, raptor nests) | — | none found | — | the *why offline* argument, not a first build (Lindenmayer & Scheele 2017) |

## Don't build
- **Camera traps** — MegaDetector (MIT) + SpeciesNet (Apache-2.0) + AddaxAI (MIT desktop app) already run offline.
- **Bird song** — BirdNET covers it, but its weights are CC BY-NC-SA 4.0: usable for research, can't ship in an AGPL app. A permissive bird-audio model is a gap, just not Gavia's shape.
- **Anything trained on CC BY-NC data** (e.g. the New Mexico refuges waterfowl set) — the licence follows the weights.

## Candidate ONE idea for the reel
"The next Gavia isn't picked by how charismatic the animal is. It's picked by four
questions, and most species fail the data one." Seals pass all four today; Maine
seabirds pass three, and the missing one is a single email to USGS for the imagery.

## Open checks before narration
- Izembek licence at doi:10.5066/P9UHP1LE.
- Big Bird's UQ licence wording.
- Whether Maine 2019 imagery is obtainable (contact Kline / Loftin, UMaine Coop Unit).
- LibKey resolution of every paper cited (needs `/mcp` login).
