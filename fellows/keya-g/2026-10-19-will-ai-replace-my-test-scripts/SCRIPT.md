# Will AI Replace My Test Scripts? — Script

**Fellow:** Keya G. · **Week 2** · **Voice:** Kokoro `af_bella` · **Pronounce:** Keya = kˈeɪjɛə ("Kay-yeah")

Story plan, topic, research and decisions: Keya. Example script drafted with Claude from Keya's story plan, research notes and work experience; Keya approved and edited it.
Visuals: simple illustrative graphics only (a mock web page, a popup with an ×, locators, a test's find→act→check steps, a look→decide→act→check loop). No real product logos, no screenshots of commercial tools, and no details of any employer's project.

## 1. Intro
Hi, I am Keya, and this video is about whether AI will replace my test scripts. The voice you’re hearing is an AI voice reading my script.

## 2. Hook
At work, one of my test scripts kept failing. Not because the app was broken, but because a button's ID changed overnight. To close a popup, I look for the X. My script looked for an ID called close button. Now AI can test a website from plain English instructions. Should I be worried?

## 3. Overview
On screen, typed then corrected: "AI will replace testers." → "AI will change what testers spend their time on."

AI won't replace testers overnight. But it will change what testers spend their time on. Let's see how, step by step.

## 4. What testing is
First, what is software testing? Before an app reaches you, someone checks that every button and page works. Doing that by hand, every day, is slow. So testers write test scripts: small programs that click through the app automatically.

## 5. Selenium and JUnit
Selenium is a tool that lets a script control a web browser. JUnit is the framework that runs those scripts as tests. Every test does three things: find an element, act on it, then check the result. Find the login button, click it, check that the page says welcome. To keep things tidy, each page's locators live in one place, called a page object.
`[Selenium docs; JUnit docs]`

## 6. Why scripts break
Scripts find elements by locators, like an ID. In one project, the IDs kept changing between builds, so I had to combine them with other attributes. Every time a locator broke, I had to investigate, find the new one, update it and run the test again. Across hundreds of tests, that cycle becomes unsustainable.
`[Keya's experience; self-healing tests intro]`

## 7. Self-healing locators
Tools like the open-source Healenium save a working locator. When it breaks, they score the elements on the page, use the best match, and report it, so a person can fix the script.
`[Healenium docs]`

## 8. Vision-based AI agents
Vision-based AI agents go further. They test the way a person does. To close a popup, I look for the X. Selenium looks for an ID. An AI agent takes a screenshot, finds the X by how it looks, clicks it, then takes another screenshot to check. Look, decide, act, check, again and again.
`[Anthropic computer use]`

## 9. My RPA link
This idea isn't completely new to me. As an RPA developer, I built bots that could click on screen elements by how they looked, not just by their code. What AI agents add is deciding what to do next.
`[Keya's experience]`

## 10. Where AI helps
AI is genuinely useful here. In my experience, it can suggest edge cases I might miss and help write test documentation, and it can keep scripts running when the page changes.
`[Keya's experience]`

## 11. Where it fails
But it has limits. Every run costs money. It can make different choices on different runs. It can hallucinate, and worst of all, it can heal to the wrong button and still say the test passed. And if an AI decides both what to test and whether it passed, who checks the AI?
`[Anthropic glossary: temperature]`

## 12. Verdict
So, will AI replace my test scripts? I don't think so. AI is an addition to automation, not a replacement. It makes my work quicker and more reliable, but a human still decides what correct looks like. Even this video was built by an AI agent, and I approved every step.

## 13. Your turn
Your turn. Paste this into Claude: Here's a Selenium test with a fragile locator. Suggest a more stable one, and explain what a self-healing tool and an AI testing agent would each do if it broke, using closing a popup as the example. And next time a test fails, ask: did the app break, or did the page just change?

Prompt shown on screen: "Here's a Selenium test with a fragile locator. Suggest a more stable one, and explain what a self-healing tool and an AI testing agent would each do if it broke, using closing a popup as the example."

## 14. Outro
Will AI Replace My Test Scripts? Built with Claude, for Humanitarians AI.

## Notes for the fact check
- Beats 6 and 9 are Keya's own work experience; keep employer names and project details out.
- Selenium's docs recommend IDs when they are stable; the problem in beat 6 was unstable IDs, not IDs in general.
- Beat 7 now follows Healenium's own documentation: it saves a working locator, scores elements when it breaks, uses the best match and reports it. It no longer says "page structure", "machine learning" or that the locator updates itself.
- Beat 10 is marked as Keya's own experience.

## Sources
- Selenium, "Test practices" — https://www.selenium.dev/documentation/test_practices/overview/
- Selenium, "Locator strategies" — https://www.selenium.dev/documentation/webdriver/elements/locators/
- JUnit User Guide, overview — https://docs.junit.org/6.1.3/overview.html
- Murilo Toloni, "Demystifying JUnit" (Medium) — https://medium.com/@murilo.g.toloni/demystifying-junit-how-it-works-behind-the-scenes-and-why-its-a-framework-ac9fe09a63f2
- "Introduction to Self-Healing Test Automation" — https://yrkan.com/blog/self-healing-tests/
- Healenium, self-healing library for Selenium — https://medium.com/geekculture/healenium-self-healing-library-for-selenium-test-automation-26c2358629c5
- AI Software Testing Knowledge Resources (GitHub) — https://github.com/aidriventesting/AI-Software-Testing-Knowledge-Resources
- Healenium docs, "How Healenium works" and "Report" — https://healenium.io/docs/how_healenium_works
- Anthropic glossary, "Temperature" — https://platform.claude.com/docs/en/about-claude/glossary
- Anthropic, computer use (Claude operating a computer through screenshots, mouse and keyboard) — search "Anthropic computer use" for the official page
