# PEDAGOGY — measuring-how-private-marks-move-and-propagate (week 8)
*Measuring How Private Marks Move and Propagate — Week 8 progress update · ai-explainer / claude-hai*

Seventh episode of the Private AI Valuation Agent series. Same chassis, same channel, same
persistent voice as weeks 1, 2, 4, 5, 6 and 7. Source: `narration_script.md` (~470 spoken
words, author-written, 3:00 target) plus `README.md`'s figure-to-beat map.

**This is the first episode that measures rather than builds.** For seven weeks the panel was
the deliverable. This week it is the instrument, and every beat is a question asked of it. The
risk that comes with that is over-reading a measurement, so three of the eight body beats
exist to narrow a claim rather than make one.

---

## Act structure audit

| Beat | Act | Check |
|------|-----|-------|
| B00 | COLD OPEN | `ClaudeComposerAsk`. Opens on the Claude UI, ask lands **ANSWERED** with three output lines (COLD OPEN LAW). Carries the requested self-introduction: "Hi, I'm Om Mali. This video is about…" ✓ |
| B01 | EXECUTIVE SUMMARY | The BLUF as a question sheet: four questions, each with the measured answer beside the expectation it beat ✓ |
| B02 | HOW OFTEN | The first finding, and the test of whether it is a finding at all ✓ |
| B03 | ONE NUMBER, USELESS | What the headline conceals ✓ |
| B04 | SAME DATE | The dispersion measurement ✓ |
| B05 | OR A ROUND ARRIVING | The competing reading of B04, shown in one real window ✓ |
| B06 | HOW FAST | The propagation measurement ✓ |
| B07 | WHAT IT IS NOT | The bounds on B06, and a claim the author deleted ✓ |
| B08 | THE GUARDS | What was excluded, and what none of it shows ✓ |
| B09 | VERDICT | One-page recap; carries the Week 9 forward statement ✓ |
| B10 | HANDOFF | HANDOFF LAW: a real prompt, read ALOUD verbatim and then discussed ✓ |
| B11 | OUTRO | OUTRO LAW: title restate, `@HumanitariansAI` handle ✓ |

Act order: COLD OPEN → EXECUTIVE SUMMARY → FINDING → CAVEAT → FINDING → CAVEAT → FINDING →
CAVEAT → LIMITS → VERDICT → HANDOFF → OUTRO ✓

**The structure is deliberately a rhythm.** Three findings, each immediately followed by the
thing that narrows it: 25% followed by the threshold test, the dispersion followed by the
window that reinterprets it, the 30-day lag followed by the calendar that bounds it. A reel
that stacked three findings and then apologised at the end would be a different, worse video.

**Where this cut departs from the script.** The script has seven sections; they become eight
body beats. Each split is a genuine seam:

1. *2:35 carried both the propagation result AND its caveat* — the script's close mentions the
   guards, and `figdata.propagation.caveat` carries two bounds the script does not speak at
   all. Split into B06 and B07, so the measurement and its limits each get a frame.
2. *2:50 carried the guards AND "what none of this shows"* — one beat, B08, but promoted from a
   closing sentence to a full beat, because it is the only place the reel states its own
   limits and a sentence at 2:50 would be heard as sign-off patter.
3. *0:00 and the panel description split into B00 and B01* — the standard series bookends.

No claim was added or dropped by the splits. Narration was expanded to fit eight body beats at
the 45–70 word budget; every added sentence is connective or judgment, and **every added
FIGURE is injected from `figdata_week8.json` under an assertion.** Four wording changes are
logged in `FACTCHECK.md`.

---

## Cold open + executive summary check

- B00 opens on the Claude UI, never a brand card ✓
- B00's ask lands answered — ASK→RESULT begins at the cold open ✓
- B00 carries the requested opening line: *"Hi, I'm Om Mali. This video is about measuring how
  private company share prices actually move, and how a new price spreads from one fund manager
  to the next."* ✓
- B01 states all four results in plain language. No "dispersion", no "propagation", no "p90"
  until B04–B06 earn them ✓
- The reel does not jump from cold open into a detail beat ✓

---

## ILLUSTRATE LAW audit

| Beat | Visual scheme | UI? |
|---|---|---|
| B00 | ClaudeComposerAsk | UI — the interface IS the subject (cold open) ✓ |
| B01 | `W8Bluf` — four question rows, measured answer beside expectation | illustration ✓ |
| B02 | `W8Remark` — a band, a mark outside it, three widenings climbing short | illustration ✓ |
| B03 | `W8ByCompany` — ten bars with their own n, and a rule drawn across them | illustration ✓ |
| B04 | `W8Dispersion` — 130 dots as a field, median and measured p90 | illustration ✓ |
| B05 | `W8Window` — 11 marks, two period-end columns, banded levels, crossings | illustration ✓ |
| B06 | `W8Propagation` — 37 lags, with 15 stacked at the origin | illustration ✓ |
| B07 | `W8Caveat` — two bound cards, a struck claim, two evidence rows | illustration ✓ |
| B08 | `W8Guards` — a subtraction, three zeroes, three limits | illustration ✓ |
| B09 | ClaudeVerdictArtifact | UI — the verdict artifact page ✓ |
| B10 | ClaudeComposerAsk | UI — the handoff ✓ |
| B11 | ClaudeTitleOutro | UI — the outro ✓ |

Eight body beats, eight different schemes. No two consecutive body beats share one ✓
Typing appears in exactly two beats — B00 and B10 ✓

**B04 and B06 are both one-dimensional dot fields and must not read as the same slide.** They
share a primitive deliberately — the same `DotField` draws both — because the point of B06 is
the SHAPE at the origin, and a viewer who learned to read the shape in B04 reads B06 faster.
What differs is what the shape says: B04's mass is spread across the axis and the argument is
its width; B06's mass piles at zero and the argument is that stack. They are also separated by
B05, which is a scatter with joined points and looks like neither.

**B02 and B03 are adjacent and both about the same statistic.** B02 is a single value tested
against a band — one number, one axis. B03 is that number dissolving into ten. One asks "is it
real", the other "is it useful", and those are different questions about the same 25%.

---

## Utility-framing lint

- "is critical for" — NOT PRESENT ✓
- "important to understand" — NOT PRESENT ✓
- "we'll cover" — NOT PRESENT ✓
- "in this video" — NOT PRESENT as a framing device. B00 says "This video is about…" **once**,
  as the author's explicitly requested opening line, and then never again ✓

Style: narration written dash-free per the author's confirmed preference ✓

---

## Honesty check

A measurement episode can go wrong by over-claiming what a number means. The cut is built so
that every finding is followed by its own limit, in the same reel, at the same volume.

- **The 25% is tested before it is believed.** B02 states the way the result could be an
  artifact — the definition of "unchanged" — and then tries three definitions on screen. The
  injection asserts all three stay under the plan's band, so a future data change that broke
  the finding would fail the build rather than ship a weaker version of this beat ✓
- **The dispersion claim is narrowed in the narration, not just in the paperwork.** The script
  says "disagreement is the normal state"; the reel says "different prices on the same date is
  the normal state", and then spends a whole beat on the reading that is not disagreement ✓
- **B05 argues against B04 on purpose.** It is the beat the README asks for, and it is given a
  real window rather than a diagram — 8 managers, 11 marks, with two of them sitting visibly
  *between* the old and new level ✓
- **The propagation number is bounded twice.** The reporting calendar sets a floor, so the lag
  measures observability rather than diligence; and first-to-last is named as the weaker
  statistic, with the reason ✓
- **A claim the author wrote is deleted on screen, with its arithmetic.** "The biggest events
  are the fastest" did not survive: 27 days against 30 on 9 events, and the smaller events
  reach the same period end more often. B07 shows both numbers rather than saying "corrected" ✓
- **The floor is spoken as zero, not as one percent.** The script said OpenAI's 1%; Groq's 0.0%
  is the true floor and is on the chart. Every bar carries its step count so an 11-step 0% is
  not read as equivalent to a 1,812-step 19.8% ✓
- **The reel ends on its limits.** B08 is the last body beat and its final line is "these are
  fund marks, not transactions" — the reel closes on what it cannot say ✓
- **No invented figures on screen.** Every number is a prop injected from `figdata_week8.json`,
  under assertions that fail the build ✓

---

## Length law

**Measured: 225.5s (3:45.5)** across twelve beats, from the Kokoro MP3s. Duration is an OUTPUT.
The script targets 3:00; the four bookends are additive, and the series has run
2:35 → 3:00 → 3:22 → 3:35 → 3:21 → 3:35 → 3:45.

Per-beat narration budget, counted against the final narration (body beats only; bookends
exempt):

B01 57w · B02 62w · B03 67w · B04 64w · B05 67w · B06 49w · B07 54w · B08 53w

**All eight sit inside the 45–70 band.** This is the longest episode in the series, and the
reason is structural rather than verbose: the finding-then-limit rhythm means three beats
(B05, B07, B08) exist to narrow claims made elsewhere. B09 is also the longest verdict in the
series at 98 words, because there are four findings to recap rather than one argument.

---

## Both orientations, from one source

As weeks 5–7, at the author's standing request: **16:9 (3840×2160) and 9:16 (2160×3840)**. The
vertical cut is a **re-layout, not a crop**. Every week-8 component reads its orientation from
`useVideoConfig()` — the dot fields narrow and grow taller, B03's bars shorten while keeping
their labels, B05's two period-end columns stay side by side because the crossing is the
argument and stacking them would destroy it. Both cuts render from the same components and the
same props, so a number cannot differ between them, and they carry the identical narration MP3s.

---

## Source fidelity

Every number traces to `figdata_week8.json` — see `FACTCHECK.md`, 20 rows, with rows 6, 9, 18
and 20 flagged as the ones worth challenging. Row 6 is the only load-bearing value that is a
prior rather than a measurement.

The five source PNGs and their SVG sources travel with this reel in `pantry/` as REFERENCE for
the rebuild; they are never slotted as media (REBUILD LAW). They were moved there from the
folder root because `run.sh` uses `images/` for compile OUTPUT and the series keeps reference
art in `pantry/`.

## Palette deviation (logged, deliberate)

Identical to weeks 1, 2, 4, 5, 6 and 7: this rebuild renders in the Claude fidelity skin (cream
`#F2F0E9`, ink `#3D3929`, terracotta `#D97757` as the ONE accent) because `ai-explainer` is a
fidelity brand that may not be retinted. **Palette change only — no datum, ordering, or label
altered.** The source figures' rule that red is the primary series and never a warning colour
is preserved in effect: terracotta marks the measured result and the subject of each beat —
the 25%, the X.AI bar, the above-p90 groups, the new price level, the zero-day events — and
never a hazard.

---

**What the author is being asked to sign off on**, having watched
`measuring-how-private-marks-move-and-propagate-slate.mp4`:

1. The three structural splits above (7 script sections → 8 body beats), in particular
   promoting the guards and "what none of this shows" from a closing sentence to a full beat.
2. Speaking Groq's 0.0% as the floor where the script said OpenAI's one percent, and putting
   every bar's step count on screen alongside.
3. Narrowing "disagreement is the normal state" to "different prices on the same date is the
   normal state".
4. `FACTCHECK.md` rows 6, 9, 18 and 20 — the plan's 30–40% prior, the by-company floor, the
   window's clustered rather than thresholded levels, and the deleted "biggest events are
   fastest" claim.
5. The B10 handoff prompt, which is new to this cut and is read aloud verbatim.
6. The palette deviation logged above, and the dual-orientation build.

VERDICT: PASS — signed by the author (Om Mali), 2026-09-18.

Audio for the pre-signature review cut was generated with `--no-gate`, recorded here rather
than passed silently; the gate was re-run WITHOUT the override after signing and passes on its
own. Measured runtime 225.11s (3:45.1), identical in both orientations — the two masters carry
the same narration files, not two renderings of the same script.
