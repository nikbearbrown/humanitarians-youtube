"""Replace the fine-print portrait Remotion boards in the three Night Yard
vertical sheets with native large-type portrait cards (portrait_cards.py).

    python3 make_vertical_cards.py [reel:beat ...]     # default: every beat listed below

Quotes are verbatim substrings of GDD.md (markdown ** and ` removed for display only);
code lines are exact lines of the game source at build 54ad5ab, picked from each
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
GODOT = PKG / 'inside-godot-completed'
GDD_LINES = (Y / 'claude-liam-nightyard-gdd/GDD.md').read_text().splitlines()
PLAIN_GDD = ' '.join(' '.join(l.replace('**', '').replace('`', '') for l in GDD_LINES).split())


def q(text):
    if ' '.join(text.split()) not in PLAIN_GDD:
        raise ValueError(f'not verbatim in GDD.md: {text!r}')
    return text


def evid(reel, name):
    return Y / f'claude-liam-nightyard-{reel}' / 'evidence' / name


GDD = {
 'B02': dict(title='How the Document Labels a Claim', status='COMPARISON · built ≠ observed ≠ approved',
             quote=q('No human has signed off any section, and nobody has playtested the game by hand.'),
             source_label='GDD.md · line 8',
             cards=[('Observed', 'playtest passes · 78 film assertions'), ('Pending', '0 human playtests')], cue_idx=[2, 3]),
 'B03': dict(title='A Vision Nobody Signed', status='PROPOSED vision · audience PENDING',
             quote=q('climb the stacks, fight your way past the yard bots, and take down the Forewoman who runs it.'),
             source_label='GDD.md · line 37', cards=[('Pillars', 'stuntman · fight · read the yard')], cue_idx=[1]),
 'B05': dict(title='Goals Nobody Has Tested', status='PROPOSED · 4 goals · all PENDING',
             quote=q('The Forewoman feels like a fight, not a wall'),
             source_label='GDD.md · line 64', cards=[('Scripted run', "K.O.'d 5× by the boss")], cue_idx=[1]),
 'B06': dict(title='Walking at the Speed of the Clip', status='SOURCE vs IMPLEMENTED',
             quote=q("walk 1.65 m/s (the walking clip's stride), run 5.2 m/s"),
             source_label='GDD.md · line 70', cards=[('Catch', 'double tap on the wall clock')], cue_idx=[2]),
 'B08': dict(title='Two Metres Up, Three Across', status='SOURCE moves · IMPLEMENTED numbers',
             quote=q('so a 2 m step can be jumped onto; 3–4 m walls need the ledge grab'), source_label='GDD.md · line 74',
             cards=[('Running jump', 'clears a 3-wide gap')], cue_idx=[1]),
 'B10': dict(title='Sixteen Attacks', status='SOURCE system · IMPLEMENTED table',
             quote=q('16 attacks, each with its clip range'), source_label='GDD.md · line 79',
             cards=[('Hammer', '9.0 · unblockable · 9 s')], cue_idx=[2]),
 'B12': dict(title='An Axe You Can Throw', status='SOURCE weapons · IMPLEMENTED inputs',
             quote=q('run + attack throws it (it flies straight, spinning)'), source_label='GDD.md · line 92',
             cards=[('Unity', 'pick up · swing · throw · put down')], cue_idx=[0]),
 'B14': dict(title='A Hundred Points, a Hundred HP', status='SOURCE numbers · IMPLEMENTED plates',
             quote=q('the plate fires 0.4 s after something steps on it'), source_label='GDD.md · line 100',
             cards=[('Unity', 'maxHP 100 · maxScore 100 · light 10')], cue_idx=[0]),
 'B16': dict(title='Bots That Have to Notice You', status='SOURCE AI · AUTHORED boss',
             quote=q('bots start unaware (for takedowns)'), source_label='GDD.md · line 105',
             cards=[('The Forewoman', '12 HP · blocks · hammer')], cue_idx=[2]),
 'B18': dict(title='Six Levels Unity Never Had', status='AUTHORED',
             quote=q('Unity delivered no levels.'), source_label='GDD.md · line 118',
             cards=[('One move each', 'ledge → boss')], cue_idx=[1]),
 'B19': dict(title='Pick Your Y Bot', status='SOURCE select · IMPLEMENTED menus',
             quote=q('Character select: hover and click, or arrow keys; Play or Enter.'), source_label='GDD.md · line 124',
             cards=[('Rebuild', 'menu · select level · pause')], cue_idx=[1]),
 'B21': dict(title='Kit Art, Synthesized Sound', status='AUTHORED world',
             quote=q('the Unity export had no audio files.'), source_label='GDD.md · line 137',
             cards=[('Art', '3 rigs share 55 clips')], cue_idx=[2]),
 'B22': dict(title='One Fighter Class', status='IMPLEMENTED',
             quote=q('One CharacterBody3D class (fighter.gd) for the player and every bot'), source_label='GDD.md · line 156',
             cards=[('Flags', 'keyboard or brain · 8 the same')], cue_idx=[1]),
 'B23': dict(title='A Pause Key That Stops Pausing', status='R-01 · found while capturing',
             quote=q('After Options in the pause menu, the pause key stops pausing.'), source_label='GDD.md · line 164',
             cards=[('Cause', 'a hidden panel keeps the key')], cue_idx=[1]),
 'B25': dict(title='What a Person Still Has to Decide', status='PENDING · 0 human playtests',
             quote=q('The film captures keep player.brain empty'), source_label='GDD.md · line 173',
             cards=[('Captures', 'same brain · key presses only')], cue_idx=[1]),
}

VERDICTS = {
 ('gdd', 'B26'): dict(title='Verdict', status='Organized, not approved', quote=None, source_label='',
                      cards=[('Observed', 'menu → 6 levels → credits · failures'), ('Checks', 'playtest · 78 film assertions'),
                             ('Found', 'the pause key after Options'), ('Pending a person', 'audience · story · boss')]),
 ('walkthrough', 'B45'): dict(title='Verdict', status='Plays end to end, unjudged', quote=None, source_label='',
                              cards=[('Seen working', '55 features, real input'), ('Defects', 'pause key · arrows to Back'),
                                     ('Not shown', 'Red, Green · audio'), ('Not judged', 'fun · 0 playtests')]),
 ('gamedev', 'B32'): dict(title='Verdict', status='Readable code, two menu defects', quote=None, source_label='',
                          cards=[('Implemented', 'thin scenes · levels as text'), ('Good habits', 'one fighter class'),
                                 ('Defects', 'options_panel.gd:53 · arrows'), ('Not judged', 'fun · 0 playtests')]),
}

TREE_CARDS = {
 'B02': dict(kind='code', title='Saved Scene vs. Live Tree', path='live tree · probed at runtime', src='tree',
             lines=[(1, 'Level01  level.gd'), (2, 'environment · moon'), (3, '103 meshes: the yard'), (4, '8 solid bodies'),
                    (5, 'lamps · fire · lights'), (6, 'spike_trap.gd'), (7, '3 fighters: player + 2 bots'),
                    (8, 'HUD · camera')],
             source_label='evidence/tree_probe.txt', note='Saved scene: 1 node. Live: 385.',
             cues=[(2.0, 1), (7.0, 3), (11.0, 6), (14.0, 7)]),
 'B31': dict(kind='code', title='The Rest of the Project', path='res:// · file listing', src='tree',
             lines=[(1, 'scenes/  10 thin .tscn'), (2, 'menus · select · credits'), (3, '17 .gd · 5,215 lines'),
                    (4, 'assets/  rigs · clips · yard'), (5, '_tools/  converter · playtest'), (6, '  the brain drives')],
             source_label='file listing of the project', note='The captures pressed keys.',
             cues=[(3.0, 2), (10.0, 4), (18.0, 5)]),
}


def landscape(reel):
    return json.loads((Y / f'claude-liam-nightyard-{reel}' / 'beat_sheet.json').read_text())


def write_card(reel, bid, spec):
    vdir = Y / f'claude-liam-nightyard-{reel}' / 'vertical'
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
                    'portrait_card': {'renderer': 'inside-captures/portrait_cards.py',
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
PORTRAIT_NOTE = {'B27': 1, 'B29': 1}   # the defect notes
PORTRAIT_LINES = {}
SPARSE = {('gamedev', 'B31'): 'File-tree summary card: six short lines at reading size; the negative space is the layout.'}


def gamedev_code_cards():
    """Each code beat: the exact source lines its landscape cues point at."""
    sys.path.insert(0, str(Y / 'claude-liam-nightyard-gamedev'))
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
