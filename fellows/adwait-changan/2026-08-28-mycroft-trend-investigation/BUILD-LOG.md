# BUILD-LOG — Mycroft "Multi-Month Trend Investigation"

Built 2026-08-13, dated Friday 2026-08-28. Toolkit `brutalist.art` (`ai-explainer`),
Kokoro `am_onyx`, **cost $0.00**.

## Result

| Cut | Format | Runtime | Beats | Slates |
|---|---|---|---|---|
| 16:9 master | 3840×2160 | ~3:54 | 13 | 0 |
| 9:16 Short | 2160×3840 | ~2:46 | 8 + endcard | 0 |

## How the subject was chosen

The brief summarised the feature as "compares monthly EBITDA." Reading `trend.py` gave a
better subject: `_load_run` contains **fifteen separate `raise TrendError` paths** before it
will admit a single month into a comparison. The film is about the refusing, not the
comparing — and `payroll`, favourable in all three periods with the detector returning `NO`,
is a genuine falsifiability case already present in the generated output. It is what makes
the three `YES` results mean anything.

Every figure came from `reports/generated/...trend-week35.md` — the artifact the code
emitted — rather than the PR description. They agree; the output is the record.

## Visual QC

**Zero defects.** Three contact-sheet frames (B01, B02, B06) looked incomplete and were all
mid-animation when checked at full resolution.

Both financial tables were authored `numbered: false` from the start. That mattered more here
than on a teaching video: a numbered financial table implies an ordering the report does not
have.

## Toolkit work

The 9:16 half depended on five portrait compositions written during this same build
(`ClaudeIllu916.tsx`) plus a `numbered` fix to `ClaudeWindow916`. Those live in the
**`brutalist.art` repo** and need their own PR; without them this build's Short is not
reproducible.

## Late revision

The fellow set a standing rule mid-build: **no week or episode numbers anywhere.** The
`greeting` prop ("Week 35,"), the outro narration and the outro `subline` were rewritten and
re-rendered in both cuts.

## Honesty boundary carried on screen

Synthetic sample data · recipe `DRAFT` · materiality `DEMO_UNAPPROVED` · human gate `OPEN` ·
no forecast, no recommendation, no causal claim. Stated in B09 and again in the verdict, not
buried in a disclaimer.

## Status

Both cuts rendered, QC clean, gates signed. **Not published, not uploaded.**
