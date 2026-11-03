# Fellowship Renewal — Ushasvi Rachel Peeka
Fellow: Ushasvi Rachel Peeka Project: Causal Couture 
Current agreement end date: October 31, 2026 
Requested renewal period: November 1, 2026 - December 31 2026 
Project Manager / Supervisor: Shourya
Video Review: Sanjana


## Renewal Request
I am requesting renewal of my Humanitarians.ai fellowship following the completion of my current agreement on October 31, 2026.
During this reporting period, I continued development of the Causal Couture project, focusing on analytical system development, decision intelligence, causal-analysis reliability, evidence interpretation, validation, documentation, and reproducible reporting.
I also completed weekly Brutalist video work, including Causal Couture progress reports and, beginning later in the reporting period, STEM/AI educational videos. Video deliverables were produced in horizontal and vertical formats where applicable.
My weekly work hours were documented in ADAMS and met or exceeded 20 hours for each completed reporting week.

## Executive Summary
During this fellowship period, I progressed Causal Couture from an analytical and scenario-based prototype toward a more structured causal evidence and reliability workflow.
My main contributions included:
1. extending the Phase 5 causal-analysis workflow with sensitivity and reliability diagnostics;
2. developing a structured methodology for interpreting multiple causal diagnostics together;
3. implementing a reproducible evidence-review workflow with automated testing;
4. producing weekly Causal Couture progress videos and STEM/AI educational videos using Brutalist;
5. maintaining supporting project documentation, source files, beat sheets, and GitHub submissions.
The later Week 7–12 Humanitarians.ai reporting materials have been submitted through GitHub Pull Request #258 and are currently pending repository review and merge.

## Completed Results
Result 1 - Phase 5 Causal Reliability and Sensitivity Framework
I extended Causal Couture's causal-analysis workflow with additional reliability diagnostics and sensitivity analysis.
This work included:
* unobserved-confounding sensitivity analysis;
* evaluation of how estimated effects behave under increasingly strong hypothetical hidden-confounding scenarios;
* structured handling of secondary diagnostic failures;
* diagnostic-error reporting;
* reconciliation of multiple causal reliability signals;
* integration of reliability information into the broader causal intelligence workflow.
My contribution included integrating these capabilities into Causal Couture, organizing the implementation, reviewing diagnostic behavior, and documenting methodological limitations so that diagnostic results were not presented as proof of causation.
Supporting evidence
Relevant implementation files include:
* apps/api/causal_sensitivity.py
* apps/api/causal_intelligence.py
* apps/api/causal_reliability_review.py
* apps/api/main.py
Additional supporting evidence is included in the Week 9 and Week 10 project/video materials submitted in:
[GitHub Pull Request #258 ](https://github.com/nikbearbrown/humanitarians-youtube/pull/258)
Limitation
The sensitivity analysis is a diagnostic stress test rather than a formal statistical sensitivity bound. The reliability framework supports interpretation but does not establish causation or automatically approve business decisions.

Result 2 - Causal Evidence Interpretation and Decision-Readiness Methodology
I developed a structured methodology for interpreting causal evidence collectively instead of relying on a single model estimate or diagnostic.
The framework distinguishes:
* diagnostic execution status from evidence interpretation;
* successful, inconclusive, unavailable, and failed diagnostic execution;
* reassuring, cautionary, mixed, and undetermined evidence signals.
It also addresses disagreements between:
* row-level and cluster bootstrap uncertainty;
* primary estimates and temporal placebo tests;
* robustness diagnostics and synthetic-confounding sensitivity;
* estimated effects and inventory, overlap, or stockout limitations.
The methodology also introduced conservative decision-readiness concepts such as:
* Insufficient Evidence for Action;
* Analyst Review Required;
* Exploratory Interpretation Only.
This work maintains a clear distinction between descriptive analytics, scenario simulation, and observational causal estimation.
Supporting evidence
* docs/week11_causal_evidence_decision_readiness.md
* Causal Couture Week 11 supporting materials
* Week 11 progress video
* Week 11 project files included in:
[GitHub Pull Request #258](https://github.com/nikbearbrown/humanitarians-youtube/pull/258)
Limitation
This stage focused on methodology and interpretation. It did not introduce a new causal estimator or claim empirical proof of a causal relationship.

Result 3 - Reproducible Causal Evidence Review and Automated Validation
I translated the Week 11 evidence-interpretation methodology into a reproducible Python evidence-review workflow.
The implementation evaluates analytical conditions including:
* missing diagnostic results;
* failed diagnostics;
* bootstrap uncertainty;
* disagreement between uncertainty estimates;
* unobserved-confounding sensitivity;
* treatment overlap;
* stockout-related warnings;
* incomplete or unavailable evidence.
The workflow can produce structured Markdown and JSON evidence-review outputs.
I also added and executed an automated test suite covering nine evidence-review scenarios.
Local validation result: 9 of 9 tests passed with 0 failures.
Supporting evidence
Relevant implementation files include:
* apps/api/causal_evidence_review.py
* apps/api/run_week12_evidence_review.py
* apps/api/test_week12_evidence_review.py
* docs/WEEK12_INSTALL_AND_RUN.txt
The Week 12 Humanitarians.ai reporting materials are included in:
[GitHub Pull Request #258](https://github.com/nikbearbrown/humanitarians-youtube/pull/258)

Limitation
The automated tests validate the implemented software paths but do not establish scientific validity of the underlying causal estimates.
Full generation and interpretation of the evidence-review workflow using a sufficiently populated real unified retail dataset remains an outstanding validation step.

## Project Demonstration — Causal Couture

The screenshots below show the current Causal Couture interface and provide visual evidence of the analytical workflow, decision-support features, scenario simulation, and causal intelligence components described in the completed-results section.

### Causal Couture Overview

<img width="1470" height="832" alt="Screenshot 2026-10-20 at 2 32 33 PM" src="https://github.com/user-attachments/assets/aa2fed34-f5aa-4421-97d5-3d243fb17543" />

*Current Causal Couture overview showing the end-to-end workflow from data upload and validation through analysis, simulation, and decision support.*

### Current Signals Dashboard

<img width="1470" height="832" alt="Screenshot 2026-10-20 at 2 33 06 PM" src="https://github.com/user-attachments/assets/6b5fdeda-f642-4b42-a07c-faef46c3e208" />


*Current signals dashboard displaying demand pressure, stock risk, engagement, conversion, overall signal, and recent-period movement.*

### Decision Intelligence

<img width="1470" height="832" alt="Screenshot 2026-10-20 at 2 34 17 PM" src="https://github.com/user-attachments/assets/569492e1-5c22-43e8-8b63-4f2229d24101" />


*Decision-support interface showing the current recommendation, confidence level, dataset summary, and the transition into scenario analysis.*

### Scenario Lab


<img width="1470" height="832" alt="Screenshot 2026-10-20 at 2 34 33 PM" src="https://github.com/user-attachments/assets/2cfa6f89-0b00-40de-a1dc-3d055ea67af7" />

*Scenario Lab interface for adjusting demand, inventory, engagement, and conversion assumptions and comparing simulated outcomes against the current baseline.*

### Causal Intelligence

<img width="1470" height="832" alt="Screenshot 2026-10-20 at 2 34 54 PM" src="https://github.com/user-attachments/assets/fad20dd6-54e7-4d27-af11-cc0d4e78d4f5" />

*Phase 5 causal intelligence interface showing the observational effect-estimation workflow, evidence status, bootstrap availability, treatment definition, and outcome definition.*

## Hours Status
Weekly work hours were documented in ADDAMS throughout the reporting period.
The work included:
* Causal Couture research and development;
* causal-analysis implementation and review;
* testing and validation;
* technical documentation;
* Brutalist video research and production;
* horizontal and vertical video preparation;
* video review and revisions;
* GitHub documentation and reporting.
Reporting period	Actual hours	Hours record
Aug 3–9	25	ADDAMS
Aug 10–16	30	ADDAMS
Aug 17–23	30+	ADDAMS
Aug 24–30	25	ADDAMS
Aug 31–Sep 6	29	ADDAMS
Sep 7–13	25	ADDAMS
Sep 14–20	30	ADDAMS
Sep 21–27	28	ADDAMS
Sep 28–Oct 4	32	ADDAMS
Oct 5–11	32	ADDAMS
Oct 12–18	28	ADDAMS
All completed reporting weeks listed above document at least 20 hours of work.
The week beginning October 19 is still in progress and is not included as a completed weekly total.

## Video Evidence
Final rendered video deliverables are stored in Google Drive.
Video evidence folder: Humanitarians.ai Video Deliverables
During the earlier part of the reporting period, the primary weekly video output was the Causal Couture progress report.
Beginning later in the fellowship period, the weekly video structure expanded to include:
* one Causal Couture progress video;
* one STEM/AI educational video;
* 16:9 horizontal versions;
* 9:16 vertical versions where applicable.
Direct individual video links will be added to the weekly evidence index before submission where available.

## Frictional Log Status
I did not maintain separate contemporaneous Frictional logs during this reporting period.
My work is instead supported by:
* ADDAMS weekly hour records;
* weekly video deliverables;
* project documentation;
* source code;
* beat sheets;
* GitHub history;
* project files;
* the pending Week 7–12 Humanitarians.ai GitHub submission.
I understand that the Frictional log is now part of the fellowship reporting requirements. This is a reporting gap in my current submission, and I will maintain dated Frictional logs contemporaneously during the next fellowship period if my renewal is approved.
I have not retroactively created logs and presented them as contemporaneous records.

## Weekly Evidence Index

| Dates | Hours | STEM / AI video | Causal Couture progress video | Frictional log status | Work evidence |
|---|---:|---|---|---|---|
| Aug 3–9 | 25 | N/A - earlier reporting format | [Progress video](https://drive.google.com/file/d/19kGIQTKtihcHHEgaI50I3oYOkPP3uLI8/view?usp=share_link) | Not maintained | Existing Week 1 project files in fellows folder |
| Aug 10–16 | 30 | N/A - earlier reporting format | [Progress video](https://drive.google.com/file/d/1V-aJ2Jfg_t7lx7dL5bS1owENZNhQ0Da1/view?usp=share_link) | Not maintained | Existing Week 2 project files in fellows folder |
| Aug 17–23 | 30+ | N/A - earlier reporting format | [Progress video](https://drive.google.com/file/d/1VMNkgEEzfT2YFzfms9wdhQyZxUUvGUSZ/view?usp=share_link) | Not maintained | Existing Week 3 project files in fellows folder |
| Aug 24–30 | 25 | N/A - earlier reporting format | [Progress video](https://drive.google.com/file/d/1pJwO-wp81JScwULIWp95vLS-lyeywucN/view?usp=share_link) | Not maintained | Existing Week 4 project files in fellows folder |
| Aug 31–Sep 6 | 29 | [STEM / AI video 1](https://drive.google.com/file/d/1B5GsoB6O4YOusyOit2F31X7AOba8pt1t/view?usp=share_link) · [STEM / AI video 2](https://drive.google.com/file/d/1Ua5Z2thOCI7J98kA-0vKG1wbjs0bnL0y/view?usp=share_link) | [Progress video](https://drive.google.com/file/d/1lH5X57LTIz_OvqR5aiKm89rQyLUNwmup/view?usp=share_link) | Not maintained | Existing Week 5 / STEM project evidence |
| Sep 7–13 | 25 | [STEM / AI video 1](https://drive.google.com/file/d/1vqWfNlP6S7lBbgUivJLeUkLejwrjtrVg/view?usp=share_link) · [STEM / AI video 2](https://drive.google.com/file/d/1fOm45_GWMDC7brzLun9cbxjNG32jFAhv/view?usp=share_link) | [Progress video 1](https://drive.google.com/file/d/1rJObXH6evk-ht9Qlvx7-1yBtVJIGbv9I/view?usp=share_link) · [Progress video 2](https://drive.google.com/file/d/1yavl88NG34PsZoco5_ue6Xkb9XEyY8ym/view?usp=share_link) | Not maintained | Existing Week 6 project evidence |
| Sep 14–20 | 30 | [STEM / AI video 1](https://drive.google.com/file/d/1bdTX8HJGS57g5F1vR4tb0MzlI9OyFKzp/view?usp=share_link) · [STEM / AI video 2](https://drive.google.com/file/d/1VNUr2y4gs0AzSgUikU5Qk6lM6MQVRDke/view?usp=share_link) | [Progress video 1](https://drive.google.com/file/d/1Gua-3J-zLdrswH52862RKRggXyAswZ9x/view?usp=share_link) · [Progress video 2](https://drive.google.com/file/d/1ESA3pPTXkmHIdE2ZvpKfVixqz_oNzpU_/view?usp=share_link) | Not maintained | Week 7 materials - PR #258 pending review |
| Sep 21–27 | 28 | [STEM / AI video 1](https://drive.google.com/file/d/1t8C3QvXraOcte-7qZvIEx8n1OutzhBAv/view?usp=share_link) · [STEM / AI video 2](https://drive.google.com/file/d/1xhBmhwOx3UYep-1I1Dbyw-bqmnN7aAPh/view?usp=share_link) | [Progress video 1](https://drive.google.com/file/d/1pnXP_28kG785x7o9pEQmDrxGvJn6AF7G/view?usp=share_link) · [Progress video 2](https://drive.google.com/file/d/1w5r-qyFzXEmIsnkbsikoCMU5mz_B8Lo9/view?usp=share_link) | Not maintained | Week 8 materials - PR #258 pending review |
| Sep 28–Oct 4 | 32 | [STEM / AI video 1](https://drive.google.com/file/d/12Su6hX8wYTDf0ezpWf3BZC-GVuhGGY4S/view?usp=share_link) · [STEM / AI video 2](https://drive.google.com/file/d/1un-8VDpGVy4BIBdfPjJ6xDtn6-QB_h19/view?usp=share_link) | [Progress video 1](https://drive.google.com/file/d/18PK9EB4jY7jpU7TEtrDHMnRL5pHqSFKT/view?usp=share_link) · [Progress video 2](https://drive.google.com/file/d/1K9P7ByleAHgoRHb4e2Tl80FbvYcWTeib/view?usp=share_link) | Not maintained | Week 9 materials - PR #258 pending review |
| Oct 5–11 | 32 | [STEM / AI video 1](https://drive.google.com/file/d/1n58eJ4kwPR3F1AWtSJjTbemdF3Oml_S7/view?usp=share_link) · [STEM / AI video 2](https://drive.google.com/file/d/1Aa48eAoD4AQN9PU6n90apUqCGwWN1dUg/view?usp=share_link) | [Progress video 1](https://drive.google.com/file/d/1Kr7i4pkNw0sAPrQXpz6qyvwe3Ff-J0Ad/view?usp=share_link) · [Progress video 2](https://drive.google.com/file/d/1FnPXZ2Xd34Jq0y55lT-BN9P1hHQ9qI_O/view?usp=share_link) | Not maintained | Week 10 materials - PR #258 pending review |
| Oct 12–18 | 28 | [STEM / AI video 1](https://drive.google.com/file/d/1z53043NcHJ9BwVhBZX57PcWM6QdOrRqS/view?usp=share_link) · [STEM / AI video 2](https://drive.google.com/file/d/1jZFnZRALmJcImq9LLOt_5i5hCaevVZQI/view?usp=share_link) | [Progress video 1](https://drive.google.com/file/d/13ztsV3JiBE71yGO7X4HJFowfTQcqxlAi/view?usp=share_link) · [Progress video 2](https://drive.google.com/file/d/1c3zWGejLE0bDS0xDIioxh4XIkOB8VRJu/view?usp=share_link) · [Progress video 3](https://drive.google.com/file/d/1u8426rLTl6NMKVJXXeNFuNGcTZUt_yrU/view?usp=share_link) · [Progress video 4](https://drive.google.com/file/d/1rG_NrHfN-fe48xuJRxZcflKJm7-w-i4j/view?usp=share_link) | Not maintained | Week 11–12 materials - PR #258 pending review |

### Later-period GitHub submission

The Week 7–12 Humanitarians.ai reporting materials have been submitted through:

[Pull Request #258 — Add Ushasvi Rachel video updates for Weeks 7–12](https://github.com/nikbearbrown/humanitarians-youtube/pull/258)

These files are pending repository review and merge and therefore may not yet appear in the `main` branch of my fellows folder.

## Degree Relevance and Supervision
This work relates to my degree through the application of:
* data analysis;
* software development;
* causal inference concepts;
* model evaluation;
* analytical system design;
* testing;
* technical documentation and communication.
Degree / program: Bryant University, Master of Science in Business Analytics
Supervisor / Project Manager: Shourya, Sanjana(Video reports)

## Authorization
Authorization type: F1 Post Completion OPT
Authorization dates: February 18 2026 - February 17 2027
Current Humanitarians.ai agreement: Through October 31, 2026.

## Next-Period Plan
I plan to continue and finish Causal Couture with the following deliverables.
1. Real-Dataset Validation
Run the current causal evidence-review workflow on a sufficiently populated unified SKU-level dataset.
The goal is to determine whether the current workflow produces interpretable results or identifies specific data and identifiability limitations.
2. Reproducible Evidence Reports
Generate and review actual Markdown and JSON evidence reports containing:
* diagnostic execution statuses;
* uncertainty findings;
* sensitivity results;
* caution flags;
* unresolved limitations.
3. API Integration
Expose the evidence-review functionality through the project API layer and add integration testing for complete, incomplete, and failed diagnostic responses.
4. Analyst-Facing Evidence Dashboard
Develop an analyst-facing interface displaying:
* evidence classifications;
* uncertainty intervals;
* diagnostic warnings;
* reliability signals;
* observational-analysis disclaimers.
5. End-to-End Validation and Demonstration
Validate the workflow from dataset input through evidence review and document a reproducible end-to-end process.
Where appropriate, prepare a short demonstration of the completed workflow and its methodological limitations.

## Outstanding Issues
1. Separate contemporaneous Frictional logs were not maintained during the current reporting period.
2. Week 7–12 Humanitarians.ai reporting files are currently submitted through Pull Request #258 and are pending repository review/merge.
3. Full real-dataset validation of the Week 12 evidence-review workflow remains incomplete.
I will address the Frictional-log reporting requirement prospectively by maintaining dated logs during the next renewal period.
