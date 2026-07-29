# The Artificial Intelligence Crossroads: Build or Buy? — Klarna Case

A ~3:06 explainer video (HAI / Pragmatist register) built for the
`claude-for-design` collection in the `humanitarians-youtube` repo,
replacing that topic's original fictional draft with a real, primary-sourced
case: Klarna's AI customer-service deployment (Feb 2024 launch → May 2025
partial reversal → Nov 2025 hybrid recovery), read through the peer-reviewed
Productivity J-Curve (Brynjolfsson, Rock & Syverson) — and closing on a
direct answer to the video's own title question.

## Files

- **`the-artificial-intelligence-crossroads-klarna.mp4`** — the final cut.
  Every beat holds on its finished visual for a full second before a hard
  cut to the next — no crossfade — giving the viewer time to process each
  section before moving on.
- **`beat_sheet.json`** — the full beat-by-beat script: narration, visual
  structure, and every Remotion component/prop used to build the video.
- **`PEDAGOGY.md`** — thesis, persona/register rationale, evidence table,
  and the GATE P sign-off.
- **`FACTCHECK.md`** — the full beat-by-beat claim audit (verdict per claim,
  source, and every correction applied).
- **`QC-REPORT.md`** — visual QC log, including the pacing revision that
  produced the final 1.0s-hold, no-crossfade cut.

## Note on the pacing pass

The 1.0s hold before every cut is **not** part of the Brutalist toolkit's
standard `compile.py` pipeline (it only supports hard-cut concatenation,
with no transition or pause mechanism at all). It was built as a separate
`ffmpeg` pass over `compile.py`'s own per-beat conformed clips — see
`QC-REPORT.md` for the full before/after history. If the beat sheet is
edited and recompiled, this pass needs to be re-run manually.

Built with the [Brutalist](https://github.com/nikbearbrown/brutalist.art)
free, local video toolkit (Kokoro TTS + Remotion) — no paid APIs, no keys.
