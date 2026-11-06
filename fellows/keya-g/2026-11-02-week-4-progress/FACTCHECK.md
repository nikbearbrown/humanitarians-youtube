# FACTCHECK — Week 4 Progress

Checked against files in `humanitarians-youtube/fellows/keya-g/` and the `brutalist.art` toolkit only.
Most claims are Keya's own account of her week. They cannot be checked against an outside source, so they
are marked EXEMPT (personal account) and kept as written. Claims about how Brutalist works were checked
against the toolkit's own files.

**Verdicts:** PASS (confirmed by the named file) · PASS, simplified (true, but the narration says less than
the full picture) · EXEMPT (personal account, Keya's own statement; not independently checkable)

**Tally:** 16 PASS · 3 PASS, simplified · 2 EXEMPT (21 claims). Nothing contradicts a file that was read.

## Sources

| Source | What it supports |
|---|---|
| `SCRIPT.md` (this folder) | The narration, verbatim |
| `keya-g/HOURS.md` | Week 4 row: Week 4 progress video, watching and reviewing Brutalist videos; the Japanese explainer as the week's STEM video; the Week 1 anime explainer as the first |
| `how-your-phone-types-japanese/README.md` and `FRICTIONAL.md` (keya-g folder) | This week's explainer: title, research, script, Claude Code build, what was learned from reviews |
| `how-your-phone-types-japanese/FACTCHECK.md` (keya-g folder) | The claim-by-claim record that review of that video produced |
| `brutalist.art/CLAUDE.md`, `runtime/scripts/run.sh`, `runtime/scripts/compile.py`, `art` | How a film is built; which gates run; the verification receipt and its SHA-256 |
| `brutalist.art/docs/PIPELINE-SAFETY.md`, `docs/FELLOWS-SUBMISSION.md` | What a final requires; that gate switches cannot authorize a final; that each export's SHA-256 is recorded |
| `beat_sheet.json` (this folder) | The voice used for narration |

## Claims

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | Keya is in week four of the Brutalist project | PASS | `HOURS.md`: Week 4 row, project "Brutalist Videos" | — |
| 2 | B00 | She is learning to create videos as code | PASS | `CLAUDE.md`: a film is built from a beat sheet and code (Manim, Remotion); Week 1 README: "film-as-code workflow" | — |
| 3 | B00 | The voice is an AI voice reading Keya's script | PASS | `beat_sheet.json`: Kokoro `af_bella`; narration is `SCRIPT.md` verbatim | — |
| 4 | B01 | This week's explainer is How Your Phone Types Japanese | PASS | `HOURS.md`: the Week 1 STEM video is the anime explainer, the Week 4 STEM video is the Japanese one | — |
| 5 | B01 | The explainer is called How Your Phone Types Japanese | PASS | Japanese explainer `README.md` and beat sheet title | — |
| 6 | B01 | She researched how Japanese keyboards guess which kanji you mean | PASS | Explainer `README.md` ("the keyboard is predicting, not converting"); `FRICTIONAL.md`, "Topic and research" | — |
| 7 | B01 | She wrote the script | PASS | Explainer `FRICTIONAL.md`, "Script and fact check"; `README.md` lists her story order, hook and takeaway as her decisions | — |
| 8 | B01 | She built the video with Claude Code | PASS | Explainer `README.md`, "Human and AI work": Claude Code wrote the beat sheets, scenes, paperwork and ran the builds with her approval | — |
| 9 | B02 | She spent time watching Brutalist videos | PASS | `HOURS.md`, Week 4: "watching and reviewing Brutalist videos" | — |
| 10 | B02 | A video is reviewed by checking each claim against its sources | PASS | Explainer `FRICTIONAL.md`: "each claim needs a source that actually says it"; the claim-by-claim `FACTCHECK.md` is that record | — |
| 11 | B02 | A video is reviewed by watching every scene with its narration | PASS, simplified | Explainer `FRICTIONAL.md`: previews with audio were needed to check sync, and the real review cut had to be watched. Keya's account of how review works; the toolkit also requires frame inspection (`CLAUDE.md` rule 4) | Kept as written |
| 12 | B03 | Every Brutalist video has to pass quality gates before it is final | PASS | `docs/PIPELINE-SAFETY.md`: a final requires the gate checks; `art final` runs Gate T before the clean master | — |
| 13 | B03 | The gates test layout, text size, contrast and facts | PASS, simplified | Layout: Gates A, B, V. Text size and contrast: Gates T and W. Facts: Gate F checks that the fact-check record exists and has no unresolved verdict; checking the facts themselves is human work (explainer `FRICTIONAL.md`: "gates can't tell placeholder text from my own") | Kept as written |
| 14 | B03 | When a gate fails, you fix the scene and render it again | PASS | `run.sh`: "Fix the scene source and re-run"; explainer `FRICTIONAL.md`: Gate V failed on almost every scene and the scenes were redesigned | — |
| 15 | B03 | You never switch the check off | PASS | `docs/PIPELINE-SAFETY.md`: `ART_QC=0`, `ART_FACTS=0`, lenient settings and `--allow-slates` cannot authorize a final. Also Keya's working rule for this project | — |
| 16 | B04 | Each final video gets a checksum, a fingerprint of the file | PASS | `compile.py`: a successful final writes a `.verified.json` receipt with the output's SHA-256; `FELLOWS-SUBMISSION.md`: record each export's SHA-256 | — |
| 17 | B04 | Anyone can use it to confirm the video on Drive is the same one that passed the gates | PASS, simplified | `PIPELINE-SAFETY.md`: "Match the hash to the media, not merely the filename." A matching SHA-256 proves the same bytes; "passed the gates" holds because the receipt is written only after the final checks pass. The hash must be shared (the README lists it). On screen the fingerprint is a drawn pattern, not a real hash | Kept as written |
| 18 | B05 | A complete folder needs every part: script, beat sheet, fact check, scenes, write-up | PASS | `run.sh` Gate F: no render without `FACTCHECK.md`, `SHOTLIST.md` and `PROMPTS.md`; the sheet and scenes are required to render; `FELLOWS-SUBMISSION.md` requires a README write-up. Keya's learning | — |
| 19 | B05 | She has become much better at working with Claude Code in the terminal | EXEMPT | Personal account (`SCRIPT.md`) | — |
| 20 | B05 | Humanitarians AI helped her learn that work smoothly | EXEMPT | Personal account (`SCRIPT.md`) | — |
| 21 | BOUT | The title: Week 4 Progress | PASS | `HOURS.md`: the Week 4 row lists the Week 4 progress video | — |

Claims 12 to 17 rest on the toolkit's own files and documentation, not on a fresh test run for this video.
The two EXEMPT claims (19, 20) are Keya's own statements about her progress and the programme. The BOUT credit
line ("Built with Claude, for Humanitarians AI") is a credit, not a factual claim.

Status: checked by Claude Code; awaiting Keya's review.
