# PROMPT — "Unblocking the Team."

The brief, and how each constraint was resolved.

## Constraints given

| # | Constraint | How it was resolved |
|---|---|---|
| 1 | Total length ~2:00 | 119.07s measured. Narration was written to a word budget (~2.85 words/sec for `af_bella`) per beat, then Kokoro confirmed it. No padding, no trimming after the fact. |
| 2 | 16:9 and 9:16, both 4K | 16:9 master rendered at 3840×2160 via `ART_REMOTION_SCALE=2` + `compile.py --height 2160`. 9:16 derived from that same master by letterbox, never rebuilt. |
| 3 | Progress update, not an explainer | Act names are reporting acts — ASK / BLOCKER / SHIPPED / IN FLIGHT / NEXT / OUTRO — not the explainer's BLUF/FRAMEWORK/MECHANICS/LIMIT/APPLY. |
| 4 | Cover the workshop and the GitHub blocker | B01, with the blocker made visual rather than narrated at. |
| 5 | Cover the Suno series as the week's main work | B02, the longest beat at 30.27s, with real runtimes on screen. |
| 6 | Cover the signup documentation as in-progress | B03, stamped `IN PROGRESS` in the graphic itself so the status cannot be misread. |
| 7 | Mention Midjourney as next | B04, on the dashed side of a NOW pin. |
| 8 | Consistent look and feel with prior videos | Same opener and outro components, same eyebrow grammar, same Claude token set, same spark-line footer. |

## Constraints inherited from earlier feedback

| Source | Rule | Applied |
|---|---|---|
| Week-01 review | Start and end screens must match across all videos | `ClaudeComposerAsk` opener, `ClaudeTitleOutro` outro — identical to both week-01 reels |
| Week-01 review | Mention Humanitarians AI in intro and outro | B00 opens with it, B05 closes with it |
| Week-01 review | "This video is very bare" — build real motion graphics | Four purpose-built scenes; zero generic text cards |
| Standing Suno rule | Internal-training register, no overselling | No perk framing anywhere; the register reports, it does not pitch |
| Standing rule | No personal references beyond the presenter | Only "Rohan Vijaykumar" appears |
| Toolkit doctrine | Library-first — search before authoring | `./art scenes` run for all four needs; all four confirmed genuine misses before any component was written |

## The register question

A progress update is the easiest place to drift into either bragging or
bookkeeping. The Pragmatist register resolves it the same way it resolves an
explainer: **lead with the constraint.** Each body beat names what was in the
way before it names what was done about it. B01 names the blocker before the
workshop. B03 names the tribal-knowledge problem before the documentation. The
work sounds necessary rather than impressive, which is the correct tone for an
internal report.

## What "2 minutes" bought

Six beats. That is enough for one blocker, one shipped thing, one in-flight
thing, and one commitment — with an opener and an outro. It is not enough for a
fifth body beat, which is why the agent-first walkthrough is folded into B01 as
the resolution rather than given a beat of its own.
