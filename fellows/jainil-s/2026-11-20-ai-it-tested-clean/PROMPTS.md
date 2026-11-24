# PROMPTS — It Tested Clean

Week ending 2026-11-20 · `ai-` track.

Deterministic Remotion scenes throughout. No image prompts, no stills, no
human-supplied media. Cost $0.00.

| # | Composition | Props from |
|---|---|---|
| B00 | `ClaudeComposerAsk` | authored |
| B01 | `BrutalistHesitantWriter` | authored · `seed: ai-it-tested-clean-b01` |
| B02 | `StageRail` | authored |
| B03 | `PairedBars` | `skew_results.json` → `offline.acc` + `skews[*].acc` |
| B04 | `ClaudeBarChart` | `skew_results.json` → `mean_score` fields |
| B05 | `CardSet` | `skew_results.json` → `skews[*].psi`, `monitoring.warehouse_psi` |
| B06 | `StageRail` | authored |
| B07 | `ClaudeComposerAsk` | authored |
| B08 | `HaiTitleOutro` | authored |

**Zero new components.** `PairedBars` shipped the previous week with
`ai-every-group-the-other-way` and carries this reel's central figure
unchanged — with `total: null`, since here there is no aggregate row, only
four independent comparisons.

## Data reconciliation

Every numeric prop is rewritten from `skew_results.json` before rendering.
**Prose figures were also checked by hand this time** — against the source,
line by line — because the previous reel shipped an invented percentage inside
card text where the numeric pass is structurally blind. The spoken figures
(73.4, 64.2, 41.5, 59.1), the PSI values on the cards and the captions were
all read back against the JSON.

## B02 and B06 are a deliberate rhyme

Both are `StageRail`, four beats apart, and they are the same diagram twice:
B02 is the broken wiring (warehouse → feature store → model, nothing
comparing), B06 is the fix (model → serving log → compare to training). Same
shape, opposite conclusion. ILLUSTRATE LAW's concern is *consecutive* beats
sharing a scheme; these are separated by three.

## The handoff prompt (B07)

> Here is how one feature is computed in training, and here is how it is
> computed at request time. Compare them on window, units, null handling and
> completeness, and tell me every way the two could return different numbers
> for the same entity.

Why this prompt: it is the reel's method applied to the viewer's own system,
and it names the four axes the episode actually measured rather than asking
vaguely for problems.

## Render

```bash
ART_CONCURRENCY=4 python3 runtime/scripts/remotion_scenes.py <reel>
python3 runtime/scripts/compile.py <reel> --height 2160 --out <reel>
python3 runtime/qc/final_frame_check.py <reel> --mp4 <reel>/<slug>.mp4
```

`--height 2160` is not optional (A20). Chain commands; never drive a build
from a script in the session scratchpad (A23). **Write FACTCHECK.md before
compiling** — GATE F blocks `final` without it (learned the hard way on the
2026-11-13 reel; this build wrote the paperwork while the beats rendered).
