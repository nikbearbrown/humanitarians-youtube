The Rally Has a Clock: When Is "No Perfect Defense" True in Pong?

An essay about Pong says it has no perfect defense: a few fixed laws, and a game to eleven. This video asks when that sentence is true, and the answer turns out to be one ratio. A defender sees the ball's direction the moment it is hit, so the whole question is whether the paddle can cover half the free height of the field in the time the ball takes to cross it. We build the smallest Pong we can, work the ratio out for a field of 858 by 525 (about 0.27 of the ball's sideways speed), then test it three ways: predict the shot where a perfect defender first loses, and count it with a search that tries every aim. The ball speeds up on every shot, so the crossing shrinks and the rally has a clock inside it. The same form works on a different field, and you get a field of your own to try at the end.

Chapters:
0:00 Shot six: a perfect defender loses
0:14 The claim: no perfect defense
0:27 The smallest Pong
0:47 What the defender knows
1:06 The worst shot
1:22 The line
1:42 Turn the dial: paddle speed
2:01 The clock inside a rally
2:18 Predicted, then found
2:38 The second dial: how far a hit can steer
2:58 The same form on a different field
3:18 Which rule carries the balance
3:39 What this does not claim
3:56 Your turn

Where this started: "Pong: Why the Simplest Game Is the Hardest to Explain", an essay by Seth Brown (Zebonastic, Humanitarians AI Fellow). Two short phrases from it, "no perfect defense" and "a game to eleven", open the film. The rest is our own model and simulation.

What this video claims, and what it does not:

- Every figure is from our own simulation of a simplified Pong, with the settings on screen: field 858 by 525, paddle 60 long, ball starting at 6 per tick and speeding up 5% every shot, paddle speeds 1.0 to 4.0 per tick. Nothing is taken from any real machine.
- The model assumes the defender sees the ball's direction the instant it is hit, that the attacker can aim anywhere (or, in the second test, within a quarter of the ball's sideways speed), and that the defender waits in the middle. There is no spin, no human reaction time and no paddle edge.
- The ratio is (field height minus paddle) divided by (2 times field width): 0.271 for 858 by 525, 0.215 when aim is limited to a quarter, 0.1875 for 1200 by 500 with a paddle of 50, and 0.225 for the closing question (1000 by 500, paddle 50, at the serve).
- Predicted and found agree: the middle paddle (speed 2.0) first loses on the sixth shot and the fast paddle (3.0) on the fourteenth; with narrower aim, on the tenth and nineteenth; on the second field, on the seventh, eighteenth and twenty-seventh at speeds 1.5, 2.5 and 4.0. With a ball that never speeds up, paddles at 2.0 and 3.0 held for all 200 shots tested, and the arithmetic says they always will.
- "Two rules carry the balance" is true of the two settings we tested (paddle speed, how far a hit can steer), not a proof that nothing else matters.
- The picture is our own drawing and simulation. The essay is credited above; no footage, images or marks from any game or company are used.

Narration is a synthetic voice (Kokoro, run locally). Visuals are original code-drawn animations; open-licence fonts only (EB Garamond, Inter).

Humanitarians AI - @HumanitariansAI
Tanmay Kulkarni, in for Humanitarians AI

Tags: pong, game design, game theory, simulation, mathematics of games, why pong works, perfect defense, reaction time, rally, paddle speed, predict then verify, model not machine, explainer, Humanitarians AI
