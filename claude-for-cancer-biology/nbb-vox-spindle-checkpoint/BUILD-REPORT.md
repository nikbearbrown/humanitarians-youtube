# BUILD-REPORT.md — NBB-wrap: vox-spindle-checkpoint

**Date:** 2026-07-16 (rebuilt from review cut)
**Protocol:** NBB-wrap (unattended build)
**Rebuild reason:** Previous build (2026-07-16T12:27:25) used the slate as the body source. This rebuild uses the review cut, which contains the corrected B04 layout (chromosome alignment graphic). The old `beat_sheet.nbb.json` is preserved as `beat_sheet.nbb.old.json`.

---

## Source video and source reel

| Field | Value |
|---|---|
| SOURCE_VIDEO | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-spindle-checkpoint/vox-spindle-checkpoint-review.mp4` |
| SOURCE_REEL | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-spindle-checkpoint/` |
| Source SHA-256 (at discovery) | `41abfe354523c43330a2b9e0221c5373b153ff1a93d216b7f5916aaf41a056a7` |
| Source SHA-256 (at build end) | `41abfe354523c43330a2b9e0221c5373b153ff1a93d216b7f5916aaf41a056a7` |
| Source SHA-256 verification | **PASS — unchanged** |

---

## Preserved prior build artifacts

| Artifact | Notes |
|---|---|
| `beat_sheet.nbb.old.json` | Previous beat_sheet.nbb.json (body from slate) preserved before rebuild |
| All wrapper MP3s and rendered media | Reused unchanged: NBB00/NBB01/NBB02/NBB03 already correct |

---

## SOURCE-DISCOVERY.md path and candidates

- Path: `nbb-vox-spindle-checkpoint/SOURCE-DISCOVERY.md`
- Candidates considered: 1 (the supplied MP4's own parent directory)
- Selection evidence: Supplied MP4 was found inside the candidate directory. `beat_sheet.json` carries `metadata.slug = "vox-spindle-checkpoint"`. All referenced `mp3/` and `clips/` assets exist. Unambiguous single-candidate match.

---

## Discovered media, audio, Manim, and provenance

| Location | Role |
|---|---|
| `vox-spindle-checkpoint/beat_sheet.json` | Source beat sheet (13 body + 2 old outro beats) |
| `vox-spindle-checkpoint/clips/B01–B13.mp4` | Conformed body clips (reused in assembly) |
| `vox-spindle-checkpoint/clips/B14–B15.mp4` | Old outro clips (not reused) |
| `vox-spindle-checkpoint/mp3/beat-B01–B13.mp3` | Body audio (locked) |
| `vox-spindle-checkpoint/mp3/beat-B14–B15.mp3` | Old outro audio (not reused) |
| `vox-spindle-checkpoint/manim/B01–B13.mp4` | Manim renders for body beats |
| `vox-spindle-checkpoint/media/B02.mp4` | Remotion-rendered body still |
| `vox-spindle-checkpoint/PEDAGOGY.md` | Source pedagogy (VERDICT: PASS) |
| `vox-spindle-checkpoint/FACTCHECK.md` | Source factcheck |

---

## Old-outro removal

| Old outro beats | Timecode removed |
|---|---|
| B14 (OutroSeries) — act: OUTRO | Body trim at 169.913 s removes both B14 and B15 |
| B15 (OutroCTA) — act: OUTRO | Same trim |

**Old-outro start timecode (from beat_sheet.json):** Sum of B01–B13 actual_duration_s = 169.913 s
**Body extracted as:** `[00:00.000, 169.913)` via stream-copy from **review** MP4

---

## Locked body

| Field | Value |
|---|---|
| Beat IDs | B01, B02, B03, B04, B05, B06, B07, B08, B09, B10, B11, B12, B13 |
| Source MP4 | `vox-spindle-checkpoint-review.mp4` (corrected B04 layout) |
| Source clips reused | `../vox-spindle-checkpoint/clips/B01–B13.mp4` |
| Source audio reused | `../vox-spindle-checkpoint/mp3/beat-B01–B13.mp3` |
| Body duration | 169.913 s (from beat sheet) / 170.000 s (extracted, stream-copy rounding) |
| Encoding | Stream-copy from review cut (body not re-encoded) |

---

## New cold-open (NBB00) — unchanged from prior build

| Field | Value |
|---|---|
| Beat ID | NBB00 |
| Scene | ClaudeComposerAsk |
| Voice | Kore / Kokoro `af_kore` |
| Greeting | "Bonjour, Kore" |
| Question | "Why does a cell stop and wait at the moment chromosomes are ready to separate?" |
| Handoff sentence | "Can you explain it, Bear?" |
| Audio path | `nbb-vox-spindle-checkpoint/mp3/beat-NBB00.mp3` |
| Audio duration | 8.94 s |
| Engine | Kokoro (free, local) |

---

## New verdict (NBB01) — unchanged from prior build

| Field | Value |
|---|---|
| Beat ID | NBB01 |
| Scene | ClaudeVerdictArtifact |
| Voice | Kokoro `af_kore` (Bear substitute — ElevenLabs key invalid, see note below) |
| Narration | "Here's what the body just demonstrated. The spindle assembly checkpoint is not a readiness vote — it is a veto machine. One unattached kinetochore out of 92 can block the entire cell from dividing. The mechanism: that rogue kinetochore assembles MCC, which inhibits APC/C, which leaves securin intact, which keeps separase inactive. The chain holds until the last attachment is made. The trade-off: speed for accuracy. A cell that shortcuts this check gains time but risks aneuploidy — wrong chromosome counts, a known cancer driver. The checkpoint optimizes for fidelity over throughput, and that choice costs real minutes at every division." |
| Audio path | `nbb-vox-spindle-checkpoint/mp3/beat-NBB01.mp3` |
| Audio duration | 35.63 s |

---

## "Your turn" handoff (NBB02) — unchanged from prior build

| Field | Value |
|---|---|
| Beat ID | NBB02 |
| Scene | ClaudeComposerAsk |
| Greeting | "Your turn." (exact) |
| runningText | "paste this into Claude…" (exact) |
| Voice | Kokoro `af_kore` (Bear substitute — see note below) |
| Prompt | "Explain what happens in [cancer type] when the spindle assembly checkpoint is weakened. What proteins are mutated, what chromosome errors result, and why does aneuploidy drive tumor progression in this case?" |
| Audio path | `nbb-vox-spindle-checkpoint/mp3/beat-NBB02.mp3` |
| Audio duration | 7.17 s |

---

## Final outro (NBB03) — unchanged from prior build

| Field | Value |
|---|---|
| Beat ID | NBB03 |
| Scene | ClaudeTitleOutro |
| Title | "Why the Spindle Checkpoint Pause Is the Most Important Moment in Cell Division" |
| Handle | "@HumanitariansAI" |
| Subline | "one unattached kinetochore, entire cell arrested" |
| Audio | Silence (6.01 s) |
| Audio path | `nbb-vox-spindle-checkpoint/mp3/beat-NBB03.mp3` |

---

## Final MP4

| Field | Value |
|---|---|
| Path | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/nbb-vox-spindle-checkpoint/vox-spindle-checkpoint-nbb.mp4` |
| Duration | 227.791 s |
| Dimensions | 1920×1080 |
| FPS | 24 |
| Video codec | H.264 |
| Audio codec | AAC |
| Audio channels | 1 (mono) |
| Audio sample rate | 44100 Hz |
| File size | 4,773,217 bytes (~4.6 MB) |
| ffprobe check | PASS (non-trivial size, correct dimensions, audio present) |

**Expected duration check:** 8.96 (NBB00) + 170.00 (body) + 35.63 (NBB01) + 7.17 (NBB02) + 6.01 (NBB03) = **227.77 s** ≈ measured 227.791 s (within 0.02 s rounding — PASS)

---

## PEDAGOGY and FACTCHECK verdicts

| Document | Verdict |
|---|---|
| `PEDAGOGY.md` | VERDICT: PASS |
| `FACTCHECK.md` | VERDICT: PASS |
| Source `PEDAGOGY.md` (body) | VERDICT: PASS (inherited) |
| Source `FACTCHECK.md` (body) | Inherits from source reel |

---

## QC sheet

- Path: `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/nbb-vox-spindle-checkpoint/QC-sheet.png`
- 9-frame 3×3 contact sheet: cold open (NBB00 @4s), title card (B01 @12s), section card (B06 @60s), MCC cascade (B08 @90s), walkthrough (B12 @150s), endcard (B13 @165s), verdict (NBB01 @185s), your turn (NBB02 @217s), outro (NBB03 @224s)

---

## Assembly notes

**One final encode approach:** The body segment was extracted from the REVIEW cut (not the slate) via stream-copy at [00:00, 169.913s] (no re-encode of body video). The wrapper beats (NBB00, NBB01, NBB02, NBB03) were previously rendered and reused unchanged. The final MP4 was assembled using the ffmpeg concat demuxer (stream-copy) joining the 5 segments: norm_NBB00 + body + norm_NBB01 + norm_NBB02 + norm_NBB03. Non-monotonic DTS warnings at join points were auto-corrected by ffmpeg (standard behavior for stream-copy concat at codec-compatible segments). The body was never re-encoded.

---

## ElevenLabs API key note

The ElevenLabs API key (`ELEVENLABS_API_KEY` in `.env`) returned HTTP 401 Unauthorized during this build (`art keys` confirmed the key is invalid). Bear's verdict (NBB01) and handoff (NBB02) were generated with **Kokoro `af_kore`** as a Bear substitute (same voice as the cold open NBB00 — all wrapper beats use `af_kore` consistently).

**To upgrade to the proper Bear voice when the key is repaired:**
1. Update `beat_sheet.nbb.json` beats NBB01 and NBB02: change `"engine": "kokoro"` to `"engine": "elevenlabs"`, remove `"voice"`, add `"voice_env": "ELEVENLABS_VOICE_NIKBEARBROWN"`.
2. Run: `python3 runtime/scripts/generate_audio.py nbb-vox-spindle-checkpoint/ --only NBB01 NBB02`
3. Re-conform and re-assemble the final MP4.

---

## Source files SHA-256 verification result

**PASS.** Source review MP4 SHA-256 at discovery: `41abfe354523c43330a2b9e0221c5373b153ff1a93d216b7f5916aaf41a056a7`
Verified at build end: **identical**. Source files were never modified.

---

## Ready to review

```
open /Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/nbb-vox-spindle-checkpoint/vox-spindle-checkpoint-nbb.mp4
```
