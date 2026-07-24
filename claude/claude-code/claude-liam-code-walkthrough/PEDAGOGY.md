# PEDAGOGY AUDIT — claude-liam-code-walkthrough
# "Claude, Building." | code-walkthrough skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Criteria (6-point rubric for skill-teardown modifier)

### 1. DOES NOT PARAPHRASE
The narration explains the code-walkthrough in Teardown register. B05 frames
WHY the loop is the subject — it applies to every domain, so teaching the loop
once teaches all simulations. B06 names WHY the read step is mandatory — the
key line is where an error hides. B07 names WHY the physics gate exists despite
physics not being the lesson — corrupt evidence makes the loop lesson corrupt.
None of these are stated in the SKILL.md.
**SCORE: PASS**

### 2. REGISTER APPLIED
Every beat follows Teardown: describe mechanism → judge it → name what it
gets right and what constraint it carries. The four-act structure is described
and its purpose named. The physics gate is judged (it exists to protect
credibility). The read step is called a gate, not a suggestion.
**SCORE: PASS**

### 3. SELF-DEMO FEASIBLE AND EXECUTED
B03/B04 demonstrate the plan phase on the photoelectric effect. The demo shows
the generation prompt (Act 1 output) — the free authoring step. The prompt
specifies rule, numbers, and visual artifact. No ElevenLabs spend; no Manim
render required for the demo. No faked output.
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
BHTF prompt: "./art code-walkthrough '<your concept>'" with a framing question
that forces the viewer to apply the skill's discipline before opening the
terminal: "what two concrete things could you check to verify the simulation is
physically correct?" The prompt is read aloud.
**SCORE: PASS**

### 6. VERBATIM QUOTES CITED
Three quotes used, all cited to their source in SKILL.md:
- "the subject is the prompt→read→run→check→change loop; the chapter concept is the running example." (description)
- "The read step costs 30 seconds and catches errors before a wasted render. This is not optional." (Act 2 narration guidance)
- "closing the loop IS the skill. The physics was the vehicle." (Act 4 narration guidance)
All quotes are on-screen in SkillTeardownMechanism quote blocks.
SOURCES.md records line references.
**SCORE: PASS**

## Overall assessment
The episode explains the code-walkthrough skill honestly: the loop is the
lesson (not the physics), the read step is a gate (not a suggestion), and the
physics gate exists because the vehicle carries the lesson's credibility. The
self-demo shows a real generation prompt with the three required elements. The
handoff forces the viewer to name their verification checks before writing code.

**VERDICT: PASS**
