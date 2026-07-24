# PEDAGOGY AUDIT — claude-liam-terminal-screencast
# "Claude, Typed." | terminal-screencast skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Criteria (6-point rubric for skill-teardown modifier)

### 1. DOES NOT PARAPHRASE
The narration explains the terminal-screencast in Teardown register. B05 names
WHY the PROBLEM beat exists — a prompt without stakes earns nothing. B06 names
WHY the revision is structural — a demo without check-and-change teaches the
wrong loop. B07 names the receipt metaphor — if prompt/code/output aren't
plausibly connected, the viewer learns choreography, not building. None of
these framings appear verbatim in the SKILL.md.
**SCORE: PASS**

### 2. REGISTER APPLIED
Every beat follows Teardown: describe mechanism → judge it → name what it
gets right and what constraint it carries. The three laws (spine, revision,
actual-code) are each described and their purpose named. The receipt metaphor
in B07 is an editorial judgment, not a SKILL.md phrase.
**SCORE: PASS**

### 3. SELF-DEMO FEASIBLE AND EXECUTED
B03/B04 demonstrate the plan phase on UV catastrophe. The demo shows the beat
spine plan output (the free authoring step) — showing how the required spine
maps to the concept before any audio or code generates. No faked output.
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
BHTF prompt: "./art terminal-screencast '<your build concept>'" with a
framing question that forces the viewer to apply the problem+revision laws:
"what is broken about the world without this artifact, and what two things
would prove it works?" The prompt is read aloud.
**SCORE: PASS**

### 6. VERBATIM QUOTES CITED
Three quotes used, all cited to their source in SKILL.md:
- "show prompt → show code → show output" (core logic)
- "a CLI video without a check-and-change is incomplete." (The Revision Law)
- "The reel is a reconstruction of how the artifact was built with Claude: the ASK prompt must plausibly generate the code shown, and the code shown must plausibly produce the OUTPUT beat." (The Actual-Code Law)
All quotes on-screen in SkillTeardownMechanism quote blocks.
SOURCES.md records line references.
**SCORE: PASS**

## Overall assessment
The episode explains the terminal-screencast honestly: the spine law (problem
before prompts), the revision law (check-and-change is structural), and the
actual-code law (the receipt must be real). The self-demo shows a realistic
beat spine plan. The handoff forces the viewer to articulate the problem and
the checks before writing the first prompt.

**VERDICT: PASS**
