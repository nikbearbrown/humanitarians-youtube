# Frictional log — Tracking & Alerting

## 2026-09-28 — the project update, in two aspect ratios

**What I was working on.** A project update explainer on building the tracking and alerting layer for the Provenance Gatekeeper, cut at 16:9 and 9:16.

**What I tried, and what I expected.** 
- I attempted to rely entirely on n8n's execution logs to track AI failures.
- I expected the workflow logs to be sufficient for querying long-term model degradation.

**Where it resisted, and what I did next.** 
- The workflow logs were ephemeral and highly unstructured, making it impossible to mathematically prove how often the underlying model lied over time.
- I bypassed this by engineering a dedicated SQLite database specifically mapped to our evaluation variance schemas, forcing a permanent write on every claim.

**What Claude contributed, and what I did with it.** 
- Mine: The core SQLite schema, webhook routing, and the architectural design.
- Claude's: Debugging the CSS flexbox bug in the `ResultsTable` component for the 9:16 cut to prevent the data rows from overlapping. I accepted the explicit `overflow:hidden` fix.

**What I understand now, and what I still do not.**
- Understood: Workflow orchestrators have ephemeral memory; you need a relational database to mathematically track an AI model's degradation over time.