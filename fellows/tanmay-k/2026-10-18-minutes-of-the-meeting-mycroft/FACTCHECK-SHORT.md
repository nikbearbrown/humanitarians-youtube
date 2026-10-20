# Week 27 work video, the Short: FACTCHECK

**Film:** *Who Fills the Blank?* (working title), the trailer for *Minutes of the Meeting* · script `SCRIPT-SHORT.md` draft 2
**Source of every claim:** `nikbearbrown/mycroft` `main` @ `8665a9f` (the merge of PR #70), read with `git show`. Committed files only.
Rows SW1 to SW9 reuse the long film's evidence (`../FACTCHECK.md`, W-rows) for the same figures. **Checked:** 2026-10-17 (the figures are the long film's; the one new claim, SW1, is checked against the same node).

Verdicts: **SUPPORTED** · **QUALIFY** (true with a stated condition or wording fix) · **INVENTED** (our sample data, so the film must label it)

| # | Claim (line) | Verdict | Evidence (main @ 8665a9f) |
|---|---|---|---|
| SW1 | The last thing the AI is told is an instruction that its action plan must strictly match the verdict, and in the film's opening the verdict is a blank (S01) | SUPPORTED, QUALIFY | The Build AI Prompt node's final template line: `IMPORTANT: Your action_plan.immediate must strictly match "${agg.final_recommendation}". If HOLD — say hold, do not say enter.` The blank is the film's device (the verdict is filled in only after the chair weighs, S04); say "your action plan must strictly match", never "the AI must say sell" in S01. Long film W12 |
| SW2 | I contributed to an open-source finance pipeline, Mycroft, and the stock is invented (S02) | SUPPORTED, INVENTED | `README.md` (a book and a working agentic repository); `recipes/what-if-simulation-agent.md`; PR #70 merged 2026-10-17, merge commit `8665a9f`; `sample/manifest.json` (`"invented": true`). W1, W3, W4 |
| SW3 | Three simulators, called voices, read one stock: Sim 1 (growth against sentiment), Sim 2 (how an aggressive investor sees it, among three investor types), Sim 3 (how close the verdict is to changing) (S02, S03) | SUPPORTED | The workflow's Sim 1, Sim 2, Sim 3 nodes; the recipe's node table. W2 |
| SW4 | The first says strong sell (82% confidence); the second says enter a full position (the aggressive investor's four limits met exactly); the third's stability is 0.05 (S03) | SUPPORTED | `simulation-results.json` c11: `sim1.output.signal: STRONG_SELL`, `confidence: 0.82`; `sim2.recommendation: ENTER_FULL_POSITION`, `pass_count: 4/4` with every `actual` on its `required`; `sim3.stability_score: 0.05`. W7 to W9 |
| SW5 | "The verdict is fragile" for a stability of 0.05 (S03) | QUALIFY | The workflow's own labels for c11: `stress_resiliency: LOW`; the briefing's insight line "HIGH SENSITIVITY: Decision is 3 sentiment-points from a change"; 3 of 6 nudges change the verdict. "Fragile" is the film's plain word for those; it makes no claim about the stock |
| SW6 | A chair weighs them 45%, 35%, 20%; together 2.17 out of 5; that is a sell (S04) | SUPPORTED | The Aggregate node (`weights { sim1: 0.45, sim2: 0.35, sim3: 0.20 }`; `score >= 1.8 → SELL`); `aggregate`: `component_scores` 0.37, 1.75, 0.05; `score: 2.17`; `final_recommendation: SELL`. W10 |
| SW7 | The AI never heard that meeting; it gets the minutes, about 470 words, and the last line is the one you just saw (S05) | SUPPORTED, QUALIFY | Build AI Prompt writes the message and the Groq node sends it as the user message; `ai_prompt` for c11 is 471 words in five sections; its last line is the SW1 line with "SELL" filled in. "Never heard that meeting" means the AI is handed the written briefing, not the request: say so if asked. W11, W12, W14 |
| SW8 | The long film's title is "Minutes of the Meeting: What an AI Is Handed" (S06) | SUPPORTED | `../beat_sheet.json` `metadata.title`; `../minutes-of-the-meeting-youtube.md` |
| SW10 | In the full film I follow one stock through the whole meeting and every figure comes from a file you can open (S06) | SUPPORTED | The long film: one stock (c11) from B03 to B07; every slate names its committed file in its source line; `../FACTCHECK.md` W1 to W20 |
| SW11 | The full film shows what the AI is handed and what the minutes don't say (S06) | SUPPORTED, QUALIFY | Long B08: the briefing's five sections, and a number someone typed printing the same as a number filled in by default (`ai_prompt` for c06). "Don't say" means the briefing carries no marker for a defaulted value; the audit records it elsewhere (long W13) |
| SW12 | The full film shows the one place where my own copy of the steps disagreed with the original, and how I caught it (S06) | SUPPORTED | Long B09; RUN_LOG 2026-10-17 "Fixed while building"; `parity-results.json` (23 of 23 identical); `self-test-results.md` (the break: 21 of 23, 2 different). Long W15 to W17 |
| SW9 | Nothing in the Short is investment advice, and the finance is not judged | SUPPORTED (stated) | On-screen label "Invented stock · sample data"; the long film's description carries the full disclaimer |

## Not claimed (and why)

| Item | Why it stays out |
|---|---|
| That the weighting, the defaults or the verdict are right or wrong | The finance is ported faithfully, not judged (RUN_LOG: "[NOT COVERED] … whether the simulators' investment logic is sound") |
| What a real AI does with the briefing, or whether it follows the last line | The AI call is never made; the Short only says what the AI is handed |
| The detail of my minute-taker, parity or NaN | S06 only says my copy disagreed once and how I caught it (a comparison run); the mechanism is in the long film |
| Any real company, ticker or price | Every one is invented |
