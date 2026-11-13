# SurveyMind Response Pattern Realism Study (Madison) — Renewal Request

**Request:** I'm requesting a fellowship renewal from October 1, 2026 through November 30, 2026. My current agreement ends September 30, 2026, and this summary covers the period from August 25 to September 30, 2026.

**Completed:**
- Built and validated a full statistical validation pipeline (Tucker's congruence coefficient, Jennrich test, bootstrap confidence intervals, per-trait KS test) for the SurveyMind Response Pattern Realism Study, tested against self-built known-outcome cases (0.9831 PASS / 0.5946 FAIL)
- Cleaned and validated the real Open Psychometrics human dataset (603,322 respondents) and independently verified the dataset's reverse-item scoring list against real response data (all 50 items consistent)

## Weekly Evidence Index

| Week / dates | Hours | Video links | Description |
|---|---|---|---|
| Aug 25–29 | 12 hrs | – | Completed Addams onboarding intake, submitted the initial proposal, and went through CRITIQ review. |
| Sep 1–5 | 21 hrs | [Drive](https://drive.google.com/drive/folders/1ZrBY5hKfTi5Iwr8dSk3f_hi8cFpMnbOS) · [Project Progress video](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/asheesh-n/SurveyMind%20-%201) · [AI Topic — Risk Classification in Financial Documents using AI](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/asheesh-n/SEC%20-%20AI%20Topic) | Pitched to Komal and Prof. Nina; confirmed the demographic-conditioning question; completed the agreement and HR onboarding (ID 275). |
| Sep 8–12 | 20 hrs | [Drive](https://drive.google.com/drive/folders/1ZrBY5hKfTi5Iwr8dSk3f_hi8cFpMnbOS) · [Project Progress video](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/asheesh-n/SurveyMind%20-%202) · [AI Topic — Multi-Token Attention](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/asheesh-n/MTA%20-%20AI%20Topic) | Gained clarity on the problem and reviewed gaps in the work completed so far. |
| Sep 15–19 | 22 hrs | [Project Progress — GitHub](https://github.com/asheeshnellutla92/surveymind-response-realism-study) · [Project Progress video](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/asheesh-n/SurveyMind%20-%20) · [AI Topic — Agent Orchestration](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/asheesh-n/Agent%20Orchestration%20-%20AI%20Topic) · [Drive](https://drive.google.com/drive/folders/1ZrBY5hKfTi5Iwr8dSk3f_hi8cFpMnbOS) | Built and validated the full pipeline; wrote and submitted a retroactive SDD through Gru; independently verified the reverse-item list. |
| Sep 22–25 | 21 hrs | [Project Progress — Code file](https://github.com/asheeshnellutla92/surveymind-response-realism-study/blob/main/SurveyMind%20Response%20Analysis.ipynb) · [Project Progress video](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/asheesh-n/SurveyMind%20-%20) · [AI Topic — Rogue Agent Containment](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/asheesh-n/Rogue%20Agent%20Containment%20-%20AI%20Topic) · [Drive](https://drive.google.com/drive/folders/1ZrBY5hKfTi5Iwr8dSk3f_hi8cFpMnbOS) | The regeneration attempt using the paper's method hit a blocker; after checking with Prof. Nina, pivoted to an independent approach. |
| Sep 29–Oct 2 | 20 hrs | [Project Progress — Code file](https://github.com/asheeshnellutla92/surveymind-response-realism-study/blob/main/SurveyMind%20Response%20Analysis.ipynb) · [Project Progress video](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/asheesh-n/SurveyMind%20-%203) · [AI Topic — Why Language Models Hallucinate](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/asheesh-n/LLM%20Hallucinations%20-%20AI%20Topic) · [Drive](https://drive.google.com/drive/folders/1ZrBY5hKfTi5Iwr8dSk3f_hi8cFpMnbOS) | Identified a circularity risk in the independent synthetic-data generation plan (testing a generator on the same data it was built from is meaningless); designed an 80/20 train/test split, derived that the held-out portion is statistically large enough to trust, set an explicit leakage boundary for the next (not-yet-made) decision on generative method, and submitted the design to Gru. |

**Degree relevance and supervision:**
This work directly applies my MS in Data Science & Analytics Engineering — correlation analysis, distribution testing, and model validation — to an unresolved research question (whether AI-generated survey data structurally replicates real human data), and builds on my prior published research benchmarking model performance against real-world baselines (IJCAI 2025).

**Supervisor:** Komal Ganapathy (Madison).

**Authorization:** F-1 OPT, EAD dates August 3, 2026 – July 8, 2027. Current volunteer agreement dates: August 25, 2026 – September 30, 2026.

**Next period:** Obtain or regenerate real SurveyMind synthetic output and run the actual Response Pattern Realism Study against the pre-registered threshold (congruence ≥ 0.90). Target date: end of October.

**Outstanding issues:**
1. Custom Jennrich test implementation still not cross-validated against R's `psych::cortest.jennrich` — highest-priority open item.
2. Whether SurveyMind's unconditioned generation implicitly skews toward a non-representative population is unresolved.
3. Real SurveyMind synthetic output still not located; independent regeneration approach in progress, not yet complete.
