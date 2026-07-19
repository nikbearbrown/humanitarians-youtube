# PEDAGOGY — pattern-analysis-subagent

## Concept
Subagents for context isolation — delegate heavy research, receive structured summary, keep the main session clean.

## Core question
How does a subagent keep the main session context clean?

## Answer
It runs in a separate context window with a restricted tool set. Only the structured output returns to the main session — the submission files, policy docs, and intermediate reasoning stay isolated.

## Teaching pattern
- B00: concrete outcome — 48% context freed by delegation
- B01: reframe — subagent as discipline of context cleanliness
- B02-B03: build the definition — YAML frontmatter, tool whitelist, output format
- B04: test the isolation — context meter stays flat
- B05-B06: WriterReviewer pattern — accuracy improvement through fresh context
- B07: three-element summary — whitelist, output format, isolation contract
- B08: forward link to three-file system

## Bloom's level
Applying → Analyzing: students can write a subagent definition and explain why isolation improves both context management and accuracy.

## Common misconception addressed
Teachers often treat subagents as a complexity layer. The video establishes that subagents reduce complexity in the main session — the isolation is the point, not an overhead.
