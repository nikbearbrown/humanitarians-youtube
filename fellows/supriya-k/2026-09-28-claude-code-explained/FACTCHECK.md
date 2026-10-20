# Sources & Fact-Check — claude-code-explained

Short paths below are relative to `brutalist.art/`; `v2/` =
`projects/banking-data-analyst-interview-prep/banking-domain-interview-end-to-end-v2/`.

## Claim-by-claim trace

| # | Claim (narrated / on screen) | Source | Verdict |
|---|---|---|---|
| 1 | Claude writes the code fast but can't watch the video (B01) | `HOW-TO.md` §1: "Claude cannot watch the video… Claude is superhuman at the build" | CONFIRMED — paraphrase |
| 2 | An earlier vertical cut was true 4K with text filling at most a fifth of the frame; 139 kbps (B01) | `v2/PLAN.md` lines 26–33: v1 9:16 2160×3840, **139.5 kbps**, "text filling only ~15–20% of frame height" | CONFIRMED |
| 3 | Nothing is built until the plan is approved (B02) | `v2/PLAN.md` Gates §1; this reel's `PLAN.md` | CONFIRMED — the process as practiced |
| 4 | Narration is signed before audio exists; the agent never signs its own gate (B02) | `CLAUDE.md` rule 3 (GATE P binds); `v2/PEDAGOGY.md` "an agent never signs its own gate" | CONFIRMED |
| 5 | The plan said the composer was already portrait-ready (B03) | `v2/PLAN.md` line 119: "`ClaudeComposerAsk` is already portrait-aware" | CONFIRMED |
| 6 | A standalone render of one beat showed everything in the top half (B03) | `v2/STATUS.md` gate 3: "content clustered in the top ~55% of frame" | CONFIRMED — "top half" rounds 55% |
| 7 | Old layout clustered 10–40% of height; rebuild spreads anchors, card at 44% (B04) | `ClaudeComposerAsk.tsx` lines 115/132/148/178 (`height * 0.10…0.40`); `ClaudeComposerAsk916.tsx` lines 87–92 | CONFIRMED — read from source |
| 8 | ~86% fill, up from 55%; 276→341 kbps, no encoder change (B05) | `v2/STATUS.md` gate 3: "≈86% of frame height (was ≈55%), bitrate 341kbps (was 276kbps)" | CONFIRMED |
| 9 | Portrait resolution doesn't change Manim's coordinate frame; audit set portrait coords in its own process; two lines fixed it (B07) | `v2/STATUS.md` "Manim CLI resolution bug"; `v2/short/scenes.py` lines 1–34 | CONFIRMED |
| 10 | Before: roughly the center quarter; after: full frame and the final frame check passed (B08) | `v2/STATUS.md`: "center 25-28% of the real canvas"; "full Gate V pass… 0 MAJOR" | CONFIRMED |

## Not in the sources, and why it isn't a fabricated fact

- B08's on-screen coordinate-grid rescale is an **illustration** of the mechanism, not a captured
  frame (REBUILD LAW). Its numbers are only the sourced ones above.
- B09's owner tags ("you" / "Claude") summarize the gate rules in claims 3–4; they're synthesis,
  not a quote.

## Dating check (DOUBLE-CHECK LAW)

No model names or version numbers in narration; the composer's model chip reads plain "Claude".

## No paid services

Kokoro (`af_bella`, local), Manim (local), Remotion (local). No keys anywhere.


## 9:16-only presentation changes (no new claims)

- B04 / B07 code: the long **comment** lines are re-wrapped to fit the portrait card. Same text,
  same order; code lines untouched (verified by script: identical once comment markers and line
  breaks are normalised). Sources unchanged: `ClaudeComposerAsk916.tsx` lines 46, 50–51, 87–92;
  `short/scenes.py` lines 27–34.
- B00 output lines shortened to fit portrait ("plan — approved first" …), matching B09's wording.
- Endcard: "Supriya" + "Plan. Gate. Execute. Verify." — restates the reel; no new claim.
