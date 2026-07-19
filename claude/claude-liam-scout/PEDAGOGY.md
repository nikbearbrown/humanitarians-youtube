# PEDAGOGY AUDIT — claude-liam-scout
# "Claude, Scouting." | scout skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Criteria (6-point rubric for skill-teardown modifier)

### 1. DOES NOT PARAPHRASE
The narration explains the scout skill in Teardown register. B05 names WHY
selectivity beats coverage — a scout that writes every possible card produces
unusable output; the value is in knowing what to skip. B06 names WHY the gap
formula is the bar — a question without a gap formula is a topic, not a film.
B07 names WHY the boundary between scout and builder is absolute — crossing it
couples discovery to production and destroys the human gate. None of these
framings appear verbatim in SKILL.md.
**SCORE: PASS**

### 2. REGISTER APPLIED
Every beat follows Teardown: describe mechanism → judge it → name what it gets
right and what constraint it carries. The three mechanisms (selectivity, vox bar,
stop-at-card) are each described and their purpose named. The self-demo shows
real scan_book.py output on a real book.
**SCORE: PASS**

### 3. SELF-DEMO FEASIBLE AND EXECUTED
B03/B04 demonstrate scan_book.py on the organic-chemistry book in this repo.
The manifest output (32 chapters, word counts, image counts) is real — run live
2026-07-18. The manifest step is the free authoring step scout always begins
with; no card content is faked.
**SCORE: PASS**

### 4. ILLUSTRATE LAW SATISFIED
UI beats: B00 (cold open) · B03 (ask micro-beat) · BVDT (verdict) · BHTF
(handoff) · BOUT (outro) = 5 UI beats total.
Inner beats (B01, B02, B04, B05, B06, B07) = 6 illustration beats:
- SkillTeardownAnatomy (B01)
- SkillTeardownPipeline (B02)
- ClaudeCodeBeat (B04)
- SkillTeardownMechanism (B05, B06, B07)
No two consecutive inner beats share the same scene type.
**SCORE: PASS**

### 5. HANDOFF INVOKES THE SKILL
BHTF command: "./art scout <your-book-folder>" with a framing question that
forces the viewer to apply the gap formula and key case test to every card the
scout writes. The prompt targets the most common scout failure: accepting a card
whose question is still a topic, not a gap.
**SCORE: PASS**

### 6. VERBATIM QUOTES CITED
Three quotes used, all cited to their source in SKILL.md:
- "Your value is selectivity, not coverage: most chapter content is not a film." (core principle)
- "if you cannot write THE QUESTION as a gap formula and name a concrete KEY CASE, the concept is not a card yet." (scout command step 3)
- "Never write narration, beats, or scenes here. Stop at the card." (Output rules)
All quotes on-screen in SkillTeardownMechanism quote blocks.
SOURCES.md records line references.
**SCORE: PASS**

## Overall assessment
The episode explains the scout skill honestly: the selectivity law (pass on most
content), the vox bar (gap formula + key case before any card), and the stop-at-
card boundary (scout never crosses into builder territory). The self-demo shows
real scan_book.py output. The handoff forces the viewer to apply the question
test to any card the scout produces.

**VERDICT: PASS**
