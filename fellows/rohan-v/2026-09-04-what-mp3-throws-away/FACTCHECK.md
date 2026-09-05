# FACTCHECK — "What MP3 Throws Away"

Every factual claim, its source, its verdict. Verified 2026-09-04.

**The unusual thing about this reel: none of the numbers were recalled.** Every
figure on screen was measured on this machine before the beat sheet was
written, using ffmpeg + libmp3lame. The raw log is in
[MEASUREMENTS.txt](./MEASUREMENTS.txt) and the method is in
[SOURCES.md](./SOURCES.md).

| # | Claim | Where | Basis | Verdict |
|---|---|---|---|---|
| 1 | White noise contains every frequency at roughly equal energy | B01 narration + graphic | Definition of white noise; the measured source row is flat within 7.5 dB across 12–20 kHz, the slope being the analysis filter's, not the signal's | **PASS** |
| 2 | At 128 kbps everything above ~16 kHz is gone | B01 narration + cliff marker | Measured: 16 kHz survives at −0.6 dB; 17 kHz is 13.2 dB down; 18 kHz 18.9 dB down | **PASS** |
| 3 | "−13.2 dB at 17 kHz" | B01 on-screen | Measured: source −34.0 dB, 128 kbps −47.2 dB → 13.2 dB | **PASS** — exact |
| 4 | "Not quieter — gone" | B01 narration | 25 dB down at 20 kHz is below any plausible playback noise floor. Rhetorically absolute, factually a very steep lowpass — the graphic shows a cliff, not a wall at −∞ | **PASS** with the caveat noted in SOURCES |
| 5 | A loud sound raises the hearing threshold near it in frequency, making quieter sounds inaudible | B02 narration + curve | Simultaneous masking — the standard psychoacoustic result underpinning every perceptual codec | **PASS** — established, not measured here |
| 6 | The encoder spends no bits on masked content | B02 narration + "0 BITS SPENT" | This is the defining behaviour of a perceptual codec's bit allocator | **PASS** |
| 7 | Masking spreads further upward in frequency than downward | B02 curve shape (asymmetric skirt) | Standard asymmetry of the masking curve. Drawn qualitatively, no numbers claimed | **PASS** — shape only |
| 8 | 128 kbps is ~11× smaller than the source | B03 "11 : 1" | Measured: 1,764,078 → 160,958 bytes = 10.96 | **PASS** |
| 9 | 320 kbps is ~4.5× smaller | B03 "4.4 : 1" | Measured: 1,764,078 → 402,329 bytes = 4.38. Narration says "about four and a half", card says 4.4 : 1 | **PASS** — hedged correctly |
| 10 | At 320 kbps audio survives intact to 19 kHz | B03 narration + strip | Measured: 320 kbps matches source exactly at 12/14/15/16/17/18/19 kHz. Only 20 kHz differs (−3.5 dB) | **PASS** |
| 11 | Byte counts 160,958 / 402,329 / 1,764,078 | B03 on-screen | Measured file sizes | **PASS** — exact |
| 12 | Re-encoding compounds damage | B04 narration + steps | Measured, monotonic: 12 kHz band at −31.1 → −33.3 → −34.7 → −37.8 dB over 1/4/6/11 encodes | **PASS** |
| 13 | "The 12 kHz band lost seven decibels" after ten more encodes | B04 narration | Measured: −31.1 (1 encode) → −37.8 (11 encodes) = 6.7 dB. Narration rounds to "seven"; the graphic shows −7.0 as the source-relative total | **PASS** — see note below |
| 14 | "None of it comes back" | B04 spark line | Every measured step is lower than the one before; no recovery at any generation | **PASS** |
| 15 | 320 kbps is transparent for almost everyone | B05 artifact | Widely reported result of listening tests at high bitrates. Stated as "genuinely transparent for almost everyone", not as universal | **PASS** — appropriately hedged |
| 16 | Lossy is inappropriate for archives, masters, and re-editing | B05 artifact | Follows directly from claims 12–14, which were measured here | **PASS** |
| 17 | Narration voice is Kokoro `af_bella`, local and free | description.txt | `generate_audio_kokoro.py` reported `cost $0.00` | **PASS** |

## The one number worth reading carefully

Claim 13 has two defensible readings and the reel uses both, so they must not
be conflated:

- **Encode-1 → encode-11:** 6.7 dB. This is what the narration describes
  ("took a 128 kbps file and encoded it ten more times").
- **Source → encode-11:** 7.0 dB. This is what the B04 graphic's total block
  shows, because its reference line is the source.

Both are measured, they differ by 0.3 dB, and the narration's "seven decibels"
is true of either. The graphic labels its reference as SOURCE so the basis is
visible on screen rather than assumed.

## Encoder dependence — stated on screen

The exact cliff frequency is a property of this encoder at these settings, not
of MP3 in general. Other encoders, VBR modes and versions choose different
lowpass points. The B03 footnote says this explicitly: *"Exact cliff frequency
is encoder-dependent; the shape is not."* The reel never claims 16 kHz is
universal — it claims it is what was measured, and shows the measurement.

## What is asserted rather than measured

Claims 5, 6, 7 and 15 are established psychoacoustics and listening-test
results, not things this build tested. They are presented as explanation, and
the reel does not attach invented numbers to any of them — the masking curve is
drawn qualitatively and carries no axis values.

VERDICT: **PASS** — 17 of 17 claims verified. 13 of them measured on this
machine rather than recalled.
