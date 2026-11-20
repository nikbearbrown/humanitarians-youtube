# Pedagogy Review

## Topic
The Answer Did Not Move: proving a neural-network compiler's rewrites changed nothing,
on my own compiler and resnet18

## Learning Objective
A tool's report that "nothing changed" is a claim, not a proof. The viewer leaves able
to verify a tool independently: run both versions and compare, and check the checker
against something that does not share its mistakes.

## Audience
General audience with some interest in AI. Layers are described by what they do (shift,
rescale) before any term is used.

## Key Findings Reported
Measured by running github.com/Kenny0bi/fuse on resnet18 exported per its data/export.sh.
- 141 operations become 32: 72 pass-through nodes removed, 20 BatchNorms folded, 17 ReLUs fused.
- Largest difference between original and optimized outputs: 1.19e-06 on outputs up to 4.68;
  same top prediction.
- The repo's runtime against onnxruntime: 2.4e-06, same top prediction.
- Fold algebra on the first Conv/BN pair in double precision: forms agree to 3.6e-15.

## Accuracy Gate
See FACTCHECK.md.

## Restraint Gate
- resnet18 is untrained (weights=None) as in the repo's export; the claim is about the
  rewrite preserving the function, not about accuracy on images.
- "About one millionth" and "about two millionths" round 1.19e-06 and 2.38e-06.
- The narration is an AI voice. The outro says so on screen.

## Takeaway
Confirm a tool's "it worked" without asking the tool.

## VERDICT: PASS
