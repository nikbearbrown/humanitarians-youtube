# PEDAGOGY AUDIT — tests-pass-user-fails

---

## Act Structure

| Act | Beats | Present? |
|-----|-------|----------|
| COLD OPEN | B01 | YES — Seth: 9/9 tests pass, reads SDD aloud, at-a-glance fails. Concrete (Seth, application tracker, insertion order). No thesis before B02. |
| THE QUESTION | B02 | YES — "Nine tests pass. Why did the build fail its user?" Named on screen AND in narration. |
| THE PROBLEM | B03–B04 | YES — Tests verify code against tests (not needs); Claude's self-generated tests inflate pass rates |
| THE MECHANISM | B05–B07 | YES — Hoare 1969 (correctness is relative to spec); three passes; Pass 3 cannot be automated |
| THE PRACTICE | B08 | YES — open SDD, read each user-need sentence aloud, check running build against each one |
| RECAP | B09 | YES — tests passing ≠ done; read user-need sentences aloud before every commit |

Order confirmed correct. ✓

---

## Key-Case Cold Open

B01: Seth finishes Phase 1 of his college application tracker. Nine tests pass. He re-reads the SDD aloud: "The user should be able to see at a glance which applications remain to submit and which are already in." Six applications in insertion order — at a glance fails. Concrete (Seth, college applications, insertion order). No thesis before B02. ✓

---

## Gap Formula — THE QUESTION Beat (B02)

"A test suite that passes all cases should confirm correctness [X should predict Y]. Nine tests passed [the case where it seemed to]. Why did the build fail the user? [the question]"

On screen: "Nine tests pass. / Why did the build fail its user?" ✓
In narration: "A test suite that passes all cases should confirm correctness. Nine tests passed. Why did the build fail the user?" ✓

---

## Utility-Framing Lint

No "is critical for" / "important to understand" / "we'll cover" / "in this video" in narration. ✓
Mystery framing: the anomaly (9/9 tests pass, build fails the user) opens the film. ✓

---

## Vocabulary Law

- "Pass 3" — debuts B06 after B05 establishes that correctness is a relation between code and spec. The three-pass sequence is introduced in B06, so Pass 3 is defined before being named in B07–B09. ✓
- "SDD" — used starting B01. Acronym is used but "spec" / "user needs section" are used interchangeably throughout to prevent opacity. Acceptable at this book's level. ✓

No term before its setup. ✓

---

## Anchor-Not-Transcript Law

| Beat | On-screen | Narration | Redundant? |
|------|-----------|-----------|------------|
| B01 | "npm test: 9 of 9 passing. / The build is done. / The user can't see their data at a glance." | Full Seth story | No — card is the kicker; narration is the case |
| B02 | "Nine tests pass. / Why did the build fail its user?" | Full question argument | No — anchor phrase vs full argument |
| B03 | "Tests verify code against tests. / The SDD named a need. / No test tested the need." | Full explanation | No — card is the compressed thesis; narration is the mechanism |
| B04 | "The tests passed. / The need was never tested. / These are not the same thing." | Full LLM-inflated-pass-rate argument | No — card is the kicker; narration is the context |
| B07 | "Pass 3 fails when the build is / functionally correct / and needfully wrong." | Full resolution story | No — card is the compressed principle; narration is the case resolution |
| B09 | "Tests passing is not done. / Done means the SDD's needs are met. / Read them aloud. Before you commit." | Full recap | Near-match as endcard — acceptable |

All clean. ✓

---

## Simulation-First Check

B06 (three passes): three stacked rows animate in sequence — Pass 1 functional, Pass 2 edge cases, Pass 3 SDD needs (read aloud). Each level appears with its label and a short descriptor. Process in time. ✓

B08 (practice): four steps animate in sequence — before you commit / open the SDD / read each user-need sentence aloud / check the running build against each one. Process sequential. ✓

---

## Length Law

Estimated duration: ~177s ≈ 2:57. Within 2–3 min band. ✓

---

## Practice Present

B08: "Before you commit, open the SDD to the User Needs section. Read each sentence aloud. After each sentence, look at the running build and ask: does a user who has not just built this experience the sentence as true?" Concrete (open SDD, read aloud, check build), checkable. ✓

---

VERDICT: PASS
