Two Customers, One Run: Writing a Pipeline's Results for a Program and a Person

Every run of a pipeline ends in front of two readers: the program that carries on from it, and the person who has to decide. They need different pages. In one open-source finance workflow I built both from the same set of facts: an agent log of sixteen fields for the next script, and a human report of fifteen sections for the person deciding. The video follows one fact through both pages, a count (twelve requests read), a reason (a portfolio whose weights add up to zero) and a call (approve the next phase, ask for fixes, or block live use), and shows what happened when I read my own log the way its reader would. It ends on a question to take to your own pipeline: who reads its last output next, what do they do with it, and what has to be on their page so they can do it? This week I contributed to Mycroft so that a sample run ends with both pages, and a check keeps them agreeing.

Chapters:
0:00 Hello, and what this week is
0:13 One fact, written down twice
0:26 The recipe
0:40 Two readers
1:00 The machine's desk
1:17 The person's desk
1:32 A count, followed
1:50 A reason, followed
2:10 A call, followed
2:29 Reading both pages as a person
2:48 The fix
3:06 What keeps the pages agreeing
3:24 Your turn
3:40 Where the recipe stands and sign-off

The contribution:
nikbearbrown/mycroft pull request #81 (merged): the Scenario Stress Testing Agent recipe, steps 4 and 6 closed in sample mode. A quality check that re-derives every stress result and reconciles it on 14 checks, then the recipe's Output Contract for each run: a 16-field agent log and a 15-section human report, for a clean set and for a set of ten deliberately flawed requests. It builds on pull request #74 (steps 1, 3 and 5).
https://github.com/nikbearbrown/mycroft/pull/81
Pull request #82 (merged) is the correction that came from reading both pages: each of the four stop conditions is now judged from evidence, the report says how many triggered, and four new checks guard it (30 of 30 pass).
https://github.com/nikbearbrown/mycroft/pull/82
The recipe stays a draft on purpose: three items are still open, and nothing calls a model, a market-data service or a database.

What this video claims, and what it does not:

- Every request is invented; the figures are sample arithmetic, not predictions about any company. Nothing here is investment advice.
- The clean sample run reads 12 requests, accepts 12, stress-tests 11 and stops 1 at a recorded hand-off; the 11 reconcile on 14 checks with no failures or duplicates. The agent log has 16 fields; the human report has 15 sections.
- The flawed set has 10 requests, all rejected at step 3 (the data-shape check), each with a reason; one of them, a portfolio whose weights total 0.0, carries the same reason line in the log and in the report.
- The report's recommendation is computed from the run's files: on the clean set approve (sample mode only) YES, request fixes NO, block live execution YES; on the flawed set approve NO, fixes YES, block YES.
- What I found by reading both pages: stop condition 1 (credentials hardcoded) was recorded as triggered in the pull request 81 version because the check matched its own source line, and the report did not mention stop conditions. Pull request 82 judges each condition from evidence; the report line now reads "Stop conditions: 0 of 4 triggered".
- Run from a clean copy of the repository with the date pinned, the two commands give the same agent log, report and quality-check file as the ones committed (checked by comparing them byte for byte).

Source: the merged repository (nikbearbrown/mycroft, main after pull request 82). Every figure on screen is read from files in it, and the files are named on screen.

Narration is a synthetic voice (Kokoro, run locally). Visuals are original code-drawn animations: no third-party images, recordings or music, and open-licence fonts only (EB Garamond, Inter, PT Mono).

Humanitarians AI - @HumanitariansAI
Tanmay Kulkarni, in for Humanitarians AI

Tags: pipeline reports, agent log, human report, logging for agents and humans, open source finance, stress testing, Mycroft, verification, Python, explainer, Humanitarians AI
