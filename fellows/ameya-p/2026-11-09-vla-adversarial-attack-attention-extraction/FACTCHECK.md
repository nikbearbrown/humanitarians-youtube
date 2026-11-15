# FACTCHECK - week8 (Nov 09)

## Primary source

`D:/Ameya/Career/Humanitarians AI/humanitarians-youtube/fellows/ameya-p/2026-11-09-vla-adversarial-attack-attention-extraction/work_report.md`

## Supporting implementation evidence

- `common/kaggle_utils.py`: `extract_llama_cross_attention_maps()` requests `output_attentions=True`, selects text-query to visual-key attention, normalizes it, and reshapes it to a 16x16 grid.
- `smoke_tests/utils_tests.py`: verifies 32 layers, 16x16 maps, 256 visual tokens, normalized sums, repeated-request equality, and instruction sensitivity against the remote endpoint.

## Claims used in the beat sheet

| Claim | Evidence | Status |
|---|---|---|
| The attention path uses a real OpenVLA forward pass. | Work report section 3; `kaggle_utils.py` lines 293-298. | Supported |
| OpenVLA's 256 visual tokens are inserted after `<BOS>`. | Work report section 3; `kaggle_utils.py` lines 336-341. | Supported |
| The output contains per-layer 16x16 maps and an average map. | Work report section 3; `kaggle_utils.py` lines 368-379. | Supported |
| Live tests observed 32 layers, per-layer sum 1.0, exact repeatability, and instruction sensitivity. | Work report section 4; `utils_tests.py` lines 124-145 and 173-230. | Supported |
| A successful physical-patch or trajectory-steering attack has occurred. | Not claimed by the report. | Excluded explicitly |

## Editorial correction

The work report calls the extracted quantity “text-to-vision attention.” The beat sheet specifies that this is causal self-attention from text query positions to inserted visual key positions, not encoder-decoder cross-attention. This follows the implementation comments and avoids overstating the architecture.
