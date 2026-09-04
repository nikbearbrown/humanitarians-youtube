# Sai Pranavi Jeedigunta

Weekly research reports on Humanitarians AI project work, documented as it happens.

## Voice

**Bella (`af_bella`)**, confirmed 2026-07-26. The name-based heuristic in
[`fellows/README.md`](../README.md) originally suggested Kore (`af_kore`),
but that voice doesn't exist in the installed `brutalist` toolkit — it only
ships two Kokoro voices, Onyx (`am_onyx`) and Bella (`af_bella`). Bella
matches the `hai` persona and `@HumanitariansAI` channel and is now locked in
for the full report series.

## Reports

| Date | Title | Type | Project |
|---|---|---|---|
| 2026-07-26 | [Recovering the Silently Dropped Filings](2026-07-26-recovering-the-silently-dropped-filings/) | Weekly work | Project 29 — Financial Regulatory Intelligence System (`mycroft`) |
| 2026-07-27 | [How Facial Recognition Actually Works (And When It Shouldn't)](2026-07-27-how-facial-recognition-actually-works/) | Weekly STEM | General AI/STEM topic explainer |
| 2026-08-17 | [Why AI-Generated Code Still Needs a Human Who Understands the System](2026-08-17-why-ai-generated-code-still-needs-a-human/) | Weekly STEM | General AI/STEM topic explainer |
| 2026-08-30 | [The Update That Almost Lied About What It Sent](2026-08-30-the-update-that-almost-lied-about-what-it-sent/) | Weekly work | Project 29 — Financial Regulatory Intelligence System (`mycroft`) |
| 2026-08-30 | [Prompt Injection: The Vulnerability Hiding in Plain Text](2026-08-30-what-prompt-injection-actually-looks-like/) | Weekly STEM | General AI/STEM topic explainer |

The first three were rebuilt 2026-08-26/28 for program-wide submission requirements: 4K (3840x2160), a title card + executive-summary opening beat, a 9:16 vertical companion (real Manim portrait relayout, not a crop), and self-assessment against each project's `PROOF.md`. Final deliverables are named per the fellowship convention (`Mycroft_SaiPranaviJeedigunta_<date>_<aspect>.mp4` for the weekly-work video, `<TopicName>_SaiPranaviJeedigunta_<date>_<aspect>.mp4` for the weekly-STEM videos) and live inside each project folder alongside the paperwork; code/paperwork for each is pushed to `github.com/nikbearbrown/humanitarians-youtube` on its own branch (see each project's `README.md` for the exact branch/commit).

The two 2026-08-30 reports (one weekly-work, one weekly-STEM — satisfying the program's two-videos-per-week cadence) were both built natively to spec from the start (4K, both aspect ratios, exec-summary beat, naming convention) rather than rebuilt after the fact:

- **Weekly work:** a real Layer 1 fix (a "Mark email sent" step re-deriving its own high-priority rule instead of reading the email step's actual output) with all on-screen numbers traced to `A7-VERIFICATION.md` and re-verified live against the database at build time — see its `README.md`/`BUILD-LOG.md`.
- **Weekly STEM:** a framework-first explainer teaching a reusable 3-question rubric (Source / Instruction-or-Data / Consequence) for whether an AI agent should act on external text, with a worked example, a falsifiability stress-test, and a scaffolded audit task — self-assessed 11/12 against `PROOF.md` — see its `README.md`/`BUILD-LOG.md`/`PEDAGOGY.md`.
