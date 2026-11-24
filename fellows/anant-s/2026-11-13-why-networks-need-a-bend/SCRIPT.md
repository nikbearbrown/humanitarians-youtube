# SCRIPT — Why Neural Networks Need a Bend

Narration for review (GATE P). Generated from beat_sheet.json by make_sheet.py; edit make_sheet.py, not this file.
Estimated runtime: 840 words ≈ 4.0 min at film 1's measured Kokoro pace (3.5 words/s).

## B00 · ASK · ClaudeComposerAsk · 32 words

Jambo, this is Liam, in for Bear. The ask: why does every neural network put a bend between its layers? Wouldn't stacking more straight layers be enough? Show me with real numbers.

*On screen:* composer card fades in on cream → greeting 'Jambo, Liam' types above the composer → the ask types in → runningText 'multiplying it out…' appears → three result lines cascade in

## B01 · BLUF · BrutalistHesitantWriter · 33 words

A bend between layers makes a network powerful. Stacking alone isn't enough: straight layers, however many, collapse into one. Add a simple bend between them, and the network can finally draw a curve.

*On screen:* cream page holds; caret blinks → types 'Stacking more layers / makes a network powerful.' → 'Stacking more layers' turns terracotta, hesitates, backspaces → types 'A bend between layers' → final lines settle: 'A bend between layers / makes a network powerful.'

## B02 · FRAMEWORK · B02_TwoMoves · 62 words

Two moves build a plain neural network. The first is a layer: multiply by a matrix. It can stretch, rotate and shear the plane, but straight lines stay straight, and parallel lines stay parallel. The second is the bend, here a ReLU: keep positive numbers, flatten negatives to zero. That one creases the plane. A network alternates the two: layer, bend, layer.

*On screen:* a square grid of the input plane draws on, axes in ink → label 'layer = multiply by a matrix' (MathTex Wx) → grid shears and rotates under a 2×2 matrix; every grid line stays straight and parallel → inset: ReLU graph, flat at zero for z<0, slope 1 for z>0 (MathTex ReLU(z)=max(0,z)) → grid passes through ReLU: negative halves fold flat onto the axes; creases light terracotta → the word 'bend' in the ReLU header is boxed in ink on 'layer, bend, layer'

## B03 · WORKED_EXAMPLE · B03_Collapse · 56 words

Here are two straight layers with no bend: seeded random matrices. Push the input, minus one, two, through the first layer: minus one, minus three. Then the second: seven, eight. Now multiply the two matrices first, into one. Push the same input through that single matrix: seven, eight. Identical. Two layers were one layer in disguise.

*On screen:* MathTex W₁ = [[3, 1], [1, -1]], W₂ = [[-1, -2], [-2, -2]], x = (−1, 2) typeset (seed 0) → left path: W₁x = (−1, −3) lands under W₁ → left path: W₂(W₁x) = (7, 8) → right path: W₂W₁ multiplies out to [[-5, 1], [-8, 0]] (one matrix) → right path: (W₂W₁)x = (7, 8) → MathTex W₂(W₁x) = (W₂W₁)x between the two results; terracotta BOX on the '='

## B04 · MECHANISM · B04_TenLayers · 67 words

Not a lucky pick. A thousand random inputs, ten random layers in a row. Multiply the ten matrices into one, and every output lands on top of the stack's output. The largest gap is in the fifteenth decimal place: rounding, not structure. Add a shift to each layer, a bias, and you still get one matrix plus one shift. Depth without a bend buys no new shapes.

*On screen:* a cloud of 1,000 input points (seed 1) → the cloud morphs through ten linear layers, one after another (layer counter 1→10) → a ghost cloud from the single multiplied-out matrix lands exactly on top → counter: largest difference 8.88e-15 (MathTex 8.88×10⁻¹⁵), chip 'float rounding' → MathTex W₂(W₁x + b₁) + b₂ = (W₂W₁)x + (W₂b₁ + b₂) typesets; terracotta box on the right-hand side

## B05 · MECHANISM · B05_NoLine · 68 words

Now a problem no straight map can touch. XOR: output one when exactly one input is on. Four corners of a square, the ones on one diagonal, the zeros on the other. Find a single line with both ones on one side. We tried over a hundred and fifteen thousand. The best gets three of four, and four lines of algebra prove no line ever gets all four.

*On screen:* unit square; corners (0,0),(1,1) as hollow ink circles '0', (0,1),(1,0) as filled ink dots '1' → a line sweeps and rotates across the square; a 'correct: n of 4' counter flickers → tally: 'lines tried 115,560' climbs; 'best: 3 of 4' locks → the best line freezes with one point on the wrong side, ringed terracotta → the four inequalities typeset (MathTex) and add to a contradiction

## B06 · MECHANISM · B06_StuckAtHalf · 60 words

So give it depth. A two-layer network with no bend, trained by gradient descent for five thousand steps. The loss sinks to zero point two five and flattens. Every output settles at one half: a shrug. That's exactly what the best single line predicts, because this network is a single line. A hundred seeds, same floor. None gets all four.

*On screen:* network strip x → W₁ → W₂ → y with the bend slot visibly empty → loss curve plots over 5,000 steps (every 250, executed) and flattens at 0.25 → four output bars settle at 0.5, 0.5, 0.5, 0.5 against targets 0, 1, 1, 0 → beside them: least-squares best line predicts 0.5, 0.5, 0.5, 0.5; terracotta '=' box joins the two → chip: '100 seeds: lowest loss 0.25, all four right: 0'

## B07 · WORKED_EXAMPLE · B07_ReluFix · 62 words

Now add one bend. Two hidden units, weights set by hand, from the Deep Learning textbook. Each unit adds up the inputs; the second also subtracts one. Then the ReLU. At zero, zero, the second unit reads minus one, and the ReLU flattens it to zero. The output takes the first unit minus twice the second. Zero, one, one, zero. XOR, exactly.

*On screen:* MathTex h = ReLU(Wx + c), y = w·h with W, c, w as matrices; caption 'weights: Goodfellow, Bengio & Courville (2016), §6.1' → table header x | Wx + c | ReLU | y | target → row x=(0, 0): z=(0, −1) → h=(0, 0); terracotta box on the −1 → 0 clip → rows (0, 1), (1, 0), (1, 1) land: h = (1, 0), (1, 0), (2, 1) → y column fills 0, 1, 1, 0 and matches the target column, row by row ✓

## B08 · MECHANISM · B08_Fold · 67 words

Here's what the bend did, geometrically. The first layer lays all four points on one line, and the two ones land on the same spot, stuck between the zeros. ReLU folds that line at the corner, pulling the zero, zero point up to the origin. Now one straight line separates them. Unfold it back to the square, and that line becomes a band: ones inside, zeros out.

*On screen:* input square with the four XOR points → linear move to (z₁, z₂): points slide onto the line z₂ = z₁ − 1; the two '1' points merge at (1, 0) → ReLU fold: the part of that line below the axis folds up; (0, −1) lands on (0, 0); the crease glows terracotta → line h₁ − 2h₂ = ½ draws, the merged '1' on one side, both '0's on the other → unfold back to the input square: the region becomes a band between x₁ + x₂ = ½ and x₁ + x₂ = 3⁄2

## B09 · FALSIFIABILITY · B09_HundredSeeds · 62 words

So is the bend enough? Same two-unit network, but now trained from a hundred random starts instead of set by hand. Here, eighteen find XOR. Eighty-two get stuck, most with a hidden unit that went flat and never woke up. The bend makes a solution possible; it doesn't make training find it. Give it eight units, and ninety-one of a hundred succeed.

*On screen:* 10×10 grid of seed tiles, labelled 'seeds 0–99, 2 hidden units' → tiles resolve in seed order: solved = ink check, stuck = hollow; counter climbs to 18 / 100 → inset for stuck seed 0: one hidden unit flat at zero on all four inputs, outputs 0.5, 0.5, 0.5, 0.5; terracotta ring on the flat unit → chip: '69 of 82 stuck runs have a dead unit' → a second grid '8 hidden units' resolves beside it: 91 / 100

## B10 · FALSIFIABILITY · B10_StraightAgain · 68 words

And the bend has a shape. Walk the hand-set network along the square's diagonal. The output is flat, then climbs in a straight line, then falls in a straight line. Two kinks, exactly where a unit switches on. Keep walking past the data and it never curves back: at three, three it says minus four. Between and beyond its kinks, a ReLU network is made of straight pieces.

*On screen:* inset square with the diagonal x = (t, t) marked; main axes t vs y → output traces left to right: flat 0, then up to 1 at t = ½, then down → terracotta dots on the two kinks at t = 0 and t = ½; labels 'unit 1 on', 'unit 2 on' → trace continues past t = 1 with no curve: (3, 3) → −4 → MathTex pieces: y = 0, y = 2t, y = 2 − 2t (straight pieces bracketed)

## BVDT · VERDICT · ClaudeVerdictArtifact · 71 words

Let's recap with Claude. A layer multiplies by a matrix: straight lines stay straight. Stacked layers without a bend multiply out to one matrix. XOR has no separating line, so no purely linear network learns it. One ReLU bend folds the plane; two hidden units solve XOR exactly. The bend makes a solution possible, not easy to find. Between and beyond its kinks, a ReLU network is made of straight pieces.

*On screen:* verdict artifact card in on cream → heading types → lines 1–6 land on their spoken cue

## BHTF · YOUR_TURN · ClaudeComposerAsk · 122 words

Your turn. Paste this into Claude: Write a short Python script using only numpy. Train a tiny network on XOR twice: once with no activation, once with a ReLU and two hidden units. Use plain gradient descent from twenty random seeds each, and print how many seeds get all four points right. Then, from the printed numbers alone, explain why the linear version never succeeds and why the ReLU version sometimes fails. Here's what to check. The linear runs should never get all four right, on any seed. For the ReLU runs that fail, ask Claude to print the hidden units, and look for one stuck at zero. And make sure the explanation comes from the printed numbers, not a recited theorem.

*On screen:* composer card in on cream → greeting 'Your turn.' types → the prompt types into the composer → runningText 'paste this into Claude…' → three check lines cascade in as each is spoken

## BOUT · OUTRO · ClaudeTitleOutro · 10 words

Why Neural Networks Need a Bend. At Nik Bear Brown.

*On screen:* cream page; polarity seeded from slug → title types → handle @NikBearBrown → slug-seeded mascot animates under the handle
