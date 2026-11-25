# Frictional log — Shipped, Then Blocked

## 2026-08-11 — 2:58, 14 beats, Bella / Humanitarians AI

Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`. Master MP4 held outside Git per repository policy. (YouTube: TBD.)

**What I was working on.** A ~3-minute cut of the ship log with no individual named.

**What I tried, and what I expected.** I expected to estimate the length by feel.

**Where it resisted, and what I did next.**
* Guessing was useless. Measured Bella's actual pace from the previous reel instead —
  1,463 words / 652.4s = **2.242 words/sec** — which set a 405-word budget for 3:00.
  Script came in at 421 words; output was 2:58.
* The constant is not stable across scripts. A later reel ran at 2.62 wps on more
  technical vocabulary. It is a planning estimate, not a precise instrument.
* Removing the name needed more than a find-and-replace: the source credits an engineer
  four times, and the handle appeared in on-screen props too. Added a programmatic guard
  over all five spellings, checking narration *and* props.

**What Claude contributed, and what I did with it.** Mine: the 3-minute constraint, the
no-name constraint, keeping the Teardown register. Claude's: the calibration, the cut,
the name guard.

**What I understand now, and what I still do not.**
* Understood: a measured pace constant beats intuition for hitting a length target, and
  a name-removal is a build-time assertion, not an edit.
* Not resolved: B06's matrix shows 450 routes while the narration says sitemaps handle
  "up to 50,000 URLs" — different quantities, easy for a viewer to conflate.
