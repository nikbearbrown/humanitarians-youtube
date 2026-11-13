"""beat_sheet.json for claude-liam-meet-muse (ai-explainer, claude-liam).

    python3 make_sheet.py author     # before Kokoro
    python3 make_sheet.py finish     # after Kokoro: padded audio, exact durations, cue times
Body visuals are drawn by scenes.py (both aspects); bookends are Remotion scenes.
"""
import json
import math
import subprocess
import sys
from pathlib import Path

REEL = Path(__file__).resolve().parent
sys.path.insert(0, str(REEL))
import script as S  # noqa: E402

FPS = 30
PATTERN = {'composer': 'ClaudeComposerAsk', 'writer': 'BrutalistHesitantWriter', 'handoff': 'ClaudeComposerAsk'}


def probe(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                                capture_output=True, text=True, check=True).stdout)


def pad(src, out, lead, total):
    ms = int(round(lead * 1000))
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(src), '-af', f'adelay={ms}|{ms},apad,atrim=0:{total:.6f}',
                    '-ar', '48000', '-ac', '2', '-c:a', 'pcm_s16le', str(out)], check=True)


def author():
    beats = []
    for spec in S.BEATS:
        b = {'beat_id': spec['id'], 'act': spec['kind'].upper(), 'narration_text': spec['narration'],
             'voice': 'am_onyx', 'engine': 'kokoro'}
        k = spec['kind']
        if k in PATTERN:
            props = {'composer': S.COMPOSER, 'writer': S.WRITER, 'handoff': S.HANDOFF}[k]
            b['shot'] = {'type': 'GRAPHIC', 'source': 'remotion',
                         'remotion': {'pattern': PATTERN[k], 'props': dict(props)},
                         'show': [{'at': 0.0, 'event': PATTERN[k]}]}
            if k == 'writer':
                b['qc'] = {'sparse_by_design': True, 'sparse_reason': ('Hesitant writer: text types on screen over '
                           'the narration; mid-beat samples show a partial page.')}
        else:
            b['shot'] = {'type': 'GRAPHIC', 'source': 'own', 'treatment': 'none', 'scene': k,
                         'reconstruction': k in ('muse_ui', 'blender', 'godot'),
                         'show': [{'at': 0.0, 'event': f'scenes.py: {k}'}]}
        if k == 'outro':
            b['tail_silence_s'] = 1.0
            b['qc'] = {'sparse_by_design': True, 'sparse_reason': 'Title-restate outro card: centred title, presenter and channel handle; the negative space is the design.'}
        if spec.get('lead'):
            b['lead_silence_s'] = spec['lead']
        beats.append(b)
    sheet = {'metadata': {'slug': S.SLUG, 'title': S.TITLE, 'topic': 'Irreducibly Human', 'skill': 'ai-explainer',
                          'channel': 'claude-hai', 'brand': 'claude-hai', 'persona': 'Liam (AI voice) presenting for Yeshwanth Balaji',
                          'presenter': 'Yeshwanth Balaji', 'playlist': 'Humanitarians AI Fellows', 'folderLabel': '@HumanitariansAI', 'voice': 'am_onyx', 'voice_kokoro': 'am_onyx', 'engine': 'kokoro',
                          'palette': 'claude', 'register': 'Plain', 'fps': FPS, 'width': 3840, 'height': 2160,
                          'aspect_ratio': '16:9', 'fit': 'crop', 'captions': False, 'caption_policy': 'none',
                          'greeting_language': 'English (Hi)',
                          'audience': ('graduate students in a game engineering / real-time 3D course who have never '
                                       'used an autonomous AI agent'),
                          'source_doc': "Presenter's brief (Yeshwanth Balaji) describing Muse",
                          'note': ('Muse, Blender and Godot screens are labelled illustrations, not captures. '
                                   'No paid calls, no upload.')},
             'beats': beats}
    (REEL / 'beat_sheet.json').write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
    print('authored', len(beats))


def finish():
    p = REEL / 'beat_sheet.json'
    sheet = json.loads(p.read_text())
    specs = {s['id']: s for s in S.BEATS}
    (REEL / 'audio').mkdir(exist_ok=True)
    for b in sheet['beats']:
        spec = specs[b['beat_id']]
        mp3 = REEL / f"mp3/beat-{b['beat_id']}.mp3"
        speech = probe(mp3)
        lead = spec.get('lead', 0.3 if spec['kind'] not in PATTERN else 0.0)
        tail = spec.get('tail', 0.0) + (0.6 if spec['kind'] not in ('outro',) else 0.0)
        total = math.ceil((lead + speech + tail) * FPS - 1e-8) / FPS
        out = REEL / f"audio/beat-{b['beat_id']}.wav"
        pad(mp3, out, lead, total)
        b['audio_file'] = f"audio/beat-{b['beat_id']}.wav"
        b['actual_duration_s'] = total
        b['speech'] = {'lead_s': lead, 'speech_s': round(speech, 3)}
        if 'remotion' in b['shot']:
            b['shot']['remotion']['props']['durationSeconds'] = total
        if spec.get('cues'):
            text = spec['narration']
            times = []
            for ph in spec['cues']:
                i = text.find(ph)
                if i < 0:
                    raise SystemExit(f"{b['beat_id']}: cue not in narration: {ph!r}")
                times.append(round(lead + speech * i / len(text), 2))
            b['shot']['cue_times'] = times
    p.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
    for b in sheet['beats']:
        print(b['beat_id'], f"{b['actual_duration_s']:.2f}s", b['shot'].get('cue_times', ''))
    print('total', round(sum(b['actual_duration_s'] for b in sheet['beats']), 1))


if __name__ == '__main__':
    {'author': author, 'finish': finish}[sys.argv[1]]()
