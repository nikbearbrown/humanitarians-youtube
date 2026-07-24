# SOURCES — How We Claude Code

## Primary source

**Anthropic CWC Workshop — How We Claude Code**
`books/anthropics/cwc-workshops/how-we-claude-code/`
Copyright 2026 Anthropic PBC. Apache-2.0 License.

| Phase | File |
|---|---|
| Phase 1 — Interview prompt | `phase-1-exploration/PROMPT.MD` |
| Phase 2 — Design directions prompt | `phase-2-planning/PROMPT.MD` |
| Phase 3 — Verifiable React README | `phase-3-verify/README.md` |

## Key claims and their sources

| Claim | Source |
|---|---|
| Phase 1 uses AskUserQuestion tool to interview | `phase-1-exploration/PROMPT.MD` — "interview me in-depth using the AskUserQuestion tool" |
| Phase 2 generates 4 static HTML mockups | `phase-2-planning/PROMPT.MD` — "Explore 4 different designs, and create a set of HTML files" |
| Phase 3 uses data-verify-* DOM contracts | `phase-3-verify/README.md` — "every component emits data-verify-* attributes" |
| `bun run verify` runs verification matrix | `phase-3-verify/README.md` — "run the verification matrix headlessly" |
| Failing probe is designed to fail | `phase-3-verify/README.md` — "TodoStats/inconsistent-counts is a probe that is DESIGNED to fail" |

## Build

- Channel: claude-liam (@HumanitariansAI)
- Voice: Kokoro af_kore (free, local)
- Built: 2026-07-16
- Runtime: ~95s (7 beats, B00–B06)
- Resolution: 1920×1080, 30fps
