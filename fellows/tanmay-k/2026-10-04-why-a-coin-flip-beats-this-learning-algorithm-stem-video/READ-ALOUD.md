# READ-ALOUD: Gate P sheet

*Why a Coin Flip Beats This Learning Algorithm* (working title) · structure: THE CORRIDOR (one answer per chapter) · voice `am_onyx`

Generated from `beat_sheet.json` by `make_read_sheet.py`. If the narration changes, this sheet is
regenerated and the read starts again.

**How to run Gate P:** read each beat out loud at speaking pace, top to bottom, in one sitting.
Listen for rhythm, emphasis, and whether each turn lands. Tick the box or write a note. Also skim
the *on screen* line under each beat: card text is checked too (PLAYBOOK §1). Then reply
**"Gate P PASS"** (with any notes) or list the beats that tripped you.

**No slates yet.** `Corridor` and `CoinCurve` aren't built, so this is a read-aloud Gate P.
Each beat's visual is reviewed as rendered stills at the next stage, before any audio.

## Mechanical pass (`gate_p_lint.py`), already clean

- 0 long sentences, 0 dropped units, 0 symbols or markup in narration.
- 4 ECHO flags, all deliberate parallels (below). 8 NAME flags moved to the ear checklist.
- 1 HOMOPHONE watch: "mint".

| Beat | Parallel | Why it stays |
|---|---|---|
| B03 | "Square one… Square two" | walking rhythm, one sentence per step |
| B09 | "At one end… At the other" | the two ends of the line |
| B13 | "Methods that score… Methods that learn" | the book's contrast, kept parallel |
| B16 | "If it disappears… If it survives" | the test's two outcomes; the parallel *is* the rubric |

## Changed since your Gate P PASS: caught by Whisper on the generated audio (2026-10-01)

Whisper transcribed what Kokoro actually said. Three phrases are heard as different words, so
only these lines changed. Every other line is word-for-word what you signed.

| Beat | Heard as | Was | Now |
|---|---|---|---|
| B02 | "a coin, **waited** to…" | It's a coin, weighted to one exact number. | It's a **biased** coin, **set** to one exact number. |
| B06 | "the book's number **two**" | That's the book's number too. | The book reports the same number. |
| B09 | "let's **wait** the coin", "every **waiting**" | So let's weight the coin. / every weighting in between / The best weighting is a little toward right. | So let's **bias** the coin. / every **setting** in between / The best **setting leans** a little toward right. |
| B11 | "the coin's **waiting**" | the coin's weighting directly | the coin's **bias** directly |
| S04 | "**waited** to land right **to** minus root two" | Weight it to land right two minus root two of the time, about fifty-eight point six percent. | **Bias** it to land right **about fifty-eight point six percent of the time: two minus root two, exactly.** |

Re-generated and re-checked: Whisper now hears all five as written. The outro card keeps "The best
move was a weighted coin": it's printed, not spoken. `gate_p_lint.py` now flags weight / weighting /
weighted / too, so this can't come back.


## Say-it-right checklist (Kokoro's own phonemes, checked; confirm by ear)

| Word | Should sound like | Kokoro | Where |
|---|---|---|---|
| Sutton and Barto | SUT-n and BAR-toe | `sˈʌʔn ænd bˈɑːɹɾoʊ` | B02 |
| Sarsa | SAR-suh | `sˈɑːɹsə` | B05, B11, B14 |
| REINFORCE | like the word "reinforce" | `ɹˌiːɪnfˈɔːɹs` | B12 |
| two minus the square root of two | as written | `tˈuː mˈaɪnəs ðə skwˈɛɹ ɹˈuːt ʌv tˈuː` | B10 |
| two minus root two | as written | `tˈuː mˈaɪnəs ɹˈuːt tˈuː` | B12, B18 |
| fifty-eight point six percent | as written | `fˈɪftiˈeɪt pˈɔɪnt sˈɪks pɚsˈɛnt` | B10, B12 |
| minus eleven point six six | as written | `mˈaɪnəs ᵻlˈɛvən pˈɔɪnt sˈɪks sˈɪks` | B10 |
| irrational | ih-RASH-uh-nul | `ɪɹˈæʃənəl` | B10 |
| mint (exactly) | must not be heard as "meant" | `mˈɪnt ɛɡzˈæktli` | B10 |
| Kulkarni | kul-KAR-nee | `kˈʌlkɑːɹni` | B02, B18 |

## Where to listen hardest

- **B01**: the puzzle has to sound like a real question to the viewer, not a setup line
- **B07**: **the turn.** "Minus twelve." needs its own beat of surprise, and "almost insulting" should sound wry, not scripted
- **B08**: the cool-down after the peak (PLAYBOOK §1a): careful, not deflated
- **B10**: quiet wonder at "irrational" and "mint", without overselling
- **B14**: stillness: "The coin was covering for what it couldn't see" is the film's thesis line
- **B16**: confident and plain. This is the rubric; it must be easy to remember on one hearing
- **B17**: inviting, not a lecture. The weak-answer line should sound friendly

## The script

### [0:00] B01 · THE PUZZLE  _(tone: curious, playful)_

Here's a puzzle from a textbook. Four squares in a row. Start on the left, reach the goal on the right, and every step costs a point. Two buttons, left and right. Easy. Except in the second square, the buttons are swapped. And you're blindfolded. Every square gives you the same reading, and you can't keep count of your steps. So whatever you do in one square, you do in all three. Which button do you press?

<sub>**On screen:** Four squares. One is swapped. · Same reading in every square. No counting steps. · Sutton & Barto, Reinforcement Learning: An Introduction, 2nd ed. (2018), Example 13.1, p. 323 · Ch. 9 opening, p. 197</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [0:23] B02 · THE PLAN  _(tone: warm, clear)_

Hi, this is Tanmay Kulkarni, in for Humanitarians AI. This video is about one example from Sutton and Barto's Reinforcement Learning: An Introduction, a textbook about machines that learn by trial and error. Here's the key to the puzzle. Any rule you could pick is really a coin: how often it presses right, from never to always. So every answer gets a spot on this line, and a score. We'll try them one at a time. By the end you'll know the best answer. It isn't a button. It's a biased coin, set to one exact number.

<sub>**On screen:** Every rule is a coin · Any rule for this corridor = one chance of pressing right. Each answer gets a spot and a score. · Sutton & Barto, Reinforcement Learning: An Introduction, 2nd ed. (2018), Example 13.1, p. 323</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [0:52] B03 · ALWAYS RIGHT  _(tone: brisk)_

First answer: always press right. Square one, right, you move to square two. Square two, right. But it's swapped, so you slide back to square one. Right. Square two. Back again. You never reach the goal. Your score doesn't just get bad. It never stops counting.

<sub>**On screen:** Rule: always right · Never reaches the goal. · From the rules of Example 13.1 · marker: always right: never finishes</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:06] B04 · ALWAYS LEFT  _(tone: dry)_

Always press left? In the first square, left walks you into the wall. You stand there. Forever.

<sub>**On screen:** Rule: always left · Never leaves square one. · From the rules of Example 13.1 · marker: always right: never finishes · marker: always left: never finishes</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:11] B05 · THE BUTTON LEARNER  _(tone: explanatory)_

So no fixed button works. Let's give the problem to a learning algorithm, a classic from the earlier chapters of the book, called Sarsa. It learns a score for each button from experience. Just one score per button, since every square reads the same. Then it mostly presses the higher one. One time in ten it presses a random button, just to keep exploring. That's what gets it out of the loops. I ran it thirty times. All thirty settled on the same thing. Mostly right.

<sub>**On screen:** Sarsa · ε = 0.1 · 30 runs · Where the button learner settled · Scores each button, presses the higher one 95% of the time · 30 of 30 runs: mostly right · 0 of 30 runs: mostly left · Our runs: experiment/corridor.py, 30 seeds (ε = 0.1, α = 0.01, 1,000 episodes)</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:37] B06 · MINUS FORTY-FOUR  _(tone: deflated)_

And mostly right is worth about minus forty-four. The book reports the same number. The only other place this learner can land, mostly left, is worse: about minus eighty-two. Those are its two options. It's built to find a best button, and in this corridor there isn't one.

<sub>**On screen:** Where a button learner can land · ε-greedy can only be mostly right or mostly left. · Sutton & Barto, Reinforcement Learning: An Introduction, 2nd ed. (2018), Example 13.1, p. 323 · values: Exact value, our calculation (experiment/corridor.py) · marker: mostly right ≈ −44 · marker: mostly left ≈ −82</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:52] B07 · THE COIN  _(tone: surprised)_

Then I tried something that felt almost insulting. No learning at all. Flip a fair coin every step. Heads, right. Tails, left. Minus twelve. A coin beat the learning algorithm by more than three and a half times. And that's not a lucky run. It's the exact value.

<sub>**On screen:** Rule: flip a fair coin · Fair coin: −12.00 (exact) · learner: −44.21 · Exact value, our calculation (experiment/corridor.py) · walk shown: one seeded sample · marker: never finishes · marker: never finishes · marker: −44 · marker: −82 · marker: fair coin −12</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [2:06] B08 · WHY THE COIN WINS  _(tone: pulling back, careful)_

Now, the coin isn't clever. It wins for a plain reason. The swapped square punishes commitment. Lean hard on either button and you pay for it, bouncing or stuck. The coin doesn't commit at all. Which raises a question. Is fifty-fifty actually the best you can do?

<sub>**On screen:** Commit hard, and you pay for it · Is 50% the best setting? · Exact value, our calculation (experiment/corridor.py) · marker: mostly right −44 · marker: mostly left −82 · marker: fair coin −12</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [2:21] B09 · WEIGHT THE COIN  _(tone: curious, building)_

So let's bias the coin. At one end it never says right. At the other, it always does. And here's the score for every setting in between. Both ends never finish. The learner's two options sit way down here. The fair coin is near the top. But it isn't the top. The best setting leans a little toward right.

<sub>**On screen:** Every setting of the coin · The best setting is not 50%. · Exact value, our calculation (experiment/corridor.py) · marker: mostly left · marker: mostly right · marker: fair coin</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [2:39] B10 · TWO MINUS ROOT TWO  _(tone: quiet wonder)_

The best setting works out to two minus the square root of two. About fifty-eight point six percent right, for a score of minus eleven point six six. The book rounds it to fifty-nine percent and leaves the exact form as an exercise for the reader. And that exact form is irrational. The best way through this corridor is a coin no one could ever mint exactly.

<sub>**On screen:** The best setting · The book: “about 0.59”, “about −11.6”. The exact form is left as Exercise 13.1. · Sutton & Barto, Reinforcement Learning: An Introduction, 2nd ed. (2018), Example 13.1, p. 323 · exact form: Exercise 13.1, p. 324 · marker: fair coin −12 · marker: best: 58.6% → −11.66</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [2:59] B11 · SOMETHING NEW  _(tone: explanatory, satisfying)_

And this is what the book is really getting at. Almost everything before chapter thirteen learns the way Sarsa did, by scoring actions. Chapter thirteen opens with, quote, in this chapter we consider something new. Learners that don't score buttons at all. They learn the coin's bias directly, shifting the odds toward whatever the runs reward.

<sub>**On screen:** Chapter 13 · Policy Gradient Methods · “In this chapter we consider something new.” · Before: score each action, then pick the best (almost all methods) · Chapter 13: learn the probabilities directly · Sutton & Barto (2018), p. 321. One earlier exception: gradient bandits, Sec. 2.8</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [3:16] B12 · THE COIN LEARNER  _(tone: building to payoff)_

The simplest one is called REINFORCE. I started it at the worst setting I had, mostly left, minus eighty-two. Within four hundred episodes it was averaging about minus thirteen. Across thirty runs, the average setting it settled on was fifty-eight point six percent. It found two minus root two on its own.

<sub>**On screen:** REINFORCE, started at mostly left · Runs ranged 53%–65%; the average landed on the best setting. · Our runs: experiment/corridor.py, 30 seeds (α = 2⁻¹², 2,000 episodes) · marker: start: −82 · marker: average 58.6% → −11.70</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [3:32] B13 · WHY IT SITS HERE  _(tone: reflective)_

The book says it plainly. Methods that score actions have no natural way of finding the best random policy. Methods that learn the probabilities can. But that leaves a fair question. Why did the best answer have to be random at all?

<sub>**On screen:** Section 13.1 · Why learn probabilities? · Action-value methods: no natural way to find stochastic optimal policies · Policy methods can, as Example 13.1 shows · Sutton & Barto (2018), Sec. 13.1, p. 323 (paraphrased)</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [3:44] B14 · TAKE OFF THE BLINDFOLD  _(tone: still, honest)_

Here's how to find out. Take off the blindfold. Same Sarsa learner as before, but now it keeps a separate score for each square. Thirty runs out of thirty, it learned right, left, right. Three steps. Minus three. Nearly four times better than the best coin. And the book says that's no accident. When the player knows exactly where it is, there's always a fixed rule that's best. The coin was covering for what it couldn't see.

<sub>**On screen:** Same learner, one score per square · 30 of 30 runs: right, left, right → −3 (best coin −11.66). Book: with full state, a deterministic optimal policy always exists. · Our runs: experiment/corridor.py, 30 seeds (sarsa_sees_state) · Sutton & Barto (2018), Sec. 17.3, p. 465</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [4:08] B15 · THE OTHER OUTCOME  _(tone: curious, then firm)_

But randomness doesn't always disappear. The book's own example is poker, where the best play is often to bluff with a specific probability. Here's a simpler one I ran. Rock, paper, scissors, against an opponent that learns your habits. Nothing is hidden. Always rock lost essentially every round. Leaning toward rock still came out behind. The even three-way split broke even. Now swap in an opponent that just plays at random, and always rock does as well as anything. That randomness is there because someone is watching for a pattern.

<sub>**On screen:** Rock, paper, scissors · 30 runs × 1,000 rounds · Against an opponent that learns your habits · Always rock: −0.999 per round (lost essentially every round) · Lean rock 50/30/20: −0.29 per round · Even 1/3 each: ≈ 0 (broke even) · Opponent that plays at random: all three ≈ 0 · Our runs: experiment/rps.py · Poker: Sutton & Barto (2018), Sec. 13.1, p. 323</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [4:35] B16 · THE BLINDFOLD TEST  _(tone: clear, confident)_

So that's the test, and you can carry it to other problems. When the best move is random, give the player more information. If the randomness disappears, it was covering for what the player couldn't see. If it survives, look for someone who'd exploit a pattern. The corridor is the first kind. Rock, paper, scissors is the second.

<sub>**On screen:** The blindfold test · When the best move is random, give the player more information. · Randomness disappears → it was covering for what the player couldn't see (corridor: −11.66 → −3) · Randomness survives → someone would exploit a pattern (rock-paper-scissors: always rock −0.999 / round) · Corridor: experiment/corridor.py · RPS: experiment/rps.py · Sutton & Barto (2018), Sec. 17.3</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [4:53] B17 · THE GOALKEEPER  _(tone: direct, inviting)_

Now try it on a goalkeeper facing a penalty, choosing which way to dive. Run the test. Does more information make the randomness disappear, or does it survive? Put your answer in the comments. A strong answer names the missing information, or the person who'd exploit the pattern. Saying it's random because it's uncertain doesn't count. And if you code, the corridor script is linked below. Run it, and watch the blindfold come off.

<sub>**On screen:** Run the blindfold test: a goalkeeper at a penalty · Does more information remove the randomness? · Strong answer: names the missing information, or who would exploit a pattern · Weak answer: “it's random because it's uncertain” · Code: experiment/corridor.py · stdlib Python · runs in under a second · Answer in the comments</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [5:15] B18 · OUTRO  _(tone: warm)_

Two minus root two. Tanmay Kulkarni, in for Humanitarians AI, signing off.

<sub>**On screen:** The best move was a weighted coin. · Tanmay Kulkarni, in for Humanitarians AI</sub>

> ☐ reads cleanly   ☐ note: ______________________

_18 beats · 1053 words · estimated runtime 5:19 at 3.3 words/s. Kokoro audio becomes the master clock once generated._

---

## The Short (its own script, its own Gate P)

Portrait, one arc, its own ending. It reuses the same corridor, never long-form beats. Read it
separately: it has to work for someone who never sees the long film. Generated from
`short/beat_sheet.json`.

**Rewritten since your Gate P PASS (2026-10-01).** It now carries one question (why does a coin win?),
the full film's blindfold test with both outcomes (S05), and your name at both ends (S01, S07), as in
the W24 Short. You signed it on 2026-10-01; since then only S04 changed (see the table above).

### S01 · THE HOOK

Hi, this is Tanmay Kulkarni, in for Humanitarians AI. In this puzzle, a coin flip beats a learning algorithm by more than three and a half times. Here's why, and what it says about randomness.

> ☐ reads cleanly   ☐ note: ______________________

### S02 · THE PUZZLE

It's from Sutton and Barto's reinforcement learning textbook. Four squares. The second one swaps your buttons. You can't see which square you're on, and you can't count your steps. So whatever you press, you press everywhere.

> ☐ reads cleanly   ☐ note: ______________________

### S03 · WHY THE LEARNER FAILS

A learning algorithm that hunts for the best button settles on mostly right, and bounces off that swapped square for about forty-four steps. There is no best button here.

> ☐ reads cleanly   ☐ note: ______________________

### S04 · THE WEIGHTED COIN

A fair coin gets there in about twelve steps. And the best coin isn't even fair. Bias it to land right about fifty-eight point six percent of the time: two minus root two, exactly. That's what chapter thirteen of the book is about: learners that tune the coin itself, and find that number on their own.

> ☐ reads cleanly   ☐ note: ______________________

### S05 · THE TEST

So why random? Give the player more information and find out. Let it see where it is, and the coin vanishes: right, left, right, three steps. But in rock, paper, scissors, against an opponent who learns your habits, the coin survives. Lean on rock, and you get punished.

> ☐ reads cleanly   ☐ note: ______________________

### S06 · THE TASK

Next time the best move is random, ask what the player can't see, or who's watching. Try it on a goalkeeper at a penalty, choosing which way to dive. Does more information make the randomness vanish, or survive? Tell me in the comments, and name the clue or the watcher. Saying it's random because it's uncertain doesn't count.

> ☐ reads cleanly   ☐ note: ______________________

### S07 · THE CLOSE

The full video works through it, step by step. Tanmay Kulkarni, in for Humanitarians AI.

> ☐ reads cleanly   ☐ note: ______________________

_277 words · about 84 s at 3.3 words/s, plus the endcard._
