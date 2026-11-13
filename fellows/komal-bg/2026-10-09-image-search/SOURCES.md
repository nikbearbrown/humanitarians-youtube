# SOURCES.md — The Query That Looks.

Internal research for the cut. **Not spoken or shown** unless the beat claims it.
DOUBLE-CHECK LAW: rewritten in Teardown. No rotting metrics (no MAU, no “X million
items indexed,” no conversion lift).

## Three machines (definitional, B02)

- **Caption / VLM:** describes a photo in words. No catalog retrieval required.
- **Classifier:** assigns a label (species, category, “this is a bag”). A name
  is not a neighbor.
- **Image search:** the image *is* the query. The system retrieves ranked
  matches from an index (visual embeddings / local features). If it cannot
  retrieve, the film treats it as still a caption or a classifier.

## Rails (B03 / B05)

- **Google Lens.** Announced Google I/O, 17 May 2017: camera understands what
  it sees and can take action; “search what you see.” Consumer rail. Not a
  luxury-house campaign.
  https://blog.google/products-and-platforms/devices/google-lens/google-lens-one-year/
  https://techcrunch.com/2017/05/17/google-lens-will-let-smartphone-cameras-understand-what-they-see-and-take-action/
- **Farfetch visual search.** 11 Dec 2018: Farfetch iOS “See it, Snap it, Shop
  it” using Syte visual search — upload/snap a look, retrieve similar luxury
  catalog items. Luxury marketplace, not a named maison first-party campaign.
  https://www.retaildive.com/news/farfetch-taps-syte-for-visual-search-feature/544053/
- **Posh Lens.** Poshmark, 19 Jul 2023 (Canada Apr 2024): snap or upload a
  look, browse matching or similar *resale* listings (apparel, shoes, bags).
  Circular-fashion retrieval, not a new-SKU factory.
  https://blog.poshmark.com/2023/07/19/introducing-posh-lens/
- **Wildbook (Wild Me).** Open-source wildlife platform: detect animals in
  photos, apply species labels, **suggest matching individuals from the
  database**. Photo-ID / mark-recapture. Human reviews matches — Wildbook
  docs: it assists photo ID and does not decide for you.
  https://www.wildme.org/wildbook.html
  https://wildbook.docs.wildme.org/data/matching-process.html
- **HotSpotter** (Crall / Princeton): query image ranked against a labeled
  animal database by local “hotspot” features. Algorithm inside Wildbook-class
  pipelines. Adjacent; not named on film.
  https://oar.princeton.edu/bitstream/88435/pr1dz29/1/AM_HotSpotter_Patterned_Species_Instance_Recognition.pdf
- **Flukebook:** Wildbook instance for whales and dolphins; same retrieval
  (fluke/fin as query). Encounter counts are rotting — not spoken.

## Fields (interpretation, B04)

- **Luxury:** catalog retrieval from a street or editorial photo. If a photo
  can retrieve the SKU, the closed door is a match list. Visual search finds
  *similar*; it does not authenticate. Entrupy-class microscopic authentication
  is a different machine (classify authentic/unidentified) — not claimed as
  image search, not named on film.
- **Conservation:** individual re-ID. The index is lives, not SKUs.
- **Animal welfare:** lost-pet matching is the same query (lost photo against
  found listings). Method exists (e.g. PetsRS 2024 flood dataset as academic
  retrieval). No consumer app is named as having “transformed” welfare.
- **Sustainability / circular resale:** Posh Lens as sourced second-hand
  retrieval. Finding a used match is the circular claim — not a carbon number.

## What this reel does not claim

- No maison named as first to ship visual search.
- No Lens/Poshmark user counts or “100 million items.”
- No claim that Wildbook IDs animals unsupervised.
- No claim that visual search authenticates luxury goods.
- No TRAFFIC reverse-image-search program as a numbered receipt (their public
  surveys are largely keyword-based; reverse image search is recommended OSINT,
  not claimed here as TRAFFIC’s method).
