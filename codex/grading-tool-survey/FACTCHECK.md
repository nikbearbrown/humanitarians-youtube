# FACTCHECK — grading-tool-survey
**Build the Grading Tool Phase 1 with Claude: Survey Before You Grade**
Source: `codex-for-teachers/chapters/08-grading-tool-build.md`

---

## Claims audit

| # | Beat | Claim | Verdict | Source / Note |
|---|------|-------|---------|---------------|
| 1 | B00 | The first build step is the safest one — and the one everyone skips | ✓ | Chapter: Phase 1 (survey pass) is described as the discipline most commonly omitted by teachers building grading tools. |
| 2 | B00 | It proves your tool can't modify a submission file before it ever touches one | ✓ | Chapter: the read-only guarantee is established in Phase 1 as the foundational constraint for all subsequent phases. |
| 3 | B01 | Phase 1: list submissions, report format and size, exit without modifying any file | ✓ | Chapter describes Phase 1 exactly this way: survey pass is list → report → exit. |
| 4 | B01 | The --dry-run flag is the contractual form of the read-only guarantee | ✓ | Chapter: dry-run is described as the mechanism that makes the read-only constraint testable and explicit. |
| 5 | B04 | survey.py generated: standard library only (verified) | SYNTHETIC | Illustrative output. The constraint (standard library only) is specified in the prompt and consistent with chapter guidance. The verification claim is a synthetic representation of a correct implementation. |
| 6 | B04 | 5 test submissions: table with correct format/size columns, all mtimes unchanged | SYNTHETIC | Illustrative output. File names, sizes, and mtime verification are synthetic examples consistent with the chapter's Phase 1 specification. |
| 7 | B06 | Read-only constraint verified post-extension: no file writes, no timestamp changes | SYNTHETIC | Illustrative output consistent with correct implementation. The constraint preservation claim is the key teaching point from the chapter. |

---

## Exclusions confirmed
- No discussion of Phase 2 (scoring) or Phase 3 (report generation)
- No discussion of error handling for malformed zip files
- No discussion of parallel processing or batch grading

## Synthetic scenarios
All code outputs, file tables, and verification results are illustrative scenarios consistent with the source chapter's Phase 1 specification. Not transcripts of actual Claude sessions or actual student submissions.
