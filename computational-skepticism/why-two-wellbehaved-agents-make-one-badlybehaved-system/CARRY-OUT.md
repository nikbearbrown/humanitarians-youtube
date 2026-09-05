# Carry-Out

## The Carry-Out Sentence
"Downstream agents treat upstream outputs as ground truth, so errors do not add—they compound."

## Wrong Guess Defeated
"If you test each agent in isolation, the combined pipeline error is simply the sum of individual failure rates."

## Falsifying Case
When Agent A errs 2% of the time and Agent B errs 3% of the time, independent addition predicts a ~5% failure rate. In reality, Agent B takes Agent A's output as unquestioned ground truth, generating dependent hallucinations that escalate into a 30% system failure rate.
