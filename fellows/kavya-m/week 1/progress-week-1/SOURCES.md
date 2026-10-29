# SOURCES — Brutalist Progress — Week 1 (Kavya)

## Primary source

This reel is self-sourced: every claim traces to this session's own build
log and the Brutalist repository's own files, not an external citation.

| Claim | File / line |
|---|---|
| UnicodeDecodeError | `runtime/scripts/pronunciation.py:23` |
| WinError 2 on bare `npx` | `runtime/scripts/remotion_scenes.py` (`NPX = shutil.which("npx") or "npx"`) |
| `node_modules/` never installed | `runtime/remotion/package.json` + `node_modules/` (installed this session) |
| ffmpeg drive-letter colon | `runtime/scripts/compile.py` (`ffescape_path()` helper) |
| GATE V timecode exclusion | `runtime/qc/final_frame_check.py` (`TIMECODE_EXCLUDE` constant) |
| ReqBars chart-scale mismatch | `runtime/remotion/src/RequireReport.tsx` (0–100% `value` contract) |

## Generative media

None. Zero generative image/video model calls — every beat is a Remotion
scene composed from authored props. No pantry stills, no archive footage.

## Seeds (reproducibility)

- B01 `BrutalistHesitantWriter` — `seed: "kavya-week1-progress-4102"`. Same
  seed → identical hesitate/backspace/retype animation on re-render.

## Brutalist toolkit version

- Repo HEAD at build time: `b21f6253a336098f3f55847a9525ae6868ccbdb7`
  (2026-10-10), branch `main` as checked out on this machine.
- This reel was built under the same session as, and directly reuses the
  factual content of, `youtube/brutalist/claude-liam-brutalist-week1-progress/`
  — see that reel's own `beat_sheet.json` metadata note for the original
  bug-by-bug trace.
