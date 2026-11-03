# Multi-Month Trend Investigation — Mycroft Finance Investigator

**Weekly work video** · Friday 2026-08-28
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> The feature compares three months. The engineering is that it tries **fifteen** separate
> times to refuse before it will — and then ships the "why did this happen" field
> deliberately blank.

## Master

`Mycroft_AdwaitChangan_2026-08-28.mp4` — 3840×2160, 3:54, 13 beats, zero slates, zero QC defects.
Review cut: `Mycroft_AdwaitChangan_2026-08-28-slate.mp4`.
**9:16 cut is not yet produced** — see `_qc/REPORT.md`, criterion 3.

## What the video does

A summary of this feature would lead with "it compares monthly EBITDA," which is the least
interesting true sentence about it. The week's actual work was the refusal surface and the
claim boundary, so that is the video.

Act 1 states the admission rule — a month may enter the comparison only if scope matches,
hashes match, and EBITDA recomputes — then shows the real three-period table. Act 2 is the
refusing: ten verbatim lines of the tamper check, and six of the fifteen conditions that end
a run. Act 3 is the test that matters: `payroll` is favourable in all three periods and the
detector returns `NO`, which is what makes the three `YES` results mean anything. Then the
boundary — the explanation field ships intentionally blank, with a named owner.

## Source

Code: [nikbearbrown/mycroft PR #17](https://github.com/nikbearbrown/mycroft/pull/17)
Figures: `reports/generated/mycroft-finance-investigator-trend-week35.md` — the artifact the
code emitted, not the PR prose.

Synthetic sample data · recipe `DRAFT` · materiality `DEMO_UNAPPROVED` · human gate `OPEN`.
All four stated on screen, not buried in a disclaimer.

## Beat map

| Beat | Pattern | What you watch |
|---|---|---|
| B00 | ClaudeComposerAsk | Intro line + the ask, answered in three lines |
| B01 | ClaudeScienceLayerStack | **The admission rule** — scope / hashes / EBITDA recomputes |
| B02 | ClaudeScienceSourceFlow | Re-derived, not re-read — it trusts nothing it was handed |
| B03 | ClaudeWindow | **Real EBITDA table** — 261,000 → 230,000 → 265,000 |
| B04 | CwcConceptCard | "It Would Rather Refuse" |
| B05 | ClaudeCodeBeat | The tamper check, ten verbatim lines of `_load_run()` |
| B06 | ClaudeScienceChipGrid | Six of the fifteen refusal paths |
| B07 | ClaudeWindow | **Falsifiability** — payroll comes back `NO` |
| B08 | ClaudeScienceLayerStack | What it computed / refuses to claim / who owns the why |
| B09 | CwcConceptCard | Still marked DRAFT, on purpose |
| BVDT | ClaudeVerdictArtifact | A comparison engine that refuses fifteen ways |
| BHTF | ClaudeComposerAsk | The viewer's prompt, read aloud |
| BOUT | ClaudeTitleOutro | Title restate  |

## Rebuild

```bash
source /Users/adwaitchangan/Study/Brutalist/brutalist.art/.venv/bin/activate
cd /Users/adwaitchangan/Study/Brutalist/brutalist.art
REEL=/Users/adwaitchangan/Study/Brutalist/humanitarians-youtube/fellows/adwait-changan/2026-08-28-mycroft-trend-investigation
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
python3 runtime/scripts/remotion_scenes.py "$REEL"
python3 runtime/scripts/compile.py "$REEL" --review
./art final "$REEL"
```

Cost: **$0.00**.

## Status

16:9 master rendered, QC clean, gates signed. **9:16 outstanding. Not published, not uploaded.**
