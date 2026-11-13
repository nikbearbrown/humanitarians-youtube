Last week, Gavia learned to listen. This week it learned a new subject: Vegnet, a model for four invasive lake plants. How good is it, and does it know a native plant when it sees one?

This week on Gavia, the offline loon app: version 0.5.0 adds a Model menu and Vegnet. We explain its headline score, then show it 40 photos of native plants that look like the invasives, using the app's own code.

The change. Check an image now has a Model menu: Loonet looks for loons, Vegnet for purple loosestrife, common reed (introduced Phragmites), water chestnut and yellow flag iris, and every box names its species. It's the model slot we pointed to two weeks ago, with a second model in it.

What 0.72 means. A box counts as a hit when its intersection over union with the reviewed box is at least 0.5. Each species gets an average precision, and the four are averaged:

- mAP = (0.959 + 0.796 + 0.587 + 0.536) / 4 ≈ 0.720
- water chestnut 0.96, common reed 0.80, yellow flag iris 0.59, purple loosestrife 0.54

Re-measured with Gavia 0.5.0's own evaluator on Vegnet's 28 validation photos (32 stands). Each species was trained on 26 photos and checked on 7, with boxes drafted by Grounding DINO and reviewed by a person.

The look-alike test. We took 40 research-grade iNaturalist photos of five native plants that resemble the invasives (fireweed, blue vervain, American reed, blue flag iris, watershield; 8 each, a fixed sample) and ran Gavia's detector with Vegnet at the app's own 0.25 threshold:

- Its own invasive validation photos: 25 of 28 boxed
- Native look-alikes: 25 of 40 boxed
- Native American reed: 5 of 8 · watershield: 7 of 8 · fireweed: 5 of 8

In the app, native fireweed came back "Purple loosestrife", 97%; watershield "Water chestnut", 95%; American reed "Common reed", 98%. Every one of Vegnet's 132 photos had an invasive in it, so it never learned what native looks like, just as the loon model once called a Maine eider two loons.

What's next, from Gavia's own roadmap: hand-checked boxes, many more photos per species, native look-alikes in training, submerged species like Eurasian watermilfoil, and GPS and dates exported for mapping. Until then, treat each box as a lead for someone who knows plants.

Try it yourself: pick an invasive plant near you, ask an assistant which native plants get mistaken for it and what tells them apart in a photo, then find one of each on iNaturalist and check every answer.

Gavia, the project in this reel: https://github.com/nikhil-kunapareddy/gavia

Chapters:
0:00 A new subject for Gavia
0:12 The Model menu
0:30 What 0.72 means
0:49 Four invaders
1:07 Native look-alikes: 25 of 40
1:26 Three natives, called invasive
1:45 Still to do
2:04 Verdict
2:20 Your turn: know the natives
2:32 Outro

Sources:
Gavia v0.5.0 (CHANGELOG, README, ROADMAP, model card, evaluator) — https://github.com/nikhil-kunapareddy/gavia/releases/tag/v0.5.0
iNaturalist (research-grade observations, CC0 / CC BY / CC BY-SA) — https://www.inaturalist.org
loonet's vegnet v1 (training data and drafted labels) — Sai's loonet project

Images:
App screens — Gavia 0.5.0 on a Mac, scratch storage folder; two small panels cropped to the result
Purple loosestrife (in the app) — Brian Finzel, CC BY-SA, via iNaturalist
Water chestnut — Jasmine Ganter, CC BY, via iNaturalist
Common reed — Eric Schmidt, CC BY, via iNaturalist
Yellow flag iris — Rob John, CC BY, via iNaturalist
Purple loosestrife — Douglas Goldman, CC BY-SA, via iNaturalist
Fireweed (in the app) — CC0, via iNaturalist
Watershield (in the app) — Steven Lamonde, CC BY, via iNaturalist
American reed (in the app) — Brandon Corder, CC BY, via iNaturalist

Hosted by Sai. Voice: Kokoro am_onyx, free and local. AI-generated narration; motion graphics built with Remotion; the equation typeset locally as SVG. The app results shown are what Gavia 0.5.0 returned on this Mac. The scores come from Gavia's own evaluator and detector at v0.5.0, run on a MacBook Pro. No image was generated. No human-performed audio or video.

Gavia: https://github.com/nikhil-kunapareddy/gavia
Humanitarians AI: https://humanitarians.ai
Musinique: https://musinique.com
Medhavy AI: https://medhavy.com

TAGS: Gavia, Vegnet, invasive species, invasive plants, purple loosestrife, common reed, Phragmites, water chestnut, yellow flag iris, native plants, fireweed, object detection, YOLO, mean average precision, iNaturalist, conservation technology, offline AI, Humanitarians AI, weekly progress, Computational Skepticism

#AI #ComputerVision #InvasiveSpecies #Conservation #Plants #OpenSource #HumanitariansAI #WeeklyUpdate
