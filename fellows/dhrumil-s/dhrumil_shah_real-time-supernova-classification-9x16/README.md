# Seven Million Alerts a Night

### How AI finds one exploding star in a flood of alerts

A 2:44 vertical science documentary on real-time supernova classification, for YouTube Shorts,
Instagram Reels, TikTok and LinkedIn. Native 9:16 at 4K. Sixteen beats. Presented by **Dhrumil
Shah**. Every frame generated from code, every claim sourced on screen, **$0.00 spent.**

**Series:** AI in Astronomy & Space Science

---

## How it opens

> **"Hi, I am Dhrumil Shah, and this video is about how artificial intelligence helps astronomers
> sort millions of nightly sky alerts, to find the exploding stars that are actually worth a
> telescope's time."**

The introduction card names the presenter, gives the film in one line, and previews the six stages
the film walks through. Then the film proper runs: the cold-open counter, the problem, and the
pipeline from SCAN to FOLLOW-UP.

---

## The question

> If an observatory reports millions of changes in the sky every night, how do astronomers find the
> one exploding star that actually matters?

And the answer the film is careful to land:

> **Machine learning does not identify supernovae. It ranks candidates, so that a scarce confirming
> measurement can be spent well.**

---

## Watch

| File | Resolution | Size | Use |
|---|---|---:|---|
| [`output/supernova_alerts_4k_vertical.mp4`](output/supernova_alerts_4k_vertical.mp4) | 2160 × 3840 | 83.4 MB | 4K vertical master |
| [`output/supernova_alerts_1080x1920.mp4`](output/supernova_alerts_1080x1920.mp4) | 1080 × 1920 | 14.8 MB | Primary social master |
| [`output/supernova_alerts_720x1280.mp4`](output/supernova_alerts_720x1280.mp4) | 720 × 1280 | 8.1 MB | Lightweight HD |
| [`output/supernova_alerts_proxy_540x960.mp4`](output/supernova_alerts_proxy_540x960.mp4) | 540 × 960 | 4.7 MB | Review / proxy |

All four: 30 fps · 4,914 frames · 163.80 s · H.264 / AAC · burned-in captions.
Caption sidecars: [`captions/captions.srt`](captions/captions.srt) · [`captions/captions.vtt`](captions/captions.vtt).
Cover art: [`thumbnails/`](thumbnails/).

---

## The pipeline the film teaches

Previewed in the introduction, then carried as a rail across every beat from B03 to B14:

```
SCAN  →  SUBTRACT  →  ALERT  →  CLASSIFY  →  RANK  →  FOLLOW-UP
```

| Stage | What happens | Who does it |
|---|---|---|
| SCAN | Wide-field repeat imaging | Rubin Observatory / LSST |
| SUBTRACT | Difference imaging against a deep template; SNR > 5 counts as a detection | Rubin Prompt Processing |
| ALERT | A packet per detection — position, brightness, time, 12 months of history, cutouts — out within 60 s | Rubin DMS |
| CLASSIFY | Stamp CNN on detection #1; light-curve random forest once ≥6 detections exist | Community brokers |
| RANK | Filtering, scoring, prioritisation | Brokers + science teams |
| FOLLOW-UP | Spectroscopy — the measurement that actually decides | Other telescopes entirely |

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

Beat IDs stayed stable when the introduction was added as B00, so every scene, caption, source line
and fact-check row still refers to the same content. Full frame specification with three stills per
beat: [`storyboard/STORYBOARD.md`](storyboard/STORYBOARD.md).

---

## The honesty contract

Enforced in the component, not just asserted in the docs:

- **The introduction makes no factual claim**, and its SOURCE line says so. It says "millions", not
  "seven million", so the headline figure is first stated — and qualified — in B01.
- **The 7,000,000 figure is the full-operations expectation**, never tonight's count. Rubin issued
  800,000 on its first public-alert night (2026-02-24).
- **The 81-day figure is labelled `DERIVED`**, with its arithmetic on screen.
- **Invented numbers are flagged before they appear** (`ILLUSTRATIVE VALUES` in B11).
- **Every published percentage carries its condition** — "~90% accurate" never appears without "on a
  balanced test set", spoken and on screen.
- **Every astronomical image is synthetic and captioned as such.**
- **A SOURCE line is visible for the whole of every beat.**
- **The word "discovers" never appears.** The intro's verb is *sort*.

Claim-by-claim verification: [`FACTCHECK.md`](FACTCHECK.md) · teaching audit, including what the
introduction costs and what it adds: [`PEDAGOGY.md`](PEDAGOGY.md).

---

## Everything here is original

No archival imagery, stock, licensed music, sound library, AI-generated stills, screen recordings or
embedded fonts.

- **Astronomical imagery** — 25 seeded PNGs from [`assets/gen_sky.py`](assets/gen_sky.py).
- **Narration** — Kokoro-82M `am_onyx`, local. No API key, no network, no cost.
- **Score** — original D-minor composition, seven sections defined by beat span, from
  [`assets/gen_audio.py`](assets/gen_audio.py); cue sheet in [`assets/music/`](assets/music/).
- **Sound design** — every effect synthesised and placed against a measured beat start.
- **Diagrams, plots, spectra, streams, the pipeline preview** — drawn in the Remotion component.

Full inventory: [`ASSETS.md`](ASSETS.md).

---

## Built for the vertical canvas

- **B00** lists the six stages down the canvas as the route the film will take.
- **B04** stacks template above new visit — a temporal reading order.
- **B05** runs the subtraction downward.
- **B08** drops packets 1,090 px into seven broker lanes.
- **B12** lifts the tracked candidate nine rows to the top of the queue.

Safe area: 140 left / 150 right / 250 top / **640 bottom**, clear of Shorts, Reels and TikTok UI.
`scripts/final_qc.py` checks it on sampled frames from the delivered master.

---

## Reproducing it

Everything is local and free.

```bash
python scripts/generate_narration.py   # Kokoro narration + MEASURED timings
python assets/gen_sky.py               # astronomical imagery
python assets/gen_audio.py             # score, sound design, final mix
python assets/gen_thumbnail.py         # cover art
python scripts/build_beat_sheet.py     # beat_sheet.json, derived from the clock
python scripts/build_captions.py       # captions.srt / .vtt, parsed from the component
python scripts/render_4k.py            # sync sources + timings, render 4,914 frames
python scripts/export_masters.py       # mux soundtrack, emit the four cuts
python scripts/build_storyboard.py     # storyboard + QC frames from the master
python scripts/final_qc.py             # automated checks
```

**Audio is the clock.** The composition imports `audio/timings.json` directly, and the beat sheet,
captions, score sections, sound-effect placements and QC expectations are all derived from the same
file. Nothing is hand-timed — change a line of narration and the whole timeline moves with it.

---

## Project layout

```
real-time-supernova-classification-9x16/
├── README.md            this file
├── research.md          research brief
├── script.md            final narration, beat by beat, including the introduction
├── beat_sheet.json      machine-readable production record (derived)
├── SHOTLIST.md          typed work order, one block per beat
├── FACTCHECK.md         claims, verdicts, sources; what was cut and why
├── PEDAGOGY.md          teaching audit, including the introduction trade-off
├── ASSETS.md            asset inventory and licensing position
├── BUILD-LOG.md         build record, defect log, QC results
├── audio/               16 beat WAVs + MP3s, narration master, mixdown, timings.json
├── captions/            captions.srt, captions.vtt
├── assets/              generators; generated/ imagery; music/; sfx/
├── scenes/
│   ├── remotion/        SupernovaAlerts9x16.tsx, chrome.tsx
│   └── renders/         raw renderer output (narration only)
├── storyboard/          STORYBOARD.md, 16 strips, 48 frames
├── thumbnails/          cover art, 3 sizes
├── config/              video-config.json, render-config.json
├── scripts/             narration, render, export, captions, storyboard, QC
├── _qc/                 preflight stills, final frames, contact sheet, render log
└── output/              the four delivered cuts
```

---

## Sources

Nine primary and official sources, listed in full in [`FACTCHECK.md`](FACTCHECK.md). Load-bearing:

- **DMTN-102, *LSST Alerts: Key Numbers*** (Graham et al. 2024) — 60 s latency requirement, SNR > 5
  threshold, packet contents, ~1,000 visits per night.
- **Rubin Observatory, *Alert Stream*** and **news release 2026-02-25** — about seven million alerts
  per night at full operations; 800,000 on the first night.
- **Förster et al. 2021, AJ 161, 242 — *The ALeRCE Alert Broker*** — stamp and light-curve
  classifiers; 90% balanced-test-set accuracy; 81% recall on TNS-confirmed SNe.
- **TiDES / 4MOST capacity and LSST photometric-cosmology forecasts** — ~1,000,000 supernovae
  expected against ~30,000 planned spectra.

---

## Not published

There is no publishing machinery in this project. The masters stay in `output/`; uploading is a
separate human decision.

*Educational explainer. All astronomical imagery is synthetic. No new astronomical result is claimed
and no observation was performed for this film.*
