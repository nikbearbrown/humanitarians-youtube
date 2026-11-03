# progressive-tool-router

Production package for the 9:16 explainer **"Why Giving an AI Agent More Tools Can Make It Worse —
Build a Progressive Tool Router with Claude"** (alt title: *1,000 AI Tools vs. 3*).

This folder is a **plan plus a working demo**, not a rendered film. Nothing has been narrated,
rendered, or published yet.

| File | What it is |
|---|---|
| `PRODUCTION-BLUEPRINT.md` | The deliverable: 14-scene table, full narration, asset list, architecture, build demo, benchmark plan, fact-check, 9:16 editing rules, metadata, QC checklist |
| `beat_sheet.json` | Machine-readable scenes (narration, on-screen text, visuals, SFX cues, citation IDs) for the Kokoro + Remotion pipeline used by the other films in this repo |
| `src/progressive_tool_router.py` | Runnable router: 1,000-tool synthetic registry → intent → retrieval → ranking → top-K → optional Claude call |
| `src/benchmark_router.py` | Benchmark harness that produces measured numbers (or refuses to call them measured) |
| `bench/tasks.jsonl` | Labelled task set for selection-accuracy scoring |

## Quick start

```bash
cd src
python progressive_tool_router.py                      # route the demo query over 1,000 tools
python progressive_tool_router.py --query "Plot revenue by month" --k 3
python progressive_tool_router.py --claude             # also call Claude with only the selected tools
python benchmark_router.py --tasks ../bench/tasks.jsonl --repeats 5
```

The demo needs only the standard library. `--claude` and authoritative token counting need
`anthropic` and `ANTHROPIC_API_KEY`.

## Claim policy for this video

1. **No invented metrics.** Token, latency, cost and accuracy figures may appear on screen only
   after `benchmark_router.py` has produced them, labelled with model, date and repeat count.
   Anything else carries an on-screen `ILLUSTRATIVE EXAMPLE` plate for its full duration.
2. **Never claim more tools make a model less intelligent.** The supported framing is context cost,
   routing complexity and selection overhead.
3. **Product claims are current-development information.** Anthropic tool-search behaviour and the
   MCP roadmap both move; re-verify every row of blueprint §F on the publish date.

## Production order (audio is the clock)

1. Approve `PRODUCTION-BLUEPRINT.md` §A narration.
2. Generate narration, measure each line, re-time `beat_sheet.json` from the measured durations.
3. Build captions from the measured audio.
4. Build the Remotion 9:16 composition (design 1080 × 1920, render `--scale=2` → 2160 × 3840).
5. Run `benchmark_router.py`; only then decide whether S9 shows measured numbers or stays qualitative.
6. Storyboard stills → review cut → 4K master → derived masters → QC sheet.
7. Complete blueprint §I before any upload. A rendered master is not permission to publish.
