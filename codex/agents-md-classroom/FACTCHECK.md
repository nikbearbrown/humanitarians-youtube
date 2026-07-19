# FACTCHECK — agents-md-classroom
**Build an AGENTS.md with Claude: Teach the AI Your Classroom Rules**
Source: `codex-for-teachers/chapters/03-agents-md.md`

---

## Claims audit

| # | Beat | Claim | Verdict | Source / Note |
|---|------|-------|---------|---------------|
| 1 | B00 | A 100-line markdown document outperforms a 30-minute calibration session because it survives the session | ✓ | Chapter thesis: AGENTS.md persists across sessions; oral calibration is session-scoped and evaporates. Framing consistent with chapter. |
| 2 | B01 | Codex starts every session with no memory of the last | ✓ | Standard Claude Codex behavior: stateless context window per session. No cross-session memory by default. |
| 3 | B01 | 200-line operational ceiling for AGENTS.md | ✓ | Chapter names the 200-line constraint explicitly as a practical and pedagogical limit. |
| 4 | B04 | 147 lines, all 5 sections present | SYNTHETIC | Illustrative scenario. The specific line count (147) is a plausible example consistent with the chapter's guidance — a well-structured 5-section AGENTS.md for a small class project typically falls in the 120–180 line range. Marked synthetic. |
| 5 | B04 | Never rules are specific: "never add a build step that requires Node.js," etc. | SYNTHETIC | Specific never-rules are illustrative examples consistent with chapter guidance on machine-specific quirks and environment constraints. The form is correct; the specific text is synthetic. |
| 6 | B06 | AGENTS.override.md takes precedence over AGENTS.md | ✓ | Chapter hierarchy: project-level overrides supersede base AGENTS.md for conflicting rules. The precedence mechanism is correctly stated. |
| 7 | B01/B07 | 200-line constraint forces you to decide what actually matters | ✓ | Chapter: the ceiling is a discipline device, not just a technical limit. Consistent with chapter framing. |

---

## Exclusions confirmed
- No discussion of AGENTS.md format variants or alternative naming conventions
- No multi-agent coordination scenarios
- No git-based workflow for AGENTS.md versioning

## Synthetic scenarios
All build outputs (line counts, specific never-rules, override behavior) are illustrative scenarios consistent with the source chapter. They are not transcripts of actual Claude sessions. Synthetic content is clearly presented as "generated output" within the video and is consistent with the chapter's guidance and examples.
