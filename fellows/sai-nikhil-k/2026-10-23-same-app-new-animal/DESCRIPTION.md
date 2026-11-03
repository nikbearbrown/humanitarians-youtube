Gavia asks one question about a photo: is this a loon? What would it take for the same app to count seals?

This week on Gavia, the offline loon-detection app, we tested it on other animals, using the released app and its own detector code, then wrote down what an extension would need.

The app today. Open a photo and Gavia boxes every loon it finds with a confidence score (88% on this video's test photo), and a person keeps the result or throws it out. Everything stays on your computer.

The run. We pointed Gavia 0.3.1's detector code at 20 frames drawn at random from NOAA's Arctic seal survey, holding 57 seals. At the app's own 0.25 threshold:

- Seals found: 0, on whole photos and with tiling on.
- Boxes it called loons: 4 on whole photos, 86 with tiling on.

In the app, a photo full of harbor seals came back "No loon detected": true, and no help if you're counting seals. A common eider from Maine came back "2 loons detected", 85%. The model has only ever seen loons, so it can't say "not a loon".

The scale. Gavia's model looks at 640 × 640 pixels. A typical seal in these survey frames is 64 pixels across. Shrink the whole 6,576-pixel frame to fit and the seal is about 6 pixels; cut it into Gavia's 960-pixel tiles first and it's about 43. Tiling makes the seal visible. Only a seal model can recognise it.

The extension:

- One model file per animal, starting with seals, trained on NOAA's open set (14,311 boxed seals, CDLA-Permissive). Gavia already loads a retrained model from its models folder.
- Tiling switched on by the model itself, because it hurts close-up loon photos (precision 0.906 → 0.074 on loonnet_v1).
- Counts per folder, exported as CSV.
- A reviewer's fixes kept as new training labels.
- Each model's measured accuracy, shown in the app.

Seals first, then Maine's seabirds once the survey photos behind their public labels are shared. No seal model exists yet: this is the plan, measured against what the app does today.

Try it yourself: pick an animal near you and ask an assistant whether a labelled photo set's licence lets you ship a model, how big the animal is in a typical survey photo, and who counts it by hand today. Then open the dataset page and check every answer.

Gavia, the project in this reel: https://github.com/nikhil-kunapareddy/gavia

Chapters:
0:00 Is this a loon? What about seals?
0:10 Gavia today
0:25 The loon model on 57 seals
0:40 Asked about other animals
0:54 Why aerial animals vanish: 6 px vs 43 px
1:13 One survey frame, two ways
1:29 What to build
1:47 The model slot, and who's next
2:03 Verdict
2:18 Your turn: pick your animal
2:33 Outro

Sources:
Gavia v0.3.1 (README, model card, detector and tiling code) — https://github.com/nikhil-kunapareddy/gavia
NOAA Arctic Seals 2019, LILA — https://lila.science/datasets/noaa-arctic-seals-2019/
USGS, Maine coastal seabirds from 2019 plane-based imagery — https://doi.org/10.5066/P92SL92P

Images:
App screens — Gavia 0.3.1 on a Mac, scratch storage folder; Settings cropped to one row
Common loon (in the app) — Andrew C, CC BY 2.0 — https://commons.wikimedia.org/wiki/File:Common_Loon_(Gavia_immer)_(16332756641).jpg
Harbor seals from the air, Alaska (in the app) — National Park Service, public domain
Common eider, Maine (in the app) — Alan Schmierer, CC0
NOAA survey frame and tile — NOAA AFSC via LILA, CDLA-Permissive 1.0; orange boxes are NOAA's labels
Harbor seals, Massachusetts — USFWS, public domain
Ringed seal, Finland — Estormiz, CC0
Herring gull, New York — Rhododendrites, CC BY-SA 4.0 — https://commons.wikimedia.org/wiki/File:American_Herring_Gull,_Quogue,_New_York_(45935).jpg

Hosted by Sai. Voice: Kokoro am_onyx, free and local. AI-generated narration; motion graphics built with Remotion; the equation typeset locally as SVG. The app results shown are what Gavia 0.3.1 returned. The seal counts come from Gavia's own detector code at v0.3.1, run on a MacBook Pro (M2 Pro) on 20 frames drawn with a fixed seed. No seal model was trained. No image was generated. No human-performed audio or video.

Gavia: https://github.com/nikhil-kunapareddy/gavia
Humanitarians AI: https://humanitarians.ai
Musinique: https://musinique.com
Medhavy AI: https://medhavy.com

TAGS: Gavia, wildlife AI, conservation technology, loon detection, seals, harbor seal, ringed seal, common eider, seabirds, Maine, aerial survey, NOAA, object detection, YOLO, image tiling, small object detection, open data, offline AI, Humanitarians AI, weekly progress, Computational Skepticism

#AI #ComputerVision #Conservation #Wildlife #Seals #OpenSource #HumanitariansAI #WeeklyUpdate
