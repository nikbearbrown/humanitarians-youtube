"""Finish a `./art vertical` plan for one walker-towerdefense reel.

    python3 make_vertical.py <reel>

- narration: copies the parent's padded audio/beat-*.wav (exact beat lengths)
- gameplay (SCREEN) beats: re-cut natively in portrait from the SAME take and the
  SAME segment list as the landscape clip (no retiming, no crop of the game)
- QC: drops landscape-only declarations (full_bleed for gameplay, landscape
  contrast boxes); the hesitant-writer sparse declaration is kept
"""
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import reelkit as rk  # noqa: E402

reel = Path(sys.argv[1]).resolve()
vert = reel / 'vertical'
parent = {b['beat_id']: b for b in json.loads((reel / 'beat_sheet.json').read_text())['beats']}
sheet = json.loads((vert / 'beat_sheet.json').read_text())
(vert / 'audio').mkdir(exist_ok=True)
for b in sheet['beats']:
    p = parent[b['beat_id']]
    src = reel / p['audio_file']
    shutil.copy2(src, vert / p['audio_file'])
    b['audio_file'] = p['audio_file']
    b['actual_duration_s'] = p['actual_duration_s']
    qc = b.get('qc') or {}
    qc.pop('full_bleed', None); qc.pop('full_bleed_reason', None)
    qc.pop('contrast_regions', None); qc.pop('contrast_reason', None)
    if qc:
        b['qc'] = qc
    else:
        b.pop('qc', None)
    if 'clip' in p['shot']:
        clip = p['shot']['clip']
        label = (['STAGED FAILURE', 'level file broken in an isolated copy', f'build {rk.BUILD_COMMIT} · Godot 4.7.2']
                 if p['shot'].get('staged') else None)
        out = vert / f"media/{b['beat_id']}.mp4"
        n = rk.cut_segments_portrait(clip['take'], clip['segments'], out, label)
        assert n == clip['frames'], (b['beat_id'], n, clip['frames'])
        b['shot']['clip'] = dict(clip, orientation='portrait 2160x3840; game 2160x1530 at y 1155')
        b['shot']['evidence_media'] = f"media/{b['beat_id']}.mp4"
        print(b['beat_id'], 'portrait gameplay', n, 'frames')
md = sheet['metadata']
md['width'], md['height'] = 2160, 3840
md['note'] = (md.get('note', '') + ' Vertical companion: designed beats re-rendered with native 916 compositions; '
              'gameplay re-cut in portrait from the same frames.').strip()
(vert / 'beat_sheet.json').write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
for doc in ('FACTCHECK.md', 'SHOTLIST.md', 'PROMPTS.md', 'SOURCES.md', 'BUILD-LOG.md'):
    if (reel / doc).exists():
        shutil.copy2(reel / doc, vert / doc)
print('vertical sheet ready:', vert)
