# FACTCHECK — How Noise-Cancelling Headphones Work

Every spoken and on-screen claim, its source, and its verdict. Checked 2026-10-23. "The run" means `anc.py` →
`evidence/run.log` / `evidence/results.json` / `evidence/scene.json` (SHA-256 in `MEASUREMENTS.txt`). The
headphone is a **simulation** (my model: 48 kHz, an 83 µs acoustic lead, 125 µs electronic latency, a 128-tap
filtered-x LMS filter), and all noise is **synthetic**; no recording is used. Outside facts, with URLs and
confidence levels: `week-09/_research/facts-anc.md` (summarised in SOURCES.md).

| # | Beat | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | B00 | Opening line "Hi, I am … and this video is about …" | `docs/FELLOWS-SUBMISSION.md` | ✅ verbatim |
| 2 | B00 | AI narration disclosed | on-screen disclosure + `metadata.ai_disclosure` | ✅ |
| 3 | B00 | They can make an engine hum nearly disappear but still let you hear someone talking | ANC works mainly on low-frequency noise (Sony manual; NRC Canada 1993); speech is hard to cancel (WASPAA 2023) (facts-anc §4) | ✅ |
| 4 | B01 | Add the same wave flipped upside down and the two cancel; that copy is called anti-noise | destructive interference; Lueg's 1936 patent (US 2,043,416) describes it (facts-anc §1) | ✅ |
| 5 | B01 | The hum at the ear, the anti-noise my simulated headphone made, and what's left | run: 40 ms of `engine` at the ear after adapting (`scene.json`), drawn on one scale | ✅ measured |
| 6 | B02 | An outside microphone hears the noise first; a chip makes anti-noise for the speaker | feedforward ANC (Rivera Benois et al. 2018; Apple support: outward-facing mics) (facts-anc §2) | ✅ |
| 7 | B02 | Many headphones also have a microphone inside, listening to what's left | feedback / hybrid ANC; Apple: inward-facing mic (facts-anc §2) | ✅ |
| 8 | B02 | My simulated one keeps adjusting its filter 48,000 times a second | `anc.py`: normalised FxLMS update every sample at 48 kHz. Stated as my simulation's, because many commercial headphones use fixed, pre-tuned filters (facts-anc "do not say") | ✅ scoped |
| 9 | B02 | The noise takes 83 µs to reach the ear; the electronics take 125 µs | my model's parameters: D_P = 4, D_S = 6 samples at 48 kHz | ✅ (a model, stated as such) |
| 10 | B02 | So the chip has to predict a little of the future | with D_S > D_P the controller must anticipate; only predictable noise can be cancelled (causality; facts-anc §4) | ✅ |
| 11 | B03 | A 0.1 ms error is 3.6° of a 100 Hz wave; the hum still drops 24 dB | φ = 360°·f·t = 3.6°; residual 2·sin(φ/2) = 0.063 → −24.0 dB; run's simulated check −24.0 dB | ✅ computed and simulated |
| 12 | B03 | At 2,000 Hz the same delay is 72°, and the anti-noise adds to the noise | φ = 72°, residual 1.176 → +1.4 dB (simulated +1.4 dB) | ✅ |
| 13 | B03 | Past 60° there's no cancellation at all | 2·sin(30°) = 1: at 60° the residual equals the original; beyond it, louder (facts-anc §4) | ✅ |
| 14 | B04 | Engine hum 25 dB quieter; low rumble 31; voices only 11; clatter none, slightly louder | run: −25.5, −31.4, −11.2, +0.9 dB (last 4 s, after adapting) | ✅ measured on my simulation |
| 15 | B04 | Steady, low sounds are predictable, so the chip stays ahead; sudden sounds aren't | causality argument; speech partly unpredictable (WASPAA 2023) (facts-anc §4) | ✅ |
| 16 | B04 | The listening clip: the hum without, then with ANC | `evidence/engine_off_then_on.wav` (2 s off, 2 s on, one file, one gain, so the real difference stays) | ✅ |
| 17 | B05 | At least 10 dB quieter up to about 300 Hz; a little up to 3,000 Hz; above that slightly louder | run, pink noise in 1/3-octave bands: ≤ −10 dB up to 315 Hz; < 0 up to 3,150 Hz; +0.5 to +2.3 dB from 4 to 8 kHz | ✅ measured on my simulation |
| 18 | B05 | Real headphones handle the high sounds with the ear cups and tips | passive isolation is mostly effective above about 200 Hz; the two together cover the range (DAGA 2019; Canadian Acoustics 2002) (facts-anc §5) | ✅ |
| 19 | B06 | Use it for steady noise: planes, trains, air conditioning | steady low-frequency noise is where ANC works (facts-anc §4) | ✅ as advice |
| 20 | B06 | Get a good seal | passive isolation depends on the fit (facts-anc §5) | ✅ as advice |
| 21 | B06 | With the hum gone, turn your music down | WHO safe listening: noise-cancelling headphones so you don't need to raise the volume (facts-anc §8) | ✅ |

## Algebra, checked separately (MATH-TYPESETTING.md)

- **Phase from a timing error.** φ = 360° · f · t. Worked: 360° × 100 Hz × 0.1 ms = 3.6°; 360° × 2,000 Hz × 0.1 ms = 72°.
- **What is left.** A tone plus an equal, inverted copy shifted by φ leaves |1 − e^{jφ}| = 2·sin(φ/2) of the tone:
  2·sin(1.8°) = 0.063 (−24.0 dB); 2·sin(36°) = 1.176 (+1.4 dB); 2·sin(30°) = 1 at 60°. `anc.py` checks each
  against a simulated late copy and gets the same dB.

## Not claimed

- That the simulated numbers are any product's: they are my model's. Commercial measurements are about 15–21 dB
  with ANC on (DAGA 2019), not stated in the video.
- That ANC protects hearing on its own; that all headphones adapt in real time; who invented ANC.
