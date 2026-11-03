Why a Coin Flip Beats This Learning Algorithm

Four squares in a row. The second one swaps your buttons, you can't see which square you're on,
and you can't count your steps. It's a puzzle from Sutton and Barto's textbook, Reinforcement
Learning: An Introduction, and in it a fair coin beats a classic learning algorithm by more than
three and a half times.

This video tries every sensible answer to the puzzle, one at a time, and scores each one on the same
line. The best answer isn't a button, and it isn't even a fair coin. It's a coin biased to press
right 2 − √2 of the time, about 58.6%. Then it asks why the best answer had to be random at all, and
hands you a test you can take to other problems: when the best move is random, give the player more
information. If the randomness disappears, it was covering for what the player couldn't see. If it
survives, look for someone who'd exploit a pattern.

Chapters:
0:00 The puzzle: four squares, one swapped
0:18 Every rule is a coin
0:44 Always right, always left
1:03 A learning algorithm that scores buttons
1:40 A fair coin beats it
1:55 Why the coin wins
2:09 Bias the coin: 2 − √2
2:44 Chapter 13: "something new"
3:01 A learner that finds the number on its own
3:18 Why random at all? Take off the blindfold
3:52 Rock, paper, scissors: when randomness survives
4:19 The blindfold test
4:36 Your case: a goalkeeper at a penalty

Try it: a goalkeeper at a penalty, choosing which way to dive. Does more information make the
randomness vanish, or survive? Tell me in the comments, and name the clue or the watcher. A strong
answer names the missing information, or who would exploit a pattern. "It's random because it's
uncertain" doesn't count.

Run it yourself: the corridor and the rock-paper-scissors experiments are plain Python (standard
library only, seeded, under a second each). Give the blindfolded learner one more clue and watch
the coin disappear.
https://github.com/nikbearbrown/humanitarians-youtube/tree/tanmay-kulkarni/fellows/tanmay-k/2026-10-04-why-a-coin-flip-beats-this-learning-algorithm-stem-video/experiment

Topic source: this video starts from Humanitarians AI's chapter-by-chapter mapping of the book,
"Reinforcement Learning: An Introduction — A Comprehensive Mapping" (February 2026), which singles
out this short-corridor example. It takes that one example and tests it.
https://humanitariansai.substack.com/p/reinforcement-learning-an-introduction

Sources, in order of appearance:

- Richard S. Sutton and Andrew G. Barto, Reinforcement Learning: An Introduction, 2nd edition
  (MIT Press, 2018), free from the authors: http://incompleteideas.net/book/the-book-2nd.html
  - Example 13.1, "Short corridor with switched actions," p. 323; Exercise 13.1, p. 324
  - Chapter 13 opening, p. 321; Section 13.1 (stochastic policies, poker), p. 323
  - Chapter 9 opening (features as partial observability), p. 197
  - Section 17.3, "Observations and State" (a deterministic optimal policy with full state), p. 465
- Our experiments: corridor.py (exact values, Sarsa, REINFORCE, a learner that can see its square;
  30 seeds each) and rps.py (rock-paper-scissors against an adaptive opponent; 30 × 1,000 rounds)

What this video claims, and what it does not:

- −44 and −82 are the book's figures for the two ε-greedy policies (ε = 0.1); it says "less than"
  each. −12 for a fair coin, 2 − √2 exactly, and every learner result are our own calculations and
  runs, labelled that way on screen.
- The book gives the best probability as "about 0.59" and leaves the exact form as an exercise.
  2 − √2 is what that exercise works out to; the video doesn't attribute it to the book.
- "30 of 30 runs" means our learner with our settings (shown on screen). It is not a claim about every
  action-value method under every setting.
- The blindfold test is a rule of thumb, not a theorem. If randomness survives full information, the
  video says to look for someone exploiting a pattern; there can be other reasons.
- The goalkeeper is a question for you. The video makes no claim about how real goalkeepers dive.
- Every chart is drawn from our own data; the book's figures (CC BY-NC-ND) are not reproduced.
  Full sourcing for every claim: FACTCHECK.md, this video's companion file.

Narration is a synthetic voice (Kokoro, run locally). Visuals are original code-drawn animations; no
third-party images, and open-licence fonts only.

Humanitarians AI — @HumanitariansAI
Tanmay Kulkarni, in for Humanitarians AI

Tags: reinforcement learning, Sutton and Barto, Reinforcement Learning An Introduction, policy
gradient, REINFORCE, Sarsa, stochastic policy, partial observability, game theory, rock paper
scissors, machine learning explained, Humanitarians AI
