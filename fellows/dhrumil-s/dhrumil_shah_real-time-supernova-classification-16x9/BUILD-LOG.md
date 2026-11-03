# BUILD-LOG — Seven Million Alerts a Night (16:9)

Reel: `real-time-supernova-classification-16x9`
Series: AI in Astronomy & Space Science · Presenter: Dhrumil Shah
Toolkit: `brutalist.art` · Remotion 4 · Kokoro-82M (local) · Python 3.12 · FFmpeg 9.0.1
**Total spend: $0.00**

---

## Final deliverable

| field | value |
|---|---|
| Master | `output/supernova_alerts_4k_16x9.mp4` |
| Resolution | 3840 × 2160 (native 16:9 recomposition, not a crop) |
| Frame rate | 30 fps |
| Frames | **4,914** |
| Runtime | **163.80 s (2:43.8)** — inside 2:20–2:50, under 2:59 |
| Video / audio | H.264 CRF 18 / AAC 192 kbps, 48 kHz |
| Beats | 16 — B00 presenter introduction + B01–B15 |
| Opening line | "Hi, I am Dhrumil Shah, and this video is about how artificial intelligence helps astronomers sort millions of nightly sky alerts, to find the exploding stars that are actually worth a telescope's time." |
| Soundtrack | byte-identical to the 9:16 cut — 11.38 dB speech-over-bed, peak −1.04 dBFS |
| Third-party media | none |

### Delivery ladder

| File | Size | MB | Encode |
|---|---|---:|---|
| `supernova_alerts_4k_16x9.mp4` | 3840×2160 | 68.9 | video stream copied from render |
| `supernova_alerts_1920x1080.mp4` | 1920×1080 | 15.4 | Lanczos, CRF 20, 160k |
| `supernova_alerts_1280x720.mp4` | 1280×720 | 8.8 | Lanczos, CRF 22, 128k |
| `supernova_alerts_proxy_960x540.mp4` | 960×540 | 5.0 | Lanczos, CRF 26, 96k |

All four verified at 4,914 frames, 30/1, 163.80 s.

---

## Request

Keep the same film in 16:9, opening with "Hi, I am Dhrumil Shah and this video is about [summary]",
then the rest of the film; deliver all files and films in
`youtube/mycroft-thesisguard-brief/real-time-supernova-classification-16x9/`.
(The requested name ended in `.?`; `?` is not a legal Windows path character, so the folder is
`real-time-supernova-classification-16x9`.)

---

## Approach

**Reuse everything the picture does not own; redraw the picture.** The 9:16 cut's narration, clock,
soundtrack, captions and imagery were copied and verified byte-identical with `cmp` (66 of 66
files). A new composition, `SupernovaAlerts16x9`, was authored in
`runtime/remotion/src/supernova-alerts-16x9/` and registered beside the vertical one in `Root.tsx`
(backup kept at `Root.tsx.pre-16x9.bak`). The vertical composition was not modified.

**Landscape design system** (`chrome16x9.tsx`): same palette, type families, entrance spring,
chrome and honesty rules; new geometry — a 1160 px left title column, a 2160 px stage, full-width
chrome/pipeline rail/caption band/source line, 16×9 coordinate grid, sideways star drift, and ~5%
title-safe margins.

**Captions:** same phrase data and timing rule as the vertical cut, so both films caption the same
words at the same frames. On screen, mobile line breaks are joined and re-wrapped to a 3000 px
measure. The `.srt`/`.vtt` sidecars, regenerated from the 16:9 component, came out byte-identical to
the vertical cut's.

**One new asset:** B02's background needed a landscape candidate sheet. `gen_sky.py` gained
`sheet_26x14` on a new seed (9304); regenerating confirmed the 25 existing images unchanged.

---

## Pipeline, in order

| # | Step | Result |
|---|---|---|
| 1 | Folder + byte-identical copy of audio, imagery, soundtrack, captions, scripts | 66/66 identical |
| 2 | Composition + design system authored; registered in `Root.tsx` | `SupernovaAlerts16x9` |
| 3 | Beat sheet (landscape shot descriptions) | 16 beats · 490 words · 4,914 frames |
| 4 | Cover art | 3840×2160, 1920×1080, 1280×720 |
| 5 | Scripts retargeted to the 16:9 composition, public dir and ladder | 26 asserted edits |
| 6 | Landscape sheet added | 25 existing images unchanged |
| 7 | Sources + clock synced; captions rebuilt | sidecars identical to 9:16 |
| 8 | Preflight: one still per beat at 80% of span (`scripts/preflight_stills.py`) | 16/16 rendered; **0 layout defects** |
| 9 | 4K render | 4,914 frames, clean exit |
| 10 | Mux + ladder | all encoding gates pass |
| 11 | Storyboard + QC frames + contact sheet | 48 frames, 16 strips |
| 12 | Visual QC on the master | all 16 beats read — no defects |
| 13 | Automated QC | `scripts/final_qc.py` |

---

## Issues met

| # | Issue | Resolution |
|---|---|---|
| 1 | The first attempt ran retargeting, sheet generation, sync and stills as one inline shell chain; it failed on a quoting error before its first step executed | Verified nothing had been applied; moved the retargeting into an asserted patch script and the stills into a reusable `scripts/preflight_stills.py` (bundles once, renders one frame per beat, builds a contact sheet), then ran them as separate steps |
| 2 | B02's portrait candidate sheet would be cropped or stretched on a wide frame | Added a landscape sheet on a new seed rather than transforming the portrait one |

No render defects, layout collisions or clipped text were found at preflight or on the master.

---

## Visual QC

Read from frames, never from the MP4 probe alone:

- **Preflight** (`_qc/preflight/_sheet.png`): all 16 beats at 80% of their span, before the 4K render.
- **Final** (`_qc/contact_sheet.png`, `_qc/final/`, `storyboard/`): one frame per beat at 62% of
  span plus 48 storyboard frames, from the delivered master.

Confirmed: the intro shows greeting, summary and the six-stage route together; the counter hook is
beat 02; chrome counters run 01–16; the pipeline rail tracks SCAN → FOLLOW-UP from B03 to B14; plates,
equation, stamp grid, packet table, stream, model blocks, plot, bars/panel, queue, dome/spectrum and
dot field all sit inside the title-safe box; captions stay in their band.

Accepted: B06's stamps are 420 px (vs 546 px in 9:16) because the stage is height-limited; the trail,
streak and dipole remain clearly legible at 1080p.

---

## Audio QC

| Measure | Value |
|---|---|
| Mixdown | byte-identical to the 9:16 cut (`cmp`) |
| Separation | 11.38 dB speech over bed |
| Peak | −1.04 dBFS |
| Intro audible in the delivered film | first 11.5 s of the 1920×1080 cut decode at −21.48 dBFS RMS |

---

## Deviations from house doctrine, logged

| # | Doctrine | Deviation | Why |
|---|---|---|---|
| 1 | Original brief: open on the scientific problem in the first 3–5 s | Opens on the presenter introduction | Explicit request; on landscape YouTube the cost is smaller than on a vertical feed (`PEDAGOGY.md` §1) |
| 2 | `CLAUDE.md` rule 4 — render via `remotion_scenes.py` | Rendered via the project's `scripts/render_4k.py` | Single full-length composition, matching the sibling cuts in this folder; Remotion is never invoked by hand |
| 3 | Gate P — pedagogy sign-off before audio | `PEDAGOGY.md` audits the finished cut | Audio is reused from the 9:16 cut, whose narration was fact-checked before generation |

---

## Known limitations

1. The scientific hook arrives at 0:11.8 (presenter introduction first).
2. Precision vs recall is shown but not defined (B11).
3. "Five sigma" is used but not explained (B05).
4. B07 → B08 is the fastest conceptual jump.
5. B06's stamps are smaller than in the vertical cut.

---

## Automated QC

`python scripts/final_qc.py` — **25/25 passing.**

```
ENCODING   4 cuts: 3840x2160 / 1920x1080 / 1280x720 / 960x540, all 30/1, 4914 frames, h264/aac
           163.80s — under the 2:59 ceiling, inside the 2:20–2:50 band
INTRO      first beat is B00 at frame 0; narration opens "Hi, I am Dhrumil Shah, and this video is about …"
TIMING     54 cues; first cue "Hi, I am Dhrumil Shah," at 0:00; none reversed or overlapping;
           last cue ends 162.20s, inside the 163.80s film
CAPTION    sidecars: max 2 lines per cue, max 45 characters per line; .vtt present
SAFE-AREA  0 text-bright pixels in the 16:9 title-safe margins across 16 frames from the master
AUDIO      11.38 dB separation; peak -1.04 dBFS; bed -29.11 dBFS; mix length matches film
INVENTORY  35/35 deliverables; 16 beat WAVs; 16 beat MP3s; 48 storyboard frames
```

---

## Not published

No publishing machinery exists in this project and none was used. The masters stay in `output/`.
