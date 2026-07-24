# SOURCES.md — claude-liam-off-switch-gram
# "An Off Switch for Dangerous Knowledge"
# Built 2026-07-16

## Primary source

**GRAM: Gradient-Routed Auxiliary Modules for Modular Pretraining**
AE Studio × Anthropic, July 2026.
Every factual claim in this reel is drawn from this paper.

On-screen caption (appears on GRAM structure beats): "After Anthropic × AE Studio, GRAM / modular pretraining (2026)"

## On-screen facts and their sources

| Fact | Source |
|---|---|
| Three goals: surgical lock, trusted access, no general-performance dent | GRAM paper, stated goals |
| Today's safety: refusal training + input/output classifiers on OUTPUT side | Standard RLHF/RLAIF pipeline, widely documented |
| Jailbreaks bypass output guards, not removed knowledge | Standard attack surface, AI safety literature |
| Filtering = one fixed set of capabilities; two configs = two training runs | GRAM paper, cost motivation |
| GRAM adds auxiliary neuron groups (modules) at every Transformer layer | GRAM paper, architecture section |
| Four dual-use categories: virology, cybersecurity, nuclear physics, niche-code | GRAM paper, explicit |
| Gradient routing: general text → whole network; virology text → module only | GRAM paper, training procedure |
| Delete module → capability gone; rest of model unchanged | GRAM paper, main claim |
| 4 categories, 2^4 = 16 deployable configurations | GRAM paper + arithmetic |
| Test 1: synthetic children's stories, topic-tagged | GRAM paper, evaluation setting 1 |
| Test 1 result: each GRAM config ≈ from-scratch filtered model | GRAM paper, Test 1 results |
| Test 2: real web + code + science, 4 domains | GRAM paper, evaluation setting 2 |
| Test 2: module deleted → capability score drops, general performance intact | GRAM paper, Test 2 results |
| Test 2: GRAM holds under fine-tuning attack; unlearning restores | GRAM paper, attack resistance finding |
| Test 3: 7 model sizes from 50M to 5B parameters | GRAM paper, evaluation setting 3 |
| Test 3: GRAM matches filtering at every size | GRAM paper, scaling results |
| Test 3: module-ON vs module-OFF gap grows as scale increases | GRAM paper, scaling results |
| Not in any production Claude model | GRAM paper, explicit caveat |
| Tested to 5B parameters; next-token prediction metric | GRAM paper, explicit scope limitation |
| Some knowledge may be inseparable from general knowledge | GRAM paper, explicit caveat |

## Media credits

All visuals: original animated diagrams built with Manim (Community Edition) and Remotion.
No stock footage, no screenshots of any kind.
All figures are clean conceptual diagrams — not reproductions of paper figures.
Voice: Kokoro TTS (af_kore) — free/local.

## Channel and publication

Channel: @HumanitariansAI
Playlist: Claude research
Persona: Kore (in for Humanitarians AI) — Kokoro af_kore, Teardown register
