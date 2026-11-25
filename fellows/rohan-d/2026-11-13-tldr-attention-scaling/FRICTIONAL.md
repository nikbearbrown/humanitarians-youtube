# Frictional log — TL;DR on a paper: why attention divides by the square root of the key length

> DRAFT written from the real build record. Edit it into your own words and add what you understand now; the guide says entries are written as the work happens and never rewritten afterwards.

## 2026-11-23 — Why Attention Divides By The Square Root

- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-13`)
- **Evidence of commit:** [add the commit link once this folder is committed]

**What I was working on.** The Transformer's scaled dot-product attention divides scores by the square root of the key length. The film shows why: longer vectors give wider scores, wide scores make softmax pick one winner and starve the gradient, a fixed divisor fits one length only, and dividing by the square root keeps the spread constant.

**What I tried, and what I expected.**
- I expected to match the format of the reference films: composer ask, a corrected overview, numbers-first Manim beats, a recap, a your-turn prompt and the locked outro.
- I expected each beat to pass the toolkit's checks (layout audit, frame QC, type size) on the first or second render.

**Where it resisted, and what was done next.**
- Manim's `MathTex` needs `dvisvgm`, which was not installable here. I switched every equation to the toolkit's MathText SVG route.
- The review cut kept showing 'B0x' footers and timecodes. I told Claude it must never appear in any video; the labels now only render with `ART_REVIEW_LABELS=1`, including on contact sheets.
- Gate T (type) failed on the TL;DR cards; Claude patched the card components' font sizes and kept the originals.
- Several Gate B/V defects (a caption off the safe area, underfilled frames, a label sitting on the axis line) were fixed scene by scene.
- The outro's 1.0 s silent tail silently did not apply at first. Claude claimed the rebuild had fixed it before measuring; measuring showed it had not. The final masters measure about 1.04 s of silence.

**What Claude contributed, and what I did with it.**
- Claude read the repo's `tldr` skill, cut the paper into sections (I picked section S2), planned the film, wrote the narration and scenes, ran the toolkit and fact-checked 17 claims.
- I picked the paper and the section, approved the plan, and set the standing rule against 'B0x' footers.
- Accepted: the film structure, the computed numbers (each recomputed in code), and the fixes above.
- Rejected / changed: [add what you rejected or changed in your own words]

**What I understand now, and what I still do not.**
- Understood: [write in your own words what you now understand about the topic]
- Not understood / not verified:
- I have not listened to the narration for delivery and pacing, only checked its words with a speech-to-text pass.
- The vertical cut's question card is small in the portrait frame.
- The weekly guide's opening line ('Hi, I am [your name] and this video is about …') is not in this film.
