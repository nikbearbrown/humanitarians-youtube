# Feedback: "Which of Gardner's Eight Intelligences Can a Machine Do?" — Tanmay Kulkarni, Week 24

> **CURRENT VERDICT (2026-09-26, after fixes 1–4): clear-for-public · teaching 10/12 ·
> production gate PASS · sources on screen PASS (32/35 claims evidenced when spoken; the other 3 are
> sourced, not defects).** See "Re-review" at the bottom. The review directly below is the
> *original* pre-fix review, kept for the record.

**Original verdict (superseded):** **unlisted-until-fixed.** Teaching **10/12**. Production gate **FAIL on one claim**
(B17), with four cheap [EDIT]s recommended alongside it.

This film attempts to show that Gardner himself answered "which intelligences can a machine do?"
(six of eight) and that the answer came from a different test than the one his theory was built
on. It delivers that, with a structure no earlier film has. It stops one prop string short of
passing its own "no source, no verdict" rule, because B17 states a book title and year that
nothing on screen supports.

**Reviewed from the final master** (`gardner-eight-intelligences-machine-final.mp4`, 3840×2160,
5:56). **35 factual claims**, each checked at the moment it is spoken: the frame was extracted at
that timestamp in the paced master and OCR'd (macOS Vision), and every miss was then confirmed by
eye. Method: `_qc/claims_at_assertion.py`; frames in `_qc/assertion/`.

## Where it improved vs film 23 (`/series`)

| Week 23 lesson | Week 24 |
|---|---|
| Leaked template content on every card (Review 4) | ✅ none. All props set explicitly, `preship_lint` clean, verified on frames |
| Uninstructed brand beat ("This is Humanitarians") | ✅ none. The film opens on its own cold open |
| Cards under-filled the 4K frame (Review 8, Gate V) | ✅ `compile.py` final-frame check passed at 3840×2160 |
| Three-question framework shared with Weeks 17–23 | ✅ replaced by a structure only this subject has (EIGHT ROOMS) |
| Standing source lower-third (recommended as a template) | ✅ every room beat and card carries its source line |

## Rubric

| Criterion | What it means | This cut |
|---|---|---|
| Explicit framework | Structure shown before the examples | **2**: the floor plan and its lighting rule land at 0:23.8 (B02), before the first room. The 3.8s over ~20s was accepted by Tanmay |
| Reusable rubric | Viewer can apply the axes to a new case | **1**: by design, no checklist. The transferable move (check *which test* produced a verdict before trusting the count, B12–B13) is shown, not packaged |
| Worked example | A case walked through live | **2**: eight rooms, one by one, each with its evidence on screen |
| Falsifiability / edge case | Framework stress-tested | **2**: room seven (evidence given, light withheld, reason unstated) and room eight (dark by definition, not failure). B12–B13 reframe the six lights the viewer just counted |
| Active task | Viewer does something structured | **1**: one open question (B18). Specific, but not a scaffold. By design |
| Friction | Viewer must resolve a tension | **2**: B12–B13 overturn the count; B14 leaves an honest open question |

**10/12**. Clears the ship bar (≥ 8). The two 1s are the known cost of dropping the checklist
format, which was the brief for this film.

## Production gate

**Legibility — PASS.** Every card and caption is readable at 4K in open-licence type. The
room-state labels ("light on / dark") are small (≈17 px at 1080p), but each state is also carried
by fill and lamp, so nothing depends on reading them.

**Sources on screen — FAIL on one claim** *(pre-fix; PASS after fix 1, see Re-review)*. 29/35 claims are fully evidenced at the moment of
assertion. Of the six misses:

| # | Time | Beat | Claim spoken | On screen at that moment | Severity |
|---|---|---|---|---|---|
| 1 | 5:17 | B17 | "his **2007** book **Five Minds for the Future**" | neither. The visible source (Education Next) names the book but not the year | **CRITICAL**: the only claim with no supporting evidence on screen |
| 2 | 2:21 | B07 | "The essay's sentence needs that one correction" | the essay's claim is only in the footer source line, footnote-sized, beneath the 1956 caption | **MAJOR**: the film's central correction, with its A-side ("not yet a serious competitor to any of them") at footnote size |
| 3 | 2:26 | B08 | "Chess and Go are filed here, under spatial, not logic" | room still dark, caption hidden. It lands ~2s later at "Mastering…" | MINOR: the beat's surprise is asserted before its evidence appears |
| 4 | 0:47 | B03 | "in a book called Frames of Mind" | heading shows "1983" but not the title. The Davis source is visible and supports it | MINOR |
| 5 | 2:16 | B07 | "by no means clear" (verbatim) | the source (MI Oasis 2024) is visible, the phrase is not | MINOR: sourced, just not shown |
| 6 | 3:06 | B11 | "from thimbles to airplanes" (verbatim) | the source is visible, the phrase is not (the caption holds for "multiply intelligent!") | MINOR: sourced, just not shown |

Not counted as a miss: B17's forklift line is an attributed paraphrase, no quote marks, and its
source ("Introducing Theorist.ai") is line 1 of the card on screen.

**Side-by-side at the moment of comparison — PASS, weakly (B07).** The essay's claim and the
record are on screen together for the whole beat, but one of them is in footer type. B17's three
words ("obsolescence / its opposite / optional") are a clean side-by-side.

## The problem

**B17, 5:17: a date and a title with no receipt.** The film is careful everywhere else: every
quote was checked word for word against the live pages. Here the narration states *2007* and
*Five Minds for the Future* while the card shows neither, and the card's only source (Education
Next, 2026) doesn't establish 2007 (FACTCHECK 4.3 sources it to HBR). One line on the card fixes
it.

## Do X next week (all [EDIT], props only, no narration or audio change, Gate P unaffected)

1. **[EDIT] B17 (critical):** card line 2 → "Gardner, Aug 2026, on *Five Minds for the Future* (2007): disciplined, synthesizing, creating minds → “will become optional for our species”". Add the HBR date source to the footnote
2. **[EDIT] B07 (major):** promote the essay's claim into the caption so both sides are the same size: "Essay: “not yet a serious competitor to any of them” · 1956: programs “carried out mathematical and logical operations”…", then trim the footer to the citations only
3. **[EDIT] B08:** `captionAtSeconds` → the cue "Chess and Go are filed", so the quote is up when the surprise is said. The room still lights at "Mastering"
4. **[EDIT] B03:** heading → "Frames of Mind, 1983: seven rooms. Mid-1990s: an eighth"
5. *(Optional)* **[EDIT] B11:** show "from thimbles to airplanes" before the "multiply intelligent!" caption takes over. This needs a second caption slot in `EightRooms`, so skip it unless the other four are already done

Cost: 4 beats re-rendered (~6 min) → recompile → pacing pass → loudness pass → re-run
`claims_at_assertion.py`.

**Standing-template note:** misses 3, 5 and 6 share a cause. `EightRooms` has one caption per
beat, so a beat that makes two quoted claims can only show one. If this component is reused, a
second caption slot with its own cue is the permanent fix.

## What works

- **The structure is the subject.** Eight rooms are Gardner's eight intelligences. It can't be
  lifted into another film, and it gives the viewer a running count they can feel, which is what
  makes B12–B13's reversal land
- **Evidence discipline.** Every quotation is verbatim against the live pages, all visuals are
  code-drawn, all type is OFL-licensed, and there are zero third-party images
- **Honest open ends.** B14 says "the paper doesn't say", and B15 says the room is dark "on their
  reading". Confidence matches the evidence throughout
- **Timing craft.** 29/35 claims have their evidence on screen at the moment they're spoken, and
  lights and captions are cued to the words

---

## Re-review — after fixes 1–4 (2026-09-26)

**Verdict: clear-for-public.** Teaching **10/12**. Production gate **PASS**.

Tanmay approved fixes 1–4. All were props only (no narration, audio or Gate P change): 4 beats
re-rendered, then recompile, pacing pass, loudness pass. The claim check was re-run on the new
master (`_qc/claims_at_assertion.py`, OCR plus eye check):

| Fix | Beat | Result at the moment of assertion |
|---|---|---|
| 1 (critical) | B17 5:17 | ✅ "Five Minds for the Future (2007)" on the card; HBR 2007 in the footnote |
| 2 (major) | B07 2:21 | ✅ "Essay: … not yet a serious competitor …" and "Record: 1956 programs …" in the same caption, same size |
| 3 | B08 2:26 | ✅ the chess/Go quote is up when "Chess and Go are filed here" is said |
| 4 | B03 0:47 | ✅ heading "Frames of Mind, 1983: …" |

**32/35 claims evidenced on screen at the moment of assertion.** The 3 remaining are all
non-defects by this review's own classification. Two are verbatim phrases whose source is on screen
(B07 "by no means clear", B11 "from thimbles to airplanes"; optional fix 5 not taken). One is B17's
attributed forklift paraphrase, whose source is on the card.

**Sources on screen:** every factual claim now has visible, supporting evidence. **Side-by-side:**
B07 and B17 both clean. **Legibility:** unchanged, PASS.

Master re-measured after the final step: 3840×2160 · 5:56 · **-14.9 LUFS / -1.9 dBTP** · video
stream identical to the paced cut.

---

## Review — visual-variety master (2026-09-27)

**Verdict: clear-for-public.** Teaching **10/12** (unchanged; narration and teach unchanged, Gate P
stands). Production gate **PASS**. Reviewed on `gardner-eight-intelligences-machine-final.mp4`
(built 2026-09-27).

**What changed:** room interiors for all eight rooms (`EightRoomsTour`) and motion on the four
long cards (`RevealScenes`: B05 timeline, B13 tiles, B16 keys, B17 triptych). Props and visuals
only.

### Production gate

| Check | Result |
|---|---|
| Sources on screen at the moment of assertion | **34/35 claims** evidenced (was 32/35). New: B11 "from thimbles to airplanes" (interior caption), B17 forklift line (verbatim, on the card). Remaining: B07 "by no means clear" (source on screen, phrase not shown) |
| GATE V (toolkit, in the compile) | **38 frames · 0 BLOCKER · 0 MAJOR** |
| Dense sweep (every 2% of all 19 beats, 950 frames, GATE V's checker) | 0 BLOCKER. 2 flags, on the **designed entrance frames** of B01 and B12 at 1% (0.2s in, fully populated by 3%). GATE V samples steady state only. Recorded as non-defects, and shared toolkit components were not changed to silence an over-dense sweep |
| Legibility / containment | every interior drawing clipped to its panel (Tanmay's rule), checked at full resolution |
| Side-by-side | B07 (essay vs. record, same caption) and B17 (three columns) clean |
| Master | 3840×2160 · 5:56 · **-14.9 LUFS / -1.9 dBTP** · 48 kHz · A/V lengths agree · video MD5 identical to the paced cut · a 0.8–1.25s pause at all 18 cuts |

### Defects found during this pass, all found on frames and all fixed before this build

| # | Defect | How it was caught | Fix |
|---|---|---|---|
| 1 | Compositions froze past their registered length: **B17's closing resolve and B07's pull-back never played** | frame-stepping B17 at 29–34s | `durationSeconds` prop + `calculateMetadata` on all 14 new compositions; the builder passes the measured audio |
| 2 | The room camera move **pushed the neighbouring rooms past the title-safe edge** (all eight rooms) | the real GATE V refused the first compile (B14 edge-bleed) | the plan never scales; a copy of the room grows into a framed card while the plan fades. Two intermediate designs were rejected by the gate (edge-bleed, then underfill) before this one passed at every 2% |
| 3 | **The plan flashed to near-blank at every room-to-room cut** (its entrance fade) | dense sweep, B06/B09 low-contrast at 1% | entrance fade removed; consecutive plan beats now join seamlessly |
| 4 | Room 3 contour ring on the panel edge + stray route-cap dot | Tanmay's screenshot | clipped panels with inner padding; the route renders only once it starts |
| 5 | Room 7 speech bubble over a head | full-res frame check | figures resized to clear both bubbles |

### Attention budget (`/pacing`), the reason for this pass

| Measure | Before | Now |
|---|---|---|
| Static floor plan share of runtime | 52% (181s) | **29% (99s)** |
| Longest unbroken same-visual run | 87.3s (B06–B11 plan) | **41.2s** (B02–B03 plan) |
| Distinct looks | 4 compositions | **16** |
| Room interiors | none | 24% of runtime |

### Rubric (unchanged, **10/12**)

Framework 2 · Reusable rubric 1 (by design) · Worked example 2 · Falsifiability 2 · Active task 1
(by design) · Friction 2. The visual pass improves watchability, not the rubric, which scores
teaching structure.

### Remaining, optional

1. **[EDIT] B07:** add "“by no means clear” then: conversation, games of strategy" to the interior caption → 35/35
2. **[EDIT] B02–B03:** the new longest static run (41s, two plan beats back to back). Candidate: a slow
   camera drift across the plan, or B03 drawn as a blueprint to mark "1983". Worth doing only if it
   still feels long on a watch-through
3. B01 and B04 hold one composition for more than 20s (the cold-open typing and the *g* caveat card). Acceptable; noted

## Addendum — B07 caption edit (2026-09-27)

Tanmay approved optional edit 1. B07's caption now ends with “By no means clear” then: passing the
Turing Test, winning games of strategy (FACTCHECK 3.4, the source's own terms, where the narration
says "conversation"). B07 was re-rendered and the master recompiled; narration is unchanged, so Gate P stands.

| Check | Result |
|---|---|
| Claims evidenced on screen at the moment of assertion | **35/35** (was 34/35); B07 "What was" passes at 2:16.46 |
| GATE V (compile) | 38 frames · 0 BLOCKER · 0 MAJOR |
| Caption fit | 3 lines in both the interior and plan views, clear of the source line (eye check, t=21s/27s/28.5s) |
| Master | 3840×2160 · 356.2s · -14.9 LUFS · -1.9 dBFS · 48 kHz · video MD5 matches the paced cut |

Verdict unchanged: **clear-for-public**. Remaining optional edit: the B02–B03 41s plan run (watch-test first).

## Addendum — two defects found while building the Short, fixed in the long (2026-09-27)

Tanmay: "go ahead and fix both defects in the long too."

| Defect | Found by | Fix | Verified |
|---|---|---|---|
| **One black frame at 5:50.38** (cut into B19) | the Short's safe-zone sweep on the same component; missed by GATE V and the dense sweep | `ClaudeTitleOutroFull`: the page is opaque from frame 0 and only the content fades (a toolkit fix, shared with the Short). B19 re-rendered | per-frame luma scan of the whole new master (YAVG < 80): **0 dark frames** (was 1) |
| **Digit years misread by Kokoro** ("nineteen hundred eighty three" ×4, "mid nineteen hundred ninety z", "nineteen hundred fifty six", "two thousand nineteen / twenty four") | phoneme check while writing the Short's read-aloud sheet | narration writes years in words (TTS spelling only, like "gee" and "M-I"; captions and cards keep the digits). "2007" already read correctly ("two thousand seven") and was left as digits. Audio regenerated for B01, B03, B05, B07, B12, B13; cues re-resolved; those beats re-rendered | every respelling checked in Kokoro's phonemes before generation; claim cues updated in `claims_at_assertion.py` |

**New master:** 3840×2160 · **5:51** (351.4s; the six regenerated beats are 0.2–1.7s shorter
without "hundred") · -14.9 LUFS · -1.9 dBFS · LRA 3.3 · 48 kHz · the video stream of the final
matches the paced cut (MD5) · GATE V 38 frames, 0 BLOCKER / 0 MAJOR · **35/35 claims on screen at the
moment of assertion** · 0 dark frames.

Gate P: the words are the ones Tanmay signed; only their spelling for the voice changed. The six
beats have **new audio**, so it's worth one listen: B01, B03, B05, B07, B12, B13.
Verdict unchanged: **clear-for-public**.

## Addendum — sync, labels, pacing (2026-09-27)

Found in the Short's viewer-pass PROOF and applied here too: the cues are pause-anchored (`cue_align.py`,
the word-position drift was mean 0.51s / max 1.17s), room labels ×1.3, and holds are 0.3s. New
master **5:46**, -14.9 LUFS / -1.9 dBFS, GATE V 0/0, 35/35, 0 dark frames. Details in
`short/PROOF-REVIEW-SHORT.md`, "Fixes 1–3 applied". Verdict unchanged: clear-for-public.
