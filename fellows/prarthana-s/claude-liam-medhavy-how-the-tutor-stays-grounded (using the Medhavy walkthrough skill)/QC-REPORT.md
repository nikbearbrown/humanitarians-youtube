# QC-REPORT.md — How the Tutor Stays Grounded in Your Textbook

This report records the QC on the final exports, run on 2026-09-29.

**Lifecycle, as of the source cleanup on 2026-09-29:**
- Both final videos were uploaded to Google Drive by Prarthana.
- The final source and docs are being prepared for manual upload to GitHub by Prarthana. The videos themselves are not in GitHub.
- Nothing has been published to YouTube. The YouTube 4K processing check applies only if and when the videos are published.

## Landscape

**File:** `exports/landscape/claude-liam-medhavy-how-the-tutor-stays-grounded.mp4`

| | |
|---|---|
| Format | 3840×2160 · H.264 + AAC 48 kHz stereo |
| Duration | 167.933 s (video and audio equal) |
| Size | 40,663,919 bytes |
| SHA-256 | `17d8c91bf26a286626c5f948032052f240a21b8287646954259947c089b80d07` (matches `.verified.json`, status `ready`) |
| Export path | `./art final` (with GATE T) |

**Checks, all passed:**
- **GATE T type check:** PASS.
- **Gate V frame check:** 0 BLOCKER, 0 MAJOR.
- **Overlay:** no timecode overlay, checked at full-resolution corners.
- **Redaction:** the hub header reads "Admin account"; no personal data is visible.
- **Edits:** no white or blank loading frames at edit boundaries.
- **Timing:** B06 lands on the moment the sources appear before the answer, and B08 ends before the 5.4 navigation.
- **Screen:** the footer warning is legible; the intro and outro are correct.
- **Audio:** no gaps or overlaps. The seven silences longer than 0.9 s are all intended narration-to-cut padding.

**Notes:**
- B00, B13 and B14 open with a 0.2–0.4 s cream fade-in. That is the library animation, not a loading frame.
- GroundingFlow (B10) is drawn in ink, not terracotta, so it passes the §8.3 contrast check.

## Vertical

**File:** `exports/vertical/claude-liam-medhavy-how-the-tutor-stays-grounded-vertical.mp4`

| | |
|---|---|
| Format | 2160×3840 · H.264 + AAC 48 kHz stereo |
| Duration | 167.933 s (video and audio equal) |
| Size | 30,465,812 bytes |
| SHA-256 | `4aab3976df371530028533c8ad7a0d10a472cba99babec09c883f3c3963fe60f` (matches `.verified.json`, status `ready`) |
| Export path | direct `runtime/scripts/compile.py --height 3840` (approved by Prarthana 2026-09-29), **not** `./art final`, because `art final`'s GATE T pre-check has no bypass |

### The automated vertical type gate (GATE T) did NOT pass

It fails on exactly one beat: **B15**.

- **B15 · ClaudeTitleOutro916:** §8.1 min-size. The smallest text run is 49 px, against a 72 px floor (1.9% of 3840).
  - The failing run is the lowercase glyphs of the "@NikBearBrown" handle.
  - ClaudeTitleOutro916 is a locked toolkit component (OUTRO-LOCK.md). Fixing this would mean modifying the locked component, which is not permitted.
  - **Manual check:** at phone width (390 pt) the handle reads clearly by eye, at about 12 pt, and the title restate is correct.

Every other GATE T beat passes, including B01 and B10 after their fixes.

### Other vertical checks, all passed

- **Gate V frame check** (run inside the compile, on the candidate): 0 BLOCKER, 0 MAJOR.
- **Overlay:** no timecode overlay, checked at full-resolution corners.
- **Clipped text:** none in B01, B10 or any corrected portrait footage beat, checked by eye on key frames. B10 also passes GATE T's own §8.1 and §8.2 checks.
- **Personal data:** none visible. The hub header reads "Admin account".
- **Edits:** no white or blank loading frames at edit boundaries.
- **Audio and sync:** audio and video run the same length. The seven silences are intended padding. B11 uses its vertical-only narration.
- **B11:** shows the follow-up question, "AI is thinking…", the new cards and "Dive deeper (10)". Only the first words of the reply ("Yes — her") peek in at the bottom. The narration does not claim the answer body is visible.

### Documented waivers (underfill only; separate from the B15 exception)

Declared as `qc.sparse_by_design` with written reasons in `vertical/beat_sheet.json`. These waive only the underfill check; edge-bleed, contrast, min-size and empty-frame still run.

| Beat | Measured fill (min 55%) | Reason |
|---|---|---|
| B01 · BrutalistHesitantWriter916 | 19% | The hesitant-writer bookend is the case this toolkit declaration exists for. It is sparse because the small "What I Checked" card was removed from the vertical only, as approved. |
| B13 · ClaudeVerdictArtifact916 | 51% | The library verdict card at its fixed portrait layout. All five lines are legible. |

### Vertical-only changes (approved 2026-09-29)

- **B01:** the "What I Checked" card and brand label are removed, and the main line enlarged to 165 px.
- **B10 · GroundingFlow916:**
  - All portrait text is at least Inter 68 / EB Garamond 90, to meet the §8.1 floor.
  - The step numbers are removed; the connectors carry the order.
  - The context pills wrap to two rows.
  - The side note "The open page doesn't decide this search" is omitted, because it could not share the title-safe box at the floor size. B05's narration carries the same point.
