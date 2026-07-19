# FACTCHECK — folder-structure-auditor

Source: `cli-agnostic-ai-tooling-for-local-project-workflows/chapters/01-why-your-agent-reads-the-wrong-file.md`
All narration claims checked against chapter content. Verdicts: ✓ holds · minor (editorial, defended) · WRONG (must fix).

| # | Claim (beat) | Verdict | Note |
|---|---|---|---|
| 1 | "Most common agent failure — reading the wrong file — caused by folder structure designed for humans, not agents" (B01) | ✓ | Chapter thesis: agents navigate file trees; human-browsing structure creates ambiguity. |
| 2 | report_v1 / report_v2 / report_final / report_final_v2 all in same folder as canonical wrong-file failure mode (B01) | ✓ | Chapter describes wrong-canonical failure mode with versioned file examples. |
| 3 | Three failure modes: wrong canonical, over-broad scope, archive confusion (B02, B03) | ✓ | Chapter explicitly names these three failure mode categories. |
| 4 | Audit script walks directory tree, scores for three modes (B03) | ✓ (minor) | Implementation detail, consistent with chapter's diagnostic approach. |
| 5 | Wrong-canonical triggered by multiple files sharing base name with version suffixes (B03) | ✓ | Direct expression of wrong-canonical failure mode from chapter. |
| 6 | Over-broad triggered when more than five similar files at same level (B03) | minor | Threshold of 5 is editorial; chapter describes the pattern without a specific count. Defended as practical threshold. |
| 7 | config.py HIGH risk / secrets.env HIGH risk / temp MED / pycache HIGH (B04) | minor | Illustrative examples consistent with chapter's risk categorization principles; specific labels are editorial. |
| 8 | "Folder structure is agent communication" (B07) | ✓ | Chapter thesis, stated directly. |
| 9 | "Structure optimized for human browsing can be catastrophic for agent navigation" (B07) | ✓ | Chapter thesis. |

**Verdict: all claims hold.** Two minor editorial thresholds and one minor illustrative example, each defended. Cleared to render.
