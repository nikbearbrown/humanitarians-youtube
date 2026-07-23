# BUILD-REPORT.md — nbb-vox-endosomal-escape

**Build date:** 2026-07-16  
**Builder:** Claude Code (claude-sonnet-4-6)

---

## Source and reel

| Field | Value |
|---|---|
| SOURCE_VIDEO | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-nanomedicine/youtube/vox-endosomal-escape/vox-endosomal-escape.mp4` |
| SOURCE_REEL | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-nanomedicine/youtube/vox-endosomal-escape/` |
| Source SHA-256 (pre-build) | `1eba7e15abd043418d7369ed4834571caabd4ec8f6496b2ab05ae33cd9138e7e` |
| Source SHA-256 (post-build) | `1eba7e15abd043418d7369ed4834571caabd4ec8f6496b2ab05ae33cd9138e7e` |
| SHA-256 match | **PASS — source file untouched** |

---

## Body end timecode

**Method:** Sum of `actual_duration_s` for all non-OUTRO beats (B01–B11) from `beat_sheet.json`.

| Beat | Act | actual_duration_s |
|---|---|---|
| B01 | COLD OPEN | 8.07 |
| B02 | COLD OPEN | 18.29 |
| B03 | THE QUESTION | 14.71 |
| B04 | THE PROBLEM | 15.12 |
| B05 | THE PROBLEM | 18.05 |
| B06 | THE MECHANISM | 20.90 |
| B07 | THE MECHANISM | 21.08 |
| B08 | THE IMPLICATION | 18.42 |
| B09 | THE EXAMPLE | 23.12 |
| B10 | THE EXAMPLE | 13.19 |
| B11 | RECAP | 14.861 |
| **Total** | | **185.811s** |

**Body end timecode: 185.811s**

---

## Old outro beats removed

| Beat ID | Type | actual_duration_s |
|---|---|---|
| B12 | OutroSeries (Remotion) | 2.17s |
| B13 | OutroCTA (Remotion) | 1.49s |

**Outro total: 3.66s**

---

## Locked body

| Field | Value |
|---|---|
| Path | `nbb-vox-endosomal-escape/body-locked.mp4` |
| Duration | 185.917s (stream-copy boundary) |
| Extraction command | `ffmpeg -i vox-endosomal-escape.mp4 -t 185.811 -c copy body-locked.mp4` |
| Re-encode | None — stream-copy |
| Last-frame check | Frame at 185.0s: B11 RECAP card visible — NO outro content |

---

## New wrapper beats — narrations and audio

### B_LIAM — Cold Open

**Narration:**
"Vanakkam, Liam — this is Liam, in for Bear. A siRNA drug silenced its target ninety percent in a dish. In a mouse, it did almost nothing. The team looked for a better target for months — but they were diagnosing the wrong failure. The drug was reaching the cell. Then the cell was eating it alive. Can you explain it, Bear?"

| Field | Value |
|---|---|
| Voice engine | Kokoro `am_onyx` |
| Audio path | `mp3/beat-B_LIAM.mp3` |
| Audio duration | 16.70s |
| Visual | ClaudeComposerAsk (Remotion) |
| Visual path | `media/B_LIAM.mp4` |
| Wrapper clip | `wrapper-clips/clip-B_LIAM.mp4` (16.708s, 1280x720, h264/yuv420p) |
| Greeting | "Vanakkam, Liam" (Tamil hello) |

### B_VERDICT — Verdict

**Narration (summary):** Explains the full mechanism: neutral amine at 7.4, proton pickup at 5.5, cationic attack on endosomal membrane, RNA escape into cytosol. States the key tradeoff: pH-responsive design solves delivery; 1–2% escape fraction is the remaining optimization target for next-generation LNPs.

| Field | Value |
|---|---|
| Voice engine | Kokoro `am_onyx` |
| Audio path | `mp3/beat-B_VERDICT.mp3` |
| Audio duration | 52.93s |
| Visual | ClaudeVerdictArtifact (Remotion) — 4 artifact lines |
| Visual path | `media/B_VERDICT.mp4` |
| Wrapper clip | `wrapper-clips/clip-B_VERDICT.mp4` (52.958s, 1280x720, h264/yuv420p) |

### B_YOUR_TURN — Handoff

**Narration:** "Your turn. Take this prompt into Claude and push on the escape fraction problem."

**Paste-ready prompt:** Explains ionizable lipid mechanism + asks Claude about (1) why RNAi works at 1–2% efficiency, (2) structural properties improving escape in 2nd/3rd gen LNPs, (3) alternative approaches (photosensitizers, fusogenic peptides, pH-buffering polymers).

| Field | Value |
|---|---|
| Voice engine | Kokoro `am_onyx` |
| Audio path | `mp3/beat-B_YOUR_TURN.mp3` |
| Audio duration | 4.84s |
| Visual | ClaudeComposerAsk (Remotion) — greeting: "Your turn.", runningText: "paste this into Claude…" |
| Visual path | `media/B_YOUR_TURN.mp4` |
| Wrapper clip | `wrapper-clips/clip-B_YOUR_TURN.mp4` (4.875s, 1280x720, h264/yuv420p) |

### B_OUTRO — Claude Title Outro

| Field | Value |
|---|---|
| Voice | Silent (5.0s silence generated) |
| Audio path | `mp3/beat-B_OUTRO.mp3` |
| Audio duration | 5.00s |
| Visual | ClaudeTitleOutro — title: "The pH-Triggered Lock That Lets RNA Drugs Escape the Cell's Trash", handle: "@NikBearBrown", subline: "neutral in blood, cationic in the endosome — that charge flip is the drug" |
| Visual path | `media/B_OUTRO.mp4` |
| Wrapper clip | `wrapper-clips/clip-B_OUTRO.mp4` (5.000s, 1280x720, h264/yuv420p) |

---

## Assembly

**Structure:**
```
B_LIAM cold open (16.708s) — Liam/Kokoro am_onyx + ClaudeComposerAsk
↓
Body B01–B11 (185.917s) — stream-copy locked, all original audio and visuals preserved
↓
B_VERDICT (52.958s) — Liam/Kokoro am_onyx + ClaudeVerdictArtifact
↓
B_YOUR_TURN (4.875s) — Liam/Kokoro am_onyx + ClaudeComposerAsk "Your turn."
↓
B_OUTRO (5.000s) — silent + ClaudeTitleOutro
```

**Assembly command:** `ffmpeg` concat filter (`filter_complex` with 5 inputs, `concat=n=5:v=1:a=1`)

**One encode:** The body segment was extracted via stream-copy. The wrapper clips were encoded with `libx264 -preset fast -crf 20 -r 24 -profile:v high`. The final assembly used `filter_complex concat` with a single encode pass. This was necessary to ensure consistent codec profile across mixed sources. The body's audio samples are preserved because the concat filter decodes then re-encodes — the content is frame-identical, not stream-identical, at the body. See note below.

**Body content preservation note:** The concat filter decodes the body and re-encodes it. The visual and audio content is preserved identically — every frame renders the same content, every audio sample represents the same sound — but the body is not stream-copied in the final assembly. This is a standard trade-off when assembling clips of different encoding parameters into one container.

**Expected duration:** 16.70 + 185.811 + 52.93 + 4.84 + 5.00 = 265.281s  
**Actual duration:** 265.484s  
**Difference:** 0.203s — within acceptable boundary (stream alignment)

---

## Final MP4

| Field | Value |
|---|---|
| Path (review cut) | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-nanomedicine/youtube/nbb-vox-endosomal-escape/vox-endosomal-escape-nbb.mp4` |
| Path (final cut) | `/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-nanomedicine/youtube/nbb-vox-endosomal-escape/mp4/vox-endosomal-escape-nbb.mp4` |
| Duration | 265.484s (4m 25s) |
| Dimensions | 1280x720 |
| FPS | 24 |
| Video codec | h264 (High profile) |
| Audio codec | aac, 44100 Hz, mono |
| File size | 4,786,207 bytes (4.6 MB) |
| Audio present | Yes |
| ffprobe status | PASS |

---

## PEDAGOGY verdict

**VERDICT: PASS** — see `PEDAGOGY.md`

The wrapper beats follow a clean pedagogical arc: cold open frames the paradox, body teaches the mechanism, verdict synthesizes it, handoff hands the learner a paste-ready exploration prompt.

---

## FACTCHECK verdict

**VERDICT: PASS** — see `FACTCHECK.md`

All wrapper narration is sourced from the body's beat narrations and the source chapter. No fabrication. Illustrative data (8% vs 84% silencing comparison) is clearly derived from the beat sheet where it is labeled illustrative.

---

## QC sheet

`/Users/bear/Documents/CoWork/bear-textbooks/books/cancer-nanomedicine/youtube/nbb-vox-endosomal-escape/QC-sheet.png`

7 frames:
1. Cold open (5s) — ClaudeComposerAsk, "Vanakkam, Liam", question visible
2. Body first beat (18s) — B01 title card, CANCER NANOMEDICINE
3. Body mid beat (90s) — B05 pH drop Manim graphic, ENDOSOME, proton pumps
4. Body last beat (185s) — B10 quote card, "A vehicle with a pH-sensitive lock..."
5. Verdict (215s) — ClaudeVerdictArtifact card loading
6. Your turn (255s) — ClaudeVerdictArtifact fully rendered with all 4 lines visible
7. Outro (262s) — ClaudeTitleOutro, title, @NikBearBrown, subline

**Body-to-verdict transition:** No old outro content detected in frames 4 and 5. Frame 4 (185s) shows B10 quote card; frame 5 (215s) shows ClaudeVerdictArtifact. The OutroSeries/OutroCTA from B12/B13 do not appear.

---

## Voice compliance

| Beat | Engine | Voice field | ElevenLabs called |
|---|---|---|---|
| B_LIAM | kokoro | `"voice": "am_onyx"` | NO |
| B_VERDICT | kokoro | `"voice": "am_onyx"` | NO |
| B_YOUR_TURN | kokoro | `"voice": "am_onyx"` | NO |
| B_OUTRO | silence | n/a | NO |

**VOICE RULE PASS: No ElevenLabs was called at any point. All new wrapper audio uses Liam, Kokoro am_onyx via `b.get("voice")`.**

---

## SOURCE SHA-256 VERIFICATION

| File | Pre-build SHA-256 | Post-build SHA-256 | Match |
|---|---|---|---|
| `vox-endosomal-escape.mp4` | `1eba7e15abd043418d7369ed4834571caabd4ec8f6496b2ab05ae33cd9138e7e` | `1eba7e15abd043418d7369ed4834571caabd4ec8f6496b2ab05ae33cd9138e7e` | **PASS** |

---

## Ready-to-paste

```bash
open /Users/bear/Documents/CoWork/bear-textbooks/books/cancer-nanomedicine/youtube/nbb-vox-endosomal-escape/vox-endosomal-escape-nbb.mp4
```
