Every part of a neural net is simple arithmetic, and nobody writes its weights. Part 1 of a look inside the black box.

This week's second video is a general one, in two parts. It follows Stephen Wolfram's 2023 explainer "What Is ChatGPT Doing … and Why Does It Work?", using his own figures. Part 1 is how a net gets its numbers.

The parts. A neural net is layers of artificial neurons. Each one multiplies its inputs by weights, adds a constant and applies a simple function: y = f(w·x + b). In Wolfram's examples f is ReLU, max(0, z), which turns negative numbers into zero. With weights of 0.5 and −0.8, both inputs 1 and a constant of 0.1, the sum is −0.2, so the neuron outputs 0. Write out everything even a tiny net computes and you get one tangled formula. ChatGPT, he writes, is a formula like that "with billions of terms".

The weights. Nobody types them in. Training shows the net examples, measures how far off its answers are, and nudges every weight downhill on that error, "like water flowing down a mountain", until it settles in some "mountain lake" that may not be the lowest. Even Wolfram's toy net needed millions of examples to learn one simple shape. Train it twice and you can get nets that agree on every example and disagree beyond them. Which one is right? Wolfram's answer: "There's really no way to say."

The run, on one laptop. We tested that claim with ten small nets (1-32-32-1, ReLU), trained on the same 400 examples of a step shape on [−1, 1], each from a different random start:

- All ten fit: the worst training error (mean squared) was 0.0022.
- Asked about x = 3, outside the data, their answers ran from −0.43 to 2.84.

Same data, same fit, no agreement on the guess. All ten seeds are reported; none were dropped.

Part 2 opens trained nets up: a vision net's layers, and every one of GPT-2's 124,439,808 weights.

Try it yourself: ask an assistant for a short script that trains two tiny neural nets on the same points with different random seeds. Plot both past the edge of your data. Then ask the hard question: where they disagree, which one would you trust, and how would you find out?

Chapters:
0:00 What's inside ChatGPT? Part 1
0:14 The parts are simple
0:32 One neuron: f(w·x + b)
0:50 Nobody writes the weights
1:11 Two nets, same data: which is right?
1:28 Ten nets, trained on this Mac
1:46 Verdict
2:01 Your turn: train two nets yourself
2:15 Outro

Source:
Stephen Wolfram, "What Is ChatGPT Doing … and Why Does It Work?" (Feb 14, 2023) — https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/

Figures (all by Stephen Wolfram, from the essay above, © Stephen Wolfram, LLC, CC BY-NC-SA 4.0 — https://creativecommons.org/licenses/by-nc-sa/4.0/):
A small net with its weights — https://content.wolfram.com/sites/43/2023/02/sw021423img46.png
Activation functions (ReLU, Tanh, Sigmoid, Mish, Swish) — https://content.wolfram.com/sites/43/2023/02/sw021423img48.png
The small net written out as one formula — https://content.wolfram.com/sites/43/2023/02/sw021423img49.png
Gradient descent on a loss surface — https://content.wolfram.com/sites/43/2023/02/sw021423img71.png
Training with 10,000 to 10,000,000 examples — https://content.wolfram.com/sites/43/2023/02/sw021423img62.png
Four equally good nets, different guesses beyond the data — https://content.wolfram.com/sites/43/2023/02/sw021423img73.png

License of this video: because it adapts CC BY-NC-SA 4.0 material, this video is released under CC BY-NC-SA 4.0 and is not monetized.

Hosted by Sai. Voice: Kokoro am_onyx, free and local, no account. AI-generated narration. Motion graphics were built with Remotion, and the equation was typeset locally as outlined SVG. The ten-net test is a constructed task, run with NumPy 1.24.4 on a MacBook Pro (M2 Pro): ten seeds, Adam, 4,000 steps each, all reported. The neuron's example values are constructed. "ChatGPT" in the essay means its 2023 model. Wolfram's figures are shown whole and scaled on a cream background; nothing was redrawn or generated. No human-performed audio or video in this production.

Humanitarians AI: https://humanitarians.ai
Musinique: https://musinique.com
Medhavy AI: https://medhavy.com

TAGS: Stephen Wolfram, What Is ChatGPT Doing, ChatGPT, neural networks, neural network explained, black box, how neural networks learn, gradient descent, loss landscape, training a neural net, ReLU, activation function, extrapolation, NumPy, AI explained, Humanitarians AI, Computational Skepticism, weekly

#AI #ChatGPT #NeuralNetworks #StephenWolfram #MachineLearning #AIExplained #HumanitariansAI #ComputationalSkepticism
