# Why Your Track Sounds Thin On A Phone

A non-technical explainer on mono fold-down: why a mix that sounds full in
headphones can come back thin on a phone, and the ten-second check that catches
it. One of the two week-04 STEM reels; the other is
[16-bit or 24-bit: What Bit Depth Does.](../2026-09-18-what-bit-depth-does/)

| | |
|---|---|
| **Runtime** | 2:05 |
| **Format** | 16:9 and 9:16, 4K (3840×2160 / 2160×3840), 30 fps |
| **Voice** | Kokoro `af_bella` — local, free, no API |
| **Beats** | 7 · 4 purpose-built scenes · 3 chassis/library · **no slates** |
| **Presenter** | Rohan V. |
| **Channel** | @HumanitariansAI |
| **Built with** | [brutalist.art](https://github.com/nikbearbrown/brutalist.art) |
| **Status** | Built and QC'd · **not published** |

## Through-line

**What survives one speaker is whatever sits in the middle.** Nothing breaks and
nothing is misconfigured: a single speaker has to add your two sides together
before it can move, and anything the two sides disagree about adds up to less
than it started as. The parts that live in the centre come through untouched.

## Written for someone who has never opened a DAW

The reel spends its first two body beats before the subject:

- **B01** — recorded music has two sides; headphones keep them apart; a phone, a
  laptop or a smart speaker is *one* speaker and has to add them together first.
  Nothing about phase, nothing about polarity.
- **B02** — two people pushing the same door. Push the same way and it swings.
  Push against each other, just as hard, and it does not move at all. Then the
  same picture as two waves.

The door has to actually move for this to work. A static diagram of two arrows is
a physics textbook; a door that swings and then refuses to is an argument. Full
vocabulary table in [PEDAGOGY.md](./PEDAGOGY.md).

## Every number measured

Two experiments, run before the script was written. `build_mono_signals.py` in
this folder; raw log [MEASUREMENTS.txt](./MEASUREMENTS.txt).

### Case 1 — the clean teaching case (B03)

A 20 s stereo track built for this: 110 Hz bass and 440 Hz vocal identical on
both sides, a 3 kHz layer inverted on the right. Measured per band, one side
alone and then summed to a single speaker:

| part | where it sits | one side | mono sum | change |
|---|---|---|---|---|
| 110 Hz bass | centre | −13.4 | −13.4 | **0.0 dB** |
| 440 Hz vocal | centre | −16.2 | −16.2 | **0.0 dB** |
| 3 kHz air | spread across both | −17.0 | −66.5 | **−49.5 dB** |

### Case 2 — what actually happens in practice (B04)

Broadband noise with the right side delayed 0.6 ms — how most stereo wideners
work. **The null positions were predicted first**, then measured:

| band | change | predicted |
|---|---|---|
| 400 Hz | −3.1 dB | slope |
| 830 Hz | **−10.2 dB** | NULL |
| 1660 Hz | −0.4 dB | peak |
| 2500 Hz | **−9.8 dB** | NULL |
| 3300 Hz | −0.6 dB | peak |

All four predicted positions landed. A delay cancels *some* frequencies and
spares others — which is exactly why a folded mix sounds hollow rather than
silent, and why the reel says **holes, not silence**.

The frequency table itself is *not on screen*. It was the most interesting thing
built for this reel and it was cut: a viewer meeting stereo for the first time
does not need a comb-filter chart. B04 shows the **shape** of the result on an
axis labelled only low-to-high, with no numbers. See
[FACTCHECK.md](./FACTCHECK.md) for all 18 claims and their verdicts.

## Word-clock choreography

Every reveal is timed to a **measured** spoken word, not a guessed fraction:

```
narration mp3 → align.py (faster-whisper) → mp3/words.json
              → cues.json (hand-authored: cue name → anchor phrase)
              → sync_cues.py → beat_sheet.json props.cues
```

28 cues authored, 28 resolved, 0 unmatched. Per-beat table in
[SHOTLIST.md](./SHOTLIST.md).

## 9:16 is a different render, not a crop

Four portrait siblings were written for this reel —
`MonoTwoSidesOneSpeaker916`, `MonoDoorToWaves916`, `MonoWhatSurvives916`,
`MonoHolesNotSilence916` — and `shorts.py` rewires the short's own beat sheet to
them (THE ONDA CHECK). Each re-lays the beat out for a tall frame; what changed
and why is in [SHOTLIST.md](./SHOTLIST.md#916).

## Files

| | |
|---|---|
| `beat_sheet.json` | the build contract — 7 beats, durations, components, props, cues |
| `cues.json` | cue name → anchor phrase, hand-authored |
| `mp3/` | Kokoro narration per beat + `words.json` word timings |
| `media/`, `clips/` | rendered 4K beats and their normalised clips |
| `short/` | the portrait beat sheet and its own `media/` |
| `_qc/` | Gate V frames and report |
| `build_mono_signals.py` | the signal builder, rerunnable |
| `MEASUREMENTS.txt` | both experiments' raw output, with the exact ffmpeg commands |
| `qc-sheet-16x9.png`, `qc-sheet-9x16.png` | contact sheets, both orientations |

The two 4K masters are **not** in git — they are in
[Google Drive](https://drive.google.com/drive/folders/1UBpIYX_NBcEpMebfTLbJYtmN7WYwZ3Kf)
under `2026-09-18/`. Only the docs and the build contract are committed.

## Rebuilding

```bash
./art final path/to/2026-09-18-why-tracks-sound-thin-on-a-phone
```

Everything is deterministic: no randomness at render time, so a rebuild produces
identical frames and the QC sheets stay comparable across builds.
