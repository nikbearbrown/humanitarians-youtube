# SOURCES — How AI Music Generators Turn Text Into Audio

All outside facts were verified on 2026-10-10; quotes and the exact claims checked are in
`week-07/_research/facts.md`.

## Executable evidence (this folder)

| Source | Used for |
|---|---|
| `synth.py` | 36 training pieces and 3 unseen test pieces in three styles; no copyrighted audio |
| `codec.py` → `evidence/run.log`, `evidence/codec.json`, `evidence/*.wav` | every token, curve, percentage and listening clip in B01–B06 |
| `export_tok_data.py` → `scenes/tokens/tokData.ts` (toolkit) | the scenes' data and the typeset equations |
| `mix_listen.py` | B04 and B06 audio: narration + the run's WAVs, level-matched |

## Methods

| Source | Used for |
|---|---|
| N. Zeghidour et al., "SoundStream: An End-to-End Neural Audio Codec", arXiv 2107.03312 (2021) | residual vector quantization in a neural codec |
| A. Défossez et al., "High Fidelity Neural Audio Compression" (EnCodec), arXiv 2210.13438 (2022) | RVQ; 1,024-entry codebooks; 75 frames/s at 24 kHz; 1.5–24 kbps |
| J. Copet et al., "Simple and Controllable Music Generation" (MusicGen), arXiv 2306.05284 (2023) | B06: EnCodec tokens, 4 codebooks at 50 Hz, a T5 text encoder conditioning one transformer |
| A. Agostinelli et al., "MusicLM: Generating Music From Text", arXiv 2301.11325 (2023) | coarse-then-fine generation (the shape of `codec.py`'s two-step generator) |
| Suno, Bark README, https://github.com/suno-ai/bark | Suno's 2023 open-source text-to-audio model: GPT-style, EnCodec tokens (background; not used to describe Suno's music model) |
| Stable Audio, arXiv 2402.04825; MAGNeT, arXiv 2401.04577 | why the narration says "many published generators", not "all" |
| Wikipedia, "Compact Disc Digital Audio" | B01, B03: 44.1 kHz, 16-bit, stereo = 1,411.2 kbit/s |

Not claimed: anything about how Suno's current music model works (no paper or technical report
found; Suno's blog posts describe features only).
