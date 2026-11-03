# SHORT — *Which of Gardner's Eight Intelligences Can a Machine Do?* (9:16, 2160×3840)

## v2 design: ONE HOUSE, ONE CAMERA (2026-09-27)

v1 (reused room beats B06/B08/B10/B15 between a new intro and outro) was rejected by Tanmay:
*"the shorts should be a trailer but the video should feel complete like not 2-3 beats stiched
together with no sync in between them."* v2 is a short-only script (`build_short_sheet.py`) with
its own arc and its own ending. It still works as a trailer: it points to the full film for
everything it doesn't open.

**Arc:** the essay's sentence (hook) → the house → six lights in one continuous take → the two
personal rooms (walk into the dark one) → the answer, and the correction to the hook → the full film.
The Short answers its own question; the long is where every door is opened.

**Sync across cuts:** after the hook, every beat is the same floor plan, and each opens in exactly
the state the previous one ended in:

| Cut | End state of the outgoing beat = start state of the incoming beat |
|---|---|
| S01 → S02 | composer → plan (the one scene change, from the essay into the house) |
| S02 → S03 | all dark, no accent, caption "A light comes on only when…" |
| S03 → S04 | six lit, accent on Naturalist, Naturalist caption |
| S04 → S05 | six lit, room 7 ajar, accent on room 8, "category error" caption |
| S05 → S06 | plan → title card (the ending) |

| Beat | Role | Visual motion |
|---|---|---|
| S01 | hook: name, the essay's sentence, "He did ask" | composer types the question, the quote appears |
| S02 | the house and the rule | the accent **walks the rooms as each is named**, then the rule caption |
| S03 | six lights | lights switch on **on the spoken cue**, the accent follows, the caption changes to each room's quote |
| S04 | the personal rooms | room 7's door opens ajar, then the camera **walks into room 8** (interior), then pulls back |
| S05 | the answer + the correction | the count caption, then the accent **moves to Logic** at "1956" |
| S06 | the full film | title card, handle, sign-off |

No silent END card: S06's title card carries the handle, so the Short ends on its own ending,
not on a duplicate card.

## Toolkit (additive; the long's renders are unchanged)

`EightRooms.tsx` gains optional props, all off by default:
- per-room `atSeconds` (each room lights up on its own cue)
- `accentAtSeconds` (move the accent without re-lighting)
- `focusFollow` / `followUntilSeconds` (the accent follows the latest cue)
- `captionSteps` (timed captions)

`tsc` is clean.

## Script — Gate P

See `beat_sheet.json` (generated). Mechanical pass: 1 flag, NAME `Gardner` (accepted in the long).
One BREATH flag in S02 was fixed by splitting the sentence.

### Fact trace (no new claims)

| Line | FACTCHECK |
|---|---|
| S01 essay's 1983 sentence; "He did ask. And he answered…" | 0.3, 0.5 (as the long's B01) |
| S02 eight rooms (seven in 1983, naturalist mid-1990s), Oct 2024 paper | 1.1, 1.2, 3.2 |
| S03 "clearly exhibit the signs" of logical-mathematical and linguistic; chess/Go under spatial; "adroitly"; naturalist | 3.3, 3.11 |
| S04 "one should be more cautious" (the personal intelligences); diplomacy… list; "category error" | 3.3, 3.5 |
| S05 1956 programs in the same paper's history; "may have been on" hedge kept | 3.4, 0.3 |
| S06 the long opens every door, asks about room seven | the long's B18 |

**GATE P: PASS. Tanmay Kulkarni, 2026-09-27.** Verbatim: *"Gate P PASS"*. Read against
`READ-ALOUD.md` (the script after the pre-audio PROOF fixes, with the years written in words). No notes.

## End card

`shorts.py`'s auto card (dark, Georgia) was regenerated cream in EB Garamond. It's unused in v2
(no END beat), and kept only in `media/END.png`.

## Delivered (2026-09-27)

`gardner-eight-rooms-short-final.mp4` · 2160×3840 · 1:37 (after fixes 1–3) · -14.8 LUFS / -1.9 dBFS · GATE V clean ·
0 UI-zone FAIL (393 frames) · 0 dark frames · 16/16 claims on screen when spoken ·
**clear-for-public** (PROOF-REVIEW-SHORT.md, "PROOF review — the Short's 4K master").
