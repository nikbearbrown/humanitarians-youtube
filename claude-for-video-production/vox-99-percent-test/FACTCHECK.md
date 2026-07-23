# FACTCHECK — vox-99-percent-test

Source of record: `books/computational-skepticism-for-ai/chapters/02-probability-uncertainty-and-the-confidence-illusion.md` (section "The test that is 99% accurate, and the patient it kills").
This film's claims are MATHEMATICAL — verified by direct computation 2026-07-06, not by web sourcing. The scenario (disease, 1-in-10,000, 99% test) is the chapter's stipulated hypothetical, not an epidemiological claim about any real disease; no disease is named on screen or in narration.

## The arithmetic — all verified by computation

| Beat | Claim | Verdict | Derivation |
|---|---|---|---|
| B02/B04 | base rate: 1 person in 10,000 | ✓ stipulated | The chapter's hypothetical. In 10,000 people: 10,000 × (1/10,000) = 1 expected case. Grid draws exactly 1 blue of 10,000. |
| B05 | "the test catches that one person" | ✓ simplification, defended | 99% sensitivity → catches the 1 case with p=0.99; the expected-count treatment rounds to 1. The chapter does the same ("catches that person — call it one true positive"). |
| B06 | "wrong about one percent of the 9,999 healthy — about a hundred false alarms" | ✓ | 9,999 × 0.01 = 99.99 ≈ 100. Grid flips exactly 100 terracotta ("about a hundred" spoken; the count is the honest rounding). |
| B07/B08 | "one hundred and one people… about one percent" | ✓ | Pool = 1 + 100 = 101. Posterior = 1/101 = 0.0099 ≈ 1%. Bayes cross-check: (0.0001 × 0.99) / (0.0001 × 0.99 + 0.9999 × 0.01) = 0.000099 / 0.010098 = 0.0098. Both routes agree. |
| B09 | "off by two orders of magnitude" | ✓ | Intuited ~90%+ vs actual ~1%: 90/1 ≈ two orders of magnitude. Matches the chapter's phrasing. |
| B10 | "right about sick people: 99%… positive actually sick: 1%" | ✓ | P(positive\|disease)=0.99 vs P(disease\|positive)≈0.0098 — the two conditionals, stated without the word "conditional" (card exclusion honors no-Bayes-vocabulary). |

## Framing claims

| Beat | Claim | Verdict | Basis |
|---|---|---|---|
| B01 | "both halves of that sentence are true" | ✓ | The test meets its spec AND the posterior is ~1% — the film's whole point; chapter: "The number on the box is honest. Nothing is broken." |
| B03 | "most engineers say ninety percent or higher" | flourish, labeled | The chapter's teaching anecdote ("I have put this question to a lot of engineers… almost everybody answers somewhere above ninety"). Author's experience, not a study — narration attributes it as typical behavior, no citation implied. Kahneman/Tversky base-rate-neglect literature independently supports the direction, but the film doesn't cite it (card exclusion territory: keep it one scenario). |
| B05/B09 | "99% accurate" meaning both directions | ✓ simplification, defended | The film inherits the chapter's simplification: accuracy = 99% sensitivity AND 99% specificity. Real tests differ per direction — but naming that split is exactly the sensitivity/specificity vocabulary the card excludes. The counting stays valid under the stipulation. |
| B11 | "the ingredient intuition always forgets… the base rate" | ✓ chapter's thesis | Chapter: "Your intuition forgot the prior. Almost all intuition, in my experience, forgets the prior." "Always" in narration is the chapter's own rhetorical register — acceptable; soften to "almost always" if it grates at the gate. |

## Exclusions honored (from the candidate card)

No Bayes' theorem formula on screen (the counting IS the proof) · no sensitivity/specificity vocabulary anywhere · no odds-form shortcut · no second domain example (fraud/security/moderation stays in the book) · no real disease named.

## Rendering honesty checks

- **Countable-true law (the film's spine):** exactly 10,000 marks in the grid, exactly 1 blue, exactly 100 terracotta, exactly 101 in the pool. Anyone freeze-framing and counting must get the narrated numbers. No decorative dots.
- B04: the one blue dot placed off-center (not dead center — it should read as "somewhere in the crowd," not staged).
- B06: the 100 terracotta dots scattered pseudo-randomly with a fixed seed (reproducible renders), never clustered into a pattern.
- B07: the pool bucket holds 101 dots in tidy rows; the 1 blue sits visibly among them — NOT on top of the pile in a privileged spot… place it in-row, because in real life nothing marks it out. (Override of the beat-sheet's "1 blue on top" — in-row is the honest choice; the blue color already finds the eye.)
- B08: "≈1%" claim card carries the counting line as its attribution — the answer must trace to the count, not float as an assertion.
- B10: the 99 and the 1 must NOT be drawn as comparable bars on one axis — they answer different questions; two separate cards, no shared scale.
- B02 plate: synthetic (ai) — disclosure line in credits; no brand, no real lab name, no real disease.

## Chapter errata

None found — the section's arithmetic is exact and its framing is consistent. (The chapter's separate DeGrave 2021 distribution-shift citation carries its own [Verify] tag, but that claim is not in this film.)
