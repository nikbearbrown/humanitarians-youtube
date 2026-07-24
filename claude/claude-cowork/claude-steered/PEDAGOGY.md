# PEDAGOGY GATE — claude-steered

> Fact-check every claim before ElevenLabs spend. No audio until VERDICT: PASS.

## Checklist

### Core thesis
- [x] "You can't name the output. You can load the dice."
  **Correct.** Conditioning text (system prompts, personas, registers) shifts the
  probability distribution but does not hard-code a specific token sequence. This
  is mechanically accurate — stochastic sampling always remains stochastic.

### Three-layer stack claim
- [x] "Method persona = WHAT. Register = HOW. Brand = WHOSE."
  **Correct framing.** These are distinct conditioning layers that independently
  bias different aspects of generation. System prompts function as
  context-window conditioning text — the model processes them before the user
  turn, shifting priors. Splitting by purpose (structural role, tonal role,
  identity role) is a valid pedagogical decomposition.

- [x] "Each layer narrows the distribution."
  **Correct.** Each additional conditioning token conditions the joint distribution
  further. More conditioning context → more constrained output distribution.
  This is a well-established principle of conditional language modeling.

### Stacking limit claim
- [x] "Steering is not specifying. The draw is still a draw."
  **Correct.** Even fully conditioned LLMs at non-zero temperature produce
  stochastic outputs. At temperature zero, the draw can be deterministic for a
  fixed context — but the *identity* of the output (which token sequence) is
  not named by the conditioning; it is derived from the model's learned
  distributions. This is consistent with E7's thesis and is the explicit
  callback to that episode.

### One pipeline claim
- [x] "One pipeline, four channels. The brand key is the only diff."
  **Verifiable in this repo.** CLAUDE-BRAND.md lists four brand variants
  (claude, claude-hai, claude-medhavy, claude-musinique). The `brand_variant.py`
  script is the mechanism. This is a real, observable fact in the codebase —
  not a hypothetical claim.

### Register-as-parameter claim
- [x] "A register is a parameter, not a person."
  **Correct and important.** Medhavy, HAI, etc. are conditioning configurations,
  not separate models or authors. The underlying model is identical; the
  conditioning differs. Framing this as a "parameter" is mechanically accurate
  and pedagogically sharp.

### What we're NOT claiming
- No claim that personas fully control output — the narrowing is probabilistic.
- No claim about model identity or "understanding" the persona.
- No claim that temperature zero eliminates variance entirely (consistent with E7).

VERDICT: PASS
