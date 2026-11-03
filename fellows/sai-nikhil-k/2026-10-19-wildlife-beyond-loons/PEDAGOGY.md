# PEDAGOGY — Seals Pass, Seabirds Wait

**Reel** `weekly_updates/2026-10-19-wildlife-beyond-loons/` · **slug** `claude-sai-seals-pass-seabirds-wait`
**Subject** which animal the next Gavia should count · **week of** 2026-10-19 (first reel)
**Host** Sai, in his own name · **Voice** Kokoro `am_onyx`, free and local
**Chassis** Remotion + two photo plates (7 freely licensed photographs), no Manim, nothing paid

---

## The ONE idea

> The next Gavia is picked by four questions (demand, data, gap, fit), not by
> which animal is most charismatic. Seals pass all four today. Maine's coastal
> seabirds pass three and wait on one request: their labels are public, their
> images aren't.

Built from this folder's `research/` notes (2026-10-19/20). On 2026-10-25 Sai
was offered this angle and said "build it", then asked for it to be finished
overnight. **Title changed from the one offered.** I proposed "Most Species Fail
the Data Question", but nothing measured supports "most": of the four candidates
the reel treats, two fail on data (bird song, Maine seabirds) and one fails on
gap (camera traps). "Seals Pass, Seabirds Wait" says only what was checked.
Sai can rename it; the title appears in B00's `segment`, the verdict card,
B10's narration and the slug.

## Act structure

| Beat | Act | Pattern | Why |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Cold open: what Gavia is, and the week's question. |
| B01 | FOUR QUESTIONS | `ClaudeScienceChipGrid` | The four questions as six chips (data and fit each have two parts, as narrated). |
| B02 | WHERE NOT TO BUILD | `BinaryBranch` | Camera traps fail gap; bird song fails data (NC weights vs AGPL). |
| B03 | WHAT DEMAND LOOKS LIKE | `TypesetMath` | Houston Audubon's SeeBird: 19% of the time → 81% ≈ their 80%; 89% of birds, so a person still checks. |
| B04 | MAINE'S SEABIRDS | photo plate · 4 photos | 268 islands, three observers, 99.0% agreement — demand and fit. |
| B05 | THE DATA QUESTION, MEASURED | `ExecutedData` | Both releases counted: 97,272 labels / 0 images vs 14,311 seals / 44,185 images. |
| B06 | SEALS PASS | photo plate · 3 photos | NOAA counts seals from photos; open data; no offline app found; fits. |
| B07 | THE RANKING | `DivergentFates` | Same four questions, split at data: build now vs request images. |
| B08 | VERDICT | `ClaudeVerdictArtifact` | One page. |
| B09 | HANDOFF | `ClaudeComposerAsk` | Run the four questions on an animal you care about. |
| B10 | OUTRO | `LogoOutro` | `@HumanitariansAI`. |

## ILLUSTRATE LAW check

Claude UI at B00, B09 and the verdict only. Body beats:

`ChipGrid → BinaryBranch → TypesetMath → photos → ExecutedData → photos → DivergentFates`

No two consecutive body beats share a pattern. Every beat has an ordered `show`
block. Each photo fades in when the narration names it, over a slow 2% push.

## 9:16

Every Remotion pattern has a registered `*916` sibling. The two photo beats have
re-composed portrait plates at `pantry/<B>-916.mp4` (rows of photo + caption).
No positional words in the narration.

## Evidence and honesty

- **Measured here:** `evidence/maine_labels.py` (97,272 bird points on 224
  islands, 0 image files in the release, 99.0% species agreement among birds seen
  by 2+ observers, species shares) and `evidence/seal_labels.py` (14,311 seals;
  28,399 boxes across colour + thermal; 44,185 colour images; 80% ringed seals).
- **Quoted, re-fetched 2026-10-25:** USGS release metadata (268 islands, "Three
  observers reviewed the images…"), LILA seal page (CDLA-Permissive), NOAA InPort
  24457 ("counted from the digital photographs"), Audubon SeeBird article (19%,
  80%, 89%, "took weeks"), BirdNET README (models CC BY-NC-SA 4.0), SpeciesNet and
  MegaDetector READMEs (AddaxAI runs them on your computer), AddaxAI repo ("Free,
  open source, for Windows, macOS and Linux"), Gavia README (AGPL-3.0, offline,
  "Every result is meant to be reviewed by a person").
- **"No offline app found" is a search result, not a proof**, and is worded that
  way on screen and in the narration.
- **Dropped because it couldn't be re-checked tonight:** the CDFW harbor-seal
  "dissecting microscope" quote (page down for maintenance), the brant/USFWS YOLO
  workflow, river herring, Lyons/Hayes/Chabot drone-count figures. See SOURCES.md.
- **The "Counting Dots" photo is South Dakota, not Maine** (pelicans and
  cormorants, USFWS). Its credit line says so; its caption says only "what
  observers count".
- **LILA says "around 80,000" images; the file list has 88,228** (44,185 colour
  + 44,043 thermal). The reel shows only the measured colour count.

## Attribution

Hosted by Sai in his own name. Named on screen: Houston Audubon and Rice
University (SeeBird), USGS, NOAA, and the photographers in each credit line.
Research notes were assembled by Claude on 2026-10-19/20; no collaborator
commits are involved.

## Pronunciation (narration only; the screen keeps the real names)

- `2019` → "twenty nineteen"
- `BirdNET` → "Bird Net" (raw: "bird N-E-T")
- `NOAA's` → "the NOAA" (raw drops the 's)

## Expected build noise (not bugs)

- SKIN LINT at B10 asking for `ClaudeTitleOutro` — wrong for this channel.
- The portrait slate reports edge-bleed on every frame (its own burn-in).
  Trust `./art final`'s gate on the clean candidate.
- **Do not edit `beat_sheet.json` while `remotion_scenes.py` is running.**

---

## Human review checklist

Nothing below has been done by the assistant.

- [ ] Title: keep "Seals Pass, Seabirds Wait", or rename?
- [ ] Is "the next Gavia" framing right for a public video — is this a plan or just a ranking?
- [ ] B02: fair to BirdNET and to the camera-trap tools?
- [ ] B05/B07: OK to say the Maine imagery has to be requested from the release's contact?
- [ ] Photos: is the South Dakota "Counting Dots" photo OK on a Maine beat, given its credit?
- [ ] Is anything here better left out of a public video?

---

## Full narration, as it will be spoken

<!-- NARRATION:BEGIN (generated from beat_sheet.json) -->

### B00 · ASK — `ClaudeComposerAsk` · 12.6s measured (39 words)

> Gavia finds loons in photos, on your own computer, and a person checks every
> box. This is Sai. This week's question: which animal should get the next
> Gavia? Not the most charismatic one. The one that passes four questions.

### B01 · FOUR QUESTIONS — `ClaudeScienceChipGrid` · 16.6s measured (59 words)

> Here are the four. Demand: is someone counting this animal by hand today, on
> the record? Data: is there a labelled set we're allowed to train on, and then
> ship the weights from? Gap: is there no installable, offline app for it yet?
> And fit: still photos or drone frames, turned into boxes or points, the way
> Gavia works.

### B02 · WHERE NOT TO BUILD — `BinaryBranch` · 21.7s measured (64 words)

> Two big areas drop out first. Camera traps fail the gap question:
> MegaDetector, Google's SpeciesNet and the free AddaxAI app already run on your
> own computer. Bird song fails on data: Bird Net is excellent, but its models
> are licensed non-commercial, and Gavia's AGPL license can't carry that.
> Gavia's niche is narrower: one kind of animal in photos, counted offline,
> checked by a person.

### B03 · WHAT DEMAND LOOKS LIKE — `TypesetMath` · 19.6s measured (67 words)

> Demand looks like this. On the Texas coast, Houston Audubon flew a drone over
> waterbird colonies, and going through the imagery took weeks. With computer
> help it took about nineteen percent of the time. One minus point one nine is
> point eight one: their eighty percent cut. And the computer found eighty-nine
> percent of the birds a biologist found, so a person still checks. That's
> Gavia's shape.

### B04 · MAINE'S SEABIRDS — `photo plate · grid2x2` · 19.1s measured (60 words)

> Now Maine's coastal islands. In twenty nineteen a survey plane photographed
> two hundred sixty-eight islands, and three observers went through the images,
> bird by bird: herring gulls, eiders, cormorants. When two or more looked at
> the same bird, they agreed on its species ninety-nine percent of the time.
> That's demand, on the record, and photos into points is Gavia's fit.

### B05 · THE DATA QUESTION, MEASURED — `ExecutedData` · 18.9s measured (51 words)

> The data question, measured. We downloaded both releases and counted. Maine:
> ninety-seven thousand two hundred seventy-two birds labelled, and zero images.
> The NOAA Arctic seals: fourteen thousand three hundred eleven seals boxed, on
> forty-four thousand colour images, under a permissive licence. Points without
> the photos under them can't train a detector.

### B06 · SEALS PASS — `photo plate · hero+2` · 20.2s measured (67 words)

> Seals pass all four. Demand: on Alaska's Iliamna Lake, NOAA photographed every
> harbor seal it saw from a plane, then counted them from the photos. Data: open
> and permissive, as we just measured, and mostly ringed seals. Gap: we found no
> installable offline app that counts seals in photos. Fit: seals hauled out on
> rocks or ice, seen from above, are boxes on a photo, like loons.

### B07 · THE RANKING — `DivergentFates` · 13.7s measured (46 words)

> So the ranking falls out of the questions. Seals: build now, on open data.
> Maine's seabirds: one step first. The labels are public and the photos aren't,
> but the release names a contact. So the next step there is a request for the
> imagery, not code.

### B08 · VERDICT — `ClaudeVerdictArtifact` · 12.1s measured (37 words)

> So, the next Gavia: picked by four questions, not by charisma. Seals pass all
> four today. Maine's seabirds wait on one request for images. Camera traps and
> bird song are already served, so we leave them alone.

### B09 · HANDOFF — `ClaudeComposerAsk` · 15.4s measured (53 words)

> Your turn. Pick an animal you care about and run the four questions with an
> assistant: who counts it by hand today, is there a labelled set whose licence
> lets you ship weights, does an offline tool already exist, and do photos fit?
> Then open the licence page yourself and check its answer.

### B10 · OUTRO — `LogoOutro` · 2.9s measured (5 words)

> Seals pass, seabirds wait. Sai.

**Total: 548 words** → 172.8s measured (2:52). Audio remains the master clock.

<!-- NARRATION:END -->

---

VERDICT: __________     — reviewer: ______________  date: __________
