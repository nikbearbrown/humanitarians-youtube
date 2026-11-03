# BUILD-PROMPT — congress-cluster-signal

claude-cli explainer of the congressional cluster-signal backtest
(source: this repo's `RESEARCH_REPORT.md`, `market_adjusted.py`, `backtest.py`).

Channel: claude-liam. Voice: Kokoro am_onyx (Onyx). 1920×1080 16:9.
Free pipeline only — no ElevenLabs, no Higgsfield, no publishing.

Beat spine: B00 INTRO → B01 PROBLEM → B02 ASK → B03 CODE → B04 OUTPUT → B05 CHANGE
→ B06 CODE → B07 OUTPUT → B08 SUMMARY → B09 NEXT STEPS → B10 OUTRO.
Full revision cycle (B05→B06→B07). Animated output beats — never static png.

DOUBLE-CHECK (all figures from RESEARCH_REPORT.md; logged in SOURCES.md / FACTCHECK.md):
13,877 trades · 108 members · May 2023–Jun 2026; 5,162 priced BUYs.
Aggregate BUY alpha +0.13% (raw +2.23% vs SPY +2.10%); SELL −0.01%.
Tiers: STRONG 815 α+0.23% win 50.3% · WATCH 1,212 α+0.54% win 50.6% ·
SKIP 132 α−0.04% win 44.7% · SOLO 3,003 α−0.05% win 44.9%.
$10k in STRONG → $10,247 vs $10,224 in SPY. Cluster = ≥2 politicians, same ticker,
30-day window; signal_score = cluster_size × max BCR; tiered at entry, no look-ahead.

NOTE: B01, B04, B07, B08 use Manim (scenes.py: B01_StockAct, B04_AggregateAlpha,
B07_TierTable, B08_Recap). B00/B02/B05/B09 = ClaudeComposerAsk; B03/B06 =
ClaudeCodeBeat (real source); B10 = ClaudeTitleOutro. Per-beat prompt spec in PROMPTS.md.

## Rebuild (from this folder, with the brutalist.art toolkit on hand)
```
python3 runtime/scripts/generate_audio_kokoro.py <this-reel>   # Kokoro narration (free)
./art run <this-reel>                                          # Manim + Remotion + compile
```
Rendered media (`media/`, `mp3/`, `manim/`, the `.mp4`) is intentionally NOT committed —
it regenerates from `beat_sheet.json` + `scenes.py` for $0.00.
