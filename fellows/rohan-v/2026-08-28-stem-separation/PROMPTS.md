# PROMPTS — "Stem Separation: Estimation, Not Extraction"

## Open slots: none

This reel has **no unfilled slots**. All 7 beats are machine-renderable.
`./art todo` should report an empty fill-list.

## Per-beat regeneration

```bash
python3 runtime/scripts/generate_audio_kokoro.py <reel> --only B01
ART_CONCURRENCY=4 python3 runtime/scripts/remotion_scenes.py <reel> --only B01 --force
python3 runtime/scripts/compile.py <reel> --height 2160
```

## Purpose-built scenes (this reel)

| Beat | Component | What it shows | Key design decision |
|---|---|---|---|
| B01 | `StemSepMixCollapse` | 4 colored tracks animate, then collapse into one combined gray waveform | The collapse animation is the thesis: individual contributions disappear into the sum |
| B02 | `StemSepStemOutput` | Mixed waveform fans into 3 output boxes with dashed borders + "PROBABILITY" badges | Dashed border + ghost bleed trace signals "estimate", not "recovered" |
| B04 | `StemSepBleedViz` | Vocal waveform with pulsing ghost drum trace + annotation + clean-vs-bleed comparison | Ghost trace pulses slightly to make the artifact visceral; comparison strip makes the difference explicit |

## Props for library scenes

| Beat | Component | Props summary |
|---|---|---|
| B00 | `ClaudeComposerAsk` | greeting "Hi, Rohan", segment "Stem Separation", 3 output lines, runningText "separating signals…" |
| B03 | `ClaudeWindow` | artifactTitle "Why unbaking is impossible", heading "Estimation, not extraction", 4 lines + sparkLine |
| B05 | `ClaudeWindow` | artifactTitle "The trust test", heading "Good enough vs. lying to you", 3 lines + sparkLine |
| B06 | `ClaudeTitleOutro` | title "Stem Separation: Estimation, Not Extraction", handle "@HumanitariansAI", subline "Rohan V." |

Full props are in `beat_sheet.json` under each beat's `shot.remotion.props`.

## The HAI standard for start and end screens

Per user instruction, all Humanitarians AI videos use:
- **Opener**: `ClaudeComposerAsk` — narration opens "Hi, I'm Rohan, for Humanitarians AI."
- **Outro**: `ClaudeTitleOutro` — `title` = video title, `handle` = "@HumanitariansAI", `subline` = "Rohan V."
  Narration closes: "I'm Rohan V., for Humanitarians AI."
