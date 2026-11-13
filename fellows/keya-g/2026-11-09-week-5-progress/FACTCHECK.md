# FACTCHECK — Week 5 Progress

Checked against files in `humanitarians-youtube/fellows/keya-g/` and the `brutalist.art` toolkit only. Most claims are
Keya's own account of her week. They cannot be checked against an outside source, so they are marked EXEMPT
(personal account) and kept as written. Claims about the explainer were checked against that explainer's own files.

**Verdicts:** PASS (confirmed by the named file) · PASS, simplified (true, but the narration says less than the full
picture) · EXEMPT (personal account, not independently checkable) · **OPEN** (a file disagrees; needs Keya's decision; none now)

**Tally:** 13 PASS · 2 PASS, simplified · 5 EXEMPT · 0 OPEN (20 claims). Narration is left exactly as written.

## Sources

| Source | What it supports |
|---|---|
| `SCRIPT.md` (this folder) | The narration, verbatim |
| `keya-g/HOURS.md` | Week 5 row: week 5 progress video, watching Brutalist videos, learning how vertical differs from landscape; the explainer's title |
| `how-duolingo-decides-what-you-practice/` (`README.md`, `FACTCHECK.md`, `FRICTIONAL.md`, `SCRIPT.md`, `beat_sheet.json`, `vertical/TYPECHECK.md`) | This week's explainer: what was researched, the 12% correction, the pronunciation choices, the sync fix, the text-size measurement |
| `brutalist.art/runtime/scripts/shorts.py` | A vertical video is its own layout: generated graphics are never cut, Manim beats are re-laid-out for portrait |
| `beat_sheet.json` (this folder) | The voice used for narration |

## Claims

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | It is week five of the Brutalist project | PASS | `HOURS.md`: Week 5 row, project "Brutalist Videos" | — |
| 2 | B00 | She is learning to create videos as code | PASS | `brutalist.art/CLAUDE.md`: a film is built from a beat sheet and code (Manim, Remotion) | — |
| 3 | B00 | The voice is an AI voice reading her script | PASS | `beat_sheet.json`: engine Kokoro, voice `af_bella`; narration is `SCRIPT.md` verbatim | — |
| 4 | B01 | This week's explainer is How Duolingo Decides What You Practice Next | PASS | `HOURS.md` Week 5 STEM topic; the explainer's `README.md` | — |
| 5 | B01 | She has been learning Japanese on Duolingo for over a year | EXEMPT | Personal account. The explainer's `FRICTIONAL.md` says the same; not checkable here | — |
| 6 | B01 | She researched the forgetting curve, spaced repetition, Leitner flashcard boxes, Duolingo's blog posts and the research paper behind its model | PASS | Explainer `README.md`: "Research from the forgetting curve, spaced repetition and Leitner sources, the Duolingo blog and Birdbrain post, and the Settles & Meeder paper" | — |
| 7 | B02 | A summary said the model improved engagement by twelve percent | PASS | Explainer `README.md` and `FRICTIONAL.md`: beat 9 first said 12% from the abstract and the blog | — |
| 8 | B02 | The results table showed that number compared two versions of the same model | PASS | Explainer `FACTCHECK.md` row 9 and `SCRIPT.md`: the 12% came from a simpler half-life regression against the full one | — |
| 9 | B02 | Against the older method, the results were mixed | PASS | Explainer `SCRIPT.md`: Table 4, half-life regression against Leitner, +0.3% overall activity and a 7.3% drop in practice sessions | — |
| 10 | B02 | She took the number out | PASS | Explainer `README.md`: "The 12% was removed" | — |
| 11 | B02 | Now she checks what a number is compared against, not just the headline | EXEMPT | Her own habit going forward | — |
| 12 | B03 | The narration is the same in vertical, but a squeezed landscape layout does not work on a phone; each vertical scene needs its own design: one idea at a time, stacked top to bottom, with bigger text | PASS, simplified | `shorts.py`: generated graphics are never cut or squeezed; each Manim beat is re-laid-out natively for portrait. "One idea at a time, bigger text" is her own design rule | — |
| 13 | B04 | Claude Code first gave a wrong figure for the vertical text size | PASS | Explainer `FRICTIONAL.md`: "Claude Code's first claim about portrait text size turned out to be wrong" | — |
| 14 | B04 | She asked it to measure the real frames | PASS | Explainer `FRICTIONAL.md`: "asked for the real text height to be measured" | — |
| 15 | B04 | Every scene's text was above her seventy-two pixel rule | PASS (resolved) | Keya changed the line from a specific figure to this claim. The explainer's `vertical/TYPECHECK.md` lists the smallest text-run height of every body beat (lowest 80 px, B07) at or above the 72 px floor; the bookend beats are hand-drawn patterns that Gate T does not measure as text. This film's own vertical `TYPECHECK.md` also passes, with a lowest text-run of 84 px | Earlier OPEN item (84 px against a later 80 px) is closed by the new wording. Narration follows `SCRIPT.md` exactly |
| 16 | B05 | She picked how to say shimasu, mimasu and Leitner by ear, from test clips | PASS, simplified | Explainer `README.md`: pronunciations chosen by ear from test clips (shimasu and mimasu option B, Leitner as "LITE-ner"); the choice itself is hers | — |
| 17 | B05 | While watching the previews she noticed the typing and the voice were out of sync in one scene, and got it fixed | PASS | Explainer `FRICTIONAL.md` and `beat_sheet.json` B03 note: lead silence removed so voice and typing start together | — |
| 18 | B06 | She kept watching Brutalist videos and looked at what topics other fellows cover, to find topics of her own | EXEMPT | `HOURS.md` Week 5: "watching Brutalist videos". The reasons and what she looked at are her account | — |
| 19 | B07 | A number needs its comparison, a vertical video needs its own layout, a claim needs a measurement | EXEMPT | Her own conclusion, drawn from claims 7-15 | — |
| 20 | BOUT | "Week 5 Progress. Built with Claude, for Humanitarians AI." | EXEMPT | Sign-off, no factual claim | — |

## Notes

- No claim was changed by the fact check. The narration is Keya's script exactly. Row 15 was open until Keya reworded the line; it is now resolved.
- Every number drawn on screen (12%, 72 px) comes from the script. Bars, meters and the ruler are illustrations, not data.
- No Duolingo logo, owl or branding appears. The app is shown only as a generic drawn phone.
