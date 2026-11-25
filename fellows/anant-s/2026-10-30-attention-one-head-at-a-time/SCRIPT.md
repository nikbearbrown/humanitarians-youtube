# SCRIPT — Attention, One Head at a Time

Narration as built, from `beat_sheet.json`. On 2026-11-24 the film was converted from the tldr format to ai-explainer, and Anant approved the new narration. Durations are the measured audio, lead silence included. The pre-conversion script is in `_superseded/format-tldr/docs/SCRIPT.md`.

## B00 · ASK · ClaudeComposerAsk

*32 words · 9.3 s*

Hello, this is Liam, in for Bear. The ask: how does a transformer let each word use the words around it? Skip the hype. Show me one attention head, with real numbers.

*On screen:* composer card fades in on cream → greeting 'Hello, Liam' types above the composer → the ask types in → runningText 'working through the math…' appears → three result lines cascade in

## B01 · BLUF · BrutalistHesitantWriter

*32 words · 10.5 s*

Each word in a sentence blends every word around it. It doesn't pick one. It takes a weighted mix, weighted by how well two words match. Every transformer runs on this step.

*On screen:* cream page holds; caret blinks → types 'Each word in a sentence / picks the one word it needs.' → 'picks the one word it needs' turns terracotta, hesitates, backspaces → types 'blends every word around it' → final lines settle

## B10 · LEARN 1 · B10_ChaseMoves

*59 words · 16.3 s*

Four words: cats chase small dogs. Each one goes into an attention head as a list of four numbers. Follow chase. It comes out as a point, right here. Now swap cats for kids. Chase's own numbers haven't changed, yet it lands somewhere else. The head only sees these four words. So how do the neighbours get inside chase?

*On screen:* sentence 'cats chase small dogs' writes across the top; each word's embedding row (mono) lands beneath it: cats [−1 −1 1 0]; chase [−1 −1 0 −1]; small [1 0 −1 1]; dogs [0 1 1 −1] → a plain ink box 'one attention head' draws between the rows and a light value plane on the right → chase's row passes through the box; a terracotta dot lands at (1.11, 1.64) on 'right here' → 'cats' morphs into 'kids'; its row ticks to [1 1 1 0]; chase's row stays put (brief dim box on it) → chase's dot glides from (1.11, 1.64) to (0.93, 1.06); a ghost stays at the first landing → HOLD on the two landings; dim caption 'toy numbers, not a trained model'

## B11 · LEARN 1 · B11_MixingPoints

*60 words · 15.6 s*

Run each word's numbers through a fixed grid of weights, giving each word a point. Mix two points: some of one, the rest of the other. Half and half lands in the middle. Put zero point eight on cats, and the mix slides toward cats. With all four, weights adding to one, the mix glides but never leaves the shape.

*On screen:* each embedding row slides through a small ink grid labelled 'fixed weights'; four labelled points drop onto the plane: cats (1, 2); chase (2, 2); small (−1, −2); dogs (0, 1) → segment cats–small draws; blend dot at (0, 0) with MathTex label 0.5·cats + 0.5·small → weight sweeps to 0.8: the dot slides to (0.6, 1.2); label morphs to 0.8·cats + 0.2·small → ghost quadrilateral outline through the four points; four weight bars appear beside the plane → bars re-balance three times; the dot glides (0.8, 1.5) → (−0.4, −0.9) → (1.4, 1.5), staying inside the outline (terracotta dot)

## B12 · LEARN 1 · B12_RequestMeetsOffer

*59 words · 17.2 s*

Who sets the weights? Two more grids give each word two more lists: a request, what it's looking for, and an offer, what it has. Chase requests one, zero, one, zero. Against cats' offer, multiply matching entries and add: three. Against its own offer, two. Small and dogs, minus one each. Ask from small instead, and the scores reshuffle.

*On screen:* two small ink grids; each word gains a 'request' row and an 'offer' row (mono integers) → chase's request [1 0 1 0] lifts out in terracotta → it slides beside cats' offer [2 1 1 2]; products [2 0 1 0] pop out and sum into the chip '3' → the request slides down the column: chips '2', '−1', '−1' land beside chase, small, dogs → small's request [1 1 −1 −1] replaces chase's; the four chips tick to [0 −3 2 −1]

## B13 · LEARN 1 · B13_EqualWeights

*49 words · 15.3 s*

Here's the obvious shortcut: skip the scores and weigh every word equally, a quarter each. Watch all four words mix. Cats, chase, small, dogs: every one lands on the same point, the middle of the shape. Four words, one meaning. Equal weights erase exactly what made each word itself.

*On screen:* a 4×4 grid of equal bars '0.25' (one row per word) lands left of the plane → four blend dots, one per word, start at their own points → all four slide together and stack at (0.5, 0.75) as each word is named → terracotta box around the single stacked point on 'one meaning' → dim caption 'equal weights → every word identical'

## B14 · LEARN 1 · B14_HeatMap

*57 words · 16.4 s*

So let the scores decide. Put every request against every offer, and you get a grid. Divide each score by two. Then softmax each row, so it turns positive and adds to one. That's the heat map: who listens to whom. Chase's row puts zero point five three on cats. Before anything moves, where does chase land?

*On screen:* 4×4 score grid fills (rows = who asks, columns = who offers): [−1 3 1 −2] / [3 2 −1 −1] / [0 −3 2 −1] / [−1 2 −3 3] → every cell divides by two (MathTex ÷2 chip; cells re-typeset as halves) → softmax sweeps row by row: cells become weights and shade by size — the heat map: [0.09 0.63 0.23 0.05] / [0.53 0.32 0.07 0.07] / [0.22 0.05 0.6 0.13] / [0.08 0.34 0.03 0.56] → dim caption 'rounded; every row sums to 1' → chase's row gets a terracotta box; the value plane with the four word points slides in on the right → HOLD ≥ 2 s: nothing moves on 'where does chase land?'

## B15 · LEARN 1 · B15_LetTheMatchMix

*40 words · 11.9 s*

Let the heat map set the mix. Zero point five three toward cats, zero point three two toward itself, a little toward the rest. There. Exactly where the head put chase. And every other row lands somewhere of its own.

*On screen:* chase's heat-map row lifts off the grid; its four cells fly to cats, chase, small, dogs and become dot masses (radius ∝ weight) → four pull lines from a blend dot to the points; the dot slides from the centre toward cats → the dot settles at (1.11, 1.64) — onto the HOOK's ghost landing, which flashes terracotta on 'There' → rows cats, small, dogs fire in quick succession; dots land at (1.11, 1.02), (−0.28, −0.52), (0.72, 1.33) (contrast: NAIVE's single stack, ghosted)

## B16 · LEARN 1 · B16_NameIt

*56 words · 15.5 s*

This thing we keep pointing at deserves a name. The request is the query. The offer is the key. The point a word hands over is its value. Stack them into grids, Q, K and V, and the whole head is one line: softmax of Q times K transposed, over root d, times V. That's attention.

*On screen:* the request rows slide together into a 4×4 grid labelled Q ('query'), terracotta label on 'query' → offer rows → K ('key'); the word points → a 4×2 grid V ('value') → Q and K slot into QKᵀ; the ÷2 chip becomes the √d_k denominator; the heat map collapses into softmax( ) → MathTex assembles: Attention(Q, K, V) = softmax(QKᵀ / √d_k) V → the word 'attention' names it, serif, terracotta

## B17 · LEARN 1 · B17_Tangent

*120 words · 35.3 s*

Read it in words. The left side: what the head hands each word. The right side: score every query against every key, shrink the scores, turn each row into weights, and blend the values. The equals sign is a promise: same thing, row for row. Q holds the queries, K the keys, V the values. d k is the length of a key, four here, so we divide by two. For chase: three, two, minus one, minus one. Halved and softmaxed: zero point five three, zero point three two, zero point zero seven, zero point zero seven. The division is a design choice: without it, long keys make huge scores, and softmax stops blending and starts picking. Back to chase.

*On screen:* split stage: the equation holds on the MAIN side; eyebrow 'Equation · tangent' over the SIDE band → LHS sentence writes; terracotta box around Attention(Q,K,V) → RHS sentence writes; box moves to softmax(QKᵀ/√d_k)V → '= : the same thing, row for row' writes; box on '=' (a box, never an underline) → glossary rows land: Q · matrix · one query per word · 4×4 | K · matrix · one key per word · 4×4 | V · matrix · one value per word · 4×2 | d_k · fixed size · key length · 4 | softmax · operator · row → weights · (0,1) → worked row (mono): scores [3 2 −1 −1] → ÷2 [1.5 1 −0.5 −0.5] → weights [0.53 0.32 0.07 0.07] → values claim (tinted box): '÷√d_k is a design choice'; mini-row: without it chase gets [0.71 0.26 0.01 0.01] → re-entry: the side band clears; the equation holds

## B18 · LEARN 1 · B18_Payoff

*59 words · 17.9 s*

Chase's point is no mystery now: zero point five three of cats, zero point three two of itself, a little of small and dogs. Swap cats for kids again. Chase's request scored three against cats' offer, but only minus one against kids'. The weight drains away, mostly back onto chase itself, and the point slides. That was the move.

*On screen:* the HOOK's sentence and chase's dot at (1.11, 1.64) return (same objects); four pull lines labelled [0.53 0.32 0.07 0.07] → 'cats' → 'kids' again; kids' point appears at (−1, 0); cats' point fades to ghost → score chip 3 → −1 beside the first column; chase's heat-map row re-shades to [0.13 0.6 0.13 0.13] → the terracotta dot slides to (0.93, 1.06), onto the HOOK's second ghost landing

## B19 · LEARN 1 · B19_OrderBlind

*59 words · 18.9 s*

Here's what attention can't do on its own. Reorder the sentence: dogs chase small cats. The heat map's rows and columns swap places, and every word lands on exactly the same point. Attention alone can't tell who chased whom. The original transformer fixes this by adding a position signal to each word's numbers. With it, cats lands somewhere new.

*On screen:* 'cats' and 'dogs' swap places in the sentence: 'dogs chase small cats' → the heat map's first and last rows and columns physically swap (cells travel, values unchanged) → output dots stay put; terracotta box on cats' dot at (1.11, 1.02) on 'exactly the same point' → a small dim '+ position' chip slides into each embedding row → cats' dot jumps (moved 1.1); dim caption 'positional encoding — not taught here'

## BVDT · VERDICT · ClaudeVerdictArtifact

*79 words · 21.9 s*

Let's recap with Claude. Every word gets a query, a key and a value, from three learned grids. A query against a key, by dot product, scores how well two words match. Divide by root d k and softmax each row, and you have the heat map. Each word's output is a weighted average of every value. Weigh them all equally and every word means the same. And attention alone can't see order, so position has to be added.

*On screen:* artifact page opens on cream → heading types → six verdict lines land in narration order

## BHTF · YOUR TURN · ClaudeComposerAsk

*117 words · 34.1 s*

Your turn. Paste this into Claude: Write a short Python script, numpy only, for one attention head on a three-word sentence. Use small integer queries, keys and values that you choose. Before running it, predict which word each word will weight most. Then print the scores, the softmax weights, and the outputs. Finally, reverse the word order, run it again, and explain what changed and what didn't. Here's what to check. Every row of weights should add up to one. The scores should be divided by the square root of the key length. And reversing the words should only reorder the outputs. If Claude says the outputs change, ask it where the position information would come from.

*On screen:* composer opens — 'Your turn.' → the prompt types in full as Liam reads it → runningText 'paste this into Claude…' → three check lines cascade in as each is spoken

## BOUT · OUTRO · ClaudeTitleOutro

*10 words · 4.6 s*

Attention, One Head at a Time. At Nik Bear Brown.

*On screen:* title restates; handle; slug-seeded mascot. Liam reads the title, then 'At Nik Bear Brown'.

**Total: 888 words · 260.7 s (4:20).**
