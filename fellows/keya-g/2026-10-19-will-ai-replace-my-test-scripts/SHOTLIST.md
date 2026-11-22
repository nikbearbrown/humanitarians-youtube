# SHOTLIST — Will AI Replace My Test Scripts?

Typed work order. Fourteen beats. Narration is `SCRIPT.md` verbatim. Beat IDs B01–B11 match script sections 1–11, so
"beat 3" and "beat 7" mean the same thing here as in the script. BVDT, BHTF and BOUT are sections 12, 13 and 14.

**Status: both review cuts are built.** The 16:9 cut (`will-ai-replace-my-test-scripts-slate.mp4`) and the 9:16 cut
(`vertical/will-ai-replace-my-test-scripts-vertical-slate.mp4`) are rendered from the beat sheet, the nine Manim scenes
(`scenes.py` for 16:9, `vertical/scenes.py` for 9:16) and the narration audio, and each has passed its gates. Total
narration is 3:29 (209.1 s). Both finals are built, 16:9 at 3840×2160 and 9:16 at 2160×3840, after Keya approved the review cuts.

## Rules for every visual

- Simple illustrative graphics only: a mock web page, a popup with an ×, locators, a test's find → act → check steps,
  a look → decide → act → check loop.
- **No real product logos.** "Selenium," "JUnit" and "Healenium" appear as text labels only. No screenshots of
  commercial tools. No employer details. The ids on screen (`close-button`, `btn-4821`) are made up.
- **Code on screen must be readable.** Beat 5 shows a short JUnit 5 / Selenium test. It uses the real API and is
  labelled "Illustrative code, not run." Monospace, at least 30 px effective at 4K (and enlarged, not shrunk, in
  portrait), five lines or fewer per view, with the active line highlighted.
- **Fill the frame.** Gate V needs the content to cover at least 55% of the safe area at 50% and at 85% of each beat.
  Every scene is built big: large type, large objects, rows and columns distributed over the whole safe area, nothing
  clustered at the top. Beats are checked against the gate, not waived.
- **Portrait (9:16):** all text sits above 86% of the frame height (y < 0.86 × H); the bottom 14% stays empty. Type
  is portrait-readable, not scaled down from 16:9. 9:16 gets its own native layouts, not a crop of 16:9.
- Palette `humanitarians`: ink `#2F2A26`, terracotta `#E4572E` (one accent per beat), teal `#1F4E5F`, navy `#29335C`,
  ground `#F3EBDD`; gold `#F3A712` for fills only, never text.
- No dates on screen or in files. Un-highlighted elements never fade below about 40% opacity.
- No person icons: a person is shown by what they do (a cursor, an eye), never an icon.

## Library check

`./art scenes` was searched first, with `--reel`, for every beat's need. A hit is a lead, not a verdict.

| Need | Result |
|---|---|
| Cold open, Your Turn | **Hit:** `ClaudeComposerAsk` and `ClaudeComposerAsk916` |
| Typed and corrected overview | **Hit:** `BrutalistHesitantWriter` and `BrutalistHesitantWriter916` (props: `text`, `triggerWords`, `replacementWords`, `fontSize`, `seed`, palette) |
| Verdict page | **Hit:** `ClaudeVerdictArtifact` and `ClaudeVerdictArtifact916` |
| Outro | **Hit:** `LogoOutro` and `LogoOutro916` (same as Keya's earlier films) |
| Mock web page with a popup and an × | **Miss.** Only `DesignPipelineClaim` (mock-free design diagrams) and `HaiExplainerFig3Command` (a command mock) came back. Custom Manim. |
| Locator tags / selecting a page element | **Miss.** Hits were unrelated (`DoodleChart`, a PagerDuty teardown figure). Custom Manim. |
| Find → act → check test steps | **Miss.** `DocCoauthoringStage2/3` are flows for a different skill. Custom Manim. |
| Page object (locators in one place) | **Miss.** Custom Manim. |
| Readable test code | **Partial lead:** `MedhavyCodeBlock` / `MedhavyCodeBlock916` (Medhavy palette, light code block). Wrong palette and not tied to the beat's highlighting, so beat 5 draws its code in Manim in the `humanitarians` palette. |
| Look → decide → act → check loop | **Partial lead:** `CodingAgentsFig1Loop` (chatbot vs. coding-agent loop, a different story). Not reused; the loop here is tied to a popup and a screenshot frame. Custom Manim. |
| Self-healing: score candidates, pick closest, rewrite locator | **Miss.** Custom Manim. |
| Old page vs. new page comparison | **Miss.** Hits were decomposition trees and document trees for other films. Custom Manim. |
| Helps / fails panels | **Miss.** Custom Manim. |
| RPA bot clicking by look | **Miss.** Custom Manim. |

The search is supposed to append genuine misses to `TEMPLATE-MISSES.md` by itself. It added nothing here, because the
searches returned weak leads rather than none, so the log was not touched. Nothing was added to the component library,
so `./art scene-index` is not needed.

## Beats

| Beat | Section | Lane | Asset | What the viewer sees | Audio (s) |
|---|---|---|---|---|---|
| B01 | 1 Intro | remotion | `ClaudeComposerAsk` | Composer: "Hi, Keya"; the ask types in; three result lines (a script looks for an ID, an AI looks for the picture, who decides what correct means) | 9.19 |
| B02 | 2 Hook | manim | `B02_Hook` | A drawn web page with a popup and ×; a test row turns red while the page is fine; the button's id flips overnight; an eye marks the ×; the script's id lookup finds nothing; plain-English instructions point at the page; a large "?" | 18.50 |
| B03 | 3 Overview | remotion | `BrutalistHesitantWriter` | Types "AI will replace testers." in terracotta, deletes it, types "AI will change what testers spend their time on." in ink over three lines | 7.55 |
| B04 | 4 What testing is | manim | `B04_WhatTestingIs` | A drawn app; a cursor checks each button by hand while a calendar flips; "slow" lands; a script window takes over and the clicks run by themselves | 14.44 |
| B05 | 5 Selenium and JUnit | manim | `B05_SeleniumJunit` | Script → drawn browser ("Selenium"); framework box ("JUnit"); readable test code with FIND, ACT, CHECK lit in turn; a "page object" box gathers the locators; "Illustrative code, not run." | 22.36 |
| B06 | 6 Why scripts break | manim | `B06_WhyScriptsBreak` | A locator tag on a button; three builds with three different ids, later two red; id + text + class chips; the investigate → find → update → rerun loop; copied into a grid of a hundred tests, many red; "unsustainable" | 20.07 |
| B07 | 7 Self-healing locators | manim | `B07_SelfHealing` | A "Healenium" text label; a working locator saved; the page changes and the locator breaks; candidates get illustrative score bars (no numbers); the best match is used; a report card (broken, healed) and a cursor on the old locator line for a person to fix | 11.20 |
| B08 | 8 Vision-based AI agents | manim | `B08_VisionAgents` | Popup with ×; Selenium lane (an id, stuck); agent lane (screenshot frame, × found by look, click, second screenshot); a look → decide → act → check ring turns | 19.37 |
| B09 | 9 My RPA link | manim | `B09_RpaLink` | A bot cursor matches a button picture by its look and clicks, the code behind it greyed; a three-way fork opens and one step is chosen | 13.38 |
| B10 | 10 Where AI helps | manim | `B10_WhereAiHelps` | An "In my experience" stamp over three cards: an edge case added to a test list, a document writing itself, a test that keeps running after the page changes | 11.95 |
| B11 | 11 Where it fails | manim | `B11_WhereItFails` | Four panels: a coin meter, two different choices from one test, a made-up button, a wrong "Buy" button with a green PASS; then both arrows come from one box and "Who checks the AI?" lands | 16.77 |
| BVDT | 12 Verdict | remotion | `ClaudeVerdictArtifact` | Artifact page: title, heading "An addition, not a replacement", Keya's four verdict lines | 18.11 |
| BHTF | 13 Your turn | remotion | `ClaudeComposerAsk` | "Your turn."; the suggested prompt types in | 20.84 |
| BOUT | 14 Outro | remotion | `LogoOutro` | The Humanitarians AI mark and `@HumanitariansAI` | 5.29 |

## Open items from the audio

- **Beat 3** is now 7.55 s of speech, about 8.35 s with the 0.8 s lead silence, which clears the 8 s floor.
- **Pronunciation** is in `PROMPTS.md`.
- **Beat 3 portrait** uses `BrutalistHesitantWriter916` with larger type over more lines.
