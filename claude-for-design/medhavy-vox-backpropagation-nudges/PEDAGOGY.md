# PEDAGOGY — medhavy-vox-backpropagation-nudges

## Learner Profile
Learner knows: what a neural network weight is, what training loss is

## Teaching Goals
Teaches:
- Desired nudges from output error (2-neuron up, 5-neuron down)
- Upstream brightness determines update magnitude
- Backward propagation layer by layer
- ∂C/∂w as the sensitivity score for each weight
- Averaging ∂C/∂w across training examples gives the gradient update

## Gate Numbers
- 13,000 weights example ✓
- ∂C/∂w for each weight ✓
- Upstream activation determines update magnitude ✓
- Chain of desired nudges from output to input ✓

## Exclusions Honored
- No chain rule calculus
- No mini-batch SGD detail
- No vanishing gradient

## Color Semantics Check
- TEAL (desired nudges / backward propagation / correct direction): correctly applied ✓
- CRIMSON (wrong output / error / what needs to change): correctly applied ✓

## Beat Structure Check
- B00: MedhavyOpen with exact narration_text ✓
- B01–B10: 10 content beats with t_start and estimated_duration_s ✓
- B11: MedhavyOutro with exact narration_text ✓
- B03: CARD kind:question ✓
- B10: CARD kind:endcard ✓
- Graphic beats use ["#009E73"] or ["#009E73","#D55E00"] ✓

VERDICT: PASS
