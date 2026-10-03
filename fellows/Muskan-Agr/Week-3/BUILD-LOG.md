# BUILD-LOG — humanitarians-ai-week3-stakeholder-strategy-hierarchy

## 2026-09-05 — authored (Claude, against the brutalist.art-main toolkit)

- HUMAN NOTE: Muskan Agrawal supplied the Week 3 scope as four threads —
  planning the stakeholder insight approach, drafting interview questions,
  building a structural hierarchy strategy, and continuing hero refinement —
  and asked for the site to be examined again so the claims are backed by
  images, plus a set of open-ended stakeholder questions to appear in the
  video, plus additional senior-level content.
- STANDING INSTRUCTION (unchanged): B00 opens "Hello, I am Muskan Agrawal, and
  this video is a summary of …".
- STANDING RULE from Week 2: the site is never shown altered, and no proposed
  layout is drawn. Honoured — see B15/B16.

## The problem this week posed, and the spine that solves it

Weeks 1 and 2 had an easy narrative engine: measure something, show the
number. Week 3's actual work was preparation — a meeting plan, a question set,
a hierarchy strategy. There is no new measurement in "I drafted questions", and
a video that just lists what was prepared would be the weakest of the four.

So the spine inverts the series' own method: **Week 3 is about where
measurement runs out.** The audit can tell you the hero is media-heavy. It
cannot tell you who the site is for, what it should say first, or what counts
as success. Those are organizational decisions, and a designer who makes them
alone is guessing with better typography.

That framing turns "no new specification this week" from a weakness into the
subject, and it makes the question set the natural payoff rather than an
appendix.

## Every question on screen is anchored to a measured finding

The nine questions in B12–B14 are not generic UX-interview boilerplate. Each
one exists because something specific was measured first:

- eight audiences with no stated priority → "which single audience matters most
  this quarter?"
- 24 named concepts in 1,200 words → "which would you keep if a stranger had to
  read the page unhelped?"
- three identically weighted asks → "if a visitor does exactly one thing, what
  should it be?"
- no outcome numbers anywhere on the page → "what is the one number that would
  show this year was worth funding?"

The full forty-question guide is in DISCUSSION-GUIDE.md, with facilitation
notes and a write-up protocol. The video shows nine.

## New measurements taken this week

Live DOM survey of humanitarians.ai on 2026-09-05, plus `/about`, `/donate`,
`/clients`, `/fellows`:

- **8 audiences** addressed on the homepage (mention counts in SOURCES.md)
- **24 named concepts** in **1,201 words** — one every 50 words
- **13 onward links**; **69 clickable labels**, **54 distinct**
- **3 identically weighted asks** mid-page (measured off the screenshot pixels)
- Trust: 501(c)(3), EIN 33-1984805 and a state registration are stated; no
  annual report, Form 990, named board or third-party rating on any of the
  five pages checked
- **23 numeric tokens on the homepage, 0 of them outcomes**

### The finding that matters most

The homepage carries **two incompatible statements about donation use**, both
beginning "100%", both on the same page:

> mid-page — "100% of donations fund the programs, mentorship, and project
> support that make this happen."
>
> footer — "100% of all donations support our direct operational costs,
> including program expenses, legal fees, and staff salaries to advance our
> mission."

A careful donor comparing them cannot tell which applies. This is the single
clearest example in the whole series of something a designer must surface and
must not resolve alone — which is exactly the argument the video makes. It is
quoted verbatim in B08 and asked as question 28 in the discussion guide.

FACTCHECK.md notes that if Muskan would rather raise this privately with the
organization before it appears in a video, B08 can be cut without breaking the
reel.

## Both reserve screenshots finally earn their place

Week 1 copied `02_tier_framework.jpg` and `05_mission_cta_spotify.jpg` into
assets/ and used neither, noting they were held for extra runtime. Week 2 did
not use them either. Week 3 uses both, and not as filler:

- `02_tier_framework.jpg` is the clearest on-site evidence of internal
  shorthand — three cards that say Tier 1, Tiers 3–6, Tier 7 with no
  explanation of what a tier is.
- `05_mission_cta_spotify.jpg` is the only capture showing the three
  simultaneous asks side by side.

No new screenshots were needed.

## QC reproduced locally before asking for a render

- **GATE A** — first pass found **six blocking errors**, all the same class as
  Week 2's B09 and B14: "shapes never change — 1 distinct shape-state". Every
  one was a scene built from Text plus a single static accent bar. B12, B13 and
  B14 (the question pages), B15, B16 and B17. Fixed by landing a maroon mark
  with each question / step / row — the same device Week 1's B08 used for its
  ladder rungs. **This is now a known pattern for this toolkit: any card-like
  scene needs at least one shape that appears over time.**
- Final: **0 blocking errors and 0 warnings across all 19 scenes.** Week 1
  shipped with 4 warnings, Week 2 with 7. Using `marked_rows()` for the list
  scenes removed the "text-only scene" warning class entirely.
- **GATE W** — **19 of 19 scenes checked, 19 of 19 clean**, no crashes. The
  Week 2 workarounds (literal `buff`, literal `font_size` inside `construct`)
  are carried forward in the module docstring as standing rules.
- **beat_lint.py** — clean.
- **GATE B geometry** pre-computed by hand: all seven annotation boxes mapped
  through `rect_in_image()` at 16:9 and confirmed on-frame.

### One geometry decision worth recording

The third tier card reaches y = −2.37, and the bottom safe-area line is
−3.40. A chip pinned at y_frac 0.87 would leave 0.16 units of clearance — legal
but uncomfortably close, and exactly the situation that produced Week 1's
hand-nudged chips. B04 and B06 therefore use `chip_below()`, which measures the
available band and fits the chip into it. Cannot collide by construction.

## Runtime

694 narration words. Calibration now has two real data points:

| build | words | seconds | wps |
|---|---|---|---|
| Week 1 | 475 | 164.57 | 2.89 |
| Week 2 | 655 | 217.61 | 3.01 |

Planned at the 3.00 midpoint → **231s (3:51)**. Week 2 landed 4% under its
estimate, so the realistic landing zone is **3:40–3:53**, inside the target
either way.

## What's NOT done yet

- **Sign FACTCHECK.md** — four open rows, all about whether the themes,
  questions and hierarchy order match what Muskan actually produced.
- **Decide on B08** — publish the donation conflict, or raise it privately first.
- **Run the audio + render locally.** See README-RUN-THIS.md.
- **The 9:16 cut** — still unresolved for Weeks 1 and 2 as well.

## Revision — B17, after Week 4 turned out differently

B17 originally closed with "WEEK 4 — THE ANSWERS", on the assumption that the
stakeholder meeting prepared in Week 3 would happen before Week 4. It did not.
Week 4 instead became navigation cleanup carried out directly with the
developer — stripping nav and footer links pointing at projects with no defined
concept behind them, the same unlabeled names Week 1 flagged — plus agreeing
the design-to-development collaboration workflow and the developer's handoff
requirements.

B17 now names that. The rest of the reel is unaffected: nothing else in Week 3
claimed the meeting had happened, and B16 already said the hero would not be
redrawn until the message owners decide. The narration also keeps "the meeting
they are for", which remains true — it is prepared and pending.

Runtime moved 3:51 -> 3:54. B17's audio needs regenerating; every other mp3 is
unchanged.

## Gate status
- [ ] GATE F (FACTCHECK.md) — DRAFT, 4 open rows
- [x] GATE — every on-screen figure measured (this log + SOURCES.md)
- [x] GATE A — reproduced locally: 0 blocking errors, 0 warnings
- [x] GATE W — reproduced locally: 19/19 checked, 19/19 clean
- [x] beat_lint — clean
- [ ] GATE B — needs the render
- [ ] Local render, 4K master, 9:16 short — not yet run
