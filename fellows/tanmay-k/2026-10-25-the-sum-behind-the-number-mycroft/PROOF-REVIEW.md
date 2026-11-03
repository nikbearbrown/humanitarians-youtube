# Feedback: "The Sum Behind the Number" — long film (16:9), script review 1

**Rubric:** `PROOF.md` teaching rubric (six criteria, 0–2 each, /12) plus the binary production gate.
**Reviewed:** `SCRIPT.md` draft 1 after the edits listed below (plan level: no frames exist yet, so legibility is *specified*, not measured). Facts: `FACTCHECK.md` (19 claims, each re-derived from committed files).
**Verdict: clear-for-public at script level.** Teaching **12/12**. Production gate **PASS at plan level**; it must be re-measured on the render.
One line: this film attempts to teach that a stress-test percentage is a sum of named shocks, and delivers it by rebuilding the workflow's own number block by block on screen.

## Rubric

| Criterion | Score | Reason |
|---|---|---|
| Explicit framework | 2 | The device is on screen from frame one (an empty stack outline beside the number, labelled "made of: ?"). The rule ("for each holding, add up the shocks that belong to it") is stated in B03, before any worked example in B04–B06. |
| Reusable rubric | 2 | The three closing questions (which shocks, from which lists, has anyone run the adder beside the original) apply to any stress-test result; the rule in B03 is reusable on a new scenario. |
| Worked example | 2 | B04 builds one holding's bar block by block (−15, −35, −40 = −90); B05 weighs three bars into the book's −78; B06 repeats the rule on a milder scenario (−45 and −30 give −33.75). Every step is on screen. |
| Falsifiability / edge case | 2 | B05's third holding is off the AI list (a different sum, −50), B06's fourth holding takes a third block, B04 notes the README names another combining rule (so the rule is a choice), and B08 shows inputs that would make the sum meaningless (weights that total 0.6 or 1.2; the flawed set that is stopped). The weakest of the six; see finding 3. |
| Active task | 2 | B03 hands over a guess ("if the market alone falls fifteen percent, how far does the biggest holding fall?") and B10 hands over three questions with a stated standard ("a good answer names the terms"). |
| Friction | 2 | The opening question (where does seventy-eight come from) plus the guess in B03, held about 3 s beside an empty bar before B04 answers it. |
| **Total** | **12/12** | |

## Production gate (plan level)

| Check | Result |
|---|---|
| Evidence legible at the moment of assertion | PASS as specified: every beat names its evidence panel (`stress-results.json` c01 and c12, the README quote, `parity-results.json`, the audits, the recipe frontmatter). **Re-measure at full 4K size on the render.** |
| Sources on screen, not just voiced | PASS: each beat carries a visible source label or evidence panel; every spoken figure (78, 15, 35, 40, 90, 50, 36, 27, 15, 45, 30, 33.75, 24, 12, 10) is printed on screen in the same beat. |
| Side-by-side at the moment of comparison | PASS by arrangement: B05 shows the three bars together under the headline number; B06 the four bars; B07 the two result columns; held ≥ 2–3 s is **not measurable until there is video**. |

## The problem

None that blocks. The film's one real risk is **ticker symbols on screen** (NVDA, AMD, TSM and so on). The portfolios are
invented and the narration never speaks a ticker, but a viewer could read "−78%" next to a real symbol as a forecast. The
script says "invented" and "not predictions" in B02 and labels every panel; see finding 2.

## Findings

1. **[EDIT, applied] Framework moved to frame one.** The first draft introduced the device in B03; B01 now shows the empty stack outline ("made of: ?") beside the number.
2. **[EDIT, optional] Ticker symbols.** The label "Invented portfolio · tickers from the workflow's own map" appears on B01, B02, B04–B06. If you want zero chance of misreading, show "chip stock A / B / C" on screen and keep the symbols in the evidence panels only. I left them in because the committed files show them.
3. **[EDIT, applied] Edge case and friction added.** B03 now ends on a guess; B04 notes that the README names another way to combine the shocks; B08's weights examples read as ambiguous inputs the workflow still handles.
4. **Positive-framing audit (standing instruction), all applied:**

| Instance that could read negatively | In the script |
|---|---|
| "−90% on a −15% market scenario" | credited as the workflow's own README worked example; "a big part of why it is so easy to check" |
| Flawed portfolios stopped | "what the checks protect"; "a sum of nothing never reaches the screen" |
| Weights off one | accepted, "the workflow rescales weights to one" |
| Open steps | "a good list for next time"; the recipe says draft "on purpose" |
| The label "critical" | "the workflow's word for losses above thirty", said once |
| My own check | "the part I wanted to be sure of"; every number, label and message matched; twelve deliberate breaks, each caught |

5. **Not yet measured (needs a render):** type sizes and contrast, hold times, the audio rate (the script plans about 3:15 of speech; the measured audio decides), and loudness.

## What works

- The running total is the argument: the number from the first second is rebuilt from its parts by the end of B05.
- Every number can be traced to a committed file or the README, and the check on my own adder is a result (24 of 24, 12 of 12), not a promise.
- The close hands the viewer something to ask, with a standard for a good answer.

## Do next

1. Read-aloud sheet; Gate P (Tanmay's read; the lint and the Kokoro phoneme check before it).
2. Decide on finding 2 (ticker symbols on screen).
3. Audio first, then stills, then video; re-run this review on the render.
