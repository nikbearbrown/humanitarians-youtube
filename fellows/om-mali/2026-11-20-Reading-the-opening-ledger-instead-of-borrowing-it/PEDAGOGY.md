# PEDAGOGY — reading-the-opening-ledger-instead-of-borrowing-it (AI Debt Tracker, week 6)
*Reading the Opening Ledger Instead of Borrowing It — Week 6 progress update · ai-explainer / claude-hai*

Seventh episode of the **AI Debt Tracker**. Same chassis, same channel and the same persistent
voice as the eleven Private AI Valuation Agent episodes and the six before this one. Source:
`narration_script.md` (author-written, 2:00–2:15 target, 305 words), `FRICTIONAL.md` and
`figdata.json`.

**The failure mode this reel has to avoid is softening a retraction.** Week 5's headline was
that the tracker beat doing nothing by seven points of recall. That number rested on every
quarter being handed an opening ledger copied from the answer key. This week the tracker
reads that ledger itself, recall falls 7.9 points to 90.1%, and the do-nothing baseline sits
at 90.9%. **The advantage was the crutch.** That sentence is in the cold open, on B05, and in
the verdict, and the build fails if agent start ever pulls ahead of B0 on recall.

**The second failure mode is reporting only the half that fell.** Precision moved the other
way — 93.3% to 95.5%, ahead of both the borrowed start and the baseline — because a ledger
holding fewer bonds holds fewer wrong ones. A reel that showed only the recall fall would be
describing a failure, and this is a trade. Both halves are on B05, on the same scale.

**The third is implying any of this was checked by a person.** It was not. The week was
delegated end to end, which rows of a table are instruments is `qwen3:4b`'s judgment, the
hand-check transcriptions are a model's reading, and the gate record says DELEGATED.

---

## Act structure audit

The script has six sections, five of them body. This cut is **twelve beats: four bookends and
eight body beats.** Four structural changes, each listed so the author can accept or reject
them individually.

| # | Change | Why |
|---|---|---|
| 1 | **0:45 splits into B02 (the reader's mechanism) and B03 (what it scored).** | The section builds a new component and then grades it, in one breath. The mechanism is the part that carries the project's oldest rule — the model never types a number — and the score is the part with two denominators that need separating. One frame holding both would make the mechanism a caption under a bar chart. |
| 2 | **The non-determinism gets its own beat, B04.** | The script gives it one clause — *"the model's pointing also changes from run to run"* — and lists it as droppable if the cut runs long. It is the only fact in the week that tells a viewer how much to trust every other number in it: 36 bonds on one ask, 22 on the next, same report. Promoting it from a clause to a beat is the biggest single judgment call in this cut and the one most worth rejecting if you disagree. |
| 3 | **1:20 splits into B05 (the three-way check) and B06 (where the gap actually sits).** | The section states a cost and then immediately qualifies it as concentrated in a few companies. Those are different claims — one is a measurement, one is a diagnosis — and the diagnosis is what makes the cost fixable rather than damning. B06 also separates the three misses from the one refusal, which is not a miss. |
| 4 | **The closing on-camera section becomes B08, a limits beat**, with the gate record and the three next steps inside it. | Every episode in this series ends on its own limits. Total debt is accented there because it is the one number the week made worse and the only one no other frame shows. |

## Cold open + executive summary check

- B00 opens with the required line — *"Hi, I'm Om Mali. This video is about my AI debt
  tracker reading its own starting ledger from a company's last report, instead of borrowing
  it from the answer key…"* — and names the week.
- COLD OPEN LAW: the ask lands **ANSWERED**, with three output lines.
- **The cold open carries the retraction.** Its third answer line is the cost and the word
  LEVEL. Nothing is held for a reveal.
- There is **no separate executive-summary beat.** The three answer lines do that work, as in
  every episode of this series.

## ILLUSTRATE LAW audit

The Claude UI appears at **B00, B09, B10 and B11 only**. Every body beat is a native animated
Remotion scene rebuilt from the data (REBUILD LAW); the four PNGs in `pantry/` are reference
and are never slotted as media.

No two consecutive body beats share a scheme — the full list is in `CHECKS-REPORT.md`. The
reel has three bar beats and they are deliberately different objects: B01 is a *count* scale
with two bars and no percentages, B03 is two *pairs* where the subject is the distance inside
each pair, and B05 is three *rows* per metric where the subject is two bars ending level.
None of the three is adjacent to another.

## Utility-framing lint

Each body beat answers "what does this let someone do":

```
B01  know that last week's wrong additions are gone, and what it cost to fix them
B02  know how the opening ledger is now produced, and who does which part
B03  know what that reader is worth against rules alone — and on what denominator
B04  know how much to trust any single number the reader produced
B05  know what the borrowed start was worth, which is the whole of last week's claim
B06  know whether the cost is a general weakness or a few hard tables
B07  know whether the system can tell when it has got a quarter wrong
B08  know where each number above stops being true, and who has checked it
```

## Honesty check

- **Removing the crutch removes last week's claim.** Agent start 90.1% against B0's 90.9% —
  level, not ahead. On B00, B05, B08 and B09, and asserted both ways. FACTCHECK row 14.
- **The trade has two halves.** Precision rose to 95.5%, ahead of both. Asserted, so no frame
  can show the fall without the rise. FACTCHECK row 15.
- **93.3% is level with 92.8%, not better.** The paired interval straddles zero and the build
  holds the gap under a point. FACTCHECK row 3.
- **The reader's percentages belong to 43 reports, not 94.** Your own figure's source line
  says so; the README is looser. Both denominators are on the frame. FACTCHECK row 8.
- **The model adds recall, not precision** — +5.9 points against +0.9. Both gaps printed.
  FACTCHECK row 10.
- **The reader is not deterministic.** 36 bonds then 22, same report. Its own beat.
  FACTCHECK row 12.
- **The refusal is not a miss.** Core Scientific's reports were withheld by the point-in-time
  rule; B06 draws that apart from the three real misses. FACTCHECK row 17.
- **The checks catch a third.** 17 of 50, with 11 false flags out of 36. FACTCHECK row 18.
- **The investigators changed nothing.** 21 of 67 settled, no graded bond moved, 24 maturity
  questions still open. FACTCHECK rows 19, 21.
- **Total debt got worse.** Within 2% on 26 of 79, down from 44. Accented on B08.
  FACTCHECK row 20.
- **The judgments are a model's.** Which rows are instruments, and the hand-check
  transcriptions. The reel never says "I transcribed". FACTCHECK row 26.
- **The gate says delegated, not cleared**, and the review is open for weeks 3 to 6.
  FACTCHECK row 28.
- **Nothing was spent.** `$0.00`. The narration is Kokoro, local; the reader model is local.

## Length law

```
12 beats · 8 body beats at 57–65 words (band 45–72) · 692 words total
body 8 beats = 145.3s   ·   bookends 4 beats = 61.1s
measured master runtime: 3:26.4  (3840x2160 and 2160x3840, 24fps, identical length)
```

The band is the one weeks 2–5 settled on. The four bookends this channel requires are
additive, as in every episode of the series.

The script's *"if you run long, drop 'That's cheating a little' and 'The model's pointing
also changes from run to run'"* note was not taken. The first is kept because naming the
borrowed start as deliberate is what stops it reading as an accident; the second is kept and
promoted to its own beat, for the reason in structural change 2.

## Both orientations, from one source

Every scene lays itself out natively at 1920×1080 **and** 1080×1920 through
`f(landscape, portrait)`, registered twice in `Root.tsx`. The 9:16 cut is a **re-layout,
never a crop**, and it is built from the same mp3s — `make_vertical.py` copies the audio
rather than regenerating it, so no number can differ between the two masters.

Portrait values are tuned, not inherited. Two lessons arrive built in: week 3's (any row
putting a value beside a track must subtract that column in portrait too) and week 5's (an
over-full portrait column leaves `space-between` nothing to distribute, and the footnote rule
then draws through the line above it). Portrait type on B06, B07 and B08 is budgeted down
rather than inherited. The beats rescaled after reading portrait frames are listed in
`BUILD-LOG.md`.

## Source fidelity

- Every on-screen figure is a prop injected from `figdata.json` under assertions.
- **The framing assertion has two halves** — oracle start must beat B0 on recall, **and**
  agent start must not. If the agent ever pulled ahead of doing nothing on recall, B00 and
  B05 would be announcing a cost that did not land.
- **The second argument is asserted the same way**: agent-start precision must be ahead of
  both the borrowed start and B0.
- **A third holds the merge result level** — the gain over B0 must stay under a point, so the
  frame has to say "level".
- **A fourth holds the reader's claim** — the recall gain over rules-only must exceed the
  precision gain, and the graded denominator must stay smaller than the read one.
- **A fifth holds the variance beat** — the two asks must give two different counts.
- Further assertions hold that 21+25+4 can never be relabelled as the 26, that the checks
  miss more wrong episodes than they catch, and that the four named companies stay four
  distinct names.
- Three claims are not measured in `figdata.json` — the gate record, whose judgment produced
  the row labels, and that the borrowed start was a deliberate ablation. Each is a named
  constant and each beat that uses one says on the frame where it came from.

## One conflict in your own files, flagged not resolved

`FRICTIONAL.md` breaks the 21 settled questions down as **19 + 2**; `description.txt` as
**17 + 2 + 2**. Both total 21. I have not guessed: **no breakdown appears on any frame.** B07
shows the 21, that most were bonds the ledger already held, and that no graded bond changed —
all true under either version. `FACTCHECK.md` row 22 records it. Tell me which is right and
it goes on the frame.

## Palette deviation (logged, deliberate)

The source figures use red `#C8102E` as their primary series, with ochre `#C8860E` for the
false-flag bar and grey `#545454` for B0. This cut renders in the Claude fidelity skin (cream
`#F2F0E9`, ink `#3D3929`, terracotta `#D97757` as the ONE accent) because `ai-explainer` is a
fidelity brand that may not be retinted. **Palette change only — no datum, ordering, or label
altered.**

Two consequences are worth the author's attention.

1. The figures give B0 its own grey; this cut has one accent, so **B0 is drawn in a softer
   ink than the oracle rows** rather than in a third colour. On B05 the accent marks the
   *agent start* — the subject of the beat — and on the precision rows the accented bar is
   the longest one while on the recall rows it is not. That asymmetry is the week.
2. On B01 the accent marks **the three wrong additions that remain**, not the improvement.
   The short bar is the accented one. It reads correctly as "this is what is left", but it
   is the opposite of the usual "accent = the good number" convention, so it is flagged.

---

**What the author is being asked to sign off on**, having read this file,
`FACTCHECK.md` and `CHECKS-REPORT.md`:

1. The four structural changes above, in particular **promoting the run-to-run variance from
   a droppable clause to its own beat (B04)** and **splitting 1:20 into the check and the
   diagnosis**.
2. **Putting the retraction in the cold open** — B00's third answer line says reading its own
   start leaves the tracker LEVEL with doing nothing on recall, which undoes week 5's
   headline.
3. Saying on camera, of the merge result, **"level with doing nothing, not better than it"**.
4. **Printing both denominators for the opening reader** — 94 reports read, 43 graded — and
   saying "graded on the forty-three the answer key covers" on camera.
5. **Giving the non-determinism a whole beat**: 36 bonds on one ask, 22 on the next, with
   "I'm reporting it rather than averaging it away" said aloud.
6. **Drawing Core Scientific's refusal apart from the three misses**, as the point-in-time
   rule working rather than a defect.
7. Saying on camera **"the checks notice seventeen times out of fifty"** and that the
   investigators **"changed no graded bond"**.
8. **Accenting total debt on B08** — within 2% on 26 of 79, down from 44 — as the weakest
   number in the week, since your script marks it "not said aloud".
9. **Drawing the gate record as the largest object on B08**, and saying on camera *"nobody
   has reviewed any of it"*.
10. `FACTCHECK.md` rows 3, 4, 5, 8, 10, 12, 14, 17, 20 and 22 — **row 22 is the conflict
    between `FRICTIONAL.md` and `description.txt` and needs your answer.**
11. The B10 handoff prompt, which is new to this cut and is read aloud: *find every place
    your evaluation hands the system something it would have to produce for itself, take the
    biggest one away, and re-run.*
12. The greeting **"Bula, HAI"** (Fijian), the next unused language in the rotation.
13. The palette deviation logged above — in particular that **the accented bar on B01 is the
    three that are left, not the improvement** — and the dual-orientation build.

VERDICT: PASS