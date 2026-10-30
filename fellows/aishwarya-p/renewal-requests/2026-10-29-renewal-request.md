# Month 3 Renewal Request - Aishwarya Patil

**Request date:** 2026-10-29

**Project:** Mycroft patent intelligence system

**Current agreement:** 2026-08-01 - 2026-10-31

**Requested period:** 2026-11-01 - 2027-01-31

**Period reviewed:** 2026-08-01 - 2026-10-29

**Project Manager and supervisor (12-29 October):** Shradha Katte (katte.shradha@humanitarians.ai). The supervisor for 1 August - 11 October is not stated in this report.

**Degree:** MS in Information Systems

**Authorization:** OPT, 2026-04-15 - 2027-02-20. Supporting documents go to HR privately, not in this file.

## Summary of work

### 1. Mycroft Patent Reader

#### The Project

A system that reads a patent's claims and citation lineage from real public data. It splits a patent's claims into independent and dependent claims, traces what the patent cites, and can optionally classify each independent claim's protection scope (broad or narrow; defensive, offensive or exploratory) with the Claude API. The data comes from Google's public patent dataset in BigQuery (`patents-public-data.patents.publications`, about 98 million rows). The system is served by a FastAPI backend with a React frontend, and is measured by an evaluation harness against hand-labelled claims.

#### Repository

[nikbearbrown/mycroft, main, projects/Patents-Intelligence-Engine/patent-reader](https://github.com/nikbearbrown/mycroft/tree/main/projects/Patents-Intelligence-Engine/patent-reader)

#### Summary of work

- **ClaimsAgent: structural reading.** I built `claims_parser.py`, which splits a patent's claims and classifies each one as independent or dependent. It was tested against 4 real patents.
  - I narrowed the multi-dependency detector to genuine claim-reference patterns.
  - Broader testing found a real bug: one patent numbers its claims `"1 ."` instead of `"1."`, and the parser silently returned 0 claims for a patent with 14. I fixed it and verified both formats.
- **ClaimsAgent: scope classification.** I built `claim_classifier.py`, which calls the Claude API for each independent claim's breadth and posture, and wired the parser and classifier together as `ClaimsAgent`.
  - Refusals on sensitive subject matter are returned as "unclear" with a caveat instead of crashing.
- **LineageAgent: backward citations.** I built `lineage_agent.py`, which reads a patent's backward citations from the same row as its claims, so there's no second query.
  - I found and fixed a real bug: BigQuery returns empty strings, not `None`, for missing fields, which made every citation look like non-patent literature.
  - I confirmed it handles international publication numbers (for example `CN-103154936-A` and `WO-2022015730-A1`).
  - Forward citations were deliberately deferred because of their expensive query pattern, and the zero-citation case is still untested.
- **Query cost discipline.** The patents table has no partitioning or clustering, so a single new patent lookup scans about 116 GB, roughly $0.71 at list price. I documented that, kept every query an exact parameterized match, and reused cached patents in all test scripts.
- **CLI, then API.** I built `patent_reader.py`, a command-line tool that wires both agents together. Then I built `api.py`, a FastAPI backend with CORS that loads its API key through python-dotenv, which removed a recurring failure where the key had to be exported by hand in every terminal.
- **React frontend.** I built a Vite React frontend that calls the backend, then hardened it:
  - three distinct error messages (wrong publication number, server error, backend unreachable);
  - a loading spinner with a hint for the slow classify path;
  - inputs disabled during a fetch;
  - classify set to off by default, so the free path is the default.
- **Classifier evaluation harness.** I built `eval_classifier.py`, which scores the classifier against hand labels with accuracy, Cohen's kappa, a majority-class baseline and a collapse check. I also built `pull_eval_claims.py`, which runs one capped BigQuery query.
  - The pull scanned 161.8 GB for $0.92 at list price and returned 160 candidate patents.
  - 147 of those 160 have only 1-3 independent claims, so the test set became 50 claims from 16 patents, 2 per CPC section A-H.
- **First baseline result.** I labelled all 50 claims by hand and ran the baseline. The cost upper bound was $0.32; the actual cost wasn't recorded.
  - Breadth: accuracy 0.66, kappa 0.08.
  - Posture: accuracy 0.60, kappa 0.00.
  - Both fall below the always-most-common-answer baseline, and the classifier leans broad/offensive on functional claim wording, not narrow/defensive as suspected.
  - All 50 posture labels are defensive, so this set can't measure posture agreement yet.
  - I also fixed a refusal bug: the model can refuse partway through an answer, so `claim_classifier.py` now treats `stop_reason == "refusal"` as declined, and all 50 claims score.
- **Communication.** 12 project progress videos and 12 STEM/AI explainers, each with narration, beat sheet, scenes and an evidence-discipline PEDAGOGY.md.

Tools: Python, Google BigQuery, Claude API, FastAPI, React (Vite), Manim, Remotion, Kokoro TTS, Claude Code.

#### Degree relevance

This work is directly relevant to an MS in Information Systems. It covers:
- building a patent intelligence system;
- querying a large public dataset in BigQuery under a cost model;
- designing an evaluation methodology for a multi-agent AI system (hand-labelled test sets, Cohen's kappa, majority-class baselines).

## Weekly Log

Weeks run Saturday to Friday, starting on the agreement's first day (1 August). The last week runs to the report date (24-29 October). Hours are my own estimate; I have no separate hours log for this period. The evidence for each week is its dated work folders in `fellows/aishwarya-p/`, where the date in the folder name is when the work was done. Code is linked to the mycroft repository. All video files are in the [Mycroft videos Drive folder](https://drive.google.com/drive/folders/1XbqBd1aPhlHIYKBQBL3cPPeqFzhPYcB6).

### 2026-08-01 - 2026-08-07: Claims and Lineage agents, first video (Mycroft Patent Reader)

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- The first project video, on a two-agent design that reads a patent's claims and its citations.
- A finance-desk concept explainer on the fluency trap in a variance note.

**Evidence folders:** [2026-08-03-patent-claims-lineage-agents](../2026-08-03-patent-claims-lineage-agents/), [2026-08-03-fluency-trap-in-a-variance-note](../2026-08-03-fluency-trap-in-a-variance-note/)

**Videos:** Project Video: Two Agents Read a Patent: Claims and Lineage with Claude. STEM Video: The Fluency Trap in a Variance Note ([Drive folder](https://drive.google.com/drive/folders/1XbqBd1aPhlHIYKBQBL3cPPeqFzhPYcB6))

### 2026-08-08 - 2026-08-14: No dated work folder

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- No dated work folder this week.
- Self-reported: approximately 25–30 hours; work done this week was committed in the 2026-08-28 and 2026-08-31 folders.

**Evidence folders:** none

**Videos:** none

### 2026-08-15 - 2026-08-21: No dated work folder

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- No dated work folder this week.
- Self-reported: approximately 25–30 hours; work done this week was committed in the 2026-08-28 and 2026-08-31 folders.

**Evidence folders:** none

**Videos:** none

### 2026-08-22 - 2026-08-28: Splitting the claims, three finance-data explainers (Mycroft Patent Reader)

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- Progress video 2, on the claim-splitting parser and its stress test.
- Three STEM explainers on financial data pitfalls: survivorship bias, correlation vs. causation, and point-in-time vs. restated data.

**Evidence folders:** [2026-08-28-patent-agent-video2-splitting-claims](../2026-08-28-patent-agent-video2-splitting-claims/), [2026-08-28-survivorship-bias-datasets](../2026-08-28-survivorship-bias-datasets/), [2026-08-28-correlation-vs-causation-signals](../2026-08-28-correlation-vs-causation-signals/), [2026-08-28-pointintime-vs-restated-data](../2026-08-28-pointintime-vs-restated-data/)

**Videos:** Project Video: Splitting the Claims. STEM Videos: Survivorship Bias in Financial Datasets; Correlation vs. Causation in Signal-Finding; Point-in-Time vs. Restated Data ([Drive folder](https://drive.google.com/drive/folders/1XbqBd1aPhlHIYKBQBL3cPPeqFzhPYcB6))

### 2026-08-29 - 2026-09-04: Claims parser, scope classifier and ClaimsAgent (Mycroft Patent Reader)

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- Built the claims parser, which splits claims and classifies each as independent or dependent. Tested against 4 real patents.
- Narrowed the multi-dependency detector to genuine claim-reference patterns.
- Built the claim scope classifier and the ClaimsAgent class.
- Progress videos 3, on the real cost of a query, and 4, on reading the claims.

**Code:** [claims parser](https://github.com/nikbearbrown/mycroft/commit/23f6f47e0bbd3bd4c85be7efaa2c7190f751b300), [multi-dependency fix](https://github.com/nikbearbrown/mycroft/commit/aaa29394e8ae66825e3561d0e332f770c139e7c9), [classifier and ClaimsAgent](https://github.com/nikbearbrown/mycroft/commit/3a89f97797dc545118e2f683047300ab89a9fd85)

**Evidence folders:** [2026-08-31-patent-agent-video3-real-cost-of-a-query](../2026-08-31-patent-agent-video3-real-cost-of-a-query/), [2026-08-31-patent-agent-video4-reading-the-claims](../2026-08-31-patent-agent-video4-reading-the-claims/)

**Videos:** Project Videos: The Real Cost of a Query; Reading the Claims ([Drive folder](https://drive.google.com/drive/folders/1XbqBd1aPhlHIYKBQBL3cPPeqFzhPYcB6))

### 2026-09-05 - 2026-09-11: Broader testing and the start of the Lineage Agent (Mycroft Patent Reader)

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- Broadened domain testing to 3 new patents: found and fixed the `"1 ."` claim-numbering bug, with zero refusals on that batch.
- Started the Lineage Agent: backward citations, and found and fixed the empty-string bug.
- Progress videos 5, on broadening the test, and 6, on starting the lineage agent, plus the Schema Drift explainer.

**Code:** [broader testing](https://github.com/nikbearbrown/mycroft/commit/e99442238a43e1806ecbd425777a817f5fee3715), [Lineage Agent](https://github.com/nikbearbrown/mycroft/commit/ff4b369fde0aabce2bc1b0c63f9def8b0948dd4f)

**Evidence folders:** [2026-09-11-patent-agent-video5-broadening-the-test](../2026-09-11-patent-agent-video5-broadening-the-test/), [2026-09-11-patent-agent-video6-starting-lineage-agent](../2026-09-11-patent-agent-video6-starting-lineage-agent/), [2026-09-11-schema-drift](../2026-09-11-schema-drift/)

**Videos:** Project Videos: Broadening the Test; Starting the Lineage Agent. STEM Video: Schema Drift ([Drive folder](https://drive.google.com/drive/folders/1XbqBd1aPhlHIYKBQBL3cPPeqFzhPYcB6))

### 2026-09-12 - 2026-09-18: The two agents wired together (Mycroft Patent Reader)

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- Broadened Lineage Agent testing to 2 more real patents and confirmed international citation formats.
- Progress video 7, on the two agents wired together, with a real CLI recording.
- STEM explainers: The Finance Agent Market, Right Now, and Why AI Models Refuse.

**Code:** [Lineage Agent testing](https://github.com/nikbearbrown/mycroft/commit/cf4f9f13c01ed09220bde1a86d67aa6061932993)

**Evidence folders:** [2026-09-12-finance-agent-market-2026](../2026-09-12-finance-agent-market-2026/), [2026-09-18-patent-agent-video7-two-agents-wired-together](../2026-09-18-patent-agent-video7-two-agents-wired-together/), [2026-09-18-why-ai-models-refuse](../2026-09-18-why-ai-models-refuse/)

**Videos:** Project Video: The Two Agents, Wired Together. STEM Videos: The Finance Agent Market, Right Now; Why AI Models Refuse ([Drive folder](https://drive.google.com/drive/folders/1XbqBd1aPhlHIYKBQBL3cPPeqFzhPYcB6))

### 2026-09-19 - 2026-09-25: No dated work folder

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- No dated work folder this week.
- Self-reported: approximately 25–30 hours; work done this week was committed in the 2026-09-30 and 2026-10-02 folders.

**Evidence folders:** none

**Videos:** none

### 2026-09-26 - 2026-10-02: From CLI to API, and the React frontend (Mycroft Patent Reader)

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- Built the FastAPI backend wrapping ClaimsAgent and LineageAgent, and updated the README with documentation for `patent_reader.py` and `api.py`.
- Reorganized the project into a backend/frontend split and added the React frontend.
- Progress videos 8, From CLI to API, and 9, Building the Frontend.
- STEM explainers: What Is an Agent Harness? and What Is AI Red Teaming?

**Code:** [FastAPI backend](https://github.com/nikbearbrown/mycroft/commit/f85d17728fdcaba975e133441eb09c7136ec1185), [README](https://github.com/nikbearbrown/mycroft/commit/46af37ce5ada9480822b1d0344ff4aada1c46e62), [backend/frontend split and React](https://github.com/nikbearbrown/mycroft/commit/85c2ce020063de317f3ad6b558dbf841bbc2befa), [load_dotenv](https://github.com/nikbearbrown/mycroft/commit/10df6ba3ff225a2c4cd03e54bb64a2e04a9dd98a)

**Evidence folders:** [2026-09-30-patent-agent-video8-cli-to-api](../2026-09-30-patent-agent-video8-cli-to-api/), [2026-09-30-what-is-an-agent-harness](../2026-09-30-what-is-an-agent-harness/), [2026-10-02-building-the-frontend](../2026-10-02-building-the-frontend/), [2026-10-02-what-is-ai-red-teaming](../2026-10-02-what-is-ai-red-teaming/)

**Videos:** Project Videos: From CLI to API; Building the Frontend. STEM Videos: What Is an Agent Harness?; What Is AI Red Teaming? ([Drive folder](https://drive.google.com/drive/folders/1XbqBd1aPhlHIYKBQBL3cPPeqFzhPYcB6))

### 2026-10-03 - 2026-10-09: No dated work folder

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- No dated work folder this week.
- Self-reported: approximately 25–30 hours; work done this week was committed in the 2026-10-12 folder.

**Evidence folders:** none

**Videos:** none

### 2026-10-10 - 2026-10-16: Hardening the frontend (Mycroft Patent Reader)

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- Hardened the React frontend:
  - three distinct error messages;
  - a loading spinner with a hint for the slow classify path;
  - inputs disabled during a fetch;
  - classify off by default.
- Progress video 10, Hardening the Frontend, and the STEM explainer What Is Prompt Injection?

**Code:** [hardened frontend](https://github.com/nikbearbrown/mycroft/commit/00d3baa65e13b17ba8bb660b0fdef58df52b2bc1)

**Evidence folders:** [2026-10-12-hardening-the-frontend](../2026-10-12-hardening-the-frontend/) ([frictional log](../2026-10-12-hardening-the-frontend/FRICTIONAL.md)), [2026-10-12-what-is-prompt-injection](../2026-10-12-what-is-prompt-injection/)

**Videos:** Project Video: Hardening the Frontend. STEM Video: What Is Prompt Injection? ([Drive folder](https://drive.google.com/drive/folders/1XbqBd1aPhlHIYKBQBL3cPPeqFzhPYcB6))

### 2026-10-17 - 2026-10-23: No dated work folder

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- No dated work folder this week.
- Self-reported: approximately 25–30 hours of local development and debugging.

**Evidence folders:** none

**Videos:** none

### 2026-10-24 - 2026-10-29: Measuring the classifier, and the first baseline (Mycroft Patent Reader)

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- Built the classifier evaluation harness and the BigQuery pull: one query, 161.8 GB, $0.92 at list price, 160 candidate patents. The real data changed the plan: 147 of 160 patents have only 1-3 independent claims, so the set became 50 claims from 16 patents.
- Labelled all 50 claims by hand and ran the baseline (cost upper bound $0.32; actual cost not recorded):
  - Breadth: accuracy 0.66, kappa 0.08.
  - Posture: accuracy 0.60, kappa 0.00.
  - Both fall below the always-most-common-answer baseline.
  - All 50 posture labels are defensive, so posture agreement can't be measured on this set.
- Fixed the refusal bug in `claim_classifier.py`, so a refusal partway through an answer is now treated as declined, and all 50 claims score.
- Progress videos 11, Measuring the Classifier, and 12, What the Baseline Found. STEM explainers: What Is RLHF? and How AI Agents Are Changing Payments.

**Code:** [harness, labels, baseline and refusal fix](https://github.com/nikbearbrown/mycroft/commit/3bcf1b1cea28265bb89bfea85f4034b6b7da37f0)

**Evidence folders:** [2026-10-28-patent-agent-video11-classifier-eval-harness](../2026-10-28-patent-agent-video11-classifier-eval-harness/) ([frictional log](../2026-10-28-patent-agent-video11-classifier-eval-harness/FRICTIONAL.md)), [2026-10-29-patent-agent-video12-baseline-results](../2026-10-29-patent-agent-video12-baseline-results/) ([frictional log](../2026-10-29-patent-agent-video12-baseline-results/FRICTIONAL.md)), [2026-10-29-what-is-rlhf](../2026-10-29-what-is-rlhf/), [2026-10-29-how-ai-agents-are-changing-payments](../2026-10-29-how-ai-agents-are-changing-payments/)

**Videos:** Project Videos: Measuring the Classifier; What the Baseline Found. STEM Videos: What Is RLHF?; How AI Agents Are Changing Payments ([Drive folder](https://drive.google.com/drive/folders/1XbqBd1aPhlHIYKBQBL3cPPeqFzhPYcB6))

---

**Total: ~325-390 hours across 13 weeks (self-reported, ~25-30 per week).** Eight weeks have dated work folders; five weeks (8-14 Aug, 15-21 Aug, 19-25 Sep, 3-9 Oct, 17-23 Oct) have none.

## Next period

- **Prompt fix and re-measurement.** Make one prompt change so functional wording alone does not count as broad, and posture is judged separately from breadth. Then re-run the 50 claims and compare the two runs with the harness. Target date: 2026-11-15.
- **Better posture coverage.** Add offensive and broad claims to the test set, so posture agreement can actually be measured. Target date: 2026-11-15.

## Outstanding issues

- **Hours** are self-reported estimates, not a documented hours log. Five weeks have no dated work folder.
- **Supervisor:** the supervisor for 1 August - 11 October isn't stated, and no supervisor feedback evidence is linked.
- **Videos** are linked to one Drive folder rather than to each video.
- **Baseline cost:** the actual cost wasn't recorded; the harness logged only the $0.32 upper bound.
- **Open items on the patent system:** deployment hasn't started, forward citations are deferred, and the zero-citation case is still untested.
