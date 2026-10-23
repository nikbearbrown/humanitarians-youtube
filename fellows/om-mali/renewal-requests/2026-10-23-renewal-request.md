# Month 6 Renewal Request - Om Mali

**Modeled request date:** 2026-10-23

**Project:** Mycroft

**Current agreement:** 2026-08-01 - 2026-10-31

**Requested period:** 2026-11-01 - 2027-01-31

## Summary of work

### 1. Hacker News AI Buzz Tracker

#### The Project

A daily data pipeline that turns Hacker News discussion into a structured attention signal for
the AI sector. For each of twelve AI companies it produces a deterministic attention score and
an LLM-generated summary of community opinion grounded in real comments. The output is stored in
Postgres and served through a dashboard and a versioned JSON API for other systems to consume.

#### Repository

<https://github.com/nikbearbrown/mycroft/tree/feature/ai-debt-tracker/data/raw/Hacker_News_AI_Buzz_Tracker>

#### Summary of work

The tracker is built as a workflow in n8n (an automation tool), backed by a Postgres database,
with language models called through the Groq API. Over these two weeks I added the parts that
make its output visible, trustworthy and usable by other systems:

- **LLM integration.** Built a branch that fetches the real comments on each company's top
  stories, cleans and groups them, and prompts a language model to summarise the community's
  opinion using only what commenters wrote. When the model's structured JSON output kept failing
  validation, I changed how the output is requested and parsed it more tolerantly, which got
  most companies working.
- **Guardrails against AI mistakes.** Added a check that skips the sector-wide summary when no
  usable opinions exist, after the model was caught inventing one from nothing. Found that
  popular posts mentioning a company only in passing were being credited to it, and fixed this
  with a rule that the company must be named in the story title.
- **Web dashboard.** Built a browser dashboard with charts for rankings, trends and news themes,
  served by the existing workflow server and reading live data from the database.
- **API design.** Designed a versioned output format with documented fields and compatibility
  rules, and built a web endpoint other software can call for the latest results. Missing or
  thin data is flagged rather than hidden.
- **Testing and debugging.** Wrote automated tests built from real failure cases, and fixed a
  set of problems that only appeared on the live system: file access limits, blocked environment
  settings, a text-replacement bug, a browser security error and a database column naming issue.
- **Security and reliability.** Caught a full-access database key exposed in the dashboard
  before release and replaced it with a read-only key. Added an email alert for when the
  pipeline itself fails, and exported every workflow into the repository so the code matches
  what actually runs.

### 2. Private AI Valuation Agent

#### The Project

A production-shaped data and agent pipeline that derives share prices for private AI
companies from mandatory SEC fund disclosures. The engineering problem is not the arithmetic
but everything around it: resolving inconsistent entity names at scale, deciding when a
machine must defer to a human, separating corporate actions from genuine price movements, and
keeping every published number traceable to the document it came from. It is built so that a
wrong answer is recoverable and an unsupported answer is refused rather than guessed.

#### Repository

<https://github.com/nikbearbrown/mycroft/tree/feature/ai-debt-tracker/data/raw/Private_AI_Valuation_Agent>

#### Summary of work

Over ten weeks I built the system end to end:

- **Large-scale data engineering.** Built an ingestion pipeline that processes several gigabytes
  of filing data per quarter with columnar storage and an analytical query engine, reducing tens
  of millions of rows to the few thousand that matter. Every stage reconciles so no record is
  silently dropped, and the raw layer is immutable so any later bug is fixed by rebuilding.
- **Entity resolution.** Built a matcher combining official identifiers, alias lookup and fuzzy
  scoring behind a coverage gate, and evaluated it against a hand-labelled set of real company
  names with the evidence for each label recorded. The evaluation set rebuilds byte-identically,
  after I fixed three sources of non-determinism in my own sampling code.
- **Evaluating a language model honestly.** Tested a locally hosted model against the
  deterministic matcher with identical inputs, fixed temperature and schema-constrained
  decoding. It performed worse, fabricating a match whenever the right answer was "none of
  these", so I kept the deterministic system under a decision rule set before the test and
  published the full comparison.
- **Human-in-the-loop agent design.** Built an agent workflow that resolves what it can and
  suspends for a human on the rest, with state persisted so a paused decision survives a
  restart. The queue is keyed on the question rather than the record, so many ambiguous rows
  collapse into a few real decisions, and none can be recorded without a named reviewer.
- **Guardrails on generated text.** The quarterly summary is written by a language model that
  sees only pre-computed figures, and every draft passes mechanical checks: numbers must exist in
  the source data, claimed rankings must hold, and placeholder output is rejected. I added the
  ranking check after a draft passed the number check while contradicting itself.
- **Serving the data to other systems.** Built a read-only MCP server with summary-first,
  size-bounded responses and query-bound cursors, because a single query could return far more
  than an assistant can read. Froze the published output behind a validated schema that refuses
  any field the data cannot support.
- **Documentation, automation and testing.** Wrote the architecture and data documentation, a
  demonstration that queries live data instead of replaying a recording, an automated quarterly
  schedule, and a test suite of over three hundred tests, including tests that reproduce what a
  real client withholds.

---

### 3. AI Debt Tracker

#### The Project

The AI Debt Tracker is an AI agent that turns unstructured financial filings into a structured,
always up to date ledger of corporate borrowing across the AI industry. It is designed as a
LangGraph supervisor that sends work to parallel reader agents over MCP tool servers, all
running on local models on a laptop GPU. It is evaluated with no information leakage against
data that companies publish later. The goal is a reliable, auditable signal of how much the AI
build-out is being financed with debt.

#### Repository

[nikbearbrown/mycroft, feature/ai-debt-tracker, data/raw/AI_Debt_Tracker](https://github.com/nikbearbrown/mycroft/tree/feature/ai-debt-tracker/data/raw/AI_Debt_Tracker)

#### Summary of work

In plain terms, the project tracks money companies have borrowed. Every loan has an amount, an
interest rate and a date it must be repaid, and companies announce new loans in public documents
long before their official quarterly summary confirms them. The project is in progress. The work
so far has built everything needed to measure an AI system on this task honestly, and the agent
system itself is the next stage.

- **Evaluation-first system design.** I wrote the full design (data sources, agents, tool
  servers, local models, evaluation plan and a ten-week schedule) and set go/no-go checks with
  pass lines fixed before any result existed.
- **Leak-proof tool server over MCP.** I built a point in time server that gives an agent access
  to filings while refusing anything published after the cutoff, failing closed on undatable
  documents and logging every call. A structural test stops any agent code from importing the
  answer key.
- **Ground truth from machine-readable data.** I built a pipeline that turns the SEC's bulk
  structured data into an answer key, with a parser for very messy labels (numbers written as
  words, typos, rounded values). The key was checked against what the reports actually contain
  instead of what was assumed.
- **A grader with honest validation.** I built a grader that scores at three levels of detail,
  using optimal one-to-one matching and bootstrap confidence intervals. I validated it against
  hand-checked reports with a separate held-out set, so the tool that found the bugs was not also
  used to grade itself.
- **Local LLM selection by experiment.** I ran a bake-off of three open-weight models on real
  documents for structured JSON extraction, with the decision rule set in advance. That
  overturned the design's original choice of the larger model.
- **Baselines and reproducibility.** I built a do-nothing baseline to measure the headroom. I
  froze the test splits and enforced the freeze in code, pinned the cutoffs against shifting
  timestamps, and kept bulky data and model weights outside the repository.
- **Human-in-the-loop governance.** Every phase ends at a gate cleared by a named person, with
  model judgments labelled as judgments and every decision logged.

Tools: Python, LangGraph, Model Context Protocol (MCP), Ollama, local LLMs (Qwen3, Llama 3.1),
Claude Code.

## Weekly Log

### 2026-07-20 - 2026-07-26: Building the AI Buzz Tracker dashboard (Hacker News AI Buzz Tracker)

**Hours completed:** 21.0 (18.0 on the project, 3.0 on the STEM video) - [time record](../weekly-hours/2026-07-27-weekly-hours.md)

**Work completed:**

- Built a live web dashboard showing which AI companies get the most attention, how that
  changes over the week, and what kind of news is driving it, connected to the live database.
- Added an LLM step that reads real comments on each company's top stories and summarises what
  people think, and fixed the output-format failure that was making every summary fail.
- Caught an exposed full-access database key before release and replaced it, and found that
  popular posts were being credited to the wrong companies.

**Evidence folder:** [2026-07-27-data-visualization-Building-the-AI-Buzz-Tracker-dashboard](../2026-07-27-data-visualization-Building-the-AI-Buzz-Tracker-dashboard/)

**Videos:** Project Video: [Watch on YouTube](https://www.youtube.com/watch?v=LiJnm8r8ArU), STEM Video: [Watch on YouTube](https://www.youtube.com/watch?v=V5lFlRKYeH0)

### 2026-07-27 - 2026-08-02: Attribution fix and JSON signal endpoint (Hacker News AI Buzz Tracker)

**Hours completed:** 21.0 (18.0 on the project, 3.0 on the STEM video) - [time record](../weekly-hours/2026-08-01-weekly-hours.md)

**Work completed:**

- Fixed how stories are matched to companies so a story only counts if its title names the
  company, added automated tests built from the real failure, and re-checked it on the live
  pipeline.
- Designed a versioned data format for the tracker's output and built a web endpoint that other
  software can call for the latest results, with thin data clearly flagged.
- Added an alert email for pipeline failures, improved the daily email summary, updated the
  database, and exported all workflows into the repository.

**Evidence folder:** [2026-08-01-api-interface-Attribution-fix-and-JSON-signal-endpoint](../2026-08-01-api-interface-Attribution-fix-and-JSON-signal-endpoint/)

**Videos:** Project Video: [Watch on YouTube](https://www.youtube.com/watch?v=LiJnm8r8ArU), STEM Video: [Watch on YouTube](https://www.youtube.com/watch?v=mPBshmrSEQ8)

### 2026-08-03 - 2026-08-09: Verifying private AI valuations from SEC filings (Private AI Valuation Agent)

**Hours completed:** 21.0 (17.0 on the project, 4.0 on the STEM video) - [time record](../weekly-hours/2026-08-08-weekly-hours.md)

**Work completed:**

- Validated the core premise by hand before building anything, reading filings directly from
  the SEC's public database and confirming the arithmetic holds across multiple fund managers.
- Found that the filter the plan specified for identifying private holdings was broken, and
  replaced it with a field that works across every manager in the sample.
- Caught two name-matching traps that would have produced a convincing price history for a
  company that was never actually in the data.

**Evidence folder:** [2026-08-08-data-verification-Verifying-private-AI-valuations](../2026-08-08-data-verification-Verifying-private-AI-valuations/)

**Videos:** Project Video: [Watch on YouTube](https://www.youtube.com/watch?v=Ksf097PNjCU), STEM Video: [Watch on YouTube](https://www.youtube.com/watch?v=jRpqnfO7aIo)

### 2026-08-10 - 2026-08-16: Bulk ingestion at scale (Private AI Valuation Agent)

**Hours completed:** 21.0 (18.0 on the project, 3.0 on the STEM video) - [time record](../weekly-hours/2026-08-15-weekly-hours.md)

**Work completed:**

- Built the ingestion pipeline that downloads several years of quarterly filings and narrows
  tens of millions of rows to the relevant holdings, reconciling at every stage.
- Found and fixed two date-handling defects that would have silently inverted the project's
  headline measurement.
- Established that the source data is published with a structural delay, and pinned that
  limit with a test so a later version cannot quietly paper over it.

**Evidence folder:** [2026-08-15-data-ingestion-Bulk-ingestion-at-scale](../2026-08-15-data-ingestion-Bulk-ingestion-at-scale/)

**Videos:** Project Video: [Watch on YouTube](https://www.youtube.com/watch?v=Ob7PZTdwDMY), STEM Video: [Watch on YouTube](https://www.youtube.com/watch?v=YiJgtnEwx2Q)

### 2026-08-17 - 2026-08-23: Building a golden set and a baseline name matcher (Private AI Valuation Agent)

**Hours completed:** 21.0 (18.0 on the project, 3.0 on the STEM video) - [time record](../weekly-hours/2026-08-22-weekly-hours.md)

**Work completed:**

- Hand-labelled an evaluation set of real company names, recording the evidence behind each
  label so the set is auditable row by row.
- Built the matcher as a cascade of official identifiers, alias lookup and gated fuzzy
  scoring, and measured its precision and recall against that set.
- Traced three independent sources of non-determinism in my own sampling code and fixed them,
  so the evaluation set now rebuilds identically every time.

**Evidence folder:** [2026-08-22-entity-resolution-Golden-set-and-baseline-matcher](../2026-08-22-entity-resolution-Golden-set-and-baseline-matcher/)

**Videos:** Project Video: [Watch on YouTube](https://www.youtube.com/watch?v=0SoakQiUi20), STEM Video: [Watch on YouTube](https://www.youtube.com/watch?v=uwTKdbn-BfM)

### 2026-08-24 - 2026-08-30: Measuring a local AI model against the matcher (Private AI Valuation Agent)

**Hours completed:** 21.0 (17.0 on the project, 4.0 on the STEM video) - [time record](../weekly-hours/2026-08-28-weekly-hours.md)

**Work completed:**

- Ran a locally hosted language model over the same test cases as the deterministic matcher,
  with identical inputs, fixed decoding settings and schema-constrained output.
- Read every disagreement individually and identified a systematic failure mode: the model
  fabricated a match whenever the correct answer was that none of the candidates applied.
- Showed its self-reported confidence carried no usable signal for triage, then retained the
  deterministic system and published the comparison with every raw reply.

**Evidence folder:** [2026-08-28-model-evaluation-Local-LLM-against-the-matcher](../2026-08-28-model-evaluation-Local-LLM-against-the-matcher/)

**Videos:** Project Video: [Watch on YouTube](https://www.youtube.com/watch?v=J6lqFF1POFw), STEM Video: [Watch on YouTube](https://www.youtube.com/watch?v=ii6fpLts5us)

### 2026-08-31 - 2026-09-06: Building the human review queue (Private AI Valuation Agent)

**Hours completed:** 21.0 (18.0 on the project, 3.0 on the STEM video) - [time record](../weekly-hours/2026-09-04-weekly-hours.md)

**Work completed:**

- Built an agent workflow that resolves what it can automatically and suspends for a human on
  the rest, persisting state so a paused decision survives a process restart.
- Keyed the queue on the question rather than the record, so a large volume of ambiguous rows
  collapses into a handful of genuine decisions that one answer each can clear.
- Answered those decisions with written rationales, then re-ran the entire process against a
  different database and confirmed it reproduced the results exactly.

**Evidence folder:** [2026-09-04-human-in-the-loop-Building-the-review-queue](../2026-09-04-human-in-the-loop-Building-the-review-queue/)

**Videos:** Project Video: [Watch on YouTube](https://www.youtube.com/watch?v=eXozYNG9duk), STEM Video: [Watch on YouTube](https://www.youtube.com/watch?v=ZIfyYmmzqsc)

### 2026-09-07 - 2026-09-13: Building the price panel and the stock-split detector (Private AI Valuation Agent)

**Hours completed:** 21.0 (18.0 on the project, 3.0 on the STEM video) - [time record](../weekly-hours/2026-09-11-weekly-hours.md)

**Work completed:**

- Built the price panel itself, keyed by company, manager and reporting date, reconciling
  exactly against the filings it derives from.
- Built a detector for corporate actions that would otherwise enter a price series as sudden
  crashes, and found my first version missed the exact case it was written for.
- Reviewed each flagged case by hand using share counts rather than prices, which is what
  actually separates a split from a genuine revaluation, and recorded measurement and
  judgement in separate fields.

**Evidence folder:** [2026-09-11-data-modeling-Marks-panel-and-split-detector](../2026-09-11-data-modeling-Marks-panel-and-split-detector/)

**Videos:** Project Video: [Mycroft_OmMali_11_09_2026.mp4](https://drive.google.com/drive/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv), STEM Video: [Watch on YouTube](https://www.youtube.com/watch?v=gHfhncbv4IU)

### 2026-09-14 - 2026-09-20: Measuring how private valuations move and spread (Private AI Valuation Agent)

**Hours completed:** 21.0 (18.0 on the project, 3.0 on the STEM video) - [time record](../weekly-hours/2026-09-18-weekly-hours.md)

**Work completed:**

- Implemented the three core measurements: how often valuations change, how far managers
  disagree on the same date, and how fast a new price propagates between them.
- Found and corrected four defects in my own measurements by reading the output rather than
  trusting the code, including a conclusion the data did not support.
- Built and tested an analysis that cannot run until further data is published, proving it
  against injected inputs so it completes itself when that data arrives.

**Evidence folder:** [2026-09-18-analysis-How-private-marks-move-and-propagate](../2026-09-18-analysis-How-private-marks-move-and-propagate/)

**Videos:** Project Video: [Mycroft_OmMali_18_09_2026.mp4](https://drive.google.com/drive/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv), STEM Video: [claude-for-astronomy_OmMali_18_09_2026](https://drive.google.com/drive/u/1/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv)

### 2026-09-21 - 2026-09-27: Joining filed funding rounds to fund entry dates (Private AI Valuation Agent)

**Hours completed:** 21.0 (18.0 on the project, 3.0 on the STEM video) - [time record](../weekly-hours/2026-09-25-weekly-hours.md)

**Work completed:**

- Added two further filing sources that record when a company raised capital and when a fund
  first acquired its position, neither of which the primary source carries.
- Demonstrated that joining those sources on company name would have been badly wrong,
  because most name matches are investment vehicles rather than the companies themselves, and
  rebuilt the join on confirmed official identifiers instead.
- Wrote a parser that reads the same disclosure across five fund groups that each format it
  differently, including one that uses no table structure at all.

**Evidence folder:** [2026-09-25-data-integration-Filed-rounds-to-fund-entry-dates](../2026-09-25-data-integration-Filed-rounds-to-fund-entry-dates/)

**Videos:** Project Video: [Mycroft_OmMali_25_09_2026.mp4](https://drive.google.com/drive/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv), STEM Video: [claude-for-astronomy_OmMali_25_09_2026](https://drive.google.com/drive/u/1/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv)

### 2026-09-28 - 2026-10-04: Serving the data over MCP and freezing the output format (Private AI Valuation Agent)

**Hours completed:** 21.0 (18.0 on the project, 3.0 on the STEM video) - [time record](../weekly-hours/2026-10-02-weekly-hours.md)

**Work completed:**

- Built a read-only MCP server exposing the panel to an AI assistant, and solved the binding
  constraint: a single query returns far more than any assistant can read, so every response
  is summary-first with a bounded page and a query-bound cursor.
- Froze the published output behind a validated schema that refuses, by name, any field the
  underlying data cannot support.
- Added mechanical checks on model-generated prose after a draft passed the existing checks
  while contradicting itself within a single paragraph.

**Evidence folder:** [2026-10-02-api-interface-MCP-server-and-frozen-signal-contract](../2026-10-02-api-interface-MCP-server-and-frozen-signal-contract/)

**Videos:** Project Video: [Mycroft_OmMali_02_10_2026.mp4](https://drive.google.com/drive/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv), STEM Video: [claude-for-astronomy_OmMali_02_10_2026](https://drive.google.com/drive/u/1/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv)

### 2026-10-05 - 2026-10-11: Documenting the system and making the demo repeatable (Private AI Valuation Agent)

**Hours completed:** 21.0 (16.0 on the project, 5.0 on the STEM video) - [time record](../weekly-hours/2026-10-09-weekly-hours.md)

**Work completed:**

- Audited the project against its own plan and found three required documents had never been
  written, then wrote them: the proposal, the system architecture and the data architecture.
- Documented the provenance chain, showing how any published figure is traced step by step
  back to the exact source file that produced it.
- Built a demonstration that queries the live system rather than replaying a recording, so it
  can never show something the data no longer supports.

**Evidence folder:** [2026-10-09-documentation-System-docs-and-a-re-runnable-demo](../2026-10-09-documentation-System-docs-and-a-re-runnable-demo/)

**Videos:** Project Video: [Mycroft_OmMali_09_10_2026.mp4](https://drive.google.com/drive/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv), STEM Video: [claude-for-astronomy_OmMali_09_10_2026](https://drive.google.com/drive/u/1/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv)

### 2026-10-12 - 2026-10-18: Building the answer key and choosing the model (AI Debt Tracker)

**Hours completed:** 21.0 (18.0 on the project, 3.0 on the STEM video) - [time record](../weekly-hours/2026-10-16-weekly-hours.md)

**Work completed:**

- Scoped the project, wrote the system design with pre-set go/no-go checks, and ran a
  feasibility spike on real filings that confirmed the problem is worth solving.
- Built the answer key pipeline and its label parser, and measured how much detail each company
  really reports. That corrected an assumption about which companies can be graded bond by bond.
- Built the leak-proof point in time MCP server and ran a three-model local LLM bake-off. The
  smallest model won under rules fixed in advance.

**Evidence folder:** [2026-10-16-feasibility-Answer-key-and-model-selection](../2026-10-16-feasibility-Answer-key-and-model-selection/)

**Videos:** Project Video: [Mycroft_OmMali_16_10_2026.mp4](https://drive.google.com/drive/u/1/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv), STEM Video: [claude-for-astronomy_OmMali_16_10_2026](https://drive.google.com/drive/u/1/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv)

### 2026-10-19 - 2026-10-25: Building the answer key, grader and baseline (AI Debt Tracker)

**Hours completed:** 21.0 (18.0 on the project, 3.0 on the STEM video) - [time record](../weekly-hours/2026-10-23-weekly-hours.md)

**Work completed:**

- Extended the answer key to every report of all companies in the study, and built the grader
  with three levels of matching and confidence intervals.
- Validated the grader against hand-checked printed reports. I fixed every bug that check found,
  then confirmed the result on a separate held-out set chosen in advance.
- Built the do-nothing baseline to measure the headroom. I locked the frozen test files against
  accidental overwrites and pinned the cutoffs after the SEC's timestamps shifted.

**Evidence folder:** [2026-10-23-Building-the-answer-key-grader-and-baseline](../2026-10-23-Building-the-answer-key-grader-and-baseline/)

**Videos:** Project Video: [Mycroft_OmMali_23_10_2026.mp4](https://drive.google.com/drive/u/1/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv), STEM Video: [claude-for-astronomy_OmMali_23_10_2026](https://drive.google.com/drive/u/1/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv)

---

**Total: 294.0 hours across 14 weeks** - 248.0 on project work and 46.0 on the STEM videos.
