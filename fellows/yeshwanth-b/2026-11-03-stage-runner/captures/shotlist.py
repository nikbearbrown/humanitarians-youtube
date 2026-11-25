"""Write SHOTLIST.md for a finished fantasy reel from its beat_sheet.json.

    python3 shotlist.py <reel> "<film title>"
"""
import json
import sys
from pathlib import Path

LABEL = ('segment', 'artifactTitle', 'title', 'section', 'text')


def visual(shot):
    if 'remotion' in shot:
        r = shot['remotion']
        props = r.get('props', {})
        label = next((props[k] for k in LABEL if props.get(k)), '')
        return f"{r['pattern']}: {' '.join(str(label).split())[:70]}"
    clip = shot.get('clip')
    if clip:
        parts = []
        for g in clip['segments']:
            if g['kind'] == 'hold':
                parts.append(f"hold +{g['output_frames']}")
                continue
            s = f"{g['kind']} {g['source_start_frame']}+{g['source_frames']}"
            if g.get('factor', 1) != 1:
                s += f" ×{g['factor']}"
            if g.get('crop'):
                s += f" crop {tuple(g['crop'])}"
            parts.append(s)
        return f"take `{clip['take']}` — " + ', '.join(parts)
    return f"take `{shot.get('capture', '?')}` — {shot.get('evidence_media', shot.get('type', '?'))}"


def main(reel, title):
    reel = Path(reel)
    beats = json.loads((reel / 'beat_sheet.json').read_text())['beats']
    rows, total = [], 0.0
    for b in beats:
        d = b.get('actual_duration_s') or b['kokoro_duration_s']
        total += d
        rows.append(f"| {b['beat_id']} | {b['act']} | {d:.2f} s | {visual(b['shot'])} |")
    m, s = divmod(round(total), 60)
    text = '\n'.join([
        f'# SHOTLIST — {title}', '',
        '3840×2160 at 30 fps; a 2160×3840 vertical companion is built from the same beats. '
        'Gameplay rows give exact source frames: start+count, with a replay factor, crop or held frames where labelled.', '',
        '| Beat | Act | Duration | Visual |', '|---|---|---|---|', *rows, '',
        f'Total {total:.1f} s ({m}:{s:02d}).', ''])
    (reel / 'SHOTLIST.md').write_text(text)
    print(f'{reel.name}: {len(rows)} beats, {total:.1f} s')


if __name__ == '__main__':
    main(*sys.argv[1:3])
