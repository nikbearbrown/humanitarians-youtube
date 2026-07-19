# PEDAGOGY AUDIT — claude-liam-math-explainer
# "Claude, Derived." | math-explainer skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Criteria (6-point rubric for skill-teardown modifier)

### 1. DOES NOT PARAPHRASE
The narration explains the math-explainer pipeline in the Teardown register —
it does not recite the skill's non-negotiables verbatim. Each mechanism is
named, judged, and given context the SKILL.md doesn't state explicitly (e.g.,
WHY the equation tangent is structural rather than a style preference; WHY the
abstraction being a reward changes how the viewer receives a definition).
**SCORE: PASS**

### 2. REGISTER APPLIED
Every beat follows the Teardown register: describe the mechanism → judge it →
name what it gets right and where it bites. B05 names why the gate enforcement
is the real constraint (not aspirational). B06 explains why transform-don't-cut
is a causal argument, not a visual preference. B07 names what the equation
tangent signals about the skill's philosophy (explanation over proof).
**SCORE: PASS**

### 3. SELF-DEMO FEASIBLE AND EXECUTED
B03/B04 demonstrate the skill running on a derivative concept (why is d/dx(x²)
= 2x?). The demo shows the command, the mode-detection output, and a realistic
beat_sheet.json snippet with the 3b1b arc — MYSTERY → CONCRETE → TRANSFORM →
ABSTRACTION → TANGENT bracket. Since math-explainer requires ElevenLabs (paid)
and Manim rendering, the ClaudeCodeBeat shows the beat sheet output (the
authoring step, which IS free) rather than the rendered video. No faked output;
no screenshot.
**SCORE: PASS**

### 4. ILLUSTRATE LAW SATISFIED
UI beats: B00 (cold open) · B03 (ask micro-beat) · BVDT (verdict) · BHTF
(handoff) · BOUT (outro) = 5 UI beats total.
Inner beats (B01, B02, B04, B05, B06, B07) = 6 illustration beats using:
- SkillTeardownAnatomy (B01)
- SkillTeardownPipeline (B02)
- ClaudeCodeBeat (B04)
- SkillTeardownMechanism (B05, B06, B07)
No two consecutive inner beats share the same scene type.
**SCORE: PASS**

### 5. HANDOFF INVOKES THE SKILL
BHTF prompt: "./art math-explainer '<your why-does question>'" with a framing
question that makes the viewer apply the concrete-before-abstract law before
they open the terminal: "what concrete instance would make a viewer feel why
the abstraction is needed?" The prompt is read aloud in the narration.
**SCORE: PASS**

### 6. VERBATIM QUOTES CITED
Three quotes used, all cited to their source in SKILL.md:
- "Concrete before abstract — enforced, not aspirational." (non-negotiable #3)
- "transform, don't cut — objects morph; the algebra formalizes what was just seen moving" (comparison table)
- "Every equation fires the equation tangent." (non-negotiable #10)
All quotes are on-screen in SkillTeardownMechanism quote blocks.
SOURCES.md records line references.
**SCORE: PASS**

## Overall assessment
The episode explains the math-explainer skill honestly: it names the
concrete-before-abstract law as the signature constraint (gate-enforced, not
aspirational), shows the transform-don't-cut law as a causal argument, and
reveals the equation tangent as the design tell that signals the skill's
philosophy. The self-demo shows a realistic beat sheet with the 3b1b arc.
The handoff prompt is actionable and extends the episode's lesson into the
viewer's own work.

**VERDICT: PASS**
