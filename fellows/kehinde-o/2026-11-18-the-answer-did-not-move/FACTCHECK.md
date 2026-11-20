# FACTCHECK — The Answer Did Not Move

Source of record: `github.com/Kenny0bi/fuse` at commit `20ffa4e`. Every figure computed in
this session by `evidence_run.py` (this folder), results in `evidence.json`. The model was
exported with `export_models.py`, which is the body of the repo's `data/export.sh`
(torchvision resnet18, weights=None, opset 13, do_constant_folding=False). Run in a
throwaway virtual environment (numpy 1.26.4, onnx 1.16.2) because the system PyTorch
2.2.2 cannot bridge to the system NumPy 2.2.6. The repo's own test suite was also run and
reports the same figures.

| # | Claim | Beat | Verdict | Measured |
|---|---|---|---|---|
| 1 | 141 operations become 32 | B02 | TRUE | nodes_before 141, nodes_after 32 |
| 2 | 72 pass-through (Identity) nodes removed | B02 | TRUE | identity_removed 72 |
| 3 | All 20 normalization layers folded | B02 | TRUE | conv_bn_fused 20 = BatchNormalization 20 |
| 4 | 17 activations fused | B02 | TRUE | relu_fused 17 |
| 5 | Fold algebra exact: forms agree to 14 decimal places | B03 | TRUE | first Conv/BN, float64: max gap 3.6e-15 |
| 6 | Compared all one thousand outputs | B04 | TRUE | resnet18 Gemm output, 1,000 classes |
| 7 | Largest difference about one millionth | B04 | TRUE | 1.19e-06 |
| 8 | On outputs as large as 4.7 | B04 | TRUE | max abs output 4.68 |
| 9 | Top prediction identical | B04 | TRUE | argmax equal |
| 10 | Runtime vs onnxruntime: about two millionths, same top prediction | B05 | TRUE | 2.38e-06, argmax equal |

Note: the repo README gives 2.6e-06 for runtime vs onnxruntime. This session measured
2.38e-06 on its own export (PyTorch 2.2.2). Same order and conclusion.

## Algebra check
BN(y) = gamma (y - mu) / sqrt(sigma^2 + eps) + beta with y = W * x + b gives
W' = gamma / sqrt(sigma^2 + eps) W and b' = gamma (b - mu) / sqrt(sigma^2 + eps) + beta.
Checked numerically on /conv1/Conv and /bn1/BatchNormalization with realistic statistics,
entirely in float64: 3.6e-15.

## Deliberately not claimed
- Not a claim about image-classification accuracy; the network is untrained, as exported by the repo.

## First-person claims added in the script revision (18 Nov 2026)

The narration was rewritten to describe what I did. Each new claim about my own work traces to the record:

| Claim | Source |
|---|---|
| I had checked my runtime against onnxruntime before trusting any comparison | Repo design: runtime verified against onnxruntime before any pass (tests/test_runtime.py) |
