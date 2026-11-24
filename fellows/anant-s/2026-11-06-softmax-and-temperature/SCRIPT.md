# SCRIPT — Softmax and Temperature, Explained

Narration for review (GATE P). Generated from beat_sheet.json by make_sheet.py; numbers in the *On screen* lines are read from demo/evidence.json.
Narrator: Liam, in for Bear (Kokoro `am_onyx`). Greeting: `Bonjour, Liam`. Pronunciation pins: logit → /ˈloʊdʒɪt/, logits → /ˈloʊdʒɪts/, "a logit" → /ɐ ˈloʊdʒɪt/.

## B00 · ASK · ClaudeComposerAsk  (29 words, ~8 s)

Bonjour, this is Liam, in for Bear. The ask: why does the same prompt give me a different answer every time? Show me the math underneath, with real numbers.

*On screen:* composer card fades in on cream → greeting 'Bonjour, Liam' types above the composer → the ask types in → runningText 'working through the math…' appears → three result lines cascade in

## B01 · BLUF · BrutalistHesitantWriter  (30 words, ~9 s; lead silence 0.8 s)

A language model rolls weighted dice for every word it writes. Softmax sets the weights. Temperature decides how lopsided they are. That's why the same prompt can come back different.

*On screen:* cream page holds; caret blinks → types 'A language model / picks the likeliest word.' → 'picks the likeliest word' turns terracotta, hesitates, backspaces → types 'rolls weighted dice' → final lines settle: 'A language model / rolls weighted dice.'

## B02 · FRAMEWORK · B02_Machine  (59 words, ~17 s)

Here's the machine. You type a prompt: the cat sat on the. The model doesn't hand back a word. It hands back a score for every token it knows, called a logit. Here are five of them. Softmax turns those scores into probabilities. A sampler rolls against those probabilities, picks one token, appends it, and the loop runs again.

*On screen:* prompt chip 'The cat sat on the ___' draws on at left → arrow into a 'model' box → five logit bars grow out of the box: mat 3.2, floor 2.4, couch 1.9, bed 1.5, roof 0.3; caption 'logits (constructed) — 5 of the whole vocabulary' → the bars pass through a 'softmax' box and come out as probability bars that sum to 1 → a 'sampler' die rolls; 'mat' lights terracotta and slides into the prompt chip → a loop arrow draws from the prompt back into the model: 'next token'

## B03 · FRAMEWORK · B03_Formula  (57 words, ~16 s)

Softmax, written down. Take each token's logit and divide it by the temperature, T. Raise e to that power, so every score turns positive. Then divide by the same thing summed over every token, so the shares add up to exactly one. A bigger logit always means a bigger share. And temperature acts first, before the exponent.

*On screen:* MathTex typesets large: p_i = e^{z_i/T} / Σ_j e^{z_j/T} → box spotlight on z_i; label below: 'logit (a score)' → box spotlight on T; label: 'temperature (you choose it, T > 0)' → box spotlight on the numerator e^{z_i/T}; label: 'always positive' → box spotlight on the denominator Σ_j; label: 'same thing, summed over every token' → chip: 'all p_i add up to 1' → box spotlight returns to z_i/T: 'temperature acts first'

## B04 · WORKED_EXAMPLE · B04_WorkedT1  (60 words, ~17 s)

Real numbers, at temperature one. Mat scores three point two; roof, zero point three. Raise e to each: mat becomes about twenty-four and a half, roof about one point three five. Add all five and you get about forty-eight. Divide each by forty-eight. Mat gets fifty-one percent, floor twenty-three, couch fourteen, bed nine, roof three. Those shares are the dice.

*On screen:* compact formula top-left (from B03) with T = 1 substituted; table header token | z | e^z | p → logit column fills: mat 3.2, floor 2.4, couch 1.9, bed 1.5, roof 0.3 → e^z column fills row by row: 24.53, 11.02, 6.69, 4.48, 1.35 → the e^z column sums into a terracotta total: 48.07 → each e^z divides by 48.07; p column fills: 51%, 22.9%, 13.9%, 9.3%, 2.8% → the p column tips over into five horizontal probability bars: 'the dice'

## B05 · MECHANISM · B05_TempSweep  (59 words, ~17 s)

Now turn the knob. At zero point two, every logit is divided by zero point two, so every gap grows five times, and mat takes ninety-eight percent. At two, the gaps shrink by half: mat falls to thirty-five, and roof climbs from almost nothing to eight. Low temperature sharpens. High temperature flattens. And watch the order: it never changes.

*On screen:* five probability bars at T = 1 (from B04); a temperature dial at right reads 1 → dial turns to 0.2; bars morph: mat 98%, floor 1.8%, couch 0.1%, bed 0%, roof 0% → mat's bar lights terracotta at 98% → dial turns through 1 to 2; bars flatten: mat 35%, floor 23.5%, couch 18.3%, bed 15%, roof 8.2% → roof's counter climbs 0% → 8.2% → labels 'sharpens' (T < 1) and 'flattens' (T > 1) land at the dial's ends → rank numbers 1–5 above the bars stay fixed through a final sweep 0.2 ↔ 2: 'order never changes'

## B06 · MECHANISM · B06_Rolls  (62 words, ~18 s)

Here's where the answers start to differ. Lay the probabilities end to end, from zero to one. A seeded random number lands somewhere on that line, and whichever token owns that stretch wins. Now the same twenty rolls at each temperature. At zero point two: mat, twenty times out of twenty. At one: four different words. At two: all five, even roof.

*On screen:* the T = 1 bars lay end to end into one strip from 0 to 1, segments labelled by token → a terracotta tick drops at u = 0.2616; the segment it lands in lights: 'mat' → three strips stack (T = 0.2, 1, 2); the same 20 ticks drop on all three at once → row T = 0.2 fills with 20 word chips: all 'mat' → row T = 1 fills: 4 distinct words — mat 11, floor 7, couch 1, bed 1 → row T = 2 fills: 5 distinct words — mat 8, floor 4, couch 6, bed 1, roof 1; 'roof' chip lights terracotta

## B07 · FALSIFIABILITY · B07_TenThousand  (58 words, ~17 s)

Twenty rolls prove very little, so test the claim. If softmax really sets the odds, ten thousand rolls should land on its predicted shares, and they could have missed. At temperature one, it predicts fifty-one percent mat; the count comes back fifty-one point three. Across all three temperatures and all five tokens, nothing misses by even one point.

*On screen:* header: 'prediction: softmax shares · test: 10,000 seeded rolls' → T = 1: hollow 'predicted' outlines for five bars draw on → solid 'counted' bars grow into them; mat counter: predicted 51% · counted 51.3% → two small panels slide in beside it: T = 0.2 and T = 2, outlines and solid bars → gap chips per temperature: T = 0.2: max gap 0.02 pts · T = 1.0: max gap 0.76 pts · T = 2.0: max gap 0.67 pts → terracotta verdict chip: 'prediction survives'

## B08 · MECHANISM · B08_Greedy  (60 words, ~17 s)

Now push the knob toward zero. At zero point five, mat holds seventy-six percent. At zero point one, ninety-nine point nine seven. In the limit there's no roll at all: just take the top token. That's greedy decoding, and it's what temperature zero means, since the formula itself can't divide by zero. Same prompt, same answer, at least in principle.

*On screen:* the 0-to-1 strip from B06; the dial reads 1, mat's segment 51.0% → dial clicks to 0.5: mat's segment widens to 76.19% → dial clicks to 0.1: mat fills 99.97%; the other four collapse to a hairline → the strip becomes solid terracotta 'mat'; the random tick disappears: 'argmax — no roll' → MathTex note: T = 0 is a rule (take the max), not a value plugged into z_i/T → 20 chips fill: 'mat' ×20; caption 'same prompt, same answer (in principle)'

## B09 · FALSIFIABILITY · B09_WrongRanking  (67 words, ~19 s)

And here's what the knob can't do. Suppose a model ranks Sydney just above Canberra as Australia's capital. At temperature one, it's wrong two times in three. Turn it down to zero point two: wrong more than four times in five. Greedy: wrong every time. Turn it up to two, and Canberra actually slips; Melbourne and Perth take the extra. Temperature changes the spread, never the ranking.

*On screen:* prompt chip 'The capital of Australia is ___'; caption 'hypothetical model · constructed logits'; Canberra marked ✓ correct → four bars at T = 1: Sydney 45%, Canberra 33.3%, Melbourne 15%, Perth 6.7%; counter 'wrong 66.7%' → dial to 0.2: Sydney 81.5%, Canberra 18.2%, Melbourne 0.3%, Perth 0%; counter 'wrong 81.8%' → greedy: Sydney's bar fills to 100% terracotta; counter 'wrong 100%' → dial to 2: Sydney 35.4%, Canberra 30.5%, Melbourne 20.4%, Perth 13.7%; Canberra's counter slips 33.3% → 30.5% → rank badges 1–4 unchanged through the whole sweep: 'spread, not ranking'

## BVDT · VERDICT · ClaudeVerdictArtifact  (63 words, ~18 s; lead silence 0.5 s)

Let's recap with Claude. A model scores every token it knows; those scores are logits. Softmax turns logits into probabilities that add up to one. Temperature divides the logits first: low sharpens, high flattens. Sampling rolls those odds, so the same prompt can come back different. Temperature zero is greedy: always the top token, no dice. Temperature changes the spread, never the ranking.

*On screen:* verdict artifact card in on cream → heading types → lines 1–6 land on their spoken cue

*Verdict card lines:* A model scores every token it knows; those scores are logits. / Softmax turns logits into probabilities that add up to one. / Temperature divides the logits first: low sharpens, high flattens. / Sampling rolls those odds, so the same prompt can come back different. / Temperature zero is greedy: always the top token, no dice. / Temperature changes the spread, never the ranking.

## BHTF · YOUR_TURN · ClaudeComposerAsk  (139 words, ~40 s)

Your turn. Paste this into Claude: Write a short Python script, no M L libraries, that applies softmax with temperature to five logits: mat three point two, floor two point four, couch one point nine, bed one point five, roof zero point three. Print the probabilities at temperatures zero point two, one and two. Then draw one thousand seeded samples at each temperature and compare the counts with the probabilities. Finally, using only the printed numbers, explain what temperature can change and what it can't. Here's what to check. At temperature one, mat should come out at fifty-one percent. The thousand-draw counts should land near the probabilities, not exactly on them. And the ranking should hold at every temperature. If Claude says turning the temperature down makes answers more accurate, ask it to show you that in the numbers.

*On screen:* composer card in on cream → greeting 'Your turn.' types → the prompt types into the composer → runningText 'paste this into Claude…' → three check lines cascade in as each is spoken

*Prompt as typed on screen:* Write a short Python script, no ML libraries, that applies softmax with temperature to five logits: mat 3.2, floor 2.4, couch 1.9, bed 1.5, roof 0.3. Print the probabilities at temperatures 0.2, 1 and 2. Then draw 1,000 seeded samples at each temperature and compare the counts with the probabilities. Finally, using only the printed numbers, explain what temperature can change and what it can't.

## BOUT · OUTRO · ClaudeTitleOutro  (8 words, ~2 s; tail silence 1.0 s)

Softmax and Temperature, Explained. At Nik Bear Brown.

*On screen:* cream page; polarity seeded from slug → title types → handle @NikBearBrown → slug-seeded mascot animates under the handle

**Total:** 751 words, about 3.6 min at film 1's measured Kokoro rate (3.51 words/s), plus 2.3 s of scripted silence.
