# FACTCHECK — vox-spec-saves-time

Source chapter: `claude-code-for-teachers/chapters/04-prompts-to-specifications.md`

## Claims verified

| Beat | Claim | Source | Status |
|---|---|---|---|
| B01 | 8-word request → 45 minutes; 90-second spec → 12 minutes | Chapter opening: "The first prompt took 8 seconds to write. The build that followed took 45 minutes... The second prompt took 90 seconds to write. The build that followed took 12 minutes." | VERIFIED |
| B02 | Claude defaults to JavaScript-rendered table, CDN font, inline styles | Chapter opening: "a JavaScript-rendered table, a CDN-loaded font, a section structure" | VERIFIED |
| B05 | Four decisions delegated to Claude: file path, CSS approach, JavaScript, dependencies | Chapter: "Each default is wrong for the class-website project" and table: file path, CSS approach, JS inclusion, external dependencies | VERIFIED |
| B06 | Five elements: operation, invariants, context, output format, negative constraint | Chapter "The five elements" section | VERIFIED |
| B07 | Example spec: Create src/syllabus.html; no JS; no CDN fonts | Chapter "Prompt vs. specification: the worked table" | VERIFIED |
| B09 | School server blocks googleapis.com (CDN) | Chapter example seed: "School server blocks googleapis.com" | VERIFIED |
| B09 | 38-minute cleanup | Chapter: "Teacher spends 38 minutes removing JS and fonts" (example seed) | VERIFIED (illustrative) |
| B10 | First time 3-5 minutes; tenth time 60-90 seconds | Chapter: "The first time you write one, it takes 3–5 minutes. By the tenth, it takes 60–90 seconds." | VERIFIED |

## Illustrative numbers (labeled)
- 8 seconds, 90 seconds, 45 minutes, 12 minutes, 38 minutes — all from chapter text or example seed; labeled as illustrative in narration.

## Terms table

| Term | Definition in film | Debut beat |
|---|---|---|
| specification | a prompt containing decisions across all five elements | B03 (shown as document), named B06 |
| five elements | operation, invariants, context, output format, negative constraint | B06 |
| negative constraint | what Claude must not do — the most under-used element | B06, example B09 |
| invariants | what must not change during a build step | B06 |

## Exclusions honored

- NO Bloom's taxonomy
- NO formal prompt engineering theory
- NO comparison of different specification formats
- NO discussion of other tools (no Copilot, no Codex)
- One mechanism: prompt delegates decisions to defaults; specification reclaims them.

## Status: VERIFIED
