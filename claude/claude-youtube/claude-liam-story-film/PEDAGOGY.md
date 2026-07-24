# PEDAGOGY AUDIT — claude-liam-story-film
# "Claude, Narrating." | story-film skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Criteria (6-point rubric for skill-teardown modifier)

### 1. DOES NOT PARAPHRASE
B05 names WHY the narration is the master clock — audio is measured first; clip
length, cut timing, and caption timing all derive from real spoken durations.
Using word-count estimates instead means every downstream phase (video, captions,
assembly) is building against a guess, not a measurement.
B06 names WHY the pipeline is phase-gated and regenerates only the failing unit —
regenerating the whole batch wastes budget on what already passed. The gate
separates the cheap phase (stills) from the expensive one (video), so a failed
clip never triggers a full re-render.
B07 names WHY the skill documents its own incomplete state — build status is
honest because a skill that claims to do more than it can will produce silent
failures. The mid-build annotation is the integrity mechanism, not a caveat.
**SCORE: PASS**

### 2. REGISTER APPLIED
Every beat follows Teardown. Three mechanisms each described and judged. The
self-demo produces a real Phase 2 beat segmentation from a real text.
**SCORE: PASS**

### 3. SELF-DEMO FEASIBLE AND EXECUTED
B03/B04 demonstrate Phase 2 beat segmentation of Poe's "The Raven" (1845,
public domain). Three beats segmented from three spoken lines with scene
description, camera choice, style preset, and characters_present filled from
the actual poem content. Phase 1 audio not generated (requires ElevenLabs —
paid, out of scope for this free pipeline demo). Phase 2 work is complete and
genuine. Not faked.
**SCORE: PASS**

### 4. ILLUSTRATE LAW SATISFIED
UI beats: B00 · B03 · BVDT · BHTF · BOUT = 5.
Illustration beats: B01 (Anatomy) · B02 (Pipeline) · B04 (Code) · B05/B06/B07 (Mechanism) = 6.
No two consecutive inner beats share same type.
**SCORE: PASS**

### 5. HANDOFF INVOKES THE SKILL
BHTF command: "./art story <your-text.md>" with two forcing questions:
can each scene be stated as one narrated line, and which phase requires paid
generation? These target the two most common failures: beats with multiple
scenes crammed into one narration line, and expecting free pipeline output
from a paid-API skill.
**SCORE: PASS**

### 6. VERBATIM QUOTES CITED
Three quotes from SKILL.md:
- "The narration is the master clock." (audio-first principle)
- "one beat = one scene = one narrated line over one generated clip." (the one rule)
- "Safe to save as a work-in-progress snapshot; not yet a finished, end-to-end skill." (honest build status)
**SCORE: PASS**

**VERDICT: PASS**
