# SOURCES — Every Image Earns Its Place

Primary source: **the author's own verbal weekly report**, given at build time
on 2026-08-21, plus **two screenshots of his Lovable mock** supplied with it.
There is no external literature behind this reel — it is a progress report, and
every claim in it is the author's account of his own week.

---

## What the author reported

| Deliverable | Beat | Detail as given |
|---|---|---|
| Centralized repository for all loon images | B01, B06 | "one place to store all the loon images" |
| Script, half one — quality | B02, B06 | "make sure each image is worthy enough to be in the training data set". Confirmed at intake as **blur/sharpness** and **resolution or altitude floor**. No threshold values supplied. |
| Script, half two — duplicates | B03, B06 | "making sure that we don't have any duplicate images". Confirmed at intake as **exact file hash only**. |
| Mock of the user flow | B04, B05, B06 | Built in **Lovable**, "as demo for ourselves for the app itself" |

Status as reported: the repository is created, the script is **being built**, the
mock is created. The reel does not describe the script as finished.

---

## Screenshots on screen

| File | Beat | Composed to |
|---|---|---|
| `images/B04-source.png` (1676×1054) | B04 | `media/B04.png` 3840×2160 · `pantry/B04-916.png` 2160×3840 |
| `images/B05-source.png` (1658×1052) | B05 | `media/B05.png` 3840×2160 · `pantry/B05-916.png` 2160×3840 |

Both are the author's own captures of his own prototype. Composition is done by
`make_plates.py` in this folder, which is re-runnable.

**Provenance note — the sources were recovered, not original.** The captures were
supplied as `~/Desktop/Screenshot 2026-08-21 at 15.34.49.png` and
`…15.35.06.png`, and were cleared off the Desktop partway through the build,
before the plates were re-composed. The regenerate failed on a missing source
rather than overwriting, so the first-pass plates survived — and the PORTRAIT
ones carried the full uncropped capture at only 1.13× upscale. `images/*-source.png`
were extracted from those and downscaled back to the original pixel dimensions,
so they are a 1.13× round trip rather than the untouched originals. Visually
equivalent at the sizes used here; very slightly softer than a fresh capture
would be. If the originals resurface, replace these two files and re-run
`make_plates.py`.

Text visible on screen and quoted or paraphrased in narration:

- "Immer helps biologists find loons, nests, and habitat change in aerial
  imagery — with every AI detection reviewed by a researcher before it becomes
  data." → paraphrased in B04's narration as the promise on the front page.
- The three landing cards: "Analyze imagery", "Review with care", "Build the
  dataset" → the analyze → review → dataset shape named in B05.

---

## Numbers: there are none

**The author confirmed he has no real figures this week.** Accordingly this reel
puts **no numeric claim** on screen or in narration — no image counts, no reject
rates, no duplicate totals, no thresholds, no percentages. `ScaleComparison`,
the numeric deck pattern, is deliberately **not used** anywhere in this reel even
though it was available and has a registered portrait sibling.

### The one place figures appear, and how it is handled

B05's screenshot is a Lovable mock and is full of Lovable's invented placeholder
data — 1,248 images analyzed, 387 loons detected, 24 nests, 17 pending reviews,
68% annotation progress, per-file confidences of 92%/87%/91%, and a "past 8
weeks" detection chart. **None of these are measurements of anything.** They are
on screen because the screenshot is the deliverable being shown.

Two mitigations, deliberately redundant:

1. **Spoken.** B05's narration states it directly: "Every figure on this screen
   is a placeholder that Lovable filled in — none of it is measured."
2. **Burned in.** The plate carries the caption `MOCK DATA · EVERY FIGURE ON
   THIS SCREEN IS A PLACEHOLDER`, so a frame pulled out of the video still
   carries the disclaimer. B04's plate is captioned `LOVABLE MOCK · USER FLOW,
   NOT A BUILD`.

---

## Honesty log

**A limitation promoted to a beat.** The dedupe is exact file hashing, which
catches a re-uploaded file and nothing else. Rather than describe the duplicate
problem as solved, B03 is built around the three cases it does not catch —
burst frames, the same bird on a second pass, the same lake minutes later. The
caption names why it matters: those are the near-duplicates that leak one
individual across a train/test split. This is stated as an open problem and
B08's tease commits it to next week.

**A claim narrowed to what was confirmed.** The author's phrasing was that the
script checks whether an image is "worthy enough" for the training set. That
could cover many things. At intake it was narrowed to sharpness and
resolution/altitude only, and B02 asserts only those two. Loon-presence and
exposure checks were explicitly **not** confirmed and so appear nowhere — the
PEDAGOGY checklist asks the reviewer to add them if the script has since grown.

**No threshold values.** B02 says "sharp enough" and "big enough" rather than
naming a variance-of-Laplacian cutoff or a pixel floor, because no numbers were
supplied and a plausible-looking threshold is still an invented figure.

**Nothing about the model.** The reel makes no claim about detection accuracy,
model architecture, or performance, because no model was trained this week. The
closing line makes that explicit rather than leaving it as an absence.

**No URLs.** No link is shown on screen or read aloud. "National Loon Center"
and "Immer" appear only as names, both visible in the author's own screenshots.

---

## Where the two cuts differ

Narration is **word for word identical** — the short reuses all nine parent
mp3s, because at 114.7s the reel is under the 180s Shorts cap, so no beat was
dropped and the outro was not rewritten. Two on-screen (not spoken) differences
were forced by the portrait frame:

| Beat | 16:9 | 9:16 | Why |
|---|---|---|---|
| B04 | ken burns, focus [0.34, 0.42] | `hold` | The portrait plate has ~148px of margin against the landscape plate's 440px, so `compile.py`'s zoompan push crossed the title-safe right edge (Gate V BLOCKER). Holding also reads better on a phone. |
| B07 | segment "Write The Admission Rule" | segment "The Admission Rule" | The longer string overflows `ClaudeComposerAsk916`'s title width. The landscape composition has room, so the long was not degraded to match. |

## Gate V status at delivery

| Cut | BLOCKER | MAJOR |
|---|---|---|
| 16:9 master | **0** | 7 — all `underfill` |
| 9:16 short | **0** | 9 — all `underfill` |

Every remaining finding is the canvas-fill check on centred cards and on the two
portrait stills. B08 (title card) reads 12% in 16:9 and 23% in 9:16 because it is
a centred title; B06 (verdict artifact) 52%; the portrait stills 41–47% because a
1.59:1 screenshot can only fill so much of a 9:16 frame. These were reviewed
against the frames and left alone rather than cropping the author's screenshots
or padding the cards to satisfy a metric.

**The short must be audited against the CLEAN master, not the slate.**
`final_frame_check.py`'s `BURN_IN_EXCLUDE` masks its own review burn-ins as
fractions tuned to 16:9. On a 2160×3840 frame the timecode (`fontsize=0.04*h`,
so ~154px tall and ~1080px wide, starting near x=1064) extends well left of the
mask's `0.84 × 2160 = 1814` boundary, sits above the safe top, and is counted as
content — producing an edge-bleed BLOCKER on every beat. Auditing the slate
reported 20 BLOCKERs; auditing the clean master reported 4, all real, all since
fixed. This is a toolkit bug, not a reel defect.
