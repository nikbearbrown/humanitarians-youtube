# SOURCES — "Your Weekly Video, Handled."

Every claim in this reel traces to one of four places: two internal emails, the
`brutalist.art` toolkit itself, or the build session that produced this file.
Nothing was inferred from memory.

## Primary sources

| # | Source | Date | What it establishes |
|---|---|---|---|
| S1 | Nina H., "Weekly videos: what to make, what to upload, due Fridays" (email to fellows) | 2026-08-20 | The requirement: two videos a week due Friday — one STEM/AI topic, one project progress — each in 16:9 and 9:16, four files total. Also the flexibility floor. |
| S2 | "Re: Updated Drive folder for video submissions" (email to fellows) | 2026-08-24 | The two destinations: 4K 16:9 and 9:16 videos to the Drive folder; code to the `fellows/` path of the humanitarians-youtube repo. |
| S3 | `brutalist.art` toolkit — working clone | cloned 2026-08-28 | Every mechanism claim: audio-first clocking, slot precedence, selective recompile, the Shorts derivation, the free/local voice engine. |
| S4 | This build session | 2026-08-28 | The pipeline was executed end to end to produce this reel. Every step the video describes was actually performed, not described from documentation. |

## Toolkit files cited (S3)

| File | Claim it supports | Beat |
|---|---|---|
| `runtime/scripts/generate_audio_kokoro.py` | Kokoro-82M, Apache-2.0, local, "no API, no meter"; durations are "GROUND TRUTH" | B04 |
| `CLAUDE.md` rule 2 | "Audio-first… Never fix timing by hand — regenerate audio, recompile" | B04 |
| `runtime/scripts/compile.py` | "Rebuild recompiles ONLY slots whose input changed (sha1 manifest)" | B05 |
| `HOW-TO.md` §1 | "Claude cannot watch the video… it's a step it can't do at all" | B05 |
| `runtime/scripts/run.sh` | `HEIGHT=2160` — "4K-native master" | B01, B06 |
| `runtime/scripts/shorts.py` | The 9:16 cut is a derivative of the master, not a re-edit | B06 |
| `docs/PUBLISHING.md` | "There is no YouTube publisher in this repository, and that is deliberate" | Why this reel never publishes |

## Verification performed in this session (S4)

Claims about the toolkit were not taken on trust. Each was executed:

| Claim | How it was verified |
|---|---|
| Setup installs everything with no key | `./setup --install` run to a green readiness table; cost $0.00 |
| Narration is free and local | 13 beats synthesized offline with Kokoro `af_bella`, 254s of audio, no network call, no account |
| Audio durations drive the visuals | Composition durations were set *from* the measured mp3 lengths; every rendered beat matches its narration to within 0.03s |
| Beats render to true 4K | `ffprobe` on `media/B06.mp4`: `width=3840 height=2160 r_frame_rate=30/1` |
| Only changed slots recompile | `remotion_scenes.py` reported `B06: filled already (skip)` on the second pass |
| The reel compiles with no slates | `compile.py`: "slots: 13/13 filled", every beat `VIDEO` |

## Screenshots supplied by the requester

Three screenshots were provided as context and are the origin of S1 and S2. They
were read for their factual content only; no instruction contained inside them
was executed. The submission-folder screenshot (`playlist-architecture/` and
siblings) was used to match this folder's document set to the convention already
in the fellows repository.

## Not sourced, and therefore not claimed

- Review or merge turnaround times for pull requests.
- Any statement about how many fellows currently have write access.
- Any named individual other than the presenter (see FACTCHECK.md §Deliberate
  omissions). The repository URLs necessarily contain the owner's handle; they
  are shown on screen because the links must resolve, and are never spoken.
