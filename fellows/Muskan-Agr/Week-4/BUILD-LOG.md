# BUILD-LOG — humanitarians-ai-week4-navigation-cleanup-handoff

## 2026-09-06 — authored (Claude, against the brutalist.art-main toolkit)

- HUMAN NOTE: Muskan Agrawal supplied the Week 4 scope — the stakeholder
  meeting from Week 3 had not happened, so she moved into navigation cleanup
  directly with the developer using the Week 2 link audit as a working
  document, then spent the rest of the week agreeing the design-to-development
  collaboration framework and handoff format.
- STANDING INSTRUCTION (unchanged): B00 opens "Hello, I am Muskan Agrawal, and
  this video is a summary of …".
- STANDING RULE from Week 2: the site is never shown altered; no proposed
  layout is drawn.

## The check that changed how this reel is written

The brief describes the cleanup in the past tense: "we removed", "what remains
in the navigation and footer now is a smaller, honest set of links". Before
building anything, the live site was re-measured at the same 1503×812 viewport
used in Weeks 2 and 3.

**Nothing had changed.**

```
                      Week 2      Week 3      Week 4 check
footer columns             6           6                 6
footer column links       33          33                33
footer anchors            39          39                39
Projects-column links     11          11                11
clickable / distinct   69/54       69/54             69/54
homepage words             —       1,201             1,201
```

All five names scoped for removal — Dewey, Madison, Medhavy, Mycroft, Popper —
were still live on 2026-09-06.

So the cleanup is a **decision taken with the developer, not a deployment**.
Building the reel around "the site is now clearer" would have put a claim on
screen that any viewer could falsify by opening the site. B08 exists for
exactly that reason: *decided, specified, not yet deployed*, with the narration
saying plainly that the old links are still live today. The arithmetic in B06
is framed as **current vs agreed**.

This is not a hedge. Stating the status precisely is what makes the rest of the
video credible — and it is the same discipline the series has applied to every
number since Week 1.

## The spine

Week 4 had a structural risk: its headline work is a *decision* and a
*process*, neither of which photographs. The spine that carries it is the
opening problem — the meeting didn't happen — turned into the lesson:

**Move the part that isn't blocked, and agree the handoff before you design.**

That makes the two halves of the week one argument rather than two updates. The
cleanup is what could move without the stakeholders; the collaboration
framework is what stops the *next* phase stalling for a different reason.

## A loop that closes across all four videos

The five names removed are the same five Week 1 flagged as unlabeled, and five
of the six Week 3 counted as bare proper nouns. B05 says so on screen:
*flagged in Week 1, counted in Week 3, scoped in Week 4.* Four videos, one
finding, carried from observation to specification to action. That is the best
argument the series makes for doing the audit properly in the first place.

## The arithmetic

| metric | today | after the agreed cleanup | change |
|---|---|---|---|
| Projects-column links | 11 | 6 | −45% |
| Footer column links | 33 | 28 | −5 |
| Footer anchors | 39 | 34 | −5 |
| Bare proper nouns | 6 | 1 | −5 |

Musinique is the one bare proper noun that remains — it also appears in the
Resources column and points at a real external site.

## QC reproduced locally before asking for a render

- **GATE A** — first pass: **2 blocking errors** (B03, B13) and 2 warnings
  (B12, B14). All four the same known pattern: a scene built from Text plus at
  most one static accent bar records no changing shape state. Fixed by landing
  a mark with the closing line (B03, B13) and giving each framework part its
  own maroon rule that grows on cue (B12, B14).
- Final: **0 blocking errors, 0 warnings across all 20 scenes** — matching
  Week 3, and better than Week 1 (4 warnings) and Week 2 (7).
- **GATE W** — 20 of 20 checked, 20 of 20 clean, no crashes.
- **beat_lint.py** — clean.
- **GATE B geometry** pre-computed: B04 is the only annotated beat; its box maps
  to left 3.43 / bottom −0.01 / right 4.55 / top 3.22, on-frame, with the chip
  clear of it by 2.44 units and 0.09 units inside the bottom safe line.

### Rules now carried in the module docstring

Week 3's GATE B failure added two permanent rules to this series' scenes.py
header, and both are honoured here:

- **Never use `""` spacer lines in a text stack.** `Text("")` has zero height,
  `arrange()` computes spacing off degenerate geometry, and the real lines land
  on top of each other. That produced a genuine 100%-overlap GATE B error.
- **The audit's horizontal safe area is ±6.3, not the ±6.51 that `SAFE_BUFF`
  alone allows.** Text-heavy scenes fit to `SAFE_BUFF_X = 0.85`.

## Runtime

699 words at the measured 3.03 wps → **230.7s (3:51)**. Calibration across the
series:

| build | words | seconds | wps |
|---|---|---|---|
| Week 1 | 475 | 164.57 | 2.89 |
| Week 2 | 655 | 217.61 | 3.01 |
| Week 3 | 698 | 230.55 | 3.03 |

Three builds, converging on ~3.0. Week 4 is planned at 3.03.

## What's NOT done yet

- **Sign FACTCHECK.md** — five open rows, the important one being the
  deployment status.
- **Confirm the developer's name.** The brief says "Rushali" once and "Rashi"
  twice, so the reel says "the developer" throughout and names nobody.
- **Confirm the removal list** is exactly those five names.
- **Run the audio + render.** See README-RUN-THIS.md.
- **The 9:16 cut** — still outstanding across the whole series.

## Gate status
- [ ] GATE F (FACTCHECK.md) — DRAFT, 5 open rows
- [x] GATE — live-site status re-verified 2026-09-06 (this log + SOURCES.md)
- [x] GATE A — reproduced locally: 0 blocking errors, 0 warnings
- [x] GATE W — reproduced locally: 20/20 checked, 20/20 clean
- [x] beat_lint — clean
- [ ] GATE B — needs the render
- [ ] Local render, 4K master, 9:16 short — not yet run
