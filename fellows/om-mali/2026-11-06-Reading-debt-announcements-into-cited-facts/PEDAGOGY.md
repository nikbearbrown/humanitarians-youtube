# PEDAGOGY — reading-debt-announcements-into-cited-facts (AI Debt Tracker, week 4)
*Reading Debt Announcements into Cited Facts — Week 4 progress update · ai-explainer / claude-hai*

Fifth episode of the **AI Debt Tracker**. Same chassis, same channel and the same persistent
voice as the eleven Private AI Valuation Agent episodes and the four before this one. Source:
`narration_script.md` (author-written, 2:30–2:40 target, 371 words), `FRICTIONAL.md` and
`figdata.json`.

**The failure mode this reel has to avoid is selling the thing that was built.** The week's
headline is a 94% that beat its baseline — and the baseline nobody planned to take seriously,
a single model call typing every value itself, read *every* field right. The reader cannot be
sold on accuracy. It can only be sold on provenance, and that is a narrower claim than the
design expected to be making. **Four separate frames carry 94% and 100% together** (B00, B03,
B04, B09), and the build fails if the reader ever overtakes B2, because then this is a
different episode.

**The second failure mode is burying two failed checks.** Triage scored 8 of 9 against a 95%
line it set itself, and the answer key agreed on 1 of 5. Both are in the cold open, both get
their own body beat, and both are in the verdict.

**The third is implying any of this was checked by a person.** It was not. The week was
delegated end to end and the gate record says so.

---

## Act structure audit

The script has seven sections, five of them body. This cut is **twelve beats: four bookends
and eight body beats.** Four structural changes, each listed so the author can accept or
reject them individually.

| # | Change | Why |
|---|---|---|
| 1 | **0:15 splits into B01 (the three steps) and B02 (the copy check, worked on Alphabet).** | The section describes a mechanism and then, 65 seconds later at 1:20, the script shows the one case that proves the mechanism matters. Those belong together. Holding the Alphabet example until after the result would make it read as an excuse for the result. |
| 2 | **0:45 splits into B03 (the three bars) and B04 (what pointing actually buys).** | The section carries two arguments: *here is the comparison*, and *here is why the comparison does not mean what you would assume*. One frame holding both makes the second a caption. B04 exists to draw the same value twice — cited and uncited — because that, and not the percentage, is the week's actual product. |
| 3 | **1:20's tally becomes its own beat, B05.** | The Alphabet case is one refusal; 24 of 254 is the shape of the problem. Splitting them lets B02 be a document and B05 be a count, and keeps a worked example from standing in for a measurement. |
| 4 | **The closing on-camera section becomes B08, a limits beat**, with the gate record and the three next steps inside it. | Every episode in this series ends on its own limits. The gate record — delegated, not cleared — is the largest object on that frame. |

## Cold open + executive summary check

- B00 opens with the required line — *"Hi, I'm Om Mali. This video is about teaching my AI
  debt tracker to read a debt announcement into structured facts…"* — and names the week.
- COLD OPEN LAW: the ask lands **ANSWERED**, with three output lines.
- **The cold open carries the bad news.** Its second answer line is B2's 160 of 160 and its
  third is the failed triage check. Nothing is held back for a reveal.
- There is **no separate executive-summary beat.** The three answer lines do that work.

## ILLUSTRATE LAW audit

The Claude UI appears at **B00, B09, B10 and B11 only**. Every body beat is a native animated
Remotion scene rebuilt from the data (REBUILD LAW); the four PNGs in `pantry/` are reference
and are never slotted as media.

No two consecutive body beats share a scheme — the full list is in `CHECKS-REPORT.md`. Two
adjacencies needed deliberate work and neither is adjacent in the end: **B03 and B06** are
both bar beats (B03's three bars have three denominators and no threshold; B06's two share
one threshold fixed before the run), and **B05 and B07** are both cell beats (B05's 24 cells
are interchangeable refusals; B07's five each stand for a named report).

## Utility-framing lint

Each body beat answers "what does this let someone do":

```
B01  know where the model is allowed to act, and where it is not
B02  know what the copy check is for, from the one case that proves it
B03  know which of three methods read the filings best — and on what denominator
B04  know what the reader actually buys, which is not accuracy
B05  know how much the copy check refused, and how much of that was a real bug
B06  know that a check the project set itself was failed, and by how much
B07  know what is still wrong with the answer key, by company and defect id
B08  know where each number above stops being true, and who has checked it
```

## Honesty check

- **The reader is not more accurate.** It beat B1, which was the week's check, and B2 read
  160 of 160. On B00, B03, B04, B09. FACTCHECK row 2.
- **The three bars do not share a denominator** — 157/167, 135/160, 160/160 — and every row
  prints its own. FACTCHECK row 4.
- **The reader invents the most.** 29 instruments the filings do not announce, against B2's 9
  and B1's 1. Asserted, so a frame cannot show the accuracy without the cost. FACTCHECK row 5.
- **The set is mostly easy.** 62 of 66 instruments were new notes in pricing documents, which
  is also why B2 did so well. B08's first limit. FACTCHECK row 8.
- **The fresh triage check failed.** 8 of 9, below a 95% line fixed before the run, on only 9
  positives. Said on camera in those words. FACTCHECK rows 14, 15, 17.
- **The answer key agreed on 1 of 5**, and last week's 3 of 3 is named as a calibration on the
  same frame. FACTCHECK row 19.
- **The hand-check slip is on the frame**, not only in the description. FACTCHECK row 22.
- **The labels are a model's judgment.** Claude read each filing; a machine check confirms 51
  of 51 bonds against the next quarterly report, and no person has read them. The reel never
  says "I labelled". FACTCHECK rows 23, 24.
- **The gate says delegated, not cleared.** Drawn largest on B08, spoken on camera, and in the
  verdict. FACTCHECK row 26.
- **No defect id is invented.** `FRICTIONAL.md` gives ids for P41–P46 and none for the three
  open reader defects; the reel shows none for them. FACTCHECK row 25.
- **Nothing was spent.** `$0.00`. The narration is Kokoro, local; the reader model is local.

## Length law

```
12 beats · 8 body beats at 54–71 words (band 45–72) · 698 words total
body 8 beats = 143.9s   ·   bookends 4 beats = 58.2s
measured master runtime: 3:22.1  (3840x2160 and 2160x3840, 24fps, identical length)
```

The band is the one weeks 2 and 3 settled on. The four bookends this channel requires are
additive, as in every episode of the series.

The script's *"if you run long, drop 'On clean pricing documents, a small model reads numbers
well'"* note was not needed: that sentence moved from the result beat to B04, where it is the
explanation for why pointing bought no accuracy rather than an aside. The optional *"the rest
were the model writing the word null"* is kept, on B05.

## Both orientations, from one source

Every scene lays itself out natively at 1920×1080 **and** 1080×1920 through
`f(landscape, portrait)`, registered twice in `Root.tsx`. The 9:16 cut is a **re-layout, never
a crop**, and it is built from the same mp3s — `make_vertical.py` copies the audio rather than
regenerating it, so no number can differ between the two masters.

Portrait values are tuned, not inherited. The chassis arrives with week 3's portrait values
and with week 3's lesson built in: any row that puts a value *beside* a track must subtract
that value column from the track width in portrait too. The beats rescaled after reading
portrait frames are listed in `BUILD-LOG.md`.

## Source fidelity

- Every on-screen figure is a prop injected from `figdata.json` under assertions.
- **The framing assertion is `B2_SHARE > READER_SHARE`.** If the reader ever overtook the
  baseline that types its own numbers, B03 and B04 would be arguing about something that no
  longer exists, and the build fails rather than let the episode become a victory lap.
- **The second argument is asserted the same way**: the fresh triage score must stay *below*
  the pass line while last week's set stays above it.
- **A third holds the reader's own cost**: its extras must stay the largest of the three.
- **A fourth closes the refusal tally** both ways — 8 + 16 = 24, and 227 + 3 + 24 = every copy
  made.
- Further assertions hold the composition (62 + 4 = 66), the answer key (1 of 5 below 3 of 3,
  four defects in four distinct companies), and that the € is in the filing and the $ in the
  copy — B02 is one character wide and the build checks the character is there.
- Three claims are not measured in `figdata.json` — the gate record, who did the labelling,
  and that the check and pass line were fixed in week 1. Each is a named constant and each
  beat that uses one says on the frame where it came from.

## Palette deviation (logged, deliberate)

The source figures use red `#C8102E` as their primary series with ochre `#C8860E` for the B2
baseline and the second grounding bar. This cut renders in the Claude fidelity skin (cream
`#F2F0E9`, ink `#3D3929`, terracotta `#D97757` as the ONE accent) because `ai-explainer` is a
fidelity brand that may not be retinted. **Palette change only — no datum, ordering, or label
altered.**

One consequence is worth the author's attention. The figures give B2 its own colour; this cut
has one accent, so **B2's bar is drawn in ink and the reader's in terracotta** — the accent
marks the subject of the beat, as it does everywhere in this series, not the winner. Because
an accented bar can be misread as the best bar, B03 prints all three fractions, states the
result in a sentence beneath the bars, and is followed immediately by B04, whose whole job is
to say what the accented bar does and does not buy.

---

**What the author is being asked to sign off on**, having read this file,
`FACTCHECK.md` and `CHECKS-REPORT.md`:

1. The four structural changes above, in particular **splitting 0:45 into B03 and B04** and
   **adding B08**.
2. **Putting the bad news in the cold open** — B00's answer lines include B2's 160 of 160 and
   the failed triage check, rather than holding either for a reveal.
3. Saying on camera, of triage, **"that is a failed check and I am not dressing it up"**.
4. **Drawing the gate record as the largest object on B08**, and saying on camera *"I handed
   the whole week to Claude and have not reviewed any of it"*.
5. **Disclosing the hand-check slip on the frame** — the key's totals for the five reports
   were printed once before the transcriptions were written.
6. **Naming the four answer-key defects on screen** with their companies and ids (P41–P44),
   and naming P45 and P46 on B06.
7. `FACTCHECK.md` rows 2, 4, 5, 8, 15, 17, 22, 25 and 26 — including that **no defect id is
   invented** for the three open reader defects, because the source gives none.
8. The B10 handoff prompt, which is new to this cut and is read aloud verbatim: *run the
   dumbest baseline that could work before you build the clever version.*
9. The greeting **"Merhaba, HAI"** (Turkish), the next unused language in the rotation.
10. The palette deviation logged above — in particular that **the terracotta bar on B03 is the
    reader, not the winner** — and the dual-orientation build.

VERDICT: PASS Om Mali 11/06/2026