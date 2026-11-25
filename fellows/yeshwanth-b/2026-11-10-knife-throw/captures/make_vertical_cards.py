"""Replace the fine-print portrait Remotion boards in the three Gino: Knife Throw
vertical sheets with native large-type portrait cards (portrait_cards.py).

    python3 make_vertical_cards.py [reel:beat ...]     # default: every beat listed below

Quotes are verbatim substrings of GDD.md (markdown ** and ` removed for display only);
code lines are exact lines of the game source at build cffbb01, picked from each
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
GODOT = PKG / 'knife-throw-platformer-godot-completed'
GDD_LINES = (Y / 'claude-liam-knife-throw-gdd/GDD.md').read_text().splitlines()
PLAIN_GDD = ' '.join(' '.join(l.replace('**', '').replace('`', '') for l in GDD_LINES).split())


def q(text):
    if ' '.join(text.split()) not in PLAIN_GDD:
        raise ValueError(f'not verbatim in GDD.md: {text!r}')
    return text


def evid(reel, name):
    return Y / f'claude-liam-knife-throw-{reel}' / 'evidence' / name


GDD = {
 'B02': dict(title='How the Document Labels a Claim', status='COMPARISON · built ≠ observed ≠ approved',
             quote=q('No human has signed off any section, and nobody has playtested the game by hand.'),
             source_label='GDD.md · line 8',
             cards=[('Observed', 'playtest passes · 46 film assertions'), ('Pending', '0 human playtests')], cue_idx=[2, 3]),
 'B03': dict(title='A Vision Nobody Signed', status='PROPOSED vision · audience PENDING',
             quote=q('Take Gino home through three hostile valleys with a sword, three knives and three hearts'),
             source_label='GDD.md · line 37', cards=[('Commit to the combo', '20 + 20 + 20 + 40 = 100 HP')], cue_idx=[2]),
 'B05': dict(title='Goals Nobody Has Tested', status='PROPOSED · 4 goals · all PENDING',
             quote=q('A first-time player finishes Rocky Outskirts on the first try'),
             source_label='GDD.md · line 61', cards=[('Scripted run', '0:43, 0 hits, but it sees everything')], cue_idx=[0]),
 'B06': dict(title='Faster Than Unity, on Purpose', status='SOURCE vs IMPLEMENTED',
             quote=q("run 105 px/s (6.5 tiles/s, tuned up from Unity's 3 units/s)"),
             source_label='GDD.md · line 70', cards=[('Godot', 'coyote 0.1 s · buffer 0.12 s')], cue_idx=[2]),
 'B08': dict(title='Four Hits, a Hundred Health', status='SOURCE chain · AUTHORED finisher',
             quote=q('Attack4 deals 40 (AUTHORED), so a full combo defeats a 100 HP enemy.'), source_label='GDD.md · line 74',
             cards=[('Unity · AttackTrigger.cs', 'dmg = 20, every hit'), ('Rebuild', '20 · 20 · 20 · 40')], cue_idx=[1, 2]),
 'B10': dict(title='Three Knives, Thirty Damage', status='SOURCE rules · IMPLEMENTED numbers',
             quote=q('420 px/s for 1.3 s (about 546 px), 30 damage, breaks on rock or an enemy.'), source_label='GDD.md · line 78',
             cards=[('Unity · KnifeMove.cs', 'flies straight · cap 3')], cue_idx=[0]),
 'B12': dict(title='Every Enemy Has a Tell', status='SOURCE behaviour · AUTHORED health',
             quote=q('100 HP and 25 points per enemy are AUTHORED.'), source_label='GDD.md · line 88',
             cards=[('Tells', 'bite 0.2 s · orb 0.7 s · rear up 0.6 s')], cue_idx=[0]),
 'B14': dict(title='Six Halves, Three Hearts', status='SOURCE vs AUTHORED',
             quote=q('an enemy hit costs 2 (a heart), spikes 1 (half a heart).'), source_label='GDD.md · line 92',
             cards=[('Unity', 'maxHealth = 6 · HeartUI halves')], cue_idx=[0]),
 'B17': dict(title='Three Levels Unity Never Had', status='AUTHORED · route-simulated',
             quote=q('Unity delivered no levels.'), source_label='GDD.md · line 103',
             cards=[('Enemies per level', '5 · 7 · 12')], cue_idx=[2]),
 'B19': dict(title='Unity Menus, Plus a Restart Key', status='SOURCE vs IMPLEMENTED',
             quote=q('R restarts from the pause or game-over menu.'), source_label='GDD.md · line 112',
             cards=[('Rebuild', 'Continue · How to Play · M · R')], cue_idx=[1]),
 'B21': dict(title='Pack Art, Synthesized Sound', status='AUTHORED world',
             quote=q('the Unity export had a SoundManager but no audio files.'), source_label='GDD.md · line 126',
             cards=[('Audio', '23 effects, 3 loops synthesized')], cue_idx=[2]),
 'B22': dict(title='One Node per Level', status='IMPLEMENTED',
             quote=q('All 6 scenes are thin.'), source_label='GDD.md · line 149',
             cards=[('level_1.tscn', 'one node · level_id = 1')], cue_idx=[0]),
 'B23': dict(title='What a Person Still Has to Decide', status='PENDING · 0 human playtests',
             quote=q("Level 3's second rope bridge stops one tile short."), source_label='GDD.md · line 157',
             cards=[('R-02', 'R on a menu: SCRIPT ERROR')], cue_idx=[0]),
}

VERDICTS = {
 ('gdd', 'B24'): dict(title='Verdict', status='Organized, not approved', quote=None, source_label='',
                      cards=[('Observed', 'menu → 3 levels → credits · pit → retry'), ('Checks', 'playtest · 46 film assertions'),
                             ('Found', 'bridge hole · R script error'), ('Pending a person', 'audience · combo · drops')]),
 ('walkthrough', 'B24'): dict(title='Verdict', status='Plays end to end, unjudged', quote=None, source_label='',
                              cards=[('Seen working', '47 features, real input'), ('Defects', 'bridge hole · R error'),
                                     ('Not shown', '4-hit combo · hearts · audio'), ('Not judged', 'fun · 0 playtests')]),
 ('gamedev', 'B28'): dict(title='Verdict', status='Readable code, two defects', quote=None, source_label='',
                          cards=[('Implemented', 'thin scenes · levels as text'), ('Good habits', 'substepped knives · ledge-aware walkers'),
                                 ('Defects', 'level.gd:761 · bridge hole'), ('Not judged', 'fun · 0 playtests')]),
}

TREE_CARDS = {
 'B02': dict(kind='code', title='Saved Scene vs. Live Tree', path='live tree · probed at runtime', src='tree',
             lines=[(1, 'Level1  level.gd'), (2, 'background layer'), (3, 'World:'), (4, '  tile map · 3 rock bodies'),
                    (5, '  61 props · 13 pickups'), (6, '  Gino + 5 enemies'), (7, 'camera'), (8, 'CanvasLayer: HUD'),
                    (9, 'CanvasLayer: menus')],
             source_label='evidence/tree_probe.txt', note='Saved scene: 1 node. Live: 200.',
             cues=[(2.0, 1), (7.0, 3), (11.0, 6), (17.0, 8)]),
 'B27': dict(kind='code', title='The Rest of the Project', path='res:// · file listing', src='tree',
             lines=[(1, 'scenes/  6 thin .tscn'), (2, 'menus · How to Play · credits'), (3, '14 .gd + 1 shader'),
                    (4, 'assets/  100 files'), (5, '_tools/  levels.py · playtest'), (6, '  steers via a hook')],
             source_label='file listing of the project', note='The captures pressed keys.',
             cues=[(3.0, 2), (10.0, 4), (18.0, 5)]),
}


def landscape(reel):
    return json.loads((Y / f'claude-liam-knife-throw-{reel}' / 'beat_sheet.json').read_text())


def write_card(reel, bid, spec):
    vdir = Y / f'claude-liam-knife-throw-{reel}' / 'vertical'
    sheet_path = vdir / 'beat_sheet.json'
    sheet = json.loads(sheet_path.read_text())
    beat = next(b for b in sheet['beats'] if b['beat_id'] == bid)
    land = next(b for b in landscape(reel)['beats'] if b['beat_id'] == bid)
    props = land['shot'].get('remotion', {}).get('props', {})
    nframes = math.ceil(beat['actual_duration_s'] * pc.FPS - 1e-8)
    if spec.get('kind') == 'code':
        for attempt in (spec, dict(spec, note=None), dict(spec, note=None, lines=spec['lines'][:3])):
            try:
                pc.code_frames(attempt, None)
            except ValueError:
                continue
            if attempt is not spec:
                print(f'  {reel} {bid}: code card shortened to fit (note dropped, {len(attempt["lines"])} lines)')
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
                    'portrait_card': {'renderer': 'knife-throw-captures/portrait_cards.py',
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
PORTRAIT_NOTE = {'B25': 1}   # the defect note, not the pause note
PORTRAIT_LINES = {'B25': [760, 761]}
SPARSE = {('gamedev', 'B27'): 'File-tree summary card: six short lines at reading size; the negative space is the layout.'}


def gamedev_code_cards():
    """Each code beat: the exact source lines its landscape cues point at."""
    sys.path.insert(0, str(Y / 'claude-liam-knife-throw-gamedev'))
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
