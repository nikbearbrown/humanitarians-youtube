"""Replace the fine-print portrait Remotion boards in the three Basketball Blaster
vertical sheets with native large-type portrait cards (portrait_cards.py).

    python3 make_vertical_cards.py [reel:beat ...]     # default: every beat listed below

Quotes are verbatim substrings of GDD.md (markdown ** and ` removed for display only);
code lines are exact lines of the game source at build 8f86cc8, picked from each
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
GODOT = PKG / 'basketball-game-godot-completed'
GDD_LINES = (PKG / 'GDD.md').read_text().splitlines()
PLAIN_GDD = ' '.join(' '.join(l.replace('**', '').replace('`', '') for l in GDD_LINES).split())


def q(text):
    if ' '.join(text.split()) not in PLAIN_GDD:
        raise ValueError(f'not verbatim in GDD.md: {text!r}')
    return text


def evid(reel, name):
    return Y / f'claude-liam-basketball-{reel}' / 'evidence' / name


GDD = {
 'B02': dict(title='How the Document Labels a Claim', status='COMPARISON · built ≠ observed ≠ approved',
             quote=q('A mechanic can be IMPLEMENTED and OBSERVED while its player-experience claim stays PENDING.'),
             source_label='GDD.md · line 25',
             cards=[('Observed', '2 takes · 59 of 59 assertions'), ('Pending', '0 human playtests')], cue_idx=[2, 3]),
 'B03': dict(title='A Vision Nobody Wrote Down', status='PENDING · vision unsigned',
             quote=q('No document says who the game is for or why someone should play it.'),
             source_label='GDD.md · line 47', cards=[('Proposed as vision', 'a short, loud arena shooter')], cue_idx=[1]),
 'B05': dict(title='Goals Nobody Has Approved', status='PROPOSED · 4 goals, none approved',
             quote=q('On this build, rushing the eggs beats fighting.'), source_label='GDD.md · line 82',
             cards=[('PX-03 · fighting pays', '25.6 s: 10 kills, 0 eggs')], cue_idx=[1]),
 'B06': dict(title='The Jetpack Unity Never Wired Up', status='AUTHORED in the port',
             quote=q('PlayerInput.cs:44 declares public bool Jetpack; and no Unity script reads it.'),
             source_label='GDD.md · line 106',
             cards=[('Godot · player.gd', 'Shift · 1.6 s fuel · 430 px/s'), ('Also authored', 'coyote 0.15 s · fire 0.4 s')],
             cue_idx=[1, 2]),
 'B08': dict(title='Three at Once', status='SOURCE + IMPLEMENTED',
             quote=q('Three or more chickens dying before the next physics frame triggers "MEGA KILL!"'),
             source_label='GDD.md · line 175',
             cards=[('Unity · AudioManager.cs', 'megaKillAmount = 3'), ('Observed', 'take campaign, frame 1795')],
             cue_idx=[0, 2]),
 'B10': dict(title='How Forgiving a Hit Is', status='IMPLEMENTED · gate-clearing AUTHORED',
             quote=q('Chickens within 260 px of the gate are removed so the respawn is fair'),
             source_label='GDD.md · line 153',
             cards=[('Per life', '3 health · 1 s safe after a hit'), ('Respawn', '2 s safe · gate cleared')], cue_idx=[0, 1]),
 'B12': dict(title='No Tests, One Distance Check', status='IMPLEMENTED · no automated tests',
             quote=q('Automated tests: none exist in the project.'), source_label='GDD.md · line 258',
             cards=[('Contact', 'distance under 58 px, every frame'), ('Film checks', 'smoke run · 59 assertions')],
             cue_idx=[1, 3]),
 'B13': dict(title='Difficulty Is One Table', status='IMPLEMENTED ramp · feel PENDING',
             quote=q('Each one is wider and has more pipes, faster spawns, a higher chicken cap and more eggs.'),
             source_label='GDD.md · line 192', image=evid('gdd', 'B13-campaign-f4300.png'), image_width=1944,
             cards=[('Autopilot egg time', '12.6 s · 13.6 s · 18.7 s')], cue_idx=[1]),
 'B15': dict(title='Eight Lines of Story', status='IMPLEMENTED · AUTHORED',
             quote=q('COACH explains the controls; MR. BLOCK replies.'), source_label='GDD.md · line 214',
             cards=[('UI', 'menu · HUD · pause · end cards')], cue_idx=[1]),
 'B17': dict(title='Whose Art Is This?', status='PENDING · art rights unrecorded',
             quote=q('Rights and authorship of that art are not recorded anywhere in this folder'),
             source_label='GDD.md · line 239',
             cards=[('Audio', 'synthesized for the port'), ('Not in this build', 'saves · settings · online')], cue_idx=[0, 2]),
 'B18': dict(title='What a Person Still Has to Decide', status='PENDING · 6 open questions',
             quote=q('the briefing prompt says "ENTER / CLICK TO CONTINUE", but clicking never advances it.'),
             source_label='GDD.md · line 264',
             cards=[('OQ-01 · OQ-02', 'Who is it for? Should fighting pay?')], cue_idx=[0]),
}

VERDICTS = {
 ('gdd', 'B19'): dict(title='Verdict', status='Organized, not approved', quote=None, source_label='',
                      cards=[('Built and observed', '3 arenas, every mechanic'), ('Machine checks', '59 of 59 assertions'),
                             ('Found', 'dead click · HUD overlap'), ('Pending a person', 'vision · art rights · playtest')]),
 ('walkthrough', 'B16'): dict(title='Verdict', status='Plays end to end, unjudged', quote=None, source_label='',
                              cards=[('Seen working', 'every move, weapon and screen'), ('Defects', 'dead click · HUD overlap'),
                                     ('Design question', 'eggs beat fighting'), ('Not judged', 'fun · 0 playtests')]),
 ('gamedev', 'B30'): dict(title='Verdict', status='Readable code, two screen bugs', quote=None, source_label='',
                          cards=[('Implemented', '8 thin scenes, data tables'), ('Good habits', 'signals · one shader, two jobs'),
                                 ('Defects', 'shade eats clicks · bars overlap'), ('Missing', 'tests · 0 human playtests')]),
}

TREE_CARDS = {
 'B02': dict(kind='code', title='Saved Scene vs. Live Tree', path='live tree · probed at runtime', src='tree',
             lines=[(1, 'Level1  game.gd'), (2, 'World'), (3, '  Backdrop · Decals · Actors'), (4, '  Projectiles · Effects'),
                    (5, '  12 platforms · 3 spotlights'), (6, '  5 nests · Camera2D'), (7, 'CanvasLayer  HUD'),
                    (8, 'CanvasLayer  fade')],
             source_label='evidence/tree_probe.txt', note='Saved scene: 1 node. game.gd builds ~100 more.',
             cues=[(2.0, 1), (6.0, 2), (11.0, 5), (15.0, 7)]),
 'B29': dict(kind='code', title='The Rest of the Project', path='res:// · file listing', src='tree',
             lines=[(1, 'scenes/  8 thin .tscn'), (2, 'menus · end_screen.gd'), (3, 'audio.gd  13 sounds'),
                    (4, 'assets/audio  14 .wav'), (5, 'effects.gd  static FX'), (6, '56 images · 3 fonts'),
                    (7, 'unused: 6 images, 1 font'), (8, 'tests/  none')],
             source_label='file listing of the project', note='No test folder at all.',
             cues=[(3.0, 2), (9.0, 4), (17.0, 6), (24.0, 8)]),
}


def landscape(reel):
    return json.loads((Y / f'claude-liam-basketball-{reel}' / 'beat_sheet.json').read_text())


def write_card(reel, bid, spec):
    vdir = Y / f'claude-liam-basketball-{reel}' / 'vertical'
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
                    'portrait_card': {'renderer': 'basketball-captures/portrait_cards.py',
                                      'reason': 'native 9:16 large-type card; shared 916 board fine print is below the GATE T portrait floor',
                                      'title': spec['title']},
                    'show': [{'at': 0.0, 'event': f"portrait card: {spec['title']}"}]}
    if (reel, bid) in SPARSE:
        beat['qc'] = {'sparse_by_design': True, 'sparse_reason': SPARSE[(reel, bid)]}
    sheet_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + '\n')
    print(reel, bid, nframes, 'frames,', len(states), 'states')


# The serif J of 'Jump, …' overhangs the 9:16 left safe edge by 13 px.
PORTRAIT_TITLES = {'B09': 'The Jump Handler'}
SPARSE = {('gamedev', 'B05'): 'Short code excerpt: four exact source lines at reading size; the negative space keeps them legible on a phone.',
          ('gamedev', 'B29'): 'File-tree summary card: eight short lines at reading size; the negative space is the layout.'}


def gamedev_code_cards():
    """Each code beat: the exact source lines its landscape cues point at."""
    sys.path.insert(0, str(Y / 'claude-liam-basketball-gamedev'))
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
