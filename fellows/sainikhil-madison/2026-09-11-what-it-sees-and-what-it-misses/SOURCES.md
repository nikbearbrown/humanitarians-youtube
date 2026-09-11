# SOURCES — What It Sees, And What It Misses

Week of 2026-09-11 · LoonNet, first iteration.

---

## Primary sources

| Source | Used for | Provenance |
|---|---|---|
| `data/val_batch0_pred.jpg` | B02 full plate; 3 of the 4 panels on B04; every per-frame confidence quoted | The author's own YOLO validation output. 1920×1280, a 4×4 sheet of 480×320 cells, 16 populated |
| `data/val_batch1_pred.jpg` | the NOT FOUND panel on B04; 10 of the 26 audited frames | The author's own YOLO validation output. 1920×1920, a 4×4 sheet of 480×480 cells, 10 populated |
| The author's written weekly update | every SUPPLIED claim in FACTCHECK.md | Supplied directly, 2026-09-11 |

Both images are staged unmodified into `images/` and composed by
`make_plates.py`. No bounding box, label or confidence value is redrawn,
retouched or repositioned anywhere in this reel.

---

## No external sources

This reel cites no papers, datasets, repositories or URLs. Every factual claim
resolves to either the author's own report or his own output images. Nothing was
looked up, and nothing needs a link.

The project context — the National Loon Center, the wider application — appears
only in the `tags` block of `beat_sheet.json`, never as an on-screen claim.

---

## Honesty log

**Numbers avoided.** No precision, recall, accuracy, mAP, F1, IoU, epoch count,
image size, batch size, train/val ratio or confidence threshold appears anywhere
in the reel. None were supplied. The author states these are coming before the
team meeting, and B07 says so on screen.

**Numbers that ARE on screen, and what they are.** 106 and 26 are the author's.
Every confidence value (0.3–0.9) and both class names are printed into the
supplied mosaics by YOLO itself. Everything else — 19 clean, 7 defective, 28
loons, ~26 found — is a hand audit performed by reading the two sheets cell by
cell, and is labelled as a hand audit in B07's fourth artifact line. **That line
is load-bearing and must not be cut for time.**

**A fourth weakness, added with the author's approval.** The author's write-up
lists three weaknesses. A fourth is plainly visible: `web_20260818_0076.jpg`
shows two loons in fog and the model returned no detection at all. This was put
to the author before the reel was built and he asked for it to be included.

**Two apparent failures that turned out not to be.** At full-sheet resolution,
`dji_20260822_143917_0141.jpg` and `nikon_20260822_122743_0135.jpg` both read as
duplicate detections. At 5× they are two separate birds with one box each; the
"duplicate" is two adjacent label bars colliding. Neither is counted as a
failure. Recorded here because the mistake is easy to repeat — the mosaic's
label bars are not clipped to their cells.

**A claim not made.** `val_batch1_pred.jpg` r4c2 (`web_20260818_0107.jpg`) shows
a black-and-white seabird on a rock, detected as `common loon` at 0.7. It has
large white wing patches and a short bill, and looks more like a **Black
Guillemot** than a Common Loon. If that is right, it is either a false positive
or a mislabelled training image — and it would be the more interesting of the
two. The identification is not certain enough to put on screen, so it is counted
nowhere, appears on no plate, and is raised here instead.

> **For the author:** worth checking this frame's provenance and label before the
> meeting. A web-sourced image of the wrong species in the set would explain more
> than a threshold would.

**Capture paths are an inference.** "Web stills, a Nikon from shore, a drone over
open water, and a phone" is read off the `web_`, `nikon_`, `dji_` and `iphone_`
filename prefixes in the supplied mosaics. It is the only inference this reel
draws from the images, and it is visible to anyone looking at the same plate.

**One editorial argument.** B05 argues that double-counting is an overlap
threshold rather than a data-volume problem. This is Claude's reasoning, not the
author's report, and is flagged for sign-off in PEDAGOGY.md.

**No names.** No teammate is named in narration, on screen, or in any file in
this folder. Collaborators appear as "we" and "the team", per the author's
instruction.
