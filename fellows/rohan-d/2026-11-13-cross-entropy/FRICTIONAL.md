# Frictional log — ML explainer: cross-entropy loss and why confident mistakes cost so much

> DRAFT written from the real build record. Edit it into your own words and add what you understand now; the guide says entries are written as the work happens and never rewritten afterwards.

## 2026-11-24 — Cross-Entropy, One Surprise at a Time

- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-13`)
- **Evidence of commit:** [add the commit link once this folder is committed]

**What I was working on.** How a classifier turns scores into a loss: softmax shares 66/24/10, loss minus-log of the right answer's share (0.417), why a confident mistake costs 4.6 while a hedge costs 0.7, the slope share-minus-answer, and the clipping floor (27.63).

**What I tried, and what I expected.**
- I expected to match the format of the reference films: composer ask, a corrected overview, numbers-first Manim beats, a recap, a your-turn prompt and the locked outro.
- I expected each beat to pass the toolkit's checks (layout audit, frame QC, type size) on the first or second render.

**Where it resisted, and what was done next.**
- I first built from the wrong reference videos. After I attached the right ones, Claude re-read them and rebuilt the film on the `ai-explainer` spine instead of the `tldr` spine.
- The writer's correction never fired: the trigger phrase ended in a period and the writer matches phrases without punctuation. Claude found it on a frame at the end of the beat and fixed it.
- Cached clips hid edits more than once (the clip is reused unless deleted); Claude learned to delete the beat's clip after every change.
- Pre-flight needed shapes that change (Transform/GrowFromEdge); Claude restructured the bars so the static check passed.
- I asked for the greeting 'Namaste' to be changed to 'Hi'; Claude re-recorded the first line and rebuilt both masters.

**What Claude contributed, and what I did with it.**
- Claude chose the topic angle, computed the numbers, wrote the script and scenes, and ran every gate.
- I supplied the reference films and asked for the format to match, and I made the greeting decision.
- Accepted: the film structure, the computed numbers (each recomputed in code), and the fixes above.
- Rejected / changed: [add what you rejected or changed in your own words]

**What I understand now, and what I still do not.**
- Understood: [write in your own words what you now understand about the topic]
- Not understood / not verified:
- Narration delivery and timing not judged by ear.
- The Fellows guide's opening line is not in this film because the reference films do not have it.
