# Frictional log — ML explainer: dropout and inverted scaling on eight activations

> DRAFT written from the real build record. Edit it into your own words and add what you understand now; the guide says entries are written as the work happens and never rewritten afterwards.

## 2026-11-24 — Dropout, One Silenced Unit at a Time

- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-27`)
- **Evidence of commit:** [add the commit link once this folder is committed]

**What I was working on.** Eight activations 1 to 8 sum to 36. A random mask keeps 1, 5, 6, 7 (sum 19, scaled 38). Ten thousand masks average 35.98, unscaled they average 18; 256 masks average exactly 36 for a plain sum; noise grows with p (4.8, 14.3, 42.9).

**What I tried, and what I expected.**
- I expected to match the format of the reference films: composer ask, a corrected overview, numbers-first Manim beats, a recap, a your-turn prompt and the locked outro.
- I expected each beat to pass the toolkit's checks (layout audit, frame QC, type size) on the first or second render.

**Where it resisted, and what was done next.**
- Two headings stacked on top of each other because I faded the new heading in without removing the old one; the layout check flagged it and Claude replaced it with a cross-fade.
- The type check said it could not find dark text in one beat that used only grey labels, so those labels became ink.
- A pale grid failed the contrast check in the portrait cut and was darkened.

**What Claude contributed, and what I did with it.**
- Claude wrote the film end to end; I asked for one more topic.
- Accepted: the film structure, the computed numbers (each recomputed in code), and the fixes above.
- Rejected / changed: [add what you rejected or changed in your own words]

**What I understand now, and what I still do not.**
- Understood: [write in your own words what you now understand about the topic]
- Not understood / not verified:
- 'Dropout trains many networks' is framed as a view, not a proof.
- Delivery not judged by ear.
