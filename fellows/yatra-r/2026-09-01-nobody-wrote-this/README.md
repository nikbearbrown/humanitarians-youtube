# Nobody Wrote This.

**AI · SOCIAL PLATFORMS** · 14 beats · 2:48.4 · narrated by Yatra
(Kokoro `af_bella`, local and free) · `@Yatra`

## What this folder is

The **source** of the video, not the video. `beat_sheet.json` is the single source of
truth: every beat's narration, its measured audio duration, the Remotion composition that
renders it, and a `show` block describing what the viewer watches. Given the toolkit, this
folder rebuilds the episode from scratch — audio, frames and all.

Media (mp4/mp3/png) is deliberately not committed.

## What the episode argues

A scan of ~1 million long-form social posts found LinkedIn is the most AI-saturated major
platform measured — 41% of posts past 250 words fully AI-generated. The stranger finding is
the shape of it: only 4.3% are AI-assisted. It is all-or-nothing, not light editing.

The episode stress-tests its own headline rather than riding it: Substack (~10%) and Reddit
(4–13%) sit at the bottom of the same scan, so saturation is a platform choice, not
something AI does on its own.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The 16:9 source of truth — narration, measured durations, scene + props per beat |
| `beat_sheet.short.json` | The 9:16 derivative, with each beat rewired to its portrait composition |
| `FACTCHECK.md` | Claim-by-claim ledger: every figure, its citation, and what is deliberately not claimed |
| `SOURCES.md` | The two sources, where each citation renders, and the DOUBLE-CHECK rewrite log |
| `PROMPTS.md` | Every prompt shown on screen, verbatim |
| `SHOTLIST.md` | Typed work order — measured durations, composition per beat |
| `CHECKS-REPORT.md` | PROOF GATE: per-beat SHOW/HOLD/CARD classification and the teaching-arc checklist |
| `QC-LOG.md` | Frame-level visual QC, the four defects found and fixed, and the GATE V verdict |
| `BUILD-PROMPT.md` | Paste-ready prompt that rebuilds the episode end to end |
| `YOUTUBE.md` | Title, description, computed chapter timings, tags |

## How to read it

Start with `FACTCHECK.md`. It states what the episode claims and — more usefully — what it
refuses to claim and why.

Two refusals are enforced by the **types**, not by memory:

- The human-written share of LinkedIn posts is arithmetically available
  (`100 − 41 − 4.3`) and is **never shown**, because it was not published.
  `LnkAllOrNothing` has no remainder-bar prop — a bar length is a number, so refusing the
  prop is the only way to refuse the number.
- Three of the values are **ranges** (`25–29%`, `4–13%`). The house `num()` helper reads
  `"4–13%"` as `413`, so `LnkLadder` takes an explicit `bar` number separate from the
  verbatim `value` string. The printed figure is always the source's; the bar is only a
  drawing instruction. The midpoint rule is recorded in `FACTCHECK.md`.

## Sources

- Pangram Labs, "AI in Your Feed," July 2026
- Tech Times (EU AI Act, Article 50 — in force August 2, 2026)

## Rebuild

Free and local: Kokoro TTS, Remotion, ffmpeg. No API keys.

```bash
python3 runtime/scripts/generate_audio_kokoro.py <this-folder>   # audio is the master clock
python3 runtime/scripts/remotion_scenes.py <this-folder>          # render each beat
./art final <this-folder>                                         # compile the master
```

Regenerating audio changes the measured durations, so each composition's
`durationInFrames` must be retargeted to match, or progress-mapped animations get trimmed.

Scenes for this episode: `../scenes/NobodyWroteThis.tsx` and `NobodyWroteThis916.tsx`.
