# Frictional log — Teaching a Machine to Be Nice

## 2026-10-19 — 5:05, 22 beats, Bella / Humanitarians AI

Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`, `build_beat_sheet.py`. Master MP4 held outside Git per repository policy. (YouTube: TBD.)

**What I was working on.** A kid-friendly explainer of a from-scratch alignment
notebook (SFT, reward model, best-of-n, RLHF with and without a KL penalty, DPO).

**What I tried, and what I expected.** I expected reward hacking to be a thing I'd have
to argue for.

**Where it resisted, and what I did next.**
* The notebook runs it deliberately. Unleashed, the judge's score climbs `+0.21 → +1.77`
  while real quality falls `+0.58 → -3.00` and grammar hits **0%**. It calls that its most
  important plot, and it is right.
* Structuring it mattered more than animating it: show the judge's blind spots *first*
  (it cannot hear "not"; it rewards repetition), and a child can predict the exploit
  before it happens.
* I wrote **three** underlength beats this time, including the centrepiece at 6.8s where
  the hacked text barely appeared. Rather than fix the one I noticed, I audited every
  dense scene by duration; three failed and all three went to 17–20s.
* The scoreboard's `-3.00` bar overflowed its track and covered its own label, because I
  had sized bars assuming values near ±1.

**What Claude contributed, and what I did with it.** Mine: Goodhart as the closing idea,
delivered without the name and connected to marks and step counts. Claude's: 7 scenes,
13 assertions, the duration audit.

**What I understand now, and what I still do not.**
* Understood: dense scene plus short narration is a failure mode I will keep hitting
  unless something checks it automatically.
* Not resolved: DPO's failure here is this run's behaviour. The notebook calls it a
  known quirk; I state that rather than implying the code is wrong.
