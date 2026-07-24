# FACTCHECK — string-similarity-semantic-gap

---

## Claims Table

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B01 | Seth has a classifier; 12 test pairs; 85% accuracy; all pass | ✓ illustrative | Chapter 05: "twelve test pairs, and on those twelve pairs the function returns 85% accuracy. The tests pass." |
| B01 | He types hunting vs haunting; function returns 0.93 | ✓ illustrative | Chapter 05: "He types a new pair into the test file by hand. ('hunting', 'haunting'). The function returns 0.93." |
| B01 | Hunting = ghost actively chasing a player; haunting = ambient-presence tag | ✓ | Chapter 05: "One means the ghost is actively chasing a player. The other is the ambient-presence tag for when the ghost is unseen but pressuring the audio mix." |
| B03 | Claude's function uses difflib.SequenceMatcher with 0.7 threshold | ✓ illustrative | Chapter 05: "The function uses difflib.SequenceMatcher with a 0.7 ratio threshold, which Claude has explained in a comment Seth has read twice." |
| B03 | The frame was wrong: string similarity ≠ semantic equivalence | ✓ | Chapter 05: "The function is doing string similarity. What Seth needed was semantic equivalence over a fixed taxonomy. Those are not the same problem." |
| B04 | Claude wrote tests for the problem the function solves, not for the problem Seth needed | ✓ | Chapter 05: "Claude wrote tests for the problem the function solves, not for the problem Seth was trying to solve." |
| B05 | What stopped Seth was not a test failure — it was an itch | ✓ | Chapter 05: "What stops him is not a test failure. What stops him is an itch — a small, specific, hard-to-articulate wrongness located somewhere between his eye and the screen." |
| B07 | Plausibility auditing = hearing the wrong note before the proof is ready | ✓ | Chapter 05: "[PA] Plausibility Auditing — hearing the wrong note in output before any test confirms it." |
| B08 | Leila's quiz grader; photosynthesis vs cellular respiration; similarity 0.67 above threshold; grader marks correct | ✓ illustrative | video-ideas.md example seed for candidate 05 |
| B10 | Tests verify the problem Claude solved, not the problem you needed | ✓ | Chapter 05: "Plausibility auditing fails in exactly one way: when you delegate it... Tests are downstream verification. They do not replace upstream perception." |

---

## Illustrative Numbers

- Seth's 12 test pairs, 85% accuracy — illustrative (chapter 05)
- 0.93 similarity for hunting/haunting — illustrative (chapter 05)
- Leila's 10 test answers, 0.67 score — illustrative composite (video-ideas.md example seed)

---

## Terms Table

| Term | Debut beat | Prior beat creates need |
|------|-----------|------------------------|
| string similarity | B01 (implicit, the score) | B01 (the cold-open anomaly: it looks high but the states are different) |
| semantic equivalence | B03 | B03 (defined in contrast to string similarity after problem established) |
| plausibility auditing | B07 | B05-B06 (Seth's itch and probe demonstrated before the term is named) |

---

## Exclusions Confirmed

- NO full NLP embedding methodology ✓
- NO semantic similarity model comparisons ✓
- NO formal NLP task taxonomy ✓
- NO Polanyi epistemology at length ✓
- NO slopsquatting / package hallucination (that is candidate 08's topic) ✓
