# Fifty Vendors, One Brief.

An **ai-explainer** reel (Brutalist toolkit) on the **claude-hai** channel
(Bella / `af_bella`, Pragmatist register, `@HumanitariansAI`).

**The one insight:** scattered public signal about AI vendors becomes one
scored, auditable, cheap-to-run brief per company — and its honesty is the
whole point.

## Subject

The AI Vendor Intelligence Platform: 5 public sources → one scored-signal
table → an on-demand, cost-tracked brief per company.

- **Collectors** pull SEC EDGAR (filings, revenue), GitHub (stars, commits,
  releases), ArXiv (research by affiliation), Google News RSS (funding,
  layoffs, partnerships), and a hand-seeded Neo4j graph (competitors, backers).
- **Storage** — Postgres `ai_company_signals` (one row per signal, typed +
  scored 0–100), plus `collection_runs`, `brief_costs`, `brief_cache`.
- **Output** — send a company name; a same-day cache hit serves free,
  otherwise the top signals are synthesized into a brief with token/cost logged.

## Spine (9 beats)

B00 ask → B01 pipeline overview → B02 the five sources → B03 signal scoring →
B04 the competitive graph → B05 the brief → B06 verdict → B07 your-turn →
B08 title outro.

Bookends render from the registered Claude Remotion comps; the body beats
(B01–B05) are illustrated via SourceFlow / ChipGrid / LayerStack (props are in
`beat_sheet.json`), rendered as reel-local Manim in `manim/scenes.py` or
wrapped Remotion comps.

## Status

- GATE P: **PASS** (see `PEDAGOGY.md`).
- Audio: generated (Kokoro, `af_bella`), ~2:53 runtime — durations are the
  master clock (rendered `mp3/` is git-ignored).
- Previz compiled; body beats B01–B05 pending final motion graphics.

## Build

```bash
python3 runtime/scripts/generate_audio_kokoro.py <this-folder>
./art run <this-folder>      # previz; ART_FACTS=0 for a first pass
./art final <this-folder>    # clean master once no slates remain
```

Rendered media (`*.mp3`, `*.mp4`) is intentionally not committed — it rebuilds
from this paperwork for $0.00.
