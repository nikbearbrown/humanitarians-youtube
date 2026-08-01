# STATUS — ai-vs-the-data-deluge
## AI vs. the Data Deluge

**State:** COMPLETE — fully rebuilt and rendered 2026-08-01. All 19 beats have measured Kokoro
narration, every Manim/Remotion/archive slot is filled, and the 4K clean master is on disk:
`claude-for-astronomy_OmMali_01_08_2026.mp4` (3840x2160, 117.52s, ffprobe-confirmed). The prior
27_07_2026 master (18-beat cut) has been superseded and deleted.

---

## Build summary

| field | value |
|---|---|
| Slug | ai-vs-the-data-deluge |
| Beats | 19 (B01–B19) — added 2026-08-01: a presenter self-introduction beat inserted as B02, shifting every former B02–B18 beat up by one |
| Voice | Kokoro `af_heart` |
| Aspect ratio | 16:9 |
| Measured narration total | 117.52s (~1:58) summed from `actual_duration_s` across all 19 beats |
| Full render runtime | 117.52s / 3840x2160 — ffprobe-confirmed on the final master |
| Slots filled | 19/19 — no open/slate slots |
| Shot-type mix | Manim: 8 beats (1, 4, 5, 9, 10, 11, 12, 13) · Remotion: 8 beats (2, 3, 6, 7, 8, 15, 17, 19) · Real archive imagery/video: 3 beats (14, 16, 18) · Higgsfield: 0 beats |
| Gate P (narration/content review) | PASS — content was human-approved upstream in `SHOTLIST.md`/`FACTCHECK.md` before audio generation; see `PEDAGOGY.md` |
| Money spend | **$0** — Kokoro narration (free/local) and free CC-licensed archive downloads only; no paid generation anywhere in this build |

---

## Real-archive assets used (credited, CC-licensed)

| Beat | Asset | Credit |
|---|---|---|
| B14 | Kepler-90 8-planet system artist concept (NASA image PIA22193) | NASA/Ames Research Center/Wendy Stenzel |
| B16 | Vera C. Rubin Observatory press photo | RubinObs/NOIRLab/SLAC/NSF/DOE/AURA |
| B18 | "Zooming into NSF–DOE Rubin's Ocean of Stars" (NOIRLab, HD 1080p) | Credit: NSF–DOE Vera C. Rubin Observatory/NOIRLab/SLAC/AURA. Acknowledgements: unWISE/NASA/JPL-Caltech/D. Lang/A. Meisner |

Full detail and source links: `FACTCHECK.md`.

---

## Series context

Episode 01 of a planned weekly "AI in Astronomy & Space Science" series (14 further topic ideas
scoped, not yet built): exoplanet hunting deep-dive, gravitational wave detection, galaxy
classification, fast radio bursts, Mars rover autonomy, cosmological simulation, asteroid
tracking, image denoising, supernova classification, generative spacecraft design, solar storm
prediction, SETI signal detection, stellar spectra classification, satellite collision avoidance.

---

## 2026-08-01 rebuild notes

- Inserted new beat 2 (presenter self-introduction / executive summary, Remotion SlateCard,
  eyebrow "WELCOME") right after the B01 cold open; every former B02–B18 beat renumbered up by
  one (old 2→3, 3→4, … 18→19).
- Regenerated Kokoro `af_heart` narration for all 19 beats from scratch (no per-beat mp3s existed
  in this repo copy prior to this rebuild); `mp3/timings.json` and `beat_sheet.json`
  `actual_duration_s`/`t_start` reflect the freshly measured durations.
- Renumbered the Manim `scenes.py` DUR-key lookups and scene-class docstrings for every GRAPHIC
  beat whose beat_id shifted (old B03/B04/B08/B09/B10/B11/B12 → new B04/B05/B09/B10/B11/B12/B13);
  the visual construct() code for each scene is unchanged.
- Renamed the three real-archive media files to their new beat numbers (old B13→B14, B15→B16,
  B17→B18) and re-downloaded the CC BY 4.0 NOIRLab "Ocean of Stars" video for B18 (the source mp4
  was missing from this repo copy — only its `.source.txt` sidecar was present; re-downloaded from
  the same URL on file, audio stripped per house convention, 32,103,981 bytes matching the
  previously-verified download).
- Rendered all 8 Manim scenes and all 8 Remotion SlateCard beats fresh, then compiled the full
  19-beat 4K master with `compile.py` (19/19 slots filled, zero slates).
- `compile.py`'s motion-pantry lint flagged `hold` at 47% of beats (over the ~40% cap) — this is a
  pre-existing characteristic of the CARD-heavy shot mix (SlateCard beats default to `hold`), not
  something changed by this rebuild; left as a warning, not treated as a blocker.

## Known gaps in this checked-in copy

- No `qc-sheet.png` contact sheet was generated for this master (only produced for `--review`
  cuts).
- `PROMPTS.md` documents Higgsfield stills that were drafted, approved, then never actually used
  (see that file) — kept for the audit trail, not because a slot is open.
- Manim's own render cache (`media/videos/`, `media/images/`, `media/texts/`) is regenerable
  scratch space, not a deliverable; `manim/B*.mp4` and `media/B*.mp4` are the files the compiler
  actually reads.
