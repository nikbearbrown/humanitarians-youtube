# SOURCE-brief — "What MP3 Throws Away"

## What was asked for

Rohan asked for a second video for the week-02 submission, brief given
2026-09-04:

> The second video will be about another stem topic likely related to
> audio/music.

and then, when offered three candidates:

> Suggest a topic → **"What MP3 throws away (Recommended)"**

Plus the standing weekly constraints: 16:9 and 9:16, both 4K, docs to GitHub,
finished cuts to Drive.

## Why this topic was recommended

Three candidates were offered — lossy compression, why AI music sounds "off",
and loudness normalisation. Lossy compression was recommended because:

1. **It is the sibling of the stem-separation reel.** Both are about
   information that is *gone* rather than hidden. The channel is accumulating a
   coherent argument about what audio models and codecs can and cannot recover.
2. **It reuses the channel's visual language.** Spectrograms and frequency
   axes were already established by the week-00 spectrogram reel.
3. **It is immediately practical.** Lyrical Literacy volunteers export from
   Suno and have to pick a format. This changes what they do on export.
4. **It is falsifiable.** Unlike the other two candidates, every claim can be
   measured locally in minutes — which is what happened.

## What it was built from

**Not from recall.** The experiment was run before the beat sheet was written:

| Claim on screen | Where it came from |
|---|---|
| 128 kbps cliff at 16 kHz; 17 kHz down 13.2 dB | measured — ffmpeg + libmp3lame, band energy on decoded white noise |
| 320 kbps intact to 19 kHz | measured — identical to source at every band through 19 kHz |
| Ratios 11:1 and 4.4:1 | measured — real file sizes on disk |
| Byte counts | measured — `ls` on the encoded files |
| Generation loss, −7 dB at 12 kHz over 11 encodes | measured — iterative re-encode loop |
| Masking mechanism and its asymmetry | established psychoacoustics, drawn qualitatively with no numbers attached |
| 320 kbps transparency for most listeners | established listening-test result, stated as "almost everyone" |

Full log: [MEASUREMENTS.txt](./MEASUREMENTS.txt). Method and limits:
[SOURCES.md](./SOURCES.md).

## What the measurement changed

One drafted line did not survive contact with the data. An early version of B03
said 320 kbps "keeps everything." The measurement showed 20 kHz is 3.5 dB down,
so the line became "survives intact all the way to nineteen." The reel says what
was observed.

## What was deliberately excluded

- **No claim that 16 kHz is universal.** It is this encoder at these settings,
  and the B03 footnote says so on screen.
- **No numbers on the masking curve.** Masking thresholds were not measured
  here, so the curve carries no axis values.
- **No "MP3 is bad" framing.** B05 concedes 320 kbps is transparent for almost
  everyone. The argument is about *where* lossy belongs in a workflow, not
  against it.
- **No personal references beyond the presenter.**
