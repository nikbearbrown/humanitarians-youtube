# PEDAGOGY AUDIT — claude-liam-shot-planner
# "Claude, Routing." | shot-planner skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Criteria (6-point rubric for skill-teardown modifier)

### 1. DOES NOT PARAPHRASE
B05 names WHY engagement and polish are not learning — the mechanism is the
illusion of understanding: slick animation buys high ratings and overestimated
comprehension without changing actual retention. Resistance to "what looks good"
is not a preference, it is a response to a measurable statistical effect.
B06 names WHY Manim is the mechanism default — not because animation teaches
better (the literature says it doesn't, d≈0.23–0.37 with no win over static
for understanding), but because Manim is schematic, pixel-precise, and
controllable: it can't hallucinate structure and enforces one-element-per-idea.
B07 names WHY the redundancy red flag is a BLOCK — baked-in verbatim text
alongside the same spoken words fires a penalty, not a bonus. It is not a
warning; it is a block.
**SCORE: PASS**

### 2. REGISTER APPLIED
Every beat follows Teardown. Three mechanisms each described and judged. The
self-demo produces real routing decisions from real beats.
**SCORE: PASS**

### 3. SELF-DEMO FEASIBLE AND EXECUTED
B03/B04 demonstrate routing two beats from the ai-1/ch07 script produced in
the previous teardown. Both beats were derived from actual chapter content
(log.csv table / failure phrase). Routing decisions are non-trivial: HOOK is
data → Remotion (correct default); INSTANCE is realworld but text-is-mechanism,
so override:design is applied and T2I is blocked by red flag 2 (generative for
mechanism). Not faked.
**SCORE: PASS**

### 4. ILLUSTRATE LAW SATISFIED
UI beats: B00 · B03 · BVDT · BHTF · BOUT = 5.
Illustration beats: B01 (Anatomy) · B02 (Pipeline) · B04 (Code) · B05/B06/B07 (Mechanism) = 6.
No two consecutive inner beats share same type.
**SCORE: PASS**

### 5. HANDOFF INVOKES THE SKILL
BHTF command: "./art route <beat_sheet.json>" with two forcing questions:
name the content_type of the hardest beat to route, and flag whether any beat
has baked-in narration text. These target the two most common failures:
content_type left missing (routing becomes guesswork) and the redundancy
red flag missed.
**SCORE: PASS**

### 6. VERBATIM QUOTES CITED
Three quotes from SKILL.md:
- "Engagement and polish are not learning." (governing principle)
- "Your job is to resist 'what looks good' and pick what the evidence supports." (the mandate)
- "It is not the default because animation 'teaches better.'" (honest Manim default)
**SCORE: PASS**

**VERDICT: PASS**
