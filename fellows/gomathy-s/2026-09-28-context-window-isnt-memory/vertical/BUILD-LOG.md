# BUILD-LOG — claude-liam-context-window-vertical

Full-length 9:16 companion (`./art vertical`), clean master built 2026-10-07 with
`./art final <reel>/vertical --height 3840`:

- Output: `brutalist.art/renders/claude-liam-context-window-vertical.mp4`
  (2160×3840, 24 fps, H.264 + AAC, 63.25 s) + `.verified.json`.
- GATE T: PASS. GATE V on the clean master: 0 BLOCKER / 0 MAJOR.
- No toolkit files were edited. Every change below lives in this folder
  (`beat_sheet.json`, `scenes.py`).

## GATE V and `--lenient` — not used

`./art run` (review cut) fails GATE V on all 24 sampled frames with `edge-bleed`.
Cause: `runtime/qc/final_frame_check.py` masks the review burn-ins (timecode
top-right, beat label bottom-left) with boxes sized for 16:9; in a portrait
frame both overlays extend past the masks and read as content. The clean master
carries no burn-ins, so this does not occur there.

The first clean-master run did surface two real defects (B05 title above the
top title-safe line; B09 underfill 19%). Because those were not overlay false
positives, `--lenient` was **not** used; both were fixed (below) and the final
check passed outright.

## Portrait-only decisions (approved)

| Beat | Change | Why |
|---|---|---|
| B00, B10 | `largeText: true` on `ClaudeComposerAsk916` | phone readability (prop-only) |
| B01 | portrait Manim `B01_HesitantWriter` replaces `BrutalistHesitantWriter916`; same text and sequence, ink only | one line can't reach GATE T's 72 px portrait floor; a second line adds the writer's fixed 400 ms newline pause, so "a fixed budget." never finishes in the 3.2 s beat |
| B04 | portrait Manim restack of `B04_TokenSplit` | Manim beats need native portrait layouts |
| B05 | label "Non-English text" → "Text in other languages"; subs shortened to one line each (≤26 chars) | the hyphen read as a 41 px sub-floor text run (FormBCard916 renders at 4320×7680 under the hardcoded `--scale=2`); two-line subs pushed the title past the top title-safe edge |
| B06 | portrait Manim `B06_CeilingClimb` replaces `AttritionChain` (no `AttritionChain916`); same data and labels, ILLUSTRATIVE on screen, ink only, all labels ≥ size 32 | no portrait composition exists; GATE T portrait floor + title-safe box |
| B09 | `qc.sparse_by_design` with reason | `ClaudeVerdictArtifact916` hardcodes a compact card; no size props |
| B10 | `runningText: ""` (status line dropped) | terracotta status text at `largeText` size fails GATE T §8.3 (2.74:1); its colour isn't a prop |
| B11 | portrait Manim `B11_OutroCard` replaces `OutroSeries` (no `OutroSeries916`; `LogoOutro916` has no title slot); text "@HumanitariansAI" / "The Context Window Isn't Memory.", ink underline | same text as the landscape outro |
| B02, B03, B05, B07, B08 | `icon: "BOX"` on every FormBCard916 item | FormBCard916 lacks the landscape's missing-icon guard and crashed loading `undefined.svg` |

## Advisory left open

- TYPECHECK §8.10: B09 narration recites the summary card (1.00) — advisory,
  inherited from the landscape reel, where B09 restates the thesis by design.
- `[art] WARNING: build stamp failed: 'str' object has no attribute 'get'` —
  toolkit stamp bug, non-blocking; the `.verified.json` was still written.
