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
| 2026-08-30 | [The Check That Never Once Fired](2026-08-30-the-check-that-never-once-fired/) | Weekly work | Project 29 — Financial Regulatory Intelligence System (`mycroft`) |
| 2026-09-07 | [The Synonyms the Classifier Never Learned](2026-09-07-the-synonyms-the-classifier-never-learned/) | Weekly work | Project 29 — Financial Regulatory Intelligence System (`mycroft`) |
| 2026-09-07 | [Embeddings: How AI Tells Similar From Different (When Keyword Matching Can't)](2026-09-07-embeddings-how-ai-tells-similar-from-different/) | Weekly STEM | General AI/STEM topic explainer |

The first three were rebuilt 2026-08-26/28 for program-wide submission requirements: 4K (3840x2160), a title card + executive-summary opening beat, a 9:16 vertical companion (real Manim portrait relayout, not a crop), and self-assessment against each project's `PROOF.md`. Final deliverables are named per the fellowship convention (`Mycroft_SaiPranaviJeedigunta_<date>_<aspect>.mp4` for the weekly-work video, `<TopicName>_SaiPranaviJeedigunta_<date>_<aspect>.mp4` for the weekly-STEM videos) and live inside each project folder alongside the paperwork; code/paperwork for each is pushed to `github.com/nikbearbrown/humanitarians-youtube` on its own branch (see each project's `README.md` for the exact branch/commit).

The three 2026-08-30 reports (two weekly-work, one weekly-STEM) were all built natively to spec from the start (4K, both aspect ratios, exec-summary beat, naming convention) rather than rebuilt after the fact:

- **Weekly work (1st):** a real Layer 1 fix (a "Mark email sent" step re-deriving its own high-priority rule instead of reading the email step's actual output) with all on-screen numbers traced to `A7-VERIFICATION.md` and re-verified live against the database at build time — see its `README.md`/`BUILD-LOG.md`.
- **Weekly STEM:** a framework-first explainer teaching a reusable 3-question rubric (Source / Instruction-or-Data / Consequence) for whether an AI agent should act on external text, with a worked example, a falsifiability stress-test, and a scaffolded audit task — self-assessed 11/12 against `PROOF.md` — see its `README.md`/`BUILD-LOG.md`/`PEDAGOGY.md`.
- **Weekly work (2nd):** a second Layer 1 fix in the same pipeline — a source classifier rule specifically written to catch CFTC filings that, tested against every live CFTC item, matched zero of them (the rule checked for text patterns that structurally can't appear in Federal Register permalinks/titles) — fixed by reading the feed's real `dc:creator` field instead of guessing. Named `Mycroft_SaiPranaviJeedigunta_20260830b_*` (suffixed `b` since two weekly-work videos landed the same day) — see its `README.md`/`BUILD-LOG.md`.

The 2026-09-07 reports (one weekly-work, one weekly-STEM):

- **Weekly work (4th in the Layer 1 series):** a partial fix, honestly reported — 18 Google News items were falling through the source classifier to "Unknown Source" (no `dc:creator` field to fall back on this time); 10 of 18 recovered via feed-agnostic synonym keywords (`adviser`/`RIA`, `broker-dealer`/`Reg BI`), with the remaining 8 explicitly left open as a deliberate tradeoff rather than an unsolved bug — see its `README.md`/`BUILD-LOG.md`.
- **Weekly STEM:** a framework-first explainer on when to use keyword matching vs. embeddings — chosen because it explains the general pattern underneath this fellow's last several weekly-work bugs (brittle exact-match rules breaking as real-world text varies), though kept fully generic with fictional examples, not a report of any specific fix. Its meaning-space scatter diagrams (B04/B05) needed 3 rounds of layout fixes after the automated frame-QC tool failed to catch a real content-distribution defect (a small cluster of points confined to one region of a much larger panel) — resolved by direct visual inspection of extracted frames across each beat's full runtime, not by trusting the tool's reported numbers. A follow-up patch also fixed a real low-contrast palette bug (a text color measuring 1.16:1 against its panel background, WCAG minimum is 4.5:1) and a text/panel-border overlap the toolkit's own layout auditor caught. See its `BUILD-LOG.md` for the full account.

## Naming/format convention going forward

All 8 reports above use the original fellowship naming (`Mycroft_SaiPranaviJeedigunta_<date>_<aspect>.mp4` / `<TopicName>_SaiPranaviJeedigunta_<date>_<aspect>.mp4`, 4K 16:9 + 1080x1920 9:16 short) and are being **kept exactly as built** — no retroactive renaming or re-rendering.

**Starting with the next video**, submissions switch to the toolkit's own official spec (`brutalist/docs/FELLOWS-SUBMISSION.md`, introduced 2026-09-07): `ProjectName_VolunteerName.mp4` (no date, no aspect suffix in the filename), separate `landscape/`/`vertical/` folders instead of a filename suffix, and a true 4K **2160x3840 full-length vertical companion** (via the toolkit's `./art vertical` command — a native portrait relayout of the whole video, not a ≤180s Shorts-style cut) instead of the 1080x1920 short used above.
