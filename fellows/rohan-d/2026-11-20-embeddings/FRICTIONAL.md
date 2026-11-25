# Frictional log — ML explainer: distance versus cosine on toy 2-D word vectors

> DRAFT written from the real build record. Edit it into your own words and add what you understand now; the guide says entries are written as the work happens and never rewritten afterwards.

## 2026-11-24 — Embeddings, One Angle at a Time

- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-20`)
- **Evidence of commit:** [add the commit link once this folder is committed]

**What I was working on.** Toy vectors cat (4,1), dog (3,2), car (1,4). Distance says a cat is 8.2 from three cats and 4.2 from a car; cosine gives 1.00 for three cats, 0.94 for dog and 0.47 for car. High cosine means near, not the same, and a zero vector has no cosine.

**What I tried, and what I expected.**
- I expected to match the format of the reference films: composer ask, a corrected overview, numbers-first Manim beats, a recap, a your-turn prompt and the locked outro.
- I expected each beat to pass the toolkit's checks (layout audit, frame QC, type size) on the first or second render.

**Where it resisted, and what was done next.**
- The distance-versus-length story needed a pair of vectors where distance really misleads; Claude picked cat versus cat times three.
- Several scene frames were underfilled and were scaled up; one portrait title touched the right edge, so a shorter on-screen title was used (the outro keeps the full title).
- The portrait labels near arrow tips initially overflowed the margin.

**What Claude contributed, and what I did with it.**
- Claude computed the angles and cosines, wrote the equations, scenes and narration, and handled the gates.
- Accepted: the film structure, the computed numbers (each recomputed in code), and the fixes above.
- Rejected / changed: [add what you rejected or changed in your own words]

**What I understand now, and what I still do not.**
- Understood: [write in your own words what you now understand about the topic]
- Not understood / not verified:
- The film uses toy 2-D vectors and says so; it does not show a trained embedding.
- Delivery not judged by ear.
