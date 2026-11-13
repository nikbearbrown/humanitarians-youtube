# SOURCES.md — The Empty Frame.

Internal research for the cut. **Not spoken or shown** unless the beat claims it.
DOUBLE-CHECK LAW: rewritten in Teardown. No rotting org-counts. Distinct from
*The Query That Looks.* (image search / Wildbook individual ID).

## Three machines (definitional, B04)

- **Detect:** is there an animal, a person, a vehicle — or a blank. Bounding
  box + confidence. Not a species name.
- **Classify:** which species (or taxon). A second model, often on the crop.
- **Identify:** which individual. Photo-ID / mark-recapture. **Wildbook** —
  already *The Query That Looks.* Named as a different machine, not remade.

## Rails

- **MegaDetector.** Open-source detector from Microsoft AI for Good Lab.
  Animals, people, vehicles in camera-trap images. Not a species classifier.
  Typical deployments: most images empty (docs: 70–95% — spoken as “most”).
  A trained reviewer: a few hundred images per hour; a million-image set is
  weeks. Blank filtering can shrink the queue by about an order of magnitude.
  Always test on your own data. Laptop ~30–50k images/day; GPU higher — not
  spoken (hardware-rotting).
  https://github.com/microsoft/MegaDetector
  https://microsoft.github.io/MegaDetector/
  https://microsoft.github.io/MegaDetector/camera-trap-ai/
  https://megadetector.readthedocs.io/en/latest/userguide.html
- **Wildlife Insights / SpeciesNet.** Classifier rail (Google / WI). Ensemble
  with MegaDetector. SpeciesNet open-sourced; ~2,500 categories, 65M training
  images — **counts not spoken**. Adjacent; not the worked example.
  https://www.wildlifeinsights.org/about-wildlife-insights-ai
  https://github.com/google/cameratrapai
- **Wildbook.** Individual matching from a photo; a human confirms. Sibling
  reel only.

## Stills

- **B02 / B03.** Generated illustrations of an empty infrared trap frame and
  a review-queue contact sheet. Sidecars: `source: ai`. Not field captures.
- **B05.** U.S. Fish and Wildlife Service trail-camera photograph of a
  black-tailed deer, Sacramento River NWR, 7 Dec 2011. Public domain.
  Terracotta `animal 0.91` box is a teaching overlay, not MegaDetector output.
  https://commons.wikimedia.org/wiki/File:Black-tailed_deer_(7146688455).jpg

## What this reel does not claim

- That MegaDetector names species.
- A numbered “80 organizations” (docs say “more than 80” — rotting; omitted).
- A named conservatory adoption or accuracy on their data.
- That Loon Conservatory / Gavia is this detector.
- EarthRanger site counts (operations platform exists; not this week’s example).
