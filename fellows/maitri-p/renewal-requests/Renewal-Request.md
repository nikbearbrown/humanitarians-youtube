# Fellowship Renewal Request — Maitri P.

- **Fellow:** Maitri Pasale. [@maitripasale](https://github.com/maitripasale)
- **Role:** AI Software Engineer
- **Project:** RL_Environment
- **Current agreement:** **09/11/2026** – **10/31/2026**
- **Requested action:** Agreement Renewal / Continuation
- **Supervising Faculty / Coordinators:** Prof. Nik Bear Brown, Dev Shah, Dhruv
- **Fellow folder:** [fellows/maitri-p](../README.md)

## Executive summary

Please consider continuing my fellowship with Humanitarians AI after my current agreement ends on **October 31, 2026**. I have reported **100 hours across five weeks**. Those hours are reconstructed estimates from my work and dated records, rather than contemporaneous time logs. My work has focused on building and evaluating external memory for the Pi agent, followed by a new Policy Decompilation research assignment connected to Optimus.

My main accomplishments during this period are:

1. **Built a testable Pi memory workflow.** I studied the agent's prompt–tool–result loop, set up repeatable runs with recorded prompts, tool calls, outcomes, timing and token usage, and worked on the procedural and metacognitive memory conditions. This gave me a way to inspect what the agent actually did across separate sessions.
2. **Ran and checked a memory pilot.** After three practice questions were used to build frozen lessons, I compared no memory, procedural memory, metacognitive memory and both types on six held-out questions. All numeric answers were correct. Mean tool calls were **6.00, 4.33, 5.00 and 6.83**, respectively. I corrected an evidence-scoring issue across all conditions, then reviewed the runs task by task and found that one difficult question accounted for much of the apparent efficiency gain. With one repetition, these are useful early signals, not a proven improvement.
3. **Scoped the next research problem.** I began Policy Decompilation by reviewing how a small trained model's choices might be represented as readable rules. I identified action agreement, task performance and rule simplicity as starting comparison measures and discussed the broader Optimus goal in meeting. This track is still at the research stage; I have not trained a model or reported an experimental result for it.

In the next period, I plan to establish a small reproducible Policy Decompilation baseline, extract an initial set of rules and test where they match or fail to match the original model. The [Pi memory research code](https://github.com/maitripasale/pi-memory-search) and linked weekly evidence show the work completed so far; some video uploads are still being added.

## Completed results

1. **Recorded memory pilot (Week 3).** I built a multi-hop pilot — 3 practice questions, then 6 unseen questions under no memory, procedural, metacognitive and both, one repetition each — with memory generated only from practice and then frozen. I also found and corrected an evidence-scoring rule that wrongly rejected valid citations, applied uniformly across conditions. Result: mean tool calls 6.00 / 4.33 / 5.00 / 6.83; metacognitive 0 tool errors vs 2; all numeric answers correct.
   Evidence: [Work report](../2026-10-09-pi-memory-pilot/WORK-REPORT.md) · [Project report and videos](../2026-10-09-pi-memory-pilot/README.md) · [Fact-check](../2026-10-09-pi-memory-pilot/FACTCHECK.md)

2. **Task-level re-analysis (Week 4).** I checked the same saved runs question by question and found one task (12 calls and 2 KeyErrors without memory, 3 calls with the metacognitive lesson) accounted for much of the average gain. Finding: storing a lesson is only part of the problem; retrieving it when it fits matters as much.
   Evidence: [Work report](../2026-10-23-pi-memory-task-review/WORK-REPORT.md) · [Project report and videos](../2026-10-23-pi-memory-task-review/README.md) · [Fact-check](../2026-10-23-pi-memory-task-review/FACTCHECK.md)

3. **New Policy Decompilation track (Week 5, scoping only).** I reviewed the proposed workflow for extracting readable decision rules from a small trained model, identified action agreement, task performance and rule simplicity as possible evaluation measures, and discussed the broader Optimus motivation with Dev. Explaining decisions and improving reasoning are separate goals; the success threshold and implementation path remain open. No model training, rule extractor or validated result is claimed. The Week 5 work report and Frictional log will be linked here when they are written.

## Hours status

| Week / dates | Hours | Progress / workflow | Brutalist videos | Meetings | Documentation |
|---|---:|---:|---:|---:|---:|
| Week 1 · Sep 21 – Sep 27 | 20 | 15 | 4 | 0 | 1 |
| Week 2 · Sep 28 – Oct 4 | 20 | 12 | 5 | 0 | 3 |
| Week 3 · Oct 5 – Oct 11 | 20 | 14 | 2 | 1 | 3 |
| Week 4 · Oct 12 – Oct 18 | 20 | 15 | 2 | 1 | 2 |
| Week 5 · Oct 19 – Oct 25 | 20 | 12 | 5 | 1 | 2 |
| **Total** | **100** | **69** | **17** | **3** | **11** |

## Evidence

### Pi memory research code

The public repository includes the [Jupyter REPL extension](https://github.com/maitripasale/pi-memory-search/blob/main/extensions/jupyter-repl.ts), which lets Pi write and run Python search code; the [memory store](https://github.com/maitripasale/pi-memory-search/blob/main/search_research/memory.py), which records and retrieves lessons from practice runs; and the [multi-hop experiment runner](https://github.com/maitripasale/pi-memory-search/blob/main/search_research/run_multihop.py), which compares fresh runs under four memory conditions. The [fixture builder](https://github.com/maitripasale/pi-memory-search/blob/main/search_research/build_multihop.py), [run dashboard](https://github.com/maitripasale/pi-memory-search/blob/main/search_research/dashboard.py), and [tests](https://github.com/maitripasale/pi-memory-search/tree/main/search_research/tests) show how I built, inspected, and checked the workflow. The [pilot report](https://github.com/maitripasale/pi-memory-search/blob/main/search_research/MULTIHOP_EXPERIMENT.md) and [task-level analysis](https://github.com/maitripasale/pi-memory-search/blob/main/search_research/WEEK3_ANALYSIS.md) document the results and their limits.

### STEM topics

| Week | Video topic | Source and work records |
|---|---|---|
| Week 1 · Sep 21 – Sep 27 | [Noise Cancellation — why noise-cancelling headphones work](../2026-10-23-noise-cancelling-headphones/README.md) | [Beat sheet](../2026-10-23-noise-cancelling-headphones/beat_sheet.json) · [Frictional log](../2026-10-23-noise-cancelling-headphones/FRICTIONAL.md) · [Fact-check](../2026-10-23-noise-cancelling-headphones/FACTCHECK.md) |
| Week 2 · Sep 28 – Oct 4 | [How Agents Use Tools](../2026-10-02-agents-use-tools/README.md) | [Beat sheet](../2026-10-02-agents-use-tools/beat_sheet.json) · [Work report](../2026-10-02-agents-use-tools/WORK-REPORT.md) · [Frictional log](../2026-10-02-agents-use-tools/FRICTIONAL.md) · [Fact-check](../2026-10-02-agents-use-tools/FACTCHECK.md) |
| Week 3 · Oct 5 – Oct 11 | [DynamoDB Hot Partitions — why a table can throttle despite spare capacity](../2026-10-23-dynamodb-hot-partition/README.md) | [Beat sheet](../2026-10-23-dynamodb-hot-partition/beat_sheet.json) · [Frictional log](../2026-10-23-dynamodb-hot-partition/FRICTIONAL.md) · [Fact-check](../2026-10-23-dynamodb-hot-partition/FACTCHECK.md) |
| Week 4 · Oct 12 – Oct 18 | [AWS Lambda Cold Starts — why the first request can be slower](../2026-10-23-lambda-cold-start/README.md) | [Beat sheet](../2026-10-23-lambda-cold-start/beat_sheet.json) · [Frictional log](../2026-10-23-lambda-cold-start/FRICTIONAL.md) · [Fact-check](../2026-10-23-lambda-cold-start/FACTCHECK.md) |
| Week 5 · Oct 19 – Oct 25 | [How GPS Knows Where You Are — your phone listens to satellites](../2026-10-23-gps-how-it-works/README.md) | [Beat sheet](../2026-10-23-gps-how-it-works/beat_sheet.json) · [Frictional log](../2026-10-23-gps-how-it-works/FRICTIONAL.md) · [Fact-check](../2026-10-23-gps-how-it-works/FACTCHECK.md) |

### Progress and research updates

| Week | Update | Work and research evidence |
|---|---|---|
| Week 1 · Sep 21 – Sep 27 | [How Pi Works](../2026-09-21-pi-week1-onboarding/README.md) | [Work report](../2026-09-21-pi-week1-onboarding/WORK-REPORT.md) · [Frictional log](../2026-09-21-pi-week1-onboarding/FRICTIONAL.md) · [Beat sheet](../2026-09-21-pi-week1-onboarding/beat_sheet.json) |
| Week 2 · Sep 28 – Oct 4 | [Memory Systems for Pi](../2026-10-03-pi-agent-memory/README.md) | [Work report](../2026-10-03-pi-agent-memory/WORK-REPORT.md) · [Frictional log](../2026-10-03-pi-agent-memory/FRICTIONAL.md) · [Fact-check](../2026-10-03-pi-agent-memory/FACTCHECK.md) |
| Week 3 · Oct 5 – Oct 11 | [Pi Memory Pilot](../2026-10-09-pi-memory-pilot/README.md) | [Work report](../2026-10-09-pi-memory-pilot/WORK-REPORT.md) · [Frictional log](../2026-10-09-pi-memory-pilot/FRICTIONAL.md) · [Pilot evidence](../2026-10-09-pi-memory-pilot/evidence.json) · [Fact-check](../2026-10-09-pi-memory-pilot/FACTCHECK.md) |
| Week 4 · Oct 12 – Oct 18 | [Memory Task Review](../2026-10-23-pi-memory-task-review/README.md) | [Work report](../2026-10-23-pi-memory-task-review/WORK-REPORT.md) · [Frictional log](../2026-10-23-pi-memory-task-review/FRICTIONAL.md) · [Run evidence](../2026-10-23-pi-memory-task-review/evidence.json) · [Fact-check](../2026-10-23-pi-memory-task-review/FACTCHECK.md) |
| Week 5 · Oct 19 – Oct 25 | [Policy Decompilation scope](../2026-10-23-policy-decompilation-scope/README.md) | [Frictional log](../2026-10-23-policy-decompilation-scope/FRICTIONAL.md) · [Beat sheet](../2026-10-23-policy-decompilation-scope/beat_sheet.json) · [Fact-check](../2026-10-23-policy-decompilation-scope/FACTCHECK.md) · [Completed results](#completed-results) |

## Drive link

All rendered videos (landscape and vertical, organized by week): [Google Drive Link](https://drive.google.com/drive/folders/1DwIjHC56x7hRwdh6-sWaPyjjEjimDhjg?usp=sharing)

Each project README above also links its individual landscape and vertical files.

## Degree relevance and supervision

- **Degree relevance:** **[MS in Computer Software Engineering / STEM]**. The Pi work involves software engineering, agent evaluation and controlled experiments; the Policy Decompilation work involves model-behavior analysis and evaluation. Confirm how both relate to the degree named in my authorization records.

## Next period plan

- Set up a small, reproducible Policy Decompilation baseline with a trained model and an environment such as CartPole.
- Record the model's decisions across different states, then look for patterns that can be expressed as readable rules.
- Compare the rules with the original model on action agreement, task performance and simplicity; document where the rules fail.
- Use the baseline findings to clarify what this approach can explain about model behavior and what further work would be needed before applying it to Optimus.