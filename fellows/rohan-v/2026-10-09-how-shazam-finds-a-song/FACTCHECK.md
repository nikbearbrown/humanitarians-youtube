# FACTCHECK — How Shazam Finds a Song

Every spoken and on-screen claim, its source, and its verdict. Checked 2026-10-10.
"The run" means `fingerprint.py` → `evidence/run.log` / `evidence/fingerprint.json` (SHA-256 in
`MEASUREMENTS.txt`). The songs in the run are **synthetic** (`synth.py`, generated from seeds);
no copyrighted recording is used, measured or played. Outside facts were verified on 2026-10-10
and are recorded with quotes and URLs in `week-07/_research/facts.md` (summarised in SOURCES.md).

| # | Beat | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | B00 | Opening line "Hi, I am … and this video is about …" | `docs/FELLOWS-SUBMISSION.md`, required wording | ✅ verbatim |
| 2 | B00 | AI narration disclosed | on-screen disclosure line + `metadata.ai_disclosure` | ✅ |
| 3 | B00 | It doesn't know the melody or the words; it looks for loud points and their timing | Wang (2003): fingerprints are spectrogram peaks and their time/frequency relations | ✅ |
| 4 | B01 | Sound becomes a spectrogram: time across, pitch up, darker = louder | the run's own STFT (1,024-point windows, 256-sample hop at 11,025 Hz), drawn as an image | ✅ shown as the run's data |
| 5 | B01 | Only points louder than everything around them are kept | `peaks()`: local maxima in a 21-bin × 15-column neighbourhood, 18 dB above the column median | ✅ |
| 6 | B01 | About twelve every second | run.log: 12.5 peaks/s over the library (on screen: 12.5) | ✅ measured, rounded in speech |
| 7 | B01 | The 2003 paper that described Shazam's method calls this a constellation map | Wang, "An Industrial-Strength Audio Search Algorithm", ISMIR 2003 ("constellation map") | ✅ (facts.md #1, #2) |
| 8 | B01 | With noise as loud as the music, 24 of these 40 points survived | run.log: 40 clean peaks in the 3 s shown; 24 still present (within 1 column, 2 bins) in the 0 dB phone clip | ✅ measured |
| 9 | B01 | 35,862 numbers in these 3 seconds | 129 columns × 278 bins (0–3 kHz) of the shown spectrogram | ✅ computed |
| 10 | B02 | Each point becomes an anchor, paired with a few points just after it | Wang (2003): anchor point and target zone, combinatorial hashing (facts.md #3); the run: up to 5 targets, 2–64 columns ahead, within 96 bins | ✅ |
| 11 | B02 | Each pair gives three numbers: two frequencies and the time between | Wang (2003); `hashes()` packs f1 (10 bits), f2 (10 bits), Δt (6 bits) | ✅ |
| 12 | B02 | Here: 786 Hz, then 1,174 Hz, 0.05 s later; packed into one code | run.log worked hash (anchor at 1.02 s); packed value on screen is the run's | ✅ measured |
| 13 | B02 | My version makes about 57 hashes every second | run.log: 57 hashes/s (13,772 hashes over 6 × 40 s) | ✅ measured |
| 14 | B03 | Plenty of songs share a few hashes by chance | the run: the clip's hashes also hit Songs A, B, D, E, F (1–18 matches each) | ✅ measured |
| 15 | B03 | Take the time in the song minus the time in the clip; a real match agrees on one moment | Wang (2003): matches of the right song lie on a diagonal; a histogram of offsets shows a peak (facts.md #4); the run's scatter and histogram | ✅ |
| 16 | B03 | Worked example 13.07 s − 1.07 s = 12.00 s | a real matching pair from the query, chosen by `export_shazam_data.py` so the rounded digits subtract exactly; typeset with `typeset_math.py` | ✅ |
| 17 | B04 | Six songs from scratch, forty seconds each; about fourteen thousand hashes | run.log: 6 × 40 s, 13,772 hashes | ✅ |
| 18 | B04 | Five seconds of Song C from 12 s, in cafe noise as loud as the music, through a phone-quality filter | `phone()`: synthetic crowd noise at 0 dB SNR, 150–4,000 Hz band-pass, level change | ✅ (noise is synthetic, not a recording) |
| 19 | B04 | Song C got 33 votes at exactly 12 seconds; the next best got two | run.log: Song C 33 votes at 12.00 s; Song E 2 | ✅ measured |
| 20 | B04 | The listening clips are the noisy clip, then the original | `evidence/clip_cafe.wav`, `evidence/original_segment.wav`, appended unedited by `mix_listen.py` (level matched only) | ✅ |
| 21 | B05 | Thirty random clips at each noise level | run.log sweep: 30 random 5 s queries per level | ✅ |
| 22 | B05 | +10 dB: all 30; 0 dB: 29; −5 dB: 22; −10 dB: 9 | run.log sweep (also +5 dB: 30, −15 dB: 0, shown on screen) | ✅ measured |
| 23 | B05 | When it failed it said no match; it never named the wrong song | run.log: 0 wrong in 180; a result below 8 votes is reported as no match | ✅ measured; the 8-vote threshold is my program's, stated on screen in B06 |
| 24 | B06 | It matches one exact recording, not the song | Wang (2003): "very sensitive to which particular version"; "not expected to generalize to live recordings" (facts.md #5) | ✅ |
| 25 | B06 | One semitone higher: one vote; 6% faster: four; hummed: one | run.log variants at +10 dB SNR (same recording: 52) | ✅ measured on re-performances rendered by `synth.py` |
| 26 | B06 | Apps that recognise humming use a different kind of fingerprint, built on the melody | Google, "The Machine Learning Behind Hum to Search" (2020) (facts.md #8). Not claimed: that Shazam itself cannot hear humming (no official statement found) | ✅ wording follows facts.md |
| 27 | B07 | Upload checks like YouTube's Content ID compare your audio with files copyright owners submit | YouTube Help, "How Content ID works": "a database of audio and visual files submitted by copyright owners" (facts.md #7) | ✅ |
| 28 | B07 | Not being matched isn't the same as being allowed | general copyright principle: permission comes from the rights holder, not from detection | ✅ as advice; no legal claim beyond it |

## Algebra, checked separately from the typography (MATH-TYPESETTING.md)

- **Rule.** Δt = t_song − t_clip, for each hash found in both the clip and a song. Free variables:
  the time of the hash's anchor in the song and in the clip; Δt in seconds.
- **Worked case.** 13.07 − 1.07 = 12.00 s, the query's true start (12.0 s). The pair is a real match
  from the run, picked so its two-decimal values subtract exactly, and asserted against the winning
  offset (12.00 s, within one 23 ms column).

## Not claimed

- Shazam's production system's parameters (zone sizes, sample rate, thresholds): mine are my own.
- Shazam's founding year: sources disagree (1999 or 2000), so the video doesn't say.
- Anything about Shazam and humming.
