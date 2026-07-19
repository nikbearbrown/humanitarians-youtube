# PEDAGOGY AUDIT — claude-liam-claude-scout
# "Claude, Finding." | claude-scout skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Criteria (6-point rubric for skill-teardown modifier)

### 1. DOES NOT PARAPHRASE
The narration explains claude-scout in Teardown register. B05 names WHY the
brand-fit test must be strict — without it, the scout fills cards with general
theory that can't land on the composer screen. B06 names WHY source pointers
are mandatory — a card without a traceable premise is a guess, and a builder
working from a guess will produce a video that contradicts the book. B07 names
WHY the scout never crosses the gate — coupling discovery to production skips
the human approval step that the whole pipeline depends on. None of these
framings appear verbatim in SKILL.md.
**SCORE: PASS**

### 2. REGISTER APPLIED
Every beat follows Teardown: describe mechanism → judge it → name what it gets
right and what constraint it carries. The three mechanisms (brand fit, honest
cap, cards-only boundary) are each described and their purpose named. The
self-demo card is a real candidate from a real chapter.
**SCORE: PASS**

### 3. SELF-DEMO FEASIBLE AND EXECUTED
B03/B04 demonstrate a real candidate card from claude-code-for-students
Chapter 1 ("The Homework/Quiz Gap"). The chapter was read live on 2026-07-18;
the premise, slug, source pointer, ask-beat command, spine, and estimated
length in the card are all derived from the actual chapter content. No faked
output.
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
BHTF command: "claude scout <your-claude-book>" with a framing question that
forces the viewer to test their cards against two criteria: does the premise
survive without the chapter? Can you type the ask into the composer right now?
These target the two most common failures: circular premises that depend on
context, and asks that don't resolve to a composable command.
**SCORE: PASS**

### 6. VERBATIM QUOTES CITED
Three quotes used, all cited to their source in SKILL.md:
- "can the whole lesson land as callouts on one screen plus a typed ask?" (What qualifies)
- "Fewer honest cards beat padded lists — a book may legitimately yield 2." (Per book step 2)
- "No beat sheets, no audio, no renders, no publishing." (Hard rules)
All quotes on-screen in SkillTeardownMechanism quote blocks.
SOURCES.md records line references.
**SCORE: PASS**

## Overall assessment
The episode explains claude-scout honestly: the brand-fit test (UI as set, not
backdrop), the honest-card discipline (source-traced, capped), and the cards-
only boundary (gate is real). The self-demo shows a genuine candidate card
drawn from a real chapter. The handoff forces the viewer to apply the two
survival tests to any card the scout produces.

**VERDICT: PASS**
