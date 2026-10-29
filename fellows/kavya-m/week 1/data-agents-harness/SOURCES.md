# SOURCES — kavya-data-agents-harness

| Source | Used for | Notes |
|---|---|---|
| `demo/harness_demo.py` (this folder) | Every figure in B03, B04 and B06 | Python stdlib `sqlite3`, synthetic data, deterministic. No network, no keys, no model calls |
| `demo/harness_demo_output.txt` | Verbatim stdout shown in B03/B04 | Regenerate with `python -I demo/harness_demo.py > demo/harness_demo_output.txt` |
| `youtube/claude-liam-data-agents-harness/beat_sheet.json` | Argument structure (four parts, thin vs real, the boundary) | Unrendered draft in this repo. Rewritten under Kavya's name; corrections logged in `FACTCHECK.md` |

No external articles, papers, images or footage are used. The data is synthetic (four customers,
six orders, nine line items) and was made only for this demonstration.

## Seeds and determinism

- `BrutalistHesitantWriter` seed: `kavya-data-agents-harness-3317`
- The demo has no randomness; the same script gives byte-identical output.
