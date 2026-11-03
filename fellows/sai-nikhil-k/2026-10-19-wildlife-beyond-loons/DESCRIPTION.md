Which animal should Gavia count next? Not the most charismatic one. The one that passes four questions.

This week on Gavia, the offline loon-detection app, there was no release. It was research: where should the next Gavia point? Four questions for each candidate. Demand: is someone counting this animal by hand today, on the record? Data: is there a labelled set we may train on and ship the weights from? Gap: is there no installable, offline app for it yet? Fit: photos or drone frames, turned into boxes or points, the way Gavia works?

Where not to build. Camera traps fail the gap question: MegaDetector, Google's SpeciesNet and the free AddaxAI app already run on your own computer. Bird song fails the data question: BirdNET's models are licensed CC BY-NC-SA 4.0, and Gavia's AGPL-3.0 licence can't carry them.

What demand looks like. On the Texas coast, Houston Audubon flew a drone over waterbird colonies, and reviewing the imagery by hand took weeks. Their computer-assisted workflow with Rice University (SeeBird) needed about 19% of the time: 1 − 0.19 = 0.81, the "80%" cut they report. It found 89% of the birds a biologist found, so a person still checks. That's Gavia's shape.

The data question, measured. We downloaded both releases and counted them:

- Maine's coastal seabirds (USGS): in 2019 a plane photographed 268 islands, and three observers reviewed the images bird by bird. The release holds 97,272 labelled birds on 224 islands (53% herring gulls), and observers agreed on species 99.0% of the time. It contains zero images.
- NOAA's Arctic seals (LILA): 14,311 seals boxed on 44,185 colour images, 80% of them ringed seals, under CDLA-Permissive.

Seals pass all four. NOAA photographs harbor seals from the air and counts them from the photos; the data is open; we found no installable offline app that counts seals; and seals seen from above are boxes on a photo, like loons. Maine's seabirds pass three: the labels are public, the photos aren't, so the next step there is a request for the imagery, not code.

Try it yourself: pick an animal you care about and ask an assistant who counts it by hand today, whether a labelled set's licence lets you ship weights, whether an offline tool already exists, and whether photos fit. Then open the licence page yourself and check its answer.

Gavia, the project in this reel: https://github.com/nikhil-kunapareddy/gavia

Chapters:
0:00 Which animal gets the next Gavia?
0:12 Four questions: demand, data, gap, fit
0:29 Where not to build: camera traps and bird song
0:50 What demand looks like: 19% of the time, 89% of the birds
1:10 Maine's coastal seabirds
1:29 The data question, measured
1:48 Seals pass all four
2:08 The ranking: build now vs request images
2:22 Verdict
2:34 Your turn: run the four questions
2:50 Outro

Sources:
USGS, Maine coastal seabirds from 2019 plane-based imagery (Kline et al. 2023) — https://doi.org/10.5066/P92SL92P
NOAA Arctic Seals 2019, LILA — https://lila.science/datasets/noaa-arctic-seals-2019/
NOAA, harbor seal aerial survey counts, Iliamna Lake — https://www.fisheries.noaa.gov/inport/item/24457
Audubon, "We're Getting Better at Surveying Seabirds" (2026) — https://www.audubon.org/washington/news/were-getting-better-surveying-seabirds
BirdNET-Analyzer · MegaDetector · SpeciesNet · AddaxAI (GitHub)

Photographs (Wikimedia Commons):
Aerial colony photo, South Dakota — USFWS, public domain
Herring gull, New York — Rhododendrites, CC BY-SA 4.0 — https://commons.wikimedia.org/wiki/File:American_Herring_Gull,_Quogue,_New_York_(45935).jpg
Common eider, Maine — Alan Schmierer, CC0
Cormorant colony, Virginia — Sarah Meadows, USFWS, public domain
Harbor seals from the air, Alaska — National Park Service, public domain
Ringed seal, Finland — Estormiz, CC0
Harbor seals, Massachusetts — USFWS, public domain

Hosted by Sai. Voice: Kokoro am_onyx, free and local. AI-generated narration; motion graphics built with Remotion; the equation typeset locally as SVG. The dataset counts come from scripts run for this video on the public USGS and NOAA files; every other figure was checked at its source on October 25, 2026. "No offline app found" is our search result, not proof that none exists. The aerial colony photo is from South Dakota, not Maine. No image was generated. No human-performed audio or video.

Gavia: https://github.com/nikhil-kunapareddy/gavia
Humanitarians AI: https://humanitarians.ai
Musinique: https://musinique.com
Medhavy AI: https://medhavy.com

TAGS: Gavia, wildlife AI, conservation technology, computer vision, seals, harbor seal, ringed seal, seabirds, Maine, herring gull, common eider, aerial survey, open data, dataset licence, BirdNET, MegaDetector, SpeciesNet, LILA, USGS, NOAA, Humanitarians AI, weekly progress, Computational Skepticism

#AI #ComputerVision #Conservation #Wildlife #OpenData #OpenSource #HumanitariansAI #WeeklyUpdate
