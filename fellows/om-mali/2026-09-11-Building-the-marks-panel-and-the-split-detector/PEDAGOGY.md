# PEDAGOGY — building-the-marks-panel-and-the-split-detector (week 7)
*Building the Marks Panel and the Split Detector — Week 7 progress update · ai-explainer / claude-hai*

Sixth episode of the Private AI Valuation Agent series. Same chassis, same channel, same
persistent voice as weeks 1, 2, 4, 5 and 6. Source: `narration_script.md` (458 spoken words,
author-written, 3:00 target) plus `README.md`'s figure-to-beat map.

**The spine of this episode is the author's own bug.** A tolerance window that was too narrow
to catch the case it was written for, and that looked correct only because a second case
happened to land inside it. The cut is built so that the bug is measured on screen rather than
confessed in a sentence.

---

## Act structure audit

| Beat | Act | Check |
|------|-----|-------|
| B00 | COLD OPEN | `ClaudeComposerAsk`. Opens on the Claude UI, ask lands **ANSWERED** with three output lines (COLD OPEN LAW). Carries the requested self-introduction: "Hi, I'm Om Mali. This video is about…" ✓ |
| B01 | EXECUTIVE SUMMARY | The BLUF: the arithmetic is one line, the detector is the week, and the detector cannot decide ✓ |
| B02 | THE PANEL | Where all 5,479 marks came from, and the subtraction that leaves nothing out ✓ |
| B03 | WHY IT MATTERS | The stakes: a split and a crash are the same shape ✓ |
| B04 | TOO NARROW | The bug, measured — the window and the miss on one number line ✓ |
| B05 | THE EVIDENCE | What the ratio cannot tell you and the share count can ✓ |
| B06 | WHO DECIDED | The rule, each case tested against it, and the name on all three ✓ |
| B07 | RATIO IS NOT FACTOR | The subtlety: measured and decided are different fields ✓ |
| B08 | THE CHECKS | Six pass, one unreachable and says why, none fail ✓ |
| B09 | VERDICT | One-page recap; carries the Week 8 forward statement ✓ |
| B10 | HANDOFF | HANDOFF LAW: a real prompt, read ALOUD verbatim and then discussed ✓ |
| B11 | OUTRO | OUTRO LAW: title restate, `@HumanitariansAI` handle ✓ |

Act order: COLD OPEN → EXECUTIVE SUMMARY → PROVENANCE → STAKES → THE BUG → EVIDENCE →
JUDGMENT → SUBTLETY → VERIFICATION → VERDICT → HANDOFF → OUTRO ✓

**Where this cut departs from the script.** The script has six sections; they become eight
body beats. Each split is a genuine seam:

1. *0:55 carried both the stakes AND the bug* — "a split makes a price look like a crash",
   then the window that missed it. Split into B03 and B04. B03 is why a detector is worth a
   week; B04 is what went wrong with mine. Neither is the other's preamble.
2. *1:35 carried both the evidence AND the judgment* — three share-count comparisons, and then
   "a person made all three calls, with the reason written down". Split into B05 and B06. The
   script's own note calls "catching it is not deciding it" the strongest beat; it cannot be
   the strongest anything while sharing a frame with a three-row table.
3. *0:00 and 0:20 split into B00 and B01/B02* — the standard series bookend structure.

**The script's cut-if-long instruction was NOT needed.** The note offers "It reconciles
exactly" onwards as the first cut. It is kept: the reconciliation is the beat's payoff, and
B02 performs the subtraction on screen rather than asserting it, which is exactly the kind of
claim the note calls "the least visual".

No claim was added or dropped by the splits. Narration was expanded to fit eight body beats at
the 45–70 word budget; every added sentence is connective or judgment, and **every added
FIGURE is injected from `figdata_week7.json` under an assertion.** Four wording changes are
logged in `FACTCHECK.md`.

---

## Cold open + executive summary check

- B00 opens on the Claude UI, never a brand card ✓
- B00's ask lands answered — ASK→RESULT begins at the cold open ✓
- B00 carries the requested opening line: *"Hi, I'm Om Mali. This video is about the price
  panel, turning S E C filings into an actual per share price history for private A I
  companies, and catching the one thing that would have silently ruined it."* ✓
- B01 states the whole result in plain language. No "tolerance", no "quarantine", no "factor"
  until B04–B07 earn them ✓
- The reel does not jump from cold open into a detail beat ✓

---

## ILLUSTRATE LAW audit

| Beat | Visual scheme | UI? |
|---|---|---|
| B00 | ClaudeComposerAsk | UI — the interface IS the subject (cold open) ✓ |
| B01 | `W7Bluf` — a formula at display size, two halves, a struck `decide` chip | illustration ✓ |
| B02 | `W7Panel` — a subtraction ladder, then a split bar and its block reasons | illustration ✓ |
| B03 | `W7Crash` — a drawn price cliff, a struck naive reading | illustration ✓ |
| B04 | `W7Tolerance` — a number line with two windows and a measured gap | illustration ✓ |
| B05 | `W7Evidence` — three filed rows, a bracketed identical value | illustration ✓ |
| B06 | `W7Verdicts` — a two-line rule, three case cards, a signature | illustration ✓ |
| B07 | `W7Factor` — one number decomposing, two divisors judged by outcome | illustration ✓ |
| B08 | `W7Checks` — a seven-row checklist and a cluster breakdown | illustration ✓ |
| B09 | ClaudeVerdictArtifact | UI — the verdict artifact page ✓ |
| B10 | ClaudeComposerAsk | UI — the handoff ✓ |
| B11 | ClaudeTitleOutro | UI — the outro ✓ |

Eight body beats, eight different schemes. No two consecutive body beats share one ✓
Typing appears in exactly two beats — B00 and B10 ✓

**B03 and B04 are adjacent and both about one price step.** B03 is a drawn line falling off a
cliff — the argument is that the shape is indistinguishable, and it is made by *feeling* the
drop. B04 is a number line — the argument is a distance, and it is made by *measuring* it.
Different scheme, different claim.

**B05 and B06 are adjacent and both about the same three companies.** B05 is a data table
whose argument is arithmetic. B06 is a rule plus three verdict cards whose argument is
authorship. One shows what the evidence is; the other shows who is answerable for reading it.

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

This is a competence episode about an incompetence. The risk is either overselling the panel
or turning the bug into a humblebrag, and the cut is built against both.

- **The bug is measured, not confessed.** B04 does not say "I got it wrong"; it draws the
  window, drops the mark outside it, and measures the gap. The viewer reaches the verdict
  before the narration states it ✓
- **The detector is not called broken.** The README's phrasing — too narrow — is used, and the
  beat shows *why* it looked fine: a second case landed on exactly 10.0000, inside any window.
  That is the honest account of how a bad threshold survives ✓
- **The splits are not claimed to be adjusted.** B02 shows the 7 marks blocked "awaiting
  adjustment (Week 8)", B07 closes on Week 8, and B09 repeats it. Nothing in the reel implies
  the price series is clean ✓
- **A mark is defined before it is counted.** B02's subtitle says what one is: a fund's
  recorded price for one security at one period end. Not a valuation of the company ✓
- **The two Perplexity securities are kept apart.** The 11.93 is ARK's common line; the ×10
  share evidence is T. Rowe's preferred line. The script uses "Perplexity" for both; the frames
  name the class, so the viewer is not silently shown two different rows as one ✓
- **The unreachable check is published as unreachable.** It carries its reason on screen, and
  B08's counts are computed from the table rather than typed — the README records the figure's
  title hardcoding "0 fail" and disagreeing with its own rows ✓
- **The ten managers are not claimed to agree exactly.** Two clusters, four thousandths apart,
  stated in the narration. The round number would have been the better soundbite ✓
- **One number in the reel has no artifact behind it**, the old ±0.02 window, and its beat says
  so in its source line rather than citing a file that does not contain it. `FACTCHECK.md`
  row 9 ✓

---

## Length law

**Measured: 214.9s (3:34.9)** across twelve beats, from the Kokoro MP3s. Duration is an OUTPUT.
The script targets 3:00; the four bookends are additive, and the series has run
2:35 → 3:00 → 3:22 → 3:35 → 3:21 → 3:35.

Per-beat narration budget, counted against the final narration (body beats only; bookends
exempt):

B01 67w · B02 48w · B03 55w · B04 69w · B05 59w · B06 56w · B07 68w · B08 54w

**All eight sit inside the 45–70 band.** B05 is the slowest per-word beat in the reel (59 words
over 17.3s) because the script asks for the share counts to be said slowly — the whole
split-versus-repricing argument depends on hearing both halves of "19,395 to 193,950, and the
value did not move".

---

## Both orientations, from one source

As weeks 5 and 6, at the author's standing request: **16:9 (3840×2160) and 9:16 (2160×3840)**.
The vertical cut is a **re-layout, not a crop**. Every week-7 component reads its orientation
from `useVideoConfig()` — B07's decomposition runs across in landscape and downward in
portrait, B05's three-column rows become stacked blocks, B04's number line narrows rather than
squeezing its labels. Both cuts render from the same components and the same props, so a number
cannot differ between them, and they carry the identical narration MP3s.

---

## Source fidelity

Every number traces to `figdata_week7.json` except the one named above — see `FACTCHECK.md`,
20 rows, with rows 9, 12, 18 and 20 flagged as the ones worth challenging.

The five source PNGs and their SVG sources travel with this reel in `pantry/` as REFERENCE for
the rebuild; they are never slotted as media (REBUILD LAW). They were moved there from the
folder root because `run.sh` uses `images/` for compile OUTPUT and the series keeps reference
art in `pantry/`.

## Palette deviation (logged, deliberate)

Identical to weeks 1, 2, 4, 5 and 6: this rebuild renders in the Claude fidelity skin (cream
`#F2F0E9`, ink `#3D3929`, terracotta `#D97757` as the ONE accent) because `ai-explainer` is a
fidelity brand that may not be retinted. **Palette change only — no datum, ordering, or label
altered.**

`README.md` correction 3 records red being misused as a *warning* colour in the source factor
figure, which `DESIGN.md` forbids — red is the primary series, never danger. That fix is
preserved here and applies throughout: terracotta marks the **correct** divisor in B07, the
human-held marks in B02, and the measured result that beat its own expectation in B08. It never
marks a mistake.

---

**What the author is being asked to sign off on**, having watched
`building-the-marks-panel-and-the-split-detector-slate.mp4`:

1. The three structural splits above (6 script sections → 8 body beats), in particular giving
   the bug and the judgment their own beats.
2. Keeping the reconciliation paragraph the script offers as the first cut, and why.
3. The four wording changes logged in `FACTCHECK.md` — in particular "three companies" rather
   than "three", naming the security class on B04 and B05, and adding the two-cluster detail to
   the ten-managers line.
4. `FACTCHECK.md` rows 9, 12, 18 and 20 — the old ±0.02 window having no artifact behind it,
   the "factor of three" that depends on it, the adjudication requirement, and the agreement
   clusters.
5. The B10 handoff prompt, which is new to this cut and is read aloud verbatim.
6. The palette deviation logged above, and the dual-orientation build.

VERDICT: PASS — signed by the author (Om Mali), 2026-09-11.

Audio for the pre-signature review cut was generated with `--no-gate`, recorded here rather
than passed silently; the gate was re-run WITHOUT the override after signing and passes on its
own. Measured runtime 214.52s (3:34.5), identical in both orientations — the two masters carry
the same narration files, not two renderings of the same script.
