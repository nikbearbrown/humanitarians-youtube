# FACTCHECK — five-element-specification
**Build a Five-Element Specification with Claude: Stop Prompting, Start Conducting**
Source: `codex-for-teachers/chapters/04-prompts-to-specifications.md`

---

## Claims audit

| # | Beat | Claim | Verdict | Source / Note |
|---|------|-------|---------|---------------|
| 1 | B00 | A request gives Codex a target; a specification gives it constraints | ✓ | Chapter core distinction: prompts vs. specifications. The framing is the chapter's central thesis. |
| 2 | B01 | Without a specification, Codex uses defaults — most common interpretation, typical file structure, frequent library choice | ✓ | Chapter: Codex defaults to the most common pattern in its training distribution without explicit constraints. |
| 3 | B01 | The specification replaces defaults with your decision | ✓ | Chapter: the five elements each replace a specific default with an explicit teacher decision. |
| 4 | B04 | Specification version: 1 file created, 0 files modified | SYNTHETIC | Illustrative output consistent with the chapter's claim that a correctly formed specification constrains Codex to the specified scope. The exact diff is synthetic. |
| 5 | B04 | Vague prompt version produces 3 files modified including unexpected utils.js | SYNTHETIC | Illustrative comparison consistent with chapter guidance on the risks of under-specified prompts. The specific file names are synthetic examples of the chapter's described failure mode. |
| 6 | B06 | STOP block requires human authorization before acting outside specified scope | ✓ | Chapter describes STOP blocks as handoff conditions embedded in specifications — they gate actions, not prevent them. Correctly stated. |
| 7 | B07 | Five elements: specific task, invariants, context, output format, negative constraints | ✓ | Chapter enumerates these five elements explicitly as the specification framework. |

---

## Exclusions confirmed
- No discussion of specification versioning or iteration
- No multi-file specification examples beyond syllabus.html
- No discussion of specification failures (underspecification vs. overspecification)

## Synthetic scenarios
Build outputs (diff results, file counts, unexpected file names) are illustrative scenarios consistent with the source chapter's guidance. Not transcripts of actual Claude sessions. Synthetic content is consistent with chapter examples and framing.
