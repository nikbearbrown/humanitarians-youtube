# BUILD-REPORT.md — nbb-vox-vhl-hif

**Build date:** 2026-07-16  
**Builder:** Claude Code (claude-sonnet-4-6)

---

## Source and reel

| Field | Value |
|---|---|
| SOURCE_VIDEO | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-vhl-hif/vox-vhl-hif-slate.mp4` |
| SOURCE_REEL | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-vhl-hif/` |
| Source SHA-256 | `4fc61d9cfe2efbcc56c7fe14d4b376e0fb97ee4d7ffd215cddd662b80b68f9d7` |
| Post-build SHA-256 | `4fc61d9cfe2efbcc56c7fe14d4b376e0fb97ee4d7ffd215cddd662b80b68f9d7` |
| SHA-256 match | **PASS** — source file untouched |

---

## SOURCE-DISCOVERY.md

**Path:** `nbb-vox-vhl-hif/SOURCE-DISCOVERY.md`

**Candidates considered:**
- `/cancer-biology/youtube/vox-vhl-hif/` — SELECTED (strongest evidence: supplied SOURCE_VIDEO lives directly inside this folder; `beat_sheet.json`, all `clips/B*.mp4`, all `mp3/beat-*.mp3`, `manim/`, `media/`, `FACTCHECK.md`, `PEDAGOGY.md` all present)

**Selection evidence:** Unambiguous — the supplied MP4 is the production reel's own output file. No detached copies found.

---

## Discovered media locations

| Category | Location |
|---|---|
| Beat sheet | `vox-vhl-hif/beat_sheet.json` |
| Body clips B01–B15 | `vox-vhl-hif/clips/B01–B15.mp4` |
| Body MP3s B01–B15 | `vox-vhl-hif/mp3/beat-B01–B15.mp3` |
| Manim renders | `vox-vhl-hif/manim/B01,B03–B15.mp4` |
| Remotion renders | `vox-vhl-hif/media/B02.mp4`, `B12.mp4`, `B16.mp4`, `B17.mp4` |
| Source PEDAGOGY | `vox-vhl-hif/PEDAGOGY.md` (VERDICT: PASS) |
| Source FACTCHECK | `vox-vhl-hif/FACTCHECK.md` |
| Source QC | `vox-vhl-hif/qc-sheet.png` |
| Vox scenes | `vox-vhl-hif/vox_scenes.py` |

---

## Old outro removal

| Field | Value |
|---|---|
| Removed beat IDs | B16 (`OutroSeries`), B17 (`OutroCTA`) |
| Removal timecode | `289.941 s` (start of B16 in source reel's actual-duration accounting) |
| Stream-copy cut | `ffmpeg -t 289.941 -c copy body-locked.mp4` → 290.042 s extracted |

---

## Locked body

| Field | Value |
|---|---|
| Duration | 290.042 s (stream-copy extract) |
| Beats | B01–B15 (15 beats) |
| Audio | Reused from `vox-vhl-hif/mp3/beat-B01–B15.mp3` (original ElevenLabs Bear voice) |
| Clips | Reused from `vox-vhl-hif/clips/B01–B15.mp4` (locked, untouched) |

**Body beat IDs and source paths:**

| Beat | Clip | Audio |
|---|---|---|
| B01 | `../vox-vhl-hif/clips/B01.mp4` | `../vox-vhl-hif/mp3/beat-B01.mp3` |
| B02 | `../vox-vhl-hif/clips/B02.mp4` | `../vox-vhl-hif/mp3/beat-B02.mp3` |
| B03 | `../vox-vhl-hif/clips/B03.mp4` | `../vox-vhl-hif/mp3/beat-B03.mp3` |
| B04 | `../vox-vhl-hif/clips/B04.mp4` | `../vox-vhl-hif/mp3/beat-B04.mp3` |
| B05 | `../vox-vhl-hif/clips/B05.mp4` | `../vox-vhl-hif/mp3/beat-B05.mp3` |
| B06 | `../vox-vhl-hif/clips/B06.mp4` | `../vox-vhl-hif/mp3/beat-B06.mp3` |
| B07 | `../vox-vhl-hif/clips/B07.mp4` | `../vox-vhl-hif/mp3/beat-B07.mp3` |
| B08 | `../vox-vhl-hif/clips/B08.mp4` | `../vox-vhl-hif/mp3/beat-B08.mp3` |
| B09 | `../vox-vhl-hif/clips/B09.mp4` | `../vox-vhl-hif/mp3/beat-B09.mp3` |
| B10 | `../vox-vhl-hif/clips/B10.mp4` | `../vox-vhl-hif/mp3/beat-B10.mp3` |
| B11 | `../vox-vhl-hif/clips/B11.mp4` | `../vox-vhl-hif/mp3/beat-B11.mp3` |
| B12 | `../vox-vhl-hif/clips/B12.mp4` | `../vox-vhl-hif/mp3/beat-B12.mp3` |
| B13 | `../vox-vhl-hif/clips/B13.mp4` | `../vox-vhl-hif/mp3/beat-B13.mp3` |
| B14 | `../vox-vhl-hif/clips/B14.mp4` | `../vox-vhl-hif/mp3/beat-B14.mp3` |
| B15 | `../vox-vhl-hif/clips/B15.mp4` | `../vox-vhl-hif/mp3/beat-B15.mp3` |

---

## New cold open (B_LIAM)

| Field | Value |
|---|---|
| Question | "Why does a broken oxygen sensor cause cancer to act permanently starved?" |
| Greeting | "Annyeong, Liam" (Korean hello) |
| Handoff line | "Can you explain it, Bear?" |
| Voice engine | Kokoro `am_onyx` (Liam in-for-Bear) |
| Audio path | `nbb-vox-vhl-hif/mp3/beat-B_LIAM.mp3` |
| Audio duration | 16.87 s |
| Visual | `ClaudeComposerAsk` (Remotion, Claude fidelity skin) |
| Visual rendered | `nbb-vox-vhl-hif/media/B_LIAM.mp4` |

---

## New verdict (B_VERDICT)

| Field | Value |
|---|---|
| Narration | "VHL is not the sensor. It is the reader. PHDs tag HIF-1 alpha — VHL converts that tag into a destruction order. Lose VHL and HIF-1 alpha accumulates regardless of oxygen. One missing protein, whole hypoxic program, permanently on. The trade-off that makes this devastating is the same one that makes normal oxygen sensing elegant: a single bottleneck. Efficient — until it is gone." |
| Voice engine | **Kokoro `am_onyx` PLACEHOLDER** — ElevenLabs API key invalid at build time (HTTP 401). See NOTE below. |
| Audio path | `nbb-vox-vhl-hif/mp3/beat-B_VERDICT.mp3` |
| Audio duration | 22.44 s |
| Visual | `ClaudeVerdictArtifact` (Remotion, Claude fidelity skin, 4 artifact lines) |
| Visual rendered | `nbb-vox-vhl-hif/media/B_VERDICT.mp4` |

---

## "Your turn" handoff (B_HANDOFF)

| Field | Value |
|---|---|
| Prompt | "I'm learning about clear cell kidney cancer and the VHL/HIF-1α pathway. VHL normally tags HIF-1α for destruction via ubiquitin ligase; in ccRCC, VHL is lost so HIF-1α accumulates constitutively. I understand belzutifan targets HIF-2α downstream. Can you walk me through: (1) why targeting HIF-2α rather than HIF-1α became the therapeutic bet, (2) what resistance mechanisms have emerged in belzutifan trials so far, and (3) what a combination approach with mTOR inhibitors is meant to address?" |
| Narration | "Your turn. Take this prompt into Claude and explore what happens when you stress-test the VHL-HIF axis from a drug-design angle." |
| Voice engine | **Kokoro `am_onyx` PLACEHOLDER** — ElevenLabs API key invalid at build time (HTTP 401). See NOTE below. |
| Audio path | `nbb-vox-vhl-hif/mp3/beat-B_HANDOFF.mp3` |
| Audio duration | 7.66 s |
| Visual | `ClaudeComposerAsk` with `greeting: "Your turn."`, `runningText: "paste this into Claude…"` |
| Visual rendered | `nbb-vox-vhl-hif/media/B_HANDOFF.mp4` |

---

## Claude title outro (B_OUTRO)

| Field | Value |
|---|---|
| Title | "Why a Broken Oxygen Sensor Causes a Cancer to Act Permanently Starved" |
| Handle | `@NikBearBrown` |
| Subline | "one missing protein — the whole program, permanently on" |
| Voice | Silent (5.04 s) |
| Visual | `ClaudeTitleOutro` (Remotion, Claude fidelity skin) |
| Visual rendered | `nbb-vox-vhl-hif/media/B_OUTRO.mp4` |

---

## Final MP4

| Field | Value |
|---|---|
| Path | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/nbb-vox-vhl-hif/vox-vhl-hif-nbb.mp4` |
| Duration | 342.106 s (5m 42s) |
| Dimensions | 1920×1080 |
| FPS | 24 |
| Video codec | h264 |
| Audio codec | aac 44100 Hz |
| File size | 6,727,545 bytes |
| Audio present | Yes |
| ffprobe status | PASS |

**Assembly structure:**
```
B_LIAM cold open (16.875 s) — Liam/Kokoro + ClaudeComposerAsk
↓
Body B01–B15 (290.042 s) — locked, stream-copy from source
↓
B_VERDICT (22.458 s) — Bear/Kokoro-placeholder + ClaudeVerdictArtifact
↓
B_HANDOFF (7.667 s) — Bear/Kokoro-placeholder + ClaudeComposerAsk "Your turn."
↓
B_OUTRO (5.042 s) — silent + ClaudeTitleOutro
```

**Total: 342.084 s (expected) vs 342.106 s (actual) — within 0.022 s, PASS**

---

## Encode note

One encode was performed to conform the wrapper Remotion renders (30fps) to 24fps and duration-match the audio. The body segment was extracted from the source via stream-copy (`-c copy`) — no re-encode of the body. The wrapper clips were encoded with `libx264 -preset fast -crf 20 -r 24`. The final assembly concatenated all segments with stream-copy.

---

## PEDAGOGY verdict

VERDICT: PASS (see `PEDAGOGY.md`)

## FACTCHECK verdict

VERDICT: PASS (see `FACTCHECK.md`)

## QC sheet

`/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/nbb-vox-vhl-hif/QC-sheet.png`

14 frames: cold open, B01 title, B02 histology, B03 HIF hub, B07 normal path, B08 VHL absent, B09 constitutive HIF, B10 side-by-side, B12 consequences, B14 VHL-null timeline, B15 recap, B_VERDICT, B_HANDOFF, B_OUTRO.

---

## SOURCE SHA-256 VERIFICATION

| File | Expected SHA-256 | Post-build SHA-256 | Match |
|---|---|---|---|
| `vox-vhl-hif-slate.mp4` | `4fc61d9cfe2ef...` | `4fc61d9cfe2ef...` | **PASS** |
| `beat_sheet.json` | `1b17b1516bc53...` | `1b17b1516bc53...` | **PASS** |
| `clips/B01.mp4` | `5ba10116dd16d...` | `5ba10116dd16d...` | **PASS** |
| `clips/B15.mp4` | `a1f7561a6e6a3...` | `a1f7561a6e6a3...` | **PASS** |

---

## CRITICAL NOTE — ElevenLabs API key invalid

`ELEVENLABS_API_KEY` returned HTTP 401 at build time (`art keys` confirmed "invalid"). B_VERDICT and B_HANDOFF were generated using Kokoro `am_onyx` (the same Liam voice) as a **placeholder**. This is a previz-quality audio track — the content is correct, the voice is not Bear's ElevenLabs clone.

**To upgrade to Bear's voice:**
1. Fix `ELEVENLABS_API_KEY` in `brutalist-art/.env`
2. Run: `python3 brutalist-art/runtime/scripts/generate_audio.py cancer-biology/youtube/nbb-vox-vhl-hif --only B_VERDICT B_HANDOFF`
3. Re-conform and re-assemble: the verdict visual (B_VERDICT.mp4, 22.44s) and handoff visual (B_HANDOFF.mp4, 7.66s) may need duration adjustment if the ElevenLabs durations differ
4. The beat sheet has `_elevenlabs_pending: true` on these beats as a reminder

---

## Ready-to-paste command

```bash
open /Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/nbb-vox-vhl-hif/vox-vhl-hif-nbb.mp4
```
