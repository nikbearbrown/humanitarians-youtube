# PEDAGOGY — running-full-episodes-from-filings-to-ledger (AI Debt Tracker, week 5)
*Running Full Episodes from Filings to Ledger — Week 5 progress update · ai-explainer / claude-hai*

Sixth episode of the **AI Debt Tracker**. Same chassis, same channel and the same persistent
voice as the eleven Private AI Valuation Agent episodes and the five before this one. Source:
`narration_script.md` (author-written, 2:05–2:15 target, 311 words), `FRICTIONAL.md` and
`figdata.json`.

**The failure mode this reel has to avoid is reporting half a result.** The week's headline
is a system that finally runs end to end and beats doing nothing — and the same run adds
twenty-six bonds that are not there. Recall rose and precision fell, and the two belong on
the same frame, in the same breath, in the cold open and in the verdict. **The build fails if
either half ever stops being true**: if recall stopped rising, or if precision stopped
falling, this would be a different episode and the beats that argue about the trade would be
arguing about nothing.

**The second failure mode is letting the opening ledger disappear.** Every quarter in this
evaluation started from the answer key's own ledger, handed to the tracker and to the
baseline alike. That is what makes the comparison fair, and it is also the largest limit on
every number in the video: the tracker is not reading its own starting point. The script's
own note says so — *don't say the tracker reads the opening ledger, that's next week*. It is
drawn as a BORROWED chip on B02's left-hand panel and accented again as a limit on B08.

**The third is implying any of this was checked by a person.** It was not. The week was
delegated end to end, the diagnosis of the twenty-six wrong additions is Claude reading its
own output, and the gate record says DELEGATED.

---

## Act structure audit

The script has six sections, four of them body. This cut is **twelve beats: four bookends and
eight body beats.** Four structural changes, each listed so the author can accept or reject
them individually.

| # | Change | Why |
|---|---|---|
| 1 | **0:15 splits into B01 (the graph) and B02 (the ledger engine, and where its opening ledger came from).** | The section describes a pipeline and then, in one clause — *applies the rest to the opening ledger* — passes over the fact that the opening ledger was borrowed. That clause is the week's biggest caveat, and a beat that is already drawing five nodes cannot also carry it. B02 exists to put the borrowed start on screen at the same size as the mechanism. |
| 2 | **0:50 splits into B03 (the two metrics) and B04 (the new bonds).** | The section carries a measurement and then the thing the measurement is *about*. "Recall rose seven points" is abstract; "thirty-four were issued, carrying forward finds none, the tracker found thirty" is the claim. Holding both on one frame would make the second a caption under a bar chart. |
| 3 | **1:15 splits into B05 (the 66 additions) and B06 (the timing bug).** | The script runs the breakdown of the wrong additions straight into the timing bug, which is a different kind of error entirely — not a misreading of a document but a bond placed in the wrong quarter. Splitting them lets B05 be a census and B06 be a span, and keeps a process failure from reading as one more category of misread. |
| 4 | **The closing on-camera section becomes B08, a limits beat**, with the gate record and the three next steps inside it. | Every episode in this series ends on its own limits. The gate record — delegated, not cleared — is the largest object on that frame. |

## Cold open + executive summary check

- B00 opens with the required line — *"Hi, I'm Om Mali. This video is about running my AI
  debt tracker end to end, from a quarter's filings to a ledger of every bond the company
  owes…"* — and names the week.
- COLD OPEN LAW: the ask lands **ANSWERED**, with three output lines.
- **The cold open carries the cost.** Its third answer line is the precision fall and the
  twenty-six wrong additions. Nothing is held back for a reveal.
- There is **no separate executive-summary beat.** The three answer lines do that work, as in
  every episode of this series.

## ILLUSTRATE LAW audit

The Claude UI appears at **B00, B09, B10 and B11 only**. Every body beat is a native animated
Remotion scene rebuilt from the data (REBUILD LAW); the four PNGs in `pantry/` are reference
and are never slotted as media.

No two consecutive body beats share a scheme — the full list is in `CHECKS-REPORT.md`. Two
adjacencies needed deliberate work: **B01 and B02** are both about mechanism (B01 is a chain
with a fan-out; B02 has no chain, only two end-state panels with operations between them),
and **B04 and B05** both count things (B04 counts 34 *discrete* cells twice; B05 splits one
*continuous* band of 66 proportionally). The second adjacency is also the argument: what
reading found, immediately followed by what it cost.

## Utility-framing lint

Each body beat answers "what does this let someone do":

```
B01  see what a whole run of the agent actually is, and where the parallelism is
B02  know which half of the system is code, and what it was handed rather than computed
B03  know how the week scored against doing nothing — both directions
B04  know what the metric that rose is measuring: bonds nobody could see before
B05  know what the metric that fell is measuring, bond by bond, with defect ids
B06  know that the first run was wrong, by how much, and why it was a timing error
B07  know whether last week's three pieces hold up on filings nobody had read
B08  know where each number above stops being true, and who has checked it
```

## Honesty check

- **This is a trade, not a win.** Recall 90.9% → 97.8%; precision 92.8% → 90.2%. Both are on
  B00, B03, B08 and B09. The build asserts both directions. FACTCHECK row 4.
- **The opening ledger was borrowed**, for the tracker and the baseline alike. B02's BORROWED
  chip, B08's accented limit. The reel never says the tracker reads its own opening ledger.
  FACTCHECK row 5.
- **The zero is the point of the recall number.** 34 issued, 30 caught, 0 by carrying
  forward — and the 4 it missed are named as still missed. FACTCHECK row 7.
- **Every wrong addition is named.** 10 + 10 + 4 + 2 = 26, with P56, P57 and P58 on the
  frame. FACTCHECK rows 9, 10.
- **The diagnosis is a model judgment.** Claude read each of the 26 after scoring; the
  narration says "by Claude, not by me". FACTCHECK rows 12, 26.
- **No defect id is invented.** The two plain misreads have none in `FRICTIONAL.md` and get
  none on the frame; `figdata.json` records the absence. FACTCHECK row 25.
- **Both runs of the timing fix are reported**, 89.2% and 90.2%, at the same size on the same
  frame — and the fix is partial, because filing date still stands in for settlement date.
  FACTCHECK rows 14, 15.
- **Triage passing is said with last week's failure attached**, and 15 positives is named as
  a small check. FACTCHECK rows 16, 17.
- **The reader is still not the most accurate thing measured.** 91% against a single model
  call's 96%, with that call's 15 invented instruments beside it. FACTCHECK rows 18, 19.
- **The answer key is 3 of 4 gradable, of 5 drawn**, and the draw had to be extended because
  only 2 of 25 companies had never been hand-checked. FACTCHECK rows 21, 22.
- **Repayments do not work yet** — 3 of 14. It is the one part of the engine no other frame
  measures, and B08 says so. FACTCHECK row 23.
- **The gate says delegated, not cleared.** Drawn largest on B08, spoken on camera, and in
  the verdict. FACTCHECK row 27.
- **Nothing was spent.** `$0.00`. The narration is Kokoro, local; the tracker's model is local.

## Length law

```
12 beats · 8 body beats at 54–70 words (band 45–72) · 686 words total
body 8 beats = 144.4s   ·   bookends 4 beats = 58.6s
measured master runtime: 3:23.0  (3840x2160 and 2160x3840, 24fps, identical length)
```

The band is the one weeks 2, 3 and 4 settled on. The four bookends this channel requires are
additive, as in every episode of the series.

The script's *"if you run long, drop 'Then it checks its own work'"* note was not needed:
that clause is what makes B02's open-questions figure mean anything, and it stays — but it
moved out of the graph beat and became the ASK operation on B02, where the 53 questions it
produces are standing beside it.

## Both orientations, from one source

Every scene lays itself out natively at 1920×1080 **and** 1080×1920 through
`f(landscape, portrait)`, registered twice in `Root.tsx`. The 9:16 cut is a **re-layout,
never a crop**, and it is built from the same mp3s — `make_vertical.py` copies the audio
rather than regenerating it, so no number can differ between the two masters.

Portrait values are tuned, not inherited. Every bar component here computes the width given
up by the columns that sit *beside* its track separately per orientation, which is week 3's
lesson and the reason week 4 needed no portrait rescale. Two shapes are new in portrait and
have never been laid out before: B01's five-node column and B04's 9-per-row cell grid. The
beats rescaled after reading portrait frames are listed in `BUILD-LOG.md`.

## Source fidelity

- Every on-screen figure is a prop injected from `figdata.json` under assertions.
- **The framing assertion is the trade, in both directions** — `recall_tracker >
  recall_baseline` **and** `precision_tracker < precision_baseline`. Either half alone is a
  different episode and the build refuses to make it.
- **The second argument is asserted the same way**: the baseline must catch exactly zero new
  bonds, and the tracker must catch more than zero and fewer than all of them.
- **A third closes the addition census** — the five drawn segments must sum to 66, and the
  real and wrong groups must too.
- **A fourth holds the timing fix honest**: the first run's precision must be below the fixed
  run's, and the fixed run must be the one every other beat quotes.
- **A fifth keeps the fresh checks from reading as a clean sweep**: the same triage line that
  passes this week must have failed last week, and the direct model call must still read more
  fields than the reader.
- Further assertions hold the graph's arithmetic (174 read + 71 reused = 245 kept), the
  answer key's three denominators (agreed < gradable < drawn), and that exactly one of the
  four ledger operations is the accented one.
- Three claims are not measured in `figdata.json` — the gate record, who produced the labels
  and the diagnosis, and that the opening ledger was deliberately borrowed. Each is a named
  constant and each beat that uses one says on the frame where it came from.

## Palette deviation (logged, deliberate)

The source figures use red `#C8102E` as their primary series, ochre `#C8860E` for the second
category in the stacked bar and for B2, and grey `#545454` for the third. This cut renders in
the Claude fidelity skin (cream `#F2F0E9`, ink `#3D3929`, terracotta `#D97757` as the ONE
accent) because `ai-explainer` is a fidelity brand that may not be retinted. **Palette change
only — no datum, ordering, or label altered.**

Two consequences are worth the author's attention.

1. The figures give the three wrong-addition kinds three different colours; this cut has one
   accent, so **B05 draws all three in terracotta at stepped weights** and the two unnamed
   misreads in grey. The accent therefore means "this is the cost", which is the beat's
   subject, rather than "this one particular cause".
2. On B03 the accent marks **the tracker** on both rows — the subject of the beat, as it is
   everywhere in this series, not the winner. On the precision row the accented bar is the
   *shorter* one. That is deliberate: the fall is drawn rather than captioned. Because an
   accented bar can be misread as the better bar, the legend naming both bars is on the frame
   before either one grows, and both figures are printed.

---

**What the author is being asked to sign off on**, having read this file,
`FACTCHECK.md` and `CHECKS-REPORT.md`:

1. The four structural changes above, in particular **splitting 0:15 into B01 and B02** to
   give the borrowed opening ledger its own frame, and **splitting 1:15 into B05 and B06**.
2. **Putting the cost in the cold open** — B00's third answer line is the precision fall and
   the 26 wrong additions, rather than holding either for a reveal.
3. **Drawing the opening ledger as BORROWED on B02** and accenting it again as the week's
   largest limit on B08, including the sentence that reading it is next week's work.
4. Saying on camera, of the 26 wrong additions, **"every one was checked, by Claude, not by
   me"** — and labelling the diagnosis a model judgment on the frame.
5. **Reporting both runs of the timing bug at the same size**, 89.2% beside 90.2%, and
   stating on the frame that the fix is partial because filing date still stands in for
   settlement date.
6. **Naming the three merge defects on screen (P56, P57, P58)** and showing the two plain
   misreads with **no id**, because `FRICTIONAL.md` gives none.
7. Saying on camera **"repayments barely work — three of fourteen"**, which no figure in the
   author's own set measures.
8. **Drawing the gate record as the largest object on B08**, and saying on camera *"I handed
   the week to Claude and have not reviewed any of it"*.
9. `FACTCHECK.md` rows 3, 4, 5, 7, 9, 12, 14, 18, 21 and 25 — including that **no defect id
   is invented** for the two plain misreads.
10. The B10 handoff prompt, which is new to this cut and is read aloud: *before you score the
    clever version, write the do-nothing baseline, and report every metric that moved —
    including the ones that moved the wrong way.*
11. The greeting **"Jambo, HAI"** (Swahili), the next unused language in the rotation.
12. The palette deviation logged above — in particular that **the shorter terracotta bar on
    B03's second row is the tracker, not a worse baseline** — and the dual-orientation build.

VERDICT: PASS