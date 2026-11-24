# FACTCHECK — Why Did the AI Say No? (Boopesh M., AI in finance)

This film explains **what the rule asks for**. It is not legal advice, and it says so on screen (B20, B90) and in
the narration (B20).

Sources and how strongly each claim is backed:

- **[REG B]** = 12 CFR § 1002.9 (Regulation B, "Equal Credit Opportunity Act (Regulation B)"), paragraphs (a)(1),
  (a)(2) and (b)(2). **Read verbatim** from a pinned plain-text mirror of the govinfo eCFR bulk XML on GitHub
  (`xerj-org/corpus-ecfr-title-12`, commit `4dc0246c`, file `parts/part-1002/sec-1002.9.txt`; the mirror's
  PROVENANCE.txt names `https://www.govinfo.gov/bulkdata/ECFR/title-12/ECFR-title12.xml`, amendment date
  Sept. 14, 2026, downloaded 2026-10-02). `ecfr.gov`, `govinfo.gov`, `consumerfinance.gov` and `law.cornell.edu`
  were all blocked from the build container (proxy 403 / host not allowed, tried 2026-11-15), so this is a
  third-party mirror of the official text, not the official site itself.
  Key sentence, (b)(2): "The statement of reasons for adverse action required by paragraph (a)(2)(i) of this section
  must be specific and indicate the principal reason(s) for the adverse action. Statements that the adverse action
  was based on the creditor's internal standards or policies or that the applicant, joint applicant, or similar
  party failed to achieve a qualifying score on the creditor's credit scoring system are insufficient."
- **[CIRC]** = CFPB, Consumer Financial Protection Circular 2022-03, "Adverse action notification requirements in
  connection with credit decisions based on complex algorithms" (issued May 26, 2022; 87 FR 35864, June 14, 2022).
  **⚠️ Not read directly** (consumerfinance.gov and every copy tried were blocked). Its content and dates come from
  **WebSearch result summaries** (the Bureau's own page as quoted in search results, and law-firm summaries:
  Goodwin, Greenberg Traurig, Orrick InfoBytes, Bankers Compliance Group). Summary wording: creditors that use complex
  algorithms, including AI or machine learning, must still give the specific principal reasons for an adverse action;
  ECOA and Regulation B do not permit creditors to use complex algorithms when doing so means they cannot provide the
  specific and accurate reasons.
- **[WITHDRAWN]** = CFPB notice withdrawing 67 guidance documents, 90 FR 20084, effective May 12, 2025, listing
  Circular 2022-03. **⚠️ Seen only in search results** (the CFPB "Withdrawn guidance" page as quoted in search
  results, Morgan Lewis guidance tracker, Forvis Mazars, Krieg DeVault, Bankers Compliance Group). The Bureau called
  the withdrawals "not necessarily final" per those summaries. Not checked: whether anything has been reissued since.
- **[SHAP]** = Scott M. Lundberg & Su-In Lee, "A Unified Approach to Interpreting Model Predictions", NeurIPS 2017
  (NIPS 30). Title, authors, year and venue read from the authors' own repository: `shap/shap`
  `docs/references/shap_nips.bib` and the README's "NeurIPS paper" citation (raw.githubusercontent.com). The paper
  itself (papers.nips.cc) was blocked; nothing else from it is claimed. The film uses only "Shapley values" as the
  method name and "Lundberg & Lee, NeurIPS 2017" as the citation.
- **[RUN]** = output of `code/credit_reasons.py` in this folder (`code/results.json`, `code/run.log`), numpy 2.5.4,
  scikit-learn 1.9.1, seed 42, `OMP_NUM_THREADS=1`. **Synthetic applicants**, said on screen (B00 composer, B30
  header, B40 kicker "also made up", B70 limits, outro) and in narration (B00, B30, B40 "also made up", B70 limits).
  Run twice (second run in a scratch folder): `run.log` identical, `results.json` identical apart from `runtime_s`.

No protected attributes (race, sex, age, etc.) are generated or used; fairness is explicitly out of scope ("fairness
is another video", B30).

| Beat | Claim | Source | Status |
|---|---|---|---|
| B00 | 20,000 synthetic applicants, 5 plain features; A denied by both; they share 2 of 3 reasons | [RUN] | ✅ |
| B10 | "the model said no" is not a reason; a lender has to name the facts behind it | [REG B] (b)(2) (reasons must be specific; "failed to achieve a qualifying score" is insufficient) — film's plain-language paraphrase | ✅ (paraphrase) |
| B20 | In the US, Regulation B under the Equal Credit Opportunity Act: a denied applicant gets specific reasons, the principal ones | [REG B] (a)(2)(i) statement of specific reasons (or a disclosure of the right to one, (a)(2)(ii)); (b)(2) "must be specific and indicate the principal reason(s)" — quoted verbatim on screen | ✅ (mirror of official text) |
| B20 | "you failed to reach our score" is not enough (on screen: "named in the rule as not enough") | [REG B] (b)(2) "failed to achieve a qualifying score on the creditor's credit scoring system are insufficient" | ✅ |
| B20 | Regulation B citation "12 CFR 1002.9(b)(2)" | [REG B] | ✅ |
| B20 | 2022: a CFPB circular (2022-03) said this holds for complex algorithms too | [CIRC] via search summaries | ⚠️ not read directly |
| B20 | it was withdrawn in 2025 "with dozens of other guidance papers" (67 documents) | [WITHDRAWN] via search summaries | ⚠️ not read directly |
| B20 | "the regulation's wording remains" / "Regulation B wording still in the rule book" (2026) | [REG B] mirror of eCFR with amendment date Sept. 14, 2026 still contains (b)(2) | ✅ |
| B20 | "what the rule asks for, not legal advice" | editorial framing | — |
| B30 | 20,000 synthetic applicants; features income, debt-to-income, missed payments, credit history length, card use | [RUN] `make_applicants`, seed 42 | ✅ |
| B30 | average applicant: income $60k, DTI 33 %, 0.4 missed payments, 10 years history, 42 % card use | [RUN] training-set means 59.80 / 33.41 / 0.448 / 10.01 / 42.44 | ✅ (rounded) |
| B30 | two models: a simple scorecard (logistic regression) and a gradient-boosted "black box" (300 trees) | [RUN] `LogisticRegression` on standardised features; `HistGradientBoostingClassifier(max_iter=300)` | ✅ |
| B30 | "both rank risk equally well": test AUC 0.84 and 0.84 | [RUN] 0.836 and 0.836 on 6,000 held-out synthetic applicants (true rule 0.847) | ✅ |
| B30 | scorecard icon bar heights | [RUN] |weight per standard deviation| of the fitted scorecard | ✅ |
| B40 | Applicant A: DTI 44 %, cards 72 % used, 1 missed payment, 4 years history, income $52k | [RUN] hand-written made-up applicant (`APPLICANT_A`) | ✅ (by construction) |
| B40 | lender's line: 30 % risk of default, "my choice" | [RUN] `CUTOFF = 0.30`, an illustrative assumption, not from any lender | ✅ labelled assumption |
| B40 | scorecard puts A at 53 %, black box at 34 %; both deny | [RUN] 53.2 % / 34.1 % (the true rule that made the data says 40.1 %) | ✅ |
| B50 | scorecard reason = weight × (A − average applicant), exact; five multiplications | [RUN] contributions in log-odds; intercept + sum of contributions = A's log-odds (asserted to 1e-9); exact Shapley values computed for the scorecard against the 500-applicant background equal weight × (A − background mean) to 7e-16 | ✅ |
| B50 | top 3: debt-to-income +0.82, card use +0.76, missed payments +0.43 (credit history +0.38, income +0.08) | [RUN] | ✅ |
| B50 | reason wording "debt payments too high for income", "card balances near their limits", "recent missed payments" | plain-language labels written for this film; not quoted from the Regulation B sample forms | editorial |
| B60 | Shapley values: every combination of A's features (2⁵ = 32) against 500 other applicants = 16,000 model runs | [RUN] exact interventional Shapley values, 32 coalitions × 500 background applicants; additivity error 0 | ✅ |
| B60 | black-box top 3: missed payments +0.60, card use +0.45, credit history +0.30 (DTI +0.20, income +0.05) | [RUN] | ✅ |
| B60 | the two models share 2 of 3 reasons (card use, missed payments); order differs | [RUN] | ✅ |
| B60 | compare A with approved applicants only → DTI back in the top 3 (#2) | [RUN] background = 500 training applicants the boosted model approves: missed +0.72, DTI +0.57, card use +0.49 | ✅ |
| B60 | retrain on another 70 % of the data → DTI back in the top 3 (#3) | [RUN] split seed 49: missed +0.66, card use +0.62, DTI +0.52; that model puts A at 50.6 % | ✅ |
| B60 | "method: Lundberg & Lee, NeurIPS 2017" | [SHAP] | ✅ (citation only) |
| B70 | pay card balances down about $3,850 (72 % → 34 % of an assumed $10,000 limit), everything else unchanged → both models say yes | [RUN] smallest single change on a 0.5-point grid that flips both: utilisation 33.5 %; risk after: scorecard 29.9 %, black box 28.7 % | ✅ (card limit is an assumption, labelled) |
| B70 | limits: synthetic applicants, a cutoff I chose, Shapley values are one method among several | honest limits of [RUN] | opinion, labelled as limits |
| B80 | prompt: retrain the black box with a different seed; same top 3? | not answered in the film | — |
| B90 | credits: Regulation B 12 CFR 1002.9; Shapley values (Lundberg & Lee, 2017) | [REG B], [SHAP] | ✅ |

Note on B30 "0.4": the average number of missed payments is 0.448 (run.log prints it as 0.45); the screen shows
one decimal, 0.4.

## Not in the film (logged in run.log / results.json)
- One-change-at-a-time alternatives: debt-to-income would need to fall from 44 % to 31 % for the scorecard (≈ $563 less
  in monthly debt payments on $4,333 monthly income) but only to 42.5 % for the black box (≈ $65/month): the two
  models disagree a lot about this path to "yes" because the boosted model learned a step near 43 %.
- Applicant A was hand-picked so that both models deny and one plain change flips both; the first cutoff tried (20 %)
  needed a $5,950 pay-down; the film uses 30 % (see FRICTIONAL.md).

## Experiment details (all [RUN])
Income lognormal (median $55k), DTI 100·Beta(2.5, 5), missed payments Poisson(0.45) capped at 8, history
Gamma(2.5, 4) years, card use 100·Beta(2, 3) + 6 × missed payments. True default log-odds: −3.0 − 0.012(income − 55)
+ 0.030(DTI − 33) + 0.090·max(DTI − 40, 0) + 0.75·min(missed, 4) − 0.55·ln(history/8) + 0.020(util − 40)
+ 0.050·max(util − 70, 0); default rate 16.0 %. 70/30 stratified split. Shapley values on the model's log-odds.
