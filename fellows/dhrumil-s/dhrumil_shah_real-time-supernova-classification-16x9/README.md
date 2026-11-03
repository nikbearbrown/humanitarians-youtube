# Seven Million Alerts a Night — 16:9

### How AI finds one exploding star in a flood of alerts

The landscape cut of a 2:44 science documentary on real-time supernova classification, for YouTube
and other widescreen players. Native 16:9 at 4K. Sixteen beats. Presented by **Dhrumil Shah**.
Every frame generated from code, every claim sourced on screen, **$0.00 spent.**

Sibling cut (vertical, 9:16): [`../real-time-supernova-classification-9x16/`](../real-time-supernova-classification-9x16/)
— same narration, clock, claims, captions and soundtrack; every scene redrawn for portrait.

---

## How it opens

> **"Hi, I am Dhrumil Shah, and this video is about how artificial intelligence helps astronomers
> sort millions of nightly sky alerts, to find the exploding stars that are actually worth a
> telescope's time."**

The introduction shows the presenter, a one-line summary and the six stages of the pipeline together
on one wide frame. Then the film proper runs from the 7,000,000 counter through SCAN → FOLLOW-UP to
the close.

---

## Watch

| File | Resolution | Size | Use |
|---|---|---:|---|
| [`output/supernova_alerts_4k_16x9.mp4`](output/supernova_alerts_4k_16x9.mp4) | 3840 × 2160 | 68.9 MB | 4K landscape master |
| [`output/supernova_alerts_1920x1080.mp4`](output/supernova_alerts_1920x1080.mp4) | 1920 × 1080 | 15.4 MB | Primary HD master |
| [`output/supernova_alerts_1280x720.mp4`](output/supernova_alerts_1280x720.mp4) | 1280 × 720 | 8.8 MB | Lightweight HD |
| [`output/supernova_alerts_proxy_960x540.mp4`](output/supernova_alerts_proxy_960x540.mp4) | 960 × 540 | 5.0 MB | Review / proxy |

All four: 30 fps · 4,914 frames · 163.80 s · H.264 / AAC · burned-in captions.
Caption sidecars: [`captions/captions.srt`](captions/captions.srt) · [`captions/captions.vtt`](captions/captions.vtt).
Cover art (16:9): [`thumbnails/`](thumbnails/) — 3840×2160, 1920×1080, 1280×720.

---

## The question and the answer

> If an observatory reports millions of changes in the sky every night, how do astronomers find the
> one exploding star that actually matters?

> **Machine learning does not identify supernovae. It ranks candidates, so that a scarce confirming
> measurement can be spent well.**

```
SCAN  →  SUBTRACT  →  ALERT  →  CLASSIFY  →  RANK  →  FOLLOW-UP
```

---

## Built for the wide frame

Every scene uses one grammar: **the left column says what the beat means; the stage shows the
mechanism.** The chrome, the six-stage pipeline rail, the captions and the source line run the full
width.

| Beat | Landscape composition |
|---|---|
| B00 | greeting + summary left; the six-stage route listed on the stage |
| B04 | template **left of** tonight's image — before → after in reading order |
| B05 | new − template → difference, written left to right like an equation |
| B11 | illustrative bars **beside** the published figures |
| B12 | the rising queue **beside** its outcome |
| B13 | the slewing dome **beside** the spectrum it measures |

Title-safe margins: 200 px left/right, 110 px top/bottom (~5%). Full per-beat work order:
[`SHOTLIST.md`](SHOTLIST.md). Frame-by-frame record: [`storyboard/STORYBOARD.md`](storyboard/STORYBOARD.md).

---

## Beats

| # | ID | Beat | Stage | VO |
|---|---|---|---|---:|
| 01 | B00 | **Presenter introduction** | — | 11.47 s |
| 02 | B01 | Cold open — the flood | — | 10.69 s |
| 03 | B02 | The impossible human problem | — | 8.81 s |
| 04 | B03 | The survey | SCAN | 9.91 s |
| 05 | B04 | Reference and new | SCAN | 8.70 s |
| 06 | B05 | Difference imaging | SUBTRACT | 10.24 s |
| 07 | B06 | What could it be | SUBTRACT | 10.73 s |
| 08 | B07 | The alert packet | ALERT | 11.88 s |
| 09 | B08 | The stream and the brokers | ALERT | 8.35 s |
| 10 | B09 | Two models, one trade | CLASSIFY | 11.10 s |
| 11 | B10 | The light curve | CLASSIFY | 10.07 s |
| 12 | B11 | Probabilities, not a verdict | CLASSIFY | 10.49 s |
| 13 | B12 | Prioritisation | RANK | 8.70 s |
| 14 | B13 | Follow-up and spectroscopy | FOLLOW-UP | 10.14 s |
| 15 | B14 | The limit | FOLLOW-UP | 9.21 s |
| 16 | B15 | Close | — | 6.93 s |

---

## The honesty contract

Enforced in the component, identical to the vertical cut:

- **The introduction makes no factual claim**, and its SOURCE line says so. It says "millions", not
  "seven million", so the headline figure is first stated — and qualified — in B01.
- **The 7,000,000 figure is the full-operations expectation**, never tonight's count.
- **The 81-day figure is labelled `DERIVED`**, with its arithmetic on screen.
- **Invented numbers are flagged before they appear** (`ILLUSTRATIVE VALUES` in B11).
- **Every published percentage carries its condition.**
- **Every astronomical image is synthetic and captioned as such.**
- **A SOURCE line is visible for the whole of every beat.**
- **The word "discovers" never appears.**

Claims: [`FACTCHECK.md`](FACTCHECK.md) · teaching audit: [`PEDAGOGY.md`](PEDAGOGY.md) · assets:
[`ASSETS.md`](ASSETS.md) · research: [`research.md`](research.md) · narration: [`script.md`](script.md).

---

## What is shared with the 9:16 cut, and what is new

| Shared, byte-identical | New for 16:9 |
|---|---|
| narration WAVs/MP3s and `timings.json` | `SupernovaAlerts16x9.tsx` + `chrome16x9.tsx` (every scene redrawn) |
| score, sound design, `mixdown.wav` | `sheet_26x14` landscape candidate sheet (new seed 9304) |
| caption sidecars (`.srt`, `.vtt`) | 16:9 cover art |
| 25 of 26 generated images | landscape delivery ladder |
| every claim, figure, source line | `scripts/preflight_stills.py` |

---

## Reproducing it

```bash
python scripts/generate_narration.py   # Kokoro narration + MEASURED timings
python assets/gen_sky.py               # astronomical imagery, incl. the landscape sheet
python assets/gen_audio.py             # score, sound design, final mix
python assets/gen_thumbnail.py         # 16:9 cover art
python scripts/build_beat_sheet.py     # beat_sheet.json, derived from the clock
python scripts/build_captions.py       # caption sidecars, parsed from the component
python scripts/render_4k.py --sync-only
python scripts/preflight_stills.py     # one still per beat, before committing to 4K
python scripts/render_4k.py            # render 4,914 frames at 3840x2160
python scripts/export_masters.py       # mux soundtrack, emit the four cuts
python scripts/build_storyboard.py     # storyboard + QC frames from the master
python scripts/final_qc.py             # automated checks
```

**Audio is the clock.** The composition imports `audio/timings.json`; beat sheet, captions, score
sections, effect placements and QC expectations all derive from the same file.

---

## Project layout

```
real-time-supernova-classification-16x9/
├── README.md  research.md  script.md  beat_sheet.json
├── SHOTLIST.md  FACTCHECK.md  PEDAGOGY.md  ASSETS.md  BUILD-LOG.md
├── audio/          16 beat WAVs + MP3s, narration master, mixdown, timings.json
├── captions/       captions.srt, captions.vtt
├── assets/         generators; generated/ imagery; music/; sfx/
├── scenes/
│   ├── remotion/   SupernovaAlerts16x9.tsx, chrome16x9.tsx
│   └── renders/    raw renderer output (narration only)
├── storyboard/     STORYBOARD.md, 16 strips, 48 frames
├── thumbnails/     16:9 cover art, 3 sizes
├── config/         video-config.json, render-config.json
├── scripts/        narration, render, preflight, export, captions, storyboard, QC
├── _qc/            preflight stills + sheet, final frames, contact sheet, render log
└── output/         the four delivered cuts
```

---

## Not published

There is no publishing machinery in this project. The masters stay in `output/`; uploading is a
separate human decision.

*Educational explainer. All astronomical imagery is synthetic. No new astronomical result is claimed
and no observation was performed for this film.*
