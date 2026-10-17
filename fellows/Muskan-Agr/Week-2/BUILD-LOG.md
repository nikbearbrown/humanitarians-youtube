# BUILD-LOG — humanitarians-ai-week2-typography-hero-concepting

## 2026-09-04/05 — authored (Claude, against the brutalist.art-main toolkit)

- HUMAN NOTE (logged first): Muskan Agrawal supplied the Week 2 scope as five
  numbered threads — scope reassessment, typography system refinement
  (hierarchy + contrast/accessibility), hero section exploration, navigation
  audit, footer audit — and asked for the site to be examined directly so the
  claims are backed by images and measurements rather than assertion.
- STANDING INSTRUCTION: the presenter intro must be present verbatim in shape:
  "Hello, I am Muskan Agrawal, and this video is a summary of …". B00 opens
  with exactly that.
- REVIEW CHECKLIST this reel is built against: brutalist format; 4K at source
  AND 4K after YouTube upload; both 16:9 and 9:16 delivered; formatting clean
  on desktop and mobile; intro line present; viewer gains a real takeaway.

## The single most useful number to come out of Week 1

Week 1's SHOTLIST estimated 3:44 using 2.3 words/sec. The finished cut ran
**2:44** — 60 seconds under, and below the brief's own 3-minute floor. Summing
Week 1's `actual_duration_s` against its narration word counts gives the real
figure:

```
475 narration words / 164.57s = 2.89 words per second
```

Week 2's script is written to that number: **655 words → 226.6s (3:47)**,
which sits inside the 3–4 minute target with room at both ends. Per-beat
word/second rates in Week 1 ranged 2.29–3.40, so the true landing zone is
roughly 3:20–4:10; if Kokoro comes in at the fast end this still clears 3:00,
and if it comes in slow there is a spare beat's worth of headroom before 4:00.

## Measurement, not estimation — the method

The brief for this week is about specifics (a scale, a contrast ratio, a line
length), so every figure was taken twice, by two independent methods, and the
reel quotes whichever one is what the viewer actually sees.

1. **Live DOM.** The homepage was opened at an emulated **1503×812** viewport
   — deliberately the exact pixel size of the Week 1 screenshots — and
   interrogated with JavaScript: computed styles for all text, bounding rects
   for geometry, canvas text metrics for characters-per-line, and header/footer
   anchor walks for link inventories.
2. **Screenshot pixels.** PIL + numpy + scipy against the Week 1 assets:
   connected-component labelling on a maroon mask for the buttons, brightness
   thresholding for the video block, ink-column profiling for footer columns.

**They agree, and the disagreement is informative.** The hero media/message
area ratio is 1.91× by DOM and 2.10× by pixels — the DOM measures the bare
`<iframe>`, the pixels measure the rendered block including player chrome.
The reel quotes 2.10× because that is the shape on screen.

**Cross-validation against Week 1.** `BTN_DONATE` reproduces Week 1's
independently-measured Donate box to four decimal places, and
`BTN_ABOUT` ∪ `BTN_CONTACT` reproduces Week 1's combined About/Contact box.
Two people-independent passes, one year of screenshot drift apart, same
numbers. That is the reason to trust the seven boxes that were only measured
once.

## Two corrections to the record

1. **Week 1's B06 crop was wrong, as Week 1 suspected.** SHOTLIST flagged the
   Projects-column crop (0.62, 0.0, 0.92, 0.55) as the one box estimated from
   column ORDER rather than pixels, and asked for it to be checked on the first
   previz. Checked now by ink-column profiling of `06_footer.jpg`: that range
   is px 931–1382, which spans **three** columns — Resources (935–1048),
   Projects (1100–1213) and Legal & Privacy (1264–1354). The correct
   Projects-only range is **0.7319–0.8071**. Week 1 is already published; this
   is logged so the number is right from here on, and Week 2 uses the corrected
   box in B05.

2. **The live site has drifted ~22 px vertically** from the Week 1 captures.
   Live DOM puts the About/Contact buttons at y=681; in the screenshot they sit
   at y≈619–659. Screenshot and live coordinates are therefore NOT
   interchangeable. Every annotation box in this reel was measured from the
   screenshot, because the screenshot is what appears on screen. Anyone
   re-deriving these from the live DOM will get boxes that miss.

## Why some beats are drawn rather than cropped

B06 (the six undecodable project names) is typeset in Manim, not cropped out of
`06_footer.jpg`. The reason is arithmetic: the source screenshots are 1503 px
wide, and the Projects column occupies about 113 px of that. Rendering that
column full-frame at 3840 px is a **~34× upscale** — unreadable mush. A
full-bleed screenshot is only a 2.55× upscale, which is what Week 1 used and
what holds up. So B05 carries the photographic evidence (the real footer, with
the column boxed in maroon) and B06 carries the reading. Same for B04, B08,
B09, B10 and B11: the data is the subject, so the data is drawn. B14 draws
nothing at all — see the revision note below.

## QC reproduced locally before asking for a render

The toolkit's own gate scripts were run against this `scenes.py` in a sandbox
first, so no local render time was spent discovering these:

- **GATE A (`static_scene_check.py`, isolated copy, per class).** Verified the
  exit-code contract in `run.sh` first: rc≥2 aborts the run, rc==1 prints
  "gate A warning" and continues. Week 1 shipped with 4 warnings and 0 errors —
  used as the control.
  - Found one real blocker: **B09 failed rc=2, "shapes never change — 1
    distinct shape-state across 9 frames."** A type-scale ladder made of Text
    plus one static accent bar has no changing shape. Fixed by giving each rung
    a maroon tick square as it lands, which is exactly why Week 1's B08 has
    ticks. Not decoration — a gate requirement.
  - Final: **0 blocking errors, 7 warnings** across 17 scenes. The warnings are
    "text-only scene" (5 cards, same class of warning Week 1 shipped) and
    "coord outside the safe area" on B03/B12, which is inherent to annotating
    the site's own header strip — those boxes genuinely sit 0.12 units from the
    frame edge because the site's nav does.

- **GATE W (`wcag_margin_check.py`).** Week 1 logged this script's internal
  `TypeError` as "ignore it, it's non-blocking". Worth being precise about what
  that costs: when it crashes, `run.sh` prints a warning and continues, and the
  scene is then **never contrast-checked at all**. On the first pass 7 of 17
  scenes crashed it. Two causes, both on our side of the line and both fixable
  without touching the toolkit script:
  - `to_edge(UP, buff=SAFE_BUFF)` — the checker reads `buff` off the AST, gets
    the bare name as a string, and dies on `FRAME_Y - 0.5 - buff`. This is
    exactly the crash Week 1 saw on B08, which uses that same call. Fixed by
    passing the literal `0.6`.
  - `Text(..., font_size=size)` inside a loop — same class of bug, dies on
    `(it.size or 30) >= 36`. Fixed by writing B09's five rungs out with literal
    sizes.
  - Result: **17 of 17 scenes now actually get checked, and all 17 come back
    clean.** The toolkit script is untouched.

- **`beat_lint.py`** on `beat_sheet.json`: clean.

- **GATE B (`manim_layout_audit.py --png --curve-strict`)** cannot be run
  without a real render, so its geometry was pre-computed by hand instead: all
  nine annotation boxes were mapped through `rect_in_image()` at 16:9 and
  confirmed on-frame.

## The chip-placement fix

Week 1 hit two real `layout_audit` errors from hand-placed overlay chips and
fixed them by nudging numbers afterwards. This file computes the placement
instead — and the arithmetic turned up a trap worth recording.

On B12 and B13 the lowest annotation edge sits at y ≈ −2.49, and the bottom
safe-area line is at −3.40. That leaves a clear band of **0.62 units**. A
default chip is taller than that. The obvious implementation — "push the chip
below the box, then clamp it to the safe area" — has the clamp win, which puts
the chip straight back through the box it was supposed to clear, silently.

`chip_below()` therefore fits the chip to the measured band instead of
clamping. At 4K a 0.62-unit band is ~168 px of chip, comfortably legible. If a
band is ever narrower than 0.3 units the helper moves the chip to the top safe
band rather than forcing an overlap.

## Revision — B14, after presenter review

The first draft of B14 drew a "current vs direction" hero wireframe. Muskan
struck it: the site's hero is not to be shown altered, because no redesign has
been settled, and a drawn layout would claim work that has not been done. B14
is now a statement card — order the hero around what a first-time visitor
expects to find first — with no layout on screen. The only hero imagery in the
reel is the unmodified screenshot (B03, B12, B13). Runtime moved 3:50 -> 3:47.

This also closes FACTCHECK row 24, which had been open pending exactly this
confirmation.

## Carried forward from Week 1 — all six fixes verified still in place

1. `runtime/scripts/generate_audio.py` stub present (confirmed on disk).
2. Text weight is the string `"BOLD"` everywhere — never the bare constant.
3. Image loader falls back to a labeled placeholder on FileNotFoundError/OSError
   for GATE A's isolated pre-flight.
4. No `Line()` anywhere in this file — GATE B's TEXT_ON_CURVE check has no
   strikethrough exemption.
5. GATE W's crash is non-blocking; the toolkit script is left alone (and this
   reel now avoids triggering it at all — see above).
6. Overlay chips are placed by computed geometry, not by hand.

## What's NOT done yet (needs Muskan, or needs the render)

- **Sign FACTCHECK.md.** Three rows describe internal project history that no
  measurement can confirm.
- **Confirm the Week 3 handoff.** B15 currently says "WEEK 3 IS THE BUILD."
  That is an assumption from Week 2's shape, not something she has stated.
- **Run the audio + render locally.** See README-RUN-THIS.md.
- **The 9:16 cut.** Week 1's `./art shorts` scaffolded `short/` but rendered
  nothing — `short/manim/` is empty and no vertical master exists anywhere in
  the checkout. The review checklist requires both aspect ratios, so this is an
  open item for Week 1 as well as Week 2.
- **qc-sheet.png** — needs a real render.


## RENDER RESULT — 2026-09-05

Rendered locally, all 17 beats, no intervention needed.

- **Runtime: 3:37.61 (217.61s)** — inside the 3–4 minute target.
- **GATE B: 0 errors, 0 warnings.** `layout_audit.md`: "No text overlaps or
  out-of-frame text detected." The computed chip placement and the pre-checked
  annotation geometry held — no post-hoc nudging was needed, unlike Week 1.
- GATE A / GATE W behaved as predicted from the sandbox run.
- 4K master written to
  `renders/humanitarians-ai-week2-typography-hero-concepting.mp4`.
- B14 rendered from the revised (statement-card) scene, not the withdrawn
  wireframe — confirmed by timestamp.

### Words-per-second calibration, updated

| build | words | seconds | wps |
|---|---|---|---|
| Week 1 | 475 | 164.57 | 2.89 |
| Week 2 | 655 | 217.61 | **3.01** |

Week 2 was estimated at 3:46.6 using Week 1's 2.89 wps and came in 9 seconds
short at 3:37.6, because Kokoro read this script slightly faster (3.01 wps).
Two builds now bracket the pace at **2.89–3.01 wps**.

**For Weeks 3 and 4: plan at 3.0 wps.** For a 3:30 target that is ~630 words;
for 3:45, ~675. Per-beat rates in this build ranged 2.32–3.36, so short beats
still run long relative to the average — the outlier is always the end card.

## Gate status
- [ ] GATE F (FACTCHECK.md) — DRAFT, 3 open rows
- [x] GATE — every on-screen figure measured and cross-validated (this log + SOURCES.md)
- [x] GATE A — reproduced locally: 0 blocking errors, 7 non-blocking warnings
- [x] GATE W — reproduced locally: 17/17 scenes checked, 17/17 clean
- [x] beat_lint — clean
- [x] GATE B — PASSED: 0 errors, 0 warnings
- [x] Local render + 4K master — done, 3:37.61
- [ ] 9:16 short — not yet verified
