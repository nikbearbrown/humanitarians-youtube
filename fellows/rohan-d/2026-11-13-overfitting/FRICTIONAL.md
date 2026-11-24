# Frictional log — ML explainer: overfitting with eight noisy points and polynomial fits

> DRAFT written from the real build record. Edit it into your own words and add what you understand now; the guide says entries are written as the work happens and never rewritten afterwards.

## 2026-11-24 — Overfitting, One Memorized Point at a Time

- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-13`)
- **Evidence of commit:** [add the commit link once this folder is committed]

**What I was working on.** Eight noisy points around y = 2x. A straight line has train error 0.099 and test error 0.074. A degree-7 curve passes through every point (train 0.000) but its test error is 0.221. Test error turns around while training error keeps falling; more data (8 to 40 points) closes the gap; noise sets a floor of about 0.0625.

**What I tried, and what I expected.**
- I expected to match the format of the reference films: composer ask, a corrected overview, numbers-first Manim beats, a recap, a your-turn prompt and the locked outro.
- I expected each beat to pass the toolkit's checks (layout audit, frame QC, type size) on the first or second render.

**Where it resisted, and what was done next.**
- The degree-7 curve was clipped flat at the bottom of my first plot because its true minimum (-0.89) was below my axis range. Claude widened the range after the frame showed a suspicious flat segment.
- The overview text at first looked tiny; making it big then bled past the edge on the corrected sentence, so the size was reduced to fit.
- In the vertical cut a title ran into the right edge; Claude forced it to wrap at the right word.
- Two labels overlapped bar values in the portrait layout; I changed the layout to rows.

**What Claude contributed, and what I did with it.**
- Claude wrote the experiment, narration, scenes and paperwork and fixed every gate failure; my part was choosing the six-topic series and keeping the format.
- Accepted: the film structure, the computed numbers (each recomputed in code), and the fixes above.
- Rejected / changed: [add what you rejected or changed in your own words]

**What I understand now, and what I still do not.**
- Understood: [write in your own words what you now understand about the topic]
- Not understood / not verified:
- Not listened to for delivery.
- The 'noise floor' claim is approximate: it equals the noise variance 0.0625 in expectation.
