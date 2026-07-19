# SOURCES — claude-liam-lyric-overlay
# "Claude, Overlaid." | lyric-overlay skill teardown

## Verbatim quotes (3 required by VERBATIM QUOTE LAW)

### Quote 1 — B05 (Mechanism · Act 1)
> "The audio is ground truth, and the audio comes from the video itself."
- Source: skills/make/lyric-overlay/SKILL.md — the one rule everything else serves
- Role: why audio is extracted from the .mp4, not brought in as a separate WAV; stated once, in B05

### Quote 2 — B06 (Mechanism · Act 2)
> "Picture and waveform can never drift, because they are the same recording."
- Source: skills/make/lyric-overlay/SKILL.md — the one rule
- Role: the guarantee that follows from extracting audio from the video; stated once, in B06

### Quote 3 — B07 (Mechanism · Act 3)
> "Edit the theme to restyle without touching timing."
- Source: skills/make/lyric-overlay/SKILL.md — theme.ts description
- Role: why all look decisions live in theme.ts — restyling never risks timing drift; stated once, in B07

## Self-demo source
- Phase: theming (theme.ts configuration) — no WAV file or video required
- Scenario: bright travel video with daytime exteriors
- Values: waveformMid=0.78 (lower band, out of sky), scrimOpacity=0.55, scrimHeight=0.35, accent='#FFFFFF', lyricStyle='outline'
- Rationale: all values derived from the documented knobs in SKILL.md; lyricStyle 'outline' chosen because current word shows bright background through outline rather than flat filled card
- Not faked: configuration follows the knob documentation exactly
