# BUILD-LOG — p-value-vertical

Full-length 9:16 companion (`./art vertical`), review cut
`p-value-vertical-slate.mp4` (63.7 s), built 2026-10-15. Same narration, audio
(mp3s byte-identical to 16:9) and on-screen text as the landscape reel. No
toolkit files edited; changes live in this folder (`beat_sheet.json`,
`scenes.py`, `mp3/timings.json`). Not committed.

## Portrait decisions

| Beat | Change | Why |
|---|---|---|
| B00, B10 | `ClaudeComposerAsk916`, `largeText: true`, `runningText: ""`, `modelLabel: "Claude"` | carried over from knowledge-cutoff |
| B01, B03, B04, B06 | native portrait Manim restacks in `scenes.py`; same text, numbers and sequence; ink only; labels ≥ size 32 | Manim beats need native portrait layouts |
| B02, B05, B07–B09 | `FormBCard916`, `icon: "BOX"` on every item, subs ≤ 26 chars | FormBCard916 crashes without icons |
| B11 | Manim `B11_OutroCard` replaces `OutroSeries` (no `OutroSeries916`); "@HumanitariansAI" / "What Does a P-Value Actually Mean?", ink underline | same text as the landscape outro |
| B06 | ≈ glyph alone scaled to 58% (`_approx()`); digits full size | GATE T §8.1 false positive, below |
| — | `mp3/timings.json` restored from the 16:9 file | `shorts.py` doesn't copy it; a `--only B06` audio run then wrote a B06-only file |

## Gate history (fixed in scene source, no `--lenient`)

1. GATE B (strict): B06 two-line title top at y 3.62, then 3.44 (> 3.4) →
   size 38 at y 2.75; cards lowered.
2. GATE T §8.1: B04 and B06 "43 px < 72 px". Measured blobs: stacked pairs
   151 × 43 px — the two strokes of MathTex "≈", not text. The checker's
   fragment cutoff at portrait scale is 27.6 px (its own comment says ≈
   strokes should fall under it). B06 fixed by scaling the ≈ glyph alone to
   58% (~25 px strokes) and closing the gap; B04 the same (below).
3. Clean-clip GATE V: B06 underfill at 50% after the narration retime → both
   card outlines from the start, contents on their sentences, p-value
   underlines on the spoken words (same as 16:9).

## GATE V — how it was run

`./art run` (review cut) fails GATE V on all 24 frames with `edge-bleed`
(top/bottom): the review burn-ins extend past masks sized for 16:9. Kept as
`_qc/REPORT-review-cut-burnins.md`. Same false positive as knowledge-cutoff and
claude-liam-context-window verticals; every BLOCKER is edge-bleed.

Strict `final_frame_check.py` on a scratch concat of `clips/*.mp4` (no
burn-ins; scratch file deleted): **24 frames, 0 BLOCKER / 0 MAJOR** (`_qc/REPORT.md`), after the B03/B04
re-render below (it was 0 BLOCKER / 1 MAJOR, B03 underfill, before).

## Resolved on review — B03 and B04 re-rendered (vertical only)

- **B04:** the ≈ glyph uses the same `_approx()` fix as B06; the beat is
  re-spaced (coin rows y 1.72 → 1.55, caption 0.45 → 0.3, "≈ 0.011" box
  −1.7 → −1.62, "About 1%" −2.53 → −2.47) so "ILLUSTRATIVE" clears the coin
  rows and the box clears "About 1%". Timing unchanged.
- **B03:** labels come in earlier, same text and layout: curve, title and
  meta together (0–0.9 s); marker + "Your data" by 1.4 s ("data" 1.96 s);
  tail + "At least this extreme" on "this extreme" (2.1–2.7 s); "Shaded share
  = p-value" on "or more" (2.7–3.1 s), ~1.5 s before "That share is the
  p-value" (4.60 s). 50% frame fill 50% → 86%.
- GATE B (strict): both clean.

## Advisory

- GATE A: B01 "no shapes recorded — scene may be text-only" — by design.
- `[art] WARNING: build stamp failed` — known toolkit stamp bug, non-blocking.
- run.sh stops at the review-cut GATE V failure, so its post-steps (ToDo.md,
  copying the cut into `mp4/`) did not run; the review cut is at the folder root.

## Review cut status (2026-10-15)

`p-value-vertical-slate.mp4` — 63.7 s.
- GATE T: PASS, 0 FAIL.
- GATE V on clean clips (strict): 24 frames, 0 BLOCKER / 0 MAJOR. GATE V on
  the review cut: 24 edge-bleed BLOCKERs, all from the burn-ins (see above).
- B03, B04 and B06 frames read by eye at 15/50/85% in the compiled cut.
- Not exported: no `./art final` run. Not committed.

## Final master (2026-10-15)

PEDAGOGY.md verdict PASS (Gomathy, after reviewing both cuts). Clean master built with `./art final` (`--height 3840`):
`brutalist.art/renders/p-value-vertical.mp4` — 2160×3840, 24 fps, H.264 + AAC, 63.71 s, + `.verified.json` (status ready).

- GATE T (art final pre-flight): PASS, 0 FAIL.
- GATE V: `./art final` does not run it, so `final_frame_check.py` (strict, no
  `--lenient`) was run on the clean master: 24 frames, 0 BLOCKER / 0 MAJOR.
- Frames read by eye (one per beat at 85%): no burn-ins, no clipping or collisions.
- `[art] WARNING: build stamp failed` — known toolkit stamp bug, non-blocking.
- No toolkit files edited. Not committed.
