# Both Sides of the Table.

**HIRING · AI VS AI** · 14 beats · 2:48.9 · narrated by Yatra
(Kokoro `af_bella`, local and free) · `@Yatra`

## What this folder is

The **source** of the video, not the video. `beat_sheet.json` is the single source of
truth: every beat's narration, its measured audio duration, the Remotion composition that
renders it, and a `show` block describing what the viewer watches. Given the toolkit, this
folder rebuilds the episode from scratch — audio, frames and all.

Media (mp4/mp3/png) is deliberately not committed.

## What the episode argues

Both sides of the hiring table now bring a machine. 86% of organizations use AI in hiring;
four in five job seekers use AI in their search. The interesting part is not that
adoption happened — it is what happens to trust when both parties know the other is
automated: 38% of candidates have walked away over an AI interview, and only 26% trust AI
to evaluate them fairly.

## The constraint this episode is built around

**Eight figures, from five different publishers.** That is the central risk here: six
numbers in one video read as a single dataset unless the reel actively works to stop them
doing so. The separation is enforced in the types, not by discipline:

- `TblSide`, `TblInterview`, `TblWalk` and `TblInject` each **require** a `source`
  string. A figure cannot be constructed without its citation.
- **`TblTrust` requires a separate source on *each* of its two figures.** The 26%
  (Greenhouse) and the 66% (Pew) come from different studies, asking different questions
  of different populations. The component has **no shared `source` field** that could
  imply they are one finding. They are never added, never merged, never summarised as a
  single claim.

No number appears anywhere in this reel, on screen or in narration, beyond the eight
supplied figures.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The 16:9 source of truth — narration, measured durations, scene + props per beat |
| `beat_sheet.short.json` | The 9:16 derivative, with each beat rewired to its portrait composition |
| `FACTCHECK.md` | The eight figures, their publishers, and how separation is enforced |
| `PROMPTS.md` | Every prompt shown on screen, verbatim |
| `SHOTLIST.md` | Typed work order — measured durations, composition per beat |
| `CHECKS-REPORT.md` | PROOF GATE: per-beat classification and the teaching-arc checklist |
| `QC-LOG.md` | Frame-level visual QC and the GATE V verdict |
| `BUILD-PROMPT.md` | Paste-ready prompt that rebuilds the episode end to end |

## How to read it

Start with `FACTCHECK.md`. With eight figures from five publishers, the fact-check is
where the episode's real work lives — not in what it claims, but in what it refuses to
let the viewer conflate.

## Sources

Gartner (via CI CoPilot) · Greenhouse · Greenhouse Candidate AI Interview Report ·
Pew Research Center · SelectSoftwareReviews — each cited on screen beside its own figure.

## Rebuild

Free and local: Kokoro TTS, Remotion, ffmpeg. No API keys.

```bash
python3 runtime/scripts/generate_audio_kokoro.py <this-folder>   # audio is the master clock
python3 runtime/scripts/remotion_scenes.py <this-folder>          # render each beat
./art final <this-folder>                                         # compile the master
```

Regenerating audio changes the measured durations, so each composition's
`durationInFrames` must be retargeted to match, or progress-mapped animations get trimmed.

Scenes for this episode: `../scenes/TableSides.tsx` and `TableSides916.tsx`.
