# SOURCES — claude-liam-lyric-resync
# "Claude, Recut." | lyric-resync skill teardown

## Verbatim quotes (3 required by VERBATIM QUOTE LAW)

### Quote 1 — B05 (Mechanism · Act 1)
> "The audio is the master clock."
- Source: skills/make/lyric-resync/SKILL.md — the one rule (unchanged)
- Role: why librosa runs before frame extraction; every clip length derives from the beat grid; stated once, in B05

### Quote 2 — B06 (Mechanism · Act 2)
> "a human-or-model eye looked at both the picture and the words and decided they belong together"
- Source: skills/make/lyric-resync/SKILL.md — Phase 4
- Role: why Phase 4 is a vision step — prompt requires examining both still and lyric simultaneously; stated once, in B06

### Quote 3 — B07 (Mechanism · Act 3)
> "regenerate only the unit that failed, never the whole batch"
- Source: skills/make/lyric-resync/SKILL.md — gates in one line
- Role: why single-unit regeneration at each gate prevents Hailuo budget waste on already-approved clips; stated once, in B07

## Self-demo source
- Song: Scarborough Fair — traditional English folk song, public domain
- Phase: 4 (prompt writing) — Phases 1-3 require WAV + video; Phase 4 reasoning is the free deliverable
- Beat: B03, lyric: "Parsley, sage, rosemary and thyme", duration_s: 5.2
- Still description: woman in grey-green linen dress, herb garden, golden hour, back to camera, hand trailing lavender stems
- image_prompt: preserve subject facing away; deepen golden light on sage and rosemary; lavender grey-green cool against warm soil
- video_prompt: subject stationary; camera drifts left past herb rows to rosemary and thyme in soft focus; land depth before cut; 5.2s
- Not faked: prompt pair written by applying Phase 4 rules to the described still and lyric line
