# FACTCHECK — `hussain-jboss-migrator-overview` · "Prove Nothing Broke."

Source: the presenter's design notes for a JBoss migrator (pasted in the build
request, 2026-10-28). The reel presents a **design**, not a shipped tool, and says so
in B00 ("this video is about designing a J-Boss migrator").

## Tool facts (stated on screen or in narration)

| Claim | Status |
|---|---|
| Red Hat Migration Toolkit for Applications (MTA) is the productized Konveyor project and has a CLI that reports issues for JBoss EAP upgrades | Correct |
| MTA issue categories: mandatory · optional · potential (· information) | Correct; categories shown are MTA's own |
| PicketLink is removed in EAP 8; security moves to Elytron | Correct (deprecated in EAP 7, removed in EAP 8) |
| OpenRewrite edits via lossless syntax trees, changes only what a recipe targets | Correct |
| Recipe names: `UpgradeToJava17`, `JakartaEE10`, `MigrateToHibernate61`, `JUnit4to5Migration` (org.openrewrite.*) | Real OpenRewrite recipes; verify exact package paths before scaffolding code |
| Eclipse Transformer rewrites javax → jakarta in third-party jars | Correct |
| Server config regenerated as JBoss CLI scripts or via the WildFly Server Migration Tool | Correct (both exist) |
| LLM step proposes fixes only, never silent edits | Design rule from the source, presented as such |

## Labelled as illustrative on screen (footnotes)

- Hostname, repo path and package paths in `migration.yaml` (B02) — from the source config.
- Commands, page names, and the `118.40` test value (B04).
- Inventory items (B05), diff and test names (B07), classes and risk levels (B08).
- `pass → pass` results in B07 are illustrative; no tool run was performed.

## Honest-limits beat (B09)

Custom security modules, vendor-specific JNDI lookups and Seam need a human — this is
the source's own "honest expectation", kept un-softened. No completion percentage is
claimed anywhere.
