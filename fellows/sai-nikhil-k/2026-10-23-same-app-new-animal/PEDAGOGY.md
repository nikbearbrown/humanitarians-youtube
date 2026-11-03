# PEDAGOGY — Same App, New Animal

**Reel** `weekly_updates/2026-10-23-same-app-new-animal/` · **slug** `claude-sai-same-app-new-animal`
**Subject** extending Gavia beyond loons · **week of** 2026-10-23
**Host** Sai, in his own name · **Voice** Kokoro `am_onyx`, free and local
**Chassis** Remotion + four image plates (6 real Gavia screenshots, a NOAA survey frame, 3 Commons photos), no Manim, nothing paid

---

## The ONE idea

> Gavia doesn't need a rewrite to count other animals. Its loon model can't see
> seals and calls an eider two loons; what it needs is a model per animal,
> tiling for aerial photos, and counts you can export. The offline,
> review-first app stays the same.

Sai's brief (2026-10-26): a video about extending Gavia to other wildlife, using
images from the app itself and of the other animals. He approved the extension
plan and the concept ("go") and gave the screen for the app captures.

## Act structure

| Beat | Act | Pattern | Why |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Cold open: "is this a loon?" → what about seals and Maine's seabirds? |
| B01 | GAVIA TODAY | image plate · 3 screenshots | The real app: result (1 loon, 88%), home, saved history. |
| B02 | THE LOON MODEL ON SEALS | `ExecutedData` | Gavia's own detector code on 20 random NOAA frames: 57 seals, 0 found; 4 / 86 "loon" boxes. |
| B03 | ASKED ABOUT OTHER ANIMALS | image plate · 2 screenshots | In the app: seals → "No loon detected"; a Maine eider → "2 loons, 85%". |
| B04 | WHY AERIAL ANIMALS VANISH | `TypesetMath` | s × 640 / L: a 64 px seal is ~6 px on a whole frame, ~43 px in a tile. |
| B05 | ONE FRAME, TWO WAYS | image plate · NOAA frame + tile | The whole frame shows nothing; one tile shows seven seals (NOAA's boxes). |
| B06 | WHAT TO BUILD | `ClaudeScienceChipGrid` | Six pieces: seal model, per-model tiling, folder counts, CSV, fixes as labels, accuracy in-app. |
| B07 | WHO'S NEXT | image plate · settings row + 3 photos | The model slot exists; harbor seals, ringed seals, then Maine's seabirds. |
| B08 | VERDICT | `ClaudeVerdictArtifact` | One page. |
| B09 | HANDOFF | `ClaudeComposerAsk` | Run three checks on an animal near you. |
| B10 | OUTRO | `LogoOutro` | `@HumanitariansAI`. |

## ILLUSTRATE LAW check

Claude UI at B00, B09 and the verdict only. Body beats:
`images → ExecutedData → images → TypesetMath → images → ChipGrid → images`.
No repeats; every beat has an ordered `show` block.

## 9:16

Every Remotion pattern has a `*916` sibling; the four image plates have
re-composed portrait plates in `pantry/`.

## Evidence and honesty

- **Executed locally, Gavia's own code:** `evidence/seal_check.rs` (a companion to
  Gavia's `examples/evaluate.rs`, same `Detector`, built at tag v0.3.1, 760e465,
  weights sha256 172fa54f…) on `evidence/seal_split.py`'s sample: 20 NOAA frames
  drawn at random (seed 20261026), 57 seals. At the app's 0.25 threshold: 0 seals
  found whole or tiled; 4 "loon" boxes whole, 86 tiled. Gavia's own
  `evaluate` agrees (P = R = AP = 0 both ways).
- **Executed locally, scale:** `evidence/seal_scale.py` replicates Gavia's
  `plan_tiles` (checked against v0.3.1's `preprocess.rs`): 54 tiles of 960 px on
  a 6576 × 4384 frame; median seal 64 px → 6.2 px whole, 42.7 px per tile.
- **Screenshots are real:** Gavia 0.3.1 from /Applications, launched with
  `GAVIA_DATA_DIR` pointing at a scratch folder (Sai's own history untouched),
  driven by accessibility + synthetic mouse, captured with `screencapture -R`.
  The eider "2 loons" and seals "No loon detected" results are what the app
  actually returned. The Settings screenshot is cropped to the Detection model
  row (the full screen showed a scratch file path).
- **The NOAA tile's orange boxes are NOAA's own labels**, not a model's output;
  the caption says so.
- **Nothing here is a seal model.** No model was trained; the reel shows what the
  current app does and what would have to be built.
- **"Tiling hurts close-up loon photos"** is from Gavia's README (v0.3.1):
  precision 0.906 → 0.074 on loonnet_v1 with tiling on.

## Attribution

Hosted by Sai; Gavia is his project. Photos credited per panel.

## Pronunciation (narration only)

- `NOAA's` → "the NOAA …" (raw drops the 's).

## Expected build noise (not bugs)

- SKIN LINT at B10 asking for `ClaudeTitleOutro` — wrong for this channel.
- The portrait slate reports edge-bleed on every frame (its own burn-in).

---

## Human review checklist

Nothing below has been done by the assistant.

- [ ] Is the extension plan (B06) the one you want to commit to in public?
- [ ] OK to show the eider "2 loons" result — an honest failure of the current model?
- [ ] B07: is "Maine's seabirds, once the survey photos are shared" fair to USGS?
- [ ] Anything here better left out of a public video?

---

## Full narration, as it will be spoken

<!-- NARRATION:BEGIN (generated from beat_sheet.json) -->

### B00 · ASK — `ClaudeComposerAsk` · 10.7s measured (41 words)

> Gavia asks one question about a photo: is this a loon? This is Sai. This week,
> a harder one: what would it take for the same app to count seals, or Maine's
> seabirds? We ran it on them to find out.

### B01 · GAVIA TODAY — `image plate · hero+2` · 14.3s measured (49 words)

> Here's Gavia today, running on this Mac. Open a photo and it asks: is this a
> loon? It boxes every loon it finds with a confidence score, here eighty-eight
> percent, and a person keeps the result or throws it out. Everything stays on
> your computer, in your own history.

### B02 · THE LOON MODEL ON SEALS — `ExecutedData` · 15.5s measured (46 words)

> So we pointed Gavia's own detector code at seals: twenty random frames from
> the NOAA Arctic seal survey, fifty-seven seals in all. It found none. On whole
> photos it drew four boxes it called loons. With tiling switched on, eighty-
> six. More looking, same model, more mistakes.

### B03 · ASKED ABOUT OTHER ANIMALS — `image plate · pair` · 14.1s measured (51 words)

> In the app, it looks like this. A photo full of harbor seals: no loon
> detected. That's true, and no help if you're counting seals. A common eider
> from Maine: two loons, eighty-five percent. The model has only ever seen
> loons, so it has no way to say: not a loon.

### B04 · WHY AERIAL ANIMALS VANISH — `TypesetMath` · 19.3s measured (63 words)

> Tiling still matters, because of scale. Gavia's model looks at six hundred
> forty pixels at a time. A typical seal in these survey frames is sixty-four
> pixels across. Shrink the whole frame to fit, and the seal is about six
> pixels. Cut it into Gavia's tiles first, and it's about forty-three. Tiling
> makes the seal visible. Only a seal model can recognise it.

### B05 · ONE FRAME, TWO WAYS — `image plate · frame+tile` · 15.6s measured (50 words)

> Here's one of those frames. Whole, it's ice and shadow. Now one tile, the size
> Gavia would cut: seven seals, hauled out on the ice. The NOAA open set has
> fourteen thousand three hundred eleven seals boxed like this, under a licence
> that lets a trained model ship inside Gavia.

### B06 · WHAT TO BUILD — `ClaudeScienceChipGrid` · 17.6s measured (54 words)

> So here's the extension. One model file per animal, starting with seals,
> trained on the NOAA set. Tiling switched on by the model itself, because it
> hurts close-up loon photos. Counts per folder, exported as a spreadsheet. A
> reviewer's fixes kept as new training labels. And each model's measured
> accuracy, shown in the app.

### B07 · WHO'S NEXT — `image plate · band+3` · 16.0s measured (50 words)

> And the slot is already there. Gavia's settings show the detection model, and
> the app loads a retrained one dropped into its models folder. Seals first:
> harbor seals on New England rocks, ringed seals on Arctic ice. Then Maine's
> seabirds, once the survey photos behind their public labels are shared.

### B08 · VERDICT — `ClaudeVerdictArtifact` · 14.8s measured (47 words)

> So: Gavia doesn't need a rewrite to count other animals. On seals, the loon
> model finds nothing, and an eider becomes two loons. What it needs is a model
> per animal, tiling for aerial photos, and counts you can export. The offline,
> review-first app stays the same.

### B09 · HANDOFF — `ClaudeComposerAsk` · 15.3s measured (52 words)

> Your turn. Pick an animal near you and ask an assistant three things: is there
> a labelled photo set whose licence lets you ship a model, how big is the
> animal in a typical survey photo, and who counts it by hand today. Then open
> the dataset page and check every answer.

### B10 · OUTRO — `LogoOutro` · 2.5s measured (5 words)

> Same app, new animal. Sai.

**Total: 508 words** → 155.8s measured (2:35). Audio remains the master clock.

<!-- NARRATION:END -->

---

VERDICT: __________     — reviewer: ______________  date: __________
