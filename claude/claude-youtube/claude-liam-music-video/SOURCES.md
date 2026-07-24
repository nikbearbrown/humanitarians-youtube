# SOURCES — claude-liam-music-video
# "Claude, Synced." | music-video skill teardown

## Verbatim quotes (3 required by VERBATIM QUOTE LAW)

### Quote 1 — B05 (Mechanism · Act 1)
> "The audio is ground truth."
- Source: skills/make/music-video/SKILL.md — the one rule everything else serves
- Role: why librosa analyze runs first; every downstream phase reads beat_data.json; stated once, in B05

### Quote 2 — B06 (Mechanism · Act 2)
> "muzak doesn't wait for a human to specify a palette: it derives a design from the audio and lyrics"
- Source: skills/make/music-video/SKILL.md — the design seam
- Role: why design is inferred from audio features (brightness→color, dynamic range→cap, density→lyric style), not from aesthetic preferences; stated once, in B06

### Quote 3 — B07 (Mechanism · Act 3)
> "Mostly code, media sparingly."
- Source: skills/make/music-video/SKILL.md — core rules
- Role: why Remotion-generated visuals are the default and custom media is only asked for where it genuinely beats code; stated once, in B07

## Self-demo source
- Phase: 4 (plan output) — Phase 1 (librosa analyze) requires a WAV file; the plan is the deliverable of the free pipeline demo
- Track profile: 128 BPM, C major, high dynamic range, bright timbre, 4 sections
- Section map: Intro (minimal waveform), Verse (smooth waveform + medium lyrics), Chorus (spectrum bars + large hook type + beat flash), Outro (waveform trail)
- Beat-sync: cuts on downbeat ×4 per chorus; lyric style shifts to large type on hook
- Media ask: 2 beats only — B13 hero image (1920×1080 JPEG at first drop), B24 artist logo SVG (final hit); all other slots code-generated
- Not faked: section map, visualizer choices, and media ask all follow the decision logic documented in SKILL.md and references/motion-patterns.md
