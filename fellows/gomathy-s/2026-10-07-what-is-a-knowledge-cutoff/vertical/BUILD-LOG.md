# BUILD-LOG — knowledge-cutoff-vertical

Full-length 9:16 companion (`./art vertical`), review cut
`knowledge-cutoff-vertical-slate.mp4` (60.5 s), built 2026-10-07.
No toolkit files edited; changes live in this folder (`beat_sheet.json`, `scenes.py`).

## Portrait decisions

| Beat | Change | Why |
|---|---|---|
| B00, B10 | `ClaudeComposerAsk916`, `largeText: true`, `runningText: ""` | phone readability; terracotta status text fails GATE T §8.3 at largeText size (prior reel) |
| B01, B02, B04, B06 | native portrait Manim restacks in `scenes.py`; same text and sequence as 16:9, ink only, labels ≥ size 32 | Manim beats need native portrait layouts |
| B03, B05, B07–B09 | `FormBCard916`, `icon: "BOX"` on every item, subs ≤ 26 chars | FormBCard916 crashes without icons (prior reel) |
| B11 | Manim `B11_OutroCard` replaces `OutroSeries` (no `OutroSeries916`); "@HumanitariansAI" / "What Is a Knowledge Cutoff?", ink underline | same text as the landscape outro |

## Gate history (all fixed in scene source, no `--lenient`)

1. GATE B (strict): B02 two-line title top at y 3.62 (> 3.4) → titles to size 40 at y 2.6; content shifted down (B02 box, B04 band, B06 cards).
2. GATE B: "Training" label sat on the axis line → moved under the box's right edge.
3. GATE B: 7th chip crossed the "cutoff" label mid-move → chips re-laid 4 + 3.
4. B04 marker label at x 1.98 (> 1.95) → max width tightened. B02 "time" label raised off y −2.9.
5. Frame review: B06 ≠ touched both card borders → cards 1.55 → 1.45 tall.

## GATE V — how it was run

`./art run` (review cut) fails GATE V on all 24 sampled frames with
`edge-bleed` (top/bottom) — the review burn-ins (timecode, beat label) extend
past masks sized for 16:9. Kept as `_qc/REPORT-review-cut-burnins.md`.
Same false positive as claude-liam-context-window/vertical. Frames inspected
by eye: all content inside title-safe.

To gate the real content without exporting a final master, `final_frame_check.py`
(strict — no `--lenient`) was run on a scratch concat of `clips/*.mp4` (the
compiler's conformed per-beat clips, which carry no burn-ins):
**24 frames, 0 BLOCKER / 0 MAJOR** (`_qc/REPORT.md`). Scratch file deleted.
`./art final` should pass the same check on the clean master.

## GATE T

PASS, 0 FAIL, no §8.10 advisories (portrait FormBCard text differs enough).

## Clean final (2026-10-09)

`knowledge-cutoff-vertical.mp4` (2160×3840, 60.5 s) + `.verified.json`.
The clean master passed both gates, no `--lenient`:

- GATE T: PASS, 0 FAIL (`TYPECHECK.md`, 2026-10-09).
- GATE V: 24 frames, 0 BLOCKER / 0 MAJOR — confirms the scratch-concat
  result above.

## Advisory

- GATE A: B01 "no shapes recorded — scene may be text-only" — by design (hesitant writer).
- `[art] WARNING: build stamp failed` — known toolkit stamp bug, non-blocking.
- Because run.sh stops at the GATE V failure, its post-steps (ToDo.md, copying
  the cut into `mp4/`) did not run for this folder; the review cut is at the
  folder root.
