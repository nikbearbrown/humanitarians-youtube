# FACTCHECK — Week 1 Progress

Checked against files in `humanitarians-youtube/fellows/keya-g/` and the `brutalist.art` toolkit only.
Most claims are Keya's own account of her background and week. They cannot be checked against an
outside source, so they are marked EXEMPT (personal account) and kept as written.

**Verdicts:** PASS (confirmed by the named file) · PASS, simplified (true, but the narration says less than
the full picture) · EXEMPT (personal account, Keya's own statement; not independently checkable)

**Tally:** 11 PASS · 2 PASS, simplified · 8 EXEMPT (21 claims). Nothing contradicts a file that was read.

## Sources

| Source | What it supports |
|---|---|
| `SCRIPT.md` (this folder) | The narration, verbatim |
| `keya-g/HOURS.md` | Week 1 work: onboarding, Monday and Thursday meetups, fellows website, Brutalist setup |
| anime-frames explainer `README.md` | The first video's topic and contents |
| anime-frames explainer `FRICTIONAL.md` | New to AI coding; the issues worked through (pronunciation, failed gates, portrait layouts) |
| `brutalist.art/CLAUDE.md`, `runtime/scripts/run.sh`, `runtime/scripts/compile.py`, `art` | How Brutalist builds a film; which quality gates run |
| `beat_sheet.json` (this folder) | The voice used for narration |

## Claims

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00 | The video is about Keya's first week with Humanitarians AI | PASS | `HOURS.md`, Week 1 row | — |
| 2 | B00 | The voice is an AI voice reading Keya's script | PASS | `beat_sheet.json`: Kokoro `af_bella`; narration is `SCRIPT.md` verbatim | — |
| 3 | B01 | Keya recently graduated with a master's in Software Engineering Systems | EXEMPT | Personal account (`SCRIPT.md`) | — |
| 4 | B01 | She has mostly worked in software development, as an automation developer | EXEMPT | Personal account (`SCRIPT.md`) | — |
| 5 | B01 | Her tools: Java, Python, AWS, SQL, Selenium and JUnit | EXEMPT | Personal account (`SCRIPT.md`). On screen as generic icons (code, cloud, database, browser test, unit test), not logos | — |
| 6 | B02 | Her last graduate project was VeriCode, a collaborative code review platform | EXEMPT | Personal account (`SCRIPT.md`) | — |
| 7 | B02 | She owned the review lifecycle | EXEMPT | Personal account (`SCRIPT.md`) | — |
| 8 | B02 | A state machine moves a pull request through five states, with undo | EXEMPT | Personal account (`SCRIPT.md`). The five states are shown with generic numbered labels (1–5), as Keya chose; the real state names are not shown | — |
| 9 | B02 | A rule stops authors approving their own code | EXEMPT | Personal account (`SCRIPT.md`) | — |
| 10 | B03 | She joined Humanitarians AI | PASS | `keya-g/README.md` and `HOURS.md` (Humanitarians AI trial month) | — |
| 11 | B03 | She went to the Monday and Thursday meetups | PASS | `HOURS.md`, Week 1: "Monday and Thursday meetups" | — |
| 12 | B03 | She explored the fellows website | PASS | `HOURS.md`, Week 1: "fellows website" | — |
| 13 | B03 | She started learning AI coding with the Brutalist film-as-code workflow | PASS | `HOURS.md` (Brutalist setup); explainer `FRICTIONAL.md` | — |
| 14 | B04 | Brutalist builds a video from code | PASS | `brutalist.art/CLAUDE.md`: "beat sheet → 4K master"; scenes are Manim/Remotion code | — |
| 15 | B04 | A beat sheet describes every moment | PASS | Every beat of a film is one entry in `beat_sheet.json` (narration, shot, show events) | — |
| 16 | B04 | The narration is generated first, and its timing drives every animation | PASS | `CLAUDE.md` rule 2, "Audio-first … their durations are the master clock"; `compile.py` conforms each clip to its audio | — |
| 17 | B04 | Quality checks test layout, text and facts before anything is final | PASS, simplified | Layout: Gates A, W, B, V. Text: Gate T (`type_check.py`, run by `./art final`). Facts: Gate F checks the fact-check record exists and has no unresolved verdict; the checking itself is human work (Keya's explainer `FRICTIONAL.md`: "a passing gate checks layout, not truth") | Kept as written |
| 18 | B05 | Her first video explains how AI draws the frames between an animator's drawings, and why anime is hard for it | PASS | Explainer `README.md`, "What I built" | — |
| 19 | B05 | She was completely new to AI coding; everything took time to understand | EXEMPT | Personal account; consistent with explainer `FRICTIONAL.md` ("I am new to AI coding") | — |
| 20 | B05 | The week was full of issues to work through | PASS, simplified | Explainer `FRICTIONAL.md`: setup network block, mispronounced name, gates F, L, A, B, V, T, a portrait render freeze, portrait layout fixes. On screen: three of these as cards | — |
| 21 | BOUT | The title: Week 1 Progress | PASS | `HOURS.md`: the Week 1 row lists the week 1 progress video | — |

B06 (bridge) and BOUT (title, "Built with Claude, for Humanitarians AI") are opinion and credit lines, not factual claims.

Status: checked by Claude Code; awaiting Keya's review.
