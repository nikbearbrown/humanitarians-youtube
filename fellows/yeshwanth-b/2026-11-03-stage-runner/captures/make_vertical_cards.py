"""Replace the fine-print portrait Remotion boards in the three Stage Runner
vertical sheets with native large-type portrait cards (portrait_cards.py).

    python3 make_vertical_cards.py [reel:beat ...]     # default: every beat listed below

Quotes are verbatim substrings of GDD.md (markdown ** and ` removed for display only);
code lines are exact lines of the game source at build d90fa19, picked from each
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
GODOT = PKG / 'stage-runner-godot-completed'
GDD_LINES = (Y / 'claude-liam-stage-runner-gdd/GDD.md').read_text().splitlines()
PLAIN_GDD = ' '.join(' '.join(l.replace('**', '').replace('`', '') for l in GDD_LINES).split())


def q(text):
    if ' '.join(text.split()) not in PLAIN_GDD:
        raise ValueError(f'not verbatim in GDD.md: {text!r}')
    return text


def evid(reel, name):
    return Y / f'claude-liam-stage-runner-{reel}' / 'evidence' / name


GDD = {
 'B02': dict(title='How the Document Labels a Claim', status='COMPARISON · built ≠ observed ≠ approved',
             quote=q('No human has signed off any section, and nobody has playtested the game by hand.'),
             source_label='GDD.md · line 8',
             cards=[('Observed', 'playtest passes · 62 film assertions'), ('Pending', '0 human playtests')], cue_idx=[2, 3]),
 'B03': dict(title='A Vision Nobody Signed', status='PROPOSED vision · audience PENDING',
             quote=q('Fly a lone wisp up three ruined streets, thin out a monster army that keeps marching, and win the city back from the Cerberus at its gate.'),
             source_label='GDD.md · line 37', cards=[('One mistake costs', '3 lives · mercy rule')], cue_idx=[3]),
 'B05': dict(title='Goals Nobody Has Tested', status='PROPOSED · 4 goals · all PENDING',
             quote=q('A first-time player clears stage 1 on the first or second try'),
             source_label='GDD.md · line 61', cards=[('Scripted run', '30.9 s, 0 hits, but it sees everything')], cue_idx=[1]),
 'B06': dict(title='Same Speed, Narrower Street', status='SOURCE vs IMPLEMENTED',
             quote=q('one Unity unit is 72 px (orthographic size 5 on a 720 px view), so 360 px/s.'),
             source_label='GDD.md · line 70', cards=[('Godot', '640 px street · focus at half speed')], cue_idx=[1]),
 'B08': dict(title='One Script, Thirteen Monsters', status='SOURCE defaults · AUTHORED roster',
             quote=q('The per-monster values are AUTHORED.'), source_label='GDD.md · line 96',
             cards=[('Unity · Enemy.cs', '3 HP · 100 points · 72 px/s'), ('Rebuild', '13 types · fall, weave, hop, hunt')], cue_idx=[0, 1]),
 'B10': dict(title='One Touch Was the Whole Game', status='SOURCE vs AUTHORED',
             quote=q('Unity ended the game on the first touch'), source_label='GDD.md · line 100',
             cards=[('Rebuild', '3 lives · 1.6 s invulnerable')], cue_idx=[1]),
 'B13': dict(title='Goals Nobody Wrote Down', status='SOURCE logic · AUTHORED values',
             quote=q('so the 2000 and 4000 goals are AUTHORED.'), source_label='GDD.md · line 112',
             cards=[('Unity · GameManager.cs', 'score ≥ goalScore → next scene')], cue_idx=[0]),
 'B14': dict(title='A Boss Unity Never Had', status='AUTHORED · OBSERVED',
             quote=q('110 HP and worth 5000 points.'), source_label='GDD.md · line 116',
             cards=[('Cycle', 'fan 5 → ring 12 → fan 5 → 2 minions'), ('Enraged at 55 HP', 'fans of 7 · rings of 16')], cue_idx=[1, 2]),
 'B16': dict(title='Restart Means This Stage', status='SOURCE vs IMPLEMENTED',
             quote=q("Unity's RestartGame() always loaded StageOne."), source_label='GDD.md · line 126',
             cards=[('Rebuild', 'restart reloads the current stage')], cue_idx=[1]),
 'B18': dict(title='Painted Streets, Synthesized Sound', status='AUTHORED world',
             quote=q('It alternates with a vertically mirrored copy, so the seam always matches.'), source_label='GDD.md · line 138',
             cards=[('Audio', 'none in the source · all synthesized')], cue_idx=[2]),
 'B19': dict(title='Seven Lines, 113 Nodes', status='IMPLEMENTED',
             quote=q('All 7 scenes are thin; their nodes are built in code.'), source_label='GDD.md · line 170',
             cards=[('stage_1.tscn', '7 lines → 113 live nodes')], cue_idx=[1]),
 'B20': dict(title='What a Person Still Has to Decide', status='PENDING · 0 human playtests',
             quote=q('the code uses ±288 px, which is 4 units.'), source_label='GDD.md · line 181',
             cards=[('R-01', 'R on the pause menu: SCRIPT ERROR')], cue_idx=[0]),
}

VERDICTS = {
 ('gdd', 'B21'): dict(title='Verdict', status='Organized, not approved', quote=None, source_label='',
                      cards=[('Observed', 'menu → 3 stages → boss · defeat → retry'), ('Checks', 'playtest · 62 film assertions'),
                             ('Found', 'R script error · spawn comment'), ('Pending a person', 'audience · goals · playtest')]),
 ('walkthrough', 'B21'): dict(title='Verdict', status='Plays end to end, unjudged', quote=None, source_label='',
                              cards=[('Seen working', '40 features, real input'), ('Defect', 'R logs a script error'),
                                     ('Not shown', 'F11 · Quit · Play Again · audio'), ('Not judged', 'fun · 0 playtests')]),
 ('gamedev', 'B32'): dict(title='Verdict', status='Readable code, one defect', quote=None, source_label='',
                          cards=[('Implemented', 'thin scenes · a STAGES table'), ('Good habits', 'mercy rule · hearts when needed'),
                                 ('Defect', 'game.gd:606, one line too late'), ('Not judged', 'fun · 0 playtests')]),
}

TREE_CARDS = {
 'B02': dict(kind='code', title='Saved Scene vs. Live Tree', path='live tree · probed at runtime', src='tree',
             lines=[(1, 'Stage1  game.gd'), (2, 'background:'), (3, '  2 street copies'), (4, 'world:'),
                    (5, '  player + 3 monsters'), (6, 'camera (shake)'), (7, 'CanvasLayer: HUD'), (8, 'CanvasLayer:'),
                    (9, '  banner, menus')],
             source_label='evidence/tree_probe.txt', note='Saved scene: 1 node. Live: 113.',
             cues=[(2.0, 1), (7.0, 3), (10.0, 5), (15.0, 7)]),
 'B31': dict(kind='code', title='The Rest of the Project', path='res:// · file listing', src='tree',
             lines=[(1, 'scenes/  7 thin .tscn'), (2, 'menus · How to Play'), (3, '14 .gd + 1 shader'),
                    (4, 'assets/  49 files'), (5, '_tools/  1 playtest'), (6, '  steers via a hook')],
             source_label='file listing of the project', note='The captures pressed keys.',
             cues=[(3.0, 2), (10.0, 4), (18.0, 5)]),
}


def landscape(reel):
    return json.loads((Y / f'claude-liam-stage-runner-{reel}' / 'beat_sheet.json').read_text())


def write_card(reel, bid, spec):
    vdir = Y / f'claude-liam-stage-runner-{reel}' / 'vertical'
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
                    'portrait_card': {'renderer': 'stage-runner-captures/portrait_cards.py',
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
PORTRAIT_NOTE = {'B27': 1}   # the defect note, not the pause note
PORTRAIT_LINES = {'B19': [587, 591], 'B27': [605, 606]}
SPARSE = {('gamedev', 'B31'): 'File-tree summary card: six short lines at reading size; the negative space is the layout.'}


def gamedev_code_cards():
    """Each code beat: the exact source lines its landscape cues point at."""
    sys.path.insert(0, str(Y / 'claude-liam-stage-runner-gamedev'))
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
