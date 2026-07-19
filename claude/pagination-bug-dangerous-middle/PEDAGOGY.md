# PEDAGOGY AUDIT — pagination-bug-dangerous-middle

---

## Act Structure

| Act | Beats | Present? |
|-----|-------|----------|
| COLD OPEN | B01 | YES — Seth's pagination: all tests pass, Avery's flashlight disappears. Specific (251 items, flashlight), no thesis before B02. |
| THE QUESTION | B02 | YES — "All tests passed. Why did 251 items fail in production?" Named on screen AND in narration. |
| THE PROBLEM | B03–B04 | YES — every test was a multiple of 50; bug fires at page_size × n + 1; the dangerous middle defined |
| THE MECHANISM | B05–B07 | YES — the joint between function and calling loop; the missing handoff condition; pre-condition shapes, post-hoc rationalizes |
| THE EXAMPLE | B08 | YES — Priya's leaderboard: 41 players, 41st never appears |
| THE PRACTICE | B09 | YES — write the non-obvious case (page_size × n + 1) before shipping |
| RECAP | B10 | YES — the most dangerous output passes every test you thought to write |

Order confirmed correct. ✓

---

## Key-Case Cold Open

B01: Seth's pagination function: tests at 50, 100, 247 items all pass. He commits. Six days later, Avery joins with 251 items. The 251st item — a flashlight — is on no page. Concrete (Avery, flashlight, 251 items). No thesis before B02. ✓

---

## Gap Formula — THE QUESTION Beat (B02)

"All tests passed [X should predict Y]. Seth's did [the case where it didn't]. Why did 251 items fail? [the question]"

On screen: "All tests passed. / Why did 251 items fail in production?" ✓
In narration: "Every test Seth wrote passed. The function compiled. The code was clean. Why did it fail the moment the inventory had 251 items?" ✓

---

## Utility-Framing Lint

No "is critical for" / "important to understand" / "we'll cover" / "in this video" in narration. ✓
Mystery framing: the anomaly (all tests pass, production fails on one case) opens the film. ✓

---

## Vocabulary Law

- "dangerous middle" — debuts B04 after B01-B03 establish the specific failure
- "handoff condition" — debuts B06 after B05 establishes the joint failure

No term before its setup. ✓

---

## Anchor-Not-Transcript Law

| Beat | On-screen | Narration | Redundant? |
|------|-----------|-----------|------------|
| B01 | "Compiles. Passes all tests. / Six days later: Avery's flashlight / doesn't exist." | Full Seth story | No — card is the kicker; narration is the case |
| B02 | "All tests passed. / Why did 251 items fail in production?" | Full question argument | No — anchor phrase vs full argument |
| B04 | "250 items: passes. / 251 items: bug fires. / The gap is one item." | Full dangerous-middle definition | No — card is the numbers anchor; narration carries the definition |
| B07 | "Write the handoff condition / before Claude runs the step. / Not after." | Full argument about pre vs post | No — card is the kicker; narration carries the argument |
| B10 | "The most dangerous output / is the one that passes every test / you thought to write." | Full recap | Near-match as endcard; acceptable — card is the compressed kicker |

All clean. ✓

---

## Simulation-First Check

B03 (test gap): number line of inventory sizes — multiples of 50 shown in INK (tests pass), 251 shown in CRIMSON (bug fires). Gap between 250 and 251 labeled. Process drawn left to right as numbers accumulate. ✓

B04 (accumulate motion): three rows accumulate: "250 items: passes" → "251 items: bug fires" → "The gap is one item." Each row appears as confirmation of the previous. ✓

B06 (handoff condition): condition text animates in as one unit — the missing sentence that would have caught the bug. Contrasted with the absent "weak" alternative ("tests pass"). ✓

B09 (practice): three steps animate in — before shipping → write the non-obvious case → run it. With page_size × n + 1 as the formula. Process sequential. ✓

---

## Length Law

Estimated duration: ~210s ≈ 3:30. Within 2–4 min band. ✓

---

## Practice Present

B09: "Before you ship any paginated output — or any function with a termination condition — write the non-obvious case. Not the round number. The round number plus one. Ask: what is the smallest input where this could be wrong? Write the handoff condition for that input. Run it." Concrete (three named steps: ask, write, run), checkable. ✓

---

VERDICT: PASS
