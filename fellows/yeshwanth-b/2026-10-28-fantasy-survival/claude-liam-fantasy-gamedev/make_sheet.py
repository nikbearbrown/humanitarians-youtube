"""Builds beat_sheet.json + gamedev-evidence.json for claude-liam-fantasy-gamedev
(godot-gamedev walker). Teaching contract: code-then-result-v1.

    python3 make_sheet.py author    # narration + shots
    python3 make_sheet.py finish    # after Kokoro: pad audio, cut result clips, cues
    python3 make_sheet.py ledger    # after Remotion: hash media, write gamedev-evidence.json

Every code panel is read from the game's own files by line number at build time.
Every result is real engine output of the same build (a514438): a scripted-input
capture (sometimes a labelled zoom of one), never retimed.
"""
import hashlib
import json
import shutil
import sys
from pathlib import Path

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

CAPS = REEL.parent / 'fantasy-captures'
sys.path.insert(0, str(CAPS))
import reelkit as rk  # noqa: E402

GODOT = REEL.parents[1] / 'fantasy-survival-crafting-godot'
sys.path.insert(0, str(REEL))
from content import *  # noqa: E402,F403


def lines(path, a, b):
    return '\n'.join((GODOT / path).read_text().splitlines()[a - 1:b])


TREE = [l.rstrip() for l in (CAPS / 'tree_probe.txt').read_text().splitlines()[1:] if l.strip() and not l.startswith('autoload') and not l.startswith('total')]
FILES_TREE = ['res://',
              '  project.godot  3 autoloads · export_presets.cfg · README.md',
              '  scenes/   6 thin .tscn',
              '  scripts/  23 .gd + 3 shaders · 3,303 lines',
              '  assets/   185 files: models, textures, sky, ui, icons, fonts, audio',
              '  _tools/   icon baker · screenshot drivers · 2 playtests',
              '  builds/   macOS .app + Windows .exe (exports)',
              '  submission/  GDD · screenshots · verification logs']

def bookends():
    head = [
     dict(id='B00', act='ASK', pattern='ClaudeComposerAsk',
      narration=GREETING_NARR,
      props=dict(greeting='Hola, Liam', topic='WALKER · GODOT · GAMEDEV', segment='Inside the Godot Code',
                 command=ASK, runningText='illustrative reconstruction — not the historical prompt',
                 output=OUTPUT,
                 folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
     dict(id='B01', act='BLUF', pattern='BrutalistHesitantWriter', lead=0.8, tail=1.5,
      narration=BLUF_NARR,
      props=dict(text=BLUF_TEXT,
                 triggerWords='from scenes', replacementWords='in code', fontSize=96,
                 lineSpacing=1.3, charMs=22, mistakeRate=3, hesitateWithin=1, hesitateBetween=6,
                 seed='fantasy-gamedev-2026-10', ink='#3D3929', accent='#D97757', bg='#FAF9F5',
                 face='serif', align='center', brandLabel='@NikBearBrown')),
     dict(id='B02', act='BODY', pattern='GodotDevWorkbench',
      narration=TREE_NARR,
      props=dict(mode='tree', title='Saved Scene vs. Live Tree', project=PROJ,
                 source='Live tree: printed from a running instance of res://scenes/game.tscn at 2 s, headless, '
                        'no input, on an isolated copy (tree_probe.gd).',
                 treeLabel='Remote (runtime) tree — probed', tree=TREE,
                 inspectorLabel='Source notes — not Inspector values',
                 notes=[{'label': 'Saved scene (game.tscn)', 'value': '1 node: Game + world.gd'},
                        {'label': 'Live at 2 s', 'value': '1,976 nodes, all created by world.gd'},
                        {'label': 'Autoloads', 'value': 'GameState · Audio · Models'}],
                 cues=[{'at': 2.0, 'line': 1, 'label': 'the only saved node'},
                       {'at': 6.0, 'line': 2, 'label': 'Level, built in _ready'},
                       {'at': 13.0, 'line': 5, 'label': 'sky, sun, HUD, windows, menu'}])),
    ]
    tail = [
     dict(id='B29', act='BODY', pattern='GodotDevWorkbench',
      narration=REST_NARR,
      props=dict(mode='tree', title='The Rest of the Project', project=PROJ,
                 source='FileSystem summary from a file listing of the project (builds/ and .godot/ noted, not taught)',
                 treeLabel='FileSystem — res://', tree=FILES_TREE,
                 inspectorLabel='Source notes — not Inspector values',
                 notes=[{'label': 'Shaders', 'value': 'terrain · water · sky'},
                        {'label': 'Audio', 'value': 'all synthesized; the source had none'},
                        {'label': 'Tests', 'value': '2 playtests, 42 checks, call functions directly'}],
                 cues=[{'at': 3.0, 'line': 2, 'label': 'menus and end screens'},
                       {'at': 10.0, 'line': 3, 'label': 'scripts and shaders'},
                       {'at': 20.0, 'line': 5, 'label': 'tools and playtests'}])),
     dict(id='B30', act='VERDICT', pattern='ClaudeVerdictArtifact',
      narration=VERDICT_NARR,
      props=dict(artifactTitle='Verdict', artifactHeading=VERDICT_HEADING, brandLabel='@NikBearBrown',
                 artifactLines=VERDICT_LINES)),
     dict(id='B31', act='HANDOFF', pattern='ClaudeComposerAsk',
      narration=HANDOFF_NARR,
      props=dict(greeting='Your turn.', topic='WALKER · YOUR TURN', segment='Predict, Then Capture',
                 command=HANDOFF_COMMAND,
                 runningText='paste this into Claude…',
                 output=['Look for: a prediction written before the capture.',
                         'Look for: the smallest change, not a rewrite.'],
                 folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
     dict(id='B32', act='OUTRO', pattern='ClaudeTitleOutro', tail=1.0,
      narration=f'{TITLE}. At Nik Bear Brown.',
      props=dict(title=TITLE, slug=SLUG, handle='@NikBearBrown', subline='')),
    ]
    return head, tail


CONTRAST_REG = [{'label': 'disclosure strip text', 'box': [0.05, 0.905, 0.58, 0.952]}]
CONTRAST_REASON = 'Gameplay beat: the frame is the real engine render (dark navy menus, pause and fade screens are game art), scaled to 90 % above a dark disclosure strip. Whole-frame sampling takes the strip as background and the game as ink. Our own essential text, the disclosure strip, is measured in its own region; the game pixels are evidence, not typography.'
QC_CLIP = {'full_bleed': True, 'full_bleed_reason': ('The engine frame (scaled to 3456x1944) runs to the top edge by '
           'design: real game pixels, not a title card. Our disclosure strip sits inside title-safe; the game HUD at the '
           'top of the frame is game UI.'),
           'contrast_regions': CONTRAST_REG, 'contrast_reason': CONTRAST_REASON}
QC_WRITER = {'sparse_by_design': True, 'sparse_reason': ('Hesitant writer: text is typed on screen over the '
             'narration, so mid-beat samples legitimately show a partial page. The finished text fills the safe '
             'area and holds for the last 1.5 s.')}


def all_beats():
    head, tail = bookends()
    beats = list(head)
    for p in PAIRS:
        code = lines(p['path'], p['a'], p['b'])
        beats.append(dict(id=p['code'], act='BODY', pattern='GodotDevWorkbench', narration=p['narration'],
                          props=dict(mode='code', title=p['title'], project=PROJ, path=f"res://{p['path']}",
                                     source=f"{p['path']}:{p['a']}-{p['b']} at a514438 · Godot editor reconstruction",
                                     code=code, startLine=p['a'], codeFontSize=p['size'],
                                     inspectorLabel='Source notes — not Inspector values',
                                     notes=[{'label': k, 'value': v} for k, v in p['notes']],
                                     output=[f"{p['path']} · lines {p['a']}–{p['b']}"]), pair=p))
        beats.append(dict(id=p['result'], act='BODY', take=p['take'], narration=p['rnarr'], pair=p, lead=0.3,
                          **({'segments': p['segments']} if 'segments' in p else {'start': p['start'], 'end': p['end']})))
    beats += tail
    return beats


def author():
    out = []
    for spec in all_beats():
        b = {'beat_id': spec['id'], 'act': spec['act'], 'narration_text': spec['narration'],
             'voice': 'am_onyx', 'engine': 'kokoro',
             'estimated_duration_s': round(len(spec['narration'].split()) / 3.3, 1)}
        if 'take' in spec:
            b['shot'] = {'type': 'SCREEN', 'source': 'own', 'treatment': 'none', 'capture': spec['take'],
                         'method': 'scripted-input', 'zoom': bool(spec['pair'].get('zoom')),
                         'type_note': "engine capture of the game's own UI; GATE T pixel checks exempt (see BUILD-LOG.md)",
                         'show': [{'at': 0.0, 'event': f"real gameplay, take '{spec['take']}', build a514438"}]}
            b['qc'] = QC_CLIP
        else:
            b['shot'] = {'type': 'GRAPHIC', 'source': 'remotion',
                         'remotion': {'pattern': spec['pattern'], 'props': dict(spec['props'])},
                         'show': [{'at': 0.0, 'event': spec['pattern']}]}
            if spec['pattern'] == 'BrutalistHesitantWriter':
                b['qc'] = QC_WRITER
        if spec['act'] == 'OUTRO':
            b['kind'] = 'outro_voice'
            b['tail_silence_s'] = 1.0
        if spec.get('lead'):
            b['lead_silence_s'] = spec['lead']
        out.append(b)
    sheet = {'metadata': {
        'slug': SLUG, 'title': TITLE, 'topic': 'WALKER · GODOT · GAMEDEV', 'skill': 'godot-gamedev', 'modifier': 'walker',
        'channel': 'claude-liam', 'brand': 'claude-liam', 'persona': 'Liam (in for Bear)', 'in_for_bear': True,
        'voice': 'am_onyx', 'voice_kokoro': 'am_onyx', 'engine': 'kokoro', 'palette': 'claude', 'register': 'Teardown',
        'fps': 30, 'width': 3840, 'height': 2160, 'aspect_ratio': '16:9', 'fit': 'crop', 'captions': False,
        'caption_policy': 'none', 'greeting_language': 'Spanish (Hola)',
        'teaching_contract': 'code-then-result-v1',
        'audience': "makers following the channel's Claude + Walker game workflows",
        'game_build': {'commit': None, 'snapshot_sha256': rk.BUILD_ID, 'engine': 'Godot 4.7.2.stable.official.ed1daf0bf'},
        'note': ('godot-gamedev walker film. Code panels are Godot editor reconstructions with verbatim source; each is '
                 'followed by real engine output of the same build. No game change, no paid calls, no upload.'),
        'tags': ['Walker', 'Godot 4', 'GDScript', 'game development', 'survival crafting', 'Claude', 'Kokoro'],
    }, 'beats': out}
    (REEL / 'beat_sheet.json').write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
    print(f'authored {len(out)} beats')


def cue_list(narration, cues, lead, dur):
    res = []
    for phrase, line, label in cues:
        pos = narration.find(phrase)
        if pos < 0:
            raise SystemExit(f'cue phrase not found: {phrase!r}')
        res.append({'at': round(lead + dur * pos / len(narration), 2), 'line': line, 'label': label})
    return sorted(res, key=lambda c: c['at'])


def finish():
    sheet_path = REEL / 'beat_sheet.json'
    sheet = json.loads(sheet_path.read_text())
    specs = {s['id']: s for s in all_beats()}
    for d in ('audio', 'media', 'capture', 'evidence'):
        (REEL / d).mkdir(exist_ok=True)
    for b in sheet['beats']:
        bid, spec = b['beat_id'], specs[b['beat_id']]
        mp3 = REEL / f'mp3/beat-{bid}.mp3'
        speech = rk.probe_duration(mp3)
        lead = spec.get('lead', 0.0)
        b['kokoro_audio_file'] = f'mp3/beat-{bid}.mp3'
        b['kokoro_duration_s'] = round(speech, 3)
        if 'take' in spec:
            take, need = spec['take'], rk.frames_for(lead + speech + 0.5)
            if spec['pair'].get('zoom'):
                n = spec['end'] - spec['start']
                info = rk.cut_zoom(take, spec['start'], n, spec['pair']['zoom'], REEL / f'media/{bid}.mp4',
                                   hold=max(0, need - n))
            else:
                if 'segments' in spec:
                    segs = list(spec['segments'])
                    have = sum(s[2] * (s[3] if s[0] == 'replay' else 1) for s in segs)
                    k, s0, n = segs[-1][:3]
                    grow = max(0, min(rk.take_frames(take) - (s0 + n), need - have))
                    segs[-1] = (k, s0, n + grow)
                    if need - have - grow > 0:
                        segs.append(('hold', need - have - grow))
                else:
                    n = spec['end'] - spec['start']
                    segs = [('play', spec['start'], n)] + ([('hold', need - n)] if need > n else [])
                info = rk.cut_segments(take, segs, REEL / f'media/{bid}.mp4')
            total = info['frames'] / rk.FPS
            held = sum(s['output_frames'] for s in info['segments'] if s['kind'] == 'hold')
            if held:
                print(f'{bid}: {held} held frames')
            b['shot']['clip'] = info
            b['shot']['evidence_media'] = f'media/{bid}.mp4'
        else:
            total = rk.frames_for(lead + speech + spec.get('tail', 0.0) + (0.4 if b['act'] == 'VERDICT' else 0.3)) / rk.FPS
            props = b['shot']['remotion']['props']
            props['durationSeconds'] = total
            if 'pair' in spec:
                props['cues'] = cue_list(spec['narration'], spec['pair']['cues'], lead, speech)
        rk.pad_audio(mp3, REEL / f'audio/beat-{bid}.wav', lead, total)
        b['audio_file'] = f'audio/beat-{bid}.wav'
        b['actual_duration_s'] = total
    for take in sorted({s['take'] for s in specs.values() if 'take' in s}):
        for suffix in ('.mp4', '-inputs.jsonl'):
            link_or_copy(rk.TAKES / f'{take}{suffix}', REEL / f'capture/{take}{suffix}')
    for name in ('tree_probe.txt', 'tree_probe.gd'):
        shutil.copy2(CAPS / name, REEL / 'evidence' / name)
    sheet_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
    for b in sheet['beats']:
        print(f"{b['beat_id']:4} {b['act']:8} {b['actual_duration_s']:7.2f}s  speech {b['kokoro_duration_s']:6.2f}s")
    print('total', round(sum(b['actual_duration_s'] for b in sheet['beats']), 1), 's')


ROLE_BY_DIR = {'scripts': 'runtime script', 'scenes': 'scene', 'assets/audio': 'audio asset or import settings',
               'assets/fonts': 'font asset or import settings'}
EXCLUSION_REASON = 'exported build artefact (macOS app / Windows exe), not source; boot-tested separately (export-boot.log)'
SUBMISSION_REASON = 'submission documents (GDD, screenshots, verification logs); the GDD is the subject of the separate GDD film'


def ledger():
    sheet = json.loads((REEL / 'beat_sheet.json').read_text())
    inv = sorted(p.relative_to(GODOT).as_posix() for p in GODOT.rglob('*')
                 if p.is_file() and not any(x in ('.godot', '.git') for x in p.relative_to(GODOT).parts)
                 and p.suffix != '.uid')
    comp_of = {}
    for cid, (_, files, _) in COMPONENTS.items():
        for f in files:
            comp_of.setdefault(f, []).append(cid)
    for cid, prefix in (('art-assets', 'assets/'), ('tools-and-tests', '_tools/')):
        group = [p for p in inv if p.startswith(prefix)]
        COMPONENTS[cid] = (COMPONENTS[cid][0], group, COMPONENTS[cid][2])
        for p in group:
            comp_of.setdefault(p, []).append(cid)
    files, exclusions = [], []
    for path in inv:
        if path.startswith('builds/'):
            exclusions.append({'path': path, 'reason': EXCLUSION_REASON})
            continue
        if path.rsplit('/', 1)[-1] == '.DS_Store':
            exclusions.append({'path': path, 'reason': 'macOS Finder folder metadata, written after the build snapshot; not game source and not in build-files.txt'})
            continue
        if path.startswith('submission/'):
            exclusions.append({'path': path, 'reason': SUBMISSION_REASON})
            continue
        if path not in comp_of:
            raise SystemExit(f'unassociated file: {path}')
        role = next((v for k, v in ROLE_BY_DIR.items() if path.startswith(k)), None)
        if role is None:
            role = 'art asset or import settings' if path.startswith('assets/') else 'project configuration'
        files.append({'path': path, 'sha256': hashlib.sha256((GODOT / path).read_bytes()).hexdigest(),
                      'role': role, 'component_ids': comp_of[path]})
    pairs = []
    for p in PAIRS:
        media = REEL / f"media/{p['result']}.mp4"
        pairs.append({'code_beat': p['code'], 'result_beat': p['result'], 'observation': p['obs'],
                      'media': {'path': f"media/{p['result']}.mp4", 'sha256': rk.sha256(media)}})
    data = {'schema_version': 1, 'teaching_contract': 'code-then-result-v1',
            'game': {'path': '../../fantasy-survival-crafting-godot', 'build_id': rk.BUILD_ID},
            'files': files,
            'components': [{'id': cid, 'explanation': e, 'beat_ids': beats, 'files': fl}
                           for cid, (e, fl, beats) in COMPONENTS.items()],
            'excerpts': [{'beat_id': p['code'], 'path': p['path'], 'start_line': p['a'], 'end_line': p['b'],
                          'text': lines(p['path'], p['a'], p['b'])} for p in PAIRS],
            'exclusions': exclusions,
            'code_result_pairs': pairs}
    (REEL / 'gamedev-evidence.json').write_text(json.dumps(data, indent=1, ensure_ascii=False) + '\n')
    print(f'ledger: {len(files)} files, {len(exclusions)} exclusions, {len(pairs)} pairs')


if __name__ == '__main__':
    {'author': author, 'finish': finish, 'ledger': ledger}[sys.argv[1]]()
