"""Replace the fine-print portrait Remotion boards in the three Fantasy Survival Crafting
vertical sheets with native large-type portrait cards (portrait_cards.py).

    python3 make_vertical_cards.py [reel:beat ...]     # default: every beat listed below

Quotes are verbatim substrings of GDD.md (markdown ** and ` removed for display only);
code lines are exact lines of the game source at build a514438, picked from each
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
GODOT = PKG / 'fantasy-survival-crafting-godot'
GDD_LINES = (GODOT / 'submission/GDD.md').read_text().splitlines()
PLAIN_GDD = ' '.join(' '.join(l.replace('**', '').replace('`', '') for l in GDD_LINES).split())


def q(text):
    if ' '.join(text.split()) not in PLAIN_GDD:
        raise ValueError(f'not verbatim in GDD.md: {text!r}')
    return text


def evid(reel, name):
    return Y / f'claude-liam-fantasy-{reel}' / 'evidence' / name


GDD = {
 'B02': dict(title='How the Document Labels a Claim', status='COMPARISON · built ≠ observed ≠ approved',
             quote=q('No human has signed off any section, and nobody has playtested the game by hand.'),
             source_label='GDD.md · line 8',
             cards=[('Observed', '42 game checks · 74 film assertions'), ('Pending', '0 human playtests')], cue_idx=[2, 3]),
 'B03': dict(title='A Vision Nobody Signed', status='PROPOSED vision · audience PENDING',
             quote=q('Wake in an abandoned valley, gather and craft through one afternoon, and keep a fire burning until dawn.'),
             source_label='GDD.md · line 37', cards=[('The clock is the enemy', 'dusk at 20:00 · cold at night')], cue_idx=[2]),
 'B05': dict(title='Goals Nobody Has Tested', status='PROPOSED · 4 goals · all PENDING',
             quote=q('A first-time player places the campfire before 20:00 without reading How to Play'),
             source_label='GDD.md · line 61', cards=[('Scripted run', 'fire at 12:25, but it knew the map')], cue_idx=[0]),
 'B06': dict(title='Same Physics, Slower Feet', status='SOURCE vs IMPLEMENTED',
             quote=q('Walk speed is 5.5 m/s, sprint 8.5 m/s, jump height 1.2 m.'), source_label='GDD.md · line 70',
             cards=[('Unity', '12 m/s · jumpHeight 3')], cue_idx=[0]),
 'B08': dict(title='The Sounds Unity Never Played', status='AUTHORED · OBSERVED in motion',
             quote=q('pines take 4 axe hits, topple away from the player and leave a stump and 2 Logs.'),
             source_label='GDD.md · line 110', cards=[('Rabbits', 'flee within 5 m')], cue_idx=[2]),
 'B10': dict(title='The Clock Is the Enemy', status='AUTHORED · OBSERVED',
             quote=q('A placed campfire warms anyone within 9 m.'), source_label='GDD.md · line 117',
             cards=[('Day', '24 s per hour'), ('Night', '12 s per hour · rest 9×')], cue_idx=[0, 1]),
 'B13': dict(title='Your Body Keeps Score', status='IMPLEMENTED · tuning PROPOSED',
             quote=q('These rates are PROPOSED tuning values and are PENDING (OQ-04).'), source_label='GDD.md · line 106',
             cards=[('Damage', 'empty stat −1/s · cold −1 per 1.4 s')], cue_idx=[1]),
 'B15': dict(title='Choices the Rebuild Made', status='IMPLEMENTED · AUTHORED',
             quote=q('Dropping onto an occupied slot swaps the two items'), source_label='GDD.md · line 85',
             cards=[('Saving', 'Unity: a menu, no code · now 1 slot')], cue_idx=[1]),
 'B17': dict(title='A Valley From Asset Packs', status='AUTHORED world',
             quote=q('A procedural 260 × 260 m valley ringed by mountains.'), source_label='GDD.md · line 141',
             cards=[('Audio', 'none in the source · all synthesized')], cue_idx=[2]),
 'B18': dict(title='Six Lines, Two Thousand Nodes', status='IMPLEMENTED',
             quote=q('All 6 scenes are thin; their nodes are built in code.'), source_label='GDD.md · line 179',
             cards=[('game.tscn', '6 lines → 1,976 live nodes')], cue_idx=[0]),
 'B19': dict(title='What a Person Still Has to Decide', status='PENDING · 0 human playtests',
             quote=q('Rabbit animations were seen in stills only; a moving capture has not been reviewed.'),
             source_label='GDD.md · line 190', cards=[('New · counters', 'ticked objectives read (0/3)')], cue_idx=[1]),
}

VERDICTS = {
 ('gdd', 'B20'): dict(title='Verdict', status='Organized, not approved', quote=None, source_label='',
                      cards=[('Observed', 'new game → dawn · load → defeat'), ('Checks', '42 game · 74 film'),
                             ('Found', 'ticked objectives read 0/3'), ('Pending a person', 'audience · tuning · playtest')]),
 ('walkthrough', 'B18'): dict(title='Verdict', status='Plays end to end, unjudged', quote=None, source_label='',
                              cards=[('Seen working', 'every survival step'), ('Defect', 'objectives read 0/3'),
                                     ('Shown honestly', 'fire in water refused'), ('Not judged', 'fun · 0 playtests')]),
 ('gamedev', 'B30'): dict(title='Verdict', status='Readable code, one display bug', quote=None, source_label='',
                          cards=[('Implemented', 'thin scenes · world.gd builds all'), ('Good habits', 'one ray target · one save dict'),
                                 ('Defect', 'counter vs done flag'), ('Not judged', 'fun · 0 playtests')]),
}

TREE_CARDS = {
 'B02': dict(kind='code', title='Saved Scene vs. Live Tree', path='live tree · probed at runtime', src='tree',
             lines=[(1, 'Game  world.gd'), (2, 'Level'), (3, '  terrain · lake'), (4, '  266 props'), (5, '  82 pickups'),
                    (6, '  36 pines'), (7, '  9 rabbits'), (8, '  47 grass chunks'), (9, 'sky · sun'), (10, 'CanvasLayers:'),
                    (11, '  HUD, windows, menu')],
             source_label='evidence/tree_probe.txt', note='Saved scene: 1 node. Live: 1,976.',
             cues=[(2.0, 1), (6.0, 2), (13.0, 9)]),
 'B29': dict(kind='code', title='The Rest of the Project', path='res:// · file listing', src='tree',
             lines=[(1, 'scenes/  6 thin .tscn'), (2, 'menus · end screens'), (3, '23 .gd + 3 shaders'),
                    (4, 'assets/  185 files'), (5, '_tools/  2 playtests'), (6, '  42 checks, direct calls')],
             source_label='file listing of the project', note='The captures pressed keys.',
             cues=[(3.0, 2), (10.0, 3), (20.0, 5)]),
}


def landscape(reel):
    return json.loads((Y / f'claude-liam-fantasy-{reel}' / 'beat_sheet.json').read_text())


def write_card(reel, bid, spec):
    vdir = Y / f'claude-liam-fantasy-{reel}' / 'vertical'
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
                    'portrait_card': {'renderer': 'fantasy-captures/portrait_cards.py',
                                      'reason': 'native 9:16 large-type card; shared 916 board fine print is below the GATE T portrait floor',
                                      'title': spec['title']},
                    'show': [{'at': 0.0, 'event': f"portrait card: {spec['title']}"}]}
    if (reel, bid) in SPARSE:
        beat['qc'] = {'sparse_by_design': True, 'sparse_reason': SPARSE[(reel, bid)]}
    sheet_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
    print(reel, bid, nframes, 'frames,', len(states), 'states')


# The serif J of 'Jump, …' overhangs the 9:16 left safe edge by 13 px.
PORTRAIT_TITLES = {}
SPARSE = {('gamedev', 'B29'): 'File-tree summary card: six short lines at reading size; the negative space is the layout.'}


def gamedev_code_cards():
    """Each code beat: the exact source lines its landscape cues point at."""
    sys.path.insert(0, str(Y / 'claude-liam-fantasy-gamedev'))
    import make_sheet as gm  # noqa: E402
    out = {}
    for p in gm.PAIRS:
        src = (GODOT / p['path']).read_text().splitlines()
        nums = sorted({line for _, line, _ in p['cues']})[:4]
        lines = []
        for i, no in enumerate(nums):
            if i and no != nums[i - 1] + 1:
                lines.append((None, '…'))
            lines.append((no, src[no - 1]))
        land = next(b for b in landscape('gamedev')['beats'] if b['beat_id'] == p['code'])
        cues = [(c['at'], c['line']) for c in land['shot']['remotion']['props']['cues']]
        label, value = p['notes'][0]
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
