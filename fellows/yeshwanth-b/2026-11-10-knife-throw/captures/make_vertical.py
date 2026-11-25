"""Finish a `./art vertical` plan for one Gino: Knife Throw reel.

    python3 make_vertical.py <reel>

- narration: copies the parent's padded audio/beat-*.wav (exact beat lengths)
- gameplay (SCREEN) beats: re-cut natively in portrait from the SAME take and the
  SAME segment list as the landscape clip (no retiming). A clip that stays inside
  a level (play, hints, pause, game over, level complete) shows a 4:3 window of the
  game view (logical x 64-1024) at full width, labelled as a crop; a clip that touches
  the main menu, How to Play or the credits keeps the whole 16:9 frame.
- QC: drops landscape-only declarations; the hesitant-writer sparse declaration is kept
"""
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import reelkit as rk  # noqa: E402

WIDE_SCENES = {'MainMenu', 'Instructions', 'Credits'}


def scene_at(log, frame):
    s = None
    for r in log:
        if r['frame'] > frame:
            break
        s = r['game'].get('scene', s)
    return s


def needs_full_frame(take, segments):
    log = rk.take_log(take)
    for seg in segments:
        if seg['kind'] == 'hold':
            continue
        a, n = seg['source_start_frame'], seg['source_frames']
        for f in range(a, a + n, 5):
            if scene_at(log, f) in WIDE_SCENES:
                return True
        if scene_at(log, a + n - 1) in WIDE_SCENES:
            return True
    return False


def portrait_qc(crop):
    gh, y0 = rk._portrait_geom(crop)
    lines = 5 if crop else 4
    top = (y0 - 70 - 64 * (lines - 1) - 92 + 12) if crop else 560
    bottom = top + 92 + 64 * (lines - 1)
    box = [0.05, round((top - 10) / rk.PH, 3), 0.95, round((bottom + 10) / rk.PH, 3)]
    what = ('a 4:3 window of the engine frame (engine x 192-3072) scaled to the full 2160 px width (2160x1620), labelled as a crop'
            if crop else 'the real engine frame scaled to the full 2160 px width (2160x1215)')
    return {'full_bleed': True,
            'full_bleed_reason': f'Portrait gameplay: {what}, edge to edge by design. Disclosure text above and input chips below sit inside the 9:16 title-safe box.',
            'contrast_regions': [{'label': 'disclosure text above the game', 'box': box}],
            'contrast_reason': 'Dark game screens sit on a dark backing; whole-frame sampling measures game art. Our own essential text, the disclosure block, is measured in its own region; game pixels are evidence.'}


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
        crop = None if needs_full_frame(clip['take'], clip['segments']) else rk.STREET
        n = rk.cut_segments_portrait(clip['take'], clip['segments'], out, crop=crop)
        assert n == clip['frames'], (b['beat_id'], n, clip['frames'])
        gh, y0 = rk._portrait_geom(crop)
        b['shot'] = dict(p['shot'])
        b['shot']['clip'] = dict(clip, orientation=f'portrait 2160x3840; game 2160x{gh} at y {y0}'
                                 + ('; 4:3 window (engine x 192-3072) of the game view' if crop else '; whole frame'))
        b['shot']['evidence_media'] = f"media/{b['beat_id']}.mp4"
        b['qc'] = portrait_qc(crop)
        print(b['beat_id'], 'portrait gameplay', n, 'frames', '4:3 window' if crop else 'whole frame')
md = sheet['metadata']
md['width'], md['height'] = 2160, 3840
md['note'] = (md.get('note', '') + ' Vertical companion: designed beats re-rendered as native 9:16 cards or 916 '
              'compositions; gameplay re-cut in portrait from the same frames.').strip()
(vert / 'beat_sheet.json').write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
print('vertical sheet ready:', vert)
