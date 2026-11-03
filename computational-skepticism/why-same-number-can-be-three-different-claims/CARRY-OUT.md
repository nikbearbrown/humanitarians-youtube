# Carry-Out

## The Carry-Out Sentence
"Every claim-verb has an evidence price — you can only spend the verb your validation actually paid for."

## Wrong Guess Defeated
"The benchmark number itself dictates how strong a claim you can make — an 87% score means the same thing whether you write 'observe', 'find', or 'conclude'."

## Falsifying Case
Three engineers review the exact same single benchmark run where a model scores 87% accuracy on a held-out test split.
- Engineer A writes: "We observe 87% accuracy under these specific test conditions."
- Engineer B writes: "We find 87% accuracy across runs."
- Engineer C writes: "We conclude the model achieves 87% accuracy and is ready for production."

The evidence in hand is a single evaluation run on a single dataset. That evidence pays the evidentiary cost for *observe* (a clean measurement with procedure and conditions stated). It does not pay for *find* (which requires replication across variation or random seeds), and it is nowhere near paying for *conclude* (which requires alternatives ruled out, subgroup checks, and sensitivity analysis). Engineer A is telling the truth; Engineers B and C are spending unearned epistemic credit.
