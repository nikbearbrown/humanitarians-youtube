# Renewal request — Adwait Changan

- **Current agreement:** 1 Aug — 31 Oct 2026
- **Requested period:** 1 Nov 2026 — 1 Feb 2027

- **Project:** Mycroft — finance investigation agent, and the "Agentic AI" explainer playlist (@HumanitariansAI)
- **Repository:** https://github.com/nikbearbrown/humanitarians-youtube
- **Work folder:** `fellows/adwait-c/`
- **Degree:** MS Computer Software Engineering, Northeastern University · **PM:** Shradha Katte (katte.shradha@humanitarians.ai)

## What the current period produced

Two parallel weekly tracks across thirteen weeks: a Mycroft finance-agent investigation each
week, and a ten-part "Agentic AI" teaching playlist that runs from "an agent is a model in a
loop" to building an MCP server. Every video ships 4K in both 16:9 and 9:16, each with a
runnable code artifact, and every build ran at $0.00.

- **Mycroft track** — twelve finance-agent investigations: specialist routing, reinvestigation,
  materiality approval, evidence freshness and coverage, a disagreement log, and a distribution
  gate. All hold one boundary: the agent verifies and routes; a named human owns the causal
  explanation and the approval.
- **Agentic AI playlist** — the full ten-episode arc (what makes AI agentic → the loop → tools →
  memory → planning → retrieval → guardrails → multi-agent → MCP → building an MCP server), plus
  two security explainers (the confused deputy; when not to build an agent).
- A published finance-investigator overview, "Building an Evidence-Driven AI Variance Engine in 3
  Weeks": https://www.humanitarians.ai/videos/building-an-evidence-driven-ai-variance-engine-in-3-weeks-for-mycroft
- Twenty-four dated work folders, each with a beat sheet, a runnable `.py`, signed PEDAGOGY and
  FACTCHECK gates, and a dated Frictional log.

### Evidence — Mycroft track

| Week | Work | Video | Log |
|---|---|---|---|
| 7 Aug | How to test a finance agent | [watch](https://www.humanitarians.ai/videos/how-to-test-mycrofts-finance-ai-agent-breaking-the-books-on-purpose) | [log](./2026-08-07-how-do-you-test-a-finance-agent/FRICTIONAL.md) |
| 14 Aug | What-if analysis without AI guessing | [watch](https://www.humanitarians.ai/videos/deterministic-what-ifs-in-mycroft-scenario-analysis-without-ai-guessing) | [log](./2026-08-14-what-if-analysis-without-ai-guessing/FRICTIONAL.md) |
| 21 Aug | Prove what the finance agent did | [watch](https://www.humanitarians.ai/videos/how-to-prove-what-your-financial-ai-actually-did-auditing-the-chain) | [log](./2026-08-21-can-you-prove-what-your-finance-agent-actually-did/FRICTIONAL.md) |
| 28 Aug | Trend investigation | on Drive | [log](./2026-08-28-mycroft-trend-investigation/FRICTIONAL.md) |
| 4 Sep | Specialist routing (two agents live) | [watch](https://www.humanitarians.ai/videos/mycroft-update-running-two-ai-agents-live) | [log](./2026-09-04-mycroft-specialist-routing/FRICTIONAL.md) |
| 11 Sep | Reinvestigation | on Drive | [log](./2026-09-11-mycroft-reinvestigation/FRICTIONAL.md) |
| 18 Sep | Materiality approval | on Drive | [log](./2026-09-18-mycroft-materiality-approval/FRICTIONAL.md) |
| 25 Sep | Evidence freshness | on Drive | [log](./2026-09-25-mycroft-evidence-freshness/FRICTIONAL.md) |
| 2 Oct | Disagreement log | on Drive | [log](./2026-10-02-mycroft-disagreement-log/FRICTIONAL.md) |
| 9 Oct | Evidence coverage | on Drive | [log](./2026-10-09-mycroft-evidence-coverage/FRICTIONAL.md) |
| 16 Oct | Whose failure is it | on Drive | [log](./2026-10-16-mycroft-whose-failure-is-it/FRICTIONAL.md) |
| 23 Oct | Distribution gate | on Drive | [log](./2026-10-23-mycroft-distribution-gate/FRICTIONAL.md) |

### Stem topics — Agentic AI playlist

| Week | Topic | Video | Log |
|---|---|---|---|
| 7 Aug | What makes AI agentic | [video](https://www.humanitarians.ai/videos/what-actually-makes-an-ai-agentic-cutting-through-the-hype) | [log](./2026-08-07-what-makes-ai-agentic/FRICTIONAL.md) |
| 14 Aug | The agent loop | [video](https://www.humanitarians.ai/videos/inside-an-ai-agent-loop-the-only-step-that-touches-reality) | [log](./2026-08-14-the-agent-loop/FRICTIONAL.md) |
| 21 Aug | Tools and function calling | on Drive | [log](./2026-08-21-tools-and-function-calling/FRICTIONAL.md) |
| 28 Aug | Agent memory | on Drive | [log](./2026-08-28-agent-memory/FRICTIONAL.md) |
| 4 Sep | Planning and decomposition | on Drive | [log](./2026-09-04-planning-and-decomposition/FRICTIONAL.md) |
| 11 Sep | Grounding and retrieval | on Drive | [log](./2026-09-11-grounding-and-retrieval/FRICTIONAL.md) |
| 18 Sep | Guardrails and evals | on Drive | [log](./2026-09-18-guardrails-and-evals/FRICTIONAL.md) |
| 25 Sep | Multi-agent systems | on Drive | [log](./2026-09-25-multi-agent-systems/FRICTIONAL.md) |
| 2 Oct | What is MCP | on Drive | [log](./2026-10-02-what-is-mcp/FRICTIONAL.md) |
| 9 Oct | Building an MCP server | on Drive | [log](./2026-10-09-building-an-mcp-server/FRICTIONAL.md) |
| 16 Oct | The confused deputy | on Drive | [log](./2026-10-16-the-confused-deputy/FRICTIONAL.md) |
| 23 Oct | When not to build an agent | on Drive | [log](./2026-10-23-when-not-to-build-an-agent/FRICTIONAL.md) |

Masters: Google Drive — *HAI Brutalist Videos › Mycroft_AdwaitChangan* (add folder link).
Weekly hours: [HOURS.md](HOURS.md) — ≥ 20 hrs each week. Weekly Frictional logs: one per work folder, linked above.

## Plan for the requested period

Production MCP → a reviewed Mycroft release, ~20 hours/week, each week gating the next:

1. **MCP server test harness** (week of 7 Nov). A client connects and asserts the discovered tool
   list; short explainer.
2. **MCP auth & permissions** (week of 14 Nov). Scope what each tool may do; apply the
   confused-deputy defense in practice.
3. **Deploy an MCP server** (week of 21 Nov). Package, run, connect a live client; explainer.
4. **Open the distribution-gate PR** (week of 28 Nov). Walk a reviewer through it and clear the
   first round of comments.

Beyond November: a reviewed Mycroft release (gate + disagreement log + coverage) and a standing
eval suite in CI. Reporting continues as a dated Frictional log per work folder and weekly hours.

## Open items I am carrying

- Oct 26-31 video generation.
- Duplicate `fellows/adwait-changan/` folder to reconcile with `fellows/adwait-c/`.