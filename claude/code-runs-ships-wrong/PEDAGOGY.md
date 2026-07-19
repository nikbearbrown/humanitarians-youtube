# PEDAGOGY AUDIT — code-runs-ships-wrong

---

## Act Structure

| Act | Beats | Present? |
|-----|-------|----------|
| COLD OPEN | B01 | YES — Seth's sort bug: compiles, passes, wrong. Concrete situation, no thesis. |
| THE QUESTION | B02 | YES — "Audit said looks good. Why was it still wrong?" Named on screen AND in narration. |
| THE PROBLEM | B03–B04 | YES — Claude's genuine strength (pattern completion) and the fluency trap (plausibility-as-truth) |
| THE MECHANISM | B05–B06, B09 | YES — same weights = not independent; what an audit actually requires; solve/verify asymmetry |
| THE EXAMPLE | B07 (short), B11 (full) | YES — Priya's leaderboard; Run Two with all five moves |
| THE PRACTICE | B10 | YES — "Name the supervisory capacity before accepting the output" — concrete and checkable |
| RECAP | B12 | YES — "The model is fine. The supervision is missing." |

Order confirmed correct. ✓

---

## Key-Case Cold Open

B01 is a concrete instance: Seth's sort compiles, passes all tests, silently returns wrong order on a tie. Shown with specifics (Bell before Adams), not summarized. No thesis before B02. ✓

---

## Gap Formula — THE QUESTION Beat (B02)

"A working sort function should pass an audit of itself [X should predict Y]. Claude's function passed every test. Claude's own review said: looks good [here's the case where it didn't]. Why? [the question]"

On screen: "The audit said: looks good. / why was it still wrong?" ✓
In narration: "A working sort function should pass an audit of itself. Claude's function passed every test. Claude's own review said: looks good. Why did Bell rank above Adams when the spec required the opposite?" ✓

---

## Utility-Framing Lint

No "is critical for" / "important to understand" / "we'll cover" / "in this video" in narration. ✓
Mystery framing throughout — the anomaly (passes tests, ships wrong) opens the film. ✓

---

## Vocabulary Law

- "pattern completion" debuts at B03 with its first use (Claude's strength) ✓
- "plausibility auditing" debuts at B06/B10 after B05 establishes the same-weights limitation ✓
- "problem formulation" debuts at B10 after B08 shows the test/real-data gap ✓
- "supervisory capacity" debuts at B10 after B09 establishes the solve/verify split ✓

No term debuts before its setup. ✓

---

## Anchor-Not-Transcript Law

| Beat | On-screen | Narration | Redundant? |
|------|-----------|-----------|------------|
| B01 | "Compiled. Tests passed. Quietly wrong." | Full Seth story | No — card is the kicker; narration is the case |
| B02 | "The audit said: looks good. / why was it still wrong?" | Full question setup | No — card is the anchor phrase; narration is the argument |
| B06 | "An audit needs access to what Claude cannot see. / the spec that lives in your head" | Full architectural explanation | No — card is keyword anchor; narration carries the logic |
| B10 | "Name the supervisory move before you accept the output." | Full practice description with examples | No — card is the rule; narration is the how-to |
| B12 | "The model is fine. The supervision is missing." | "The model is fine. The supervision is missing..." | SAME LINE — this is intentional for the endcard kicker; it IS the recap line, matching chapter's last line. Acceptable as endcard. |

✓ All beats anchor correctly. Endcard repetition is standard practice.

---

## Simulation-First Check

B05 (same-weights diagram): the mechanism is structural (production and audit are the same operation), shown as an animated diagram with two arrows from one box — this is the most honest visualization of a structural constraint. ✓

B09 (solve/verify chart): two lines on a time axis, one rising steeply, one flat — the divergence animates in. ✓

B11 (Run Two): four steps animate in sequence, showing the process as it unfolds. ✓

---

## Length Law

Estimated duration: ~150s ≈ 2:30. Within 2–3 min band. ✓

---

## Practice Present

B10: "Before you accept a Claude output, name the supervisory capacity the step requires." Concrete (name the move), checkable (either you named it or you didn't). Not vague. ✓

---

VERDICT: PASS
