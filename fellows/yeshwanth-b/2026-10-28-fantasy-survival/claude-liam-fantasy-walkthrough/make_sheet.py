"""Builds beat_sheet.json + coverage.json for claude-liam-fantasy-walkthrough
(godot-waikthrough walker).

    python3 make_sheet.py author    # narration + shots (before Kokoro)
    python3 make_sheet.py finish    # after Kokoro: exact clips, padded audio, coverage

Gameplay beats are consecutive, non-overlapping windows of the three scripted-input
takes of the real game (build a514438). A clip is never retimed: if narration
outruns its window, the clip ends on a labelled held frame.
"""
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

sys.path.insert(0, str(REEL))
from content import *  # noqa: E402,F403  (clips, features, narration)


def bookends():
    head = [
     dict(id='B00', act='ASK', pattern='ClaudeComposerAsk',
      narration=GREETING_NARR,
      props=dict(greeting='Hola, Liam', topic='WALKER · GODOT · WALKTHROUGH', segment='Every Feature, Played',
                 command=ASK, runningText='illustrative reconstruction — not the historical prompt',
                 output=OUTPUT,
                 folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
     dict(id='B01', act='BLUF', pattern='BrutalistHesitantWriter', lead=0.8, tail=1.5,
      narration=BLUF_NARR,
      props=dict(**BLUF_PROPS, fontSize=96,
                 lineSpacing=1.3, charMs=22, mistakeRate=3, hesitateWithin=1, hesitateBetween=6,
                 seed='fantasy-walkthrough-2026-10', ink='#3D3929', accent='#D97757', bg='#FAF9F5',
                 face='serif', align='center', brandLabel='@NikBearBrown')),
    ]
    tail = [
     dict(id='B18', act='VERDICT', pattern='ClaudeVerdictArtifact',
      narration=VERDICT_NARR,
      props=dict(artifactTitle='Verdict', artifactHeading='Plays end to end, unjudged', brandLabel='@NikBearBrown',
                 artifactLines=VERDICT_LINES)),
     dict(id='B19', act='HANDOFF', pattern='ClaudeComposerAsk',
      narration=("Your turn. Paste this into Claude in your own Godot project: Use Walker on my Godot game. Write an "
                 "input-only capture script that plays one feature through real key and mouse events, asserts what "
                 "should happen on screen, and fails loudly if it doesn't. Then tell me one thing the capture can't "
                 "prove. That last part matters: a script that wins is not a player who had fun. Liam, in for Bear."),
      props=dict(greeting='Your turn.', topic='WALKER · YOUR TURN', segment='Capture One Feature',
                 command=("Use Walker on my Godot game. Write an input-only capture script that plays one feature through "
                          "real key and mouse events, asserts what should happen on screen, and fails loudly if it "
                          "doesn't. Then tell me one thing the capture can't prove."),
                 runningText='paste this into Claude…',
                 output=['Look for: inputs, not teleports.', 'Look for: an honest limit, written down.'],
                 folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
     dict(id='B20', act='OUTRO', pattern='ClaudeTitleOutro', tail=1.0,
      narration=f'{TITLE}. At Nik Bear Brown.',
      props=dict(title=TITLE, slug=SLUG, handle='@NikBearBrown', subline='')),
    ]
    return head, tail


CONTRAST_REG = [{'label': 'disclosure strip text', 'box': [0.05, 0.905, 0.58, 0.952]}]
CONTRAST_REASON = 'Gameplay beat: the frame is the real engine render (dark navy menus, pause and fade screens are game art), scaled to 90 % above a dark disclosure strip. Whole-frame sampling takes the strip as background and the game as ink. Our own essential text, the disclosure strip, is measured in its own region; the game pixels are evidence, not typography.'
QC_CLIP = {'full_bleed': True, 'full_bleed_reason': ('The engine frame (scaled to 3456x1944) runs to the top edge '
           'by design: real game pixels, not a title card. Our disclosure strip sits inside title-safe; the game HUD '
           'at the top of the frame is game UI.'),
           'contrast_regions': CONTRAST_REG, 'contrast_reason': CONTRAST_REASON}
QC_WRITER = {'sparse_by_design': True, 'sparse_reason': ('Hesitant writer: text is typed on screen over the '
             'narration, so mid-beat samples legitimately show a partial page. The finished text fills the safe '
             'area and holds for the last 1.5 s.')}


def author():
    head, tail = bookends()
    beats = []
    for spec in head + CLIPS + tail:
        b = {'beat_id': spec['id'], 'act': spec.get('act', 'BODY'), 'narration_text': spec['narration'],
             'voice': 'am_onyx', 'engine': 'kokoro',
             'estimated_duration_s': round(len(spec['narration'].split()) / 3.3, 1)}
        if 'take' in spec:
            b['shot'] = {'type': 'SCREEN', 'source': 'own', 'treatment': 'none', 'capture': spec['take'],
                         'type_note': "engine capture of the game's own UI; GATE T pixel checks exempt (see BUILD-LOG.md); overlays verified by eye",
                         'method': 'scripted-input',
                         'show': [{'at': 0.0, 'event': f"real gameplay, take '{spec['take']}', build a514438"}]}
            b['qc'] = QC_CLIP
        else:
            b['shot'] = {'type': 'GRAPHIC', 'source': 'remotion',
                         'remotion': {'pattern': spec['pattern'], 'props': dict(spec['props'])},
                         'show': [{'at': 0.0, 'event': spec['pattern']}]}
            if spec['pattern'] == 'BrutalistHesitantWriter':
                b['qc'] = QC_WRITER
        if spec.get('act') == 'OUTRO':
            b['kind'] = 'outro_voice'
            b['tail_silence_s'] = 1.0
        if spec.get('lead'):
            b['lead_silence_s'] = spec['lead']
        beats.append(b)
    sheet = {'metadata': {
        'slug': SLUG, 'title': TITLE, 'topic': 'WALKER · GODOT · WALKTHROUGH', 'skill': 'godot-waikthrough',
        'modifier': 'walker', 'channel': 'claude-liam', 'brand': 'claude-liam', 'persona': 'Liam (in for Bear)',
        'in_for_bear': True, 'voice': 'am_onyx', 'voice_kokoro': 'am_onyx', 'engine': 'kokoro',
        'palette': 'claude', 'register': 'Teardown', 'fps': 30, 'width': 3840, 'height': 2160,
        'aspect_ratio': '16:9', 'fit': 'crop', 'captions': False, 'caption_policy': 'none',
        'greeting_language': 'Spanish (Hola)',
        'audience': "makers following the channel's Claude + Walker game workflows",
        'game_build': {'commit': None, 'snapshot_sha256': rk.BUILD_ID,
                       'engine': 'Godot 4.7.2.stable.official.ed1daf0bf'},
        'note': ('godot-waikthrough walker film. Every gameplay beat is an exact-frame window of a scripted-input take '
                 'of the real game; no human playtest. Game audio was not captured; narration only. No paid calls, no upload.'),
        'tags': ['Walker', 'Godot 4', 'survival crafting', 'gameplay walkthrough', 'Claude', 'Kokoro'],
    }, 'beats': beats}
    (REEL / 'beat_sheet.json').write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
    print(f'authored {len(beats)} beats')


def finish():
    sheet_path = REEL / 'beat_sheet.json'
    sheet = json.loads(sheet_path.read_text())
    head, tail = bookends()
    specs = {s['id']: s for s in head + CLIPS + tail}
    for d in ('audio', 'capture', 'media'):
        (REEL / d).mkdir(exist_ok=True)
    windows = {}
    for b in sheet['beats']:
        bid, spec = b['beat_id'], specs[b['beat_id']]
        mp3 = REEL / f'mp3/beat-{bid}.mp3'
        speech = rk.probe_duration(mp3)
        lead = spec.get('lead', 0.0)
        b['kokoro_audio_file'] = f'mp3/beat-{bid}.mp3'
        b['kokoro_duration_s'] = round(speech, 3)
        if 'take' in spec:
            need = rk.frames_for(lead + speech + 0.5)
            take = spec['take']
            n = spec['end'] - spec['start']
            segs = [('play', spec['start'], n)]
            if need > n:
                segs.append(('hold', need - n))
            info = rk.cut_segments(take, segs, REEL / f'media/{bid}.mp4')
            total = info['frames'] / rk.FPS
            rk.pad_audio(mp3, REEL / f'audio/beat-{bid}.wav', lead, total)
            b['audio_file'] = f'audio/beat-{bid}.wav'
            b['actual_duration_s'] = total
            b['shot']['clip'] = info
            b['shot']['evidence_media'] = f'media/{bid}.mp4'
            windows[bid] = (take, (spec['start'], spec['end']))
            held = sum(s['output_frames'] for s in info['segments'] if s['kind'] == 'hold')
            if held:
                print(f'{bid}: {held} held frames ({held / 30:.1f}s) — narration outran the window')
            continue
        total = rk.frames_for(lead + speech + spec.get('tail', 0.0) + (0.4 if b['act'] == 'VERDICT' else 0.25)) / rk.FPS
        rk.pad_audio(mp3, REEL / f'audio/beat-{bid}.wav', lead, total)
        b['audio_file'] = f'audio/beat-{bid}.wav'
        b['actual_duration_s'] = total
        b['shot']['remotion']['props']['durationSeconds'] = total
    captures = {}
    for take in sorted({t for t, _ in windows.values()}):
        for suffix in ('.mp4', '-inputs.jsonl'):
            link_or_copy(rk.TAKES / f'{take}{suffix}', REEL / f'capture/{take}{suffix}')
        captures[take] = {'path': f'capture/{take}.mp4', 'sha256': rk.sha256(REEL / f'capture/{take}.mp4'),
                          'build_id': rk.BUILD_ID, 'method': 'scripted-input',
                          'input_log': f'capture/{take}-inputs.jsonl',
                          'note': 'unmodified game code; harness window config only (see CAPTURE.md)'}
    features = []
    for fid, bid, take, action, obs, riff in FEATURES:
        t, (w0, w1) = windows[bid]
        assert t == take, (fid, t, take)
        if not w0 < action < w1:
            raise SystemExit(f'{fid}: action frame {action} outside {bid} window {w0}-{w1}')
        features.append({'id': fid, 'status': 'implemented', 'evidence': [{
            'capture': take, 'beat_id': bid, 'start_s': round(w0 / 30, 3), 'action_s': round(action / 30, 3),
            'end_s': round(w1 / 30, 3), 'observation': obs, 'riff': riff}]})
    coverage = {'schema_version': 1, 'game': {'name': 'fantasy-survival-crafting', 'build_id': rk.BUILD_ID},
                'captures': captures, 'features': features,
                'not_exercised': [{'id': k, 'reason': v} for k, v in NOT_SHOWN]}
    (REEL / 'coverage.json').write_text(json.dumps(coverage, indent=1, ensure_ascii=False) + '\n')
    sheet_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
    for b in sheet['beats']:
        print(f"{b['beat_id']:4} {b['act']:8} {b['actual_duration_s']:7.2f}s  speech {b['kokoro_duration_s']:6.2f}s")
    print('total', round(sum(b['actual_duration_s'] for b in sheet['beats']), 1), 's;',
          len(FEATURES), 'features shown,', len(NOT_SHOWN), 'not exercised')


if __name__ == '__main__':
    {'author': author, 'finish': finish}[sys.argv[1]]()
