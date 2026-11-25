# SCRIPT — Overfitting, When a Perfect Score Lies

Narration for review (GATE P). Generated from beat_sheet.json.
Greeting: Namaste, Liam. Voice: Kokoro am_onyx. Pronounce: Namaste → /nˈʌməstˌeɪ/.

## B00 · ASK · ClaudeComposerAsk · 28 words

Namaste, this is Liam, in for Bear. The ask: my model scored zero error on its training data. Perfect. Should I trust it? Show me with real numbers.

*Composer text:* My model scored zero error on its training data. Perfect. Should I trust it? Show me with real numbers.

*Result lines:* degree 15: training error 0, test error 9,882.6 · degree 3: training error 0.0586, test error 0.0471 · the honest grade comes from data the model never saw

*On screen:* composer card fades in on cream → greeting 'Namaste, Liam' types above the composer → the ask types in → runningText 'fitting sixteen noisy points…' appears → three result lines cascade in; '9,882.6' is the one terracotta moment

## B01 · BLUF · BrutalistHesitantWriter · 33 words

A perfect training score can mean memorized noise. A model flexible enough to pass through every point it was shown has learned the points, not the pattern, and stumbles on the next one.

*On screen:* cream page holds; caret blinks → types 'A perfect training score / means a perfect model.' → 'means a perfect model' turns terracotta, hesitates, backspaces → types 'can mean memorized noise' → final lines settle: 'A perfect training score / can mean memorized noise.'

## B02 · FRAMEWORK · B02_Setup · 58 words

Here's the setup. A smooth curve, the truth, which the model never gets to see. Sixteen points drawn from it, each knocked off by random noise: that's the training set. A thousand more, drawn the same way and locked away: the test set. The model fits the sixteen. We grade it on the thousand it has never seen.

*On screen:* axes draw on, x from −1 to 1 → dashed curve y = sin(πx) draws on; tag 'the truth (hidden from the model)' → 16 ink dots drop onto the curve, then each jumps off it by its noise; faint tick joins each dot to the curve → bracket chip: 'training set · 16 points' → 60 faint hollow dots (preview of the 1,000) fade in beside, then slide into a box labelled 'test set · 1,000 points · locked' → the dashed truth curve fades to 40% (the model can't see it); arrows: 'fit ← training' and 'grade ← test'; the 'grade' arrow is terracotta

## B03 · FRAMEWORK · B03_ErrorMeasure · 63 words

The grade is one number, the mean squared error. For each point, take the gap between the real value and the model's guess, and square it, so misses above and below both count, and big misses count most. Then average over every point. On the training points, that's training error. On the test points, test error. Zero means every point was hit exactly.

*On screen:* MathTex typesets: MSE = (1/n) Σᵢ₌₁ⁿ (yᵢ − f̂(xᵢ))² → box spotlight on yᵢ: 'real value'; box spotlight on f̂(xᵢ): 'model's guess' → box spotlight on the '−' and the square: 'gap, squared' → worked term slides in under the equation: one training point, the line's worst miss: gap -1.032, squared 1.065 → box spotlight on (1/n) Σ: 'average over all 16': 4.546 ÷ 16 = 0.284 → two chips under the equation: 'on training points → training error' | 'on test points → test error' → terracotta '= 0' chip: 'every point hit exactly'

## B04 · WORKED_EXAMPLE · B04_ThreeFits · 70 words

Fit three models to the same sixteen points. A straight line, degree one, is too stiff: it misses the bend, at about zero point two eight in training, zero point two seven on test. Degree three follows the curve: zero point zero six, and zero point zero four seven. Degree fifteen has sixteen coefficients for sixteen points, so it threads every one. Training error: zero. Test error: almost ten thousand.

*On screen:* three panels side by side, the same 16 dots in each; headers 'degree 1', 'degree 3', 'degree 15' → left: straight line draws through the dots; counters train 0.284 | test 0.273 → middle: cubic draws, hugging the hidden curve; counters 0.059 | 0.047 → right: degree-15 curve threads every dot, swinging off the panel between them (clipped at the frame, arrow marks the exit) → right counter train → 0 → right counter test spins up to 9,882.6 in terracotta

## B05 · MECHANISM · B05_TheU · 67 words

Do that for every degree from zero to fifteen. Training error, in ink, only ever goes down: a more flexible model can always fit the same points at least as well. Test error falls too, at first. It bottoms out around degree three to six, just above the dashed line, which is the noise itself. Then it turns, climbs, and leaves the chart. That U is overfitting.

*On screen:* axes: x 'degree 0–15', y 'error 0–0.6'; dashed floor line at 0.040: 'noise floor: even the true curve scores 0.04' → ink training-error dots land degree by degree, stepping down to 0 at 15 → test-error dots land degree by degree, falling with the ink ones → minimum ringed at degree 5: 0.0466 → test dots climb, then exit the top from degree 11; terracotta exit chips 1.8 · 26.4 · 5,807.1 · 8,251.1 · 9,882.6 → the gap between the two curves shades; tag 'overfitting'; small chip 'same shape across 500 fresh datasets'

## B06 · FALSIFIABILITY · B06_MoreData · 70 words

Here's where the simple story bends. Is degree fifteen just too complex? Keep the model, and add data. At twenty points, test error drops to about twenty-nine. At a hundred, zero point zero four eight. At a thousand, zero point zero four one, right on the noise floor, and training error has risen from zero to meet it. Complexity alone isn't the problem. Complexity the data can't pin down is.

*On screen:* the degree-15 panel from B04, wild curve over 16 dots; counter n = 16 → dots multiply to 20; curve refits; test counter 28.8 → dots multiply to 100; curve calms; test 0.048 → 1,000 dots; curve lies on the hidden truth; test 0.041 → side ladder: train ↑ and test ↓ counters for n = 16 (0 | 9,882.6), 20 (0.006 | 28.776), 30 (0.018 | 0.13), 50 (0.021 | 0.098), 100 (0.034 | 0.048), 200 (0.039 | 0.047), 1000 (0.041 | 0.041) → both counters meet at the dashed 0.040 floor; terracotta ring on the meeting point

## B07 · FALSIFIABILITY · B07_PeekedScore · 70 words

One more way a score can lie. Say you try all sixteen degrees and keep whichever scores best on a held-out validation set. Now that score helped choose the model. Across a thousand repeats, it came in better than the real error seven times in ten. The fix: choose on validation, then report on a test set nobody touched. That lands about half and half, as an honest score should.

*On screen:* data strip splits into three labelled blocks: 'train 30 · validation 20 · test 20' → sixteen candidate curves flicker; validation picks one (the chosen degree glows) → left panel 'choose and report on validation': a 10×10 grid of 100 trials fills; optimistic trials fill terracotta → left counter: 70% optimistic; median reported 0.0439 vs real 0.0508 → right panel 'choose on validation, report on untouched test' fills the same way → right counter: 55% optimistic; median 0.0506 vs 0.0508; reference chip 'degree fixed in advance: 53%'

## BVDT · VERDICT · ClaudeVerdictArtifact · 67 words

Let's recap with Claude. Training error grades the model on answers it has already seen. Test error, on data held back, is the honest grade. As flexibility grows, training error falls; test error falls, then climbs. A perfect training score can mean the noise was memorized. More data lets a flexible model behave. And a score you chose by is spent, so keep one test set untouched.

*Card lines:* Training error grades the model on answers it has already seen. / Test error, on data held back, is the honest grade. / As flexibility grows, training error falls; test error falls, then climbs. / A perfect training score can mean the noise was memorized. / More data lets a flexible model behave. / A score you chose by is spent; keep one test set untouched.

*On screen:* verdict artifact card in on cream → heading types → lines 1–6 land on their spoken cue

## BHTF · YOUR_TURN · ClaudeComposerAsk · 141 words

Your turn. Paste this into Claude: Using only Python and NumPy, draw sixteen points from y equals sine of pi x on the interval from minus one to one, with Gaussian noise of standard deviation zero point two, plus a thousand more as a test set. Fit polynomials of degree zero to fifteen and print the training and test error for each. Repeat with two hundred training points. Then, from the printed numbers only, tell me which degree you would ship in each case, and how you chose it. Here's what to check. Training error should never go up as the degree rises. With sixteen points, degree fifteen should score essentially zero in training and something enormous on test. And watch how Claude picks the degree. If it picks by the test error, ask it what it should have used instead.

*Composer text:* Using only Python and NumPy, draw 16 points from y = sin(pi x) on the interval from -1 to 1, with Gaussian noise of standard deviation 0.2, plus 1000 more as a test set. Fit polynomials of degree 0 to 15 and print the training and test error for each. Repeat with 200 training points. Then, from the printed numbers only, tell me which degree you would ship in each case, and how you chose it.

*Result lines:* check: training error never rises as the degree goes up · check: 16 points, degree 15 → training error ≈ 0, test error huge · check: the degree is chosen without peeking at the test set

*On screen:* composer card in on cream → greeting 'Your turn.' types → the prompt types into the composer → runningText 'paste this into Claude…' → three check lines cascade in as each is spoken

## BOUT · OUTRO · ClaudeTitleOutro · 10 words

Overfitting, When a Perfect Score Lies. At Nik Bear Brown.

*On screen:* cream page; polarity seeded from slug → title types → handle @NikBearBrown → slug-seeded mascot animates under the handle
