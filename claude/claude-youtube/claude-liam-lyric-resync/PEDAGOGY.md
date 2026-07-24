# PEDAGOGY AUDIT — claude-liam-lyric-resync
# "Claude, Recut." | lyric-resync skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Criteria (6-point rubric for skill-teardown modifier)

### 1. DOES NOT PARAPHRASE
B05 names WHY the audio is the master clock — beat timing comes from the real waveform (librosa), never a word-count guess. If a clip length is derived from a word count, it does not match the actual beat, and the resync fails at the frame level: the clip ends before or after the next line begins.
B06 names WHY Phase 4 is a vision step — the prompt for each beat is written by looking at BOTH the chosen still and its lyric line. Writing the prompt from only the lyric (without looking at the frame) produces a prompt that fights the source image; writing from only the frame (without the lyric) misses the line's meaning. The match requires both.
B07 names WHY the gates enforce single-unit regeneration — stills are cheap relative to Hailuo clips. If a clip fails, regenerate that clip only; the stills that passed are still valid. Regenerating the whole batch wastes Hailuo budget on already-approved beats.
**SCORE: PASS**

### 2. REGISTER APPLIED
Every beat follows Teardown. Three mechanisms each described and judged. The self-demo produces real Phase 4 work — an image_prompt and video_prompt written by examining a described still and its matching lyric line from "Scarborough Fair" (traditional English folk, public domain).
**SCORE: PASS**

### 3. SELF-DEMO FEASIBLE AND EXECUTED
B03/B04 demonstrate Phase 4 prompt writing for one beat from "Scarborough Fair" (traditional English folk song, public domain). The still description is concrete; the lyric is from the song; the image_prompt and video_prompt are written per the Phase 4 rule (preserve subject/pose/composition, push expression+light toward what the lyric means, never put lyric text in prompt). Phase 1-3 require a WAV file and video — out of scope for the free pipeline demo. Phase 4 prompt writing is the genuine free deliverable. Not faked.
**SCORE: PASS**

### 4. ILLUSTRATE LAW SATISFIED
UI beats: B00 · B03 · BVDT · BHTF · BOUT = 5.
Illustration beats: B01 (Anatomy) · B02 (Pipeline) · B04 (Code) · B05/B06/B07 (Mechanism) = 6.
No two consecutive inner beats share same type.
**SCORE: PASS**

### 5. HANDOFF INVOKES THE SKILL
BHTF command: "./art lyric-resync <video.mp4>" with two forcing questions:
is the audio locked (Phase 1 librosa beat grid runs before frames are extracted), and for each beat are you looking at the still AND the lyric line before writing the prompt? These target the two most common failures: deriving clip lengths from word counts instead of the real waveform, and writing the image prompt from the lyric alone without examining the source frame.
**SCORE: PASS**

### 6. VERBATIM QUOTES CITED
Three quotes from SKILL.md:
- "The audio is the master clock." (the one rule)
- "a human-or-model eye looked at both the picture and the words and decided they belong together" (Phase 4)
- "regenerate only the unit that failed, never the whole batch" (gates in one line)
**SCORE: PASS**

**VERDICT: PASS**
