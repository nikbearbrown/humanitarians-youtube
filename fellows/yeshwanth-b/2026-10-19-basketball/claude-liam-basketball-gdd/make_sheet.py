"""Builds beat_sheet.json for claude-liam-basketball-gdd (godot-gdd walker).

    python3 make_sheet.py author    # narration + shots (run before Kokoro)
    python3 make_sheet.py finish    # after Kokoro: pad audio, cut clips, cues, ledger

Every excerpt is read from GDD.md by line number at build time, so the screen
can only show what the document says. Gameplay comes only from the scripted-
input takes in ../basketball-captures (same build, 8f86cc8).
"""
import json
import shutil
import sys
from pathlib import Path

from PIL import Image

REEL = Path(__file__).resolve().parent
CAPS = REEL.parent / 'basketball-captures'
sys.path.insert(0, str(CAPS))
import reelkit as rk  # noqa: E402

PKG = REEL.parents[1]
GDD = PKG / 'GDD.md'
SLUG = 'claude-liam-basketball-gdd'
TITLE = 'Basketball Blaster: The Design Document Came Last'
LINES = GDD.read_text().splitlines()


def excerpt(a, b):
    return '\n'.join(LINES[a - 1:b])


SRC = 'GDD.md · Basketball Blaster @ 8f86cc8 · agent-drafted v0.1, unapproved'

ASK_COMMAND = ('Please use Walker to convert my game design document about Basketball Blaster: Fowl Play — '
               'Mr. Block, armed with a basketball gun and basketball grenades, collects every egg across three '
               'arenas while chickens pour out of pipes — into a playable Godot project.')

# Board beats: (id, sections, design_status, excerpt lines, props, cue phrases)
# Clip beats: take + action window; narration must fit the real action.
BEATS = [
 dict(id='B00', act='ASK', kind='composer',
  narration=("Hola, this is Liam, in for Bear. This is how Walker is meant to be asked: hand it a game design "
             "document, get back a playable Godot project. The prompt on screen is a reconstruction, not a "
             "transcript, because this game was built first, and its document came after."),
  props=dict(greeting='Hola, Liam', topic='WALKER · GODOT · GDD', segment='The Design Document',
             command=ASK_COMMAND, runningText='illustrative reconstruction — not the historical prompt',
             output=['What happened: a Unity arena shooter was ported to Godot first.',
                     'GDD.md was written afterwards, from the folder\'s own evidence.'],
             folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
 dict(id='B01', act='BLUF', kind='writer', lead=0.8, tail=1.5,
  narration=("Basketball Blaster came before its design document. It ports a Unity arena shooter to Godot and "
             "stretches it to three arenas. The document was written last, from the evidence, and nothing in "
             "it is signed off."),
  props=dict(text=("Basketball Blaster\nwas built from its design document.\n"
                   "It ports a Unity arena shooter\nto Godot, in three arenas.\n"
                   "The document was written last,\nand nothing in it is signed off."),
             triggerWords='was built from', replacementWords='came before',
             fontSize=96, lineSpacing=1.3, charMs=22, mistakeRate=3, hesitateWithin=1, hesitateBetween=6,
             seed='basketball-gdd-2026-10', ink='#3D3929', accent='#D97757', bg='#FAF9F5', face='serif',
             align='center', brandLabel='@NikBearBrown')),
 dict(id='B02', act='BODY', kind='board', status='comparison',
  sections=['Status vocabulary', '1. Metadata'], lines=(25, 25),
  narration=("Before anything else, the document refuses to let one word mean two things. Every claim wears a "
             "label: recovered from the Unity code, stated in the README, invented for the port, built, seen in a "
             "capture, or still waiting on a human. The build runs end to end: eight scenes, two scripted takes, "
             "fifty-nine assertions passing. Zero human playtests. Both are true at once."),
  props=dict(title='How the Document Labels a Claim', section='Status vocabulary · 1. Metadata',
             status='COMPARISON · built ≠ observed ≠ approved',
             visualLabel='Labels grouped from the GDD\'s seven-term vocabulary', layout='cards',
             cards=[{'label': 'Source · README · Authored', 'text': 'from the Unity C#, the project README, or new in the port'},
                    {'label': 'Implemented', 'text': '14 GDScript files + 1 shader, 2,408 lines'},
                    {'label': 'Observed', 'text': '2 scripted takes · 59 of 59 assertions pass'},
                    {'label': 'Pending', 'text': '0 human playtests · no section signed off'}]),
  cues=['recovered from', 'built,', 'eight scenes', 'Zero human']),
 dict(id='B03', act='BODY', kind='board', status='pending',
  sections=['2. Vision', '3. Pillars'], lines=(45, 47),
  narration=("Section two admits a gap. The README says what was ported and what was added, but no document says "
             "who this game is for, or why anyone should play it. So the vision line on screen is the agent's "
             "proposal, and it's marked that way. The three pillars are read off the code: eggs end a level, kills "
             "never do; the arena is vertical; and every hit is loud."),
  props=dict(title='A Vision Nobody Wrote Down', section='2. Vision · 3. Pillars',
             status='PENDING · vision unsigned · pillars proposed from the code', layout='cards',
             visualLabel='Real gameplay for this section is in the adjacent clips',
             cards=[{'label': 'README', 'text': 'a port, plus three arenas, a jetpack, a briefing'},
                    {'label': 'Proposed as vision', 'text': 'a short, loud arena shooter: eggs, not kills'}]),
  cues=['The README', 'the vision line']),
 dict(id='B04', act='BODY', kind='clip', status='observed', sections=['4. Core loop'],
  take='campaign', start=2440, min_end=2960, lead=0.4,
  narration=("Here's the core loop, on the real build, played by a script. He's just lost a life to the flock, and "
             "respawns at the gate. Then he heads for the nearest nest, shooting whatever is close, and each egg "
             "ticks the counter. The fifth egg ends the arena: court cleared. Notice what decided it. Eggs. Kills "
             "never end a level.")),
 dict(id='B05', act='BODY', kind='board', status='proposed',
  sections=['5. Player-experience goals'], lines=(77, 82),
  narration=("Experience goals are where a design document starts guessing, so all four are labelled proposed. "
             "And the captures already push back on two of them. The autopilot collected every egg in under twenty "
             "seconds per arena. Fighting in place for twenty-five seconds earned ten kills, cost a life, and "
             "collected nothing. On this build, rushing beats fighting. That's not a playtest. It's a reason to run one."),
  props=dict(title='Goals Nobody Has Approved', section='5. Player-experience goals',
             status='PROPOSED · 4 goals · none approved', layout='cards',
             visualLabel='Real gameplay for this section is in the adjacent clips',
             cards=[{'label': 'PX-02 · each arena feels harder', 'text': 'eggs taken in 12.6 s · 13.6 s · 18.7 s'},
                    {'label': 'PX-03 · fighting is worthwhile', 'text': '25.6 s: 10 kills, 1 life lost, 0 eggs'}]),
  cues=['the captures', 'Fighting in place']),
 dict(id='B06', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(104, 106),
  narration=("Mechanics, and one honest discovery. The Unity project declared a jetpack input, a single true-or-false "
             "field, and no script ever read it. The port wires it up: hold Shift, burn one point six seconds of "
             "fuel, rise at up to four hundred and thirty pixels a second. That's new, so the document labels it "
             "authored, not recovered. Two quieter retunes get the same label: coyote time and the fire rate."),
  props=dict(title='The Jetpack Unity Never Wired Up', section='M-01 · M-02 · M-03',
             status='IMPLEMENTED · AUTHORED in the port · OBSERVED in take campaign', layout='cards',
             visualLabel='Unity source vs. the Godot port (values from the code)',
             cards=[{'label': 'Unity · PlayerInput.cs:44', 'text': 'public bool Jetpack; — declared, never read'},
                    {'label': 'Godot · player.gd', 'text': 'Shift · 1.6 s of fuel · rise capped at 430 px/s'},
                    {'label': 'Also authored', 'text': 'coyote time 0.5 → 0.15 s · fire every 0.5 → 0.4 s'}]),
  cues=['declared a jetpack', 'The port wires', 'Two quieter']),
 dict(id='B07', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='campaign', start=1226, min_end=1694, lead=0.3,
  narration=("In play. A walk, a jump, then a second press in mid-air: the double jump launches him again. Shift "
             "lights the jetpack, and the blue fuel bar drains. The gun follows the crosshair and fires a ball every "
             "four tenths of a second. Right-click lobs a grenade: three beeps, then the blast. And watch the health "
             "balls, top left. Chickens tag him twice during the demo.")),
 dict(id='B08', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(175, 177),
  narration=("The mega kill comes straight from the Unity audio manager: three or more chickens dying before the "
             "next physics frame. The port keeps the number and the rule. In practice it means a grenade, landed in "
             "a crowd. The capture got one."),
  props=dict(title='Three at Once', section='M-04 · M-08',
             status='SOURCE + IMPLEMENTED · OBSERVED at frame 1795', layout='cards',
             visualLabel='Where the rule lives',
             cards=[{'label': 'Unity · AudioManager.cs', 'text': 'DeathWindowRoutine · megaKillAmount = 3'},
                    {'label': 'Godot · game.gd:470-479', 'text': 'counts deaths, waits one physics frame'},
                    {'label': 'Grenade', 'text': '3-beep, 3 s fuse · 230 px · 3 damage'}]),
  cues=['three or more', 'keeps the number', 'In practice']),
 dict(id='B09', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='campaign', segments=[('play', 1680, 120), ('replay', 1780, 24, 4), ('play', 1800, 90)], lead=0.3,
  narration=("Fight phase. He comes in with one health ball and loses a life almost at once. Then a grenade lands "
             "among four chickens: mega kill. Here it is again at a quarter of the speed, labelled as a replay, not a "
             "second run. The idea is simple: hold one spot, shoot, and lob grenades at clusters.")),
 dict(id='B10', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(151, 153),
  still=('defeat', 618, 'Real frame: respawn at the gate after a lost life (take defeat)'),
  narration=("Damage is forgiving by design. A touch costs one of three health and buys a second of invulnerability. "
             "Three hits cost a life, and you respawn at the gate with two seconds of safety. Before you reappear, any "
             "chicken camping the gate is deleted. That last rule isn't in the Unity code. It's the port's own "
             "fairness patch."),
  props=dict(title='How Forgiving a Hit Is', section='M-06 · Damage, lives and respawn',
             status='IMPLEMENTED · gate-clearing is AUTHORED', layout='cards',
             visualLabel='Real gameplay for this section is in the adjacent clips',
             cards=[{'label': 'Per life', 'text': '3 health · 1 s invulnerable after a hit'},
                    {'label': 'Respawn', 'text': '2 s invulnerable · chickens within 260 px removed'}]),
  cues=['A touch costs', 'any chicken']),
 dict(id='B11', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='defeat', start=485, min_end=1150, lead=3.5,
  narration=("Now the failure path, on purpose. The driver walks into the flock without firing. Three hits, a fade "
             "to navy, and a respawn at the gate. Again. And again. With the third life gone, the defeat screen asks: "
             "the flock won arena one, run it back? Retry Arena loads the same court with all three lives restored.")),
 dict(id='B12', act='BODY', kind='board', status='implemented',
  sections=['7. Systems', '14. Technical'], lines=(257, 258),
  narration=("Under the hood, two choices matter. Contact damage isn't a physics collision. Every frame, the arena "
             "measures the distance from Mister Block to each chicken. And there are no automated tests at all. The "
             "only machine checks are this film's: a smoke run of all eight scenes, and the assertions inside the two "
             "scripted takes."),
  props=dict(title='No Tests, One Distance Check', section='7. Systems · 14. Technical',
             status='IMPLEMENTED · no automated tests in the project', layout='cards',
             visualLabel='What the code actually does',
             cards=[{'label': 'Input', 'text': 'keys, mouse and pad bound in code at boot'},
                    {'label': 'Contact', 'text': 'distance under 58 px, checked every physics frame'},
                    {'label': 'Tests in the project', 'text': 'none'},
                    {'label': 'Film checks', 'text': '8-scene smoke run · 59 capture assertions'}]),
  cues=['Contact damage', 'Every frame', 'no automated tests', 'The only machine']),
 dict(id='B13', act='BODY', kind='board', status='comparison',
  sections=['8. Progression', '9. World and levels'], lines=(194, 198),
  still=('campaign', 4300, 'Real frame: arena 3, Fowl Play Finals'),
  narration=("Progression is one table. Each arena is wider, with more pipes, faster spawns, a higher cap and more "
             "eggs, and arena three's chickens take four hits. Whether that feels harder is a human question. The "
             "captures can only say the autopilot needed about thirteen, fourteen, then nineteen seconds."),
  props=dict(title='Difficulty Is One Table', section='8. Progression · 9. World and levels',
             status='IMPLEMENTED ramp · felt difficulty PENDING', layout='image',
             visualLabel='Real frame: arena 3, build 8f86cc8',
             cards=[{'label': 'Ramp (code)', 'text': '2 → 3 → 4 pipes · 3.0 → 2.2 s · 5 → 7 eggs'},
                    {'label': 'Autopilot egg time', 'text': '12.6 s · 13.6 s · 18.7 s'}]),
  cues=['Each arena', 'The captures']),
 dict(id='B14', act='BODY', kind='clip', status='observed', sections=['8. Progression', '9. World and levels'],
  take='campaign', segments=[('play', 3398, 170), ('play', 3977, 190)], lead=0.3,
  narration=("Arena two, Sunset Rooftops: three pipes, an orange tint, six eggs. Cut to arena three, the Fowl Play "
             "Finals: four pipes, a darker navy tint, seven eggs, and one more platform row near the ceiling.")),
 dict(id='B15', act='BODY', kind='board', status='implemented',
  sections=['10. Narrative and characters', '11. UI and controls'], lines=(214, 216),
  narration=("The story is eight lines long: a pre-game briefing where the coach explains the controls and Mister "
             "Block says, let's ball. Unity had none of it. The rest of the interface is a main menu, how to play, "
             "a pause screen, and the end cards. And the briefing is where the first defect lives."),
  props=dict(title='Eight Lines of Story', section='10. Narrative · 11. UI and controls',
             status='IMPLEMENTED · AUTHORED in the port', layout='cards',
             visualLabel='Real gameplay for this section is in the adjacent clips',
             cards=[{'label': 'Narrative', 'text': 'COACH explains the controls · MR. BLOCK replies'},
                    {'label': 'UI', 'text': 'menu · how to play · HUD · pause · end cards'}]),
  cues=['eight lines', 'The rest']),
 dict(id='B16', act='BODY', kind='clip', status='observed', sections=['11. UI and controls', '15. Risks and known defects'],
  take='campaign', start=440, min_end=640, lead=0.3,
  narration=("The prompt says enter or click to continue. Watch the click on the dialogue box: nothing. Above it: "
             "nothing. Enter works, and Escape skips. The reason: a full-screen shade layer swallows every click before "
             "the briefing can see it. It's small, but it's the first thing a new player touches.")),
 dict(id='B17', act='BODY', kind='board', status='pending',
  sections=['12. Audio and art', '13. Out of scope'], lines=(233, 239),
  narration=("Every sound and the music loop were synthesized for the port, because the Unity export had no audio "
             "files. The art is the Unity project's, cropped and sliced. Who owns it, and whether it can be published, "
             "isn't written down anywhere. Out of scope, by omission: saves, settings, accessibility options, online play."),
  props=dict(title='Whose Art Is This?', section='12. Audio and art · 13. Out of scope',
             status='PENDING · art rights unrecorded', layout='cards',
             visualLabel='What the folder records',
             cards=[{'label': 'Audio', 'text': '13 named sounds + a music loop, synthesized for the port'},
                    {'label': 'Art', 'text': 'reused from the Unity project · rights not recorded'},
                    {'label': 'Not in this build', 'text': 'saves · settings · accessibility · online'}]),
  cues=['synthesized', 'The art', 'Out of scope']),
 dict(id='B18', act='BODY', kind='board', status='pending',
  sections=['15. Risks and known defects', '16. Open questions', 'Appendix A — Acceptance tests',
            'Appendix B — Provenance', 'Appendix C — Changes'], lines=(264, 268),
  narration=("Section fifteen lists what the captures found: the dead click, and HUD hints drawn over their own bars. "
             "Then six open questions only a person can answer. Who is this for? Should fighting pay? Are the retunes "
             "intended? Who owns the art? The appendices hold the acceptance table, with one row still empty: a human "
             "playtest."),
  props=dict(title='What a Person Still Has to Decide', section='15 · 16 · Appendices A–C',
             status='PENDING · 6 open questions · 0 human playtests', layout='cards',
             visualLabel='Real gameplay for this section is in the adjacent clips',
             cards=[{'label': 'OQ-01 · OQ-02', 'text': 'Who is it for? Should fighting pay?'},
                    {'label': 'Appendix A', 'text': 'machine rows pass · human playtest: not run'}]),
  cues=['six open', 'The appendices']),
 dict(id='B19', act='VERDICT', kind='verdict',
  narration=("Verdict. This document organizes; it doesn't approve. What's built is observed working end to end, "
             "with fifty-nine machine assertions behind it. What it found is concrete: a dead click, overlapping hints, "
             "and a loop where eggs beat fighting. What's left belongs to a person: the purpose, the art rights, the "
             "feel, and whether it's worth playing at all."),
  props=dict(artifactTitle='Verdict', artifactHeading='Organized, not approved', brandLabel='@NikBearBrown',
             artifactLines=['Built and observed: 3 arenas, every mechanic, pause, defeat, retry, victory.',
                            'Machine checks: 8-scene smoke run · 59 of 59 capture assertions.',
                            'Found: dead click-to-continue · HUD hints over their bars · eggs beat fighting.',
                            'Pending a person: the vision, 4 experience goals, art rights, a playtest.'])),
 dict(id='B20', act='HANDOFF', kind='composer',
  narration=("Your turn. Paste this into Claude with your own design document: Here is my game's design document. "
             "Pick one proposed experience goal. Rewrite it as a hypothesis with a test I can run with three players, "
             "and tell me which result would make me change the design. If no result would change your mind, it isn't "
             "a hypothesis yet. Liam, in for Bear."),
  props=dict(greeting='Your turn.', topic='WALKER · YOUR TURN', segment='Test One Design Hypothesis',
             command=("Here is my game's design document. Pick one proposed experience goal. Rewrite it as a "
                      "hypothesis with a test I can run with three players, and tell me which result would make me "
                      "change the design."),
             runningText='paste this into Claude…',
             output=['Look for: a measurement, not an opinion.', 'Look for: a result that would change the design.'],
             folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
 dict(id='B21', act='OUTRO', kind='outro', tail=1.0,
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
                         'show': [{'at': 0.0, 'event': f"real gameplay, take '{spec['take']}', build 8f86cc8"}]}
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
        'source_doc': 'basketball-game-godot/GDD.md (v0.1, agent-drafted, unapproved)',
        'game_build': {'commit': None, 'snapshot_sha256': rk.BUILD_ID,
                       'engine': 'Godot 4.7.2.stable.official.ed1daf0bf'},
        'note': ('godot-gdd walker film. Board excerpts are read verbatim from GDD.md by line. Gameplay '
                 'is scripted-input capture of the real main scene, same build; no human playtest exists. '
                 'No paid calls, no upload.'),
        'tags': ['Walker', 'Godot 4', 'game design document', 'arena shooter', 'Claude', 'Kokoro', 'Remotion'],
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
                                           f'build 8f86cc8)' + (', cropped to the HUD and enlarged 2x' if 'hud' in png.name else ''),
                                 'supports': f'{bid}: {label}'})
    # copy the takes used as evidence into the reel and hash them
    for take in sorted({s['take'] for s in BEATS if s['kind'] == 'clip'}):
        for suffix in ('.mp4', '-inputs.jsonl'):
            src = rk.TAKES / f'{take}{suffix}'
            dst = REEL / f'capture/{take}{suffix}'
            shutil.copy2(src, dst)
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
              'document': {'path': '../../GDD.md', 'sha256': rk.sha256(GDD),
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
