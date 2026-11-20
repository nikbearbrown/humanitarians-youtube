"""Pre-checks the rendered HyperFrames clips against Gate V and GATE T before ./art final (no surprises at 4K).

Extracts 4K frames of media/B0x.mp4 and pantry/B0x-916.mp4 at Gate V's sample points (50%, 85% of the beat)
plus 97%, then runs final_frame_check.analyze_frame (Gate V) and type_check's size / contrast / overlap tests;
contrast is also run on the beat's declared qc.contrast_regions when the sheet has them.

    python hfgate.py <reel-dir> [B01 B02 ...]
"""
import json
import subprocess
import sys
from pathlib import Path

T = "D:/Rohan/Claude/HAI/RohanClaudeHAIbrutalist.art/runtime"
sys.path.insert(0, T + "/qc")
sys.path.insert(0, T + "/scripts")
argv, sys.argv = sys.argv, ["x"]
import final_frame_check as fv  # noqa: E402
import type_check as tc  # noqa: E402
from PIL import Image  # noqa: E402

reel = Path(argv[1]).resolve()
only = argv[2:] or None
out = reel / "_gate"
out.mkdir(exist_ok=True)
sheets = {"l": json.loads((reel / "beat_sheet.json").read_text(encoding="utf-8"))}
vs = reel / "vertical" / "beat_sheet.json"
if vs.exists():
    sheets["v"] = json.loads(vs.read_text(encoding="utf-8"))
for a in ("l", "v"):
    beats = {b["beat_id"]: b for b in sheets.get(a, sheets["l"])["beats"]}
    for bid, b in beats.items():
        if b["shot"].get("source") != "hyperframes" or (only and bid not in only):
            continue
        clip = reel / ("pantry" if a == "v" else "media") / (f"{bid}-916.mp4" if a == "v" else f"{bid}.mp4")
        if not clip.exists():
            print(a.upper(), bid, "no clip yet")
            continue
        D = b["actual_duration_s"]
        for fr in (0.5, 0.85, 0.97):
            png = out / f"{a}_{bid}_{int(fr * 100)}.png"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{D * fr:.3f}", "-i", str(clip), "-frames:v", "1", str(png)],
                           check=True, stdin=subprocess.DEVNULL)
            d, cover = fv.analyze_frame(str(png), b.get("qc", {}).get("contrast_regions"))
            img = Image.open(png).convert("RGB")
            pat = "HyperFrames:" + b["shot"]["hyperframes"]["composition"]
            line = [a.upper(), bid, f"{int(fr * 100)}%", "GateV", [x[1] for x in d] or "clean", f"fill {cover * 100:.0f}%",
                    "| size", tc.check_min_size(img, bid, pat)[0], "contrast", tc.check_contrast(img, bid, pat)[0],
                    "| overlap", tc.check_bbox_overlap(img)[0]]
            if "contrast_regions" in b.get("qc", {}):
                line += ["| regions", tc.check_declared_contrast(img, b, pat)]
            print(*line, flush=True)
