"""Gate V declarations for the HyperFrames beats (B01-B07), in beat_sheet.json and vertical/beat_sheet.json.

contrast_regions: the night-map look puts thousands of dim road pixels on screen; Gate V's whole-frame test
averages them with the text and reads "low contrast". These beats declare where their text lives (the title,
and the HUD text or the Google-style card it sits on), and Gate V checks contrast there instead. Each box was
tested against frames of the rendered clips before being written here.

sparse_by_design: two phone beats (B02, B04) reveal their HUD panels on the narration cue, so the 50% frame is
mostly the map; only the underfill / clustered checks are waived for them (Gate V's own rule).

    python add_qc.py      # run after ./art vertical (which rewrites vertical/beat_sheet.json)
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REASON = ("Night-map look: dim roads fill the frame by design; contrast is checked where the text is (title + HUD), "
          "regions tested on the rendered clips.")
TITLE_L, TITLE_V = [0.06, 0.06, 0.6, 0.17], [0.06, 0.05, 0.95, 0.135]
HUD_L = {"B01": [0.625, 0.2, 0.95, 0.84], "B02": [0.625, 0.2, 0.95, 0.84], "B03": [0.625, 0.2, 0.95, 0.84],
         "B04": [0.625, 0.2, 0.95, 0.84], "B05": [0.62, 0.36, 0.95, 0.84], "B06": [0.545, 0.235, 0.925, 0.53],
         "B07": [0.525, 0.45, 0.95, 0.84]}
HUD_V = {"B01": [0.06, 0.47, 0.95, 0.85], "B02": [0.06, 0.47, 0.95, 0.85], "B03": [0.06, 0.47, 0.95, 0.85],
         "B04": [0.06, 0.47, 0.95, 0.85], "B05": [0.06, 0.6, 0.95, 0.85], "B06": [0.08, 0.52, 0.92, 0.7],
         "B07": [0.06, 0.7, 0.95, 0.85]}
SPARSE_V = {"B02": "HUD panels reveal on their narration cue; the 50% frame is mostly the exploded map stack",
            "B04": "HUD stats reveal on their narration cue; the 50% frame is mostly the traffic map"}

for sheet, vertical in ((HERE / "beat_sheet.json", False), (HERE / "vertical" / "beat_sheet.json", True)):
    s = json.loads(sheet.read_text(encoding="utf-8"))
    for b in s["beats"]:
        bid = b["beat_id"]
        if bid not in HUD_L:
            continue
        qc = b.setdefault("qc", {})
        qc["contrast_regions"] = [{"label": "title", "box": TITLE_V if vertical else TITLE_L},
                                  {"label": "hud", "box": (HUD_V if vertical else HUD_L)[bid]}]
        qc["contrast_reason"] = REASON
        if vertical and bid in SPARSE_V:
            qc["sparse_by_design"] = True
            qc["sparse_reason"] = SPARSE_V[bid]
    sheet.write_text(json.dumps(s, ensure_ascii=False, indent=1), encoding="utf-8")
    print("qc declarations written:", sheet.relative_to(HERE))
