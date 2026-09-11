# FACTCHECK — What It Sees, And What It Misses

Every claim the reel makes, where it comes from, and how far it can be pushed.
Three tiers: **SUPPLIED** (the author said it), **ON THE PLATE** (the YOLO
plotter printed it into the supplied image, quotable verbatim), and **HAND
AUDIT** (Claude counted it off the sheets — not a model metric).

---

## SUPPLIED by the author

| Claim | Where it appears | Status |
|---|---|---|
| 106 images in the training set | B00 output, B01, B07 line 1 | SUPPLIED |
| ~26 images held out for validation, from the same repository | B00, B01, B07 | SUPPLIED — the reel says "twenty-six"; the sheets contain exactly 26 populated cells, so the author's "approximately 26" is confirmed by the plates |
| Training images include web-sourced and team-captured photographs | B01 narration ("pooled from the web and from our own cameras") | SUPPLIED |
| Blue boxes are detections; the adjacent number is confidence, 0 low to 1 high | B02 narration | SUPPLIED |
| The model sometimes detects the same loon more than once | B03, B04, B05, B07 | SUPPLIED, and independently visible |
| In one image a section of land was read as a loon | B04, B07 | SUPPLIED, and independently visible |
| A larger, more diverse training set should help | B05 branch "More images first" | SUPPLIED |
| No dedicated false-positive evaluation has been run yet | B05 ghostText, B07 line 4 | SUPPLIED |
| Precision / recall / accuracy are not yet available and come before the meeting | B07 line 4 | SUPPLIED |
| Proposed feature order, 7 items | B06 | SUPPLIED verbatim, in the author's order |
| Recommendation: keep CVAT, do not build an annotation tool | B06 | SUPPLIED |

---

## ON THE PLATE — printed by YOLO into the supplied mosaics

| Claim | Evidence | Status |
|---|---|---|
| Confidence values run 0.3 to 0.9 | Both sheets; lowest seen 0.3, highest 0.9 | VERIFIED — no value outside this range appears |
| Two classes were trained: `common loon` and `non loon` | `val_batch0_pred.jpg` r4c4 carries a `non loon0.8` label | VERIFIED — this is why B01 shows two class chips |
| A duck beside the reed bed is labelled `common loon0.3` | `val_batch0_pred.jpg` r4c4 | VERIFIED |
| The reed bed itself carries a detection box | `val_batch0_pred.jpg` r4c4, upper box | VERIFIED |
| One bird carries three overlapping boxes | `val_batch0_pred.jpg` r2c1 (`web_20260818_0042.jpg`) | VERIFIED |
| Two loons in fog returned no detection | `val_batch1_pred.jpg` r1c3 (`web_20260818_0076.jpg`) | VERIFIED — no box of any kind in that cell |
| Two distant birds in a drone frame were both detected, at 0.6 and 0.8 | `val_batch0_pred.jpg` r3c1 (`dji_20260822_143917_0141.jpg`) | VERIFIED |
| Four capture paths are present | filename prefixes `web_`, `nikon_`, `dji_`, `iphone_` | VERIFIED — this is an inference from filenames and is the only inference the reel draws from the images |

---

## HAND AUDIT — Claude's counts, labelled as such on screen

Performed by splitting both sheets into their 4×4 grids and reading every
populated cell. **These are not model metrics.** B07's fourth artifact line
states this on screen and must not be cut.

| Figure | Value | How it was obtained |
|---|---|---|
| Populated frames | 26 | 16 in `val_batch0_pred.jpg` + 10 in `val_batch1_pred.jpg`; the remaining 6 cells of sheet 1 are blank |
| Common loons visible | 28 | counted by eye, cell by cell |
| Frames with a clean result | 19 | every visible loon boxed exactly once, nothing else boxed |
| Frames with at least one defect | 7 | the complement |
| Loons found | ~26 of 28 | the 2 missed are both in the fog frame |
| Frames with duplicate boxes | 4 | `web_..._0042`, `web_..._0046`, `web_..._0037`, `web_..._0051` |
| Frames with a false positive | 1 | `web_..._0104` — the reed bed, plus a duck at 0.3 |
| Frames with a total miss | 1 | `web_..._0076` |

**Known soft edge.** `val_batch0_pred.jpg` r3c4 (`web_..._0115`) carries a second
low box near the frame edge that could be a duplicate or a separate false
positive. It is counted in the 7 defective frames but is not attributed to a
specific failure mode anywhere on screen or in narration.

**Two corrections made during the audit, recorded so they are not re-introduced.**
At full-sheet resolution, `dji_..._0141` and `nikon_..._0135` both look like
duplicate detections — each shows what reads as one label string over what reads
as one bird. Zooming in shows **two separate birds with one box each** in both
cases; the appearance of a duplicate is two adjacent labels colliding. Neither is
counted as a failure. The mosaic's label bars are not clipped to their cells, so
label collisions are an artifact of the plot, not of the model.

---

## Claims deliberately NOT made

| Not claimed | Why |
|---|---|
| Any precision, recall, mAP, F1 or IoU figure | Not supplied, and not computable from rendered JPEGs without ground-truth labels |
| Epoch count, image size, batch size, confidence threshold, train/val ratio | Not supplied |
| Which YOLO release was used | Not supplied |
| That `web_..._0107` (apparent Black Guillemot, detected as a common loon at 0.7) is a false positive | The species identification is not certain enough to assert. Logged in SOURCES.md as a data-quality item for the author. Counted nowhere; on no plate |
| That the duplicate-detection fix is definitely an NMS/IoU threshold change | B05 frames this as the voice's argument, not as a reported finding. Flagged for sign-off in PEDAGOGY.md |
| Any teammate's name | The author's explicit instruction |

---

## The one editorial argument

**B05** asserts that double-counting is a threshold setting rather than a
data-volume problem, and therefore that more images will not fix it. This is a
reasonable and conventional reading — overlapping duplicate boxes are normally a
non-maximum-suppression question — but it is **Claude's argument, not the
author's report**. It is called out in the PEDAGOGY.md checklist for explicit
sign-off before the reel is built.
