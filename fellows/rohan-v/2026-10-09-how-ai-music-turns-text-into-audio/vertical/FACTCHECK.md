# FACTCHECK — How AI Music Generators Turn Text Into Audio

Every spoken and on-screen claim, its source, and its verdict. Checked 2026-10-10.
"The run" means `codec.py` → `evidence/run.log` / `evidence/codec.json` (SHA-256 in
`MEASUREMENTS.txt`). All music in the run is **synthetic** (`synth.py`); no copyrighted audio is
used. Outside facts were verified on 2026-10-10 and are recorded with quotes and URLs in
`week-07/_research/facts.md` (summarised in SOURCES.md).

| # | Beat | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | B00 | Opening line "Hi, I am … and this video is about …" | `docs/FELLOWS-SUBMISSION.md`, required wording | ✅ verbatim |
| 2 | B00 | AI narration disclosed | on-screen disclosure line + `metadata.ai_disclosure` | ✅ |
| 3 | B00 | Suno hasn't published how its own model works | no Suno paper or technical report found; blog posts describe features only (facts.md #14) | ✅ — the video never describes Suno's internals |
| 4 | B00 | Many published music generators turn sound into tokens and predict them one at a time | MusicGen, MusicLM, Suno's open-source Bark all predict audio tokens autoregressively (facts.md #12–#15) | ✅ "many", not "all": Stable Audio (diffusion) and MAGNeT (non-autoregressive) are exceptions |
| 5 | B01 | A CD stores 44,100 numbers every second for each ear | Compact Disc Digital Audio: 44.1 kHz, 16-bit, 2 channels (facts.md #9) | ✅ |
| 6 | B01 | A three-minute song is almost sixteen million numbers | 44,100 × 2 × 180 = 15,876,000, computed in `export_tok_data.py` | ✅ |
| 7 | B01 | The waveform shown is 4 ms of my test music, 96 numbers | the run's test piece at 24 kHz, samples from 2.0 s | ✅ |
| 8 | B02 | A codec cuts the sound into frames about a hundredth of a second long | the run: 256-sample hop at 24 kHz = 10.7 ms (on screen) | ✅ |
| 9 | B02 | A codebook of 1,024 typical sound shapes, learned from music | the run: k-means, 1,024 entries per codebook, trained on 36 synthetic pieces; EnCodec also uses 1,024-entry codebooks (facts.md #11) | ✅ |
| 10 | B02 | The number of the closest entry is the token; 0 to 1,023 | `encode()`: nearest entry by squared distance; the token on screen is the run's for that frame | ✅ |
| 11 | B03 | A second codebook codes what the first missed, a third what's left | residual vector quantization, as in SoundStream (2021) and EnCodec (2022) (facts.md #10, #11); `train_rvq()` | ✅ |
| 12 | B03 | Add the pieces and you get closer each time | run.log: residual energy 28.0% → 14.9% → 9.4% → 6.4% … of the original on training music; frame shapes in B03 are decoded from 1, 2, 4 codebooks | ✅ measured |
| 13 | B03 | About 94 frames a second; four codebooks = 375 tokens a second | 24,000 / 256 = 93.75; × 4 = 375 (typeset) | ✅ computed |
| 14 | B03 | Nearly 400 times less data than a CD | 375 × 10 bits = 3.75 kbit/s; 1,411.2 / 3.75 = 376 (typeset) | ✅ computed |
| 15 | B04 | Trained on 36 short pieces I generated; tested on a piece it had never heard | run.log: 36 tracks × 20 s training; test tracks use different seeds | ✅ |
| 16 | B04 | One codebook: treble down by 17 dB; twelve: less than 6 | run.log: treble (4–12 kHz) kept −16.7 dB at 1 codebook, −12.7 at 4, −5.6 at 12 | ✅ measured |
| 17 | B04 | One codebook sounds dull and smeared; four clearer | run.log SNR 4.3 → 9.0 → 12.5 dB; spectral centroid of the decodes 188 → 276 → 328 Hz vs 338 Hz original (BUILD-LOG §3) | ✅ measured; "dull" is the falling treble and centroid |
| 18 | B04 | The listening clips are 1, 4, 12 codebooks, then the original | `evidence/codec_01/04/12_books.wav`, `original.wav`, the same 3 s, level matched only (`mix_listen.py`) | ✅ |
| 19 | B05 | A music model reads tokens and guesses the next one | autoregressive token models (MusicGen, MusicLM, Bark) (facts.md #15) | ✅ |
| 20 | B05 | Mine counts which token follows each pair | `Trigram`: counts over pairs of previous coarse tokens, with backoff | ✅ |
| 21 | B05 | It guessed right 16.5% of the time on music it had never heard | run.log: 557 / 3,375 on the three unseen test pieces | ✅ measured |
| 22 | B05 | A blind guess is right one time in a thousand | 1 / 1,024 = 0.10%; always guessing the commonest token: 1.2% (on screen) | ✅ |
| 23 | B05 | Example row: 2 right out of 10 (the phone cut shows the last six: 2 of 6) | `lm_example`: the 12-token window of the unseen piece (from 4.0 s) whose hit rate is closest to the overall 16.5%, chosen by `codec.py` | ✅ measured; window selection stated |
| 24 | B06 | In published systems, a text encoder turns the prompt into numbers that steer every prediction | MusicGen conditions the token model on a T5 text encoder (facts.md #12) | ✅ |
| 25 | B06 | MusicGen: four codebooks, fifty frames a second, T5 | Copet et al. (2023), arXiv 2306.05284: 32 kHz EnCodec, 4 codebooks at 50 Hz, T5 encoder (facts.md #12) | ✅ |
| 26 | B06 | In my toy, the words only pick which music it learned from | `codec.py`: one trigram per labelled training set ("calm piano", "busy drums") | ✅ |
| 27 | B06 | Neither is copied: the longest stretch it repeats from training is a quarter of a second | run.log: longest copied run 0.26 s (piano, 101 seams) and 0.13 s (drums, 133 seams) | ✅ measured |
| 28 | B06 | The listening clips are the two generations | `evidence/generated_piano.wav`, `generated_drums.wav`, first 4 s each | ✅ |
| 29 | B07 | The words shift the odds, they don't write the notes | follows from B05–B06; true of token models conditioned on text | ✅ as explanation; Suno's own method not claimed |
| 30 | B07 | When sound is squeezed into tokens, the high end is the first thing to go | measured in my codec (B04: treble kept −16.7 dB at the lowest rate) | ✅ for codecs like mine; not claimed for Suno specifically |

## Algebra, checked separately from the typography (MATH-TYPESETTING.md)

- **Residual sum.** x_t ≈ C₁[k₁] + C₂[k₂] + C₃[k₃] + C₄[k₄]: frame t is approximated by the sum of
  one entry from each codebook; k_q is the token from codebook q. This is exactly `decode()`.
- **Rate.** 93.75 frames/s × 4 = 375 tokens/s; 375 × 10 bits = 3,750 bit/s = 3.75 kbit/s
  (1,024 entries = 2¹⁰, so 10 bits per token).
- **Against a CD.** 44,100 × 16 × 2 = 1,411,200 bit/s = 1,411.2 kbit/s; 1,411.2 / 3.75 = 376.3 ≈ 376.
  All four rows are computed in `export_tok_data.py` from the run's parameters, never typed in.

## Not claimed

- How Suno's model works, or that Suno uses tokens like these.
- That my toy is how real systems sound or perform: it is a trigram over 36 synthetic pieces.
