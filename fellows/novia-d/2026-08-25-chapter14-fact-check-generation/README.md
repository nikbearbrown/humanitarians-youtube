# Fact-Check Generation — Chapter 14

**Fellow:** Novia Dsilva
**Voice:** Bella (`af_bella`)
**Skill:** `cli-explainer`
**Title:** Fact-Check Generation
**Chip:** CANCER TEXTBOOK · CHAPTER 14
**16:9:** 2:59 (179.8s) · **9:16 Short:** 2:22 (drops B05–B07 to fit the 3:00 cap)

The reel is a workbook, not a TME lecture. Counts and named findings come from `14_factcheck_report_ai_only_editorial.md` (see `SOURCES.md` / `FACTCHECK.md`). 138 sentences · 92 AI-only / 46 web-flagged · 8 editorial · 5 hallucination flags on the 92. No invented split of the 46.

## Rebuild

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./art run path/to/2026-08-25-chapter14-fact-check-generation --height 1080
```

`scenes.py` is reel-local Manim (B04 / B07). Remotion patterns: ClaudeComposerAsk, ClaudeScienceLayerStack, ClaudeCodeBeat, ClaudeWindow, ClaudeTitleOutro.

9:16: `./art shorts <this-folder> --drop B05 B06 B07 --handle @Medhavy` then compile `short/` at `--height 1920`.
