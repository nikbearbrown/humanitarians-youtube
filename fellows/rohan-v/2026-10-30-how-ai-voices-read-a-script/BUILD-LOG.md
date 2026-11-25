# BUILD-LOG — "How AI Voices Read a Script"

What broke, what it cost, and what changed because of it. Built 2026-11-01 for the week of 26–30 Oct.

## 1 — Toolkit update first

`git fetch` brought 23 upstream commits (217 files: the SEIS speaker-series skill, thumbnails, setup fixes
including a live check of faster-whisper decoding and a cap on `av` below 19). Only the two generated scene
indexes (`scenes.json`, `SCENE-DOC-TODO.md`) conflicted, and were regenerated. Remotion stays at 4.0.535.

## 2 — The wrong pronunciation step, caught in research

The first research brief described our narrator as Kokoro with misaki, Kokoro's official G2P. Ours is not: the
toolkit's `phonemize()` goes through kokoro-onnx 0.6.1, whose tokenizer calls espeak-ng through `phonemizer`.
The research was redirected, facts-tts gained its §0 on our actual pipeline, and `voice.py` calls the toolkit's
own `phonemize()`, so every IPA string is what the narration really gets. The video says "e-speak" and never
names misaki.

## 3 — "Read and read" sounded the same

B03's first line was "I tested eight of them: read and read, lead and lead, live and live, and five more…".
Voiced, both readings came out identically, which is the very mistake the beat is about, so the line taught
nothing. It now says "like read, which can be reed or red", spelling out both sounds, and was re-voiced
(21.42 s → 19.99 s).

## 4 — The narration would have made B05's mistakes itself

B05's draft said "It said dhol as dee haal, and sitar as sitter". Voiced as written, the narrator would have
misread both instrument names in the sentence about misreading them. The narration uses the run's respellings,
"dhole" (dˈoʊl) and "sitaar" (sɪtˈɑːɹ), and calls the dhol "the drum" so the respelled word is still clear.
The presenter's name is "Row-Haan" in every script for the same reason.

## 5 — Sanity checks on the run

- **B02 needed real examples.** Four everyday words were added to `voice.py` (book, night, phoneme, Boston) and
  the run repeated; the regenerated clips matched the ones already mixed into B04 and B05 (the narrator is
  deterministic).
- **The recogniser can't hear the fix.** faster-whisper wrote "Rohan" for both name clips, so the video claims
  the fix from the phonemes and lets the viewer hear both clips; it never says the recogniser confirmed it.
- **"Six of seven" includes two judgment calls**: "in 2026" read as "two thousand twenty-six" and "at 10:30" as
  "ten thirty" both count as right (FACTCHECK #19).
- **Listening clips are levelled, nothing else**: −2.7 dB (price), −4.2 and −3.4 dB (name), unedited otherwise.

## Gates and layout fixes (4K probes before the render)

- **Gate V underfill at mid-beat (landscape)**: content sat in the top two thirds until the spark line arrived.
  Every landscape layout now has the same ghost baseline above the spark line from the first frame (the toolkit
  gained `LandBaseline` beside `PhoneBaseline`), and listening chips show as ghosts until they play.
- **GATE T §8.1 (39 px landscape, 72 px phone, at 4K)**: serif rows at 34–40 units measured 35–36 px
  (landscape) and 65–71 px (phone). Body text raised to 44–50 units landscape and about 1.0× the phone body size.
- **Looked at, not just gated**: the 4K contact sheets showed overlaps the gates passed: phone titles that
  wrapped onto the content, stats on top of a grid, labels running together. Phone titles were shortened
  (vertical_strings.py) and the layouts re-spaced, then probed again.
- **Phone B04 bled off the right edge**: "one thousand twenty-four bytes" did not fit beside its typed form. The
  phone stacks each row (typed, then what was read) and keeps the five cases the narration names; the
  landscape cut keeps all seven.
- **Phone B05**: the respelling rows were re-laid out (written form, then the respelling in bold) so "Row-Haan"
  and its phonemes fit.
- **Narration matched to the run**: B04 first said "one thousand and twenty-four", which the run never read;
  reworded to "one thousand twenty-four" and re-voiced before the render (audio 135.69 s).

## Render

Masters (`./art final`, receipts `*.verified.json` beside each file; SHA-256 re-checked on copy):

| Cut | File | Size | Length | SHA-256 |
|---|---|---|---|---|
| 16:9 | `landscape/AIVoices_RohanV.mp4` | 3840×2160 | 135.83 s | `be35130f6924306d3d58ca5df7cdc415eb07fdcc28af1eaac803c31b1224de02` |
| 9:16 | `vertical/AIVoices_RohanV.mp4` | 2160×3840 | 135.83 s | `938ae583f5349b4d6ac064f67562f8b44b1417e17a74737d0a4f26ece254dcca` |

Gates on the accepted finals: GATE F pass; GATE T pass, 0 FAILs ([TYPECHECK.md](./TYPECHECK.md),
[vertical/TYPECHECK.md](./vertical/TYPECHECK.md)); Gate V clean, 0 BLOCKER / 0 MAJOR
(16 landscape and 16 portrait frames sampled). Looked at by eye: [qc-sheet-16x9.png](./qc-sheet-16x9.png),
[qc-sheet-9x16.png](./qc-sheet-9x16.png) (one frame per beat at 85%, from the finals).

Both cuts accepted on the first final, 2026-11-01 (finished 00:05 on 2026-11-02).

Uploaded to Google Drive `2026-10-30/landscape/` and `2026-10-30/vertical/`; md5 of each Drive copy
matches the local master.
