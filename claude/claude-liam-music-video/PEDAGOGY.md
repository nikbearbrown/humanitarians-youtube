# PEDAGOGY AUDIT — claude-liam-music-video
# "Claude, Synced." | music-video skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Criteria (6-point rubric for skill-teardown modifier)

### 1. DOES NOT PARAPHRASE
B05 names WHY analyze runs first — every animation length, cut, flash, and lyric hit is derived from the actual WAV via librosa; guessing the BPM or eyeballing lyrics produces timing that drifts from the actual music, and then the sync that makes a music video worth watching does not exist.
B06 names WHY design is inferred from the song rather than specified by default — bright timbre maps to cool color, high dynamic range disallows strobing flash caps, dense lyrics restrict which animation styles are safe. A synthwave palette on a sparse acoustic track doesn't match what the ear hears. The design is a response to the audio, not a preference.
B07 names WHY the media ask is sparing — Remotion can draw everything in code; asking for custom media for every beat defeats the point and costs the user Higgsfield budget on slots that a beat-reactive visualizer would serve better. Ask only where hand-made media genuinely beats code, with exact specs.
**SCORE: PASS**

### 2. REGISTER APPLIED
Every beat follows Teardown. Three mechanisms each described and judged. The self-demo produces a real Phase 4 plan section map with visualizer choices and media ask for a specified track profile.
**SCORE: PASS**

### 3. SELF-DEMO FEASIBLE AND EXECUTED
B03/B04 demonstrate Phase 4 plan output for a 128 BPM, bright, C-major dance track — section map with 4 sections named and visualizer assigned per section, beat-sync move list, and media ask (2 beats with specific files/specs, rest fully code-generated). This is the deliverable of the `plan` phase and requires no paid APIs. Not faked.
**SCORE: PASS**

### 4. ILLUSTRATE LAW SATISFIED
UI beats: B00 · B03 · BVDT · BHTF · BOUT = 5.
Illustration beats: B01 (Anatomy) · B02 (Pipeline) · B04 (Code) · B05/B06/B07 (Mechanism) = 6.
No two consecutive inner beats share same type.
**SCORE: PASS**

### 5. HANDOFF INVOKES THE SKILL
BHTF command: "./art music-video <wav>" with two forcing questions:
does the WAV exist (analyze needs the actual audio, not guessed timing), and is the look derived from the song (features → design.json) rather than from a preferred aesthetic? These target the two most common failures: starting with design before analysis, and defaulting to a synthwave look the track doesn't support.
**SCORE: PASS**

### 6. VERBATIM QUOTES CITED
Three quotes from SKILL.md:
- "The audio is ground truth." (the one rule)
- "muzak doesn't wait for a human to specify a palette: it derives a design from the audio and lyrics" (design seam)
- "Mostly code, media sparingly." (core rule)
**SCORE: PASS**

**VERDICT: PASS**
