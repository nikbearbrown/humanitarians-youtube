# BUILD-LOG — The Role That Lied

## Output

| | |
|---|---|
| Master 16:9 | `medhavy-role-matching.mp4` · 3840x2160 · 24 fps · 100.708 s |
| Master 9:16 | `medhavy-role-matching-916.mp4` · 1216x2160 · 24 fps · 100.708 s |
| Audio | AAC 48 kHz stereo, Kokoro `am_onyx`, per-beat timeline |
| Beats | 8, all filled from `media/` |

## Architecture

Toolkit read-only. Visuals rendered out of tree by `scenes/render_scenes.py`
(Pillow) into `media/<beat>.mp4`. Core — layout, fonts, `fit()`, elastic
allocation, assembly — reused verbatim from `medhavy-canvas-sync`.

**Single stacked column throughout.** Every beat is full-width rows with vertical
arrows; nothing is placed side by side and nothing is positioned by a fraction of
the frame width. That is why the 9:16 cut needed no portrait variant: the same
scene functions render at 2160x3840 and conform to 1216x2160.

The 9:16 cut is its own reel directory with its own beat sheet declaring
`aspect_ratio: 9:16` and `canvas: 2160x3840`. Pointing `./art final` at a sheet
that still declared 16:9 made it conform the portrait beats back into a landscape
frame, which GATE V correctly rejected.

## Duration drift

Script estimate 101 s from 337 words at 3.35 words/sec. Measured 100.5 s of
narration, 100.7 s conformed. Closest of the series. No holds padded.

## Defects found in QC and fixed

1. **B02's closing caption never rendered.** The state list was
   `[draw(0), draw(1), draw(1)]` — the second state was called twice and the third
   never reached, so the two lines explaining the shortcut did not exist in the
   output. No gate caught it; the beat was the right length and looked finished.
   Found by reading the contact sheet against the script.
2. **B01 left a dead band.** A three-row stack with only two rows used. Rebuilt as
   two taller rows with the arrow in the gap, and the URN scaled up.
3. **B02 and B04 underfilled the frame.** Both widened and their type raised.
4. **`footer()` clipped every caption at 9:16.** It drew at a constant
   `L.caption` with no width check. At 16:9 the captions happened to fit; at 9:16
   the frame is narrower and every footer was cut mid-word. Fixed in the shared
   core and propagated to all six reels in the series.

Defect 4 is the one with reach — it had been wrong in every reel since the first
and only surfaced when the canvas changed.

## Lints — reported, not silenced

- `SKIN LINT: NO RENDERABLE BEATS` — expected for this architecture; same run
  reports `8/8 filled`.
- `'hard-snap' carries 5/8 beats (62%) — over the ~40% cap` — labels come from the
  script's own shot list and were left as written.

## Gates

GATE F satisfied. GATE V clean on both cuts: 16 frames, 0 blockers, 0 majors on
the 9:16 pass. `PEDAGOGY.md` carries `VERDICT: PENDING` and is not self-signed.

## Not done

No captions or word clock (`faster-whisper` not installed).
