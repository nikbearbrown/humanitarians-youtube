# Week 26 — PEDAGOGY (Gate P verdict log, append-only)

## Gate P, beat sheet draft 2 — 2026-10-10

**Verdict: PASS** (Tanmay), read from `READ-ALOUD.md` (28 beats, 1,186 words).
No notes returned. The pronunciation overrides in the say-it-right table were accepted as listed.

## Change after PASS — 2026-10-10 (re-opens Gate P for one line)

**Why:** The measured York Minster recording became unusable.
- OpenAIR's York Minster page is offline: the host now serves a suspended-account page.
- The replacement, the York Minster Chapter House dataset (Zenodo 4040994), is labelled CC BY 4.0
  on Zenodo. Its own `LICENCE.txt` says **CC BY-NC-SA 4.0**. Non-commercial is incompatible with a
  monetised channel, so the dataset was not used.
- The download was verified (MD5 matched Zenodo), read for its licence, then deleted, as Tanmay asked.

Tanmay chose to simulate our own echo instead (synthetic impulse response, labelled on screen).

| Beat | Was (signed) | Now |
|---|---|---|
| B01 | Listen to one sentence, spoken inside a cathedral. | Listen to one sentence, inside a simulated cathedral. |

Every other narration line is word-for-word what was signed. On-screen labels for the cathedral
beats change from "York Minster, measured impulse response" to the simulated-echo label. Those
are visual, so they're checked at stills review. **B01 needs a Gate P re-read** (one line).

## Second change after PASS — 2026-10-10 (re-opens Gate P for B02)

**Why:** the cold open's claim was tested and didn't hold. `experiment/` keeps every run:
1. Slowing Kokoro uniformly made the cathedral line *less* intelligible (Whisper 0.5 → 0.2):
   stretched words smear further.
2. A grid found that **pauses** beat normal pace in every room, while stretching didn't. That
   matches the cellist's own account (FACTCHECK A11, A15), so D02/D03 now use pauses.
3. A pre-registered final run (whisper small.en, closer to a human listener) showed the normal
   sentence is still mostly followable (0.65 vs 0.70 with pauses). "Most of that got lost" was
   not supported, and per the rule the line is rewritten, not the room tuned further.

| Beat | Was (signed) | Now |
|---|---|---|
| B02 | Most of that got lost, right? Every word is still ringing when the next one arrives. Same sentence, same cathedral. This time, slower. | Hear that? Every word is still ringing when the next one arrives. Same sentence, same cathedral. This time, slower, with room between the phrases. |

What the cold open now claims is what was measured: every word overlaps the last one's echo,
and with pauses the echo falls 11–14 dB before the next phrase (FACTCHECK B1). D02/D03 are now
phrases with 0.6 s gaps; D04 (dry) stays stretched, the researchers' held-notes reading (A12).
**Gate P re-read needed: B01 and B02.**

## Gate P re-read (B01, B02) and stills approval — 2026-10-10

**Gate P: PASS** for B01 and B02 (Tanmay). The whole narration is now signed as it stands in
`beat_sheet.json`.
**Stills: approved** (Tanmay), all 56 (28 beats × 16:9 and 9:16), as rendered in `_stills/`.

## Short Gate P — 2026-10-10

**Verdict: PASS** (Tanmay), read from `short/READ-ALOUD-SHORT.md` (11 beats, 299 words, ~1:41).
The Short is signed as it stands in `short/beat_sheet.json`.

## Short Gate P re-read (Option A) — 2026-10-10

**Verdict: PASS** (Tanmay) for the new and changed lines S03, S07, S08 and S09
(`short/READ-ALOUD-SHORT.md`). The 14-beat Short is signed as it stands in `short/beat_sheet.json`.
