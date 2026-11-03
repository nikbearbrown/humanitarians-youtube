# CHECKS-REPORT — Suno, Part Two.

PROOF GATE exit condition for the beat sheet. Written before any render.
Classification per `skills/make/nopunt/SKILL.md` (SHOW / HOLD / CARD).

## Per-beat classification

| Beat | Act | Class | Artifact the beat SHOWS |
|---|---|---|---|
| B00 | cold open | SHOW | composer; ask types, three result lines reveal the video's three dimensions |
| B01 | BLUF | SHOW | the worked sentence; a fan of faint possibilities opens on "vague", collapses to one track on "specific", then three underlines resolve under style/mood/topic |
| B02 | vague vs specific | SHOW | split stage — pale possibility-cloud of many waveforms vs one resolved waveform |
| B03 | style | SHOW | three-rung ladder, GENRE → INSTRUMENTS → PRODUCTION, waveform visibly tightening at each rung |
| B04 | mood | SHOW | feeling × energy axes; the example plots at their crossing; caution card lands off-target |
| B05 | topic | SHOW | one subject at three distances; lyric fragments thicken as the framing closes in |
| B06 | iterate | SHOW | one description branching into three single-variable edits, then the three-at-once counter-example |
| B07 | Advanced | SHOW | Suno window; tab slides Simple → Advanced; panel splits into Styles + Lyrics; structure tags type onto their own lines |
| BVDT | verdict | CARD | artifact page — seven lines revealing in turn (bookend; CARD is legal here) |
| BHTF | recap + Part 3 tease | SHOW | composer returns; Part 3 question types; three preview lines reveal |
| BOUT | outro | CARD | title restate, handle, name in small print (bookend; OUTRO LAW) |

**Totals: 9 SHOW / 0 justified-HOLD / 0 PUNT-flagged.** The two CARDs are the
verdict and outro bookends, which the law exempts.

## Teaching-arc checklist

| Item | Status | Where |
|---|---|---|
| FRAMEWORK beat before examples | ✓ | B01 states the principle (precision narrows the output) before any vocabulary is taught |
| WORKED EXAMPLE | ✓ | The Part 1 sentence — *"a gentle acoustic folk song, warm and hopeful, about children discovering the joy of reading"* — is pulled apart across B03–B05 and reassembled in B07's Styles box |
| FALSIFIABILITY | ✓ | B06. Change three dimensions at once and the result cannot tell you which one worked. This is what makes the rest testable rather than advice |
| SCAFFOLDED TASK | ✓ | B06 hands over a habit the viewer can run immediately: change one dimension, regenerate, compare |
| BOUNDS | ✓ | B03 states the two failure modes (negatives; artist names on the BVDT card) rather than only the happy path |
| BOOKENDS | ✓ | cold open → BLUF → body → verdict → recap/tease → title outro |
| NO-SOURCE-NO-VERDICT | ✓ | Every claim logged in `FACTCHECK.md`, with a "deliberately NOT claimed" section for the research that was excluded |

## Word budget and pacing

All body beats sit inside the 45–70 word budget. Estimated total **3:10**;
actual comes from Kokoro at audio lock.

## Register check

- Internal volunteer training. Pro access was covered once in Part 1 B03 and is
  **not** re-sold here.
- Host's full name spoken exactly once, in BOUT, phonetically spelled.
- Evidence lives on screen: the facts that do not fit the narration budget
  (artist names blocked; Advanced splits in two) ride the BVDT artifact card.

## Heteronym pass (new discipline, after Part 1)

Part 1 shipped "where the actions **live**", which Kokoro read as /laɪv/. The
build cannot hear itself, so narration is now scanned before audio lock.

| Beat | Word | Action |
|---|---|---|
| B03 | `close` in "close miked" | **Rewritten** to "intimate" — no grammatical cue for /kloʊs/ in a list of adjectives, and it was jargon for this audience |
| B03 | `read` in "negatives read poorly" | **Rewritten** to "work" — present-tense `read` is a coin flip |
| B02 · B05 · BVDT | `subject` (noun) | Kept — preceded by an article/adjective, so the noun sense is unambiguous |
| B05 · BVDT | `close` in "how close you stand" | Kept — adverbial after "how" |

**Ear-check list for this reel** (cannot be verified by the build; a human must
listen): `lo-fi` in B03, and `Rohaan` in BOUT.

## Deviations from default doctrine (deliberate)

1. **HANDOFF LAW — "Your Turn" replaced by recap + Part 3 tease.** Author's
   standing choice for this series; the composer beat and typing convention are
   preserved.
2. **Kicker.** Reel runs on the `claude-hai-lyrical` channel (kicker "Lyrical
   Literacy") rather than `claude-hai` ("Irreducibly Human"), which is not this
   series. GATE L passes.
3. **BOUT canvas fill.** `ClaudeTitleOutro` is a shared house component; its
   sparse poster card is the intended OUTRO LAW look and trips Gate V's 55%
   bounding-box test under `--lenient`. Accepted, as in Part 1.
