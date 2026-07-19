# FACTCHECK — vox-panda-proxy

Source: `computational-skepticism-for-ai/chapters/04-robustness-what-understanding-means-when-a-pixel-can-break-the-model.md`

## Terms table

| Term | Definition used in video | Chapter reference |
|---|---|---|
| Adversarial perturbation | Invisible noise added to an image that flips model classification with high confidence | Lines 11–15 |
| Proxy feature | A feature that correlated reliably with correct labels during training but is not the human-relevant feature | Lines 49–51 |
| Shape channel | Outlines, pose, and color that humans use to recognize the subject | Line 247 (card description) |
| Texture channel | High-frequency statistical patterns invisible to humans | Lines 11–13, 49 |
| Fragile framing | Treating adversarial vulnerability as a defect to patch | Lines 27, 51 |
| Proxy framing | Treating adversarial vulnerability as revealing what the model actually learned | Lines 27, 49 |

## Claim-by-claim check

| Beat | Claim | Chapter support | Status |
|---|---|---|---|
| B02 | Panda → gibbon with 99.3% confidence after invisible perturbation | Lines 11–15: panda→gibbon, Goodfellow et al. ICLR 2015 | PASS |
| B04 | Natural reaction: model is brittle; correct diagnosis: model learned wrong thing | Lines 27, 49 | PASS |
| B05 | Perturbation leaves shape unchanged, slides texture from panda to gibbon | Lines 11–13, card description line 247–251 | PASS |
| B07 | Model learned statistical signature of pixel arrangements in panda training images | Line 49: exact | PASS |
| B08 | Quote: proxy feature definition | Lines 49–51: paraphrase of exact text | PASS |
| B09 | Patching moves attack surface without fixing underlying problem | Line 51: exact | PASS |
| B10 | Quote: adversarial perturbations as features (Ilyas et al.) | Line 53: paraphrase | PASS |
| B11 | 94% accuracy does not mean robust or that model learned intended features | Lines 18, 65 | PASS |

## B12 — THE EXAMPLE beat (illustrative)

| Claim | Status |
|---|---|
| Skin lesion classifier scores 92% on test set | illustrative |
| Malignant cases in training: ruler present 89%; benign: 12% | illustrative |
| Model learned "ruler = cancer" as proxy | illustrative (same mechanism as panda texture proxy, lines 49–51) |
| Without rulers: accuracy 62% | illustrative |

All specific numbers and scenario details are invented. The mechanism (proxy feature learned from spurious correlation) is chapter-accurate (lines 49–51).

## VERDICT: PASS
