# PEDAGOGY AUDIT — claude-liam-lyric-overlay
# "Claude, Overlaid." | lyric-overlay skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Criteria (6-point rubric for skill-teardown modifier)

### 1. DOES NOT PARAPHRASE
B05 names WHY the audio is extracted from the video rather than brought in separately — if you analyze a separate WAV, the composition's audio source and the video's embedded audio are two different recordings that can drift from each other. Because overlay_new.py extracts audio from the source mp4 and uses that same extracted track as the composition's only audio source, picture and waveform are guaranteed to be the same recording and can never drift.
B06 names WHY the scrim exists — the overlay's karaoke text and waveform must be legible over footage that was not designed to carry text. The scrim is a vertical gradient that darkens a horizontal band around the waveform's vertical position. Without it, white text and a thin waveform disappear over bright or busy footage. The knobs (waveformMid, scrimOpacity, scrimHeight) let the overlay adapt to any source video without re-rendering the original.
B07 names WHY the two-pass lyric timing strategy exists — the beat-grid seed spaces lines evenly across the real beat grid without knowing when each word is actually sung. It is good enough to preview layout and approve the look. Forced alignment (faster-whisper) puts each word on the frame it was actually sung. The seed pass is cheap; the forced alignment pass requires a model download. Run the seed first, approve the look, then run the final with --whisper.
**SCORE: PASS**

### 2. REGISTER APPLIED
Every beat follows Teardown. Three mechanisms each described and judged. The self-demo produces a real theme.ts configuration for a specific video scenario (bright travel footage) with documented knob values.
**SCORE: PASS**

### 3. SELF-DEMO FEASIBLE AND EXECUTED
B03/B04 demonstrate Phase 5 theming — a theme.ts configuration object with specific values for a bright travel video overlay. waveformMid=0.78 (lower band), scrimOpacity=0.55 (legible over bright sky), scrimHeight=0.35, accent=white, lyricStyle=outline (current word outlined, not filled, so bright background shows through). All values are taken from the knobs documented in SKILL.md. No paid APIs or WAV files required. Not faked.
**SCORE: PASS**

### 4. ILLUSTRATE LAW SATISFIED
UI beats: B00 · B03 · BVDT · BHTF · BOUT = 5.
Illustration beats: B01 (Anatomy) · B02 (Pipeline) · B04 (Code) · B05/B06/B07 (Mechanism) = 6.
No two consecutive inner beats share same type.
**SCORE: PASS**

### 5. HANDOFF INVOKES THE SKILL
BHTF command: "./art lyric-overlay <video.mp4>" with two forcing questions:
is the audio extracted from the video (not brought in separately), and has the seed-pass preview been approved before running --whisper forced alignment? These target the two most common failures: using a separate WAV that drifts from the video's embedded audio, and running forced alignment without first approving the layout.
**SCORE: PASS**

### 6. VERBATIM QUOTES CITED
Three quotes from SKILL.md:
- "The audio is ground truth, and the audio comes from the video itself." (the one rule)
- "Picture and waveform can never drift, because they are the same recording." (extraction rationale)
- "Edit the theme to restyle without touching timing." (theming pattern)
**SCORE: PASS**

**VERDICT: PASS**
