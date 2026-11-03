"""Finish a `./art vertical` plan for one Basketball Blaster reel.

    python3 make_vertical.py <reel>

- narration: copies the parent's padded audio/beat-*.wav (exact beat lengths)
- gameplay (SCREEN) beats: re-cut natively in portrait from the SAME take and the
  SAME segment list as the landscape clip (no retiming, no crop of the game)
- zoom beats: the same labelled zoom, re-composed for portrait
- QC: drops landscape-only declarations; the hesitant-writer sparse declaration is kept
"""
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import reelkit as rk  # noqa: E402

PORTRAIT_QC = {'full_bleed': True, 'full_bleed_reason': 'Portrait gameplay: the real engine frame is scaled to the full 2160 px width (2160x1215) by design; cropping it would cut the game. Disclosure text above and input chips below sit inside the 9:16 title-safe box.', 'contrast_regions': [{'label': 'disclosure text above the game', 'box': [0.05, 0.14, 0.95, 0.235]}], 'contrast_reason': 'Dark game screens sit on a dark backing; whole-frame sampling measures game art. Our own essential text, the disclosure block, is measured in its own region; game pixels are evidence.'}

reel = Path(sys.argv[1]).resolve()
vert = reel / 'vertical'
parent = {b['beat_id']: b for b in json.loads((reel / 'beat_sheet.json').read_text())['beats']}
sheet = json.loads((vert / 'beat_sheet.json').read_text())
(vert / 'audio').mkdir(exist_ok=True)
for b in sheet['beats']:
    p = parent[b['beat_id']]
    shutil.copy2(reel / p['audio_file'], vert / p['audio_file'])
    b['audio_file'] = p['audio_file']
    b['actual_duration_s'] = p['actual_duration_s']
    qc = b.get('qc') or {}
    for k in ('full_bleed', 'full_bleed_reason', 'contrast_regions', 'contrast_reason'):
        qc.pop(k, None)
    if qc:
        b['qc'] = qc
    else:
        b.pop('qc', None)
    if 'clip' in p['shot']:
        clip = p['shot']['clip']
        out = vert / f"media/{b['beat_id']}.mp4"
        if clip['segments'][0]['kind'] == 'zoom':
            z = clip['segments'][0]
            n = rk.cut_zoom_portrait(clip['take'], z['source_start_frame'], z['source_frames'], z['crop'], out,
                                     hold=sum(s['output_frames'] for s in clip['segments'] if s['kind'] == 'hold'))
        else:
            n = rk.cut_segments_portrait(clip['take'], clip['segments'], out)
        assert n == clip['frames'], (b['beat_id'], n, clip['frames'])
        b['shot'] = dict(p['shot'])
        b['shot']['clip'] = dict(clip, orientation='portrait 2160x3840; game 2160x1215 at y 1312')
        b['shot']['evidence_media'] = f"media/{b['beat_id']}.mp4"
        b['qc'] = dict(PORTRAIT_QC)
        print(b['beat_id'], 'portrait gameplay', n, 'frames')
md = sheet['metadata']
md['width'], md['height'] = 2160, 3840
md['note'] = (md.get('note', '') + ' Vertical companion: designed beats re-rendered as native 9:16 cards or 916 '
              'compositions; gameplay re-cut in portrait from the same frames.').strip()
(vert / 'beat_sheet.json').write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
print('vertical sheet ready:', vert)
