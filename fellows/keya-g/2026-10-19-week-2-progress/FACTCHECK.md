# FACTCHECK — Week 2 Progress

Checked against files in `humanitarians-youtube/fellows/keya-g/` and the `brutalist.art` toolkit only. Most claims are
Keya's own account of her week. They cannot be checked against an outside source, so they are marked EXEMPT
(personal account) and kept as written. Claims about how Brutalist works were checked against the toolkit's own files.

**Verdicts:** PASS (confirmed by the named file) · PASS, simplified (true, but the narration says less than the full
picture) · EXEMPT (personal account, Keya's own statement; not independently checkable)

**Tally:** 11 PASS · 2 PASS, simplified · 10 EXEMPT (23 claims). Nothing contradicts a file that was read.

## Sources

| Source | What it supports |
|---|---|
| `SCRIPT.md` (this folder) | The narration, verbatim |
| `keya-g/HOURS.md` | Week 2 row: week 2 progress video, checking Brutalist videos, choosing topics; the STEM topic "Will AI Replace My Test Scripts?" |
| `will-ai-replace-my-test-scripts/` (keya-g folder: `README.md`, `FACTCHECK.md`, `SHOTLIST.md`) | This week's explainer: title, its subjects (Selenium, self-healing locators, vision-based testing agents), how it was built |
| `brutalist.art/CLAUDE.md`, `runtime/scripts/run.sh`, `runtime/scripts/remotion_scenes.py` | A film is built from a beat sheet and code; audio durations are the master clock; the gates; the `ART_CHROME` browser override |
| `brutalist.art/docs/PIPELINE-SAFETY.md` | A command's success is not the result; `build-state.json` records `failed`, `blocked` or `ready`; an older file is not the new result |
| `beat_sheet.json` (this folder) | The voice used for narration |

## Claims

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | Keya is in week two of the Brutalist project | PASS | `HOURS.md`: Week 2 row, project "Brutalist Videos" | — |
| 2 | B00 | She is learning to create videos as code | PASS | `CLAUDE.md`: a film is built from a beat sheet and code (Manim, Remotion) | — |
| 3 | B00 | The voice is an AI voice reading her script | PASS | `beat_sheet.json`: engine Kokoro, voice `af_bella`; narration is `SCRIPT.md` verbatim | — |
| 4 | B01 | This week's explainer is "Will AI Replace My Test Scripts?" | PASS | `HOURS.md` Week 2 STEM topic; the explainer folder's `README.md` | — |
| 5 | B01 | It comes from her own work writing Selenium tests | EXEMPT | Personal account of her own work. The explainer is about Selenium tests, which fits; the work history itself is not checkable here | — |
| 6 | B01 | She researched self-healing locators and AI testing agents | PASS | The explainer's `FACTCHECK.md` and `SHOTLIST.md` cover self-healing locators (beat 7) and vision-based agents (beat 8) | — |
| 7 | B01 | She wrote the script and built the video with Claude Code | PASS, simplified | The explainer folder holds her `SCRIPT.md` and the build was done with Claude Code in this toolkit; the narration does not say how the work was split | — |
| 8 | B01 | She also checked some Brutalist videos | PASS | `HOURS.md` Week 2: "checking Brutalist videos" | — |
| 9 | B01 | She spent time choosing topics that matter to her and interest her | PASS | `HOURS.md` Week 2: "choosing topics" (the reasons are hers) | — |
| 10 | B02 | In the first days her Manim scenes kept failing the quality checks | EXEMPT | Personal account. The checks exist (`run.sh` gates A, W, B, V, T) | — |
| 11 | B02 | The failures were code that wouldn't run, labels outside the safe area and frames that were too empty | EXEMPT | Personal account of what failed. Each kind has a matching gate: scene checks, margin check, fill check | — |
| 12 | B02 | Some Remotion renders froze for over an hour | EXEMPT | Personal account of her own renders | — |
| 13 | B02 | They fixed each scene instead of switching the checks off | PASS | `PIPELINE-SAFETY.md`: `ART_QC=0`, `ART_FACTS=0` and lenient settings cannot authorize a final | — |
| 14 | B02 | Remotion ran with a different browser and a time limit | EXEMPT | Keya's own build experience: the time limit came from the Playwright wrapper in the scratchpad, not a toolkit setting. (The toolkit does support a different browser through `ART_CHROME`.) | — |
| 15 | B03 | The script holds her words; the beat sheet times every moment; the fact check ties each claim to a source; the build state records whether the video really passed | PASS, simplified | Folder files: `SCRIPT.md`, `beat_sheet.json` (narration durations are the clock), `FACTCHECK.md`, `build-state.json`. The narration names the roles in plain words | — |
| 16 | B04 | A command that says done, or even pass, isn't proof | PASS | `PIPELINE-SAFETY.md`: "that older file is not the new result" | — |
| 17 | B04 | Once, a pass came from old frames | EXEMPT | Personal account of what happened to her; consistent with the same file's warning about stale media | — |
| 18 | B04 | `build-state.json` records the real result | PASS | `PIPELINE-SAFETY.md`: check `build-state.json` for `failed` or `blocked`; `run.sh` and `compile.py` write its status | — |
| 19 | B05 | She changed her intro line near the end, so only that beat needed new audio and a new render; the rest stayed the same | PASS | `CLAUDE.md` rule 2: narration durations are the master clock, audio is regenerated per beat, then recompiled | — |
| 20 | B06 | The hard part was coding with AI in the terminal: prompting clearly, and understanding each step instead of just approving | EXEMPT | Personal account | — |
| 21 | B06 | It's only week two and she's still learning | EXEMPT | Personal account | — |
| 22 | B07 | Like the testing agents in her video, Claude Code does the work, but she decides what correct looks like | EXEMPT | Her own conclusion. The explainer's verdict is the same idea (an addition, not a replacement) | — |
| 23 | BOUT | "Week 2 Progress. Built with Claude, for Humanitarians AI." | EXEMPT | Sign-off, no factual claim | — |

## Notes

- No claim was changed. The narration is Keya's script exactly.
