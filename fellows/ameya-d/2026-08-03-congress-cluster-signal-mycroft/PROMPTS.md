# PROMPTS.md — congress-cluster-signal

Beat-prefixed prompts. The Manim OUTPUT beats are authored directly in
`scenes.py` (no open slots), so these prompts document how each output beat was
specified — the reconstruction that satisfies the ACTUAL-CODE LAW (the on-screen
ASK plausibly generates the on-screen CODE, which plausibly produces the OUTPUT).

## B01 — STOCK Act setup (Manim: B01_StockAct)
Animate the framing: title "The STOCK Act, 2012 — disclose every trade within 45
days", the transformation line "a law to deter insider trading → becomes → a
public dataset of what powerful people buy", three stat cards (13,877 trades ·
108 members · 2023–26), and the closing question "Follow every buy — beat the
index?" underlined in terracotta.

## B04 — aggregate alpha (Manim: B04_AggregateAlpha)
Two near-identical bars: congressional BUY raw +2.23% vs SPY +2.10% over the same
windows; isolate the +0.13% residual as a terracotta sliver labeled "alpha =
+0.13%"; verdict "Congress rides the market." with SELL alpha −0.01% as a footnote.
n = 5,162 priced BUYs.

## B07 — tier table (Manim: B07_TierTable)
Animate a four-row table (columns TIER · n · alpha · win%): STRONG 815 +0.23%
50.3% · WATCH 1,212 +0.54% 50.6% · SKIP 132 −0.04% 44.7% · SOLO 3,003 −0.05%
44.9%. Box the two clustered rows (STRONG, WATCH) in terracotta; bottom lines:
"~5-point win gap across 5,162 events" and "$10k in STRONG → $10,247 vs $10,224
in SPY".

## B08 — recap (Manim: B08_Recap)
Three verdict rows with glyphs: ✅ "Cluster membership carries the edge —
independent members converge on one ticker"; ❌ "The conviction score does NOT
rank — WATCH +0.54% beat STRONG +0.23%, not monotone"; ❌ "Small samples lie — 64
members looked inverted; stable only at 108". Closing line in terracotta: "A
noise filter — not a profit engine." + subline "research & education only — not
financial advice".

## Composer / code beats (Remotion — verbatim from beat_sheet.json)
- **B00 / B02 / B05 / B09** → `ClaudeComposerAsk` `command` field is the prompt shown.
- **B03** → `ClaudeCodeBeat` — real `market_adjusted.py` lines.
- **B06** → `ClaudeCodeBeat` — real `backtest.py: tag_signal` lines.
- **B10** → `ClaudeTitleOutro` — title restate.
