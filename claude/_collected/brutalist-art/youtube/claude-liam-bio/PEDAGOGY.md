# PEDAGOGY AUDIT — claude-liam-bio
# "Claude, Chronicling." | bio skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Criteria (6-point rubric for skill-teardown modifier)

### 1. DOES NOT PARAPHRASE
B05 names WHY every beat's duration equals its narration length exactly — this is not a style choice; it is what lets compile.py drop footage on the right cuts. Animation time added on top of a beat's budget causes drift and shot overhang. The clip is B-roll, not lip-synced, so the narration IS the timeline.
B06 names WHY the alternating clip/card structure is enforced — photoreal opens and closes with soul-id beats; the Manim dark cards carry dates and words that footage cannot carry cleanly. Without the alternation, the bio collapses into either pure talking-head B-roll or a text-heavy slideshow.
B07 names WHY length is an output, not a target — a figure with one clean idea needs ~30s; a layered life may need ~5 minutes. Compressing a beat below the consolidation floor to hit a clock doesn't make it shorter; it makes it fail to register. Never pad, never compress.
**SCORE: PASS**

### 2. REGISTER APPLIED
Every beat follows Teardown. Three mechanisms each described and judged. The self-demo produces a real Phase 2 beat sheet for Ada Lovelace (1815–1852) with clip/card alternation, soul-id placement, and the verbatim Note G quote verified against the source.
**SCORE: PASS**

### 3. SELF-DEMO FEASIBLE AND EXECUTED
B03/B04 demonstrate Phase 2 beat sheet authoring for Ada Lovelace — 5 beats, short length, alternating structure with soul-id open and close, world clip, title card, quote card. Phase 3 (Higgsfield clips) is paid and out of scope for the free pipeline demo. The beat structure and narration lines are real and complete. Not faked.
**SCORE: PASS**

### 4. ILLUSTRATE LAW SATISFIED
UI beats: B00 · B03 · BVDT · BHTF · BOUT = 5.
Illustration beats: B01 (Anatomy) · B02 (Pipeline) · B04 (Code) · B05/B06/B07 (Mechanism) = 6.
No two consecutive inner beats share same type.
**SCORE: PASS**

### 5. HANDOFF INVOKES THE SKILL
BHTF command: "./art bio <figure>" with two forcing questions:
can you state the who/why/impact in narration only (no lip-sync), and does Higgsfield have a Soul ID already trained for the figure? These target the two most common failures: narration that expects the footage to carry the story (they're decorative B-roll, not active carriers), and assuming a soul-id exists when it hasn't been trained yet.
**SCORE: PASS**

### 6. VERBATIM QUOTES CITED
Three quotes from SKILL.md:
- "Every beat's on-screen time — fade-out included — equals its narration length dur(bid) exactly." (timing contract)
- "Photoreal is the star; cards carry the dates and the words." (alternating structure)
- "Do not write to a 30-second (or any) clock." (length is output)
**SCORE: PASS**

**VERDICT: PASS**
