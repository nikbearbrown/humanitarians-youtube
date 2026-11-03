# Carry-Out

## The Carry-Out Sentence
"Model outputs cost milliseconds and fractions of a cent while verifying them takes scarce human expertise — unverified outputs pile up looking like successes, so systems must be designed so the check a human can afford reveals what matters."

## Wrong Guess Defeated
"Because generating an answer with AI is fast and automated, verifying whether the output is correct and safe will scale just as easily."

## Falsifying Case
In classical computer science and cryptography, checking an answer is dramatically cheaper than finding one (e.g., verifying factors vs factoring). In AI deployment, this asymmetry completely inverts: producing a plausible-looking output takes milliseconds and pennies, but verifying its validity requires scarce domain expertise and deep manual auditing. If verification is not explicitly budgeted and architected for human bandwidth, unverified outputs accumulate into silent systemic failure debt.
