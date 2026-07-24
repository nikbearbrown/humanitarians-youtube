# PEDAGOGY GATE — claude-on-average

> Fact-check every claim before ElevenLabs spend. No audio until VERDICT: PASS.

## Checklist

### Core thesis
- [x] "You're not querying a database. You're sampling a distribution."
  **Correct.** Autoregressive LLMs generate a probability distribution over the
  next token at each step; the output is drawn from that distribution. This is
  mechanically accurate and well-established.

- [x] "Same prompt, different draw — that's not a bug, that's the definition."
  **Correct at non-zero temperature.** At temperature > 0, sampling is stochastic;
  the same prompt can yield different outputs each run. This is the intended
  behavior, not a defect.

### Next-token prediction claim
- [x] "It predicts the most likely continuation of everything before it — including
  the prompt, the system message, and everything it's already generated."
  **Correct.** Autoregressive transformers condition on the full preceding context
  window. This is standard mechanistic description, no controversy.

### Temperature-zero claim
- [x] "Temperature zero makes the most probable token always win. But probable is
  conditioned on everything in the context — the prompt, the system message, the
  persona. Add a different persona and you shift what's most probable, even at
  temperature zero."
  **Correct.** At temp=0, greedy decoding picks argmax over the logits. But the
  logits are a function of the full context, so changing any part of the context
  (including the system prompt/persona) changes the probability distribution and
  therefore can change the argmax output. The claim does NOT say temp=0 is
  non-deterministic — it says steering ≠ specifying, which is accurate.

- [x] "Steering the distribution is not the same as specifying an output."
  **Correct and important.** A persona biases the conditional distribution; it
  does not hard-code a particular token sequence. This is the key pedagogical
  distinction tying back to E8 (Steered).

### Variance / creativity claim
- [x] "The variance is the creativity. The tails of the distribution are where the
  interesting answers live."
  **Defensible and standard framing.** Higher temperature (or nucleus sampling)
  produces more varied, sometimes more creative outputs. Framing variance as a
  feature rather than a bug is accurate for creative tasks. No overclaiming.

### One-draw / gate claim
- [x] "One draw is not the answer. One draw is a sample."
  **Correct.** A single stochastic draw cannot be taken as the authoritative
  answer for high-stakes decisions. Standard argument for ensemble/multi-sample
  approaches or deterministic verification (gates, scripts).

- [x] "Scripts pin the exact. Skills bias the draw. Gates catch the bad draws."
  **Correct summary of the series thesis.** Each claim has been established in
  prior episodes (E6 for scripts, E5 for skills, E9 for gates). Recapping here
  as consequences of the distribution framing is accurate.

### What we're NOT claiming
- No benchmark comparisons.
- No "understanding" / sentience / consciousness claims.
- No model-specific temperature defaults or API details.
- No claim that temp=0 is always non-deterministic (we say it doesn't SPECIFY,
  not that it doesn't repeat).

## Caution items addressed
The roadmap flagged this as "most likely to attract pedants." Main risk: the
temp=0 claim. The narration was revised to say "most probable token wins — but
probable shifts with context" rather than "temp-0 isn't deterministic." This
is factually precise and avoids the common misread.

VERDICT: PASS
