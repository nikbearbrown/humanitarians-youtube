# SHOTLIST — Why Did the AI Say No? (16:9, 3840×2160)

| Beat | Lane | Visual |
|---|---|---|
| B00 | Remotion `ClaudeComposerAsk` | "Hi, Boopesh" composer: "When an AI credit model denies a loan, how do you find the specific reasons it said no?" answered in three lines (synthetic applicants · A denied by both models · 2 of 3 reasons shared); chip @HumanitariansAI |
| B10 | Remotion `BrutalistHesitantWriter` | "You were denied because the model said no." corrected to "…because your debt is too high for your income." |
| B20 | Manim `B20_Rule` | cream card: Equal Credit Opportunity Act · Regulation B 12 CFR 1002.9(b)(2), the "must be specific and indicate the principal reason(s)" quote, ✓ "debt payments too high for income" vs ✗ "you failed to reach our score"; dark timeline 2022 circular → 2025 withdrawn → 2026 Regulation B wording still there; "not legal advice" |
| B30 | Manim `B30_Models` | "20,000 synthetic applicants": five features with the average applicant; scorecard card (weight bars from the fitted model) and black-box card (trees); test AUC 0.84 / 0.84 |
| B40 | Manim `B40_ApplicantA` | Applicant A's five values; risk axis with the 30 % lender's line (my choice): black box 34 %, scorecard 53 %; "BOTH SAY NO" |
| B50 | Manim `B50_Scorecard` | the one formula (push toward no = weight × (A − average)); five bars, top 3 numbered in terracotta; dark card "reasons on the notice" 1–3 |
| B60 | Manim `B60_BlackBox` | "16,000 model runs for one person": 32 combinations × 500 applicants; Shapley bars, top 3; side-by-side top-3 lists, "2 of 3 reasons shared"; "the black box's list can shift" (approved-only comparison, retrained) |
| B70 | Manim `B70_Change` | card balance bar $7,200 (72 %) → $3,350 (34 %), "pay down $3,850"; risk markers slide left of the 30 % line (29.9 %, 28.7 %), "BOTH SAY YES"; limits strip |
| B80 | Remotion `ClaudeComposerAsk` | "Your turn." composer with the prompt |
| B90 | Manim `B90_Outro` | title, SUBSCRIBE + HAI mark + @HumanitariansAI; credit Boopesh M. · Fellow · Brutalist team; data/rule/method line; AI narration · not legal advice |

Every number is read from `code/results.json` (synthetic applicants).
