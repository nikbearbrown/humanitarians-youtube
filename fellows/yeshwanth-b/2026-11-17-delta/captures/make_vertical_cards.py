"""Replace the fine-print portrait Remotion boards in the three Delta
vertical sheets with native large-type portrait cards (portrait_cards.py).

    python3 make_vertical_cards.py [reel:beat ...]     # default: every beat listed below

Quotes are verbatim substrings of GDD.md (markdown ** and ` removed for display only);
code lines are exact lines of the game source at build 25e03b2, picked from each
landscape beat's cue lines. Cue timings are reused from the landscape props, so
highlights land on the same spoken phrases. Each media file is exactly the beat's
frame count.
"""
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import portrait_cards as pc  # noqa: E402

Y = HERE.parent
PKG = Y.parent
GODOT = PKG / 'delta-godot-completed'
GDD_LINES = (Y / 'claude-liam-delta-gdd/GDD.md').read_text().splitlines()
PLAIN_GDD = ' '.join(' '.join(l.replace('**', '').replace('`', '') for l in GDD_LINES).split())


def q(text):
    if ' '.join(text.split()) not in PLAIN_GDD:
        raise ValueError(f'not verbatim in GDD.md: {text!r}')
    return text


def evid(reel, name):
    return Y / f'claude-liam-delta-{reel}' / 'evidence' / name


GDD = {
 'B02': dict(title='How the Document Labels a Claim', status='COMPARISON · built ≠ observed ≠ approved',
             quote=q('No human has signed off any section, and nobody has playtested the game by hand.'),
             source_label='GDD.md · line 8',
             cards=[('Observed', 'playtest passes · 90 film assertions'), ('Pending', '0 human playtests')], cue_idx=[2, 3]),
 'B03': dict(title='A Vision Nobody Signed', status='PROPOSED vision · audience PENDING',
             quote=q('Fold yourself between two layers of a broken station, carry energy where it is needed'),
             source_label='GDD.md · line 37', cards=[('One floor plan, two layers', 'Upper and Lower Delta, 50 m apart')], cue_idx=[1]),
 'B05': dict(title='Goals Nobody Has Tested', status='PROPOSED · 4 goals · all PENDING',
             quote=q('Players read the guardian\'s strike warning and get clear'),
             source_label='GDD.md · line 63', cards=[('Scripted run', 'read the timers, not the warning')], cue_idx=[1]),
 'B06': dict(title='The Starter Controller, Ported', status='SOURCE vs IMPLEMENTED',
             quote=q('mouse look at 0.11° per pixel × sensitivity'),
             source_label='GDD.md · line 70', cards=[('Godot', 'same speeds · coyote 0.1 s')], cue_idx=[1]),
 'B08': dict(title='One Ray, Two Keys', status='SOURCE ray · IMPLEMENTED keys',
             quote=q('F or the left mouse button picks up and drops'), source_label='GDD.md · line 74',
             cards=[('Unity', 'interactionDistance = 3')], cue_idx=[0]),
 'B10': dict(title='Fifty Metres, Unless Something Is There', status='SOURCE shift · AUTHORED refusal',
             quote=q('if the other layer has no floor at that spot or something solid is in the way'), source_label='GDD.md · line 78',
             cards=[('Unity', 'would leave you stuck in a wall')], cue_idx=[2]),
 'B12': dict(title='Eleven Devices, One Currency', status='SOURCE devices · IMPLEMENTED',
             quote=q('throws a charged cell back with a 0.3 s arc; a flat cell passes'), source_label='GDD.md · line 89',
             cards=[('Energy cell', '3000 · 750 in, 1500 out per second')], cue_idx=[0]),
 'B14': dict(title='Falls Are Forgiven, Plasma Is Not', status='SOURCE vs IMPLEMENTED',
             quote=q('falling off a deck returns the player to the last checkpoint'), source_label='GDD.md · line 98',
             cards=[('Plasma or a strike', 'restarts the level')], cue_idx=[1]),
 'B16': dict(title="Unity's Clock, a New Arena", status='SOURCE timings · AUTHORED layout',
             quote=q('attacks start 17 s in, then every 20 s.'), source_label='GDD.md · line 101',
             cards=[('Strike', 'follow 5 s · lock 3 s · 3 m'), ('Arena', 'generators · vault · shield')], cue_idx=[1, 3]),
 'B18': dict(title='Twelve Levels Unity Never Had', status='AUTHORED',
             quote=q('Unity delivered no levels.'), source_label='GDD.md · line 121',
             cards=[('One idea each', 'Cold Start → Delta')], cue_idx=[2]),
 'B20': dict(title='A Pause Menu That Ignores You', status='SOURCE vs IMPLEMENTED',
             quote=q('Pause (Esc or P): Resume, Restart level [R], Skip level [N], Options, Main menu.'), source_label='GDD.md · line 127',
             cards=[('Captured', 'clicks and R / N do nothing')], cue_idx=[1]),
 'B22': dict(title='Kit Art, Synthesized Sound', status='AUTHORED world',
             quote=q('the Unity export had an AudioManager but no audio files.'), source_label='GDD.md · line 139',
             cards=[('Audio', '33 effects, 3 music tracks synthesized')], cue_idx=[2]),
 'B23': dict(title='One Node per Level', status='IMPLEMENTED',
             quote=q('Every level scene is one node running level.gd with a level_id'), source_label='GDD.md · line 159',
             cards=[('level_01.tscn', 'one node · level_id = 1')], cue_idx=[0]),
 'B24': dict(title='What a Person Still Has to Decide', status='PENDING · 0 human playtests',
             quote=q('The pause menu ignores mouse clicks.'), source_label='GDD.md · line 166',
             cards=[('R-02', 'R, N and Esc dead while paused')], cue_idx=[0]),
}

VERDICTS = {
 ('gdd', 'B25'): dict(title='Verdict', status='Organized, not approved', quote=None, source_label='',
                      cards=[('Observed', 'menu → 12 levels → ending · failures'), ('Checks', 'playtest · 90 film assertions'),
                             ('Found', 'pause clicks · pause keys · shuttle'), ('Pending a person', 'audience · voice · level 12')]),
 ('walkthrough', 'B43'): dict(title='Verdict', status='Plays end to end, unjudged', quote=None, source_label='',
                              cards=[('Seen working', '51 features, real input'), ('Defects', 'pause clicks · pause keys'),
                                     ('Not shown', 'pad shift · strike death · audio'), ('Not judged', 'fun · 0 playtests')]),
 ('gamedev', 'B30'): dict(title='Verdict', status='Readable code, two pause defects', quote=None, source_label='',
                          cards=[('Implemented', 'thin scenes · levels as text'), ('Good habits', 'shift refusal · one copy'),
                                 ('Defects', 'hud.gd:316 · level.gd:804'), ('Not judged', 'fun · 0 playtests')]),
}

TREE_CARDS = {
 'B02': dict(kind='code', title='Saved Scene vs. Live Tree', path='live tree · probed at runtime', src='tree',
             lines=[(1, 'Level01  level.gd'), (2, 'environment · sun'), (3, 'Items: the cell'), (4, 'UpperDelta:'),
                    (5, '  walls · 41 meshes · 18 lamps'), (6, '  socket · door · lift'), (7, 'HUD  hud.gd'),
                    (8, 'Player + camera')],
             source_label='evidence/tree_probe.txt', note='Saved scene: 1 node. Live: 604.',
             cues=[(2.0, 1), (7.0, 3), (10.0, 4), (15.0, 8)]),
 'B29': dict(kind='code', title='The Rest of the Project', path='res:// · file listing', src='tree',
             lines=[(1, 'scenes/  15 thin .tscn'), (2, 'menus · How to play · credits'), (3, '27 .gd + 3 shaders'),
                    (4, 'assets/  239 files'), (5, '_tools/  converter · playtest'), (6, '  steers via a hook')],
             source_label='file listing of the project', note='The captures pressed keys.',
             cues=[(3.0, 2), (10.0, 4), (18.0, 5)]),
}


def landscape(reel):
    return json.loads((Y / f'claude-liam-delta-{reel}' / 'beat_sheet.json').read_text())


def write_card(reel, bid, spec):
    vdir = Y / f'claude-liam-delta-{reel}' / 'vertical'
    sheet_path = vdir / 'beat_sheet.json'
    sheet = json.loads(sheet_path.read_text())
    beat = next(b for b in sheet['beats'] if b['beat_id'] == bid)
    land = next(b for b in landscape(reel)['beats'] if b['beat_id'] == bid)
    props = land['shot'].get('remotion', {}).get('props', {})
    nframes = math.ceil(beat['actual_duration_s'] * pc.FPS - 1e-8)
    if spec.get('kind') == 'code':
        tries = [spec, dict(spec, note=None)]
        tries += [dict(spec, mono=m, **n) for m in (124, 104, 88) for n in ({}, {'note': None})]
        tries += [dict(spec, note=None, lines=spec['lines'][:3])]
        for attempt in tries:
            try:
                pc.code_frames(attempt, None)
            except ValueError:
                continue
            if attempt is not spec:
                print(f'  {reel} {bid}: code card fitted (mono {attempt.get("mono", pc.F_MONO)}, note {"kept" if attempt.get("note") else "dropped"}, {len(attempt["lines"])} of {len(spec["lines"])} lines)')
            spec = attempt
            break
        lines = spec['lines']
        shown = {n for n, _ in lines if n}
        states = [(0.0, pc.code_frames(spec, None))]
        for at, line in sorted(spec['cues']):
            if line in shown:
                states.append((at, pc.code_frames(spec, line)))
    else:
        if 'cue_idx' in spec:
            cue_times = [props['cues'][i]['at'] for i in spec['cue_idx']]
        else:
            d = beat['actual_duration_s']
            cue_times = [1.5, d * 0.3, d * 0.55, d * 0.78][:len(spec['cards'])]
        for attempt in (spec, dict(spec, cards=spec['cards'][:1]), {k: v for k, v in dict(spec, cards=spec['cards'][:1]).items() if k != 'image'}):
            try:
                pc.board_frames(attempt, -1)
            except ValueError:
                continue
            if attempt is not spec:
                print(f'  {reel} {bid}: shortened to fit ({len(attempt["cards"])} card, image {"kept" if "image" in attempt else "dropped"})')
            spec = attempt
            break
        cue_times = cue_times[:len(spec['cards'])]
        states = [(0.0, pc.board_frames(spec, -1))]
        for i, at in enumerate(cue_times):
            states.append((at, pc.board_frames(spec, i)))
    out = vdir / f'media/{bid}.mp4'
    pc.write_states(states, nframes, out)
    beat['shot'] = {'type': 'GRAPHIC', 'source': 'own', 'treatment': 'none',
                    'portrait_card': {'renderer': 'delta-captures/portrait_cards.py',
                                      'reason': 'native 9:16 large-type card; shared 916 board fine print is below the GATE T portrait floor',
                                      'title': spec['title']},
                    'show': [{'at': 0.0, 'event': f"portrait card: {spec['title']}"}]}
    if (reel, bid) in SPARSE:
        beat['qc'] = {'sparse_by_design': True, 'sparse_reason': SPARSE[(reel, bid)]}
    sheet_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
    print(reel, bid, nframes, 'frames,', len(states), 'states')


# The serif J of 'Jump, …' overhangs the 9:16 left safe edge by 13 px.
PORTRAIT_TITLES = {}
# Cue lines too long to fit together at portrait size: show the scene-change pair only.
PORTRAIT_NOTE = {'B25': 1, 'B27': 1}   # the defect notes
PORTRAIT_LINES = {'B25': [316, 318], 'B27': [812, 813]}
SPARSE = {('gamedev', 'B29'): 'File-tree summary card: six short lines at reading size; the negative space is the layout.'}


def gamedev_code_cards():
    """Each code beat: the exact source lines its landscape cues point at."""
    sys.path.insert(0, str(Y / 'claude-liam-delta-gamedev'))
    import content as gm  # noqa: E402
    out = {}
    for p in gm.PAIRS:
        src = (GODOT / p['path']).read_text().splitlines()
        nums = PORTRAIT_LINES.get(p['code']) or sorted({line for _, line, _ in p['cues']})[:4]
        lines = []
        for i, no in enumerate(nums):
            if i and no != nums[i - 1] + 1:
                lines.append((None, '…'))
            lines.append((no, src[no - 1]))
        land = next(b for b in landscape('gamedev')['beats'] if b['beat_id'] == p['code'])
        cues = [(c['at'], c['line']) for c in land['shot']['remotion']['props']['cues']]
        label, value = p['notes'][PORTRAIT_NOTE.get(p['code'], 0)]
        out[p['code']] = dict(kind='code', title=PORTRAIT_TITLES.get(p['code'], p['title']), path=p['path'].split('/')[-1], lines=lines, strip=True,
                              source_label=f"{p['path']} · lines {p['a']}–{p['b']}", note=f'{label}: {value}', cues=cues)
    return out


if __name__ == '__main__':
    want = set(sys.argv[1:])
    jobs = [('gdd', b, s) for b, s in GDD.items()]
    jobs += [(r, b, s) for (r, b), s in VERDICTS.items()]
    jobs += [('gamedev', b, s) for b, s in TREE_CARDS.items()]
    jobs += [('gamedev', b, s) for b, s in gamedev_code_cards().items()]
    for reel, bid, spec in jobs:
        if not want or f'{reel}:{bid}' in want:
            write_card(reel, bid, spec)
