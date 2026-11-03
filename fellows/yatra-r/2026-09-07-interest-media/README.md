# Interest Media.

**SOCIAL · THE SHIFT** · 13 beats · 2:29.6 · narrated by **Bella, in for Yatra**
(Kokoro `af_bella`, local and free) · `@Yatra`

## What this folder is

The **source** of the video, not the video. `beat_sheet.json` is the single source of
truth: every beat's narration, its measured audio duration, the Remotion composition that
renders it, and a `show` block describing what the viewer watches. Given the toolkit, this
folder rebuilds the episode from scratch — audio, frames and all.

Media (mp4/mp3/png) is deliberately not committed.

## What the episode argues

Social media stopped sorting your feed by **who you know** and started sorting it by
**what you're interested in** — a framing credited to Gary Vaynerchuk, who calls the result
*interest media* rather than social media.

The episode runs that claim on the viewer's own feed (when did it last show you your
cousin?), explains why the old sort key gave out (too much posted daily for a personal
network to surface the best of it), then draws the consequence for anyone making content:
followers used to be the gate on reach, and a post can now travel before an audience
exists. So the question stops being *how do I get more followers* and becomes *how do I
make something that earns attention on its own, one post at a time.*

## The two constraints this episode is built around

Both are enforced **structurally**, in the component types, rather than by discipline.

**1. Credited, never quoted.** The instruction was to credit Gary Vaynerchuk for the
framing and *not* quote him, because the script is already a paraphrase.

- `ItmSource` has a field called `claimParaphrase` and **no field called `quote`**.
- No component in the `Itm*` family renders quotation marks around attributed words.
- `stamp` is required and renders directly beneath the attribution, reading
  `PARAPHRASED — NOT A QUOTE`, so the disclaimer travels with the credit.

No date, venue, publication or link is cited for the framing either — none was supplied,
so none is invented. The credit is to a person for an idea, which is exactly what was given.

**2. No numbers at all.** This episode has no verified statistics behind it, so it claims
none. **There is no `value`, `pct`, `count`, `bar`, `stat` or `share` prop anywhere in the
`Itm*` family**, and nothing in either scene file computes a number and prints it.

The place that mattered most is `ItmVolume` (B04), whose entire subject is *volume* — the
one beat that invites a fabricated "X million posts per day." Its marks are unlabelled and
uncounted, it has no caption slot a figure could occupy, and its band reads
`more than a network can sort`, which is an ordering claim rather than a measurement.
`ItmJob`'s tick row is the same: marks for the phrase "one post at a time", not a tally.

Verified by regex sweep over every on-screen string in the beat sheet — **0 numerals**. The
one qualification, stated in `FACTCHECK.md` rather than glossed: the shared
`ClaudeVerdictArtifact` component numbers its five verdict lines `1.`–`5.` as list
furniture. Those digits enumerate sentences; they assert nothing.

## The narrator

This is the first episode on this channel where the voice is introduced as a **stand-in**.
B00 opens "Hello, this is Bella, in for Yatra, reading Yatra's notes this week," and B12
signs off the same way — IN-FOR-BEAR LAW in its Yatra form. Consequently the greeting slot
carries the **narrator's** name (`Vanakkam, Bella`) while the corner bug stays `@Yatra`,
exactly as `@NikBearBrown` stays the bug on a Liam-narrated reel.

If a later episode wants the greeting to read `Vanakkam, Yatra` instead, that is one field
in `beat_sheet.json` and a single beat re-render.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The 16:9 source of truth — narration, measured durations, scene + props per beat |
| `beat_sheet.short.json` | The 9:16 derivative, with each beat rewired to its portrait composition |
| `FACTCHECK.md` | Claim ledger, the attribution rules, and the numeral sweep |
| `SOURCES.md` | Where each claim comes from, and the DOUBLE-CHECK rewrite log |
| `PROMPTS.md` | Every prompt shown on screen, verbatim |
| `SHOTLIST.md` | Typed work order — measured durations, composition and accent per beat |
| `CHECKS-REPORT.md` | PROOF GATE: per-beat classification and the teaching-arc checklist |
| `QC-LOG.md` | Frame-level visual QC — seven defects found by looking, and their fixes |
| `BUILD-PROMPT.md` | Paste-ready prompt that rebuilds the episode end to end |
| `YOUTUBE.md` | Title, description, computed chapter timings, tags |

## How to read it

Start with `QC-LOG.md` on this one. Every defect in it was caught by reading rendered
frames, not by any numeric check — including a gate drawn overlapping the node it was
meant to sit *before*, and an endcard that shipped another channel's handle because
`shorts.py --handle` defaults to `@nikbearbrown`. It is a useful record of what the mp4
probe does not tell you.

## Source

- The "interest media" framing — **Gary Vaynerchuk**, paraphrased throughout, never quoted.
  No further citation was supplied and none is invented. See `SOURCES.md`.

## Rebuild

Free and local: Kokoro TTS, Remotion, ffmpeg. No API keys.

```bash
python3 runtime/scripts/generate_audio_kokoro.py <this-folder>   # audio is the master clock
python3 runtime/scripts/remotion_scenes.py <this-folder>          # render each beat
./art final <this-folder>                                         # compile the master
```

Regenerating audio changes the measured durations, so each composition's
`durationInFrames` must be retargeted to match, or progress-mapped animations get trimmed.

Scenes for this episode: `../scenes/InterestMedia.tsx` and `InterestMedia916.tsx`.

**For the vertical cut, two manual steps `shorts.py` will not do for you:** pass
`--handle "@Yatra"` (its default is `@nikbearbrown`), and regenerate the endcard PNG at
2160×3840 — `shorts.py` hardcodes it at 1080×1920, so a 4K compile upscales it. Both are
written up in `QC-LOG.md` and `BUILD-PROMPT.md`.
