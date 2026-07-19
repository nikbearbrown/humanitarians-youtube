# SOURCES — claude-liam-logo
# "Claude, Stung." | logo skill teardown

## Verbatim quotes (3 required by VERBATIM QUOTE LAW)

### Quote 1 — B05 (Mechanism · Act 1)
> "The MP3 is the clock — and the jingle is NEVER cut."
- Source: skills/make/logo/SKILL.md — Law 1
- Role: the audio-first law applied to jingles; tail silence inside the beat protects the ring-out; stated once, in B05

### Quote 2 — B06 (Mechanism · Act 2)
> "Random once, then locked."
- Source: skills/make/logo/SKILL.md — Law 2
- Role: the stability rule; pick recorded in shot.remotion.picked; rebuild reuses lock; stated once, in B06

### Quote 3 — B07 (Mechanism · Act 3)
> "No TTS ever touches it."
- Source: skills/make/logo/SKILL.md — Law 5
- Role: reuse_audio: true on the LogoOutro beat; generate_audio.py measures, never synthesizes; stated once, in B07

## Self-demo source
- Phase: beat JSON output — showing the LogoOutro beat entry the logo script appends to beat_sheet.json
- Reference: representative LogoOutro beat with spring-entrance technique, bear-brown brand, 4.8s MP3 + 1.0s tail
- Output: JSON in B04 ClaudeCodeBeat showing all fields: beat_id, act, narration_text (empty), shot.remotion.pattern, picked, props (durationS/brand/svg/technique/tail), audio_file, reuse_audio, actual_duration_s
- Not faked: beat JSON matches the LogoOutro.tsx zod schema exactly; reuse_audio field is correct; all fields documented in SKILL.md
