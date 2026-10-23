# PEDAGOGY — grounding-an-ai-debt-tracker-in-real-sec-filings (AI Debt Tracker, week 1)
*Grounding an AI Debt Tracker in Real SEC Filings — Week 1 progress update · ai-explainer / claude-hai*

Second episode of the **AI Debt Tracker**, a new Mycroft project. Same chassis, same channel
and the same persistent voice as the eleven Private AI Valuation Agent episodes before it.
Source: `narration_script.md` (author-written, 3:00 target, 438 words) and `figdata.json`.

**The failure mode this reel has to avoid is sounding finished.** Nothing in the agent is
built. What exists is the ground under it: an answer key, a point-in-time server that refuses
late filings, a matcher, and a model chosen by a bake-off. A four-box pipeline diagram and a
run of green pass marks will read as a working system unless the reel says otherwise, out
loud and on the frame. B02 carries that correction in writing, and the script's own Notes
("Keep the tense honest") ask for it.

**The second failure mode is the good news being louder than its denominator.** Four of the
numbers here — 87.5%, 93.4%, 99%, and "15 not 21" — each have a narrower reading that the
author wrote down in the script's Notes and that would otherwise never reach the screen.
B08 exists to put all five on camera, and FACTCHECK rows 9, 12, 15 and 18 record them.

---

## Act structure audit

The script has seven sections plus an on-camera open and close. This cut is **twelve beats:
four bookends and eight body beats.** Five structural changes, each listed here so the author
can accept or reject them individually.

| # | Change | Why |
|---|---|---|
| 1 | **0:32 splits into two beats** — B02 (what the agent will do) and B03 (what it is graded against, and the cut-off). | The script's own shot note says this section has two movements and that the second "is the line that makes every later number trustworthy". At ~75 spoken words it is also the longest section; one frame cannot hold a four-stage pipeline *and* a grading relation without one of them becoming decoration. |
| 2 | **1:18 and 1:50 stay separate beats** (B05 answer key, B06 what it grades on), as the script has them, rather than being merged onto one figure. | `adt-w1-levels.png` carries both the partition and the bottom strip. On screen they are two different arguments — a recount, and a split with a score — and the second is not a caption on the first. |
| 3 | **B08, a limits beat, is added.** It is not in the script's section list. | Every episode in this series ends on its own limits. Its content is entirely from the script's Notes section, which otherwise reaches no frame at all. |
| 4 | **Oracle's partial 10-Qs move from the voice to the frame.** | The script marks that line as the one to drop if the cut runs long. Dropping it from the narration and keeping it as a written example beside Microsoft's keeps the evidence without the four seconds. |
| 5 | **"Wrong almost half the time" becomes "wrong in twenty-one of those forty-six".** | "Almost half" is true of the conservative count and of nothing else that is said aloud. The fraction is unambiguous and the raw 33 of 46 is printed beside it. FACTCHECK row 12. |

## Cold open + executive summary check

- B00 opens with the required line — *"Hi, I'm Om Mali. This video is about the AI Debt
  Tracker…"* — and names the project, what it follows, and what the week actually did.
- COLD OPEN LAW: the ask lands **ANSWERED**, with three output lines that are the three
  findings (495 cases, 15 not 21, the smallest model at $0).
- The ask is the week's real instruction: *ground it before you build it.* It is not a
  rhetorical question dressed as a prompt.
- There is **no separate executive-summary beat.** The three answer lines do that work, and
  B01 goes straight to why the project exists. With eight body beats and four bookends, a
  BLUF beat would be a thirteenth and would restate B09.

## ILLUSTRATE LAW audit

The Claude UI appears at **B00, B09, B10 and B11 only** — cold open, verdict, handoff, outro.
Every body beat is a native animated Remotion scene rebuilt from the data (REBUILD LAW); the
six PNGs in `pantry/` are reference and are never slotted as media.

No two consecutive body beats share a scheme — the full list is in `CHECKS-REPORT.md`. The
one that needed deliberate work is B05: three bars would have invited a comparison of 15
against 4 against 6, which is not the beat. The beat is that **one fixed set of 25 companies
splits differently once coverage is measured**, so the 25 is drawn once, whole, and the
assumption is drawn as an outline over it.

## Utility-framing lint

Each body beat answers "what does this let someone do":

```
B01  know that the thing being financed is debt, and that nobody was tracking it
B02  know what would be built, and that it has not been
B03  know why any score here is worth anything at all
B04  know there is a baseline to beat, measured before the build
B05  know what the ground truth can actually support — the week's real finding
B06  know what is held back, and how well bonds match today
B07  know which model to run, and that it costs nothing
B08  know where each number stops being true
```

## Honesty check

- **The agent does not exist.** Said in B00, written on B02's frame, repeated in B09.
- **87.5% is 56 of 64, not 56 of 73.** The nine excluded bonds are old bonds newly tagged;
  including them gives 76.7%, under the pass line. FACTCHECK row 9.
- **21 of 46, not "almost half".** Raw is 33 of 46 and includes re-tagging. Both printed.
- **15 rather than 21 is a measurement, not a correction of bad data.** 21 counted tags; 15
  measures coverage. 14 qualified outright and one moved up on a 4–4 tie, said on camera.
- **93.4% is the per-bond quarters.** Across every quarter it is 85%. Both printed.
- **99% is after six truth corrections**, on 29 documents, from one plain prompt. 95% before,
  same winner. Printed on B07 and again on B08.
- **$121bn is not this project's measurement.** Bank of America via Reuters. B08 says so.
- **Nothing was spent.** `$0.00`. The bake-off ran on an 8 GB laptop GPU; the narration is
  Kokoro, local.

## Length law

```
12 beats · 8 body beats at 54–68 words (band 45–68) · 731 words total
body 8 beats = 145.87s (2:25.9)   ·   bookends 4 beats = 67.87s (1:07.9)
measured master runtime: 213.74s (3:33.7), identical in both orientations
```

The script targets 3:00 for its own seven sections. The four bookends this channel requires
are additive, as they have been in every episode of the series (week 11 ran 212s on the same
structure). The measured runtime is recorded here rather than reached by cutting a body beat
below the band.

## Both orientations, from one source

Every scene lays itself out natively at 1920×1080 **and** 1080×1920 through
`f(landscape, portrait)`, registered twice in `Root.tsx`. The 9:16 cut is a **re-layout, never
a crop**, and it is built from the same mp3s — `make_vertical.py` copies the audio rather than
regenerating it, so no number can differ between the two masters.

Portrait values are tuned, not inherited; the beats rescaled after reading portrait frames are
listed in `BUILD-LOG.md`.

## Source fidelity

- Every on-screen figure is a prop injected from `figdata.json` under assertions.
- **The framing assertion is `MEASURED_BY_BOND < ASSUMED`**, over a partition asserted to sum
  to the whole 25-company universe. If measuring by coverage ever stopped lowering the count,
  or the three levels stopped accounting for every company, the build fails rather than ships
  a beat arguing about nothing.
- **The second argument is asserted the same way**: the bake-off winner must be the *smallest*
  model and must win outright.
- Five claims are not in `figdata.json` — the Mycroft recipe count, the pipeline design, the
  point-in-time server's two files, and Microsoft's and Oracle's tagging. Each is a named
  constant, and each beat that uses one says on the frame where it came from.

## Palette deviation (logged, deliberate)

The source figures use red `#C8102E` as their primary series with amber `#C8860E` pass lines.
This cut renders in the Claude fidelity skin (cream `#F2F0E9`, ink `#3D3929`, terracotta
`#D97757` as the ONE accent) because `ai-explainer` is a fidelity brand that may not be
retinted. **Palette change only — no datum, ordering, or label altered.** The figures' rule
that red is the primary series and never a warning colour is preserved in effect: terracotta
marks the 2025 bar, the ledger, the cut-off, the test under discussion, the measured 15, the
held-back 400 and the smallest model — the subject of each beat, never a hazard.

---

**What the author is being asked to sign off on**, having watched
`grounding-an-ai-debt-tracker-in-real-sec-filings-slate.mp4`:

1. The five structural changes above, in particular **adding B08**, which is not in the
   script's section list, and **splitting 0:32 into B02 and B03**.
2. Saying on camera, twice, that **the agent is not built** — including the change from the
   script's "The agent watches / reads" to "The agent **will** watch".
3. Replacing "wrong almost half the time" with "wrong in twenty-one of those forty-six", and
   printing the raw 33 of 46 beside it.
4. Saying on camera that **fifteen rather than twenty-one came down to one company on a 4–4
   tie**, and that 93.4% is the per-bond quarters while every quarter is 85%.
5. Saying on camera that 99% is **after correcting six expected values** on a 29-document set.
6. `FACTCHECK.md` rows 3, 4, 6, 7 and 14 — the five claims `figdata.json` does not contain.
7. The B10 handoff prompt, which is new to this cut and is read aloud verbatim.
8. The greeting **"Salve, HAI"** (Latin), the next unused language in the rotation.
9. The palette deviation logged above, and the dual-orientation build.

VERDICT: PASS — Om Mali, 10/16/2026.


**GATE P did not hold on this build, and the reason is recorded here rather than passed over.**
Audio for the pre-signature review cut was generated WITHOUT `--no-gate`, and the gate let it
through although this file said `VERDICT: PENDING` at the time. `generate_audio_kokoro.py`
searched the whole file for the substring `VERDICT: PASS`, and the PENDING block underneath the
verdict line carried a template instruction that spelled the phrase out. A gate a placeholder
can satisfy is not a gate. It has been hardened to read the first VERDICT token on a line and
require that it says PASS, and was checked against all 134 `PEDAGOGY.md` files in the fellows
tree: the only four that change behaviour are four that say `VERDICT: PENDING` in as many
words, and no signed reel is newly refused. See `BUILD-LOG.md` defect 6.

The audio was NOT regenerated after signing: the mp3s measured, locked and rendered against are
the mp3s in the masters, so the signed cut is bit-for-bit the cut that cleared GATE V.
