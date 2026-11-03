# BUILD-LOG — "How AI Music Generators Turn Text Into Audio"

What broke, what it cost, and what changed because of it. Built 2026-10-10 for the week of 5–9 Oct.
The toolkit update (40 upstream commits merged, a UTF-8 fix to the new pronunciation module) is
logged in the Shazam reel's BUILD-LOG §1; both reels build on the same merge.

## 1 — Facts first, because Suno hasn't published anything

A fact-check before writing (`week-07/_research/facts.md`) found no Suno paper or technical
report, so the script names Suno only to say that, and the explanation rests on published systems
(SoundStream, EnCodec, MusicGen, MusicLM). It also found that not every music generator predicts
tokens (Stable Audio is diffusion; MAGNeT is non-autoregressive), so the narration says "many".

## 2 — The codec didn't generalise, then dropped the treble

`codec.py` is residual vector quantization on MDCT frames, with k-means codebooks of 1,024.
- **Too little music.** Trained on 12 short pieces, it reached 21 dB on its own training music but
  only 11.7 dB on an unseen piece. Tripled to 36 pieces.
- **The treble vanished.** Plain k-means minimises total error, and above 4 kHz there is very little
  energy, so it never spent an entry there. A spectral weighting (each coefficient scaled by its
  typical level) was tried and was worse on the unseen piece (lower SNR, worse below 2 kHz), so it
  was dropped (`CODEC_WEIGHTED=1` repeats that test).
- **The metric lied.** The first band metric said the treble was 34–38 dB off at every rate. In 59%
  of frames the treble is over 40 dB below the bass: the metric was mostly measuring silence. It now
  reports how much treble energy the decode keeps (−16.7 dB at 1 codebook → −5.6 dB at 12) and the
  spectral distance only on bands within 30 dB of each frame's loudest.

## 3 — Checked by measurement, since the clips can't be heard here

The decodes get brighter as codebooks are added: spectral centroid 188 → 276 → 328 Hz against
338 Hz for the original. The two generations differ the way their prompts say: 1.0 note onsets per
second for "calm piano", 4.7 for "busy drums".

## 4 — The first generator just replayed its training music

Generating whole 4-token frames with a trigram gave 6 seconds that were one training passage copied
verbatim (0 seams). That is an honest finding about tiny models, but not "generation". The generator
now works coarse-then-fine (the shape MusicLM uses): the trigram predicts the coarse token one step
at a time, and each coarse token gets the finer tokens most often seen with it. Result: 101 and 133
seams, longest copied stretch 0.26 s and 0.13 s. B06 reports that number.

## 5 — Gate findings from probe stills (before any render)

- **Gate V contrast (B02).** 1,024 pale grid cells were mid-tone "ink" that pulled the frame's
  ink/background separation under 0.30: cells darker and smaller, the frame's filled shape stronger.
- **Gate V underfill (B05, B06 at 50%).** Their charts appeared only on late cues: now shown faintly
  from the start and filled on cue.
- **GATE T, phone.** "frames/s" inside the long typeset rows shrank under the 4K floor: the phone cut
  uses phone-length rows (the same arithmetic, units moved into the captions above them). The pill
  "your prompt" and the thin arrows were under the floor: bigger pills ("the prompt"), drawn arrows.
- **Overflow, phone.** Long labels in B03, B04 and B05 ran off the right edge: phone strings shortened.

## 6 — The example row was unlucky

B05's first example stretch (from 2.0 s) had 0 right in 8 guesses: real, but not typical of a model
that is right 16.5% of the time. `codec.py` now picks the 12-token window whose hit rate is closest
to the overall accuracy (from 4.0 s: 2 of 10), and FACTCHECK says the window was selected that way.

## 7 — Finals the gates passed, and one they didn't

- **App quit mid-render.** The first full render died with "browser crashed" errors when the desktop
  app was quit (it killed the renderer); relaunched, it completed with no errors.
- **GATE T §8.6b blocked the first 9:16 final (B06).** First, the toy label landed on the MusicGen
  card and the PLAYING label pushed a token row into a column; then the "the prompt" pill's border
  touched the TEXT ENCODER chip, which the checker read as one shape around text. The phone branch
  now places every block at a fixed height with real gaps, and the probe tool runs the §8.6b check too.
- **Seen on the contact sheets, not by the gates.** 16:9 B05: the "big models" caption sat on the last
  bar's value; B04: the 1-codebook value labels sat on the y-axis ticks and the line. 9:16 B05: the row
  labels were cut off under the token boxes and the caption sat on the last bar. All fixed, re-rendered,
  and both finals rebuilt; the phone spark lines became "Words steer the guesses." and "Learn what
  follows." (a word with no tall letters, like "comes", falls under the 4K phone floor).
- **Phone maths.** The four-term sum and a short "≈" can't reach the 9:16 floor at any width that fits,
  so the phone shows F ≈ A + B + C and the exact 1,411.2 ÷ 3.75 = 376.32.

## 8 — The end of a beat, checked too late

After Rohan found an end-of-beat collision in the Shazam 9:16, every beat of both videos was checked at
97% of its length. Here, B02: in 16:9 the range note overlapped the codebook grid and the token row its
bottom (the note moved into the token label, the grid made smaller, the token row and example entries
shown faintly from the start so the mid-beat frame isn't underfilled); in 9:16 the token row sat on the
grid's caption (caption dropped on the phone, the narration says it) and the spark line wrapped (now
"Find the closest shape."). Re-rendered in 4K and both finals rebuilt.

## Render

Masters (`./art final`, receipts `*.verified.json` beside each file; SHA-256 re-checked on copy):

| Cut | File | Size | Length | SHA-256 |
|---|---|---|---|---|
| 16:9 | `landscape/AIMusicTokens_RohanV.mp4` | 3840×2160 | 209.29 s | `54ea386750c33e296393c2e29a19bc342217a5bedb1435f601e0952a3e06414d` |
| 9:16 | `vertical/AIMusicTokens_RohanV.mp4` | 2160×3840 | 209.29 s | `79a982f61e5d300feb42e8a5223cb879e6776233f27bf78023d4c15bbff35a67` |

Gates on the accepted finals: GATE F pass; GATE T pass ([TYPECHECK.md](./TYPECHECK.md),
[vertical/TYPECHECK.md](./vertical/TYPECHECK.md)); Gate V clean, 0 BLOCKER / 0 MAJOR
(18 landscape and 18 portrait frames sampled). Looked at by eye: [qc-sheet-16x9.png](./qc-sheet-16x9.png),
[qc-sheet-9x16.png](./qc-sheet-9x16.png).

Landscape: the first final passed, then was rebuilt after the contact-sheet fixes in §7. Portrait: refused three times by GATE T §8.6b on B06 (the third was a run that still had the old B06), accepted, then rebuilt once more after the B05 fixes (§7), all on 2026-10-10. Both cuts were rebuilt again on 2026-10-11 after the end-of-beat fixes (§8); those are the finals in the table.

Uploaded to Google Drive `2026-10-09/landscape/` and `2026-10-09/vertical/`; md5 of each Drive copy
matches the local master (re-uploaded and re-checked 2026-10-11).
