# STATUS — ai-vs-the-data-deluge
## AI vs. the Data Deluge

**State:** audio present — assembled narration master (`clips/master.m4a`) and full per-beat
build manifests exist; the rendered MP4 (`ai-vs-data-deluge.mp4`) and per-beat mp3/mp4 files were
intentionally not checked into this repo copy (see "Known gaps" below) — repo policy keeps large
distribution media out of Git (`.gitignore`: `*.mp3`, `*.mp4`), matching every other project in
this repository.

---

## Build summary

| field | value |
|---|---|
| Slug | ai-vs-the-data-deluge |
| Beats | 18 (B01–B18) |
| Voice | Kokoro `af_heart` |
| Aspect ratio | 16:9 |
| Measured narration total | ~106.9s (~1:47) summed from `actual_duration_s` across all 18 beats |
| Full render runtime | not independently re-measured here (no `ffprobe` on this machine, and the rendered MP4 isn't part of this repo copy) — narration total plus card holds/transitions will run a little longer than ~1:47 |
| Slots filled | 18/18 — no open/slate slots |
| Shot-type mix | Manim: 8 beats · Remotion: 7 beats · Real archive imagery/video: 3 beats · Higgsfield: 0 beats |
| Gate P (narration/content review) | PASS — content was human-approved upstream in `SHOTLIST.md`/`FACTCHECK.md` before audio generation; see `PEDAGOGY.md` |
| Money spend | **$0** — all 4 originally-approved Higgsfield beats (1, 2, 6, 8) were reassigned to free Manim/Remotion before generation; see `FACTCHECK.md` "Resolved decisions" |

---

## Real-archive assets used (credited, CC-licensed)

| Beat | Asset | Credit |
|---|---|---|
| B13 | Kepler-90 8-planet system artist concept (NASA image PIA22193) | NASA/Ames Research Center/Wendy Stenzel |
| B15 | Vera C. Rubin Observatory press photo | RubinObs/NOIRLab/SLAC/NSF/DOE/AURA |
| B17 | "Zooming into NSF–DOE Rubin's Ocean of Stars" (NOIRLab, HD 1080p) | Credit: NSF–DOE Vera C. Rubin Observatory/NOIRLab/SLAC/AURA. Acknowledgements: unWISE/NASA/JPL-Caltech/D. Lang/A. Meisner |

Full detail and source links: `FACTCHECK.md`.

---

## Series context

Episode 01 of a planned weekly "AI in Astronomy & Space Science" series (14 further topic ideas
scoped, not yet built): exoplanet hunting deep-dive, gravitational wave detection, galaxy
classification, fast radio bursts, Mars rover autonomy, cosmological simulation, asteroid
tracking, image denoising, supernova classification, generative spacecraft design, solar storm
prediction, SETI signal detection, stellar spectra classification, satellite collision avoidance.

---

## Known gaps in this checked-in copy

- No `qc-sheet.png` contact sheet — not regenerated for this repo copy; the original build
  environment produces one but it wasn't part of what was migrated here.
- `PROMPTS.md` documents Higgsfield stills that were drafted, approved, then never actually used
  (see that file) — kept for the audit trail, not because a slot is open.
- The final rendered `ai-vs-data-deluge.mp4`, the per-beat narration `mp3` files, the per-beat
  rendered `clips/B*.mp4`, and the Manim/Remotion scene-render caches were deliberately left out
  of this repo copy — they're large, regenerable from `beat_sheet.json` + `scenes.py`, and every
  other project in this repository keeps the same files out for the same reason (`.gitignore`
  excludes `*.mp3`/`*.mp4` repo-wide). The original full build, including the rendered video,
  still exists at the source production location outside this repo.
