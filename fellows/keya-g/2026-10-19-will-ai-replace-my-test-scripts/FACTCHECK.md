# FACTCHECK — Will AI Replace My Test Scripts?

## How this was checked

Keya allowed the web sources in `SCRIPT.md` to be fetched; local file access stayed inside `brutalist.art` and
`humanitarians-youtube`. Each verdict names the page it rests on. A claim is SUPPORTED only where a fetched page
says it. Nothing was inferred to fill a gap. Narration was **not** changed: this file only reports what the
sources do and do not say. Anything that needs a decision from Keya is in **Decisions for Keya** below.

| Source (as listed in `SCRIPT.md`) | What was actually read |
|---|---|
| Selenium, "Test practices" | Whole page. |
| Selenium, "Locator strategies" | The first part verbatim (about 40k of 129k characters); the rest through a summary only. |
| JUnit User Guide (docs.junit.org, 6.1.3) | The index and overview in full. They describe the modules and say nothing about pass or fail. Sub-pages tried for it returned 404. |
| Murilo Toloni, "Demystifying JUnit" (Medium) | **Blocked: HTTP 403.** Not read, not worked around. |
| "Introduction to Self-Healing Test Automation" (yrkan.com) | Whole page. |
| Healenium article (Medium, geekculture) | **Blocked: HTTP 403.** Not read, not worked around. Healenium's own documentation was read instead (below). |
| AI Software Testing Knowledge Resources (GitHub) | README only. It is small (6 commits, 4 stars), and several citations point to generic homepages. Many papers it lists were not opened. |
| Anthropic glossary (added) | Whole page. Used for the "different choices on different runs" line. |
| Anthropic, computer use | `platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool` (the old docs.anthropic.com address redirects there). The first ~40k of 128k characters verbatim; the rest through a summary. Items resting on the summary are marked. |

**Added by this check (not in `SCRIPT.md`'s source list; suggested for it):**

| Added source | Why | What was read |
|---|---|---|
| Selenium, "Locators" under encouraged test practices | To settle the "IDs are recommended when stable" note | Whole page. |
| Selenium, "Page object models" | The beat 5 page-object sentence | Whole page. |
| Selenium documentation home | A sentence on what Selenium is | The home page. |
| Healenium docs: "How Healenium works", Overview, Report, IntelliJ plugin | The brief: confirm how Healenium matches elements | All four pages, in full. |
| Healenium GitHub: `healenium`, `healenium-web`, `healenium-backend` | The same | READMEs and the file listing. No source code file was opened, so the algorithm itself was not read. |

**Verdicts:** SUPPORTED (a fetched page says it) · PARTLY (some of it) · SIMPLIFIED (true in outline, with detail
left out) · NOT IN SOURCES (no fetched page says it) · CONTRADICTED (a fetched page says otherwise) · OWN
EXPERIENCE (Keya's work, no outside source applies) · OWN FRAMING (Keya's explanation, not a sourced claim) ·
RHETORICAL (a question, not a claim).

## Claims, by beat

### Beat 1 — Intro

| # | Claim in the narration | Verdict | Evidence |
|---|---|---|---|
| 1 | "The voice you're hearing is an AI voice reading my script." | SUPPORTED | Narration is Kokoro `af_bella`, generated locally. Required AI-narration disclosure per `docs/FELLOWS-SUBMISSION.md`. |

### Beat 2 — Hook

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 2 | "Hi, I am Keya, and this video is about whether AI will replace my test scripts." | OWN EXPERIENCE | Keya's introduction; "my test scripts" refers to Keya's own work. |
| 3 | "At work, one of my test scripts kept failing. Not because the app was broken, but because a button's ID changed overnight." "My script looked for an ID called close button." | OWN EXPERIENCE | Keya's own project. Employer and project details are kept out, per `SCRIPT.md`. The on-screen ids are illustrative. |
| 4 | "To close a popup, I look for the X." | OWN FRAMING | A human-eye illustration of how a person finds the button. |
| 5 | "Now AI can test a website from plain English instructions." | PARTLY | Anthropic's computer use page says Claude can control a computer through screenshots, mouse and keyboard, driven by a task the developer gives it. It says nothing about *testing*. The AI Software Testing README lists tools that "see" the UI (for example askUI VisionAgent). Fine as a broad statement; it is not a measured capability. |
| 6 | "Should I be worried?" | RHETORICAL | |

### Beat 3 — Overview

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 7 | "AI won't replace testers overnight. But it will change what testers spend their time on." | OWN FRAMING | Keya's thesis. Consistent with the rest of the film, not a sourced fact. |

### Beat 4 — What testing is

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 8 | Software testing is someone checking "that every button and page works" before an app reaches you. | SIMPLIFIED | Selenium's test practices page frames testing as setting up data, performing actions and evaluating results. "Every button and page" is a plain-language simplification. |
| 9 | Doing that by hand every day "is slow," so testers write scripts "that click through the app automatically." | SIMPLIFIED | Selenium describes automating browsers (below, claim 10). "Slow" is Keya's framing; no source gives a figure, and none is shown on screen. |

### Beat 5 — Selenium and JUnit

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 10 | "Selenium is a tool that lets a script control a web browser." | SUPPORTED | Selenium docs home: "Selenium is an umbrella project for a range of tools and libraries that enable and support the automation of web browsers." and "WebDriver drives a browser natively." |
| 11 | "JUnit is the framework that runs those scripts as tests." (replaces "…reports pass or fail") | SUPPORTED (outline) | JUnit User Guide (docs.junit.org, 6.1.3): "The JUnit Platform serves as a foundation for launching testing frameworks on the JVM"; the Jupiter module "provides a TestEngine for running Jupiter based tests on the platform." It does not use the word "scripts"; Selenium scripts written as JUnit tests are the usual setup, and the beat's code shows one. The earlier pass-or-fail wording is gone. |
| 12 | "Every test does three things: find an element, act on it, then check the result." | OWN FRAMING (PARTLY) | Selenium's overview names a three-step outline ("Set up the data," "Perform a discrete set of actions," "Evaluate the results"), which differs from find, act, check. Selenium's own locators example finds an element and then asserts, without calling it a pattern. Fine as a teaching frame; not a quote from the docs. |
| 13 | "Find the login button, click it, check that the page says welcome." | OWN FRAMING | An illustrative example. The on-screen Java uses the standard JUnit 5 / Selenium WebDriver API (`findElement`, `By.id`, `click`, `getText`, `assertEquals`). It is **not executed** and is labelled so on screen. |
| 14 | "Each page's locators live in one place, called a page object." | SUPPORTED | Selenium page object models: "The locators for these elements should only be defined once." and "there is only one place in your test suite with knowledge of the structure of the HTML of a particular (part of a) page." Note the page also says page objects "should never make verifications or assertions"; the on-screen code keeps the check in the test, not in the page object. |

### Beat 6 — Why scripts break

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 15 | "Scripts find elements by locators, like an ID." | SUPPORTED | Selenium locator strategies: ID is "Locates elements whose ID attribute matches the search value." |
| 16 | In one project the IDs kept changing between builds, so Keya combined them with other attributes. | OWN EXPERIENCE | As `SCRIPT.md` notes, the problem was *unstable* IDs, not IDs in general. Selenium's locators page: "if HTML IDs are available, unique, and consistently predictable, they are the preferred method for locating an element on a page." The on-screen text does not say IDs are bad. |
| 17 | When a locator broke: investigate, find the new one, update it, run again. | OWN EXPERIENCE | |
| 18 | "Across hundreds of tests, that cycle becomes unsustainable." | SUPPORTED (wording) | yrkan: "This process multiplied across hundreds of tests becomes unsustainable." The article's percentage claims (a 36% budget share citing a 2024 report, 60–70% reductions, "up to 80%") are **not used** in the film; they are vendor or secondary figures and could not be verified. |

### Beat 7 — Self-healing locators

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 19 | "Tools like the open-source Healenium save a working locator." | SUPPORTED | Healenium, "How Healenium works": "Healenium saves a successful locator in the storage to use it as a baseline for the next test executions." Open source: Apache-2.0 on its GitHub repositories. |
| 20 | "When it breaks, they score the elements on the page, use the best match…" | SUPPORTED (for Healenium) | Same page: Healenium "catches NoSuchElement exception, triggers the LSC algorithm, passes the current page state, gets previous successful locator path, compares them, and generates the list of healed locators. It takes the locator with the highest score and performs an action with this locator." "They" generalises from Healenium to tools like it; yrkan describes confidence scoring for such tools in an illustrative sample only. |
| 21 | "…and report it, so a person can fix the script." | SUPPORTED | Healenium's report page: "Healenium generates a detailed report after each Selenium session", listing the failed locator, the healed locator and the score. Its IntelliJ plugin page: "To perform updates in the code, simply right-click on the failed locator and select the 'Healing results' action. Then, choose the new locator with the highest score." The tool does not rewrite the script by itself, which is the point of the sentence. |
| 22 | *Withdrawn.* The earlier lines about machine learning and "compare the old page structure with the new one" are no longer in the narration. | — | Not counted. |

### Beat 8 — Vision-based AI agents

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 23 | AI agents "test the way a person does." | OWN FRAMING | An analogy. Anthropic describes screenshot-plus-mouse-and-keyboard control, not "testing like a person." |
| 24 | "An AI agent takes a screenshot, finds the X by how it looks, clicks it, then takes another screenshot to check." | SUPPORTED (outline) | Anthropic computer use: Claude "provides screenshot capabilities and mouse/keyboard control"; the app returns "an image for `screenshot`" and "Steps 3 and 4, repeated without user input, form the 'agent loop'." "Finds the X by how it looks" is a plain description of vision, not a quoted line. |
| 25 | "Look, decide, act, check, again and again." | SUPPORTED (outline) | The agent loop above. The four-word names are Keya's. |
| 26 | "Selenium looks for an ID." | SUPPORTED | Selenium locators (claim 15). Selenium also supports CSS, XPath and others, so "an ID" is the example, not the only option. |

### Beat 9 — My RPA link

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 27 | "As an RPA developer, I built bots that could click on screen elements by how they looked, not just by their code." | OWN EXPERIENCE | Keya's work. For context only: the AI Software Testing README lists SikuliX, "A GUI automation tool based on image recognition," so image-based clicking is a known approach. |
| 28 | "What AI agents add is deciding what to do next." | OWN FRAMING | The Anthropic loop has Claude choose the next action (`tool_use`), which fits. |

### Beat 10 — Where AI helps

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 29 | "In my experience, it can suggest edge cases I might miss and help write test documentation…" | OWN EXPERIENCE | Marked as Keya's experience in the narration and on screen ("In my experience" stamp). The AI Software Testing README lists "AI-powered test case generation" as a topic, which is context, not proof of these two uses. |
| 30 | "…and it can keep scripts running when the page changes." | SUPPORTED | yrkan and Healenium both describe healing broken locators automatically. |
| 31 | *Merged into rows 29 and 30.* | — | Not counted. |

### Beat 11 — Where it fails

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 32 | "Every run costs money." | PARTLY | Anthropic's agent-loop sample warns about "unexpected API costs" from infinite loops. Per-run cost is a consequence of paid API use; a summary (unverified verbatim) put screenshots at roughly 1,000–1,800 tokens each. No figure is used in the film. |
| 33 | "It can make different choices on different runs." | SUPPORTED (for the model) | Anthropic glossary, "Temperature": "Even with temperature set to 0, the results will not be fully deterministic," and "identical inputs might produce different outputs across API calls." That describes the model API; applying it to a testing agent is a short step, not a measurement of any agent. |
| 34 | "It can hallucinate." | PARTLY | A summary of Anthropic's page (not verbatim) says Claude "might make mistakes or hallucinate when outputting specific coordinates." Anthropic's verbatim text also warns that Claude "follows commands found in content even when they conflict with your instructions." |
| 35 | "It can heal to the wrong button and still say the test passed." | SUPPORTED | yrkan: "The biggest risk: healing finds the *wrong* element." Its metrics include a `false_positives` counter ("Element found but wrong element"). No Healenium page says this; the claim rests on yrkan. |
| 36 | "If an AI decides both what to test and whether it passed, who checks the AI?" | RHETORICAL | Anthropic advises "Asking a human to confirm decisions that might result in meaningful real-world consequences," which agrees with the question. |

### Beats 12–14 — Verdict, Your turn, Outro

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 37 | "I don't think so." "AI is an addition to automation, not a replacement." | OWN FRAMING | Keya's conclusion. |
| 38 | "It makes my work quicker and more reliable, but a human still decides what correct looks like." | OWN EXPERIENCE | Quicker and more reliable are Keya's observations; no measured figure. |
| 39 | "Even this video was built by an AI agent, and I approved every step." | OWN EXPERIENCE | True only if Keya reviews every step. The workflow stops for her at audio, previews, both review cuts, and finals. |
| 40 | The Your Turn prompt. | SUPPORTED | The on-screen prompt is the one in `SCRIPT.md` word for word, with the last sentence ("And next time a test fails, ask…") spoken only. Selenium accepts a more stable locator such as a unique ID, as its locators page says. |
| 41 | "Built with Claude, for Humanitarians AI." | OWN EXPERIENCE | Matches the workflow: the script was drafted with Claude and approved and edited by Keya (see `SCRIPT.md`). |

**Tally (39 claims; rows 22 and 31 are withdrawn):** 16 SUPPORTED · 3 PARTLY · 0 NOT IN SOURCES · 2 SIMPLIFIED · 0 CONTRADICTED · 9 OWN EXPERIENCE · 7 OWN FRAMING · 2 RHETORICAL.

## Changes since the first check

Keya's edits are in `SCRIPT.md`, the beat sheet and this file; beats B02, B03, B07, B10 and B11 were regenerated.

- **Beat 2:** the repeated "I used to write test scripts for a living" is gone, and beat 1 no longer says it either (beat 1 now reads "Hi, I am Keya, and this video is about whether AI will replace my test scripts."); "plain English instructions" replaces "one sentence of English."
- **Beat 3:** now ends "Let's see how, step by step."
- **Beat 7:** rewritten to Healenium's own documentation. The machine-learning and "page structure" lines are gone, which removes the earlier conflict with Healenium's overview.
- **Beat 10:** marked as Keya's experience.
- **Beat 11:** "different choices on different runs" is now sourced to Anthropic's glossary.
- **Beat 5:** "reports pass or fail" replaced by "JUnit is the framework that runs those scripts as tests" (row 11), which the JUnit guide supports.

## Still open

1. **Healenium's pronunciation** is hee-LEE-nee-um (the engine default); see `PROMPTS.md`.

## Corrections applied

On screen: no figures from the yrkan article are used; no product logos; the Healenium name appears as a text label only; the beat 5 code is labelled illustrative and not run; beat 10 carries an "In my experience" stamp.
