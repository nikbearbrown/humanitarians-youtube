# Fact-Check Generation — Chapter 28

**Fellow:** Novia Dsilva
**Voice:** Bella (`af_bella`)
**Skill:** `cli-explainer`
**Title:** Fact-Check Generation
**Chip:** CANCER TEXTBOOK · CHAPTER 28
**16:9:** 3:17 (197.4s) · **9:16 Short:** 2:31 (drops B05–B07 to fit the 3:00 cap)

Short chapter setup (Nanotechnology in Cancer: delivery, imaging, theranostics). The fact-check report is the main event. Counts from `28_factcheck_report_ai_only_editorial.md` (copied here as `SOURCE-editorial.md`): 168 sentences · 114 AI-only / 54 web-flagged · 13 editorial · 3 hallucination flags on the 114. No invented split of the 54.

## Rebuild

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./art run path/to/2026-08-26-chapter28-fact-check-generation --height 1080
```

`scenes.py` is reel-local Manim (B04 / B07). Remotion patterns: ClaudeComposerAsk, ClaudeScienceLayerStack, ClaudeCodeBeat, ClaudeWindow, ClaudeTitleOutro.

9:16: `./art shorts <this-folder> --drop B05 B06 B07 --handle @Medhavy` then compile `short/` at `--height 1920`.
