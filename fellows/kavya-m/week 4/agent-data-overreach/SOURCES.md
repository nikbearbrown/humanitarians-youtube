# SOURCES — kavya-agent-data-overreach

| Source | Used for | Notes |
|---|---|---|
| `demo/overreach_demo.py` (this folder) | Every figure and output line in B00, B03, B04 and B06 | Python stdlib `sqlite3`, fake data, deterministic. No network, no keys, no model calls |
| `demo/overreach_demo_output.txt` | Verbatim stdout shown in B03/B04 | Regenerate with `python -I demo/overreach_demo.py > demo/overreach_demo_output.txt` |
| `youtube/claude-liam-agent-data-overreach/beat_sheet.json` | Scenario (ticket 4471, customers 812 and 903) and four-part framing | Unrendered draft in this repo with an authored run. Rebuilt as running code under Kavya's name |

The framing (least privilege, row-level scope, centralized enforcement, audit trails) is general
access-control practice. It is not quoted from, or attributed to, any one vendor or standard. No external
articles, images or footage are used. All names and card digits are fake.

## Seeds and determinism

- `BrutalistHesitantWriter` seed: `kavya-data-overreach-6043`
- The demo has no randomness; the same script gives byte-identical output.
