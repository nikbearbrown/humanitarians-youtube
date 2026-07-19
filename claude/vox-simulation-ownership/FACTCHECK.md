# FACTCHECK — vox-simulation-ownership

Source chapter: `claude-code-for-teachers/chapters/12-three-file-system.md`

## Claims verified

| Beat | Claim | Source | Status |
|---|---|---|---|
| B01 | "build me an interactive sorting algorithm simulator" — one line; loop ran ~8 minutes | Chapter opening: "The teacher opened Claude Code in a fresh project directory and typed: build me an interactive sorting algorithm simulator. The agentic loop ran for about eight minutes." | VERIFIED (verbatim) |
| B01 | Result "worked" but "was not theirs" | Chapter: "It worked. It also was not theirs." | VERIFIED (verbatim) |
| B02 | Material Design default palette — bright blue, white, gray | Chapter: "The color scheme was Material Design's default palette — bright blue, white, gray." | VERIFIED (verbatim) |
| B02 | Teacher's class website used four earth tones | Chapter: "The teacher's class website used four earth tones" | VERIFIED |
| B02 | Interaction model was drag-and-drop; teacher wanted single-click stepping | Chapter: "The interaction model was drag-and-drop — the teacher had wanted single-click stepping." | VERIFIED |
| B02 | Pedagogical scaffolding missing | Chapter: "The pedagogical scaffolding (what each color meant, why the algorithm slowed down on certain inputs, what the comparison count was telling the student) was missing." | VERIFIED |
| B04 | One line of intent → Claude fills everything else with defaults | Chapter: "Claude had filled in everything else with defaults." | VERIFIED |
| B05 | Three-file system: CLAUDE.md (technical), DESIGN.md (visual), PROJECT.md (pedagogical/intent) | Chapter section "The three files" | VERIFIED |
| B07 | Six named colors; escalate if a seventh seems necessary | Chapter DESIGN.md sample: "If a sixth color seems necessary, escalate to the human; do not invent." | VERIFIED (verbatim) |
| B07 | Color roles: warm white, near-black, terracotta, blue, gray, amber | Chapter DESIGN.md sample: exact hex values and roles listed | VERIFIED |
| B08 | 45-minute test: CLAUDE.md 15 min, DESIGN.md 15 min, PROJECT.md 15 min | Chapter: "CLAUDE.md (15 minutes; mostly refined from /init), DESIGN.md (15 minutes; the six-color rule forces decision), PROJECT.md (15 minutes; Intent Layer first)" | VERIFIED (verbatim) |
| B08 | Over 45 minutes → scope down | Chapter: "A simulation that requires three hours of file-writing is a simulation with too many decisions for one build. Decompose." | VERIFIED |

## Terms table

| Term | Definition in film | Debut beat |
|---|---|---|
| three-file system | CLAUDE.md + DESIGN.md + PROJECT.md; written before code generation | B05 |
| CLAUDE.md | Technical constitution: stack, file structure, never-touch | B05 |
| DESIGN.md | Visual constitution: six named colors, interaction vocabulary, never-list | B05, B07 |
| PROJECT.md Intent Layer | Pedagogical contract: what students understand, questions answered/refused | B05 |
| 45-minute test | If you cannot write all three files in 45 minutes, scope is too large | B08 |

## Exclusions honored

- NO Brutalist design system history
- NO CSS custom properties tutorial
- NO comparison with other design systems (designmd.app, getdesign.md)
- NO full six-principle framework
- One mechanism: one-line prompt delegates all decisions to Claude's defaults; three-file system moves decisions to explicit human choices before generation.

## Status: VERIFIED
