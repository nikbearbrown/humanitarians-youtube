# BUILD-LOG — "How Shazam Finds a Song"

What broke, what it cost, and what changed because of it. Built 2026-10-10 for the week of 5–9 Oct.

## 1 — Toolkit update first

`git fetch` brought 40 upstream commits (1,703 files: a writing kit, the Professor Bear portrait
library and law, a Liam pronunciation dictionary, GATE T fixes, a `--stills` preflight). The merge
conflicted in `.gitignore`, `ClaudeTitleOutro.tsx`, `ClaudeVerdictArtifact.tsx`, `scenes.json` and
`SCENE-DOC-TODO.md`; each was two independent additions, kept from both sides, and the generated
files were rebuilt with `./art scene-index` (859 renderable). `tsc` shows only the two upstream errors
seen last week. The new pronunciation module read its dictionary with Windows' default encoding and
stopped every narration run; fixed to read UTF-8 (toolkit commit "fix(pronunciation)").

New rule checked: the PROFESSOR BEAR LAW (a person icon must be a portrait). No beat shows a
person, so it does not apply.

## 2 — The evidence is a program, and its first result was wrong

`fingerprint.py` follows the 2003 paper: spectrogram peaks, anchor/target-zone hashes, offset votes.
The first sweep said +10 dB noise was *worse* than 0 dB (11 vs 20 of 30 correct). Checked before
trusting it: every "miss" was the right song at an offset exactly 4 or 8 bars away. The first
`synth.py` looped bar for bar, so the start time was genuinely ambiguous. `synth.py` was rewritten
with verse/chorus sections, two melodies, drum fills and human timing; the sweep is now graded on
naming the song (with the start time reported separately), and a result under 8 votes counts as
"no match". After: 30/30 at +10 dB, 29/30 at 0 dB, falling to 0/30 at −15 dB, never a wrong song.

## 3 — The hum was too good

The first "hummed" version matched (19 votes), because it was a note-perfect copy of the song's
lead synth. A real hum is an octave lower, softer, and wanders in pitch and timing. `synth.py` now
hums with a ±30-cent, ±40 ms wobble (its own random stream, so the song is unchanged): 1 vote, no
match. The narration does **not** say Shazam can't hear humming: the fact-check found no official
statement, so B06 says what this kind of fingerprint does.

## 4 — "Usually survive" became a number

B01's script said the loudest points "usually survive" noise. Measured instead: 24 of the 40 peaks in
the shown 3 seconds are still there at 0 dB. B01 was re-voiced with the number (the rest of the
reel's audio unchanged), re-aligned and re-synced.

## 5 — The worked example had to subtract on screen

The first pair picked for B03 would have been shown as 13.03 − 1.02 = 12.00: right to three
decimals, but the shown digits don't subtract. `export_shazam_data.py` now picks a real matching pair whose
rounded values subtract exactly (13.07 − 1.07 = 12.00) and asserts it.

## 6 — Gate findings from probe stills (before any render)

- **GATE T §8.1, the spectrogram.** Its stripes read as 35 px "text" at 4K. They are data, and every
  label passes on frames where the image is faded back, so `ShazamPeaks` and `ShazamHashPairs` (+916)
  joined type_check's DIEGETIC list with a comment. The portrait scatter (`ShazamOffsetVote916`, 16 px
  dots) joined for the same reason.
- **GATE T §8.1, real labels.** "Song C" in the B04 clip card and "/ 30" in B05 were too small: enlarged.
  On the phone, single words with no tall letters ("or", "ermission") fall under the 72 px floor at
  4K, so two B07 strings were reworded ("Own the rights to it", "Check the rights first.").
- **Gate V.** B05 underfilled at mid-beat (47%): the empty squares were drawn in the border colour,
  invisible to the gate; now ghost-grey, legend from the start (73%). Portrait: Hz tick labels past
  the safe edge (gutter widened), B04's phone layout rebuilt, B06's name column fixed.
- **Contrast.** Thick #D97757 borders on the lit card read as accent text: lit borders use SPARK_TEXT.

## 7 — Spectrogram as an image

18,000 SVG cells per frame would be slow at 4K, so `export_shazam_data.py` renders the run's STFT to
`public/shazam/spec-clean.png` / `spec-noisy.png` (ink alpha = level); peaks and hashes are vectors over it.

## 8 — The first portrait master passed the gates and still had to be redone

The first 9:16 final passed GATE T and Gate V (0 blockers, 0 majors), but its contact sheet showed
three layouts the gates can't see: in B04 the vote labels sat on the song cards' borders; in B05 the
noise labels wrapped onto two lines; in B06 the MATCH / NO MATCH chips wrapped under their bars, so
the rows grew into the stamp and footnote. All three phone layouts were tightened (shorter labels,
no-wrap rows, taller cards), checked on 4K stills, re-rendered, and the portrait final rebuilt.

## 9 — The end of a beat, checked too late

Rohan spotted it in the delivered 9:16: at the end of B02 the "57 per second" stat landed on the card's
header and the card ran into the spark line. The probes sampled each beat at 50% and 85%, before the last
reveals. B02's phone card was rebuilt (every row on its own line, the rate as the last row, the panel
shorter so the card clears the baseline), and every beat of both videos in both cuts was then checked at
97%. That found two more here: the "79 chance matches" chip sat on the 16:9 scatter (moved under the
histogram), and the 9:16 x-axis caption touched the equation (equations moved down). Re-rendered in 4K
and all finals rebuilt.

## Render

Masters (`./art final`, receipts `*.verified.json` beside each file; SHA-256 re-checked on copy):

| Cut | File | Size | Length | SHA-256 |
|---|---|---|---|---|
| 16:9 | `landscape/SongFingerprinting_RohanV.mp4` | 3840×2160 | 202.58 s | `5b24240fbbae7f1be861c22bf052bc20ca44fb4029e21af6bc411277f5c1c4ee` |
| 9:16 | `vertical/SongFingerprinting_RohanV.mp4` | 2160×3840 | 202.58 s | `c21324ac1adb5afb6c0d0048cdd62c39bc5f313bbb810bd063b4cc54cb85cb06` |

Gates on the accepted finals: GATE F pass; GATE T pass ([TYPECHECK.md](./TYPECHECK.md),
[vertical/TYPECHECK.md](./vertical/TYPECHECK.md)); Gate V clean, 0 BLOCKER / 0 MAJOR
(18 landscape and 18 portrait frames sampled). Looked at by eye: [qc-sheet-16x9.png](./qc-sheet-16x9.png),
[qc-sheet-9x16.png](./qc-sheet-9x16.png).

Landscape: accepted on the first final (2026-10-10). Portrait: the first final passed every gate but its contact sheet showed three layout defects (§8); rebuilt and accepted on the second (2026-10-10). Both cuts were rebuilt again on 2026-10-11 after the end-of-beat fixes (§9); those are the finals in the table.

Uploaded to Google Drive `2026-10-09/landscape/` and `2026-10-09/vertical/`; md5 of each Drive copy
matches the local master (re-uploaded and re-checked 2026-10-11).
