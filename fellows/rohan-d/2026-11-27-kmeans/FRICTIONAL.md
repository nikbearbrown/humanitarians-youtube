# Frictional log — ML explainer: k-means on seven points and a bad start

> DRAFT written from the real build record. Edit it into your own words and add what you understand now; the guide says entries are written as the work happens and never rewritten afterwards.

## 2026-11-24 — K-Means, One Reassignment at a Time

- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-27`)
- **Evidence of commit:** [add the commit link once this folder is committed]

**What I was working on.** Seven points, two centers starting at (1,1) and (5,6) settle at (1.25,1.5) and (3.9,5.1) in two rounds; inertia falls from 19.25 to 8.53 and never rises. Four rectangle corners show two stable answers, inertia 4 and 16, depending on the start.

**What I tried, and what I expected.**
- I expected to match the format of the reference films: composer ask, a corrected overview, numbers-first Manim beats, a recap, a your-turn prompt and the locked outro.
- I expected each beat to pass the toolkit's checks (layout audit, frame QC, type size) on the first or second render.

**Where it resisted, and what was done next.**
- My first starting centers left one point exactly equidistant from both, so the example depended on a tie-break. Claude moved the second center to (5,6) to remove the tie.
- The master was blocked by the type check on one beat with 38 px text. Enlarging the readouts did not fix it; making the half-drawn lines static did, which suggests partially drawn lines were being read as small text.
- Scatter frames were underfilled until the plane was enlarged and outlined.

**What Claude contributed, and what I did with it.**
- Claude computed the iterations, wrote the scenes and handled the gates.
- Accepted: the film structure, the computed numbers (each recomputed in code), and the fixes above.
- Rejected / changed: [add what you rejected or changed in your own words]

**What I understand now, and what I still do not.**
- Understood: [write in your own words what you now understand about the topic]
- Not understood / not verified:
- Why partial lines trip the text check is my guess, not confirmed.
- Delivery not judged by ear.
