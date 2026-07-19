# BUILD-REPORT.md — nbb-vox-p53-circuit

**Build date:** 2026-07-16
**Builder:** Claude Code (claude-sonnet-4-6)

---

## Source and reel

| Field | Value |
|---|---|
| SOURCE_VIDEO | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-p53-circuit/vox-p53-circuit-slate.mp4` |
| SOURCE_REEL | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-p53-circuit/` |
| Source SHA-256 (pre-build) | `dda5b9bf5c7b601d6314b6e86813cee4f99e0a75a8fa64cad6c2ca3d173a7ada` |
| Source SHA-256 (post-build) | `dda5b9bf5c7b601d6314b6e86813cee4f99e0a75a8fa64cad6c2ca3d173a7ada` |
| SHA-256 match | **PASS** — source file untouched |

---

## SOURCE-DISCOVERY.md

**Path:** `nbb-vox-p53-circuit/SOURCE-DISCOVERY.md`

**Selection evidence:** Unambiguous — the supplied MP4 is the production reel's own output file, living directly inside the canonical source folder. `beat_sheet.json`, all `clips/B*.mp4` (B01–B17), all `mp3/beat-*.mp3`, `FACTCHECK.md`, `PEDAGOGY.md`, `manim/`, `media/` all present.

---

## Discovered media locations

| Category | Location |
|---|---|
| Beat sheet | `vox-p53-circuit/beat_sheet.json` |
| Body clips B01–B15 | `vox-p53-circuit/clips/B01–B15.mp4` |
| Body MP3s B01–B15 | `vox-p53-circuit/mp3/beat-B01–B15.mp3` |
| Source PEDAGOGY | `vox-p53-circuit/PEDAGOGY.md` (VERDICT: PASS) |
| Source FACTCHECK | `vox-p53-circuit/FACTCHECK.md` |
| Source QC sheet | `vox-p53-circuit/qc-sheet.png` |

---

## Old outro removal

| Field | Value |
|---|---|
| Removed beat IDs | B16 (`OutroSeries`), B17 (`OutroCTA`) |
| Removal timecode | 241.614 s (sum of B01–B15 actual_duration_s) |
| Stream-copy cut | `ffmpeg -t 241.614 -c copy body-locked.mp4` → 241.708 s extracted (stream-copy frame boundary) |

---

## Locked body

| Field | Value |
|---|---|
| Duration | 241.708 s (stream-copy extract) |
| Beats | B01–B15 (15 beats) |
| Audio | Original narration, unchanged |
| Clips | `vox-p53-circuit/clips/B01–B15.mp4`, locked untouched |

---

## New cold open (B_LIAM)

| Field | Value |
|---|---|
| Question | "Why does the same DNA damage kill one cell but let another divide?" |
| Greeting | "Merhaba, Liam" (Turkish hello) |
| Intro | "this is Liam, in for Bear" |
| Handoff line | "Can you explain it, Bear?" |
| Voice engine | Kokoro `am_onyx` (Liam in-for-Bear) |
| Audio path | `nbb-vox-p53-circuit/mp3/beat-B_LIAM.mp3` |
| Audio duration | 19.31 s |
| Visual | `ClaudeComposerAsk` (Remotion, Claude fidelity skin) |
| Visual rendered | `nbb-vox-p53-circuit/media/B_LIAM.mp4` |
| Wrapper clip | `nbb-vox-p53-circuit/wrapper-clips-44k/clip-B_LIAM.mp4` (19.333 s) |

---

## New verdict (B_VERDICT)

| Field | Value |
|---|---|
| Voice engine | Kokoro `am_onyx` (Liam in-for-Bear) |
| Audio path | `nbb-vox-p53-circuit/mp3/beat-B_VERDICT.mp3` |
| Audio duration | 43.20 s |
| Visual | `ClaudeVerdictArtifact` (Remotion, Claude fidelity skin, 4 artifact lines) |
| Visual rendered | `nbb-vox-p53-circuit/media/B_VERDICT.mp4` |
| Wrapper clip | `nbb-vox-p53-circuit/wrapper-clips-44k/clip-B_VERDICT.mp4` (43.208 s) |
| Key content | p53 as threshold filter (not binary switch); MDM2 kinase-load model; single load-bearing bottleneck; TP53 as most mutated gene |

---

## "Your turn" handoff (B_HANDOFF)

| Field | Value |
|---|---|
| Voice engine | Kokoro `am_onyx` |
| Audio path | `nbb-vox-p53-circuit/mp3/beat-B_HANDOFF.mp3` |
| Audio duration | 6.12 s |
| Visual | `ClaudeComposerAsk` with `greeting: "Your turn."`, `runningText: "paste this into Claude…"` |
| Visual rendered | `nbb-vox-p53-circuit/media/B_HANDOFF.mp4` |
| Wrapper clip | `nbb-vox-p53-circuit/wrapper-clips-44k/clip-B_HANDOFF.mp4` (6.125 s) |
| Paste-ready prompt | p53 reactivation strategies, APR-246/eprenetapopt, MDM2 inhibitors vs BCL-2 family — therapeutic angle |

---

## Claude title outro (B_OUTRO)

| Field | Value |
|---|---|
| Title | "Why Cancer Cannot Read Its Own Death Instructions" |
| Handle | `@NikBearBrown` |
| Subline | "p53 is the hinge — remove it and the kill-switch has no trigger" |
| Voice | Silent (5.0 s) |
| Visual | `ClaudeTitleOutro` (Remotion, Claude fidelity skin) |
| Visual rendered | `nbb-vox-p53-circuit/media/B_OUTRO.mp4` |
| Wrapper clip | `nbb-vox-p53-circuit/wrapper-clips-44k/clip-B_OUTRO.mp4` (5.013 s) |

---

## Final MP4

| Field | Value |
|---|---|
| Path | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/nbb-vox-p53-circuit/mp4/vox-p53-circuit-nbb.mp4` |
| Duration | 315.411 s (5m 15s) |
| Dimensions | 1920×1080 |
| FPS | 24 |
| Video codec | h264 |
| Audio codec | aac 44100 Hz stereo |
| File size | 6,628,250 bytes (6.32 MB) |
| Audio present | Yes |
| ffprobe status | **PASS** |

**Assembly structure:**
```
B_LIAM cold open (19.333 s) — Liam/Kokoro + ClaudeComposerAsk
↓
Body B01–B15 (241.708 s) — locked, stream-copy from source
↓
B_VERDICT (43.208 s) — Liam/Kokoro + ClaudeVerdictArtifact
↓
B_HANDOFF (6.125 s) — Liam/Kokoro + ClaudeComposerAsk "Your turn."
↓
B_OUTRO (5.013 s) — silent + ClaudeTitleOutro
```

**Total: 315.387 s (expected) vs 315.411 s (actual) — within 0.024 s, PASS**

---

## Assembly method

1. Body extracted via stream-copy (`ffmpeg -t 241.614 -c copy`) from source — no re-encode of body.
2. Wrapper clips encoded: Remotion visuals (30fps → looped to audio duration) + Kokoro audio → `libx264 -preset fast -crf 20 -r 24 + aac`.
3. Wrapper clips re-encoded to 44100 Hz audio (matching body sample rate) for clean concat.
4. Final concat via `ffmpeg -f concat -safe 0 -c copy` — single pass.

---

## PEDAGOGY verdict

VERDICT: PASS (see `PEDAGOGY.md`)

## FACTCHECK verdict

VERDICT: PASS (see `FACTCHECK.md`)

## QC sheet

`/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/nbb-vox-p53-circuit/QC-sheet.png`

14 frames: B_LIAM cold open, B_LIAM command typed, B01 title card, B03 question, B04 expected circuit, B06 p53 hub, B07 PUMA/NOXA/BAX fan, B09 full circuit, B10 circuit collapse, B13 two-cell example, B15 recap endcard, B_VERDICT artifact, B_HANDOFF "Your turn.", B_OUTRO title poster.

---

## SOURCE SHA-256 VERIFICATION

| File | Pre-build SHA-256 | Post-build SHA-256 | Match |
|---|---|---|---|
| `vox-p53-circuit-slate.mp4` | `dda5b9bf5c7b601d6314b6e86813cee4f99e0a75a8fa64cad6c2ca3d173a7ada` | `dda5b9bf5c7b601d6314b6e86813cee4f99e0a75a8fa64cad6c2ca3d173a7ada` | **PASS** |

---

## NOTE — All wrapper beats use Kokoro am_onyx (Liam)

Per the NBB-wrap protocol for this build: ALL new wrapper beats use Kokoro `am_onyx` (Liam, in for Bear). No ElevenLabs spend. The body retains its original ElevenLabs Bear narration unchanged.

To upgrade wrapper beats to Bear's ElevenLabs voice when the key is valid:
1. Fix `ELEVENLABS_API_KEY` in `brutalist-art/.env`
2. Run: `python3 brutalist-art/runtime/scripts/generate_audio.py cancer-biology/youtube/nbb-vox-p53-circuit --only B_LIAM B_VERDICT B_HANDOFF`
3. Re-conform wrapper clips and re-assemble

---

## Ready-to-open command

```bash
open /Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/nbb-vox-p53-circuit/mp4/vox-p53-circuit-nbb.mp4
```
