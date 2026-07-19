# PEDAGOGY AUDIT — prompt-is-a-wish-spec-is-a-contract

---

## Act Structure

| Act | Beats | Present? |
|-----|-------|----------|
| COLD OPEN | B01 | YES — Seth's one-sentence prompt → broken MD5 function. Concrete, shown with specifics. No thesis before B02. |
| THE QUESTION | B02 | YES — "The request was clear. Why was the output broken?" Named on screen AND in narration. |
| THE PROBLEM | B03–B04 | YES — prompt-as-wish (Claude fills from training distribution); training distribution = the most common pattern |
| THE MECHANISM | B05–B07 | YES — specification-as-contract (names invariants, boundary); six sentences worked example; Claude's clarifying question |
| THE EXAMPLE | B08 | YES — Tomas: prompt vs spec side-by-side comparison |
| THE PRACTICE | B10 | YES — four pre-spec steps: decide, read, name boundary, write handoff condition |
| THE IMPLICATION | B11 | YES — time vs quality; boondoggle named |
| RECAP | B12 | YES — prompt is a wish; spec is a contract |

Order confirmed correct. ✓

---

## Key-Case Cold Open

B01: Seth's prompt produces a specific, concrete broken function (MD5, global dict, empty strings, 12 lines). Shown with specifics, not summarized. No thesis before B02. ✓

---

## Gap Formula — THE QUESTION Beat (B02)

"A prompt should specify the task clearly enough to get the right output [X should predict Y]. 'Write me a login function' is a clear request [the case where it didn't]. Why? [the question]"

On screen: "The request was clear. / why was the output broken?" ✓
In narration: "A prompt should specify the task clearly enough to get the right output. 'Write me a login function' is a clear request. Why did it produce a function that would fail in production?" ✓

---

## Utility-Framing Lint

No "is critical for" / "important to understand" / "we'll cover" / "in this video" in narration. ✓
Mystery framing: the anomaly (clear request, broken output) opens the film. ✓

---

## Vocabulary Law

- "prompt" — debuts B01/B02 as the thing that failed
- "specification" — debuts B05 after B03-B04 establish why the prompt fails
- "invariants" — debuts B05 within the specification definition
- "boundary" — debuts B05 within the specification definition
- "handoff condition" — debuts B10 after B09 establishes that the decision is the work
- "boondoggle" — debuts B11 after the time/quality contrast is established

No term before its setup. ✓

---

## Anchor-Not-Transcript Law

| Beat | On-screen | Narration | Redundant? |
|------|-----------|-----------|------------|
| B01 | "One sentence. Twelve lines. Broken." / "same Claude, six sentences later: production-ready" | Full Seth story | No — card is the kicker; narration is the case |
| B02 | "The request was clear." / "why was the output broken?" | Full question argument | No — anchor phrase vs full argument |
| B04 | "Claude completed the most common pattern." / "the most common pattern is not production code" | Full explanation | No — anchor pair vs full mechanism |
| B09 | "The decision is the work." / "the typing is the easy part" | "The prompt is what you say to Claude before you have decided..." | No — card is the kicker; narration is the definition |
| B11 | "6 seconds: a boondoggle." / "20 minutes: something to put your name on" | Full time/quality comparison | No — card is the numbers anchor; narration carries the argument |
| B12 | "A prompt is a wish. A spec is a contract." | "The prompt is what you wish for. The specification is what you contract for." | Near-match on the kicker line — acceptable as endcard; the card abbreviates, narration carries the third sentence |

All clean. ✓

---

## Simulation-First Check

B03 (prompt divergence): one prompt → six different possible outputs, shown as fan of arrows. Process animated left to right. ✓

B05 (spec → one output): spec elements list in, arrow to one output. Contrasts with B03 visually. ✓

B06 (six sentences): sentences animate in one by one as the contract builds. Process in time. ✓

B10 (four steps): steps animate in sequence with arrows. ✓

---

## Length Law

Estimated duration: ~150s ≈ 2:30. Within 2–3 min band from card. ✓

---

## Practice Present

B10: "Decide what you're building. Read what exists. Name the boundary. Write the handoff condition before any code is written." Concrete (four named steps), checkable (either you did each or you didn't). Not vague. ✓

---

VERDICT: PASS
