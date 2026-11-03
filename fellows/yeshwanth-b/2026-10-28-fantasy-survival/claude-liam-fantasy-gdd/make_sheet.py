"""Builds beat_sheet.json for claude-liam-fantasy-gdd (godot-gdd walker).

    python3 make_sheet.py author    # narration + shots (run before Kokoro)
    python3 make_sheet.py finish    # after Kokoro: pad audio, cut clips, cues, ledger

Every excerpt is read from the game's own submission/GDD.md by line number at build
time, so the screen can only show what the document says. Gameplay comes only from
the scripted-input takes in ../fantasy-captures (same build, a514438).
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

CAPS = REEL.parent / 'fantasy-captures'
sys.path.insert(0, str(CAPS))
import reelkit as rk  # noqa: E402

PKG = REEL.parents[1]
GDD = PKG / 'fantasy-survival-crafting-godot/submission/GDD.md'
SLUG = 'claude-liam-fantasy-gdd'
TITLE = 'Fantasy Survival Crafting: The Design Document Came Last'
LINES = GDD.read_text().splitlines()


def excerpt(a, b):
    return '\n'.join(LINES[a - 1:b])


SRC = 'GDD.md · Fantasy Survival Crafting @ a514438 · agent-drafted v0.1, unapproved'

ASK_COMMAND = ('Please use Walker to convert my game design document about a first-person survival-crafting game — '
               'wake in an abandoned valley, gather sticks, gold and stone, craft an axe and a campfire, and survive '
               'one night until dawn — into a playable Godot project.')

BEATS = [
 dict(id='B00', act='ASK', kind='composer',
  narration=("Hola, this is Liam, in for Bear. This is how Walker is meant to be asked: hand it a game design document, "
             "get back a playable Godot project. The prompt on screen is a reconstruction, not a transcript, because this "
             "game was rebuilt first, and its document came after."),
  props=dict(greeting='Hola, Liam', topic='WALKER · GODOT · GDD', segment='The Design Document',
             command=ASK_COMMAND, runningText='illustrative reconstruction — not the historical prompt',
             output=['What happened: a partial Unity prototype was rebuilt in Godot first.',
                     'GDD.md was written afterwards, from the evidence.'],
             folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
 dict(id='B01', act='BLUF', kind='writer', lead=0.8, tail=1.5,
  narration=("Fantasy Survival Crafting came before its design document. It rebuilds a Unity prototype that had no scenes, "
             "no audio and no way to win, and completes it into one night of survival. The document was written last, and "
             "nothing in it is signed off."),
  props=dict(text=("Fantasy Survival Crafting\nwas built from its design document.\n"
                   "It finishes a Unity prototype\ninto one night of survival.\n"
                   "The document was written last,\nand nothing in it is signed off."),
             triggerWords='was built from', replacementWords='came before',
             fontSize=92, lineSpacing=1.3, charMs=22, mistakeRate=3, hesitateWithin=1, hesitateBetween=6,
             seed='fantasy-gdd-2026-10', ink='#3D3929', accent='#D97757', bg='#FAF9F5', face='serif',
             align='center', brandLabel='@NikBearBrown')),
 dict(id='B02', act='BODY', kind='board', status='comparison',
  sections=['Status vocabulary', '1. Metadata'], lines=(8, 8),
  narration=("The document opens by separating six kinds of claim: recovered from the Unity code, invented for the rebuild, "
             "built, observed, proposed, or still waiting on a person. Built is large: twenty-three scripts and three "
             "shaders. Observed: forty-two of the game's own checks, and seventy-four more in this film's three scripted "
             "takes. Human playtests: zero."),
  props=dict(title='How the Document Labels a Claim', section='Status vocabulary · 1. Metadata',
             status='COMPARISON · built ≠ observed ≠ approved',
             visualLabel="Labels from the GDD's six-term vocabulary", layout='cards',
             cards=[{'label': 'Source · Authored', 'text': 'recovered from the Unity C#, or new in the rebuild'},
                    {'label': 'Implemented', 'text': '23 GDScript files + 3 shaders, 3,303 lines'},
                    {'label': 'Observed', 'text': "42 of the game's checks · 74 film-capture assertions"},
                    {'label': 'Pending', 'text': '0 human playtests · no section signed off'}]),
  cues=['recovered from', 'Built is', 'Observed:', 'Human playtests']),
 dict(id='B03', act='BODY', kind='board', status='pending',
  sections=['2. Vision', '3. Pillars (PROPOSED)'], lines=(37, 39),
  narration=("The vision is a proposal: wake in an abandoned valley, gather and craft through one afternoon, keep a fire "
             "burning until dawn. Who it's for is left open on purpose. The three pillars are read off the code: every "
             "tool comes from the land, the clock is the enemy, and your body keeps score."),
  props=dict(title='A Vision Nobody Signed', section='2. Vision · 3. Pillars',
             status='PROPOSED vision · audience PENDING', layout='cards',
             visualLabel='Pillars, proposed from the code',
             cards=[{'label': 'Every tool from the land', 'text': 'crafting only from what you gathered'},
                    {'label': 'The clock is the enemy', 'text': 'dusk at 20:00 · the cold at night'},
                    {'label': 'Your body keeps score', 'text': 'walking burns calories · time burns water'}]),
  cues=['The vision', 'every tool', 'the clock', 'your body']),
 dict(id='B04', act='BODY', kind='clip', status='observed', sections=['4. Core loop (IMPLEMENTED, OBSERVED)'],
  take='day', segments=[('play', 1430, 80), ('play', 2370, 50), ('play', 2680, 100), ('play', 4130, 90)], lead=0.3,
  narration=("Here's the core loop on the real build, played by a script, not a person. Look at a stick and press E. "
             "Craft the axe. Fell a pine in four swings. Then the campfire goes down by the lake. Every step is a cut "
             "from the same morning's take, in order.")),
 dict(id='B05', act='BODY', kind='board', status='proposed',
  sections=['5. Player-experience goals (PROPOSED, all PENDING a human playtest)'], lines=(59, 64),
  narration=("Four experience goals, all proposed, each with a test a person has to run. The captures can only hint. "
             "The scripted run placed its fire at twelve twenty-five, more than seven hours before dark, but it already "
             "knew the map. And food did matter: calories fell from a hundred to thirty-five by early afternoon, and three meals "
             "brought them back."),
  props=dict(title='Goals Nobody Has Tested', section='5. Player-experience goals',
             status='PROPOSED · 4 goals · all PENDING a playtest', layout='cards',
             visualLabel='What the scripted run can and cannot say',
             cards=[{'label': 'PX-01 · fire before 20:00', 'text': 'script placed it at 12:25, but it knew the map'},
                    {'label': 'PX-02 · food matters', 'text': 'calories 100 → 35 by 12:47; 3 meals restored them'}]),
  cues=['The captures', 'And food']),
 dict(id='B06', act='BODY', kind='board', status='comparison',
  sections=['6. Mechanics'], lines=(70, 70),
  narration=("Mechanics start with movement, and an honest retune. Unity moved the player at twelve metres a second with a "
             "three-metre jump. The rebuild keeps the gravity and the jump formula, but walks at five and a half, sprints "
             "at eight and a half, and jumps one point two metres, tuned for a ten-minute session."),
  props=dict(title='Same Physics, Slower Feet', section='M-01 · Movement and look',
             status='SOURCE vs IMPLEMENTED · retune PENDING (OQ-04)', layout='cards',
             visualLabel='Unity source vs. the Godot rebuild',
             cards=[{'label': 'Unity · PlayerMovement.cs', 'text': '12 m/s · jumpHeight 3'},
                    {'label': 'Godot · player.gd', 'text': 'walk 5.5 · sprint 8.5 m/s · jump 1.2 m'}]),
  cues=['Unity moved', 'The rebuild']),
 dict(id='B07', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='day', segments=[('play', 1420, 100), ('play', 2310, 180)], lead=0.3,
  narration=("Pickup and crafting, in play. The centre of the screen is the selector: the stick's name appears, E collects "
             "it, and a popup confirms. Later, the crafting screen shows the axe's recipe, three gold and three sticks, "
             "both owned, so the Craft button appears. One click, and press one to equip it.")),
 dict(id='B08', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(109, 111),
  narration=("Chopping and hunting are new, but Unity hinted at them: its sound manager declared a tool-swing and a chop "
             "sound that no script ever played. The rebuild uses them. Pines take four hits and drop two logs. Rabbits "
             "wander like Unity's AI, and bolt when you come within five metres."),
  props=dict(title='The Sounds Unity Never Played', section='M-06 · Chopping and hunting',
             status='AUTHORED · OBSERVED in motion', layout='cards',
             visualLabel='Where the feature came from',
             cards=[{'label': 'Unity · SoundManager', 'text': 'toolSwingSound, chopSound: declared, never played'},
                    {'label': 'Rebuild', 'text': 'pine: 4 hits → 2 logs · rabbit: flees within 5 m'}]),
  cues=['its sound manager', 'Pines take', 'Rabbits']),
 dict(id='B09', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='day', segments=[('play', 2650, 150), ('play', 3400, 180)], lead=0.3,
  narration=("Four swings, four shakes, and the pine topples away from the player. Then a rabbit, in motion, which the "
             "document itself says nobody had reviewed until now. It runs, the axe connects, it plays its death clip, and "
             "leaves meat.")),
 dict(id='B10', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(115, 118),
  narration=("The clock is the design's spine. Day runs at twenty-four seconds per game hour, night at twelve, and the "
             "game starts at half past seven. A placed fire warms you within nine metres. Resting there runs time nine "
             "times faster. And victory needs both: dawn, and part of the night spent beside your fire."),
  props=dict(title='The Clock Is the Enemy', section='M-07 · Day, night and campfire',
             status='AUTHORED · OBSERVED in takes day and night', layout='cards',
             visualLabel='What the code does with time',
             cards=[{'label': 'Day', 'text': '07:30 → 20:00 · 24 s per hour'},
                    {'label': 'Night', 'text': '12 s per hour · rest = 9× · warm within 9 m'}]),
  cues=['Day runs', 'A placed fire', 'victory needs']),
 dict(id='B11', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='day', segments=[('play', 3840, 90), ('play', 4120, 100)], lead=0.3,
  narration=("One rule the document doesn't list. Facing the lake, the fire is refused: you can't build a fire in the "
             "water, because its spot lands two and a half metres ahead. A few steps inland, the same right-click lights it.")),
 dict(id='B12', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='night', segments=[('play', 4920, 180), ('play', 5345, 120), ('play', 5790, 100)], lead=0.3,
  narration=("Night falls at eight, and the fire keeps the cold away. E at the fire rests, and the clock races. At dawn: "
             "dawn breaks, day two, sixteen items, two trees, one rabbit.")),
 dict(id='B13', act='BODY', kind='board', status='proposed',
  sections=['6. Mechanics'], lines=(100, 106),
  narration=("Survival stats follow Unity's, with added pressure. Water drops every five seconds. Idle time burns calories "
             "too. An empty stat costs one health a second, the night cold one every one point four, and you heal only "
             "when well fed. All of these rates are proposed, pending a human playtest."),
  props=dict(title='Your Body Keeps Score', section='6. Mechanics · M-05',
             status='IMPLEMENTED · tuning PROPOSED (OQ-04)', layout='cards',
             visualLabel='Rates from player_state.gd',
             cards=[{'label': 'Drain', 'text': 'water −1 per 5 s · calories −1 per 5 m and per 25 s idle'},
                    {'label': 'Damage', 'text': 'empty stat −1/s · cold −1 per 1.4 s'}]),
  cues=['Water drops', 'An empty stat', 'All of these']),
 dict(id='B14', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='day', start=4205, min_end=4740, lead=0.3,
  narration=("Cooking needs a fire nearby, and now there is one. Rabbit meat becomes cooked meat. In the inventory, hover an "
             "item for its description, drag one to the last slot, and right-click to eat: cooked meat, an apple, a "
             "mushroom. Calories go from thirty-five back to a hundred.")),
 dict(id='B15', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(85, 86),
  narration=("Two more decisions the rebuild made on its own. Dropping an item onto a full slot swaps the two, where Unity "
             "left it in place. And the save menu Unity drew, with no code behind it, now writes one save slot, with Load "
             "Game on the main menu and Load Save on the defeat screen."),
  props=dict(title='Choices the Rebuild Made', section='M-03 Inventory · M-09 Menus and saving',
             status='IMPLEMENTED · AUTHORED', layout='cards',
             visualLabel='Unity behaviour vs. the rebuild',
             cards=[{'label': 'Drag onto a full slot', 'text': 'Unity: no change · rebuild: swap'},
                    {'label': 'Saving', 'text': 'Unity: a menu, no code · rebuild: 1 JSON slot'}]),
  cues=['Dropping an item', 'And the save']),
 dict(id='B16', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='defeat', segments=[('play', 224, 240), ('play', 1150, 210)], lead=0.3,
  narration=("The failure path, from the night save. Walk away from the fire, and the cold sets in: a blue overlay and a "
             "warning. The N key, Unity's own debug damage, speeds it along. Lost to the wilds. Load Save puts you back "
             "beside the fire.")),
 dict(id='B17', act='BODY', kind='board', status='implemented',
  sections=['7. World (AUTHORED)', '8. Art and audio'], lines=(141, 142),
  narration=("The world is authored: a procedural valley two hundred and sixty metres across, ringed by mountains, with a "
             "lake, a village and three pine groves. Every model comes from the source asset packs, repaired at load time. "
             "Every sound was synthesized, because the source folders had none."),
  props=dict(title='A Valley From Asset Packs', section='7. World · 8. Art and audio',
             status='AUTHORED world · art from the source packs', layout='cards',
             visualLabel='What the folders supplied',
             cards=[{'label': 'World', 'text': '260 × 260 m · lake · village · 3 pine groves'},
                    {'label': 'Audio', 'text': 'none in the source · all synthesized'}]),
  cues=['a procedural valley', 'Every model', 'Every sound']),
 dict(id='B18', act='BODY', kind='board', status='implemented',
  sections=['9. UI (IMPLEMENTED)', '10. Out of scope', '11. Technical'], lines=(179, 181),
  narration=("Under the hood, every scene is thin. The game scene file is six lines, and the running valley holds nearly "
             "two thousand nodes, all built in code. Out of scope, by decision: more save slots, more nights, building "
             "beyond the fire, enemies and weather."),
  props=dict(title='Six Lines, Two Thousand Nodes', section='9. UI · 10. Out of scope · 11. Technical',
             status='IMPLEMENTED · scope set by the rebuild', layout='cards',
             visualLabel='Measured from the running game (tree_probe.txt)',
             cards=[{'label': 'game.tscn', 'text': '6 lines → 1,976 live nodes'},
                    {'label': 'Out of scope', 'text': 'multiple save slots · more nights · building · enemies · weather'}]),
  cues=['every scene is thin', 'Out of scope']),
 dict(id='B19', act='BODY', kind='board', status='pending',
  sections=['12. Risks and known defects', '13. Acceptance tests (OBSERVED)', '14. Provenance', '15. Open questions (PENDING)'],
  lines=(189, 190),
  narration=("The risks section is candid: nobody has played this by hand, and rabbit animation was only seen in stills. "
             "The film's captures close that second gap, and find one thing the document misses. Once a recipe uses your "
             "materials, the objective list still ticks them, but reads zero of three. Five open questions remain for a person."),
  props=dict(title='What a Person Still Has to Decide', section='12 · 13 · 14 · 15',
             status='PENDING · 5 open questions · 0 human playtests', layout='cards',
             visualLabel='Found on screen in the film captures',
             cards=[{'label': 'R-04 · rabbit in motion', 'text': 'now seen moving and dying in take day'},
                    {'label': 'New · objective counters', 'text': '[x] Gather 3 Sticks (0/3) after crafting'}]),
  cues=["The film's", 'Once a recipe']),
 dict(id='B20', act='VERDICT', kind='verdict',
  narration=("Verdict. This document organizes; it doesn't approve. The loop runs end to end in real input, from a new game "
             "to dawn and to defeat. The rebuild's own additions are clearly labelled. One small display bug slipped past "
             "every check. What's left is a person's call: the audience, the tuning, and whether one night is enough."),
  props=dict(artifactTitle='Verdict', artifactHeading='Organized, not approved', brandLabel='@NikBearBrown',
             artifactLines=['Observed end to end: new game → axe → fire → dawn; and load → freeze → defeat.',
                            "Checks: the game's 42 pass · 74 film-capture assertions pass.",
                            'Found: ticked objectives read 0/3 once a recipe uses the materials.',
                            'Pending a person: audience, drain rates, night length, 0 playtests.'])),
 dict(id='B21', act='HANDOFF', kind='composer',
  narration=("Your turn. Paste this into Claude with your own design document: Here is my game's design document. Pick one "
             "proposed experience goal. Rewrite it as a hypothesis with a test I can run with three players, and tell me "
             "which result would make me change the design. If no result would change your mind, it isn't a hypothesis "
             "yet. Liam, in for Bear."),
  props=dict(greeting='Your turn.', topic='WALKER · YOUR TURN', segment='Test One Design Hypothesis',
             command=("Here is my game's design document. Pick one proposed experience goal. Rewrite it as a hypothesis "
                      "with a test I can run with three players, and tell me which result would make me change the design."),
             runningText='paste this into Claude…',
             output=['Look for: a measurement, not an opinion.', 'Look for: a result that would change the design.'],
             folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
 dict(id='B22', act='OUTRO', kind='outro', tail=1.0,
  narration=f'{TITLE}. At Nik Bear Brown.',
  props=dict(title=TITLE, slug=SLUG, handle='@NikBearBrown', subline='')),
]

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
                         'type_note': 'engine capture of the game\'s own UI; GATE T pixel checks exempt (see BUILD-LOG.md); overlays verified by eye',
                         'capture': spec['take'], 'method': 'scripted-input',
                         'show': [{'at': 0.0, 'event': f"real gameplay, take '{spec['take']}', build a514438"}]}
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
        'source_doc': 'fantasy-survival-crafting-godot/submission/GDD.md (v0.1, agent-drafted, unapproved)',
        'game_build': {'commit': None, 'snapshot_sha256': rk.BUILD_ID,
                       'engine': 'Godot 4.7.2.stable.official.ed1daf0bf'},
        'note': ('godot-gdd walker film. Board excerpts are read verbatim from GDD.md by line. Gameplay '
                 'is scripted-input capture of the real main scene, same build; no human playtest exists. '
                 'No paid calls, no upload.'),
        'tags': ['Walker', 'Godot 4', 'game design document', 'survival crafting', 'Claude', 'Kokoro', 'Remotion'],
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
                                           f'build a514438)' + (', cropped to the HUD and enlarged 2x' if 'hud' in png.name else ''),
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
              'document': {'path': '../../fantasy-survival-crafting-godot/submission/GDD.md', 'sha256': rk.sha256(GDD),
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
