# STATUS — exoplanet-hunting

## Exoplanet Hunting: Teaching AI to Show Its Work

**State: BUILT — 4K master rendered.** Kokoro `af_heart` narration generated for all 20 beats,
all Manim/Remotion visual beats rendered, and the full cut compiled to a 4K
(3840x2160) master: `claude-for-astronomy_OmMali_01_08_2026.mp4` (149.97s / ~2:30).

Rebuilt 2026-08-01: a new presenter self-introduction/executive-summary beat was inserted as **B02**
(right after the B01 cold open), pushing every former B02-B19 beat up by one to B03-B20. This
mirrors the identical insertion already made to `ai-vs-the-data-deluge` (Ep.01) for series
consistency: same "WELCOME" eyebrow, same "Hi, I'm Om Mali." headline convention on the Remotion
`SlateCard`. No other beat's narration, visuals, or claims changed — only beat numbers and file
names shifted. New B02's narration:

> "Hi, I'm Om Mali. This video is about how NASA built an AI system that explains exactly why it
> thinks a signal is a real planet, instead of just giving a yes or no answer."

---

## Build summary

| field | value |
|---|---|
| Slug | exoplanet-hunting |
| Beats | 20 (B01-B20) |
| Voice | Kokoro `af_heart` (matches Ep.01, for series consistency) |
| Aspect ratio | 16:9 |
| Measured narration total | 149.97s (~2:30), from actual Kokoro audio |
| Slots filled | 20/20 |
| Shot-type mix | Manim: 11 beats · Remotion: 9 beats · Real archive imagery/video: 0 beats (by design, see `FACTCHECK.md`) · Higgsfield: 0 beats (none drafted, see `PROMPTS.md`) |
| Gate P (narration/content review) | cleared |
| Money spend | $0 — no paid generation used |
| Final master | `claude-for-astronomy_OmMali_01_08_2026.mp4`, 3840x2160, 149.97s |

---

## What changed in the 2026-08-01 beat-2 insertion

1. Renumbered `beat_sheet.json` beat_ids B02-B19 -> B03-B20; inserted new B02; recomputed every
   `t_start` from measured `actual_duration_s` values (new total 149.97s, up from the prior
   19-beat cut).
2. Renamed every per-beat asset file to match the shift, working backwards (highest number
   first) to avoid collisions: `mp3/beat-B02..19.mp3` -> `beat-B03..20.mp3`; `manim/B03,04,05,06,
   09,10,11,12,13,14.mp4` -> `B04,05,06,07,10,11,12,13,14,15.mp4`; `media/B02,07,08,15,16,17,18,
   19.mp4` -> `B03,08,09,16,17,18,19,20.mp4`; `clips/B02..19.mp4` -> `B03..20.mp4`.
3. Updated `scenes.py`'s DUR-key lookups (e.g. `DUR["B03"]` -> `DUR["B04"]` inside the class that
   used to be keyed to old B03) to match the new beat_ids; Scene class names and all visual
   `construct()` logic were left untouched, matching the approach already used for Ep.01.
4. Generated Kokoro `af_heart` audio for new B02 only (11.95s measured) — no other beat's audio
   was regenerated.
5. Rendered new B02's Remotion `SlateCard` (`media/B02.mp4`, WELCOME eyebrow, "Hi, I'm Om Mali."
   headline).
6. Recompiled the full 20-beat film at 4K via `compile.py`, which also re-stamped every beat's
   `build` record and `metadata.build` (20/20 filled).
7. Updated `SHOTLIST.md`'s beat table and `FACTCHECK.md`'s Beat(s) column references; added a
   `FACTCHECK.md` "Resolved decisions" note documenting new B02 as a presenter self-introduction,
   not a factual claim requiring a source.
8. Updated the top-level `claude-for-astronomy/README.md` inventory row for this project.

---

## Series context

Episode 02 of the planned weekly "AI in Astronomy & Space Science" series (see
`weekly_stem_videos/ideas.md`, Astronomy section). Episode 01, `ai-vs-the-data-deluge`, covered
AstroNet's two-view CNN and the Kepler-90i discovery. This episode intentionally covers different
ground: the three false-positive types Ep.01 never named, and NASA's ExoMiner (2021) — a
separate-diagnostic-branch classifier, its 301-planet batch validation, and its 2026 TESS
extension (ExoMiner++). Both episodes now open with a matching presenter self-introduction beat
(B02) for series consistency. 13 further topic ideas from the same backlog remain unbuilt:
gravitational wave detection, galaxy classification, fast radio bursts, Mars rover autonomy,
cosmological simulation, asteroid tracking, image denoising, supernova classification, generative
spacecraft design, solar storm prediction, SETI signal detection, stellar spectra classification,
satellite collision avoidance.
