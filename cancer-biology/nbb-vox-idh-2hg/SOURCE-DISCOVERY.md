# SOURCE-DISCOVERY.md

## Input
SOURCE_VIDEO: `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-idh-2hg/vox-idh-2hg-cut.mp4`

## Slug Derivation
Filename: `vox-idh-2hg-cut.mp4`
Removed suffix: `-cut` (known output suffix)
Derived slug: `vox-idh-2hg`

## Search
Search root: `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-idh-2hg/`
Ancestors/siblings searched: Yes — parent `cancer-biology/youtube/` inspected.

## Candidates Found

| Candidate | Match Type | Evidence |
|---|---|---|
| `cancer-biology/youtube/vox-idh-2hg/` | STRONGEST | MP4 parent; `beat_sheet.json` slug="vox-idh-2hg"; all clips/mp3/media referenced by beat sheet present; vox-idh-2hg-cut.mp4 lives here |
| `cancer-biology/youtube/claude-liam-vox-idh-2hg/` | SECONDARY | Derived variant; beat_sheet.json slug="vox-idh-2hg" with audience="Claude", derived_from="beat_sheet.json"; shares same subject but is a renarrated variant, not the source |

## Selection

**Canonical SOURCE_REEL: `cancer-biology/youtube/vox-idh-2hg/`**

Evidence:
- SOURCE_VIDEO (`vox-idh-2hg-cut.mp4`) lives directly in this directory.
- `beat_sheet.json` slug matches, title matches, all body audio MPs and conformed clips present.
- Clip sum (B01–B13 = 271.124s, B14–B15 = 3.583s) matches source video duration (274.390s) within rounding.
- Outro beats are B14 (OutroSeries, 2.125s) and B15 (OutroCTA, 1.458s) — identified as the beats to remove.

The `claude-liam-vox-idh-2hg/` folder is a Kokoro/Liam audio variant, not the production reel that produced the supplied cut.

## Outro Identification

| Beat | Act | Duration | Component | Removal decision |
|---|---|---|---|---|
| B14 | OUTRO | 2.125s | OutroSeries | REMOVE |
| B15 | OUTRO | 1.458s | OutroCTA | REMOVE |

Body = B01–B13. Outro start timecode in assembled video = **271.124s**.

## Source Video SHA-256
`118d3d5d4f0179dfec4de7ccd51c1a0cc1c570df0398d4e8b89fa42a30f2306c`
File size: 4,081,987 bytes
