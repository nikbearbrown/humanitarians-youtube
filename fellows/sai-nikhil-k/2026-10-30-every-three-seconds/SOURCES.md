# SOURCES — Every Three Seconds

## Provenance

Sai asked (2026-11-09) for two backlog videos, one feature each, from his repo
<https://github.com/nikhil-kunapareddy/gavia>: October 30 = "Audio detection
model of the loon call". He chose the angle and title, said nothing is to be
left out, and gave a hands-off window for the app screenshots.

## Sources

| What | Where | Used for |
|---|---|---|
| Gavia v0.4.0 release + source | github.com/nikhil-kunapareddy/gavia @ `7909a76` (tag v0.4.0); archived: `research/gavia_CHANGELOG_v0.4.0.md`, `research/gavia_README_v0.4.0.md`, `research/gavia_ROADMAP_v0.4.0.md`, `research/gavia_looncall_v1_card.json`, `research/gavia_commit_e5ac987.txt` | the feature, formats, 3 s windows, 48 kHz, threshold 0.5, licence |
| Gavia v0.5.0 (built + run) | tag v0.5.0, `5dd8471`, scratch clone; `/Applications/Gavia.app` 0.5.0 | evidence runs; screenshots (audio code unchanged since 0.4.0) |
| loonet looncall v1 | `~/Documents/loonet` (local; commit `76a6c41`); archived: `research/loonet_looncall_v1_README.md`, `research/loonet_looncall_v1_metrics.json` | the formula, training data, the "easy by construction" val set, the drone test |
| loonet looncall val split | `data/annotated/looncall_v1/val.csv` (65 windows, 28 loon) + `data/looncall_raw/` (not committed) | B05 re-run |
| Releases | `evidence/releases.out` (`gh api …/releases`) | dates only (0.4.0 published 2026-10-30) |

## Week-scope commits (Gavia, after the 10-23 reel)

| Commit | Date | Author | What |
|---|---|---|---|
| `e5ac987` | 2026-10-30 | Sai Nikhil Kunapareddy | Listen for loon calls in recordings |
| `1b2ef35` | 2026-10-30 | Sai Nikhil Kunapareddy | Fix cargo audit: bump rustls, accept three unreachable zip advisories |
| `7909a76` | 2026-10-30 | Sai Nikhil Kunapareddy | Release 0.4.0 |

loonet the same day: `76a6c41` "looncall: detect loon calls in audio; v1 on
BirdNET embeddings" (Sai). No other authors in the window.

## Images

| Beat | File | What | Credit / licence |
|---|---|---|---|
| B01 | `app_audio_clean.png` | result: 2 calls, 4 of 8 stretches | Gavia 0.5.0 screenshot · recording iNaturalist (Mount Desert, ME), CC0 |
| B01 | `app_audio_home.png` | "Is that a loon?" | Gavia 0.5.0 screenshot |
| B01 | `app_audio_loaded.png` | recording loaded, before checking | Gavia 0.5.0 screenshot · same recording |
| B06 | `app_audio_clean_crop.png` | the clean result, cropped to the card | as above |
| B06 | `app_audio_drone_crop.png` | the same recording + drone noise at 5 dB: 2 of 8 | as above + Sai's drone footage noise (loonet) |

Every file has a sidecar `images/src/<slug>.json` (capture method, size, sha256,
the recording's observation and licence).

## Honesty log

- **The screenshots are 0.5.0**, the release after this reel's week; the audio
  path is byte-identical to 0.4.0 (no diff under `src/calls/`, `CallResult`,
  `AudioUploader`, `AudioPage`). Captions say 0.5.0.
- **The loonet README's drone-noise table was re-measured, not quoted**: the
  notebook cell (commit `76a6c41`, cell 6) was repeated step for step in
  `drone_mix.py` and then scored by Gavia's Rust detector. Same numbers.
- **The clean-val 1.000 is shown only to be discounted**, which is how loonet's
  own README presents it.
- **Prose that disagrees with the code:** `ROADMAP.md` still calls item 3 "Not
  started" at v0.4.0 and v0.5.0. Logged in PEDAGOGY for Sai; not in the video.
- **One recording in B06** is a single demonstration; B05's table is the
  systematic measurement.
