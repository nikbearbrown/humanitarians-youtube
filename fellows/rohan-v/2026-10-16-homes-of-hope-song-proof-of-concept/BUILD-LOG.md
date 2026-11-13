# BUILD-LOG — "Homes of Hope Songs: Proof of Concept Progress"

What broke, what it cost, and what changed because of it. Built 2026-10-17 for the week of 12–16 Oct.
The toolkit update (9 upstream commits, Remotion 4.0.535 / React 19) is logged in the tempo reel's
BUILD-LOG §1; both reels build on the same merge.

## 1 — Ninety seconds

Rohan asked for 90 s or less. Seven beats, one idea each, came out at 83.86 s of measured narration
(83.75 s after the re-voice in §2). The handbook update two weeks ago ran 140 s with eight beats; the
cut here was a separate "what to do" beat, folded into B05 as one ask (a fluent Hindi reviewer).

## 2 — The instruments were mispronounced

A free transcription of the narration heard "dhol, tabla and sitar" as "D-Haul, Tabla and Sitter".
The G2P read "dhol" as /dˈiːhˈɑːl/ and "sitar" as /sˈɪɾɚ/. The narration now spells them "dhole,
tubla and sitaar" (/dˈoʊl/, /tˈʌblə/, /sɪtˈɑːɹ/); B03 was re-voiced, re-aligned and re-synced. On
screen they are spelled normally.

## 3 — LOGO LAW, new this week

Any company or tool named on screen must show its logo. B05's card said "Versions made in Suno", and
the roadmap scene can't hold a logo, so it now says "Song versions generated" (the narration still says
Suno in B03, which is speech, not a visual reference).

## 4 — Layouts found on probe stills (before any render)

- **16:9 B01 and B02 were underfilled** (two short cards in the top half): larger lyric lines and
  bars, more padding, and the melody line drawn as a ghost from the start.
- **9:16 B03's title wrapped onto the first row** ("The Sound Revision"): shortened to "New Sound".
- **9:16 B05's roadmap overflowed** (long labels ran off the right edge and pushed the "committed next"
  header into its cards): phone strings cut to two words each.

## 5 — The gates on 4K stills, then the contact sheet

- **GATE T §8.3, B05 (16:9)**: the library roadmap draws "NOW", "COMMITTED NEXT" and the due chips in
  #D97757 (2.74:1 on cream). The scene gained an opt-in `accentText` prop (SPARK_TEXT for text-bearing
  accents; earlier reels unchanged), set on this beat.
- **§8.1 on the phone (72 px at 4K)**: small caps labels in B01, then the italic "um" of "hum" and the
  word "meaning" in the spark line. Labels and lyric lines enlarged on the phone, the spark line now
  "English lands with its Hindi.", and other x-height-only words in the phone strings reworded
  ("careers", "answers", "or", "more").
- **Contact sheet, after the first 9:16 final**: B01's second lyric card ran past the baseline (the
  larger lines wrap), and B02's melody line touched the second card. On the phone the two lyric pairs
  now share one card slot, the second replacing the first after the group's answer; the melody line
  moved down. B01 and B02 re-rendered and the 9:16 final rebuilt.

## Render

Masters (`./art final`, receipts `*.verified.json` beside each file; SHA-256 re-checked on copy):

| Cut | File | Size | Length | SHA-256 |
|---|---|---|---|---|
| 16:9 | `landscape/HomesOfHopePoC_RohanV.mp4` | 3840×2160 | 83.88 s | `5c818794b32615b2ff6bf2ce7b6953f3df538f40af9aec748ffbb91d2b6aa449` |
| 9:16 | `vertical/HomesOfHopePoC_RohanV.mp4` | 2160×3840 | 83.88 s | `00196f15d0fa87b89a88b0fb9577eca6702e87287f04f3ab83a0ae3145578a47` |

Gates on the accepted finals: GATE F pass; GATE T pass, 0 FAILs ([TYPECHECK.md](./TYPECHECK.md),
[vertical/TYPECHECK.md](./vertical/TYPECHECK.md)); Gate V clean, 0 BLOCKER / 0 MAJOR
(14 landscape and 14 portrait frames sampled). Looked at by eye: [qc-sheet-16x9.png](./qc-sheet-16x9.png),
[qc-sheet-9x16.png](./qc-sheet-9x16.png), plus single frames of the rebuilt beats.

Landscape: accepted on the first final. Portrait: the first final passed every gate but its contact sheet showed B01's card past the baseline and B02's melody line on a card (§5); B01 and B02 re-rendered and the final rebuilt. All on 2026-10-17/18.

Uploaded to Google Drive `2026-10-16/landscape/` and `2026-10-16/vertical/`; md5 of each Drive copy
matches the local master.
