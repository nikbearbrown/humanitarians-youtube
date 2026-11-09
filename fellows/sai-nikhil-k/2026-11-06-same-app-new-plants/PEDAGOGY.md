# PEDAGOGY — Same App, New Plants

**Reel** `weekly_updates/2026-11-06-same-app-new-plants/` · **slug** `claude-sai-same-app-new-plants`
**Subject** Gavia 0.5.0's Vegnet and Model menu (invasive plant detection) · **week of** 2026-11-06 (built 2026-11-09, backlog)
**Host** Sai, in his own name · **Voice** Kokoro `am_onyx`, free and local
**Chassis** Remotion + three image plates (real Gavia 0.5.0 screenshots, 4 iNaturalist photos), no Manim, nothing paid

---

## The ONE idea

> The same offline app now looks for invasive lake plants as well as loons: a
> Model menu, and Vegnet naming four species. Its mean AP of 0.72 is a spread
> (0.96 water chestnut, 0.54 purple loosestrife), and because every photo it
> trained on held an invasive, it boxed 25 of 40 native look-alikes.

Sai's brief (2026-11-09): two backlog videos, one feature each; this one is
November 6, "Invasive vegetation detection". His repo link is the content. He
picked the angle "Same App, New Plants" (continuity with 10-23's model slot,
mean AP as a spread, a native look-alike test) and "nothing to leave out".

## Act structure

| Beat | Act | Pattern | Why |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Last week Gavia listened; this week a new subject. How good, and does it know a native? |
| B01 | THE MODEL MENU | image plate · 3 screenshots | Loosestrife boxed and named (97%); the Model menu; the 10-23 model slot, second model in it. |
| B02 | WHAT 0.72 MEANS | `TypesetMath` | IoU ≥ 0.5 is a hit; mAP = mean of four APs; (0.959 + 0.796 + 0.587 + 0.536)/4 ≈ 0.720. |
| B03 | FOUR INVADERS | image plate · 4 photos | The four species with their APs; 26 training + 7 val photos each; drafted, reviewed boxes. |
| B04 | NATIVE LOOK-ALIKES | `ExecutedData` | Gavia's detector: 25/28 invasive val photos boxed; 25/40 natives; reed 5/8; watershield 7/8. |
| B05 | CALLED INVASIVE | image plate · 3 screenshots | In the app: fireweed → loosestrife 97%, watershield → water chestnut 95%, American reed → common reed 98%. |
| B06 | STILL TO DO | `ClaudeScienceChipGrid` | The roadmap's own fixes: hand-checked boxes, more photos, natives, submerged species, GPS/date, export. |
| B07 | VERDICT | `ClaudeVerdictArtifact` | One page. |
| B08 | HANDOFF | `ClaudeComposerAsk` | Pick an invasive near you; ask which natives are mistaken for it; check on iNaturalist. |
| B09 | OUTRO | `LogoOutro` | `@HumanitariansAI`. |

## ILLUSTRATE LAW check

Claude UI at B00, B08 and the verdict only. Body beats:
`images → TypesetMath → images → ExecutedData → images → ChipGrid`.
No repeats; every beat has an ordered `show` block.

## 9:16

Every Remotion pattern has a `*916` sibling; the three image plates have
re-composed portrait plates in `pantry/`. Portrait-only edits: none planned.

## Evidence and honesty

- **Executed locally, Gavia's own evaluator:** `evaluate_vegnet.out` — Gavia's
  `examples/evaluate.rs` at tag v0.5.0 (`5dd8471`), veg_v1.onnx sha256
  `677b3955…`, on loonet's vegnet_v1 val split (28 photos, 32 stands): AP@0.5
  water chestnut 0.9594, common reed 0.7959, yellow flag iris 0.5868, purple
  loosestrife 0.5361, mean 0.7195. Matches the README's 0.720. `plants` tests 5/5.
- **Executed locally, look-alikes:** `lookalike_fetch.py` takes a fixed sample
  (North America, research grade, CC0/BY/BY-SA, newest below a fixed id, first
  8 per taxon) of five natives: fireweed, blue vervain, American reed
  (*Phragmites australis americanus*), blue flag iris, watershield.
  `lookalike_check.rs` runs Gavia's `Detector` with veg_v1 at the app defaults
  (0.25, no tiling): 25 of 40 got at least one box. Per taxon: fireweed 5/8,
  blue vervain 4/8, American reed 5/8, blue flag iris 4/8, watershield 7/8. Its
  own val photos: 25/28. The sample was not filtered after looking (it includes
  seed heads and leaf-only shots).
- **"Never learned what native looks like"**: all 132 vegnet_v1 photos (104
  train, 28 val) have at least one labelled box, and all are of the four
  invasives — counted from the label files, not assumed.
- **Screenshots are real:** Gavia 0.5.0 from /Applications with `GAVIA_DATA_DIR`
  set to a scratch folder, driven by accessibility + synthetic mouse, captured
  with `screencapture -R`. App results equal the evidence run (0.97, 0.95, 0.98).
  Two small panels and the Settings row are cropped (sidecars say how).
- **The American reed caveat:** native and introduced *Phragmites* are hard to
  tell apart even for people, and an iNaturalist subspecies ID can be wrong. The
  reel counts them as natives because research-grade IDs say so; fireweed and
  watershield carry the point on their own.
- **Not used on screen:** the model card's 0.798 (Ultralytics, recorded in the
  checkpoint) and loonet's README 0.77 / Gavia commit's 0.731 (Ultralytics' square
  pipeline) — the same weights through different evaluators. The reel uses
  Gavia's own 0.720, the number for what the app does. Logged in SOURCES.

## QC changes made after the first render (2026-11-09)

- **Data beat → table mode.** In `mode: "probability"`, four bar rows pushed the
  provenance note below the frame (GATE V: edge-bleed at 50% and 85%). The beat
  now shows the same counts as a table, and the note is on screen.
- **`qc.sparse` declared on B06 (ChipGrid) and B07 (verdict)**, with the reason in the sheet: B06 at the 50% sample lights 4 of 6 chips (portrait 29%); B07 is a centred card at 35%.
  Looked at the frames first; the 85% frames are full. Carried in `build_beats.py`,
  so `shorts.py --vertical` copies it on a re-derive.
- **B02's middle equation** was flattened from ¼·Σ to one fraction (it typeset at the 2% floor).

## Continuity

- 10-23 ("Same App, New Animal") said each new subject needs its own model file
  and showed the Detection model slot in Settings. B01 says this is that slot with
  a second model in it; B05 recalls the eider the loon model called two loons.
- 10-30 ("Every Three Seconds") is "last week, Gavia learned to listen" in B00.

## Attribution

Hosted by Sai; Gavia and loonet are his projects. Every commit in the window
(`e329602`, `4ac6248`) is Sai's. Photos credited per panel (iNaturalist, CC0 /
CC BY / CC BY-SA).

## Pronunciation (narration only)

- `Vegnet` → "Veg Net" · `Loonet` → "Loon Net" · `Phragmites` → "frag-MY-teez".

## Expected build noise (not bugs)

- SKIN LINT at B09 asking for `ClaudeTitleOutro` — wrong for this channel.
- The portrait slate reports edge-bleed on every frame (its own burn-in).

---

## Human review checklist

Nothing below has been done by the assistant.

- [ ] Is "25 of 40 native look-alikes boxed" fair to show in public for Vegnet 1.0?
- [ ] OK to count American reed as native on iNaturalist's research-grade IDs?
- [ ] B06: is the roadmap list the plan you want to commit to on camera?
- [ ] Anything here better left out of a public video?

---

## Full narration, as it will be spoken

<!-- NARRATION:BEGIN (generated from beat_sheet.json) -->

### B00 · ASK — `ClaudeComposerAsk` · 12.4s measured (46 words)

> Last week, Gavia learned to listen. This is Sai. This week, it learned a new
> subject: Veg Net, a model for four invasive lake plants. How good is it? And
> does it know a native plant when it sees one? We showed it forty of them.

### B01 · THE MODEL MENU — `image plate · hero+2` · 17.9s measured (60 words)

> Here's the change, on a stand of purple loosestrife: the box names the
> species, at ninety-seven percent. Check an image now has a Model menu. Loon
> Net looks for loons. Veg Net looks for purple loosestrife, common reed, water
> chestnut and yellow flag iris. It's the model slot we pointed to two weeks
> ago, with a second model in it.

### B02 · WHAT 0.72 MEANS — `TypesetMath` · 19.5s measured (63 words)

> Veg Net's headline number is a mean average precision of zero point seven two.
> A box counts as a hit when its intersection over union with the reviewed box
> is at least one half. Each species gets an average precision, and the four are
> averaged. Water chestnut scores zero point nine six. Purple loosestrife, zero
> point five four. One mean, a wide spread.

### B03 · FOUR INVADERS — `image plate · four` · 17.8s measured (51 words)

> Meet the four. Water chestnut, with its floating rosettes. Common reed, the
> introduced frag-MY-teez. Yellow flag iris. And purple loosestrife, with its
> magenta spikes, the one Veg Net finds hardest. Each was trained on twenty-six
> photos and checked on seven, with boxes drafted by another model and reviewed
> by a person.

### B04 · NATIVE LOOK-ALIKES — `ExecutedData` · 18.6s measured (58 words)

> So we asked it about natives. On its own invasive photos, Veg Net draws a box
> on twenty-five of twenty-eight. On forty iNaturalist photos of native look-
> alikes, it boxed twenty-five. Five of eight native American reeds. Seven of
> eight watershields. The rest were fireweed, blue vervain and blue flag iris,
> and not one of the forty is invasive.

### B05 · CALLED INVASIVE — `image plate · hero+2` · 19.7s measured (61 words)

> In the app, it looks like this. Native fireweed: purple loosestrife, ninety-
> seven percent. Native watershield: water chestnut, ninety-five. Native
> American reed: common reed, ninety-eight. It's the eider from two weeks ago,
> the one the loon model called two loons. Every one of Veg Net's hundred and
> thirty-two photos had an invasive in it, so it never learned what native looks
> like.

### B06 · STILL TO DO — `ClaudeScienceChipGrid` · 19.0s measured (57 words)

> Gavia's own roadmap already names the fixes. Boxes checked by hand, not
> drafted. Many more photos per species. Native look-alikes in the training set,
> so the model learns what no looks like. Submerged invaders, like Eurasian
> watermilfoil. And the place and date of each photo, exported for mapping.
> Twenty-five of forty is now the number to beat.

### B07 · VERDICT — `ClaudeVerdictArtifact` · 15.1s measured (48 words)

> So: the same offline app now looks for invasive plants as well as loons. Veg
> Net finds water chestnut well and purple loosestrife poorly, and it boxed
> twenty-five of forty native look-alikes. Until it has seen natives, treat each
> box as a lead for someone who knows plants.

### B08 · HANDOFF — `ClaudeComposerAsk` · 12.6s measured (41 words)

> Your turn. Pick an invasive plant near you, and ask an assistant which native
> plants get mistaken for it, and what tells them apart in a photo. Then find
> one of each on iNaturalist, and check every answer against the pictures.

### B09 · OUTRO — `LogoOutro` · 2.5s measured (5 words)

> Same app, new plants. Sai.

**Total: 490 words** → 155.1s measured (2:35). Audio remains the master clock.

<!-- NARRATION:END -->

---

VERDICT: PASS  — reviewer: SAI NIKHIL KUNAPAREDDY  date: 11/09/2026
