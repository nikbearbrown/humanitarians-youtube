# SOURCES — kavya-ai-junk-data-gate

| Source | Used for | Notes |
|---|---|---|
| `demo/junk_gate_demo.py` (this folder) | Every figure in B00, B03, B04 and B06 | Python stdlib only, synthetic rows, deterministic. No network, keys or model calls |
| `demo/junk_gate_demo_output.txt` | Verbatim stdout shown in B03/B04 | Regenerate with `python -I demo/junk_gate_demo.py > demo/junk_gate_demo_output.txt` |

The framing (provenance, range checks, near-duplicate detection, quarantine) is standard data-quality
practice. It is not quoted from any one tool or vendor. The near-duplicate check is Jaccard similarity on
word 3-shingles, a common textbook technique. No external articles, images or footage are used. All rows
are synthetic.

## Seeds and determinism

- `BrutalistHesitantWriter` seed: `kavya-ai-junk-gate-7319`
- The demo has no randomness; the same script gives byte-identical output.
