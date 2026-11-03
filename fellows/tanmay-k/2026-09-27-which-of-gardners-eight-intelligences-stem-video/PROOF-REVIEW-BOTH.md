# PROOF review — Week 24, both films, final masters (2026-09-27)

Tanmay: *"now do a proof review on both videos, then we can move onto captions and descriptions for youtube."*

| | Long | Short |
|---|---|---|
| File | `gardner-eight-intelligences-machine-final.mp4` | `short/gardner-eight-rooms-short-final.mp4` |
| **Verdict** | **clear-for-public** | **clear-for-public** |
| Rubric | teaching **10/12** (the two 1s are by design: no checklist; one open question) | trailer gate **12/12** |
| Production gate | **PASS** | **PASS** |
| Gate P | signed 2026-09-26; years respelt for TTS since (spelling only) | signed 2026-09-27 |

## Production gate: measured on the masters

| Check | Long | Short |
|---|---|---|
| Format | 3840×2160 · 24 fps · **5:46** (346.0s) | 2160×3840 · 24 fps · **1:37** (96.5s) |
| Loudness | -14.9 LUFS · -1.9 dBFS · LRA 3.0 | -14.8 LUFS · -1.9 dBFS |
| Picture = paced cut (MD5) | ✓ | ✓ |
| GATE V (the gate's own samples) | 38 frames · 0 BLOCKER · 0 MAJOR | 12 frames · 0 · 0 |
| **Dense GATE V** (every 2% of every beat, `dense_sweep.py`) | 950 frames · **2 steady-state flags, both transitions** (below) · 5 entrance frames | 300 frames · **0** steady-state · 4 entrance frames |
| Claims on screen when spoken (OCR) | **35/35** | **16/16** |
| Dark frames (every frame, luma < 80) | **0** | **0** |
| Shorts UI zones (every 0.25s) | n/a | **0 FAIL** / 387 frames. Button-column LOOKs are card edges, no text |
| Sync, picture vs speech (`sync_check.py`) | 3 measurable lights: +0.27 / +0.58* / +0.38s | 7 lights: mean **+0.28s**, each switching **on its word** (≈0.3s is the light's own rise to half-bright) |
| Gaps at cuts | 19 · mean 0.86s · max 0.97s | 6 · 0.62–0.92s |
| Rendered sheet = current sheet | **✓** (diff: none) | ✓ |
| Fonts / images | OFL only · no third-party images | same |

\* B11: the cue is exactly on "Light on." (7.03s, anchored to the pause). The room is lit on the
shrinking room copy as the camera pulls out, and the probe reads the plan cell only once the move
ends.

## Found in this review

1. **REAL, fixed: a stale-sheet race left the long on the old cue rule.** `remotion_scenes.py` writes
   the whole beat sheet back when it exits. The long's sheet was rebuilt (the interpolation fix)
   while B17/B18 were still rendering, and their exit restored the old values. The next batch and the
   compile used them. Caught by diffing a rebuild under the old rule against the compiled sheet: 7
   beats, 0.03–0.30s (B08, B09, B10, B11, B13, B16, B17), all mid-phrase cues. Fixed: sheet rebuilt
   with no render running, the 7 beats re-rendered, recompiled, all gates re-run, and the compiled
   sheet now matches the rebuilt one exactly. The Short was unaffected (no render was running during
   its rebuild; values verified). Process rule saved: never rebuild a sheet while a render runs.
2. **Not a defect: the two steady-state flags in the long's dense sweep are dissolves.** B08 at
   2:18.14 is 0.16s after the camera enters room 3 (the door cross-fade). B19 at 5:40.42 is the
   title's 0.47s fade-in. Both are checked by eye (`_qc/flags.png`).
3. **Not a defect: B14's pull-back** shows the room copy at zoom with a large "Interpersonal" label for
   0.84s (12.62–13.46s). The label is in proportion to the zoomed card and settles into the plan at
   normal size.
4. **MINOR, accepted: entrance frames.** Each film opens on a cream frame for ~0.3s while the composer
   fades in, and the outro title fades up from cream (B04 and B12's cards too). By design; the gate
   never samples them. If YouTube picks frame 0 for a thumbnail, choose a custom one at upload.

## Still open

- Optional [NARRATION]: "Using that word for a program at all" (S04 / B15) has no clear antecedent.
  It needs Gate P and new audio.
- **Publishing kit (next):** titles, descriptions and `.srt` captions for both.

## Toolkit changes this week (brutalist.art, local and uncommitted)

- EightRooms / EightRoomsTour:
  - per-room cues, follow accent, timed captions
  - portrait Shorts UI zones, and the portrait walk-in fills the band
  - labels ×1.5 portrait / ×1.3 landscape
- ClaudeComposerAsk: portrait zones and larger output text
- ClaudeTitleOutroFull: portrait zones, no fade-from-black, duration hook
- Root.tsx: a duration hook on ClaudeTitleOutroFullOFL916

Reel-side tools: `cue_align.py`, `sync_check.py`, `dense_sweep.py`, `short/_qc/safezone_check.py`,
`short/_qc/cue_drift.py`.

## Addendum — Whisper timing pass (2026-09-27)

Tanmay approved downloading faster-whisper base.en (141 MB), on condition: "fix the timings only if
it's necessary". Result:

- **Words:** no mispronunciations. Whisper's differences were spellings ("a jar", "Kolkarni", "g").
  B16's last phrase, which Whisper first dropped, was confirmed present on a tail re-transcription.
- **Timing:** rendered cues vs Whisper word starts had a **median |Δ| of 0.00s** (anchored cues
  agree). Over 0.25s: long B05/B06/B07/B17 (up to 0.74s) and Short S02/S04/S05 (up to 1.37s, the
  S02 room walk ~1s ahead of the names). **Necessary → fixed**: those 7 beats moved to the Whisper
  clock, re-rendered and recompiled. Everything else (≤0.23s) was left as rendered.
- **Rejected on evidence:** the rate-constrained alignment (v2). Whisper showed it moved correct
  anchors (B13 tiles 0.8s early), so it was reverted to v1.
- **New masters:**
  - Long 5:46, GATE V 0/0, -14.9 LUFS, 35/35 (Whisper-timed), 0 dark frames
  - Short 1:37, GATE V 0/0, -14.8 LUFS, 16/16, 0 dark frames
  - video = paced (MD5) for both
- Captions regenerated on the Whisper clock.

## FINAL PROOF — the deliverables in `topic-video-final/` (2026-09-27)

Checked on the files you'll upload, not on working copies (MD5 confirmed identical).

| Check | Long | Short |
|---|---|---|
| Format | h264 3840×2160 · 24 fps · 5:46 · AAC 48 kHz | h264 2160×3840 · 24 fps · 1:37 · AAC 48 kHz |
| Loudness | **-14.9 LUFS** · -1.9 dBFS · LRA 3.0 | **-14.8 LUFS** · -1.9 dBFS · LRA 2.7 |
| GATE V | 38 frames · 0 / 0 | 12 frames · 0 / 0 |
| Dense sweep, the 7 re-rendered beats (every 2%) | B05/B06/B07/B17: 200 frames · **0** | S02/S04/S05: 150 frames · **0** |
| Claims on screen when spoken (Whisper-timed) | **35/35** | **16/16** |
| Dark frames | 0 | 0 |
| Shorts UI zones | — | **0 FAIL** / 387 frames |
| Picture vs speech, every cue vs Whisper | 85 cues · median 0.00s · **max 0.23s** | 41 cues · median 0.00s · **max 0.00s** |
| Captions (`.srt` / `.vtt`) | 122 cues · in order, no overlaps, in range · ≤2×42 · text = narration (written forms) | 34 cues · same |
| YouTube copy | title 56 chars · description 4,710 / 5,000 · **16 chapters match the master's beat starts** | title 64 chars · description 1,507 · link placeholder to fill |

**Rubric (unchanged):** long teaching **10/12** (the two 1s are by design), Short trailer gate **12/12**.
**Production gate: PASS** for both. **Verdict: clear-for-public**, both films.

**Open, and all yours at upload:**
- the altered/synthetic-content toggle
- a custom thumbnail (frame 0 is cream)
- the Short's link to the long
- optional: the "Using that word…" wording (Gate P + new audio)
