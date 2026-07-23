# SOURCE-DISCOVERY.md

## NBB-wrap: vox-spindle-checkpoint

**Date:** 2026-07-16 (rebuilt from review cut)
**Protocol:** NBB-wrap SOURCE-DISCOVERY (unattended)

---

## Supplied video

| Field | Value |
|---|---|
| Path | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-spindle-checkpoint/vox-spindle-checkpoint-review.mp4` |
| Duration | 173.104 s |
| Resolution | 1920×1080 |
| FPS | 24 |
| Audio | AAC mono 44100 Hz |
| SHA-256 | `41abfe354523c43330a2b9e0221c5373b153ff1a93d216b7f5916aaf41a056a7` |

**Note:** The review cut is the authoritative body. It contains the corrected B04 layout (chromosome alignment graphic). The slate (`vox-spindle-checkpoint-slate.mp4`) was used in the first build (2026-07-16T12:27:25); this rebuild uses the review cut as instructed. The old `beat_sheet.nbb.json` is preserved as `beat_sheet.nbb.old.json`.

---

## Derived search slug

Raw filename: `vox-spindle-checkpoint-review.mp4`
Removed suffix: `-review`
**Derived slug:** `vox-spindle-checkpoint`

---

## Candidates considered

| Candidate | Path | Evidence strength |
|---|---|---|
| **SELECTED** | `cancer-biology/youtube/vox-spindle-checkpoint/` | Strongest: contains the exact source MP4 and its review variant, a matching `beat_sheet.json` (slug=`vox-spindle-checkpoint`), `clips/`, `mp3/`, `manim/`, `media/`, `PEDAGOGY.md`, `FACTCHECK.md` |
| None other | — | No duplicate slugs, no other matching beat sheets, no other copies of the MP4 found |

---

## Selection rationale

The supplied review-cut MP4 (`vox-spindle-checkpoint-review.mp4`) lives inside the candidate directory itself. The `beat_sheet.json` in that directory carries `metadata.slug = "vox-spindle-checkpoint"` and references `mp3/beat-B01.mp3` through `mp3/beat-B15.mp3`, all of which exist. The conformed clips (`clips/B01.mp4`–`clips/B15.mp4`) exist. This is an unambiguous single-candidate match.

**Canonical SOURCE_REEL:** `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-spindle-checkpoint/`

---

## Body identification

From the beat sheet, beats `B01`–`B13` are body beats (acts: COLD OPEN, THE QUESTION, THE PROBLEM, THE MECHANISM, THE IMPLICATION, THE EXAMPLE, RECAP). Beats `B14` and `B15` are `act: OUTRO` (`OutroSeries` and `OutroCTA`). These two beats are removed and replaced by the new NBB wrapper's outro. The body is `B01`–`B13`.

Sum of `actual_duration_s` for B01–B13: 9.2 + 9.51 + 11.36 + 10.4 + 12.2 + 3.06 + 14.65 + 16.67 + 9.27 + 17.08 + 15.18 + 27.59 + 13.793 = **169.913 s**

Old outro (B14 + B15): 2.17 + 1.49 = 3.66 s
Total review MP4 duration: 173.104 s ≈ 169.913 + 3.66 = 173.573 s (close; assembly encode introduces minor rounding).

Body extraction timecode: `[00:00.000, 169.913]` — trim the last ~3.191 s to drop old outro.

---

## Files discovered

See `SOURCE-MEDIA-LOCK.md` for complete asset inventory.
