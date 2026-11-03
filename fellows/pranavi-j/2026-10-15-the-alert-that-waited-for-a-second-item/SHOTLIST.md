# SHOTLIST — The Alert That Waited for a Second Item
## Total: 123.34s (measured Kokoro audio, B00 silent) · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.05s | Silent title card: "The Alert That Waited for a Second Item" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 15.94s | Personal-intro card: name + role + one-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_CounterHook (scenes.py) | 12.5s | 0 / 1 (flagged, boxed) / 2 item counter — the exactly-one-item edge case the alert was never built to handle |
| B03 | SETUP | manim | GRAPHIC | B03_BuggyLineOfCode (scenes.py) | 16.54s | The real `hasData` guard line from `Generate Email`, shown verbatim; `newItems.length > 1` flagged gold/crimson via character-index slicing (no paraphrase) |
| B04 | DISCOVERY-FIX | manim | GRAPHIC | B04_DeadEndAndFix (scenes.py) | 16.49s | Before/after diff (`> 1` struck through, `> 0` added) chained to the real dead end: fails the check -> `has_items: false` -> If-node TRUE branch `[ ]` — nowhere to go |
| B05 | VERIFICATION | manim | GRAPHIC | B05_BeforeAfterTable (scenes.py) | 22.9s | The real 0/1/2-item before/after harness table; the 1-item row boxed gold as the one that changed; closing line notes the re-run against the real patched file on disk |
| B06 | HONEST-LIMITS | manim | GRAPHIC | B06_HonestLimits (scenes.py) | 23.38s | 2 honest-limit cards, full weight: (1) caught by code review, not a live incident; (2) a related `source_feed` compatibility gap, flagged not fixed |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 10.03s | Statement card: an alert system is only as good as the cases it was built to handle |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 1.51s | @HumanitariansAI brand card, "explained with Claude Code", "in for Sai Pranavi J." — very short beat, narration is just "Explained with Claude Code." |

## Lane summary
- MANIM: all 9 beats, self-contained in this reel's own `scenes.py` (landscape)
  and `vertical/scenes.py` (native-portrait companion). No pantry stills, no
  Remotion components, no `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `T()`, `fit()`, `panel()`, `box_around()`)
  copied from this fellow's closest sibling,
  `2026-10-06-the-classifier-that-learned-when-not-to-guess` (same fellow,
  same voice, same series, same toolkit version), for house-style consistency.
- Every quoted code line (B03's `hasData` guard, B04's diff and dead-end
  output) and every number (B05's before/after table) is verbatim from
  `/Users/pranavijs/mycroft/scripts/regulatory-intel/B6-VERIFICATION.md` — see
  `SOURCES.md`'s claim -> source mapping. Nothing paraphrased except the
  B01/B02/B06/B07 on-screen summary/statement cards, which are intentionally
  shorter restatements of their own spoken narration (same convention as every
  sibling reel's exec-summary/hook/statement beats).
- B03 is this reel's most legibility-critical beat: the real `hasData` guard
  line is shown in full (not paraphrased), with the exact substring
  `newItems.length > 1` isolated via Manim `Text` character-index slicing and
  boxed — per `FACTCHECK.md` item #1 and the Legibility Contract.
- B04's dead-end chain (fails the check -> `has_items: false` -> If-node TRUE
  branch `[ ]`) matches the traced node-graph connections exactly, per
  `FACTCHECK.md` item #2.
- B05 shows the full real before/after table (0/1/2 items) together, per
  `FACTCHECK.md` item #4 and the Legibility Contract.
- B06's two honest limits are stated at full weight, neither softened, per
  `FACTCHECK.md` items #5/#6 and house style.

## Vertical companion
`vertical/scenes.py` documents the native-portrait redesign of all 9 beats
built via `./art vertical` — parent's 3-tile row (B02), 3-card row (B05) and
2-card row (B06) each become a single stacked column; B03's code line is
re-wrapped across more/narrower lines (same verbatim substrings); B04's chain
was already a single column in the landscape parent and is simply narrowed.

## QC status
See `BUILD-LOG.md` for GATE A/W/V results and per-beat visual-inspection
findings once the render pipeline has run.
