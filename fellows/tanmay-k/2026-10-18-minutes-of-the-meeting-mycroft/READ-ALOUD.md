# READ-ALOUD: Gate P sheet (work video)

*Minutes of the Meeting* (working title) · structure: MINUTES OF ONE MEETING · voice `am_onyx`

Generated from `SCRIPT.md` by `make_read_sheet.py`. Read each beat aloud at speaking pace, top to bottom, in one
sitting; tick or note; skim the *on screen* line too. **Draft 2:** draft 1 was signed; only B02, B07, B09 and B11 changed (marked below).
Re-read those four; the other eight are unchanged. Reply **"Gate P PASS"** or list the beats that tripped you.

## Say-it-right checklist (Kokoro's phonemes, checked 2026-10-17)

| Word | Should sound like | Kokoro alone | Override | Where |
|---|---|---|---|---|
| Mycroft | MY-croft | `mˈɪkɹɔft ✗ (MICK-roft)` | `mˈaɪkɹɔft` | B02 |
| Tanmay Kulkarni | TAN-may kul-KAR-nee | `tˈænmeɪ kˈʌlkɑːɹni ✓` | `—` | B02, B12 |
| Ironbridge Power | EYE-urn-bridge POW-er | `ˈaɪɚnbɹɪdʒ pˈaʊɚ ✓` | `—` | B03 |
| price-to-earnings | price to earnings | `pɹˈaɪstʊˈɜːnɪŋz ✓` | `—` | B03, B05 |
| minute-taker | MIN-it taker | `mˈɪnɪttˈeɪkɚ ✓ (not my-NOOT)` | `—` | B09 |
| Python, JavaScript | PIE-thon, JAH-vuh-script | `pˈaɪθən ✓, dʒˈɑːvə skɹˈɪpt ✓` | `—` | B09 |
| summarise | SUM-uh-rize | `sˈʌmɚɹˌaɪz ✓` | `—` | B11 |

## Where to listen hardest

- **B01**: the cold open: the quoted line is read plainly, as a line of text, then the question lands: "So who decided the verdict?"
- **B02**: **changed:** the new line "who had a vote, and how much?" is the question the whole video answers; say it as a promise, lightly
- **B03**: "The meeting starts anyway": dry, not alarmed. The chair and voices are a metaphor; say it lightly
- **B05**: the four limits are quick and parallel; let "Four out of four" land before "Enter a full position"
- **B07**: **changed, and the reversal.** "Now they disagree." then the numbers calmly; "Nobody has made a mistake" is warm, not defensive
- **B08**: "looks exactly like": a plain observation about the briefing, not a complaint
- **B09**: **the turn, and it is mine.** "Here's where I got something wrong" said lightly, then the fix, plain and quick; no flourish
- **B10**: plain and honest; "on purpose" without a flourish
- **B11**: **changed:** a real question, unhurried, three short questions each with its own breath; then a good answer and a weak one, the weak one with a small smile

## The script

### [0:00] B01 · COLD OPEN, the last line

This is the last line of a message an AI is about to receive. "Your action plan must strictly match: sell." A workflow writes that line, to hold a model to a verdict it has already been given. So who decided the verdict? Let me take you to the meeting.

<sub>**On screen:** the closing lines of the briefing, typeset as plain text; the line `IMPORTANT: Your action_plan.immediate must strictly match "SELL". If HOLD — say hold, do not say enter.` is highlighted. Evidence panel: `simulation-results.json`, c11, last line of `ai_prompt`. Label: "From the sample run · invented company". *Refs:* W12, W4.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [0:15] B02 · WHAT THIS IS  ← CHANGED, please re-read

Hi, this is Tanmay Kulkarni, in for Humanitarians AI. This week I contributed to Mycroft, a book and a working repository of finance pipelines. It calls them recipes. One of them, the What-If Simulation Agent, asks three different questions about a stock, then hands an AI the answers. Three voices, one written record, and one question for this whole video: who had a vote, and how much? My pull request, now merged, made the six steps before the AI runnable on test data, with checks. Every company you'll see is invented, and none of this is investment advice.

<sub>**On screen:** "Mycroft: both a book and a working agentic repository" (README line quoted); the recipe name; a strip of six steps, then a seventh box "AI", greyed; "PR #70 · merged"; "Every company and number in this video is invented. Not investment advice." *Refs:* W1, W2, W3, W4.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [0:44] B03 · THE CHAIR OPENS

Today's stock is Ironbridge Power. Invented. Growth, five percent. Sentiment, point three five. A price-to-earnings of eighty, and an aggressive investor. I'll call the workflow the chair, and the three simulators its voices. The chair's first job is to make sure every seat has something to read. Ironbridge arrived with everything filled in. But if a request arrives with nothing, the chair fills every seat itself. A company called Unknown Company, growth fifteen percent, sentiment point five. The meeting starts anyway.

<sub>**On screen:** the request as a small card (Ironbridge Power, IRB, growth 5%, sentiment 0.35, P/E 80, D/E 1.5, risk "high"); a second, empty card that fills in with the defaults (Unknown Company, N/A, 15%, 0.5, 25, 0.5, "medium"). Caption: "defaults, as the workflow's first step defines them". Evidence panel: `c06-empty-body-all-defaults` result; `validate-audit.md` ("fields filled by the workflow's defaults"). Label: "Invented · not a real company". *Refs:* W5, W6, W20.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:09] B04 · FIRST VOICE

First voice: growth against sentiment. It sorts a stock into one of nine boxes, low, medium or high on each. Ironbridge is low and low. The voice says strong sell, with eighty-two percent confidence.

<sub>**On screen:** the 3×3 grid, the LOW/LOW cell highlighted; "Sim 1 · STRONG_SELL · 82%". Evidence panel: `simulation-results.json`, c11 `sim1_growth_sentiment`. Label: "Invented". *Refs:* W7.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:19] B05 · SECOND VOICE

Second voice: the same stock, judged for three kinds of investor. Conservative says avoid. Balanced says avoid. Aggressive has the loosest limits. Growth at least five percent. Sentiment at least point three five. Price-to-earnings no more than eighty. Debt to equity no more than one and a half. And Ironbridge sits exactly on all four. Four out of four. Enter a full position.

<sub>**On screen:** three seats (Conservative: AVOID; Balanced: AVOID; Aggressive: ENTER); the aggressive seat's four criteria ticking one at a time, each showing actual against limit (5% ≥ 5%, 0.35 ≥ 0.35, 80 ≤ 80, 1.50 ≤ 1.5). Evidence panel: c11 `criteria_evaluation`. Label: "Invented". *Refs:* W8.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:38] B06 · THIRD VOICE

Third voice, and this one asks something different. Not what should we do, but how close is it to changing its mind. It nudges growth and sentiment up and down, six ways, and watches the verdict. Three of the six nudges change it. The stability score: point oh five, out of one.

<sub>**On screen:** six small nudges, three flipping their label; a stability gauge near zero, "0.05 / 1.0". Evidence panel: c11 `sim3_threshold_break` (`stress_breach_count`, `stability_score`). Label: "Invented". *Refs:* W9.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:54] B07 · THEY DISAGREE  ← CHANGED, please re-read

Now they disagree. The first voice says strong sell. The second says enter a full position. Nobody has made a mistake. They were asked different questions. So the chair weighs them: forty-five, thirty-five and twenty. The chair's scale runs from one to five. Strong sell sits at the bottom, and enter a full position at the top. So a smaller weight on the top can outweigh a bigger weight on the bottom. The voices contribute point three seven, one point seven five, and point oh five. Together, two point one seven out of five. Anywhere from one point eight to two point eight, the chair writes down as sell.

<sub>**On screen:** the three voices' verdicts side by side; the three weights; the three weighted pieces summing to 2.17; a ruler showing 1.8 to 2.8 labelled SELL; the chair's pen writing "SELL"; the five-point scale drawn once, STRONG_SELL at the bottom and ENTER_FULL_POSITION at the top. Evidence panel: c11 `aggregate` (`component_scores`, `score`, `final_recommendation`). Label: "Invented". *Refs:* W10.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [2:27] B08 · THE MINUTES

Then the chair writes the minutes. About four hundred and seventy words. The stock, each voice, the stress tests, the verdict. And one last instruction, for someone who wasn't in the room: the action plan must strictly match sell. The AI only ever receives the minutes. And in the minutes, a number somebody typed looks exactly like a number the chair filled in.

<sub>**On screen:** the briefing scrolling past in miniature, its sections labelled (company profile, the three simulations, aggregate verdict); the final line highlighted again; two numbers side by side, "0.5 (typed)" and "0.5 (filled in by default)", rendered identically in the briefing. Evidence panel: c06 `ai_prompt` ("Sentiment Score: 0.5/1.0"). Label: "Invented". *Refs:* W11, W12, W13, W14.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [2:46] B09 · THE TURN, MY MINUTE-TAKER  ← CHANGED, please re-read

Here's where I got something wrong. To check the original, I wrote a second minute-taker, a Python copy of those six steps, and ran both on the same meetings. On two requests, it wrote a different verdict. Those were requests where growth was typed as the letters A, B, C, and sentiment was left as empty text. Python and JavaScript disagree about the smallest of a list when one entry isn't a number. I fixed it. Now both write the same minutes, to the letter, on all twenty-three requests, and a test keeps that slip from coming back.

<sub>**On screen:** two columns of minutes, "original" and "mine", one verdict line differing, then equal; "21 of 23 → 23 of 23"; the self-test row "BREAK: min/max with NaN … caught". Evidence panel: `logs/RUN_LOG.md` 2026-10-17 "Fixed while building"; `parity-results.json` (23/23). *Refs:* W15, W16, W17.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [3:16] B10 · ADJOURNED

Nothing was sent anywhere. The step that would call the AI, and the step that would save the answer, are written down as hand-offs, marked not approved. Five items in the recipe are still open, and it still says draft, on purpose.

<sub>**On screen:** the two hand-offs with `approved_for_live_action: false`; the recipe's frontmatter (`status: DRAFT`, `todos_open: 5`). Evidence panel: `run-approved-tools-2026-10-17.json` (`live_handoffs`); the recipe's frontmatter. *Refs:* W18, W19.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [3:29] B11 · CLOSE  ← CHANGED, please re-read

If an AI is going to summarise your next meeting, have you read the minutes? Who had a vote? And how much of one? A good answer names the voices and their weights. "The AI will figure it out" doesn't count.

<sub>**On screen:** the minutes, dimmed; the three questions. *Refs:* none.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [3:41] B12 · OUTRO

Adjourned. Tanmay Kulkarni, in for Humanitarians AI, signing off.

<sub>**On screen:** title outro. *Refs:* none.</sub>

> ☐ reads cleanly   ☐ note: ______________________

_12 beats · 740 words · about 3:44 at 3.3 words/s, before holds._
