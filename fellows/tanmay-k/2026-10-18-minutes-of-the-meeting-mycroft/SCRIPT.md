# SCRIPT: *Minutes of the Meeting* (Week 27 work video, Mycroft PR #70)

**Draft 2, 2026-10-17** (Gate P PASS on draft 1; the PROOF review edited B02, B07, B09 and B11; Gate P PASS again on those four, the other eight unchanged). Angle A, approved by Tanmay 2026-10-17
(see `ANGLE.md`): disagreement beat uses **c11**; the briefing's "must strictly match" line is quoted on screen.
Structure: MINUTES OF ONE MEETING. One invented stock, three voices, a chair who weighs them, and a record handed
to the one party who was not in the room, an AI. About 670 words, roughly 4:30 at the voice's measured pace.

**Framing:** defaults, the weighting and the NaN behaviour are described as how the workflow works, never as faults.
The finance is not judged. The only mistake in this film is mine (B09), shown with its fix. Humble, first person on
the genuine turns only (B02, B07, B09). Every company and number is invented, said once in B02 and labelled on
screen wherever a number appears; not investment advice, said once. Committed files only (`FACTCHECK.md`).
"Voices" and "chair" are a metaphor for the three simulators and the aggregate step, said as such in B03.

**TTS spelling:** numbers in words in the narration; digits on screen only. "Mycroft" keeps its real spelling
everywhere; the audio step feeds Kokoro the override `mˈaɪkɹɔft` (MY-croft). Short fragments ("Invented.", "Four out of four.") are checked by Whisper at the audio step. "What-If" is voiced as "what if" (Kokoro merges the hyphenated form into "wudif"); the text and captions keep the real spelling. Each beat is synthesised whole, not sentence by sentence (sentence-by-sentence came out about 30% slower).

---

### B01 · COLD OPEN, the last line
> This is the last line of a message an AI is about to receive. "Your action plan must strictly match: sell." A workflow writes that line, to hold a model to a verdict it has already been given. So who decided the verdict? Let me take you to the meeting.

*On screen:* the closing lines of the briefing, typeset as plain text; the line `IMPORTANT: Your action_plan.immediate must strictly match "SELL". If HOLD — say hold, do not say enter.` is highlighted. Evidence panel: `simulation-results.json`, c11, last line of `ai_prompt`. Label: "From the sample run · invented company". *Refs:* W12, W4.

### B02 · WHAT THIS IS
> Hi, this is Tanmay Kulkarni, in for Humanitarians AI. This week I contributed to Mycroft, a book and a working repository of finance pipelines. It calls them recipes. One of them, the What-If Simulation Agent, asks three different questions about a stock, then hands an AI the answers. Three voices, one written record, and one question for this whole video: who had a vote, and how much? My pull request, now merged, made the six steps before the AI runnable on test data, with checks. Every company you'll see is invented, and none of this is investment advice.

*On screen:* "Mycroft: both a book and a working agentic repository" (README line quoted); the recipe name; a strip of six steps, then a seventh box "AI", greyed; "PR #70 · merged"; "Every company and number in this video is invented. Not investment advice." *Refs:* W1, W2, W3, W4.

### B03 · THE CHAIR OPENS
> Today's stock is Ironbridge Power. Invented. Growth, five percent. Sentiment, point three five. A price-to-earnings of eighty, and an aggressive investor. I'll call the workflow the chair, and the three simulators its voices. The chair's first job is to make sure every seat has something to read. Ironbridge arrived with everything filled in. But if a request arrives with nothing, the chair fills every seat itself. A company called Unknown Company, growth fifteen percent, sentiment point five. The meeting starts anyway.

*On screen:* the request as a small card (Ironbridge Power, IRB, growth 5%, sentiment 0.35, P/E 80, D/E 1.5, risk "high"); a second, empty card that fills in with the defaults (Unknown Company, N/A, 15%, 0.5, 25, 0.5, "medium"). Caption: "defaults, as the workflow's first step defines them". Evidence panel: `c06-empty-body-all-defaults` result; `validate-audit.md` ("fields filled by the workflow's defaults"). Label: "Invented · not a real company". *Refs:* W5, W6, W20.

### B04 · FIRST VOICE
> First voice: growth against sentiment. It sorts a stock into one of nine boxes, low, medium or high on each. Ironbridge is low and low. The voice says strong sell, with eighty-two percent confidence.

*On screen:* the 3×3 grid, the LOW/LOW cell highlighted; "Sim 1 · STRONG_SELL · 82%". Evidence panel: `simulation-results.json`, c11 `sim1_growth_sentiment`. Label: "Invented". *Refs:* W7.

### B05 · SECOND VOICE
> Second voice: the same stock, judged for three kinds of investor. Conservative says avoid. Balanced says avoid. Aggressive has the loosest limits. Growth at least five percent. Sentiment at least point three five. Price-to-earnings no more than eighty. Debt to equity no more than one and a half. And Ironbridge sits exactly on all four. Four out of four. Enter a full position.

*On screen:* three seats (Conservative: AVOID; Balanced: AVOID; Aggressive: ENTER); the aggressive seat's four criteria ticking one at a time, each showing actual against limit (5% ≥ 5%, 0.35 ≥ 0.35, 80 ≤ 80, 1.50 ≤ 1.5). Evidence panel: c11 `criteria_evaluation`. Label: "Invented". *Refs:* W8.

### B06 · THIRD VOICE
> Third voice, and this one asks something different. Not what should we do, but how close is it to changing its mind. It nudges growth and sentiment up and down, six ways, and watches the verdict. Three of the six nudges change it. The stability score: point oh five, out of one.

*On screen:* six small nudges, three flipping their label; a stability gauge near zero, "0.05 / 1.0". Evidence panel: c11 `sim3_threshold_break` (`stress_breach_count`, `stability_score`). Label: "Invented". *Refs:* W9.

### B07 · THEY DISAGREE
> Now they disagree. The first voice says strong sell. The second says enter a full position. Nobody has made a mistake. They were asked different questions. So the chair weighs them: forty-five, thirty-five and twenty. The chair's scale runs from one to five. Strong sell sits at the bottom, and enter a full position at the top. So a smaller weight on the top can outweigh a bigger weight on the bottom. The voices contribute point three seven, one point seven five, and point oh five. Together, two point one seven out of five. Anywhere from one point eight to two point eight, the chair writes down as sell.

*On screen:* the three voices' verdicts side by side; the three weights; the three weighted pieces summing to 2.17; a ruler showing 1.8 to 2.8 labelled SELL; the chair's pen writing "SELL"; the five-point scale drawn once, STRONG_SELL at the bottom and ENTER_FULL_POSITION at the top. Evidence panel: c11 `aggregate` (`component_scores`, `score`, `final_recommendation`). Label: "Invented". *Refs:* W10.

### B08 · THE MINUTES
> Then the chair writes the minutes. About four hundred and seventy words. The stock, each voice, the stress tests, the verdict. And one last instruction, for someone who wasn't in the room: the action plan must strictly match sell. The AI only ever receives the minutes. And in the minutes, a number somebody typed looks exactly like a number the chair filled in.

*On screen:* the briefing scrolling past in miniature, its sections labelled (company profile, the three simulations, aggregate verdict); the final line highlighted again; two numbers side by side, "0.5 (typed)" and "0.5 (filled in by default)", rendered identically in the briefing. Evidence panel: c06 `ai_prompt` ("Sentiment Score: 0.5/1.0"). Label: "Invented". *Refs:* W11, W12, W13, W14.

### B09 · THE TURN, MY MINUTE-TAKER
> Here's where I got something wrong. To check the original, I wrote a second minute-taker, a Python copy of those six steps, and ran both on the same meetings. On two requests, it wrote a different verdict. Those were requests where growth was typed as the letters A, B, C, and sentiment was left as empty text. Python and JavaScript disagree about the smallest of a list when one entry isn't a number. I fixed it. Now both write the same minutes, to the letter, on all twenty-three requests, and a test keeps that slip from coming back.

*On screen:* two columns of minutes, "original" and "mine", one verdict line differing, then equal; "21 of 23 → 23 of 23"; the self-test row "BREAK: min/max with NaN … caught". Evidence panel: `logs/RUN_LOG.md` 2026-10-17 "Fixed while building"; `parity-results.json` (23/23). *Refs:* W15, W16, W17.

### B10 · ADJOURNED
> Nothing was sent anywhere. The step that would call the AI, and the step that would save the answer, are written down as hand-offs, marked not approved. Five items in the recipe are still open, and it still says draft, on purpose.

*On screen:* the two hand-offs with `approved_for_live_action: false`; the recipe's frontmatter (`status: DRAFT`, `todos_open: 5`). Evidence panel: `run-approved-tools-2026-10-17.json` (`live_handoffs`); the recipe's frontmatter. *Refs:* W18, W19.

### B11 · CLOSE
> If an AI is going to summarise your next meeting, have you read the minutes? Who had a vote? And how much of one? A good answer names the voices and their weights. "The AI will figure it out" doesn't count.

*On screen:* the minutes, dimmed; the three questions. *Refs:* none.

### B12 · OUTRO
> Adjourned. Tanmay Kulkarni, in for Humanitarians AI, signing off.

*On screen:* title outro. *Refs:* none.
