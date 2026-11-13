# FACTCHECK — Same Prompt, Different Answer

Every claim with its verdict. Rows citing the script are reproducible by running
`sampling_evidence.py`, which ships here.

| # | Beat | Claim as made | Verdict | Source |
|---|---|---|---|---|
| 1 | B01 | The model produces a probability for every next word; something then draws one | **VERIFIED** | Definition of softmax decoding |
| 2 | B01 | Temperature does not add randomness, it decides how peaked the distribution is | **VERIFIED** | Script: temperature divides the logits before the softmax. The sampling step is unchanged |
| 3 | B02 | Top token takes 46.5% at T=1.0 | **VERIFIED** | Script, from the stated logits |
| 4 | B02 | "Better than half the time you get something that is not *the*" | **VERIFIED** | 100 − 46.5 = 53.5% |
| 5 | B03 | At T=0.2 the top word takes 95.1% and the rest flatten | **VERIFIED** | Script. Third candidate is already at 0.1%, the rest round to 0.0% |
| 6 | B03 | Both shapes are drawn on the same scale | **VERIFIED** | Both normalised by the T=0.2 maximum; the script prints both normalised arrays |
| 7 | B04 | Chance all tokens take the top choice: 95% at 1 token, 60.5% at 10, 8.1% at 50, 0.004% at 200 | **VERIFIED** | Script, 0.951^n. Series printed for exactly the lengths plotted |
| 8 | B04 | 200 tokens is 1 in 22,991 | **VERIFIED** | 1 / 0.951^200 |
| 9 | B05 | The same 1000 float32 numbers summed two ways give −48028.30078125 and −48028.27343750 | **VERIFIED** | Script, fixed seed. Reproducible on any IEEE-754 machine |
| 10 | B05 | Floating point addition is not associative, so order changes the result | **VERIFIED** | IEEE 754. Demonstrated directly by row 9 |
| 11 | B06 | Non-associativity alone does not make a model nondeterministic | **VERIFIED** | A fixed operation sequence on fixed inputs is deterministic. This is the correction described in `SOURCES.md` |
| 12 | B06 | Dynamic batching changes the reduction order | **VERIFIED VERBATIM** | SGLang docs, quoted on the card |
| 13 | B06 | Temperature 0 does not guarantee identical output | **VERIFIED VERBATIM** | SGLang docs: "Even with temperature=0, standard LLM inference can produce different outputs due to dynamic batching" |

## Claims considered and cut

| Claim | Why it was cut |
|---|---|
| "Temperature 0 isn't deterministic because floating point isn't associative" | **Wrong, and it was the original framing.** Non-associativity is the mechanism, not the cause. The cause is batching changing the order. Corrected before authoring |
| A divergence rate for a named model | Single secondary report on a system we have not run |
| "Argmax flips X% of the time" | Measured on a near-tie we constructed by hand. Not a property of real decoding |
| A throughput cost for deterministic inference | One benchmark, not reproduced here |
| That these logits are a real model's | They are illustrative and the reel says so |

## Note on the illustrative logits

The seven candidates and their scores are invented for the demonstration, which
is stated in the narration ("this is one position in one answer") and in the
script's own comments. Everything derived from them — 46.5%, 95.1%, 1 in 22,991
— is computed, not asserted. No claim is made that any particular model assigns
these probabilities. The float32 demonstration uses no logits at all and is
reproducible on any machine.
