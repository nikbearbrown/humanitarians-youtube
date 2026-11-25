# FACTCHECK — How Auto-Captions Find Each Word

Every spoken and on-screen claim, its source, and its verdict. Checked 2026-11-01. "The run" means `captions.py` →
`evidence/run.log` / `evidence/results.json` / `evidence/scene.json` (SHA-256 in `MEASUREMENTS.txt`). The
recogniser is faster-whisper 1.2.1, model base, on the CPU with `word_timestamps=True`. The test speech is
**synthetic**: 24 everyday English sentences built word by word from our narrator's voice (Kokoro af_bella), so
every true word start is known; the noise is synthetic pink noise. No recording is used. B05's two clean-speech
examples are the voice reel's audio check (`2026-10-30-how-ai-voices-read-a-script/evidence/run.log`). Outside
facts, with URLs and confidence levels: `week-10/_research/facts-asr.md` (summarised in SOURCES.md).

| # | Beat | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | B00 | Opening line "Hi, I am … and this video is about …" | `docs/FELLOWS-SUBMISSION.md` | ✅ verbatim |
| 2 | B00 | AI narration disclosed | on-screen disclosure + `metadata.ai_disclosure` | ✅ |
| 3 | B00 | Our own videos depend on it; every animation here is timed by it | `align.py`: faster-whisper base gives each word's time, the known narration is matched onto it, `sync_cues.py` places every cue (`_audio.log`: "aligned 8, fallback 0"; "all anchors resolved") | ✅ |
| 4 | B01 | The sound becomes a spectrogram with eighty frequency bands | Whisper: 80-channel log-Mel spectrogram, 16 kHz, 25 ms windows, 10 ms hop (facts-asr §1.5); only large-v3 uses 128 (§1.6), not our base | ✅ |
| 5 | B01 | Read in thirty-second chunks | facts-asr §1.7 | ✅ |
| 6 | B01 | On screen: one test sentence as the model sees it | sentence 1, recomputed by `export_cap_data.py` the way Whisper's front end does (16 kHz, 400 / 160 samples, 80 Mel bands, clamped 8 log10 below the peak); a picture of the input, not the model's own tensor | ✅ |
| 7 | B01 | The model our videos use is Whisper | our pipeline runs faster-whisper, a CTranslate2 rebuild of Whisper (facts-asr §2.9); `align.py --model` defaults to `base` | ✅ |
| 8 | B01 | An open model first trained on 680,000 hours of audio from the web | facts-asr §1.1, §1.3; "first" because large-v3 used a different mix (§1.13); base is one of the original models | ✅ |
| 9 | B01 | It predicts the text one small piece at a time | encoder-decoder Transformer; the decoder predicts tokens (facts-asr §1.4, §1.10) | ✅ |
| 10 | B02 | It checks where in the sound it was looking while it wrote each word, and lines those moments up in order: dynamic time warping | cross-attention of chosen alignment heads + DTW, in openai/whisper and in faster-whisper / CTranslate2 (facts-asr §2.1, §2.3, §2.10, §2.11) | ✅ |
| 11 | B02 | One sentence: when each word really starts, and when Whisper says it starts | `scene.json`: "The train to Boston leaves from platform nine at noon"; true starts 0.255, 0.56, 1.127, 1.599 … s; Whisper's 0.0, 0.4, 0.88, 1.3 … s | ✅ measured |
| 12 | B03 | Twenty-four sentences from this narrator's voice, word by word, so I know when each word starts | run: "24 sentences, 238 words, 131 s of speech (Kokoro af_bella, word by word, true starts known)" | ✅ (choppier than a real read; stated as built this way in `captions.py`) |
| 13 | B03 | Whisper's base model, the one our pipeline uses | run: "recogniser faster-whisper base"; `align.py` default `base` | ✅ |
| 14 | B03 | 234 of the 238 words right | run, clean: "WER 1.7% … (234 words matched)"; `results.json` 4 substitutions, 0 deletions, 0 insertions; screen "234/238", "WRITTEN WRONG: 4" | ✅ measured |
| 15 | B03 | Its word starts came about a quarter of a second early | run, clean: "signed median -241 ms"; screen "0.24 s". **In my test**, on speech built word by word; not a general claim about Whisper | ✅ measured, scoped |
| 16 | B03 | Nine in ten were within three tenths of a second | run, clean: "90% within 302 ms"; screen "0.3 s" (302 ms, rounded) | ✅ measured (rounded) |
| 17 | B04 | Speech ten decibels louder than the noise: still ninety-seven percent of the words | run: "+10 dB SNR WER 2.9%" → 100 − 2.9 = 97.1% (232 of 238 matched) | ✅ measured |
| 18 | B04 | At five decibels, eighty-nine percent | run: "+5 dB SNR WER 10.9%" → 89.1% (214 matched) | ✅ measured |
| 19 | B04 | Noise as loud as the speech: an error rate of over seventy percent | run: "+0 dB SNR WER 73.1%"; the earlier run gave 76.9% (see below) | ✅ measured, holds for both runs |
| 20 | B04 | On screen: the bars | `scene.json` curve, final run, rounded: clean 2%, +20 dB 2%, +10 dB 3%, +5 dB 11%, 0 dB 73% (1.7, 2.1, 2.9, 10.9, 73.1) | ✅ measured |
| 21 | B04 | Listen to that sentence, and what it wrote | `evidence/sentence_1_0db.wav`, written inside the run from exactly the audio it transcribed, appended by `mix_listen.py` (level matched only, −4.1 dB); screen: said "The train to Boston leaves from platform nine at noon", wrote "let's try to block a bridge from that old knife right now" (`results.json`, 0 dB, sentence 1) | ✅ measured |
| 22 | B05 | Louder noise didn't make it stop: over three hundred words written for 238 | run, −5 dB: 309 words written for 238 (sum over `results.json` detail), WER 126.5% (214 sub, 8 del, 79 ins); the earlier run gave 306 (see below); screen "238" / "309" | ✅ measured, holds for both runs |
| 23 | B05 | Phrases repeated over and over | `results.json`, −5 dB: "the train to washington washington washington washington washington" (on screen), "so find that giant one two one two one two …"; repeat loops are a documented failure (facts-asr §6.1) | ✅ measured |
| 24 | B05 | Even on clean speech it writes what it expects: my narrator says "Row-Haan", and it writes "Rohan" | voice reel run: `name_fixed 'Hi, I am Row-Haan.' -> heard 'Hi, I am Rohan.'`; the model card's own explanation, predicting the next word as well as transcribing (facts-asr §6.2) | ✅ measured |
| 25 | B05 | It hears "dollar, three, fifty", and writes a neat price with a dollar sign | voice reel run: the narrator's phonemes `dˈɑːlɚ θɹˈiː. fˈɪfti`; `price 'It costs $3.50.' -> heard 'It costs $3.50.'` | ✅ measured |
| 26 | B06 | Read auto-captions before you publish, especially names and numbers | follows from B05; YouTube encourages creators to review automatic captions (facts-asr §7.3) | ✅ as advice |
| 27 | B06 | YouTube itself says automatic captions can get words wrong | YouTube Help, "Use automatic captioning": they may misrepresent speech (facts-asr §7.2) | ✅ |
| 28 | B06 | Record somewhere quiet: a few decibels make a big difference | run: +5 dB 10.9% → 0 dB 73.1% | ✅ measured |
| 29 | B07 | "Picture the sound, predict the words, line them up, and then check them" | summary of B01–B06 | ✅ |

## The noisy runs differ, and how the narration handles it

`captions.py` was run twice with the same code. Clean, +20, +10 and +5 dB came out **identical** both times. The
two noisiest did not: 0 dB WER **76.9%** then **73.1%**; −5 dB **306** then **309** words written for 238 (WER
**124.8%** then **126.5%**). The audio is the same each time (the noise is seeded, `default_rng(11)`); the
transcripts are not, because faster-whisper falls back to temperature sampling on hard audio (1.2.1 defaults:
temperatures 0.0 to 1.0, tried when the compression ratio passes 2.4 or the average log-probability falls below
−1.0), and that sampling is not seeded. The first script used the first run's values; the narration was reworded
to "over seventy percent" and "over three hundred words" so it holds for either run, and the screen shows the
final run's values (73%, 309), the ones in `run.log`.

## Arithmetic, checked separately

- **Word error rate.** WER = (substitutions + deletions + insertions) / words actually said (facts-asr §4.1),
  after lower-casing, removing punctuation and spelling out numbers 0–99 on both sides. Final run, from
  `results.json`: clean (4 + 0 + 0) / 238 = 1.7%; 0 dB (149 + 8 + 17) / 238 = 73.1%; −5 dB (214 + 8 + 79) / 238
  = 126.5%. Above 100% is possible because insertions aren't capped (facts-asr §4.2).
- **Signal-to-noise ratio.** The pink noise is scaled so the speech's power (over its non-silent samples) is
  10^(SNR/10) times the noise's: +10 dB is ten times the power, 0 dB equal.

## Not claimed

- That YouTube's auto-captions use Whisper or any named model; any accuracy figure for YouTube's captions. The
  97% in B04 is Whisper base on my sentences at +10 dB, not "97% accurate" in general (facts-asr §4, "do not say").
- That Whisper's word starts run about 0.24 s early in general: it is in my test, on speech built word by word,
  and the cause is not established.
- That 680,000 hours is large-v3's training data; Careless Whisper's hallucination rates; that silence causes
  hallucination; that faster-whisper's code is identical to openai/whisper's.
- That the narrator's mistakes come from misaki (its pronunciation step is espeak-ng through `phonemizer`, in
  kokoro-onnx 0.6.1); that YouTube requires AI narration to be labelled.
