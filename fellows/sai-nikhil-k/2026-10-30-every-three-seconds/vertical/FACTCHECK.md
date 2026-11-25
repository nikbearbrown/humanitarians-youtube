# FACTCHECK — Every Three Seconds

| # | Claim | Where | Checked against | Result |
|---|---|---|---|---|
| 1 | Until now Gavia only looked at photos; 0.4.0 listens to recordings | B00 | CHANGELOG 0.1.0–0.3.1 (photos only), 0.4.0 "Check an audio" | ✅ |
| 2 | It marks every three seconds where a loon calls | B00, B01 | looncall_v1.json `window_seconds: 3.0`; app: "Each bar is three seconds" | ✅ |
| 3 | Recording from Mount Desert, Maine: 2 calls, 4 of 8 stretches | B01, B06 | screenshot `app_audio_clean.png`; `listen.out` (4 windows ≥ 0.5); manifest: loon_2081153, "Oak Hill Rd, Mount Desert, ME", CC0 | ✅ observed |
| 4 | Click a call to hear it; save every stretch as a spreadsheet | B01 | screenshot: "Play call 1…", "Download CSV"; CHANGELOG 0.4.0 "a CSV of every stretch" | ✅ |
| 5 | Front page asks "is that a loon?"; takes almost any recording, even a video's sound | B01 | screenshot `app_audio_home.png`: "Is that a loon?", "WAV, MP3, FLAC, OGG or M4A, or a video's sound" | ✅ |
| 6 | Decode any format; mono; 48 kHz; 3 s back to back | B02, B03 | `src/calls/mod.rs`, `windows.rs` ("back to back from the first sample"), `decode.rs`; card `sample_rate: 48000` | ✅ |
| 7 | BirdNET 2.4 from the Cornell Lab of Ornithology | B02 | card: "BirdNET 2.4 … by the K. Lisa Yang Center for Conservation Bioacoustics" (part of the Cornell Lab of Ornithology) | ✅ |
| 8 | 1,024 numbers; a small classifier → one probability | B02, B03 | loonet README ("a 1024-number embedding"); `weights.npz` shapes (1024,) — `weights_npz.out` | ✅ |
| 9 | Nothing is sent | B02 | CHANGELOG 0.4.0: "runs on your computer and nothing is sent anywhere" | ✅ |
| 10 | 3 s × 48,000 = 144,000 samples | B03 | card input shape `[batch, 144000]`; asserted in build_beats.py | ✅ |
| 11 | z = ((x − μ)/σ)·w + b; P = 1/(1+e^(−z)) | B03 | loonet README: `p = sigmoid(((embedding - mean) / scale) · coef + intercept)`; reproduced on 325 clips (`drone_mix.out`) | ✅ |
| 12 | A loon at P ≥ 0.5, exactly when z ≥ 0; b ≈ −0.25 | B03 | card `defaults.threshold 0.5`; σ(0) = 0.5, monotone; `weights_npz.out` intercept −0.249714 | ✅ |
| 13 | Perfect 1.0 on val; windows picked by BirdNET (> 0.4 loon, < 0.02 not); the model card says so | B04 | loonet README "Scores"; `metrics.json` P = R = AP = 1.0 | ✅ |
| 14 | Through Gavia's Rust code: 28, 24, 19, 13 of 28 at clean/10/5/0 dB | B05, B00, B07 | `noise_check.out` | ✅ measured |
| 15 | 0 false alarms among the 37 other windows | B05, B07 | `noise_check.out` (0/37 at every level) | ✅ measured |
| 16 | Loonet's own Python agrees to within four millionths | B05 | `noise_check.out`: worst 0.000004 over 325 clips; `drone_mix.out` identical table | ✅ measured |
| 17 | At 0 dB the propeller is as loud as the recording | B05 | notebook gain: noise scaled to the window's own RMS ÷ 10^(SNR/20) → equal RMS at 0 dB | ✅ |
| 18 | Same recording + drone at 5 dB: 2 of 8, strongest 77% (clean 88%) | B06 | screenshots; `listen.out` (0.767 / 0.693 vs 0.885 max) | ✅ observed |
| 19 | Both calls still found; quieter halves fall below the line | B06 | app: 2 calls in both; windows 3–6 s (0.543 → 0.472) and 15–18 s (0.517 → 0.421) drop under 0.5 (`listen.out`) | ✅ |
| 20 | Non-commercial (BirdNET's licence); can't tell a wail from a tremolo | B07 | card licence CC-BY-NC-SA-4.0; card classes `["no loon", "common loon"]`; ROADMAP item 3 asked for call types | ✅ |

## The math (B03)

1. `n = 3 s × 48 000 Hz = 144 000`
2. `z = (x − μ)/σ · w + b`
3. `P = 1/(1 + e^(−z)) ≥ 0.5 ⇔ z ≥ 0`

Read from the source: the card's input shape (144,000) and threshold (0.5), and
loonet's README formula, whose arrays are `weights.npz` (mean, scale, coef:
1,024 each; intercept −0.2497). The equivalence in row 3: the logistic is
strictly increasing and equals ½ at 0. Asserted in `build_beats.py`.

**Reproducible numeric case:** `drone_mix.py` computes z and P with exactly this
formula from BirdNET 2.4 TFLite embeddings for 325 clips and reproduces loonet's
table (28/24/19/13/4 of 28); Gavia's ONNX graph gives the same P to 0.000004.
E.g. the clean Maine window at 12–15 s: P = 0.885 (`listen.out`) → z = ln(0.885/0.115) ≈ 2.04.

**Rendered-frame math review (both aspects):** _pending — fill in after render._
