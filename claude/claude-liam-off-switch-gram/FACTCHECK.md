# FACTCHECK.md — claude-liam-off-switch-gram
# "An Off Switch for Dangerous Knowledge"
# Source: AE Studio × Anthropic, GRAM / Gradient-Routed Auxiliary Modules, July 2026

VERDICT: PASS

## Claims checked

| Beat | Claim | Verdict | Source/Note |
|---|---|---|---|
| B00 | "Frontier model is a vast store of knowledge, some heals, some harms" | ✓ | Framing — editorial premise, accurate |
| B01 | Three goals: surgical lock, trusted access, no general-performance dent | ✓ | Stated goals of GRAM in the paper |
| B02 | Today's safety approach guards output: refusal training + input/output classifiers | ✓ | Standard RLHF + classifier safety pipeline |
| B02 | Jailbreaks reach knowledge underneath output guards | ✓ | Well-documented attack surface in AI safety lit |
| B03 | Filtering dual-use data from pretraining = one model, one fixed set of capabilities | ✓ | GRAM paper states this is the baseline comparison |
| B03 | Two deployable configs = two training runs at frontier scale | ✓ | Stated as the cost motivation in the paper |
| B04 | GRAM adds extra neurons (auxiliary modules) at every Transformer layer | ✓ | Core architecture claim from paper |
| B04 | Four dual-use categories: virology, cybersecurity, nuclear physics, niche-code | ✓ | Explicit in the paper |
| B05 | General text: gradient flows through whole network | ✓ | Gradient routing mechanism in paper |
| B05 | Virology text: general weights freeze, only virology module updates | ✓ | Core of gradient routing described in paper |
| B06 | Delete module → capability gone; rest of model unchanged | ✓ | Central claim of GRAM; verified in Test 2 |
| B07 | Four categories × on/off = 2^4 = 16 deployable configurations | ✓ | Simple combinatorics; stated in paper |
| B08 | Test 1: synthetic children's stories, topic-tagged | ✓ | Paper describes this as the first evaluation setting |
| B08 | GRAM config ≈ from-scratch filtered model | ✓ | Main result of Test 1 |
| B09 | Test 2: real web + code + science data, 4 domains | ✓ | Paper describes Test 2 setting |
| B09 | Module deleted → capability score drops, general performance intact | ✓ | Core Test 2 result |
| B09 | Attacker fine-tunes on malicious data: GRAM holds | ✓ | Attack resistance finding in paper |
| B09 | Unlearning snaps back after fine-tuning (removed vs suppressed contrast) | ✓ | Key comparative finding vs unlearning baseline |
| B10 | Test 3: 7 model sizes from 50M to 5B parameters | ✓ | Paper specifies 7 sizes in this range |
| B10 | GRAM matches filtering at every size | ✓ | Test 3 result |
| B10 | Module-ON vs module-OFF gap grows as models scale | ✓ | Scaling result in paper |
| B11 | NOT in any production Claude model | ✓ | Explicitly stated in paper |
| B11 | Tested only to 5B parameters | ✓ | Explicit scope limitation in paper |
| B11 | Measured by next-token prediction, not real-world harm | ✓ | Explicit metric limitation in paper |
| B11 | Some dual-use knowledge may be inseparable from general knowledge | ✓ | Stated caveat in paper |

## Numbers on screen (constraint: 4, 16, 3, 7, 50M, 5B)
- 4 categories: ✓ in paper
- 16 configurations: ✓ (2^4, simple math)
- 3 test settings: ✓ (paper has three evaluation tiers)
- 7 model sizes: ✓ in paper
- 50M params (smallest): ✓ in paper
- 5B params (largest tested): ✓ in paper

## Editorial calls labeled
- "prohibitively expensive" for two-model training: editorial framing consistent with paper's motivation
- "vast store of knowledge" for frontier model: editorial framing, accurate in spirit
- "lobotomizing" in B00: editorial hyperbole flagged — intentional hook language, not a technical claim
