# SHOTLIST.md — congress-cluster-signal (typed work order)

Skin: **claude** · Persona: **Liam (Onyx)** · Register: **Teardown** · 16:9 master.
Spine: INTRO → PROBLEM → ASK → CODE → OUTPUT → CHANGE → CODE → OUTPUT → SUMMARY → NEXT → OUTRO.

| Beat | Lane | Scene / Pattern | Fill | Note |
|------|------|-----------------|------|------|
| B00 | remotion | ClaudeComposerAsk | ✅ auto | cold open, ask answered; IN-FOR-BEAR hello |
| B01 | manim | B01_StockAct | ✅ scenes.py | STOCK Act → dataset → the question |
| B02 | remotion | ClaudeComposerAsk | ✅ auto | the ASK — write market_adjusted.py |
| B03 | remotion | ClaudeCodeBeat | ✅ auto | ACTUAL code: market_adjusted.py |
| B04 | manim | B04_AggregateAlpha | ✅ scenes.py | run 1 — BUY vs SPY, +0.13% residual |
| B05 | remotion | ClaudeComposerAsk | ✅ auto | the REVISION — cluster tiering |
| B06 | remotion | ClaudeCodeBeat | ✅ auto | ACTUAL code: backtest.py tag_signal |
| B07 | manim | B07_TierTable | ✅ scenes.py | run 2 — alpha + win% by tier (the result) |
| B08 | manim | B08_Recap | ✅ scenes.py | the lesson — what carries the edge |
| B09 | remotion | ClaudeComposerAsk | ✅ auto | HANDOFF — "Your turn." prompt typed in |
| B10 | remotion | ClaudeTitleOutro | ✅ auto | title restate + @HumanitariansAI |

**Open slots:** none. All Manim outputs are authored in `scenes.py`; all input/
bookend beats render from the Claude Remotion templates. No pantry stills needed.

**Revision cycle (cli-explainer REVISION LAW):** B05 (change) → B06 (revised
code) → B07 (deeper output). Present. ✔
