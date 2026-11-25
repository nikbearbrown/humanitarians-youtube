"""Builds beat_sheet.json for claude-liam-knife-throw-gdd (godot-gdd walker).

    python3 make_sheet.py author    # narration + shots (run before Kokoro)
    python3 make_sheet.py finish    # after Kokoro: pad audio, cut clips, cues, ledger

Every excerpt is read from GDD.md (written for this film set; the game folder has no
GDD and is not modified) by line number at build time, so the screen can only show what the document says. Gameplay comes only from
the scripted-input takes in ../knife-throw-captures (same build, cffbb01).
"""
import json
import shutil
import sys
from pathlib import Path

from PIL import Image

REEL = Path(__file__).resolve().parent


def link_or_copy(src, dst):
    """Hard-link a take into the reel (same bytes, no extra disk); copy across volumes."""
    import os
    dst = Path(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        dst.unlink()
    try:
        os.link(src, dst)
    except OSError:
        shutil.copy2(src, dst)

CAPS = REEL.parent / 'knife-throw-captures'
sys.path.insert(0, str(CAPS))
import reelkit as rk  # noqa: E402
sys.path.insert(0, str(REEL))

PKG = REEL.parents[1]
GDD = REEL / 'GDD.md'
SLUG = 'claude-liam-knife-throw-gdd'
TITLE = 'Gino: Knife Throw: The Design Document Came Last'
LINES = GDD.read_text().splitlines()


def excerpt(a, b):
    return '\n'.join(LINES[a - 1:b])


SRC = 'GDD.md · Gino: Knife Throw @ cffbb01 · agent-drafted v0.1, unapproved'

from beats import BEATS  # noqa: E402

PATTERN = {'composer': 'ClaudeComposerAsk', 'writer': 'BrutalistHesitantWriter',
           'board': 'GodotDesignBoard', 'verdict': 'ClaudeVerdictArtifact', 'outro': 'ClaudeTitleOutro'}


def author():
    sheet_path = REEL / 'beat_sheet.json'
    old = json.loads(sheet_path.read_text()) if sheet_path.exists() else {'beats': []}
    old_by = {b['beat_id']: b for b in old.get('beats', [])}
    beats = []
    for spec in BEATS:
        b = {'beat_id': spec['id'], 'act': spec['act'], 'narration_text': spec['narration'],
             'voice': 'am_onyx', 'engine': 'kokoro',
             'estimated_duration_s': round(len(spec['narration'].split()) / 2.6, 1)}
        if spec['act'] == 'BODY':
            b['design_status'] = spec['status']
            b['gdd_sections'] = spec['sections']
        if spec['kind'] == 'clip':
            b['shot'] = {'type': 'SCREEN', 'source': 'own', 'treatment': 'none',
                         'type_note': 'engine capture of the game\'s own UI; GATE T pixel checks exempt (see FACTCHECK.md); overlays verified by eye',
                         'capture': spec['take'], 'method': 'scripted-input',
                         'show': [{'at': 0.0, 'event': f"real gameplay, take '{spec['take']}', build cffbb01"}]}
            b['qc'] = {'full_bleed': True, 'full_bleed_reason': ('The engine frame (scaled to 3456x1944) runs to the '
                       'top edge by design: real game pixels, not a title card. Our disclosure strip sits inside '
                       'title-safe; the game HUD at the top of the frame is game UI.'),
                       'contrast_regions': [{'label': 'disclosure strip text', 'box': [0.05, 0.905, 0.58, 0.952]}],
                       'contrast_reason': ('Gameplay beat: real engine render above a dark disclosure strip; our own '
                                           'essential text is measured in its own region; game pixels are evidence.')}
        else:
            props = dict(spec['props'])
            if spec['kind'] == 'board':
                props['excerpt'] = excerpt(*spec['lines'])
                props['source'] = f"{SRC} · lines {spec['lines'][0]}–{spec['lines'][1]}"
            b['shot'] = {'type': 'GRAPHIC', 'source': 'remotion',
                         'remotion': {'pattern': PATTERN[spec['kind']], 'props': props},
                         'show': [{'at': 0.0, 'event': f"{PATTERN[spec['kind']]}: {props.get('title', props.get('segment', ''))}"}]}
        if spec['kind'] == 'writer':
            b['qc'] = {'sparse_by_design': True, 'sparse_reason': ('Hesitant writer: text is typed on screen over '
                       'the narration, so mid-beat samples legitimately show a partial page. The finished six-line '
                       'text fills the safe area and holds for the last 1.5 s.')}
        if spec['kind'] == 'outro':
            b['kind'] = 'outro_voice'
            b['tail_silence_s'] = 1.0
        if spec.get('lead'):
            b['lead_silence_s'] = spec['lead']
        prev = old_by.get(spec['id'])
        if prev and prev.get('narration_text') == spec['narration']:
            for k in ('audio_file', 'actual_duration_s', 'kokoro_audio_file', 'kokoro_duration_s'):
                if k in prev:
                    b[k] = prev[k]
        beats.append(b)
    sheet = {'metadata': {
        'slug': SLUG, 'title': TITLE, 'topic': 'WALKER · GODOT · GDD', 'skill': 'godot-gdd',
        'modifier': 'walker', 'channel': 'claude-liam', 'brand': 'claude-liam',
        'persona': 'Liam (in for Bear)', 'in_for_bear': True,
        'voice': 'am_onyx', 'voice_kokoro': 'am_onyx', 'engine': 'kokoro',
        'palette': 'claude', 'register': 'Teardown', 'fps': 30, 'width': 3840, 'height': 2160,
        'aspect_ratio': '16:9', 'fit': 'crop', 'captions': False, 'caption_policy': 'none',
        'greeting_language': 'Spanish (Hola)',
        'audience': 'makers following the channel\'s Claude + Walker game workflows',
        'source_doc': 'GDD.md in this reel (v0.1, agent-drafted, unapproved)',
        'game_build': {'commit': None, 'snapshot_sha256': rk.BUILD_ID,
                       'engine': 'Godot 4.7.2.stable.official.ed1daf0bf'},
        'note': ('godot-gdd walker film. Board excerpts are read verbatim from GDD.md by line. Gameplay '
                 'is scripted-input capture of the real main scene, same build; no human playtest exists. '
                 'No paid calls, no upload.'),
        'tags': ['Walker', 'Godot 4', 'game design document', '2D action platformer', 'Claude', 'Kokoro', 'Remotion'],
    }, 'beats': beats}
    sheet_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
    print(f'authored {len(beats)} beats -> {sheet_path}')


def cue_times(narration, phrases, lead, dur):
    out = []
    for i, ph in enumerate(phrases):
        pos = narration.find(ph)
        if pos < 0:
            raise ValueError(f'cue phrase not in narration: {ph!r}')
        out.append({'at': round(lead + dur * pos / len(narration), 2), 'card': i})
    return out


def finish():
    sheet_path = REEL / 'beat_sheet.json'
    sheet = json.loads(sheet_path.read_text())
    specs = {s['id']: s for s in BEATS}
    (REEL / 'audio').mkdir(exist_ok=True)
    (REEL / 'evidence').mkdir(exist_ok=True)
    (REEL / 'capture').mkdir(exist_ok=True)
    evidence, clips = [], {}
    for b in sheet['beats']:
        spec = specs[b['beat_id']]
        bid = b['beat_id']
        mp3 = REEL / f'mp3/beat-{bid}.mp3'
        if not mp3.exists():
            raise SystemExit(f'{bid}: no Kokoro audio yet; run generate_audio_kokoro.py first')
        speech = rk.probe_duration(mp3)
        lead = spec.get('lead', 0.0)
        b['kokoro_audio_file'] = f'mp3/beat-{bid}.mp3'
        b['kokoro_duration_s'] = round(speech, 3)
        if spec['kind'] == 'clip':
            take = spec['take']
            need = rk.frames_for(lead + speech + 0.5)
            if 'segments' in spec:
                segs = list(spec['segments'])
                have = sum(s[2] * (s[3] if s[0] == 'replay' else 1) if s[0] != 'hold' else s[1] for s in segs)
                if have < need:  # extend the last real-time segment, never retime
                    k, s0, n = segs[-1][:3]
                    room = rk.take_frames(take) - (s0 + n)
                    grow = min(room, need - have)
                    segs[-1] = (k, s0, n + grow)
                    if need - have - grow > 0:   # take ran out: labelled held frame
                        segs.append(('hold', need - have - grow))
            else:
                n = max(spec['min_end'] - spec['start'], need)
                room = rk.take_frames(take) - spec['start']
                segs = [('play', spec['start'], min(n, room))]
                if n > room:
                    segs.append(('hold', n - room))
            info = rk.cut_segments(take, segs, REEL / f'media/{bid}.mp4')
            frames = info['frames']
            total = frames / rk.FPS
            if total + 1e-6 < lead + speech:
                raise SystemExit(f'{bid}: narration {lead + speech:.2f}s exceeds clip {total:.2f}s')
            rk.pad_audio(mp3, REEL / f'audio/beat-{bid}.wav', lead, total)
            b['audio_file'] = f'audio/beat-{bid}.wav'
            b['actual_duration_s'] = total
            b['shot']['clip'] = info
            b['shot']['evidence_media'] = f'media/{bid}.mp4'
            clips[bid] = info
            continue
        tail = spec.get('tail', 0.0)
        total = rk.frames_for(lead + speech + tail + (0.4 if spec['kind'] in ('board', 'verdict') else 0.25)) / rk.FPS
        rk.pad_audio(mp3, REEL / f'audio/beat-{bid}.wav', lead, total)
        b['audio_file'] = f'audio/beat-{bid}.wav'
        b['actual_duration_s'] = total
        props = b['shot']['remotion']['props']
        props['durationSeconds'] = total
        if spec['kind'] == 'board':
            props['cues'] = cue_times(spec['narration'], spec['cues'], lead, speech)
            if 'still' in spec:
                b['qc'] = {'contrast_regions': [
                    {'label': 'title', 'box': [0.05, 0.03, 0.95, 0.13]},
                    {'label': 'excerpt panel', 'box': [0.055, 0.15, 0.42, 0.87]},
                    {'label': 'status banner', 'box': [0.44, 0.14, 0.945, 0.195]},
                    {'label': 'card 1 text', 'box': [0.45, 0.635, 0.94, 0.715]},
                    {'label': 'card 2 text', 'box': [0.45, 0.765, 0.94, 0.845]}],
                    'contrast_reason': ('The right column embeds a real engine frame whose pale board colours pull the '
                                        'whole-frame ink average toward the cream page; essential text is measured in '
                                        'its own regions instead. The game image itself is evidence, not typography.')}
                take, frame, label = spec['still']
                png = REEL / f'evidence/{bid}-{take}-f{frame}.png'
                if take == 'hud':   # D-02: HUD bottom-left of take defeat frame 250, cropped and enlarged
                    tmp = REEL / 'evidence/_full.png'
                    rk.still('defeat', 250, tmp)
                    im = Image.open(tmp).crop((0, 1860, 1100, 2140))
                    im.resize((im.width * 2, im.height * 2), Image.NEAREST).save(png)
                    tmp.unlink()
                    take, frame = 'defeat', 250
                else:
                    rk.still(take, frame, png)
                props['image'] = rk.data_uri(png)
                evidence.append({'path': f'evidence/{png.name}', 'sha256': rk.sha256(png),
                                 'method': f'engine viewport frame {frame} of take "{take}" (scripted input, '
                                           f'build cffbb01)' + (', cropped to the HUD and enlarged 2x' if 'hud' in png.name else ''),
                                 'supports': f'{bid}: {label}'})
    # copy the takes used as evidence into the reel and hash them
    for take in sorted({s['take'] for s in BEATS if s['kind'] == 'clip'}):
        for suffix in ('.mp4', '-inputs.jsonl'):
            src = rk.TAKES / f'{take}{suffix}'
            dst = REEL / f'capture/{take}{suffix}'
            link_or_copy(src, dst)
        evidence.append({'path': f'capture/{take}.mp4', 'sha256': rk.sha256(REEL / f'capture/{take}.mp4'),
                         'method': 'scripted-input capture of the real main scene; engine viewport saved per '
                                   'frame at --fixed-fps 30, native 3840x2160 (see CAPTURE.md)',
                         'supports': f'gameplay clips cut from take "{take}"; input log capture/{take}-inputs.jsonl'})
    for bid, info in clips.items():
        p = REEL / f'media/{bid}.mp4'
        evidence.append({'path': f'media/{bid}.mp4', 'sha256': rk.sha256(p),
                         'method': f'exact-frame cut of take "{info["take"]}": {json.dumps(info["segments"])}',
                         'supports': f'{bid}: shown gameplay ({specs[bid]["sections"][0]})'})
    gdd_bytes = GDD.read_bytes()
    gdd_copy = REEL / 'evidence/GDD.md'
    gdd_copy.write_bytes(gdd_bytes)
    evidence.append({'path': 'evidence/GDD.md', 'sha256': rk.sha256(gdd_copy),
                     'method': 'byte copy of the source GDD at film build time', 'supports': 'every excerpt'})
    headings = [l[3:].strip() for l in LINES if l.startswith('## ')]
    cover = {h: [] for h in headings}
    for s in BEATS:
        for sec in s.get('sections', []):
            cover[sec].append(s['id'])
    ledger = {'schema_version': 1,
              'document': {'path': 'GDD.md', 'sha256': rk.sha256(GDD),
                           'version': 'v0.1 agent draft, unapproved', 'build_id': rk.BUILD_ID},
              'sections': [{'heading': h, 'beat_ids': ids} for h, ids in cover.items()],
              'excerpts': [{'beat_id': s['id'], 'start_line': s['lines'][0], 'end_line': s['lines'][1],
                            'text': excerpt(*s['lines'])} for s in BEATS if s['kind'] == 'board'],
              'evidence': evidence}
    missing = [h for h, ids in cover.items() if not ids]
    if missing:
        raise SystemExit(f'uncovered sections: {missing}')
    (REEL / 'gdd-evidence.json').write_text(json.dumps(ledger, indent=1, ensure_ascii=False) + '\n')
    sheet_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
    for b in sheet['beats']:
        print(f"{b['beat_id']:4} {b['act']:8} {b['actual_duration_s']:7.2f}s  speech {b['kokoro_duration_s']:6.2f}s")
    print('total', round(sum(b['actual_duration_s'] for b in sheet['beats']), 1), 's')


if __name__ == '__main__':
    {'author': author, 'finish': finish}[sys.argv[1]]()
