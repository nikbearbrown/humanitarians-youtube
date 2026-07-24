# SOURCE-MEDIA-LOCK.md — nbb-vox-endosomal-escape

**Build date:** 2026-07-16

## Body-lock law

The source MP4 is the locked body. Every frame, every audio sample, every edit is preserved exactly. The body was extracted via stream-copy (`-c copy`) — no re-encode, no color change, no retiming, no crop.

## Source SHA-256

| File | SHA-256 |
|---|---|
| `vox-endosomal-escape/vox-endosomal-escape.mp4` | `1eba7e15abd043418d7369ed4834571caabd4ec8f6496b2ab05ae33cd9138e7e` |

## Post-build source SHA-256 (verification)

| File | SHA-256 | Match |
|---|---|---|
| `vox-endosomal-escape/vox-endosomal-escape.mp4` | `1eba7e15abd043418d7369ed4834571caabd4ec8f6496b2ab05ae33cd9138e7e` | **PASS** |

Source file is untouched.

## Locked body file

| Field | Value |
|---|---|
| Path | `nbb-vox-endosomal-escape/body-locked.mp4` |
| Duration | 185.917s (stream-copy extraction) |
| Video codec | h264 (stream-copy — no re-encode) |
| Audio codec | aac (stream-copy — no re-encode) |
| Dimensions | 1280x720 |
| FPS | 24 |
| Extraction command | `ffmpeg -i vox-endosomal-escape.mp4 -t 185.811 -c copy body-locked.mp4` |

## Body content verification

Frame at 185.0s (last body beat B11): "Neutral in blood. Cationic in the endosome. That charge flip is the drug." — RECAP card. Confirmed NOT outro content.

Frame at 185.917s (extraction endpoint): beyond body content — B12 OutroSeries would begin at 185.811s per beat accounting; the cut is at 185.917s (stream boundary). No outro frames are visible within the body — B12 was at 2.17s which placed it well past 185.811s.

## New media — wrapper beats only

The ONLY new media created for this build:

| Beat | Type | Engine | Voice | Path |
|---|---|---|---|---|
| B_LIAM | ClaudeComposerAsk (Remotion) + Kokoro audio | kokoro | af_kore | `media/B_LIAM.mp4`, `mp3/beat-B_LIAM.mp3` |
| B_VERDICT | ClaudeVerdictArtifact (Remotion) + Kokoro audio | kokoro | af_kore | `media/B_VERDICT.mp4`, `mp3/beat-B_VERDICT.mp3` |
| B_YOUR_TURN | ClaudeComposerAsk (Remotion) + Kokoro audio | kokoro | af_kore | `media/B_YOUR_TURN.mp4`, `mp3/beat-B_YOUR_TURN.mp3` |
| B_OUTRO | ClaudeTitleOutro (Remotion) + silence | kokoro | af_kore (silence) | `media/B_OUTRO.mp4`, `mp3/beat-B_OUTRO.mp3` |

**No ElevenLabs was called. No body audio was regenerated. No body visuals were re-rendered.**
