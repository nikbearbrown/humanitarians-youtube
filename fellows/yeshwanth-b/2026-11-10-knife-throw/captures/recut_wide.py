"""Re-cut only the whole-frame portrait gameplay beats of one vertical sheet with the
current reelkit layout, and refresh their contrast-region declaration.

    python3 recut_wide.py <reel>
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import reelkit as rk  # noqa: E402

sys.argv = [sys.argv[0], sys.argv[1]]
src = (Path(__file__).resolve().parent / 'make_vertical.py').read_text()
ns = {"__file__": str(Path(__file__).resolve().parent / "make_vertical.py")}
exec(src.split('\nreel = Path(sys.argv[1])')[0], ns)   # helpers only, not the main pass
portrait_qc = ns['portrait_qc']

vert = Path(sys.argv[1]).resolve() / 'vertical'
sheet_path = vert / 'beat_sheet.json'
sheet = json.loads(sheet_path.read_text())
for b in sheet['beats']:
    clip = b['shot'].get('clip')
    if not clip or 'whole frame' not in clip.get('orientation', ''):
        continue
    n = rk.cut_segments_portrait(clip['take'], clip['segments'], vert / f"media/{b['beat_id']}.mp4")
    assert n == clip['frames'], (b['beat_id'], n, clip['frames'])
    b['qc'] = portrait_qc(None)
    print(b['beat_id'], 're-cut whole frame', n, 'frames')
sheet_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
