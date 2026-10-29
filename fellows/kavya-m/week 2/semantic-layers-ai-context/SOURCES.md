# SOURCES — kavya-semantic-layers-ai-context

| Source | Used for | Notes |
|---|---|---|
| `demo/semantic_demo.py` (this folder) | Every figure in B00, B03, B04 and B06 | Python stdlib `sqlite3`, synthetic data, deterministic. No network, no keys, no model calls |
| `demo/semantic_demo_output.txt` | Verbatim stdout shown in B03/B04 | Regenerate with `python -I demo/semantic_demo.py > demo/semantic_demo_output.txt` |
| `youtube/claude-liam-semantic-layers-ai-context/beat_sheet.json` | Argument structure (four parts, two agents disagreeing, the boundary) | Unrendered draft in this repo with authored figures. Rewritten under Kavya's name with measured figures; corrections are in `FACTCHECK.md` |

No external articles, papers, images or footage are used. The data is synthetic (ten October orders)
and was made only for this demonstration. The four-part framing is general semantic-layer practice
(central metric definitions, as in tools like dbt's Semantic Layer or Cube). It is not attributed to,
or quoted from, any one vendor.

## Seeds and determinism

- `BrutalistHesitantWriter` seed: `kavya-semantic-layers-4127`
- The demo has no randomness; the same script gives byte-identical output.
