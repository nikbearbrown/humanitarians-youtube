# BUILD-LOG — "How Auto-Captions Find Each Word"

What broke, what it cost, and what changed because of it. Built 2026-11-01 for the week of 26–30 Oct. The
toolkit update (23 upstream commits; only two generated indexes conflicted) is logged in the voice reel's
BUILD-LOG §1.

## 1 — A test with known answers

To measure timing, the true start of every word has to be known. `captions.py` builds 24 sentences word by word
from our narrator's voice: each word synthesised alone, trimmed, and joined with short gaps, so every start is
known to the sample. That speech is a little choppier than a real read, and the script and FACTCHECK say it was
built this way. The recogniser is faster-whisper base, the model `align.py` already uses and already on this
machine, so nothing was downloaded.

## 2 — The first start error was +848 ms

The first run put Whisper's word starts 848 ms late on clean speech. faster-whisper reads a NumPy array as
16 kHz audio, and ours was 24 kHz, so every time came out stretched by half again. The run now resamples to
16 kHz before transcribing (`to16k`). After: a median of 241 ms *early*, the figure B03 reports.

## 3 — "9" is not "nine"

Whisper writes numbers as digits ("platform 9" in sentence 1) and the reference has words, so a correctly heard
number counted as an error and inflated the word error rate. Both sides now have numbers 0–99 spelled out before
scoring (`norm`).

## 4 — The misheard list

The run log's "Misheard (0 dB, first 3)" line had a slicing bug and didn't list the first three misheard
sentences. Fixed: the slice is now taken on the list of sentences.

## 5 — The noisy runs vary

A second run, with the same code, changed the two noisiest results: 0 dB WER 76.9% → 73.1%; −5 dB 306 → 309
words written for 238 (WER 124.8% → 126.5%). Clean, +20, +10 and +5 dB were identical. The audio is identical too
(seeded noise); on hard audio faster-whisper falls back to temperature sampling, which isn't seeded. The first
script said "seventy-seven percent" and "three hundred and six"; the narration was reworded to "over seventy
percent" and "over three hundred words", true for either run, and the screen shows the final run's values.

## 6 — Sanity checks on the run

- **"Nine in ten within three tenths of a second"**: the 90th percentile is 302 ms, rounded to 0.3 s on screen.
- **B04's percentages are 100 − WER** (97.1%, 89.1%); the counts of matched words (232, 214) agree.
- **The 0 dB clip is the transcribed audio**: `sentence_1_0db.wav` is written inside the run from exactly what was
  sent to the recogniser, and `mix_listen.py` only levels it (−4.1 dB).
- **B05's clean examples come from the voice reel's run**, not this one; `CapCatch`'s header, the beat sheet's note and FACTCHECK say so.

## Gates and layout fixes (4K probes before the render)

- **Gate V underfill at mid-beat (landscape)**: content sat in the top two thirds until the spark line arrived.
  Every landscape layout now has the same ghost baseline above the spark line from the first frame (the toolkit
  gained `LandBaseline` beside `PhoneBaseline`), and listening chips show as ghosts until they play.
- **GATE T §8.1 (39 px landscape, 72 px phone, at 4K)**: serif rows at 34–40 units measured 35–36 px
  (landscape) and 65–71 px (phone). Body text raised to 44–50 units landscape and about 1.0× the phone body size.
- **Looked at, not just gated**: the 4K contact sheets showed overlaps the gates passed: phone titles that
  wrapped onto the content, stats on top of a grid, labels running together. Phone titles were shortened
  (vertical_strings.py) and the layouts re-spaced, then probed again.
- **Phone B01**: the 80-band spectrogram's formant stripes read as sub-floor text. Every flagged run lies inside
  the image and the scene's own labels pass, so `CapSpectro916` joined the diegetic list in `type_check.py`
  (§8.2 and §8.3 still run on it).
- **Phone B02**: Whisper's word labels ran together ("TRAINTO"); they now alternate between two rows, and the
  last one is right-aligned so it stays inside the frame.
- **Phone B04 and B05**: shorter axis label and listening chip, smaller chart, and a five-word sample of the
  repeat loop, so the sentence, what Whisper wrote and the clean-speech pairs fit above the spark line.

## Render

Masters (`./art final`, receipts `*.verified.json` beside each file; SHA-256 re-checked on copy):

| Cut | File | Size | Length | SHA-256 |
|---|---|---|---|---|
| 16:9 | `landscape/AutoCaptions_RohanV.mp4` | 3840×2160 | 136.92 s | `df9167c57e64e050403d5f48784cc086b5364f355d9e728adce9eed2d2845df6` |
| 9:16 | `vertical/AutoCaptions_RohanV.mp4` | 2160×3840 | 136.92 s | `72089a97d106156c1e37c4cdb47a3b10295d382ba95fe9ce0c2259b63f3c5754` |

Gates on the accepted finals: GATE F pass; GATE T pass, 0 FAILs ([TYPECHECK.md](./TYPECHECK.md),
[vertical/TYPECHECK.md](./vertical/TYPECHECK.md)); Gate V clean, 0 BLOCKER / 0 MAJOR
(16 landscape and 16 portrait frames sampled). Looked at by eye: [qc-sheet-16x9.png](./qc-sheet-16x9.png),
[qc-sheet-9x16.png](./qc-sheet-9x16.png) (one frame per beat at 85%, from the finals).

Both cuts accepted on the first final, 2026-11-01 (finished 00:05 on 2026-11-02).

Uploaded to Google Drive `2026-10-30/landscape/` and `2026-10-30/vertical/`; md5 of each Drive copy
matches the local master.
