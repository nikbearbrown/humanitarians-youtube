# PEDAGOGY AUDIT — claude-liam-cli-scout
# "Claude, Hunting." | cli-scout skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Criteria (6-point rubric for skill-teardown modifier)

### 1. DOES NOT PARAPHRASE
The narration explains cli-scout in Teardown register. B05 names WHY the
BUILD/RESEARCH classification is done per concept, not per book — a humanities
book can have quantitative chapters and a CS book can have conceptual ones. B06
names WHY the artifact must be named before the prompt seed — an unnamed
artifact produces a prompt that optimizes for impressiveness rather than the
lesson. B07 names WHY motion is non-negotiable — a static png in the output
beat teaches a frame, not a process; the viewer came to watch a thing happen.
None of these framings appear verbatim in SKILL.md.
**SCORE: PASS**

### 2. REGISTER APPLIED
Every beat follows Teardown: describe mechanism → judge it → name what it gets
right and what constraint it carries. The three laws (BUILD/RESEARCH, artifact,
motion) are each described and their purpose named. The self-demo card is
derived from a real LLM exercise in a real chapter.
**SCORE: PASS**

### 3. SELF-DEMO FEASIBLE AND EXECUTED
B03/B04 demonstrate harvesting from java-programming Chapter 3 ("The
Conductor's Frame"), which has an explicit "## LLM Exercises" section. The
exercise was read live on 2026-07-18; the resulting BUILD lane card (GCD with
Euclidean algorithm, Manim curve output, fully synthetic) is derived from actual
chapter content. Not faked.
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
BHTF command: "./art cli-scout <your-book-folder>" with a framing question
that forces the viewer to name the artifact in one concrete sentence and verify
the output beat is motion. These target the two most common cli-scout failures:
writing vague artifact descriptions and naming a static png as the output.
**SCORE: PASS**

### 6. VERBATIM QUOTES CITED
Three quotes used, all cited to their source in SKILL.md:
- "can it be reduced to a script whose output is a deterministic computed artifact?" (The one classification)
- "If you can't name the artifact the run produces, it is not a CLI-video card yet." (Output rules)
- "A static png is never the output of a CLI video." (The prime rule)
All quotes on-screen in SkillTeardownMechanism quote blocks.
SOURCES.md records line references.
**SCORE: PASS**

## Overall assessment
The episode explains cli-scout honestly: the two-lane classification, the
artifact-first discipline, and the motion requirement. The self-demo harvests
a real LLM exercise from a real chapter and produces a complete BUILD lane
card. The handoff forces the viewer to apply both the artifact test and the
motion test before writing any card.

**VERDICT: PASS**
