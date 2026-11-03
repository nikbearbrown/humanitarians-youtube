# SOURCES — Every Box, Checked

Loon-detector weekly progress reel, week of **2026-09-04**.
Slug `claude-sai-every-box-checked`.

---

## 1. Where the content came from

| Source | What it supplied | How it is used |
|---|---|---|
| **The author (Sai), directly** | The whole week: annotation is complete on every image he quality-checked last week; about 136 images are now ready to be trained on the latest YOLO vision model. | The entire spoken content of B00–B07. |
| **`val_batch0_labels.jpg`** (author's own, supplied with the request) | A 1920×1280 YOLO label mosaic — a 4×4 sheet of 480×320 cells, each an annotated frame with `common loon` boxes drawn on. | B02, as two composed plates. Staged unmodified to `images/B02-source.jpg`. |

**No external links, papers, datasets or repos are cited in this reel**, because
none were supplied. Nothing on screen is attributed to a third party.

---

## 2. The one inference this reel makes from the image

The author did not say where the images came from. The reel states three
capture paths — **web stills, a Nikon shot from shore, and drone frames over
open water** — on B01, in B05's verdict, and in the B00 result lines.

That claim is **read off the filename prefixes visible in the supplied mosaic**:

- `web_20260818_*` — 11 of the 16 visible cells
- `nikon_20260822_*` — 3 of the 16 visible cells
- `dji_20260822_*` — 1 of the 16 visible cells (`dji` is DJI, the drone maker;
  the cell is a near-vertical view of open water, consistent with aerial capture)

The prefixes are legible on both plates, so the claim is **shown, not just
asserted** — a viewer can check it against the frame. It is nonetheless an
inference about provenance from a naming convention, and it is the only
inference in the reel. **If the prefixes do not mean what they appear to mean,
B01, B05 and B00's third result line are the three places to correct.**

The reel does **not** infer per-source counts from those cells. Sixteen cells
is what one mosaic page shows, not a census of ~136 images, so no "11 web, 3
Nikon, 1 drone" split appears anywhere.

---

## 3. Honesty log — what was deliberately NOT put on screen

Per the **DOUBLE-CHECK LAW**. The only figure the author supplied is *about 136
images*. Everything below was available as a plausible-sounding number and was
left out because he did not supply it:

| Not shown | Why |
|---|---|
| mAP, precision, recall, any accuracy figure | No training run has happened. There is nothing to report. |
| Epochs, image size, batch size, learning rate | Not supplied, and not knowable from a label mosaic. |
| Train/val split ratio | The filename `val_batch0_labels.jpg` implies a validation split was defined, but the author never stated a ratio. The reel says the labels are "read back the way the trainer sees it" and asserts no split. |
| A YOLO version number | He said "the latest YOLO vision model" and did not name a release. Screen and voice say **"the latest YOLO"** everywhere. Never v8/v11/v12. |
| Total instance/box count | Not supplied. Several cells hold more than one box, so it is not ~136 either. |
| Annotation hours, images-per-hour | Not supplied. |
| Class count beyond the one visible class | Only `common loon` appears on the plate. The reel says "one class" and does not claim the project will only ever have one. |
| How many images failed quality control | Not supplied. The reel says the check ran first and that nothing was labelled that would be thrown away; it never says how much was discarded. |

**`about 136`.** The author's qualifier was "about one thirty six". It is spoken
as *"about a hundred and thirty-six"* in all four beats that mention it. The
bare string `136` appears only on B04's `slideMeta` — where the beat's whole
subject is the size of the set — and in B01/B05 prose that carries "About"
alongside it.

**Nothing has been trained.** He said the set is *ready to be* trained. B05 and
B07 say so explicitly, which is also consistent with week one's reel.

---

## 4. Two things on the plate that are NOT data errors

Recorded here so that neither is ever read as one, by a viewer or by a later
build:

1. **`corcommon loon` on the drone cell.** This is two `common loon` box
   captions overlapping in the mosaic plot — the two specks are close together
   and their labels collide. It is a **plotting artifact of the label
   visualiser**, not a mislabelled or misspelled instance. No beat mentions it.
2. **Truncated filenames and a clipped caption tail.** The mosaic draws
   per-cell filenames and box captions without clipping, so the long `nikon_*`
   names overflow their cell to the right. On the 16:9 plate this shows as
   crowding between columns; on the 9:16 re-tile the cells were chosen so that
   no cell inherits an *orphan* fragment from its left neighbour, and the only
   remaining artifact is one cell truncating its own `.jpg` tail. See
   `make_plates.py` for the selection rule.

---

## 5. Claims that are the voice's argument, not the author's report

Flagged so a reviewer can strike them if they overreach:

- **B04's fork — "train now, or keep annotating?"** The author did not describe
  making this decision. He said the set is ready to train. The fork, both
  branches and the resolver ("the first run tests the plumbing, not the
  detector") are **editorial** — the reel's argument about what to do at this
  size, not a report of a choice he made.
- **B03's "the far frames are where it actually gets judged."** An argument
  about small-object detection, made from the visible scale range on the plate.
  No benchmark is cited and no failure rate is claimed.
- **B01/B05's "nothing was labelled that was going to be thrown away."** This
  is the reel's reading of the *order* he described — quality check last week,
  annotation this week. He did not phrase it as a strategy.
- **B06's handoff** (sort your boxes by area; compare the smallest tenth to the
  largest) is advice the reel gives the viewer, not something the author reported
  doing.

---

## 6. Corrections

None yet. If the capture-path inference in §2 is wrong, correct B01's chip grid,
B05's third artifact line, and B00's third result line together — they carry the
same claim.
