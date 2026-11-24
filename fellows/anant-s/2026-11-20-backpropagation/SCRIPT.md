# SCRIPT — Backpropagation, One Error at a Time

Narration for review (GATE P). Generated from beat_sheet.json.

## B00 · ASK · ClaudeComposerAsk

Hola, this is Liam, in for Bear. The ask: gradient descent needs a slope for every weight. How does a network get all of them at once? Show me backpropagation, with real numbers.

*On screen:* composer card fades in on cream → greeting 'Hola, Liam' types above the composer → the ask types in → runningText appears → three result lines cascade in

## B01 · BLUF · BrutalistHesitantWriter

Backpropagation sends the error backward once. It doesn't test the weights one by one. It runs the chain rule from the loss back to the input, and every weight gets its slope.

*On screen:* cream page holds; caret blinks → types 'Backpropagation / tests every weight one by one.' → the wrong phrase turns terracotta, hesitates, backspaces → types 'sends the error backward once' → final lines settle

## B02 · FRAMEWORK · B02_Chain

Here's the whole network: four small steps in a row. Multiply by the first weight. Squash with tanh. Multiply by the second weight. Then score it: the loss is how far we land from the target, squared. Every step is simple, and every step has its own local slope. Backpropagation only ever needs those.

*On screen:* node x appears at left → box '× w₁' → node z draws on → box 'tanh' → node h draws on → box '× w₂' → node y draws on → box '(y − t)²' → node L (loss) draws on → under each box, a small 'local slope' tag appears, one by one

## B03 · FRAMEWORK · B03_ChainRule

The chain rule says how a change in the first weight reaches the loss: multiply the local slopes along the path. How the loss moves with the output. How the output moves with h, which is the second weight. How tanh bends. And how z moves with the first weight, which is just the input. Four factors, one product.

*On screen:* MathTex: ∂L/∂w₁ = ∂L/∂y · ∂y/∂h · ∂h/∂z · ∂z/∂w₁ → box spotlight on ∂L/∂y; label 'how the loss moves with the output' → box on ∂y/∂h; label 'the second weight, w₂' → box on ∂h/∂z; label 'how tanh bends: 1 − h²' → box on ∂z/∂w₁; label 'the input, x' → all four factors underlined together: 'one product'

## B04 · WORKED_EXAMPLE · B04_Forward

Real numbers. Input one, target zero point two, weights zero point five and two. Forward: z is zero point five. Tanh gives zero point four six. Times two, the output is zero point nine two. We wanted zero point two, so the loss is about zero point five two. Now run it backward.

*On screen:* the B02 chain returns; x=1, t=0.2, w₁=0.5, w₂=2 tagged → z fills: 0.5 → h fills: 0.4621 → y fills: 0.9242 → L fills: 0.5245 (terracotta)

## B05 · WORKED_EXAMPLE · B05_Backward

Backward, the slopes multiply. The loss moves one point four five per unit of output. Times the second weight: two point nine. Times the tanh slope, zero point seven nine: two point two eight. That's the first weight's slope. The second weight's is zero point six seven. One step, step size zero point one, and the loss falls from zero point five two to just under zero point one.

*On screen:* terracotta arrows run right-to-left under the chain → ∂L/∂y = 1.4485 appears at y → × w₂ → ∂L/∂h = 2.8969 → × tanh slope 0.7864 → ∂L/∂z = 2.2783 → × x → ∂L/∂w₁ = 2.2783; ∂L/∂w₂ = 0.6694 → step: loss counter 0.5245 → 0.0983

## B06 · MECHANISM · B06_Check

Is that slope real? Check it the slow way: nudge the first weight up and down by a hundred-thousandth, and measure how the loss changes. Backprop says two point two seven eight three. The nudge says the same, to eight decimal places. But nudging costs two passes per weight. With a million weights, that's two million passes. Backprop needs one.

*On screen:* w₁ dial nudges ± 0.00001; two loss readings appear → side by side: backprop 2.27828974 | nudge 2.27828974 → difference chip: 2.68e-10 → cost bars: '2 passes per weight × 1,000,000' vs 'one backward pass'

## B07 · FALSIFIABILITY · B07_Vanishing

Here's where it bites. Stack ten sigmoid layers. A sigmoid's slope is never more than a quarter, so every layer multiplies the gradient by about zero point two two. By the time the error reaches the first layer, it's about three and a half ten-millionths. The early layers barely learn. That's the vanishing gradient, and it's one reason deep networks moved to ReLU.

*On screen:* ten sigmoid layers stack left to right → chip: 'sigmoid slope ≤ 0.25' → gradient bars shrink layer by layer, right to left (log scale) → first-layer bar labelled 3.483e-07 (terracotta)

## BVDT · VERDICT · ClaudeVerdictArtifact

Let's recap with Claude. Backprop runs the chain rule from the loss back to every weight. Each step only needs its own local slope, and slopes multiply along the path. One backward pass gives every weight its slope. A finite-difference check agrees, at far higher cost. And long chains of small slopes make gradients vanish.

*On screen:* verdict artifact card in on cream → heading types → lines 1–6 land on their spoken cue

## BHTF · YOUR_TURN · ClaudeComposerAsk

Your turn. Paste this into Claude: Write a short Python script, no M L libraries, for y equals w two times tanh of w one times x, with loss y minus t, squared. Use x equals one, t equals zero point two, w one equals zero point five, w two equals two. Compute the slope of the loss for both weights with the chain rule, then check both with central finite differences, using a step of one hundred-thousandth. Print each pair and their difference. Then set w one to five, and explain, from the numbers, which factor in the chain shrinks the first weight's slope. Here's what to check. The first weight's slope should be about two point two eight, and match the finite difference. At w one equals five, watch the tanh slope collapse to almost nothing. And see whether Claude names the culprit: one minus tanh squared.

*On screen:* composer card in on cream → greeting 'Your turn.' types → the prompt types into the composer → runningText 'paste this into Claude…' → three check lines cascade in as each is spoken

## BOUT · OUTRO · ClaudeTitleOutro

Backpropagation, One Error at a Time. At Nik Bear Brown.

*On screen:* cream page; polarity seeded from slug → title types → handle @NikBearBrown → slug-seeded mascot animates under the handle
