"""Gate V declarations for a week-12 reel's HyperFrames beats (B01-B06), in beat_sheet.json and vertical/beat_sheet.json.

contrast_regions: the dark three.js stage puts glows, particles and dim grid lines on screen; Gate V's whole-frame
test averages them with the text and reads "low contrast". These beats declare where their text lives (the title,
and the HUD column), and Gate V checks contrast there instead. The boxes follow hfkit.Frame's layout (title block;
HUD column x 0.615-0.935 W landscape, y 0.455-0.86 H phone) and were tested on frames of the rendered clips
(week-12/hfgate.py) before the finals.

    python add_qc.py <reel-dir>      # run after ./art vertical (which rewrites vertical/beat_sheet.json)
"""
import json
import sys
from pathlib import Path

reel = Path(sys.argv[1]).resolve()
REASON = ("Dark three.js stage: glows, particles and grid lines fill the frame by design; contrast is checked where "
          "the text is (title + HUD column), regions tested on the rendered clips.")
TITLE_L, TITLE_V = [0.06, 0.06, 0.6, 0.17], [0.06, 0.04, 0.95, 0.13]
HUD_L, HUD_V = [0.605, 0.2, 0.95, 0.84], [0.06, 0.45, 0.95, 0.87]
# sparse_by_design (phone): beats whose HUD numbers reveal on narration cues after Gate V's 50% sample; only the
# underfill / clustered checks are waived for them (Gate V's own rule). Each was measured on the rendered clip.
SPARSE_V = {"netflix-streaming-explainer": {
    "B05": "The far / near trip times reveal on their narration cues (70% and 87% of the beat); the 50% frame holds "
           "the globe, the Open Connect tag and the overnight note (53% fill)"}}
for sheet, vertical in ((reel / "beat_sheet.json", False), (reel / "vertical" / "beat_sheet.json", True)):
    if not sheet.exists():
        continue
    s = json.loads(sheet.read_text(encoding="utf-8"))
    for b in s["beats"]:
        if b["shot"].get("source") != "hyperframes":
            continue
        qc = b.setdefault("qc", {})
        qc["contrast_regions"] = [{"label": "title", "box": TITLE_V if vertical else TITLE_L},
                                  {"label": "hud", "box": HUD_V if vertical else HUD_L}]
        qc["contrast_reason"] = REASON
        why = SPARSE_V.get(s["metadata"]["slug"].replace("-vertical", ""), {}).get(b["beat_id"]) if vertical else None
        if why:
            qc["sparse_by_design"] = True
            qc["sparse_reason"] = why
    sheet.write_text(json.dumps(s, ensure_ascii=False, indent=1), encoding="utf-8")
    print("qc declarations written:", sheet.relative_to(reel))
