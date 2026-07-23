# FACTCHECK — agent-friendly-cli-checker

Source: `cli-agnostic-ai-tooling-for-local-project-workflows/chapters/10-agent-workflow-patterns-that-actually-work.md` (CLI design section)
All narration claims checked against chapter content. Verdicts: ✓ holds · minor (editorial, defended) · WRONG (must fix).

| # | Claim (beat) | Verdict | Note |
|---|---|---|---|
| 1 | "CLI designed for human eyes breaks agents — colored output, progress spinners, verbose prose errors become noise on stdout" (B01) | ✓ | Chapter section on CLI design states human-centric CLIs cause agent parse failures. |
| 2 | "Color codes appear as escape sequences; spinners corrupt the data stream" (B01) | ✓ | Chapter describes ANSI escape codes and progress output as specific failure modes. |
| 3 | Seven agent-friendly design rules: stdout for results / stderr for logs / meaningful exit codes / --json flag / --dry-run / --quiet / business logic separated (B02) | ✓ | Chapter lists these seven rules explicitly in the CLI design section. |
| 4 | Checklist result: 4 PASS / 3 FAIL — ANSI on stdout, progress not on stderr, no dry-run (B04) | minor | Illustrative scores consistent with chapter's "before" CLI example; specific pass/fail counts are editorial for demonstration. Defended. |
| 5 | "CLI is interface for two audiences simultaneously — human at terminal and agent in pipe" (B07) | ✓ | Chapter thesis for CLI design section. |
| 6 | "Seven rules are minimum surface for a CLI an agent can trust" (B07) | ✓ | Chapter frames the seven rules as minimum requirements, not optional best practices. |
| 7 | ANSI strip fix takes "ten minutes" (B08) | minor | Editorial time estimate for a straightforward code change; consistent with the chapter's framing of it as the easiest win. Defended. |

**Verdict: all claims hold.** Two minor editorial items (illustrative scores, time estimate), each defended. Cleared to render.
