# SCRIPT — Gradient Descent, One Step at a Time

Narration for review (GATE P). Generated from beat_sheet.json.

## B00 · ASK · ClaudeComposerAsk

Ciao, this is Liam, in for Bear. The ask: how does a neural network actually learn? Skip the hype. Show me the one rule underneath, with real numbers.

*On screen:* composer card fades in on cream → greeting 'Ciao, Liam' types above the composer → the ask types in → runningText 'working through the math…' appears → three result lines cascade in

## B01 · BLUF · BrutalistHesitantWriter

Training a model keeps stepping downhill. It never searches for the best answer. It measures which way the error rises, takes a small step the other way, and repeats, step after step.

*On screen:* cream page holds; caret blinks → types 'Training a model / finds the best answer.' → 'finds the best answer' turns terracotta, hesitates, backspaces → types 'keeps stepping downhill' → final lines settle: 'Training a model / keeps stepping downhill.'

## B02 · FRAMEWORK · B02_Landscape

Here is the whole picture. Across the bottom, one setting of the model. Call it theta. Up the side, the loss: how wrong the model is at that setting. The model sits somewhere on this curve, and it can't see the bottom. All it can measure is the slope right where it stands. The slope points uphill. So step the other way.

*On screen:* axes draw on; x labelled 'setting θ', y labelled 'loss' → the bowl L(θ)=θ² draws on → a terracotta ball lands at θ=3 → tangent line draws through the ball: 'slope' → arrow points uphill, then a second arrow flips to point downhill: 'step'

## B03 · FRAMEWORK · B03_UpdateRule

Written down, it's one line. The new setting becomes the old setting, minus a step. The step is two things multiplied: the slope of the loss right here, called the gradient, and eta, the step size, a number you choose. Steep slope, big step. Flat ground, tiny step. That minus sign is the whole idea: go against the slope.

*On screen:* update rule typesets: θ_{t+1} = θ_t − η ∇L(θ_t) → spotlight on θ_{t+1}; label below: 'new setting' → spotlight on θ_t; label: 'current setting' → spotlight on ∇L(θ_t); label: 'slope of the loss here' → spotlight on η; label: 'step size (you choose it)' → spotlight on the minus sign: 'against the slope'

## B04 · WORKED_EXAMPLE · B04_FiveSteps

Real numbers. Loss is theta squared, so the slope is two theta. Start at three, step size zero point one. Slope six, step zero point six: we land at two point four. Slope four point eight: one point nine two. Each step shrinks theta by the same factor, zero point eight. Five steps in, the loss fell from nine to just under one.

*On screen:* bowl and ball at θ=3; table header t | θ | slope | loss → row t=0: 3 | 6 | 9 → ball steps to 2.4; row t=1 lands → ball steps to 1.92; row t=2 lands → rows t=3..5 land with each step; '×0.8 per step' chip appears → loss column highlights 9 → 0.9664

## B05 · FALSIFIABILITY · B05_StepSize

The step size is where this bites. Same bowl, same start, three choices. At zero point zero one, ten steps later theta has barely moved: two point four five. At zero point one, it's down to zero point three two. At one point one, every step overshoots the bottom and lands further out; after ten steps, theta is past eighteen. Too big, and it doesn't slow down. It runs away.

*On screen:* three bowls side by side, labelled η=0.01, η=0.1, η=1.1 → left ball creeps; counter settles at θ₁₀ = 2.4512 → middle ball rolls in; counter θ₁₀ = 0.3221 → right ball zig-zags across the bottom, each bounce wider; terracotta → right counter climbs to θ₁₀ = 18.5752

## B06 · FALSIFIABILITY · B06_TwoValleys

The second failure: the slope only knows where you are. This loss has two valleys. Start on the right, and the ball settles into the shallow one, at a loss of minus one point oh seven, and stops, because the slope there is zero. The deeper valley, at minus three point five one, is right next door, and gradient descent never sees it. Where you start decides where you end.

*On screen:* two-valley curve L(θ)=θ⁴−3θ²+θ draws on → ball drops at θ=2 and rolls into the right valley → label at rest: 'loss -1.0702', slope chip '0' → left valley lights terracotta: 'loss -3.5139' → ghost ball from θ=−2 rolls into the deep valley: start decides end

## B07 · MECHANISM · B07_Batches

Real models run a version of this same rule on millions, even billions, of settings at once, so the bowl becomes a landscape you can't draw. Two tricks make that affordable. Backpropagation computes every slope in one backward pass. And each step looks at a small batch: here, eight points out of two hundred. The path wobbles, but each step costs a twenty-fifth as much, and the fit lands within a few percent.

*On screen:* contour map of the loss over two settings (w, b) fades in → chip: 'backpropagation: every slope in one backward pass' → smooth ink path: 'all 200 points per step' draws to the minimum → wobbly terracotta path: '8 points per step' draws beside it → end chips: loss 0.15 vs 0.1533

## BVDT · VERDICT · ClaudeVerdictArtifact

Let's recap with Claude. Loss measures how wrong the model is, and the gradient is its slope. Each step, the new setting is the old setting minus the step size times the slope. The step size decides it: too small crawls, too big runs away. It finds a valley, not necessarily the lowest one. And at scale: backpropagation for the slopes, small batches for speed.

*On screen:* verdict artifact card in on cream → heading types → lines 1–5 land on their spoken cue

## BHTF · YOUR_TURN · ClaudeComposerAsk

Your turn. Paste this into Claude: Write a short Python script, no M L libraries, that runs gradient descent on loss equals theta squared, starting at theta equals three, for ten steps, with step sizes zero point zero one, zero point one, zero point nine and one point one. Print theta after every step. Then, using only the printed numbers, tell me which runs converge, which oscillate, which blow up, and predict the largest step size that still converges. Here's what to check. Zero point one should go three, two point four, one point nine two. Zero point nine is the interesting one: it flips sign every step and still lands. And watch whether Claude derives the cutoff from the numbers, or just asserts it. If it says one, ask it why.

*On screen:* composer card in on cream → greeting 'Your turn.' types → the prompt types into the composer → runningText 'paste this into Claude…' → three check lines cascade in as each is spoken

## BOUT · OUTRO · ClaudeTitleOutro

Gradient Descent, One Step at a Time. At Nik Bear Brown.

*On screen:* cream page; polarity seeded from slug → title types → handle @NikBearBrown → slug-seeded mascot animates under the handle
