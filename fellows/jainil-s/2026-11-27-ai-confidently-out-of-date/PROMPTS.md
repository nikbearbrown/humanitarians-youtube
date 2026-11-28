# PROMPTS — Confidently Out Of Date

Week ending 2026-11-27 · `ai-` track.

Deterministic Remotion scenes throughout. No image prompts, no stills, no
human-supplied media. Cost $0.00.

| # | Composition | Props from |
|---|---|---|
| B00 | `ClaudeComposerAsk` | authored |
| B01 | `BrutalistHesitantWriter` | authored · `seed: ai-confidently-out-of-date-b01` |
| B02 | `StageRail` | authored |
| B03 | `PairedBars` | `staleness_results.json` → `curve` + `migrant_case` |
| B04 | `CardSet` | `staleness_results.json` → `migrant_case`, `stale_top5_topic_mix` |
| B05 | `StageRail` | authored, with the two similarity figures from the JSON |
| B06 | `ClaudeComposerAsk` | authored |
| B07 | `HaiTitleOutro` | authored |

**Zero new components.** `PairedBars` carries its third different argument in
three weeks — Simpson's paradox (11-13), training-serving skew (11-20), and
now stale-vs-rebuilt recall — this time with `total: null` and four rows,
which is the shape that forced the A25 fill fix.

## Data reconciliation

Every numeric prop is rewritten from `staleness_results.json` before
rendering. **Prose figures were checked by hand as a separate pass**, against
the JSON, line by line: `0.892`, `100%`, `0.96 before, 0.89 after`. That
second pass exists because the numeric reconciliation is structurally blind to
numbers inside sentences.

It earned its keep on this build. The B05 narration originally said the
similarity score "never dropped at all" — it falls from 0.961 to 0.892, which
is small but not nothing. The line was rewritten to state the actual move
rather than defend the rhetoric, and the stage card prints both figures so a
viewer can see it. Recorded in `FACTCHECK.md`.

## B02 and B05 are a deliberate rhyme

Both `StageRail`, three beats apart. B02 is what goes wrong (index built,
language moves, index does not). B05 is what to do (clock, canary, and the
metric that will not help). Same shape, opposite job.

## The handoff prompt (B06)

> Here is a month of live queries and the corpus our search index was built
> from. What fraction of query terms are out-of-vocabulary for that corpus —
> and which in-vocabulary terms have changed which words they co-occur with
> since?

Why this prompt: the two clauses are the reel's two failure modes, in the
order the viewer can act on them. The first number says *when to rebuild*; the
second says *what you have already been getting wrong*.

## Render

```bash
ART_CONCURRENCY=4 python3 runtime/scripts/remotion_scenes.py <reel>
python3 runtime/scripts/compile.py <reel> --height 2160 --out <reel>
python3 runtime/qc/final_frame_check.py <reel> --mp4 <reel>/<slug>.mp4
```

`--height 2160` is not optional (A20). Chain commands; never drive a build
from a scratchpad script (A23). Write FACTCHECK.md before compiling — GATE F
blocks `final` without it.
