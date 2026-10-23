# PEDAGOGY — building-the-answer-key-grader-and-baseline (AI Debt Tracker, week 2)
*Building the Answer Key, Grader and Baseline — Week 2 progress update · ai-explainer / claude-hai*

Third episode of the **AI Debt Tracker**. Same chassis, same channel and the same persistent
voice as the eleven Private AI Valuation Agent episodes and the two before this one. Source:
`narration_script.md` (author-written, 3:00 target, 448 words) and `figdata.json`.

**The failure mode this reel has to avoid is sounding like a system that works.** It is full of
scores — 10 of 10, 90.7%, 30 of 32 — and the thing being scored does not exist. What exists is
the answer key, the grader and the floor. B00 says so, B02's subtitle says so on the frame, and
B08's last row says so again.

**The second failure mode is letting the good number be the one a viewer keeps.** Two numbers
here are flattering and nearly meaningless on their own: *10 of 10* was calibrated on the ten
reports that found the bugs, and *90.7%* is what you score by doing nothing. Both are drawn so
the thing that qualifies them is the larger object on the frame — a dashed rule in B04, an
empty track in B05.

---

## Act structure audit

The script has seven sections plus an on-camera open. This cut is **twelve beats: four bookends
and eight body beats.** Five structural changes, each listed so the author can accept or reject
them individually.

| # | Change | Why |
|---|---|---|
| 1 | **1:13 splits into two beats** — B03 (the five bugs) and B04 (calibrated vs measured). | At ~95 spoken words it is by far the longest section, and it contains two different arguments: *the grader was wrong in five specific ways*, and *the number that follows a fix is not evidence*. One frame holding both would make the second a footnote on the first. |
| 2 | **B05 leads with the zero, not with 90.7%.** The script says the recall first. | Said in the script's order a listener hears a 90% system with a caveat attached. The zero is the finding; the recall is the thing that hides it. The frame draws the empty track before either flattering number appears. |
| 3 | **"So ten of ten is a calibration, not a score" is added to the voice.** | The script's Notes make exactly this point and the script's body does not. It is the sentence that stops the reel overselling itself. |
| 4 | **The closing on-camera section becomes B08, a limits beat**, with the three next steps inside it. | Every episode in this series ends on its own limits. The limits come from the script's Notes, which otherwise reach no frame. |
| 5 | **Oracle and Broadcom are named in the voice; AMD and Equinix only on the frame.** | Five company names in one spoken sentence is a list, not evidence. Two carry the point aloud and all five are legible on screen. |

## Cold open + executive summary check

- B00 opens with the required line — *"Hi, I'm Om Mali. This video is about building the answer
  key and the grader for my AI debt tracker…"* — and names the week, the project and the fact
  that the agent is still unwritten.
- COLD OPEN LAW: the ask lands **ANSWERED**, with three output lines that are the three
  findings (the key's size, the grader's own bugs, the baseline's zero).
- The ask is the week's real instruction: *build what will grade it, before it exists.*
- There is **no separate executive-summary beat.** The three answer lines do that work, and a
  thirteenth beat would restate B09.

## ILLUSTRATE LAW audit

The Claude UI appears at **B00, B09, B10 and B11 only** — cold open, verdict, handoff, outro.
Every body beat is a native animated Remotion scene rebuilt from the data (REBUILD LAW); the
three PNGs in `pantry/` are reference and are never slotted as media.

No two consecutive body beats share a scheme — the full list is in `CHECKS-REPORT.md`. The
adjacency that needed deliberate work is B04/B05/B06, all three of which involve a horizontal
track. B04 fills bars and divides them with a rule; **B05 draws one track and leaves it
empty**, which is the only thing on that frame doing any work; B06 puts two readings on one
axis and draws the distance between them.

## Utility-framing lint

Each body beat answers "what does this let someone do":

```
B01  know what the agent will be graded against, and how uneven that ground truth is
B02  know the exact rule a bond has to satisfy before any score means anything
B03  know that the grader was checked, and what checking it found
B04  know which of the two hand-check numbers is evidence
B05  know the floor — and that its best-looking number hides a zero
B06  know how much of the gap is reachable from the filings at all
B07  know why the cut-off no longer depends on a wall clock
B08  know where each number above stops being true
```

## Honesty check

- **The agent does not exist.** Said in B00, written on B02's frame, repeated in B08 and B09.
- **10 of 10 is a calibration.** The same ten reports found the five bugs. The measurement is
  2 of 3, on reports picked before reading and graded once — and three is a small check, said
  as one. FACTCHECK row 12.
- **Every disagreement was the grader's fault, not the reports'.** Five named defects, each
  attributed to the company whose printed table exposed it. Not softened. FACTCHECK row 9.
- **90.7% is what doing nothing scores**, with a 87.5–93.5% interval, and it is high for the
  same reason the zero is zero. It is never presented as a target. FACTCHECK row 15.
- **30 of 32, not 30 of 36.** Four new bonds carry no tagged interest rate and could not be
  searched for at all. Both numbers are on the frame. FACTCHECK row 17.
- **The timestamp explanation is an inference.** EDGAR published no note; B07 says the word.
- **Nothing was spent.** `$0.00`. The narration is Kokoro, local.

## Length law

```
12 beats · 8 body beats at 58–71 words (band 45–72) · 718 words total
body 8 beats = 143.49s (2:23.5)   ·   bookends 4 beats = 61.02s (1:01.0)
measured master runtime: 204.51s (3:24.5), identical in both orientations
```

The band is four words wider at the top than week 1's. This script **speaks its large
numbers** — "one thousand and ninety three", "nine thousand six hundred and fifty three",
"eighty seven and a half" — and a single figure can cost six words. Tightening the band would
mean cutting evidence to pay for the way a number is pronounced. The four bookends this channel
requires are additive, as in every episode of the series.

## Both orientations, from one source

Every scene lays itself out natively at 1920×1080 **and** 1080×1920 through
`f(landscape, portrait)`, registered twice in `Root.tsx`. The 9:16 cut is a **re-layout, never
a crop**, and it is built from the same mp3s — `make_vertical.py` copies the audio rather than
regenerating it, so no number can differ between the two masters.

Portrait values are tuned, not inherited. The chassis arrives with week 1's portrait values
already raised; the beats rescaled after reading portrait frames are listed in `BUILD-LOG.md`.

## Source fidelity

- Every on-screen figure is a prop injected from `figdata.json` under assertions.
- **The framing assertion is `HELD_OUT_SHARE < AFTER_SHARE`.** If the held-out score ever
  caught up with the calibrated one, B04 would be drawing a distinction that no longer exists,
  and the build fails rather than ship it.
- **The second argument is asserted the same way**: the baseline's recall must stay above 90%,
  its new-bond count must stay at zero, and its exact-quarter share must stay under half. A
  flattering number hiding a zero is the whole of B05.
- Further assertions hold the partition (900 + 41 + 152 = 1,093, and "most" means a majority),
  the searchable denominator (36 − 4 = 32), and the repayment arithmetic (16 − 9 − 1 = 6).
- Three claims are not in `figdata.json`'s measured block — that the agent is unbuilt, that the
  timestamp shift is an inference, and what the held-out miss was. Each is a named constant and
  each beat that uses one says on the frame where it came from.

## Palette deviation (logged, deliberate)

The source figures use red `#C8102E` as their primary series with ochre `#C8860E` for the
middle category. This cut renders in the Claude fidelity skin (cream `#F2F0E9`, ink `#3D3929`,
terracotta `#D97757` as the ONE accent) because `ai-explainer` is a fidelity brand that may not
be retinted. **Palette change only — no datum, ordering, or label altered.** The figures' rule
that red is the primary series and never a warning colour is preserved in effect: terracotta
marks the bond-by-bond majority, the pairing rule, the fixed grader, the held-out check, the
empty track, the announcements and the moved timestamps — the subject of each beat, never a
hazard.

---

**What the author is being asked to sign off on**, having watched
`building-the-answer-key-grader-and-baseline-slate.mp4`:

1. The five structural changes above, in particular **adding B08** and **splitting 1:13 into
   B03 and B04**.
2. **Reordering B05 to lead with the zero** rather than with 90.7%, against the script's order.
3. Adding to the voice: *"so ten of ten is a calibration, not a score"*, and *"three untouched
   reports, once"*.
4. Saying on camera that **every disagreement was my bug, not theirs**, with Oracle and
   Broadcom named aloud and AMD and Equinix on the frame.
5. Saying on camera that **the agent still does not exist**, twice.
6. `FACTCHECK.md` rows 4, 5, 9, 13 and 20 — the claims `figdata.json` does not measure.
7. The B10 handoff prompt, which is new to this cut and is read aloud verbatim.
8. The greeting **"Sveiki, HAI"** (Latvian), the next unused language in the rotation.
9. The palette deviation logged above, and the dual-orientation build.

VERDICT: PASS Om Mali 10/23/2026

*To sign, replace the line above with the word VERDICT, a colon, and the word PASS, followed by
your name and the date. I do not sign it, and this file deliberately does not spell that phrase
out anywhere else — a placeholder that quotes it is what opened the audio gate on an unsigned
reel last week.*
