# How Claude Skills Work: Automation vs. AI Judgment

AI narrator: Liam / Kokoro am_onyx, narrating for Deepa.

## B00 — A skill is not expertise

Can an AI assistant become an expert simply by learning a new skill? Claude Skills make AI workflows more structured, but there is an important difference between following instructions and understanding a problem. This is Liam, narrating for Deepa.

## B01 — Inside a skill

A Claude Skill is a reusable package of instructions and supporting resources for a particular task. Its SKILL dot M D file explains when to use the skill and how to approach the workflow. Some packages include scripts or reference material. These instructions guide the assistant; they do not automatically give it expert judgment.

## B02 — Web Artifacts Builder

Web Artifacts Builder guides Claude through building interactive web artifacts. It provides a structured path from setting up a project to developing and bundling the interface. That can make the work more consistent. But an interface that appears on screen still needs testing for functionality, accessibility, code quality, and a usable experience.

## B03 — Webapp Testing

Webapp Testing supports checking local web applications with Playwright. The workflow can inspect a page, exercise user interactions, and capture useful evidence such as screenshots or browser logs. Passing tests is valuable evidence about the cases tested. It is not proof that every device, unexpected input, or user journey is free of defects.

## B04 — XLSX

The XLSX skill supports spreadsheet work with tools such as pandas and openpyxl. It helps organize data, write formulas, and validate workbook outputs. Yet a formula can calculate successfully while using the wrong input or an unrealistic assumption. Technical correctness and business accuracy are different questions. Someone still needs to check what the numbers mean.

## B05 — Slack GIF Creator

Slack GIF Creator supplies guidance and utilities for creating animated GIFs for Slack. It supports frame assembly, animation concepts, and technical checks. A file can meet those checks without communicating well. Timing, readability, context, and the meaning a viewer takes away still need a thoughtful visual review.

## B06 — Automation needs judgment

Across these examples, skills can improve consistency, repeatability, and task execution. They do not automatically provide domain expertise, independent judgment, or guaranteed accuracy. Ask two questions: did the workflow run as intended, and is the result suitable for the real problem? Those are related, but they are not the same test.

## B07 — Reliable work, thoughtful review

Try this with a task you know: name one thing an automated check can verify, and one thing that still needs your judgment. AI Skills can make automation more reliable, but the quality of the outcome still depends on clear instructions, meaningful validation, and human judgment. Liam, narrating for Deepa. Humanitarians AI.
