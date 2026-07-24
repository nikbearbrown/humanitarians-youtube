# PEDAGOGY AUDIT — claude-liam-ai-explainer
# "Claude, Self-Taught." | ai-explainer skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Criteria (6-point rubric for skill-teardown modifier)

### 1. DOES NOT PARAPHRASE
The narration rewrites the skill's content in the Teardown register — it does not
parrot the SKILL.md. Each mechanism is explained in Kore's voice, judged honestly,
and given context the SKILL.md does not state explicitly (e.g., WHY the fidelity
palette choice works, not just THAT it exists).
**SCORE: PASS**

### 2. REGISTER APPLIED
Every beat follows the Teardown register: describe the mechanism → judge it →
name what it gets right and where it bites. B07 (design tell) explicitly names
what the fidelity choice gets right (the palette IS the instruction) and does not
oversell it. B05 names the failure case (wallpaper) before explaining the law.
**SCORE: PASS**

### 3. SELF-DEMO FEASIBLE AND EXECUTED
B03/B04 demonstrate the skill running on its closest sibling (sketch-explainer).
The demo uses a real command (`./art ai-explainer skills/make/sketch-explainer/SKILL.md`),
shows the actual output structure (a beat_sheet.json with real schema), and is
rendered natively via ClaudeCodeBeat — no screenshot, no fabricated output.
Feasibility note: the demo runs on a sibling skill, not recursively on itself,
which is the honest mirror move the SKILL.md names.
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
BHTF prompt: "Use the ai-explainer skill on a SKILL.md you've written or found…"
The prompt is read aloud verbatim in the narration, and the narration explains
WHY this prompt works (finding the line that doesn't belong in a summary = the
episode). The prompt is genuinely interesting and extends the episode's lesson
into the viewer's own work.
**SCORE: PASS**

### 6. VERBATIM QUOTES CITED
Three quotes used, all cited to their exact source in SKILL.md:
- "Two consecutive beats on the same visual scheme is the smell..." (ILLUSTRATE LAW)
- "A faked demo is a DOUBLE-CHECK LAW violation, not a shortcut." (SELF-DEMO LAW)
- "The moment it stops looking like the actual Claude app it loses its reason to exist." (FIDELITY BRAND)
All quotes are on-screen, cited once per figure. SOURCES.md records the line references.
**SCORE: PASS**

## Overall assessment
The episode explains the ai-explainer skill honestly: it demonstrates what the
pipeline actually does (not what it claims to do), names the laws that govern
the middle beats, and self-demos by running the skill on its nearest sibling.
The mirror move (this video IS the skill demonstrating itself) is named explicitly
in B00 so the viewer doesn't miss it. The design tell in B07 judges the fidelity
choice without overselling it.

**VERDICT: PASS**
