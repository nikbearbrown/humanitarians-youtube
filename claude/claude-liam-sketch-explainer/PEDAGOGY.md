# PEDAGOGY AUDIT — claude-liam-sketch-explainer
# "Claude, Sketching." | sketch-explainer skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Criteria (6-point rubric for skill-teardown modifier)

### 1. DOES NOT PARAPHRASE
The narration explains the sketch-explainer pipeline in the Teardown register — it does
not list the skill's commands verbatim. Each mechanism is named, judged, and given context
the SKILL.md does not state explicitly (e.g., WHY the accumulation law is pedagogically
sound, not just THAT it exists; WHY gates are a spend policy, not a ceremony).
**SCORE: PASS**

### 2. REGISTER APPLIED
Every beat follows the Teardown register: describe the mechanism → judge it → name what
it gets right and where it bites. B05 names why the accumulation law is the pedagogy
(causality visible). B07 explains what "optional" signals about what the pipeline trusts.
B06 reframes the gate system as a spend policy, not a workflow ceremony.
**SCORE: PASS**

### 3. SELF-DEMO FEASIBLE AND EXECUTED
B03/B04 demonstrate the skill running on an entropy concept (Mode B). The demo shows the
command (`./art sketch-explainer 'What is entropy?'`), the mode detection output, and a
realistic beat_sheet.json snippet with scene_state and new_element fields — the two fields
that enforce the accumulation law. The demo is rendered natively via ClaudeCodeBeat; no
screenshot, no fabricated output that misrepresents the schema.
**SCORE: PASS**

### 4. ILLUSTRATE LAW SATISFIED
UI beats: B00 (cold open) · B03 (ask micro-beat) · BVDT (verdict) · BHTF (handoff)
· BOUT (outro) = 5 UI beats total.
Inner beats (B01, B02, B04, B05, B06, B07) = 6 illustration beats using:
- SkillTeardownAnatomy (B01)
- SkillTeardownPipeline (B02)
- ClaudeCodeBeat (B04)
- SkillTeardownMechanism (B05, B06, B07)
No two consecutive inner beats share the same scene type.
**SCORE: PASS**

### 5. HANDOFF INVOKES THE SKILL
BHTF prompt: "./art sketch-explainer '<your concept>'" with framing that directs the
viewer to a specific starting question (what does the accumulation law force you to cut?).
The prompt is read aloud in the narration. The starting question is pedagogically active —
it makes the viewer apply the accumulation law before they open the terminal.
**SCORE: PASS**

### 6. VERBATIM QUOTES CITED
Three quotes used, all cited to their source in SKILL.md:
- "One sentence = one new visual element. No exceptions." (non-negotiable #4)
- "Never time animation from word-count estimates." (non-negotiable #1)
- "The finished video is Manim + voiceover. That is the complete, self-sufficient deliverable." (line 25)
All quotes are on-screen inside SkillTeardownMechanism quote blocks, cited once per figure.
SOURCES.md records the line references.
**SCORE: PASS**

## Overall assessment
The episode explains the sketch-explainer skill honestly: it names the accumulation law
as the signature mechanism, demonstrates it in action through a realistic beat_sheet.json
snippet, and shows why the optional/required distinction is the pipeline's real design tell.
The gate system is reframed as a spend policy (not a ceremony) — the kind of judgment the
SKILL.md implies but does not state. The handoff prompt is actionable and extends the
episode's lesson into the viewer's own work.

**VERDICT: PASS**
