# PEDAGOGY — building-the-filing-timeline-triage-and-document-server (AI Debt Tracker, week 3)
*Building the Filing Timeline, Triage and Document Server — Week 3 progress update · ai-explainer / claude-hai*

Fourth episode of the **AI Debt Tracker**. Same chassis, same channel and the same persistent
voice as the eleven Private AI Valuation Agent episodes and the three before this one. Source:
`narration_script.md` (author-written, 3:00 target, 441 words) and `figdata.json`.

**The failure mode this reel has to avoid is the perfect score.** It contains three of them —
*3 of 3*, *24 of 24*, *22 of 22* — and each is true and each means less than it sounds. The
first is a calibration on reports the fixes were made against. The second is recall on 24
positives inside a 50-filing sample, with precision at 24 of 26 and the event type right 20
times in 24. Every one of them is drawn with the thing that qualifies it as the larger object
on the frame.

**The second failure mode is sounding like the agent reads filings.** It does not. This week
built what *finds* the filings and what lets a future reader *point into* them. B00 says so,
B04's footnote says so, and B08's last row says so again.

---

## Act structure audit

The script has eight sections. This cut is **twelve beats: four bookends and eight body
beats.** Five structural changes, each listed so the author can accept or reject them
individually.

| # | Change | Why |
|---|---|---|
| 1 | **0:15 splits into B01 (the two scores) and B02 (the three named reports).** | At ~95 spoken words it is the longest section and it carries two arguments: *which of these scores is evidence*, and *what specifically is still wrong*. One frame holding both makes the named defects a caption on a bar chart. |
| 2 | **"Two of them had no debt on either side" is moved ahead of the fraction.** | The script's Notes carry the exclusion but its body states "of the three that had any debt" after the fact. Said first, the denominator can never be heard as 5 — and the two excluded reports are drawn on the frame rather than dropped. |
| 3 | **The optional line "and one reading mistake was mine" is kept.** | The script offers it "if you have time". It costs two seconds and removes an asymmetry in which only the answer key's mistakes get named. FACTCHECK row 7. |
| 4 | **The two false alarms are named on the frame rather than left inside "precision 24 of 26".** | A denominator is a number; a tender offer for Alphabet shares is a thing a viewer can judge. The build asserts the two named alarms are exactly the 26 − 24 gap. |
| 5 | **The closing on-camera section becomes B08, a limits beat**, with the three next steps inside it. | Every episode in this series ends on its own limits, and the limits live in the script's Notes, which otherwise reach no frame. |

## Cold open + executive summary check

- B00 opens with the required line — *"Hi, I'm Om Mali. This video is about teaching my AI
  debt tracker to find the debt news in SEC filings…"* — and names the week, the three pieces
  built, and the fact that the agent still cannot read a filing.
- COLD OPEN LAW: the ask lands **ANSWERED**, with three output lines that are the three
  findings (the funnel, the check including what it got wrong, the fresh answer-key score).
- The ask is the week's real instruction: *find the news, and prove nothing was thrown away.*
- There is **no separate executive-summary beat.** The three answer lines do that work.

## ILLUSTRATE LAW audit

The Claude UI appears at **B00, B09, B10 and B11 only**. Every body beat is a native animated
Remotion scene rebuilt from the data (REBUILD LAW); the four PNGs in `pantry/` are reference
and are never slotted as media.

No two consecutive body beats share a scheme — the full list is in `CHECKS-REPORT.md`. The
adjacency that needed deliberate work is B04/B05, both horizontal bars: **B04 keeps the full
593 outline on every row**, so each stage reads as a slice of one narrowing population and
carries no pass line at all; **B05's four bars have four different denominators** and share one
mark that was written down before the check ran.

## Utility-framing lint

Each body beat answers "what does this let someone do":

```
B01  know which of last week's two scores is evidence
B02  know exactly what is still wrong, by name and by defect id
B03  know what the agent is allowed to look at, and when the window shuts
B04  know how little of this is a model, and how much is five plain rules
B05  know whether the filter loses anything — and what it wrongly keeps
B06  know what broke, and what each failure changed
B07  know why the agent will never have to retype a number
B08  know where each number above stops being true
```

## Honesty check

- **The agent still cannot read a filing into structured events.** B00, B04's footnote, B08.
- **3 of 3 is a calibration**, on the reports last week's fixes were made against. The measured
  number is 1 of 3, and the 2 drawn reports with nothing to grade are drawn as excluded rather
  than counted as agreements. FACTCHECK rows 1 and 3.
- **Two answer-key defects are left open on purpose.** Fixing them against the reports that
  found them would turn next week's check into another calibration. They carry ids on screen.
- **One reading mistake in the hand-check was the author's own**, said on camera.
- **24 of 24 is recall**, on 24 positives in a 50-filing sample. Precision 24 of 26, event type
  20 of 24, both on the same scale directly beneath it. FACTCHECK rows 13–14.
- **The labels are a model's judgment**, made by Claude before triage ran — a different model
  from the one tested, but not a person. The reel never says "I labelled". FACTCHECK row 16.
- **The model decides a third of triage, not all of it.** Five plain rules settle 394 of 593.
- **A non-verbatim quote is not an invention.** 8 of 21; the reel says what the check actually
  compares and keeps the filing. FACTCHECK row 19.
- **Nothing was spent.** `$0.00`. The narration is Kokoro, local; the triage model is local.

## Length law

```
12 beats · 8 body beats at 54–70 words (band 45–72) · 704 words total
body 8 beats = 144.7s   ·   bookends 4 beats = 60.8s
measured master runtime: 3:25.4  (3840x2160 and 2160x3840, 24fps, identical length)
```

The band is the one week 2 settled on. This script speaks its large numbers aloud — "five
hundred and ninety three", "twenty four of twenty four" — and one figure can cost six words.
The four bookends this channel requires are additive, as in every episode of the series.

## Both orientations, from one source

Every scene lays itself out natively at 1920×1080 **and** 1080×1920 through
`f(landscape, portrait)`, registered twice in `Root.tsx`. The 9:16 cut is a **re-layout, never
a crop**, and it is built from the same mp3s — `make_vertical.py` copies the audio rather than
regenerating it, so no number can differ between the two masters.

Portrait values are tuned, not inherited. The chassis arrives with week 2's portrait values
already raised; the beats rescaled after reading portrait frames are listed in `BUILD-LOG.md`.

## Source fidelity

- Every on-screen figure is a prop injected from `figdata.json` under assertions.
- **The framing assertion is `FRESH_SHARE < LAST_WEEK_SHARE`.** If the fresh answer-key score
  ever caught up with the calibrated one, B01 would be drawing a distinction that no longer
  exists, and the build fails rather than advertise a recovered answer key.
- **The second argument is asserted the same way**: recall must stay perfect *while* precision
  and the event type stay below it.
- **A third assertion ties the named false alarms to the precision denominator** — the two
  things B05 names must be exactly the gap between 24 found and 26 kept.
- Further assertions hold the composition (469 + 94 + 30 = 593), the funnel (394 + 199 = 593,
  163 + 21 = 184), the draw (3 + 2 = 5), and that every failure in B06 carries a consequence.
- Three claims are not measured in `figdata.json` — that the agent is unbuilt, who labelled the
  sample, and the author's own transcription error. Each is a named constant and each beat that
  uses one says on the frame where it came from.

## Palette deviation (logged, deliberate)

The source figures use red `#C8102E` as their primary series with ochre `#C8860E` for the
model stage. This cut renders in the Claude fidelity skin (cream `#F2F0E9`, ink `#3D3929`,
terracotta `#D97757` as the ONE accent) because `ai-explainer` is a fidelity brand that may not
be retinted. **Palette change only — no datum, ordering, or label altered.** The figures' rule
that red is the primary series and never a warning colour is preserved in effect: terracotta
marks the fresh score, the two open defects, the cut-off, the model's share of the funnel, the
recall bar, what changed after each failure, the cited sentence and the refusal — the subject
of each beat, never a hazard.

---

**What the author is being asked to sign off on**, having read this file,
`FACTCHECK.md` and `CHECKS-REPORT.md`:

1. The five structural changes above, in particular **adding B08** and **splitting 0:15 into
   B01 and B02**.
2. **Saying the exclusion before the fraction** — "two of them had no debt on either side" —
   and drawing those two reports on the frame as an excluded tail.
3. Keeping the script's optional line **"and one reading mistake was mine"**.
4. Saying on camera that **3 of 3 is a calibration**, and putting that sentence on B01's frame.
5. **Naming the two false alarms** on screen rather than leaving them inside a denominator.
6. Saying on camera, twice, that **the agent still cannot read a filing**.
7. `FACTCHECK.md` rows 2, 7, 9 and 16 — the claims `figdata.json` does not measure, including
   that the 50 labels are Claude's judgment and not a person's.
8. The B10 handoff prompt, which is new to this cut and is read aloud verbatim.
9. The greeting **"Zdravo, HAI"** (Croatian), the next unused language in the rotation.
10. The palette deviation logged above, and the dual-orientation build.

VERDICT: PASS