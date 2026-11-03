# SHOTLIST — The Classifier That Learned When Not to Guess
## Total: 159.68s (measured Kokoro audio, B00 silent) · 9 beats · all Manim, no pantry/toolkit assets

| Beat | Act | Lane | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|---|
| B00 | TITLE | manim | GRAPHIC | B00_TitleCard (scenes.py) | 4.05s | Silent title card: "The Classifier That Learned When Not to Guess" + @HumanitariansAI, no narration |
| B01 | EXEC-SUMMARY | manim | GRAPHIC | B01_ExecSummary (scenes.py) | 17.59s | Personal-intro card: name + role + one-line plain-language summary, spoken |
| B02 | HOOK | manim | GRAPHIC | B02_CounterHook (scenes.py) | 14.86s | Counter: 21 -> 13 resolved -> 8 remaining, landing on boxed "8" |
| B03 | SETUP | manim | GRAPHIC | B03_ResidualHeadlines (scenes.py) | 30.41s | 3 of the real 8 residual headlines shown verbatim (24-Hour Trading, KYC, RAUM), "+5 more, same shape" tag, caption "no fixed keyword list resolves these safely" |
| B04 | DISCOVERY-FIX | manim | GRAPHIC | B04_PipelineDiagram (scenes.py) | 26.5s | Pipeline diagram: existing Normalize Data node -> conditional gate ("ONLY IF source_feed == 'Unknown Source'") -> NEW Layer 2 - LLM Source Classification node (Ollama, local) vs. bypass branch for every other item ("never touched"), fail-open validation note, merge into Filter Valid Content |
| B05 | PROOF | manim | GRAPHIC | B05_ProofNumbers (scenes.py) | 27.12s | The 4 real numbers together: 0 mutated / 1 resolved / 7 declined / 0 errors, plus the one resolved headline (JD Supra enforcement piece) and its new label (FINRA Enforcement News) |
| B06 | HONEST-LIMITS | manim | GRAPHIC | B06_HonestLimits (scenes.py) | 24.34s | "1 of 8 — and that's the correct number," framed as correct not a shortfall, with all 7 declined real headlines dimmed below |
| B07 | TAKEAWAY | manim | GRAPHIC | B07_Statement (scenes.py) | 13.3s | Statement card: the win is knowing when not to guess |
| B08 | SIGN-OFF | manim | GRAPHIC | B08_BrandOutro (scenes.py) | 1.51s | @HumanitariansAI brand card, "explained with Claude Code", "in for Sai Pranavi J." — very short beat, narration is just "Explained with Claude Code." |

## Lane summary
- MANIM: all 9 beats, self-contained in this reel's own `scenes.py` (landscape)
  and `vertical/scenes.py` (native-portrait companion). No pantry stills, no
  Remotion components, no `brutalist/` toolkit changes.
- Style/palette/helpers (PALETTE, `T()`, `fit()`, `panel()`, `box_around()`)
  copied from this fellow's closest sibling,
  `2026-09-29-the-keyword-that-cried-wolf` (same fellow, same voice, same
  series), for house-style consistency.
- Every quoted string on screen (B03's 3 residual headlines, B04's node name
  and condition text, B05's 4 proof numbers and the resolved headline/label,
  B06's 7 declined headlines) is verbatim from
  `/Users/pranavijs/mycroft/scripts/regulatory-intel/B2-VERIFICATION.md` (the
  2026-10-06 addendum) and `workflow.dev.json`'s `Layer 2 - LLM Source
  Classification` node — see `SOURCES.md`'s claim -> source mapping. Nothing
  paraphrased except the B01/B06/B07 on-screen summary/statement cards, which
  are intentionally shorter restatements of their own spoken narration (same
  convention as every sibling reel's exec-summary/statement beats).
- B04 is this reel's most legibility-critical beat: the new node's conditional
  gate ("ONLY IF source_feed == 'Unknown Source'") and the untouched bypass
  branch are both shown explicitly as separate paths, not narrated alone —
  matching `FACTCHECK.md` item #3 and the Legibility Contract.
- B05 shows all 4 real numbers together (0 mutated / 1 resolved / 7 declined /
  0 errors), per `FACTCHECK.md` item #4 and the Legibility Contract.
- B06's "1 of 8" framing is stated as a correct outcome, not softened or
  apologized for, per `FACTCHECK.md` item #6 and house style.

## Vertical companion
`vertical/SHOTLIST.md` documents the native-portrait redesign of all 9 beats
built via `./art vertical` — see that file for the per-beat
side-by-side -> stacked notes for B04 (flow diagram) and B06 (two-column
declined-headline list).

## QC status
See `BUILD-LOG.md` for GATE A/W/V results and per-beat visual-inspection
findings once the render pipeline has run.
