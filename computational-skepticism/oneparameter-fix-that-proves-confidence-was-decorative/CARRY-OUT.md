# Carry-Out

## The Carry-Out Sentence
"If dividing by one learned number fixes the probabilities without altering a single decision, the original confidence was decorative all along."

## Wrong Guess Defeated
"A neural network's extreme confidence score is an inseparable measure of its classification strength that cannot be altered without changing its decisions."

## Falsifying Case
Temperature scaling divides logits by a single scalar T before the softmax function. Because division by a positive constant is strictly monotonic, it preserves the exact ranking and top-one decision across every case, while spreading the probability distribution to match empirical accuracy. This proves that confidence and correctness were completely separable all along.
