# Frictional log — ML explainer: a 3 by 3 edge kernel on a 6 by 6 image

> DRAFT written from the real build record. Edit it into your own words and add what you understand now; the guide says entries are written as the work happens and never rewritten afterwards.

## 2026-11-24 — Convolution, One Window at a Time

- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-20`)
- **Evidence of commit:** [add the commit link once this folder is committed]

**What I was working on.** A 3 by 3 kernel with columns -1, 0, 1 slides over a 6 by 6 image whose rows are 0 0 0 9 9 9. The output rows read 0, 27, 27, 0. One kernel of 9 weights replaces 576 in a fully connected layer, and each unpadded layer shrinks the map by 2.

**What I tried, and what I expected.**
- I expected to match the format of the reference films: composer ask, a corrected overview, numbers-first Manim beats, a recap, a your-turn prompt and the locked outro.
- I expected each beat to pass the toolkit's checks (layout audit, frame QC, type size) on the first or second render.

**Where it resisted, and what was done next.**
- Several beats were underfilled in the frame check (too much empty space), so elements were enlarged or brought in earlier.
- A stray panel edge and a label crossed each other; Claude moved the labels in and narrowed the highlight box.
- The narration for the overview came out under the 9 s minimum, so Claude added one sentence and regenerated that line.
- Portrait layout: the sum readout sat on the right margin, and a shortened label fixed another overflow.

**What Claude contributed, and what I did with it.**
- Claude wrote the experiment, scenes and paperwork; I kept the series going and reviewed the contact sheets.
- Accepted: the film structure, the computed numbers (each recomputed in code), and the fixes above.
- Rejected / changed: [add what you rejected or changed in your own words]

**What I understand now, and what I still do not.**
- Understood: [write in your own words what you now understand about the topic]
- Not understood / not verified:
- Delivery not judged by ear.
- In the vertical film one label sits very close to its bar.
