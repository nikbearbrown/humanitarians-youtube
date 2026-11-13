# The Mask Slips.

**CREATORS · THE AI INFLUENCER** · 13 beats · 2:48.3 · narrated by Yatra
(Kokoro `af_bella`, local and free) · `@Yatra`

## What this folder is

The **source** of the video, not the video. `beat_sheet.json` is the single source of
truth: every beat's narration, its measured audio duration, the Remotion composition that
renders it, and a `show` block describing what the viewer watches. Given the toolkit, this
folder rebuilds the episode from scratch — audio, frames and all.

Media (mp4/mp3/png) is deliberately not committed.

## What the episode argues

An AI persona went viral two days after it was created — 26,000 followers, 2.2 million
likes, and a reported $13,700 from a single video. Then the mask slipped. Once an account
is identified as AI, engagement does not merely wobble: one early account lost roughly
half of it, and another AI persona saw the same drop.

The episode's subject is that the reveal is the business risk, not the deception.

## The constraint this episode is built around

**One source supplies every figure: Garbage Day, October 2026.** Two disciplines are
enforced in the component types rather than by memory:

- `MskSpike`, `MskMoney` and `MskDrop` each **require** a `source` string. A number
  cannot reach the screen uncited, because the type will not permit it. `SourceLine`
  always renders in `MUTE`, never in the accent — a citation is provenance, not emphasis.
- **Every `value` is a string printed verbatim**, never a number formatted at render
  time. `$13,700` is never rounded or converted; `2.2 million` is never expanded to
  `2,200,000`; and **`roughly 50%` keeps its hedge**, because the supplied figure is
  approximate and the screen must not sharpen it.

The `$13,700` additionally carries a `reported` chip, because that is how the source
states it. No number appears anywhere in this reel beyond the supplied figures.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The 16:9 source of truth — narration, measured durations, scene + props per beat |
| `beat_sheet.short.json` | The 9:16 derivative, with each beat rewired to its portrait composition |
| `FACTCHECK.md` | The supplied figures, and how citation and verbatim wording are enforced |
| `PROMPTS.md` | Every prompt shown on screen, verbatim |
| `SHOTLIST.md` | Typed work order — measured durations, composition per beat |
| `CHECKS-REPORT.md` | PROOF GATE: per-beat classification and the teaching-arc checklist |
| `QC-LOG.md` | Frame-level visual QC and the GATE V verdict |
| `BUILD-PROMPT.md` | Paste-ready prompt that rebuilds the episode end to end |

## How to read it

Start with `FACTCHECK.md`. The episode paraphrases rather than quotes, by instruction, so
the fact-check is where the line between the source's claims and the narrator's reading is
drawn.

## Source

Garbage Day, October 2026 — cited on screen beside each figure.

## Rebuild

Free and local: Kokoro TTS, Remotion, ffmpeg. No API keys.

```bash
python3 runtime/scripts/generate_audio_kokoro.py <this-folder>   # audio is the master clock
python3 runtime/scripts/remotion_scenes.py <this-folder>          # render each beat
./art final <this-folder>                                         # compile the master
```

Regenerating audio changes the measured durations, so each composition's
`durationInFrames` must be retargeted to match, or progress-mapped animations get trimmed.

Scenes for this episode: `../scenes/MaskSlips.tsx` and `MaskSlips916.tsx`.
