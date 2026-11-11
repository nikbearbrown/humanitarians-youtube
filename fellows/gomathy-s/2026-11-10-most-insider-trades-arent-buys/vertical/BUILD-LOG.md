# BUILD-LOG — insider-buying-noise/vertical

Portrait 9:16 companion, 12 beats, review cut
`insider-buying-noise-vertical-slate.mp4` (64.7 s), built 2026-11-10 with
`./art vertical` then `./art run`. Same narration and audio as the 16:9 reel
(`mp3/timings.json` copied from the parent; `shorts.py` doesn't copy it). No
toolkit edits. Not committed.

## What changed from the 16:9 sheet

| Beats | Portrait handling | Why |
|---|---|---|
| B00, B10 | `ClaudeComposerAsk916`, largeText, `runningText: ""`, `modelLabel: "Claude"` | p-value pattern |
| B04, B08, B09 | `FormBCard916`, `icon: "BOX"` on every item, subs ≤ 26 chars | FormBCard916 crashes without icons |
| B01–B03, B05–B07 | native portrait Manim in `scenes.py` (frame 4.5 × 8, SAFE_W 3.9, labels ≥ size 32, text y −2.85 … 3.4) | no portrait Remotion equivalents |
| B11 | Manim `B11_OutroCard` replaces `OutroSeries` (no `OutroSeries916`) | same text as landscape |

Portrait label shortenings, made to keep every label at or above size 32
without width-scaling. The numbers don't change:

| Beat | 16:9 | 9:16 |
|---|---|---|
| B02 | "Non-derivative table · Form 4 only" / "14 quarters, by filing date" | "Non-derivative table" / "14 quarters, filing date" |
| B03 | "Tax/exercise payments (F)"; footer "Share of all 999,542 Form 4 rows, by transaction code" | "Tax/exercise (F)"; "Share of 999,542 rows" |
| B05 | "Pre-Registered Filters"; "Private deals, ESPP, DRIP"; "Filed >30 days after trade"; footer on one line | "Registered Filters"; "Private, ESPP, DRIP"; "Over 30 days to file"; "10b5-1: kept, flagged" / "Joint filing: 1 insider" |
| B07 | "25 random buys, each compared with its filing"; "Example, Equifax price: filed $166.1941 · data set $166.19" | "25 random buys"; "e.g. filed $166.1941" / "data set $166.19" (Equifax name dropped) |

B05 portrait: the footer fades in with the title, not at the end, so the
mid-beat frame fills the canvas (GATE V underfill 47% before).

## Gate results

| Gate | Result |
|---|---|
| A | warnings only (text-only scenes) |
| W | pass |
| B (strict) | B05: three numbers at x = 1.95 flagged outside the safe area → number column 1.95 → 1.9. B07: "10 rounding only" right edge 2.01 → legend start −1.45 → −1.75. Then CLEAN, all seven scenes |
| T | PASS, 12/12 (min text-run 89 px vs 72 px portrait floor) |
| V on the review cut | 24 BLOCKER, all `edge-bleed` from the review burn-ins (same false positive as the p-value, knowledge-cutoff and claude-liam verticals). Kept as `_qc/REPORT-review-cut-burnins.md` |
| V strict on a scratch concat of `clips/*.mp4` | **24 frames, 0 MAJOR, 2 BLOCKER: B06_50 and B06_85 `edge-bleed` right/bottom.** Diagnosis below. `_qc/REPORT.md` |

### The B06 BLOCKER is the compile pad strip, not scene content

- `compile.py` scales the 2160 × 3840 render to 1215 × 2160 and pads to 1216
  with `0xF3EBDD` (`vf_fit`). That leaves a 2-px column at x = 1214–1215.
- After x264, that column reads (243, 235, 218), which is 30 from the inferred
  background (248, 248, 248). The threshold is 28. In other beats the same
  strip reads (243, 235, 221) = 27 and passes.
- Raw `manim/B06.mp4` has a clean right column, (249, 247, 244).
- The only ink right of the safe edge (x > 1155) is that strip: 4,040 px, 0 px elsewhere.
- Diagnostic only, not a pass: with the strip replaced by its neighbouring column, B06_50 and B06_85 both return no defects (fill 58% / 78%).
- The fix would belong in `compile.py` (pad colour, or an even scaled width). That's a toolkit edit, so it hasn't been made.

Eye check: frames at 15/50/85% of every beat read on a contact sheet. All text
legible and inside the frame, numbers identical to 16:9, no terracotta text.

## Pre-final rewording rebuild (2026-11-10)

B04, B06, B07 and B08 narration reworded and re-voiced in the parent; their mp3s
and `timings.json` copied here, `actual_duration_s` synced. B06/B07 retimed
(final waits 1.65 / 1.89 s); B08 card item 1 "Filters fixed first / Before any
returns". Cut 64.7 s. GATE B CLEAN, GATE T PASS. GATE V on the review cut: 24
burn-in false positives again (`_qc/REPORT-review-cut-burnins.md`). Strict GATE
V on the clean-clip concat: **4 BLOCKER, 0 MAJOR: B06_50, B06_85, B08_50,
B08_85**, all `edge-bleed` right/bottom. B08 is new and has the same cause as
B06: in all four frames the only ink right of x = 1155 is the 2-px pad column
(243, 235, 218), 4,320 px; 0 px elsewhere. With that column replaced by its
neighbour, all four frames return no defects (diagnostic only, not a pass). The
fix is still in `compile.py`; not made.

## Final master (2026-11-10, approved by Gomathy)

`./art final vertical --height 3840 --out vertical` →
`insider-buying-noise-vertical.mp4`, 2160 × 3840, 24 fps, H.264 + AAC, 64.625 s.

1. **First attempt REFUSED by compile.py's built-in GATE V: B03_50 `edge-bleed`
   left.** This was real content, not padding. Scanning the 4K frame showed ink
   at x = 94–107, rows 2490–2812, inside the safe inset (x = 108, margin 8). It
   was the Purchases (P) row sliding in from X0 − 0.15 = −2.10 and its box at
   ≈ −2.01, both outside the ±1.95 safe area. The 1216-px review compile had
   sampled it below threshold. Fix in this folder's `scenes.py` only: B03
   `X0, MAXW = −1.95, 2.75 → −1.85, 2.65` (bar right edge unchanged) and
   slide-in shift 0.15 → 0.08. Re-rendered, GATE A/W/B clean. B03 ink scanned
   every 0.1 s across the beat: x = 153 … 2014 (safe 108 … 2052). Numbers and
   wording unchanged. The review slate was rebuilt with the same fix.
2. **Second attempt: written.** Strict GATE V on the final master:
   **24 frames, 0 BLOCKER, 0 MAJOR** (`_qc/REPORT.md`). GATE T PASS.

**Compiler padding false positive (B06/B08, review cuts only).** The review
cuts are compiled at height 2160, so `vf_fit` scales the 2160 × 3840 render to
1215 × 2160 and pads to 1216 with `0xF3EBDD`. That 2-px column reads
(243, 235, 218) after x264, which is 30 from the background against a threshold
of 28, so GATE V reported right-edge bleed on B06_50/85 and B08_50/85.
Evidence:
- Raw renders have a clean right column (249, 247, 244).
- In all four frames the only ink right of x = 1155 was that column (4,320 px); 0 px elsewhere.
- With the column replaced by its neighbour, all four frames pass.
- At `--height 3840` no scaling or padding happens and the same beats pass strict GATE V.

The fix (pad colour, or an even scaled width, in `compile.py`) is a toolkit
change; not made.

Stopped after the final master. Not committed. `./art final` not run.
