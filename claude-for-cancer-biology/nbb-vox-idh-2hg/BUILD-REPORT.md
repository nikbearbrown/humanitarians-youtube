# BUILD-REPORT — nbb-vox-idh-2hg

## Source

- **SOURCE_VIDEO**: `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-idh-2hg/vox-idh-2hg-cut.mp4`
- **SOURCE_REEL**: `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-idh-2hg/`

## Discovery Summary

- **SOURCE-DISCOVERY.md**: `cancer-biology/youtube/nbb-vox-idh-2hg/SOURCE-DISCOVERY.md`
- **Candidates considered**: 2 — `vox-idh-2hg/` (selected) and `claude-liam-vox-idh-2hg/` (secondary variant)
- **Selection evidence**: SOURCE_VIDEO lives in `vox-idh-2hg/`; beat_sheet.json slug matches; all body clips present; clip sum matches video duration.

## Source Media Locations

| Asset type | Location |
|---|---|
| Source beat sheet | `vox-idh-2hg/beat_sheet.json` |
| Body clips | `vox-idh-2hg/clips/B01.mp4` through `clips/B13.mp4` |
| Body audio (ElevenLabs) | `vox-idh-2hg/mp3/beat-B01.mp3` through `mp3/beat-B13.mp3` |
| Manim renders | `vox-idh-2hg/manim/` (B01, B03–B09, B11–B13) |
| Remotion SlateCards | `vox-idh-2hg/media/B02.mp4`, `media/B10.mp4` |
| Outro clips (excluded) | `vox-idh-2hg/clips/B14.mp4`, `clips/B15.mp4` |
| Source factcheck | `vox-idh-2hg/FACTCHECK.md` (PASS) |
| Source pedagogy | `vox-idh-2hg/PEDAGOGY.md` (PASS) |

## Old-Outro Removal

- **Removed beat IDs**: B14 (OutroSeries), B15 (OutroCTA)
- **Outro start timecode**: 271.124s (from clip sum B01–B13)
- **Stream-copy body**: extracted `[0, 271.124s)` from source video using `ffmpeg -t 271.124 -c copy`

## Body

- **Body beat IDs**: B01, B02, B03, B04, B05, B06, B07, B08, B09, B10, B11, B12, B13
- **Body duration (clips)**: 271.124s
- **Body duration (extracted)**: 271.208s (stream-copy), 271.333s (after re-encode)
- **Body source clips**:

| Beat | Reused clip | Duration |
|---|---|---|
| B01 | `vox-idh-2hg/clips/B01.mp4` | 10.625s |
| B02 | `vox-idh-2hg/clips/B02.mp4` | 21.750s |
| B03 | `vox-idh-2hg/clips/B03.mp4` | 18.500s |
| B04 | `vox-idh-2hg/clips/B04.mp4` | 21.250s |
| B05 | `vox-idh-2hg/clips/B05.mp4` | 19.333s |
| B06 | `vox-idh-2hg/clips/B06.mp4` | 19.625s |
| B07 | `vox-idh-2hg/clips/B07.mp4` | 22.083s |
| B08 | `vox-idh-2hg/clips/B08.mp4` | 23.792s |
| B09 | `vox-idh-2hg/clips/B09.mp4` | 16.750s |
| B10 | `vox-idh-2hg/clips/B10.mp4` | 24.000s |
| B11 | `vox-idh-2hg/clips/B11.mp4` | 21.125s |
| B12 | `vox-idh-2hg/clips/B12.mp4` | 25.833s |
| B13 | `vox-idh-2hg/clips/B13.mp4` | 26.458s |

## Source SHA-256 Verification

- **Source SHA-256 at start**: `118d3d5d4f0179dfec4de7ccd51c1a0cc1c570df0398d4e8b89fa42a30f2306c`
- **Source SHA-256 at end**: `118d3d5d4f0179dfec4de7ccd51c1a0cc1c570df0398d4e8b89fa42a30f2306c`
- **Result**: PASS — source video unchanged

## New Wrapper Beats

### Cold Open (NBB00)
- **Question**: "Why does a metabolic enzyme mutation produce an epigenetic block to differentiation?"
- **Kore audio**: `nbb-vox-idh-2hg/mp3/beat-NBB00.mp3`
- **Duration**: 8.704s
- **Visual**: ClaudeComposerAsk — greeting "Jambo, Kore", command types the central question
- **Remotion render**: `nbb-vox-idh-2hg/media/NBB00.mp4`

### Verdict (NBB01)
- **Narration**: Synthesizes mechanism: neomorphic mutation → 2HG oncometabolite → competitive inhibition of alpha-KG-dependent demethylases → methyl mark accumulation → blast arrest. States ivosidenib restores differentiation. Names trade-off: IDH-mutant disease only.
- **Kore audio**: `nbb-vox-idh-2hg/mp3/beat-NBB01.mp3`
- **Duration**: 41.69s (new audio — previous verdict was 38.57s with incorrect repeat-body content)
- **Visual**: ClaudeWindow (artifact view) — "The mechanism" heading, 6 verdict lines, spark line "Poison by resemblance."
- **Remotion render**: `nbb-vox-idh-2hg/media/NBB01.mp4` (re-rendered from ClaudeVerdictArtifact → ClaudeWindow; 12s clip looped to fill 41.7s audio)

### Your Turn (NBB02)
- **Prompt**: Competitive inhibition in cancer metabolism — asks why 2HG is competitive vs allosteric, and predicts DNA methylation patterns over time.
- **Kore audio**: `nbb-vox-idh-2hg/mp3/beat-NBB02.mp3`
- **Duration**: 7.765s
- **Visual**: ClaudeComposerAsk — greeting "Your turn.", runningText "paste this into Claude…"

### Outro (NBB03)
- **Title**: "Why a Metabolic Enzyme Mutation Can Lock Cells Into an Immature State"
- **Handle**: @HumanitariansAI
- **Subline**: "Poison by resemblance — 2HG blocks the eraser that frees the cell."
- **Kore audio**: `nbb-vox-idh-2hg/mp3/beat-NBB03.mp3`
- **Duration**: 6.03s
- **Visual**: ClaudeTitleOutro

## Final MP4

| Property | Value |
|---|---|
| Path | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/nbb-vox-idh-2hg/vox-idh-2hg-nbb.mp4` |
| Duration | 335.55s |
| Dimensions | 1280x720 |
| Video codec | H.264 (libx264, CRF 20) |
| Audio codec | AAC 128kbps 44100Hz 1ch |
| File size | 7,745,453 bytes (7.39 MB) |
| SHA-256 | `6006d2145601447ff0212a994aba7c8860b85328bf11823960664a9c914d6026` |

## Duration Breakdown

| Segment | Duration |
|---|---|
| NBB00 Cold open | 8.7s |
| Body (B01–B13) | 271.3s |
| NBB01 Verdict | 41.7s |
| NBB02 Your turn | 7.8s |
| NBB03 Outro | 6.0s |
| **Total** | **335.5s** |

## Assembly Method

1. Stream-copied body from source: `ffmpeg -t 271.124 -c copy`
2. Re-encoded body to 1280x720/24fps/h264/aac for consistent spec
3. Encoded wrapper beats: Remotion renders (1920x1080) scaled to 1280x720, looped to audio duration
4. Concat via `ffmpeg -f concat -safe 0` → final encode (CRF 20, fast preset, faststart)

**One re-encode**: body was stream-copied then re-encoded once to match wrapper spec. Wrapper beats were rendered by Remotion at 30fps and re-encoded to 24fps/1280x720. This is the one unavoidable encode.

## PEDAGOGY Verdict
PASS — see `nbb-vox-idh-2hg/PEDAGOGY.md`

## FACTCHECK Verdict
PASS — see `nbb-vox-idh-2hg/FACTCHECK.md`

## QC Sheet
`/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/nbb-vox-idh-2hg/QC-sheet.png`

## Open Command

```
open /Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/nbb-vox-idh-2hg/vox-idh-2hg-nbb.mp4
```
