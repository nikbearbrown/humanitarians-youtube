# FACTCHECK — Brutalist Progress — Week 1 (Kavya)

Every claim mapped to its evidence, with an honest status on each.

## What kind of reel this is

A real, independently verifiable recap of this session's own work setting up
and debugging the Brutalist toolkit on this machine — not an illustrative or
constructed example. Every bug named on screen is real and was fixed at an
actual file/line this session.

## B00 — Cold open

- **"2 missing dependencies, found and installed"** — real: Kokoro voice
  model + `runtime/remotion/node_modules` (never installed by setup; `npm
  install` run this session).
- **"6 real bugs, fixed at the root"** — see B04/B05 below for the full list.
- **"2 final videos shipped, zero blocking defects"** — refers to the
  `claude-liam-schema-scout` reel (10 beats, 16:9 + 9:16), the first reel
  built on this pipeline this session.

## B01 — BLUF

- No factual claim beyond the thesis restated in B00/B06.

## B02 — Pipeline framework

- **Four stages (beat sheet → Kokoro audio → Remotion render/ffmpeg compile
  → QC gates)** — this is a description of the actual pipeline used to build
  every reel in this session, not a simplification for effect.

## B03 — What got built

- **"Toolkit setup"** — real: Kokoro model, ffmpeg, Node deps were not
  pre-installed; this session installed/configured all three.
- **"First reel authored — Schema Scout, 10 beats"** — real, see
  `youtube/claude-liam-schema-scout/`.
- **"Six pipeline bugs fixed"** — see B04/B05.
- **"Two formats shipped, 16:9 and 9:16"** — real, confirmed by the rendered
  mp4s in that reel's folder.

## B04 — The breaks, part 1

- **UnicodeDecodeError in `pronunciation.py:23`** — real. Windows defaults to
  cp1252; fixed by adding `encoding="utf-8"` to the `read_text()` call.
- **WinError 2 on bare `"npx"`** — real. Windows needs `npx.cmd`, not `npx`;
  fixed in `remotion_scenes.py` via `shutil.which("npx") or "npx"`.
- **`node_modules/` never installed** — real; `runtime/remotion/` had no
  dependencies installed until `npm install` was run this session.

## B05 — The breaks, part 2

- **ffmpeg drive-letter colon breaking the filtergraph** — real, in
  `compile.py`'s `drawtext=fontfile=` argument; fixed via
  `os.path.relpath()` to avoid a bare Windows drive letter colon in the
  filter string.
- **GATE V (`final_frame_check.py`) never excluding the review timecode from
  its own edge-bleed check** — real; `BURN_IN_EXCLUDE` only covered the
  bottom-left per-beat label, not the top-right global timecode, causing
  every beat to false-positive. Fixed by adding a second `TIMECODE_EXCLUDE`
  zone.
- **A chart (ReqBars) fed a 123x-style multiplier into a 0–100%-scale
  component** — real; overflowed the bar past the frame on first render.
  Fixed by reframing the chart data as an actual percentage breakdown.

## B06 — Verdict

- Restates B02/B03's claims; no new facts introduced.

## B07 — Handoff

- No factual claim; a prompt for the viewer to run on their own pipeline.

## B08 — Outro

- No factual claim; "Built by — Kavya Mehta" credit card.

## Corrections & caveats applied during this build

- This reel reuses the real, already-fixed-at-the-root bug list from the
  original `claude-liam-brutalist-week1-progress` build earlier this
  session — the bugs and fixes are identical and real; only the on-screen
  persona, greeting, folder chip, and outro were changed to remove the
  claude-liam / Nik Bear Brown branding and credit Kavya Mehta by name,
  per explicit direction.
- GATE T (`type_check.py`) flagged one advisory finding on B03 (an "8px text
  run" below the legibility floor). Two extracted frames (mid-clip and
  near end-of-clip) were visually inspected and show every text element —
  all four card titles and sub-labels — fully legible at normal size. The
  flagged element is almost certainly the narrow colored accent bar on the
  left edge of each card being misread as a text run by the checker, the
  same class of false positive previously documented for `ReqBars`' bar
  fill (see BUILD-LOG.md). Not treated as a blocking defect; logged here
  rather than silently dismissed.
