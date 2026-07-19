# FACTCHECK — vox-prompt-six-slots

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B01 | "Improve this" leaves six decisions to Claude | ✓ | Chapter 1: "A strong Claude prompt separates six kinds of information." The card's core idea: "six missing decisions" |
| B02 | Dr. Osei scenario: specialist committee, general-audience output | illustrative | Adapted from card key case (researcher, specialist committee). Illustrative. |
| B03 | Polished rewrite optimized for wrong audience | ✓ | Chapter 1: "She gets a polished rewrite — reorganized, well-phrased, and optimized for a general academic audience. Her actual audience is a specialist review committee." |
| B04 | Six slots: task, context, sources, constraints, format, evaluation criteria | ✓ | Chapter 1: "A strong Claude prompt separates six kinds of information... Task, Context, Constraints, Output Format, Examples, Evaluation Criteria" (chapter uses 6 names; card's 6 include "sources" instead of "examples") |
| B05 | Claude's generic guesses for each slot are plausible | ✓ | Chapter 1: "Claude has no way to know... So Claude applies defaults." |
| B06 | Context slot: specialist vs general audience | ✓ | Card key case verbatim |
| B07 | Same input, two different outputs depending on slots filled | ✓ | Chapter 1 before/after examples demonstrate this |
| B08 | Each filled slot removes a generic guess | ✓ | Chapter 1: "The six components... each one exists to prevent a specific failure." |
| B09 | Dr. Osei's filled slots (verbatim from card) | ✓ | Card example seed: task, context, sources, constraints, format, evaluation verbatim |
| B10 | Six slots apply to any request | ✓ | Chapter 1: general principle |
| B11 | Jamie scenario: "analyze this dataset" → descriptive stats | illustrative | Invented. Plausible. Labeled illustrative. |
| B12 | Jamie fills task slot → outlier report | illustrative | Illustrative extension. |
| B13 | Thirty-second slot check before any vague request | ✓ | Chapter 1 skeleton/template approach |
| B14 | Prompt is a work order with six slots | ✓ | Chapter 1 thesis |

## Terms table
| Term | Debuts | Prior need |
|------|--------|-----------|
| six slots / components | B04 | B01–B03: saw the problem (vague request → wrong output) |
| specification | B04 | same |
| generic guesses | B05 | B04: slots defined, now viewer wants name for what fills them |

## Exclusion confirmation
- No chain-of-thought research: CONFIRMED absent
- No XML-tag syntax: CONFIRMED absent
- No framework comparison: CONFIRMED absent
