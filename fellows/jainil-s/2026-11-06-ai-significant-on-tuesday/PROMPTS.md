# PROMPTS — Significant On Tuesday

Week ending 2026-11-06 · `ai-` track.

The typed work order. Every beat is a deterministic Remotion scene driven by
arrays from `beat_data.json` — there are no image prompts, no generated
stills, and no human-supplied media in this reel.

---

## Scene fills

| # | Composition | Props from |
|---|---|---|
| B00 | `ClaudeComposerAsk` | authored |
| B01 | `BrutalistHesitantWriter` | authored · `seed: ai-significant-on-tuesday-b01` |
| B02 | `ThresholdWalk` | `beat_data.json` → `hero.z`, band 1.96 |
| B03 | `ClaudeBarChart` | `beat_data.json` → `fpr_by_looks` |
| B04 | `DistributionShape` | `beat_data.json` → `curse.curve` (40 bins, ±15 pp) |
| B05 | `CardSet` | `beat_data.json` → `boundaries` |
| B06 | `ThresholdWalk` | `beat_data.json` → `hero.z`, band 2.66 |
| B07 | `ClaudeComposerAsk` | authored |
| B08 | `HaiTitleOutro` | authored |

**The beat sheet is populated from the JSON, not retyped.** A reconciliation
pass rewrites every data prop from `beat_data.json` before rendering and
prints whether each already matched. On this build it caught a real drift: the
B04 density array had been hand-transcribed and was **not** identical to the
generated one. Re-run the reconciliation after any edit to the evidence.

---

## The handoff prompt (B07)

Read aloud verbatim, then discussed, per HANDOFF LAW:

> Simulate an A/B test where both arms are identical. Check significance every
> 100 users and stop at the first p < 0.05. Report how often it declares a
> winner, and how large the measured effect is when it does.

Why this prompt: it is the whole reel in four lines, and it is falsifiable on
the viewer's own machine in under a minute. The second number is the one that
does the work — a viewer who runs it sees the winner's curse appear in their
own output rather than taking it from a chart.

---

## Render

```bash
python3 runtime/scripts/remotion_scenes.py <reel>
python3 runtime/scripts/compile.py <reel>
```

`remotion_scenes.py` in the foreground (CLAUDE.md rule 4) — never a hand-rolled
`npx remotion render`. The Short is a separate beat sheet written by
`shorts.py` into `short/`, rewired to the `916` companions; it is never a
centre-crop.

New compositions this reel: `ThresholdWalk`, `ThresholdWalk916`. Registered in
`Root.tsx` and indexed with `build_scene_index.py` (645 renderable). The GATE L
punt that produced them is in `TEMPLATE-MISSES.md`.

---

## Not used

No Higgsfield, no Manim, no Smithsonian stills, no pantry media, no human
screen recordings. Free path end to end: Kokoro `am_onyx` for audio, Remotion
for every frame. Cost $0.00.
