# Frictional log — ML explainer: momentum in gradient descent on a narrow valley

> DRAFT written from the real build record. Edit it into your own words and add what you understand now; the guide says entries are written as the work happens and never rewritten afterwards.

## 2026-11-24 — Momentum, One Remembered Step at a Time

- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-20`)
- **Evidence of commit:** [add the commit link once this folder is committed]

**What I was working on.** On the loss 0.5(x^2 + 25y^2) from (4, 1), plain descent bounces across the valley and needs 47 steps to reach loss 0.01; momentum with beta 0.5 needs 20; beta 0.9 needs 53; beta 0.99 does not settle in 200 steps. The film shows why: swings across the valley cancel in the velocity while steady slopes along it add up.

**What I tried, and what I expected.**
- I expected to match the format of the reference films: composer ask, a corrected overview, numbers-first Manim beats, a recap, a your-turn prompt and the locked outro.
- I expected each beat to pass the toolkit's checks (layout audit, frame QC, type size) on the first or second render.

**Where it resisted, and what was done next.**
- Pale valley contours failed the contrast check (ink-on-background separation below 0.3); I darkened them.
- The slope bars in one beat collided with their header and a legend; Claude resized the bars and re-spaced the labels.
- In the vertical cut the valley is turned on its side so its long axis fits the tall frame.
- A 'start' label sat on a contour line and failed the label-on-line check, so it became a ring around the start point.

**What Claude contributed, and what I did with it.**
- Claude computed all step counts, wrote the equations (MathText SVG), narration and scenes, and ran the gates.
- Accepted: the film structure, the computed numbers (each recomputed in code), and the fixes above.
- Rejected / changed: [add what you rejected or changed in your own words]

**What I understand now, and what I still do not.**
- Understood: [write in your own words what you now understand about the topic]
- Not understood / not verified:
- Delivery and timing not judged by ear.
