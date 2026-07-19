# PEDAGOGY AUDIT — claude-liam-explainer-deepen
# "Claude, Deepened." | explainer-deepen skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Criteria (6-point rubric for skill-teardown modifier)

### 1. DOES NOT PARAPHRASE
The narration explains explainer-deepen in Teardown register. B05 names WHY the
audit gate is bidirectional — passing videos are never rewritten, a point the
SKILL.md makes in "What NOT to do" but doesn't frame as a design choice. B06
names WHY the lift law discards pacing rather than carrying it forward — because
a longer version of the same prose is not depth. B07 names WHY instances (not
length) determine runtime — the depth is earned by pedagogy, not by adding beats.
None of these framings appear verbatim in SKILL.md.
**SCORE: PASS**

### 2. REGISTER APPLIED
Every beat follows Teardown: describe mechanism → judge it → name what it gets
right and what constraint it carries. The audit rubric (B05), lift law (B06), and
depth law (B07) are each described and their purpose named. The self-demo output
(B04) is a real audit result — not a mock.
**SCORE: PASS**

### 3. SELF-DEMO FEASIBLE AND EXECUTED
B03/B04 demonstrate the audit phase on claude-liam-sketch-explainer (video 2 of
this batch). The audit was run live via `scripts/audit.py` — the scorecard in B04
is the real output: 2 critical failures (no INSTANCE beats, missing equation
tangent), 5 warnings, verdict NEEDS-BB-CONVERSION. No faked output.
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
BHTF command: "./art explainer-deepen audit <your-doodle-folder>" with a framing
question that forces the viewer to find the one insight and name two instances
before writing anything. The prompt targets the two most common conversion
failures: pasting the doodle prose and padding with length.
**SCORE: PASS**

### 6. VERBATIM QUOTES CITED
Three quotes used, all cited to their source in SKILL.md:
- "Never 'convert' a video that already passes the audit." (What NOT to do)
- "you keep what it teaches, not how it sketched it." (convert step 2)
- "depth comes from instances and the tangent, never from padding." (convert step 3)
All quotes on-screen in SkillTeardownMechanism quote blocks.
SOURCES.md records line references.
**SCORE: PASS**

## Overall assessment
The episode explains explainer-deepen honestly: the audit gate (bidirectional —
stops the convert if it would be wasted), the lift law (concept not script), and
the depth law (instances + tangent earn runtime). The self-demo uses a real audit
on a real video in this batch with genuine scorecard output. The handoff forces
the viewer to name the insight and the instances before starting.

**VERDICT: PASS**
