# READ-ALOUD — Where the Eighty Lives (long film, 16:9), draft 3

Narration only, in order, as the voice will say it. Numbers in words. Read it aloud once at your own pace and mark anything that rushes, confuses or trips your tongue. **For your read, not yet the Gate P sign-off.** Draft 3 corrects the figures after FACTCHECK found the first measurement was not like for like (B02, B05, B07, B09); draft 2 was Gate P signed on 2026-11-07 (`READ-ALOUD-v2-signed.md`). The picture-side fixes (the three-panel frame on screen from the start, source lines for the eighty and the memory idea) are in `PROOF-REVIEW.md` and go into the beat sheet. Previous draft: `READ-ALOUD-v1.md`. Every number comes from `MEASUREMENTS.md` (our own compiled runs) or from the first-principles count stated in the film. The "eighty" is the figure from the library film this one grows out of.

**B00 · THE OBSERVATION** (~12 s)

A small model that runs eighty times slower than a bigger one. I read that, and it stuck with me. By its parameter count, the small one should be the fast one. So where does the extra time go? I wanted to find the eighty, and see where it lives.

**B01 · THE SETUP** (~14 s)

I built two tiny models that share the same weights, and I gave them the same job. I'm Tanmay Kulkarni, in for Humanitarians AI. One reads a sequence the way a recurrent model does. The other spreads the same weights across the whole sequence at once. Everything you see comes from my own measurements.

**B02 · ONE STEP** (~19 s)

Start with a single step of the recurrent model. It takes the next input, and it takes its own memory from the step before. It multiplies both by one block of weights, and out comes a new memory. That multiplication is the part we count. About two hundred thousand operations, one for each weight.

**B03 · THE OTHER WAY** (~17 s)

Now the other model. Same block of weights, but the inputs are all known up front, so nothing waits for anything. It applies that block at every position of the sequence. Same weights. Same two hundred thousand operations per position. The only thing that changed is whether a position has to wait for the one before it.

**B04 · MATCHED** (~14 s)

So the arithmetic matches. A hundred positions is twenty million operations on each side. Not roughly. Exactly the same. If time follows arithmetic, these two should take the same time. Let me find out.

**B05 · DIAL AT ZERO** (~18 s)

Here is the dial. It says how much the chip can do at once. I turned it all the way down, plain loops, one thing at a time. The recurrent model took six point one milliseconds. The other took six point four. The same, within five percent. In this test, with nothing to overlap, the eighty is not there.

**B06 · WHAT A CHIP CAN DO** (~21 s)

So what does turning the dial up buy? Mostly one specific thing. Load a weight once, and use it on many positions before putting it down. The second model can do that, because its positions do not depend on each other. The recurrent model cannot. Step two needs the answer from step one, so it fetches the weights again, every single step.

**B07 · TURN IT UP** (~19 s)

I turned the dial up a notch, eight positions per weight load. The gap opened to one point three times. Then I used a proper optimized matrix multiply. Three point seven times. Same weights. Same twenty million operations. The arithmetic never changed. The waiting did.

**B08 · THE OTHER AXIS** (~18 s)

There is a second axis, the length of the sequence. From twenty-five steps to four hundred, sixteen times more steps, and the recurrent time grew sixteen times. Steady, no surprises. The ratio between the two models stayed in the same range. So length makes the loop longer. It is the chip that decides how much the loop costs.

**B09 · WHERE THE EIGHTY LIVES** (~22 s)

Here is what surprised me. Not one number lives in the model. The gap lives between the model and the chip. On my laptop, the most I could make was about four times. On a small chip, where the weights may sit in slow memory and be read again every step, I would expect more room. I have not measured one, so I will not give you a number. But now I know where to look.

**B10 · THREE NUMBERS** (~17 s)

So I have three numbers for a model now. Parameters tell you what it stores. Operations tell you what it computes. And overlap tells you how long it waits. A model can be small, cheap to count, and still do its work in a line.

**B11 · WHAT THIS DOES NOT CLAIM** (~15 s)

One boundary, because I would rather say it than have you find it. This is my laptop, not a microcontroller. A dense recurrent model, one input at a time. My ratios are smaller than eighty, and I make no claim about any particular chip or product. It shows where the time can come from.

**B12 · YOUR TURN** (~24 s)

Your turn. The cost of one step is four times the hidden size, times the hidden size plus the inputs. Take sixty-four hidden units and sixty-four inputs. Thirty-two thousand, seven hundred sixty-eight operations per step, about three point three million over a hundred steps. Now the question to ask of any model: which of its steps have to wait for another one? A recurrent model across time does. One convolution across positions does not. I'm Tanmay Kulkarni, in for Humanitarians AI.

---
13 beats · 728 words · about 208 s at 3.5 words per second (draft 1: 706 words). Estimate only, to be measured on the voice.
