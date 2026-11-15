# FACTCHECK — Week 3 Progress

Checked against files in `humanitarians-youtube/fellows/keya-g/` and the `brutalist.art` toolkit only. Most claims are
Keya's own account of her week. They cannot be checked against an outside source, so they are marked EXEMPT
(personal account) and kept as written. Claims about the explainer were checked against that explainer's own files.

**Verdicts:** PASS (confirmed by the named file) · PASS, simplified (true, but the narration says less than the full
picture) · EXEMPT (personal account or opinion, not independently checkable) · **OPEN** (a file disagrees; needs Keya's decision; none now)

**Tally:** 10 PASS · 3 PASS, simplified · 9 EXEMPT · 0 OPEN (22 claims). Narration is left exactly as written.

## Sources

| Source | What it supports |
|---|---|
| `SCRIPT.md` (this folder) | The narration, verbatim |
| `keya-g/HOURS.md` | Week 3 row: week 3 progress video, going through Brutalist videos and the film-as-code workflow, researching and choosing topics, learning how scripts and fact checks work; the explainer's title |
| `how-google-docs-lets-two-people-type/` (`README.md`, `FRICTIONAL.md`, `SCRIPT.md`, `FACTCHECK.md`, `beat_sheet.json`) | This week's explainer: its title, how the topic was chosen, the script's beat-by-beat form with sources, the fact check, the verdict line "shifted, ordered and shared" |
| `brutalist.art/CLAUDE.md` | A film is built from a beat sheet and code (Manim, Remotion) |
| `brutalist.art/docs/PIPELINE-SAFETY.md` | Final export requires a nonempty `FACTCHECK.md` |
| `beat_sheet.json` (this folder) | The voice used for narration |

## Claims

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | It is week three of the Brutalist project | PASS | `HOURS.md`: Week 3 row, project "Brutalist Videos" | — |
| 2 | B00 | She is learning film as code | PASS | `HOURS.md` Week 3: "the film-as-code workflow"; `brutalist.art/CLAUDE.md`: a film is built from a beat sheet and code (Manim, Remotion) | — |
| 3 | B00 | The voice is an AI voice reading her script | PASS | `beat_sheet.json`: engine Kokoro, voice `af_bella`; narration is `SCRIPT.md` verbatim | — |
| 4 | B01 | This week's explainer is How Google Docs Lets Two People Type in the Same Sentence | PASS | `HOURS.md` Week 3 STEM topic; the explainer's `README.md` | — |
| 5 | B01 | She uses shared documents every day | EXEMPT | Personal account. The explainer's `README.md` and `FRICTIONAL.md` also call it a tool she uses every day, but it is not checkable here | — |
| 6 | B01 | She had never looked at what happens behind shared documents | EXEMPT | Personal account | — |
| 7 | B01 | Understanding that backend was the most interesting part of her week | EXEMPT | Her own view | — |
| 8 | B02 | She is still learning the film as code workflow, one part at a time | EXEMPT | Personal account. `HOURS.md` Week 3 lists "the film-as-code workflow" as work done | — |
| 9 | B02 | In the first few days she went through Brutalist videos and worked out how each piece fits together | PASS, simplified | `HOURS.md` Week 3: "going through Brutalist videos and the film-as-code workflow". "The first few days" and "how each piece fits" are her own account | — |
| 10 | B03 | She spent time researching topics, understanding some and discarding others | PASS, simplified | `HOURS.md` Week 3: "researching and choosing topics". Which ones she kept or dropped is her own account | — |
| 11 | B03 | She looked at what other fellows have already made | PASS | Explainer `README.md`: "I looked at what topics other fellows had made, then chose this one" | — |
| 12 | B03 | She asked how a topic could connect AI or STEM with her own interests | EXEMPT | Her own method. The explainer's `FRICTIONAL.md` says she chose a system design topic about a tool she uses every day that fits her software background | — |
| 13 | B04 | She learned that the script is the source of every video | PASS, simplified | `beat_sheet.json` of the explainer and this film: `derived_from` is `SCRIPT.md`, and narration is the script verbatim. "Every video" is her description of this workflow | — |
| 14 | B04 | The script holds her words beat by beat, with the sources behind them | PASS | Explainer `SCRIPT.md`: one numbered section per beat, each followed by a bracketed source note (for example the Google Drive blog and Wikipedia) | — |
| 15 | B04 | She learned how fact checks work: every claim is checked against a source | PASS | Explainer `FACTCHECK.md`: every claim has a row with a verdict and the source it rests on | — |
| 16 | B04 | The fact check is an important part of the quality gates | PASS | `brutalist.art/docs/PIPELINE-SAFETY.md`: final export requires a nonempty `FACTCHECK.md` | — |
| 17 | B05 | Understanding the topic was not especially hard this week, because Google Docs is a tool she already uses | EXEMPT | Personal account. The line now says "Understanding the topic", so it is about the subject, not the build; the explainer's `FRICTIONAL.md` does record build snags (frozen renders, text overlap), which this wording does not contradict. Kept as written | — |
| 18 | B05 | Learning what happens underneath, how every change is shifted, ordered and shared | PASS | Explainer `SCRIPT.md` verdict beat: "Behind every keystroke, changes are shifted, ordered and shared" | — |
| 19 | B05 | It made a familiar tool feel new | EXEMPT | Her own view | — |
| 20 | B06 | The tools she uses every day hide some of the most interesting engineering | EXEMPT | Her own conclusion, drawn from claim 18 | — |
| 21 | B06 | This week she learned to look behind them | EXEMPT | Her own conclusion | — |
| 22 | BOUT | "Week 3 Progress. Built with Claude, for Humanitarians AI." | PASS | Matches the sign-off pattern of her other progress videos; the title matches the folder name | — |

## Notes

- No claim was changed by the fact check. The narration is Keya's script exactly.
- Nothing shown on screen carries a number or data. Every shape is an illustration of what the script says.
- No Google logo, Docs screenshot or branding appears. A shared document is drawn as a generic page of plain lines with
  two cursors. The explainer's title appears only as plain text, because the narration says it.
