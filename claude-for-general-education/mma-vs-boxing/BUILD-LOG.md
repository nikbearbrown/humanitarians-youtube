# BUILD-LOG.md — mma-vs-boxing

Built 2026-08-03. Cost: **$0.00** (Kokoro local TTS, Remotion local render).

## What this reel is

A 3-and-a-half-minute explainer on the difference between MMA and boxing, for
viewers who follow neither. Host: Param Madan. Voice: Kokoro `af_bella`.

Claim: **MMA's top tier is one organization; boxing's is four** — which is why
"world champion" is one name in MMA and up to four in boxing.

## Why this is a rebuild, not a re-cut

The July 2026 version (`~/Desktop/mma-vs-boxing-VOICED.mp4`) was 1280×720 with
no surviving source project — no beat sheet, no scene code, no narration files.
Nothing to re-cut from, and upscaling flat vector art is explicitly forbidden
(`RENDER-4K-AND-UPLOAD.md`: Topaz degrades this content). Reaching 4K therefore
meant rebuilding.

The script was recovered by transcribing the old mp4 with `faster-whisper`, then
re-verified claim by claim against live sources. See `SOURCES.md` for the ledger
and the four corrections.

## The correction that changed the reel's argument

The old script's spine was *"MMA has exactly one champion per division; boxing
has up to four."* That is no longer true: the UFC heavyweight division currently
carries an interim champion (Ciryl Gane) alongside the undisputed champion (Tom
Aspinall). The clean contrast had quietly expired.

Rather than delete the wrinkle, B03 names it and the reel re-centres on a fact
that does not expire: **one organization versus four.** The interim title then
reads as *one body managing itself* — supporting evidence rather than a
contradiction. A viewer who learns "one org versus four" still answers correctly
next year, when every name has changed.

Two further corrections: "12 divisions, 12 belts" became "12 weight divisions,
one champion in each" (women's featherweight has been vacant since 2023), and
"only one boxer in the entire sport is undisputed" became "in men's boxing
today" (women's boxing has had several undisputed champions).

## What was written

**New:** `runtime/remotion/src/scenes/MmaVsBoxing.tsx` — nine scenes
(`MvbPromise`, `MvbFloorPlan`, `MvbWeapons`, `MvbOneOrg`, `MvbFourOrgs`,
`MvbSplitBelts`, `MvbUndisputed`, `MvbTest`, `MvbOutro`), all registered in
`Root.tsx` under an `MmaVsBoxing` folder at 1920×1080/30fps and rendered at
`--scale=2` for native 3840×2160. Every scene is a pure function of `useP()` and
lays content inside `SAFE`.

Bookends reuse the shipped `ClaudeComposerAsk` unmodified (B00, B08).

**Every expiring figure is a prop**, never a hardcoded string — belt holders,
the champion's name, the "as of" date. Re-verifying the reel next year means
editing `beat_sheet.json`, not the scene code.

## Deviations from house law — all deliberate

1. **IN-FOR-BEAR LAW dropped.** The host is Param Madan.
2. **OUTRO-LOCK not applied.** `MvbOutro` carries the host's name instead of the
   `@NikBearBrown` card. Matches `worldcup-2026-twenty-shots`.
3. **`folderLabel` is the host's name**, not a channel handle. None was supplied.

## Visual QC findings, and what was fixed

Per rule 5, frames were sampled and *read* rather than trusting the mp4 probe.
Two real defects, both caught and re-rendered:

1. **B02 (`MvbWeapons`) had a dead lower half** — both rows clustered under the
   spark line over an empty band, failing FILL-THE-CANVAS. Rows were resized to
   span the full band between spark and lesson strip, chips and numerals scaled
   up.
2. **B03 (`MvbOneOrg`) collided** — the "Heavyweight: Tom Aspinall" line
   overlapped the lesson strip, because the column ran ~25px past the strip's
   top edge. Tightened the stack (smaller UFC card, gaps 30→20, top offset
   108→62).

One cosmetic fix: the `Cage` tile in B00B clipped its descender against the
caption at `lineHeight: 0.9`; `Tile` now takes an `lh` prop.

## Pronunciation check

Kokoro was verified by round-tripping the generated MP3s back through
`faster-whisper`: `M M A`, `U F C`, `W B C`/`W B A`/`I B F`/`W B O` all read
back as spelled acronyms, which is what the spaced-letter spelling in
`narration_text` is there to force.

## Gate status

| Gate | Status |
|---|---|
| GATE P (`PEDAGOGY.md`) | **UNSIGNED — awaiting a human `VERDICT: PASS`** |
| DOUBLE-CHECK LAW (`SOURCES.md`) | passed — 12 claims ledgered, 4 corrected from the old script, 2 cut for staleness |
| Audio | generated, 11/11 beats, durations are ground truth |
| VISUAL QC LAW | performed — 2 defects found and re-rendered (above) |
| GATE T (type-lock) | requires `scripts/type_check.py`; not present in this cut |
| Captions | `faster-whisper` available, not run |

## Not done

- Never watched end to end by a human.
- The WBC holder rests on a secondary source; wbcboxing.com returns HTTP 403.
