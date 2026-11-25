# PROMPTS — Every Group Went The Other Way

Week ending 2026-11-13 · `ai-` track.

Deterministic Remotion scenes throughout. No image prompts, no generated
stills, no human-supplied media. Cost $0.00.

| # | Composition | Props from |
|---|---|---|
| B00 | `ClaudeComposerAsk` | authored |
| B01 | `BrutalistHesitantWriter` | authored · `seed: ai-every-group-the-other-way-b01` |
| B02 | `PairedBars` | `simpson_results.json` → `departments` + `aggregate` |
| B03 | `ClaudeBarChart` | `simpson_results.json` → `shares.overall_rate` |
| B04 | `CardSet` | `simpson_results.json` → `easy_share_men` / `easy_share_women` |
| B05 | `ClaudeBarChart` | `simpson_results.json` → `aggregate` + `standardised_women_rate` |
| B06 | `StageRail` | authored |
| B07 | `ClaudeComposerAsk` | authored |
| B08 | `HaiTitleOutro` | authored |

## Data reconciliation — and its blind spot

Every **numeric prop** is rewritten from `simpson_results.json` before
rendering rather than typed. On this build all numeric props matched.

**It still missed an invented figure.** B04's card read "74% applied to C, E
or F" where the data says 72.3%. That number lives inside a *card line* —
prose, not a numeric prop — so the reconciliation could not see it. Figures
embedded in sentences need a separate read against the source. Treat prose
containing numbers as unverified until someone has checked it by hand.

## The handoff prompt (B07)

Read aloud verbatim, then discussed, per HANDOFF LAW:

> Here is a metric we report as a single number, and a segment column. Split
> it, and tell me whether any segment moves the opposite way to the total —
> and what would have to be true about the segments for that to happen.

Why this prompt: it is falsifiable on the viewer's own data in minutes, and
the second clause is the teaching — it asks for the *condition*, not just the
check, which is the part that transfers.

## Render

```bash
ART_CONCURRENCY=4 python3 runtime/scripts/remotion_scenes.py <reel>
python3 runtime/scripts/compile.py <reel> --height 2160 --out <reel>
python3 runtime/qc/final_frame_check.py <reel> --mp4 <reel>/<slug>.mp4
```

`--height 2160` is not optional (A20). Drive the build by chaining commands,
never from a script in the session scratchpad (A23). **Write FACTCHECK.md
before compiling** — GATE F blocks `final` without it, which is exactly what
happened on this build.

New compositions this reel: `PairedBars`, `PairedBars916`. The GATE L punt
that produced them is in `TEMPLATE-MISSES.md`.
