# FACTCHECK — vox-base-rate

Source of truth: `books/the-reallocation-engine/chapters/05-verifying-the-data.md`
(the "Base rates and the confidence illusion" section §64–92, the worked example
§145, and Figure 5.4 §147). Every narration line, viz count, and card string
checked. ✓ holds · minor (editorial/simplification, defended) · WRONG (must fix).

This film deliberately excludes: the Bayes theorem formula/derivation, any
calibration-curve discussion, cost-asymmetry threshold analysis, and the verb
taxonomy — none are asserted. The medical example appears in exactly one beat
(B05), per the card's exclusion.

| # | Claim (beat) | Verdict | Source / derivation | Note |
|---|---|---|---|---|
| 1 | The scorer returns **0.68**, sourced and **calibrated** (B01, B02, B08, B09) | ✓ | §68: "a '0.65 probability'…"; §139/§145 worked example: "The Sponsorship Scorer returns 0.68." §78 defines calibration as a property. | 0.68 is the worked-example figure (§145), not the §68 illustration (0.65). Correct. |
| 2 | The score "answered only half a question" — it omits **how rare a sponsor is** (B03) | ✓ | §70: "It depends on the base rate." §76: "the signal has to overcome that prior." | Editorial framing of the base-rate point; faithful. |
| 3 | In this category, **8 of 100** companies have ever sponsored — the base rate (B04) | ✓ | §145: "In this SIC code (pharmaceutical and medicine manufacturing), the three-year LCA filing rate among employers … is approximately 8%." | 8% ⇒ 8 in 100. Exact. Grid uses 8 navy + 92 grey. |
| 4 | A **99%-accurate** test at **1-in-10,000** prevalence ⇒ **almost every alarm is false** (B05) | ✓ | §72: "A 99%-accurate test applied to a population where 1 in 10,000 … produces … ~1 true positive and ~100 false positives … fewer than 1% are genuine." | Verbatim structure. Bar shows ~1 navy : ~100 crimson. The ONLY medical beat. |
| 5 | A positive signal **lands on rare sponsors and common non-sponsors alike** (B06) | ✓ | §72: "most positive signals land on non-sponsors"; §70 base-rate mechanism. | Qualitative; no FP count stamped. |
| 6 | So many non-sponsors that **false positives swamp** the few real ones (B07) | ✓ | §72: "when only 8% … most positive signals land on non-sponsors." Candidate card §66. | The swamp is qualitative — the B07 pile (8 navy / 12 crimson) is labelled "illustrative," no claim of exactness. |
| 7 | The genuine share **isn't 68%**; the base rate drags the marker **toward 0.40** (B08) | ✓ | §145: "posterior approximately 0.38–0.45"; §147 Fig 5.4: markers at prior ~0.08, raw 0.68, corrected posterior high-30s to mid-40s. | Film says "toward forty" — inside the 0.38–0.45 band and matching the candidate title's 0.40. Markers 0.08 / 0.68 / ~0.40 are all from Fig 5.4. |
| 8 | **Nothing was miscalculated**; 0.68 = signal strength, **0.40 = what it's worth** (B09) | ✓ | §145: "This does not change the conclusion dramatically … the 0.68 overstates the posterior … by 50–75%." §66: "nothing about the score is wrong." | 0.68 → ~0.40 is the posterior, not a recomputation error. Faithful. |
| 9 | It's **a lead worth checking, not a promise** — ask directly first (B10) | ✓ | §150: "a demonstrated filing history that makes them a reasonable target for further investigation — specifically, a direct inquiry about current H-1B sponsorship." | Editorial compression of §150; no cost-ratio threshold math (excluded). |
| 10 | "A strong signal for a rare thing is still a long shot." (B11) | ✓ (minor) | Faithful epigram for §70–§76 + §145. | Editorial closing line; asserts nothing beyond the chapter. |
| 11 | Card title "Why your 0.68 is really a 0.40" (B01) | ✓ | Candidate 05 card title, `vids/video-ideas.md` §63. | 0.40 is within the §145 posterior band. |
| 12 | Endcard "from The Reallocation Engine — chapter 5" (B11) | ✓ | Source chapter is `05-verifying-the-data.md`. | — |

## Simplifications, labeled (defended)

- **"toward forty" / "0.40"** (B08, B09, title): the chapter gives the posterior as
  "approximately 0.38–0.45." 0.40 sits inside that band and is the candidate title's
  own figure. Using a single round number for a spoken line is a defensible
  simplification of a stated range; the on-screen marker lands in the high-30s/low-40s
  region, not on a false-precise point. Defended.
- **The B07 swamp pile (8 navy / 12 crimson)** is labelled "illustrative" in the beat
  sheet and carries no on-screen number. It depicts "most flagged are false," which the
  chapter asserts; it does not claim a specific false-positive count. Defended.
- **Medical example rounded** ("almost every alarm is false"): the chapter says "fewer
  than 1% are genuine" (≈1 true : 100 false). "Almost every alarm is false" is an exact
  plain-language reading. Defended.

## Numbers appearing on screen (viz)

- B04: **8 navy + 92 grey = 100** (8% base rate) — §145. ✓
- B05: ~**1 navy : ~100 crimson** per 10,000 — §72. ✓
- B08: probability markers **0.08 · 0.68 · ~0.40** — §147 Fig 5.4. ✓
- B09: **0.68** (signal) vs **0.40** (worth) — §145. ✓
- No Bayes formula, calibration curve, or cost-ratio number appears anywhere (confirmed
  against beat_sheet.json).

**Verdict: all claims hold.** One minor closing epigram (B11) and three labeled
simplifications, each defended. No WRONG claims. Cleared to render.
