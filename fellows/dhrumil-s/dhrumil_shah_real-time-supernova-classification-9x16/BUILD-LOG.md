# BUILD-LOG — Seven Million Alerts a Night

Reel: `real-time-supernova-classification-9x16`
Series: AI in Astronomy & Space Science · Presenter: Dhrumil Shah
Toolkit: `brutalist.art` · Remotion 4 · Kokoro-82M (local) · Python 3.12 · FFmpeg 9.0.1
**Total spend: $0.00**

---

## Final deliverable

| field | value |
|---|---|
| Master | `output/supernova_alerts_4k_vertical.mp4` |
| Resolution | 2160 × 3840 (native 9:16, not cropped) |
| Frame rate | 30 fps |
| Frames | **4,914** |
| Runtime | **163.80 s (2:43.8)** — inside the 2:20–2:50 target, under the 2:59 ceiling |
| Video / audio | H.264 CRF 18 / AAC 192 kbps, 48 kHz |
| Beats | 16 — B00 presenter introduction + B01–B15 |
| Opening line | "Hi, I am Dhrumil Shah, and this video is about how artificial intelligence helps astronomers sort millions of nightly sky alerts, to find the exploding stars that are actually worth a telescope's time." |
| Measured narration | 157.40 s speech · 162.21 s with 0.32 s gaps · 1.58 s closing tail |
| Soundtrack | speech −17.73 dBFS · bed −29.11 dBFS · **11.38 dB separation** · peak −1.04 dBFS |
| Slots filled | 16 / 16 — no slates, no placeholders, no human-supply slots |
| Third-party media | none |

### Delivery ladder

| File | Size | MB | CRF | Audio |
|---|---|---:|---|---|
| `supernova_alerts_4k_vertical.mp4` | 2160×3840 | 83.4 | 18 (video stream copied from render) | 192k |
| `supernova_alerts_1080x1920.mp4` | 1080×1920 | 14.8 | 20, Lanczos | 160k |
| `supernova_alerts_720x1280.mp4` | 720×1280 | 8.1 | 22, Lanczos | 128k |
| `supernova_alerts_proxy_540x960.mp4` | 540×960 | 4.7 | 26, Lanczos | 96k |

All four verified at 4,914 frames, 30/1, 163.80 s.

---

## This build: adding the presenter introduction

**Request:** keep the same 9:16 film, but open with "Hi, I am Dhrumil Shah and this video is about
[summary]", then run the rest of the film; deliver all files and films in
`youtube/mycroft-thesisguard-brief/real-time-supernova-classification-9x16/`.

**Starting state.** The previous reel folder at that path no longer existed. What survived was the
Remotion source in `runtime/remotion/src/supernova-alerts/` (verified to be the final, fully-patched
version) and the staged narration and imagery in `runtime/remotion/public-supernova-alerts/`. All
scripts, documents, WAVs, captions, storyboard and films were rebuilt into a fresh folder.

**What changed in the film**

| # | Change | Where |
|---|---|---|
| 1 | New beat **B00** — narration, measured at 11.47 s | `scripts/generate_narration.py` |
| 2 | New scene **S00** — greeting, one-line summary, six-stage pipeline preview drawn down a spine | `SupernovaAlerts9x16.tsx` |
| 3 | B00 captions (4 cues) and a SOURCE line stating the intro makes no factual claim | `SupernovaAlerts9x16.tsx` |
| 4 | Chrome counter now reads NN / 16 | automatic, from beat count |
| 5 | Score gains a quiet "welcome" section; every later section shifts with its beats | `assets/gen_audio.py` |
| 6 | Intro sound design: a D-minor chord under the greeting, one blip per stage row | `assets/gen_audio.py` |
| 7 | Everything else — B01–B15 narration, visuals, sources — unchanged | — |

Beat IDs were kept stable (the intro is B00, not a renumbering of B01–B15), so every existing
caption, source line, scene component and fact-check row still refers to the same content.
Deliverable WAVs are numbered by play order: `beat_01.wav` is the introduction.

**Reproducibility confirmed during the rebuild**

- **Kokoro is deterministic.** Regenerating all sixteen beats reproduced the fifteen original beats'
  measured durations exactly; only B00 is new.
- **Imagery is deterministic.** `gen_sky.py`, rebuilt from its final recipe, produced 25 PNGs
  **byte-identical** to the previously staged set.

---

## Structural fixes made while rebuilding

The introduction shifted every time value in the film by 11.79 s. Rather than re-type those values,
the places that had them hard-coded were changed to derive them:

| # | Before | After |
|---|---|---|
| 1 | Composition carried a hand-copied table of 15 measured durations and a literal `4560` frame count | Composition **imports `audio/timings.json`**; total frames computed as `round((Σ durations + gaps + 1.58 s tail) × 30)`. `render_4k.py` syncs the file |
| 2 | Score sections defined in absolute seconds (0.0–20.1, 20.1–49.9, …) | Sections defined **by the beats they span** (B01–B03, B03–B06, …), so music moves with picture |
| 3 | Mix length hard-coded to 152.0 s | Derived from the clock with the same formula |
| 4 | Export and QC scripts asserted 4,560 frames / 152 s | Both read the expected count from `beat_sheet.json`; export refuses to run if the render's frame count disagrees |
| 5 | Beat-sheet builder hard-coded the total | Derived, and written to `metadata.duration_frames` as the single figure every validator uses |
| 6 | B02 caption used a double-quoted string, which the caption parser (single quotes only) could mis-read | Switched to a single-quoted string with a typographic apostrophe; B02 now parses to its three intended cues |
| 7 | `render_4k.py` could leave stale narration MP3s in the public dir | Sync clears `beat-B*.mp3` before copying |

The same formula now appears in the composition, `build_beat_sheet.py` and `gen_audio.py`, and all
three agreed on **4,914 frames** before a single frame was rendered.

---

## Pipeline, in order

| # | Step | Result |
|---|---|---|
| 1 | Narration (16 beats) | 157.40 s speech · $0.00 |
| 2 | Imagery | 25 PNGs, byte-identical to prior set |
| 3 | Score + sound design + mix | 163.80 s, 11.38 dB separation |
| 4 | Beat sheet | 16 beats · 490 words · 4,914 frames |
| 5 | Captions | 54 cues · max 2 lines · max 45 chars |
| 6 | Cover art | 3 sizes |
| 7 | Composition edit + sync | S00 added; clock imported |
| 8 | Preflight stills | 5 frames read at delivery scale — intro at 1.3 s and 11.5 s, B01 at 18.7 s, tail at 163.3 s — no defects |
| 9 | 4K render | 4,914 frames, concurrency 4, clean exit |
| 10 | Mux + ladder | 4 cuts, all encoding gates pass |
| 11 | Storyboard + QC frames | 48 frames, 16 strips, contact sheet |
| 12 | Visual QC on the master | all 16 beats read from `_qc/contact_sheet.png` — no defects |
| 13 | Automated QC | `scripts/final_qc.py` |

---

## Visual QC

Performed by reading frames, never by the MP4 probe alone:

- **Preflight**, before committing to the render: the intro at 1.3 s (greeting only) and 11.5 s
  (greeting, summary and full six-stage preview); B01 at 18.7 s to confirm the counter hook now sits
  at beat 02 with the chrome reading 02 / 16; the closing tail.
- **Final**, from the delivered master: one frame per beat at 62% of its span (`_qc/final/`), 48
  storyboard frames, and a 16-up contact sheet (`_qc/contact_sheet.png`).

Observations on the intro frame: greeting, summary, six rows and spine all inside the safe area;
caption band clear; source line legible. One stylistic note left as-is: the headline card reads
"Hi, I'm" while the narration and captions say "I am" — a headline contraction over the spoken form,
not an inconsistency in the words heard or captioned.

**Defects found this build: 0.** The layout fixes from the original build (difference-image contrast,
zoom crops, dark candidate sheet, canvas fill, dome geometry, light-curve shape, mobile type sizes)
were all present in the surviving source and carried through.

---

## Audio QC

| Measure | Value |
|---|---|
| Mix length | 163.80 s — matches the film |
| Speech RMS | −17.73 dBFS |
| Bed RMS (score + effects, where no speech) | −29.11 dBFS |
| Separation | **11.38 dB** — narration clearly dominant, bed audible |
| Peak | −1.04 dBFS — no clipping |
| Intro audible in the delivered film | first 11.5 s of the 1080×1920 master decode at −21.48 dBFS RMS |

---

## Deviations from house doctrine, logged

| # | Doctrine | Deviation | Why |
|---|---|---|---|
| 1 | Brief: "the first 3–5 seconds must open on the scientific problem; do not spend the opening on the presenter" | The film now opens on the presenter introduction; the counter hook lands at 0:11.8 | Explicit later request from the presenter. Cost and mitigations recorded in `PEDAGOGY.md` §0 and `script.md` — the summary states the stake within the first 8 s, and the frame previews the pipeline rather than sitting as a name card |
| 2 | `CLAUDE.md` rule 4 — render Remotion only via `remotion_scenes.py` | Rendered the full composition via the project's own `scripts/render_4k.py` | `remotion_scenes.py` fills per-beat slots; this is a single full-length composition, matching the sibling quantum-materials cut in this folder. Remotion is never invoked by hand |
| 3 | Gate P — pedagogy sign-off before audio | `PEDAGOGY.md` is an audit of the finished cut | Stated rather than backdated. Fact-checking preceded narration; the pedagogy document does not claim to have been a pre-audio gate |

---

## Known limitations

1. The scientific hook arrives at 0:11.8 rather than 0:00 (deliberate; see deviation 1).
2. Precision vs recall is shown but not defined (B11).
3. "Five sigma" is used but not explained (B05).
4. B07 → B08 is the fastest conceptual jump in the film.
5. A fast viewer may over-generalise ALeRCE's architecture to all brokers.

None produces a false belief; each is incompleteness rather than error.

---

## Automated QC

`python scripts/final_qc.py` — **25/25 passing.**

```
ENCODING   4 cuts: 2160x3840 / 1080x1920 / 720x1280 / 540x960, all 30/1, 4914 frames, h264/aac
           163.80s — under the 2:59 ceiling, inside the 2:20–2:50 band
INTRO      first beat is B00 at frame 0
           narration opens "Hi, I am Dhrumil Shah, and this video is about …"
TIMING     54 cues; first cue "Hi, I am Dhrumil Shah," at 0:00; none reversed or overlapping
           last cue ends 162.20s, inside the 163.80s film
CAPTION    max 2 lines per cue; max 45 characters per line; .vtt present
SAFE-AREA  0 text-bright pixels in the platform UI reserves across 16 frames from the master
AUDIO      11.38 dB separation; peak -1.04 dBFS; bed -29.11 dBFS; mix length matches film
INVENTORY  35/35 deliverables; 16 beat WAVs; 16 beat MP3s; 48 storyboard frames
```

---

## Not published

No publishing machinery exists in this project and none was used. The masters stay in `output/`.
