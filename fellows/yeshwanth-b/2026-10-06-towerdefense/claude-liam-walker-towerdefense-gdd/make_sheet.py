"""Builds beat_sheet.json for claude-liam-walker-towerdefense-gdd (godot-gdd walker).

    python3 make_sheet.py author    # narration + shots (run before Kokoro)
    python3 make_sheet.py finish    # after Kokoro: pad audio, cut clips, cues, ledger

Every excerpt is read from GDD.md by line number at build time, so the screen
can only show what the document says. Gameplay comes only from the scripted-
input takes in ../walker-towerdefense-captures (same build, caf082c).
"""
import json
import shutil
import sys
from pathlib import Path

REEL = Path(__file__).resolve().parent
CAPS = REEL.parent / 'walker-towerdefense-captures'
sys.path.insert(0, str(CAPS))
import reelkit as rk  # noqa: E402

GAME = REEL.parents[1] / 'Walker-Godot-TowerDefense'
GDD = GAME / 'GDD.md'
SLUG = 'claude-liam-walker-towerdefense-gdd'
TITLE = 'Walker Tower Defense: The Design Document Came Last'
LINES = GDD.read_text().splitlines()


def excerpt(a, b):
    return '\n'.join(LINES[a - 1:b])


SRC = 'GDD.md · walker-towerdefense @ caf082c · agent-drafted v0.1, unapproved'

# ---- beats -----------------------------------------------------------------
# Board beats: (id, sections, design_status, excerpt lines, props, cue phrases)
# Clip beats: take + action window; narration must fit the real action.

ASK_COMMAND = ('Please use Walker to convert my game design document about a four-element '
               'tower defense — Fire, Ice, Poison and Storm towers on a 12-by-8 grid, where '
               'every tower you build reshapes the monsters\' route — into a playable Godot project.')

BEATS = [
 dict(id='B00', act='ASK', kind='composer',
  narration=("Hola — this is Liam, in for Bear. This is how Walker is meant to be asked: hand it "
             "a game design document, get back a playable Godot project. The prompt on screen is a "
             "reconstruction, not a transcript — because this game happened the other way round."),
  props=dict(greeting='Hola, Liam', topic='WALKER · GODOT · GDD', segment='The Design Document',
             command=ASK_COMMAND, runningText='illustrative reconstruction — not the historical prompt',
             output=['What happened: a lost Unity game was rebuilt in Godot first.',
                     'GDD.md was written afterwards, from the repo\'s own evidence.'],
             folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
 dict(id='B01', act='BLUF', kind='writer', lead=0.8, tail=1.5,
  narration=("Walker Tower Defense came before its design document. It rebuilds a lost Unity game "
             "from twenty-seven surviving scripts. The document was written last, from the evidence — "
             "and every human sign-off in it is still pending."),
  props=dict(text=("Walker Tower Defense\nwas built from its design document.\n"
                   "It rebuilds a lost Unity game\nfrom 27 surviving scripts.\n"
                   "The document was written last,\nand nothing in it is signed off."),
             triggerWords='was built from', replacementWords='came before',
             fontSize=96, lineSpacing=1.3, charMs=22, mistakeRate=3, hesitateWithin=1, hesitateBetween=6, seed='walker-towerdefense-gdd-2026-10',
             ink='#3D3929', accent='#D97757', bg='#FAF9F5', face='serif', align='center',
             brandLabel='@NikBearBrown')),
 dict(id='B02', act='BODY', kind='board', status='comparison',
  sections=['Status vocabulary', '1. Metadata'], lines=(23, 24),
  narration=("Before anything else, the document refuses to let one word mean two things. Every "
             "claim wears a label: recovered from the Unity code, decided by a person, invented for "
             "the port, built, checked by a machine — or still waiting on a human. Sixty-five "
             "automated checks pass. Zero of twenty-two playtest items are done. Both are true at once."),
  props=dict(title='How the Document Labels a Claim', section='Status vocabulary',
             status='COMPARISON · built ≠ machine-checked ≠ approved',
             visualLabel='Labels grouped from the GDD\'s eight-term vocabulary',
             layout='cards',
             cards=[{'label': 'Recovered · Decided · Authored', 'text': 'from the Unity C#, a human ruling, or invented for the port'},
                    {'label': 'Implemented', 'text': 'present in the Godot code at the cited line'},
                    {'label': 'Auto-verified', 'text': '65 automated checks pass (4 suites)'},
                    {'label': 'Pending', 'text': '0 of 22 playtest items · 4 design gates unsigned'}]),
  cues=['recovered from', 'built,', 'Sixty-five', 'Zero of']),
 dict(id='B03', act='BODY', kind='board', status='pending',
  sections=['2. Vision', '3. Pillars'], lines=(54, 56),
  still=('opening', 40, 'Real frame: the game\'s menu card, same build, scripted-input capture'),
  narration=("Section two is the awkward one, and it says so. Nobody ever wrote down what this game "
             "is for. What exists is a project brief: rebuild it faithfully, invent nothing. The line "
             "on the menu — four elements, one road — was written by the agent during the build. "
             "There are no pillars either: just three things the code makes true."),
  props=dict(title='A Vision Nobody Wrote Down', section='2. Vision · 3. Pillars',
             status='PENDING · vision gate unsigned · no pillars exist', layout='image',
             visualLabel='Real frame: menu card, build caf082c (scripted-input capture)',
             cards=[{'label': 'Decided (project brief)', 'text': 'faithful port — invent nothing'},
                    {'label': 'Proposed as vision', 'text': 'menu copy, written by the agent'}]),
  cues=['project brief', 'The line']),
 dict(id='B04', act='BODY', kind='clip', status='observed', sections=['4. Core loop'],
  take='opening', start=330, min_end=905, lead=0.4,
  narration=("Here's the core loop, played on the real build by a script, not a person. Build: Fire "
             "at the corner, Ice beside the road — fifty gold, gone. Space releases wave one: two "
             "monsters, a beat apart, walking the shortest route from in to out. The towers fire on "
             "their own. Every kill pays four gold. Then you spend it, and go again. There's no win "
             "state; the run is endless, by decision.")),
 dict(id='B05', act='BODY', kind='board', status='proposed',
  sections=['5. Player-experience goals'], lines=(114, 116),
  still=('opening', 1400, 'Real frame: scripted Fire + Ice opening, run over at wave 3'),
  narration=("Experience goals are where a design document starts guessing — so this one labels "
             "all eight as proposed: each one a checklist question, restated as a claim you could "
             "reject. Two already have evidence against them. Making this film, a scripted Fire-and-Ice "
             "opening lost all five lives by wave three. That's not a playtest. It's a reason to run one."),
  props=dict(title='Goals Nobody Has Approved', section='5. Player-experience goals',
             status='PROPOSED · 8 goals restated from the checklist · none approved', layout='image',
             visualLabel='Real frame: film capture, scripted input — not a human playtest',
             cards=[{'label': 'PX-06 · difficulty by wave 5', 'text': 'counter-evidence: lost at wave 3'},
                    {'label': 'Status', 'text': 'PENDING a human playtest'}]),
  cues=['Two already', 'not a playtest']),
 dict(id='B06', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(309, 317),
  narration=("Now the finding the whole design turns on. It's called an elemental tower defense, and "
             "there is no elemental damage system. Every hit calls this one function. It subtracts one "
             "number. It never learns which element fired, or what colour the monster is — the four "
             "colours are cosmetic. The elements differ only in what they do after the hit. Hit-flash "
             "is the one later line, and it's presentation."),
  props=dict(title='The Elemental Game With No Elements', section='M-06 · Damage and the four elements',
             status='IMPLEMENTED · AUTO-VERIFIED by check no-elemental-matrix', layout='cards',
             visualLabel='What actually differs, per tower_tuning.gd (recovered values)',
             cards=[{'label': 'Fire', 'text': '1.0 s cooldown · no effect'},
                    {'label': 'Ice', 'text': 'slows to half speed · refreshes, never stacks'},
                    {'label': 'Poison', 'text': '0.7 damage per second for 1.5 s'},
                    {'label': 'Storm', 'text': 'chains to 2 more within 1.25 tiles'}]),
  cues=['which element', 'differ only', 'after the hit', 'Hit-flash']),
 dict(id='B07', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='poison', start=196, min_end=440, lead=0.3,
  narration=("Poison, in play — with a surprise. Wave one happens to be two monsters of the cosmetic "
             "green variant, so poison's green tint shows you nothing. Escape pauses mid-wave; Enter "
             "resumes. In wave two, watch the lead monster once it's poisoned: it turns pale, not green. "
             "Every poison tick counts as a hit, and every hit flashes white. Can a player read that? "
             "Checklist item ten. Still open.")),
 dict(id='B08', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='storm', segments=[('play', 129, 75), ('replay', 173, 6, 8), ('play', 204, 60)], lead=0.3,
  narration=("Storm is the one that chains. Watch the beam leave the tower, hit one monster, then jump "
             "to its neighbour. At real speed it's on screen for about a fifth of a second — so here it "
             "is again, slowed down and labelled. Does that read as a chain, or a flicker? That's "
             "checklist item eleven, and it's open.")),
 dict(id='B09', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(191, 193),
  narration=("One rule here is new. The Unity original let you wall the road off completely — and any "
             "monster left without a route was simply teleported to the exit. A human ruled that out. "
             "Now, before a tower goes down, the game pretends it already exists, and checks that the "
             "entrance, and every monster on the board, can still reach the exit."),
  props=dict(title='The Rule the Original Didn\'t Have', section='M-02 · Route and maze',
             status='DECIDED (O-04 / D-06, 2026-09-21) · IMPLEMENTED', layout='cards',
             visualLabel='Before and after the human ruling; shown live in the next beat',
             cards=[{'label': 'Unity source (Monster.cs:190-201)', 'text': 'walls allowed; stranded monsters teleported to the exit'},
                    {'label': 'This port (grid.gd:152-165)', 'text': 'assume the tower exists; spawn and every monster must still reach the exit'},
                    {'label': 'Refusal shown to the player', 'text': '"Would block the path"'}]),
  cues=['teleported', 'Now, before']),
 dict(id='B10', act='BODY', kind='clip', status='observed', sections=['6. Mechanics'],
  take='maze', start=330, min_end=800, lead=0.3,
  narration=("Watch it work. One Fire tower beside the spawn: fine. A second that would seal the corner: "
             "refused — would block the path. That reason is on screen for three-tenths of a second. "
             "Then a tower dropped straight onto the road. Nothing refuses it; the route tint bends "
             "round it, and the next wave follows the new path. It's a maze, not a gun line.")),
 dict(id='B11', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(250, 254),
  narration=("Difficulty comes from exactly one place — and it's a bug. In the Unity code, the health "
             "increase sat inside the per-monster spawn loop, so it compounds. It's also the only "
             "difficulty curve the game has; remove it and every wave plays the same. So a person kept "
             "the curve exactly, and fixed only the part where it leaked into your next run."),
  props=dict(title='A Bug Kept on Purpose', section='M-04 · Waves and the difficulty ramp',
             status='SOURCE quirk · DECIDED (O-03 / D-05) · AUTO-VERIFIED', layout='cards',
             visualLabel='Monster health after waves 0–5 (check compounding-hp-curve)',
             cards=[{'label': 'Health, waves 0 → 5', 'text': '3.0 · 3.1 · 3.4 · 4.0 · 5.0 · 6.5'},
                    {'label': 'Why it compounds', 'text': 'the ramp ran once per monster, not per wave'},
                    {'label': 'Decision', 'text': 'keep the curve; reset it on restart'}]),
  cues=['per-monster', 'only', 'kept']),
 dict(id='B12', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics', '8. Progression'], lines=(366, 368),
  still=('opening', 1722, 'Real frame: an upgraded Fire tower — SELL 34, MAXED'),
  narration=("The economy is half archaeology, half invention. Fifty gold, five lives, four per kill — "
             "those came from the source. The prices didn't: they lived in Unity Inspector fields that "
             "never survived, so they were authored, then approved. Each tower upgrades once. Between "
             "runs, the only thing that carries over is your best wave."),
  props=dict(title='Prices Nobody Recovered', section='M-07 · Economy · 8. Progression',
             status='SOURCE (start, rewards) · AUTHORED + DECIDED (prices, O-02)', layout='image',
             visualLabel='Real frame: one upgrade, then MAXED; sale value 10 + round(0.8 × 30)',
             cards=[{'label': 'Recovered', 'text': '50 gold · 5 lives · 4 per kill'},
                    {'label': 'Authored', 'text': 'Fire 20 · Ice 25 · Poison 30 · Storm 35'}]),
  cues=['came from', 'The prices']),
 dict(id='B13', act='BODY', kind='board', status='observed',
  sections=['15. Risks'], lines=(596, 599),
  narration=("The risks section starts with history. Fifty-six automated checks passed while the game "
             "was unplayable — twice. The keyboard was completely dead, because no test ever pressed a "
             "key. And it ran three times too slow: the Unity timings were faithful to a board where a "
             "tile was one unit, not sixty-four pixels. A person found both in minutes."),
  props=dict(title='Twice Unplayable, All Checks Green', section='15. Risks · history',
             status='HUMAN-OBSERVED · both fixed (51e4eec, b67653a)', layout='cards',
             visualLabel='Recorded in PORTING_NOTES.md §4.4 and GAME-BRIEF.md §16',
             cards=[{'label': '56 checks', 'text': 'green throughout'},
                    {'label': 'Failure 1', 'text': 'keyboard dead — no test pressed a key'},
                    {'label': 'Failure 2', 'text': '3× too slow — faithful to the wrong reference frame'},
                    {'label': 'Found by', 'text': 'a person, in minutes'}]),
  cues=['Fifty-six', 'keyboard', 'three times', 'A person']),
 dict(id='B14', act='BODY', kind='board', status='pending',
  sections=['9. World', '10. Narrative', '11. Characters'], lines=(444, 446),
  still=('opening', 112, 'Real frame: the one authored map, "Open Ground", 12 × 8'),
  narration=("The world is one authored map. The original level file was lost, and its loader shows it "
             "held numbered levels — so the port ships one where there were several. Narrative and "
             "characters are empty, deliberately. The source has no story and no cast, and the document "
             "won't invent either just to fill a template."),
  props=dict(title='One Map, and No Story', section='9. World · 10. Narrative · 11. Characters',
             status='AUTHORED map (O-01) · world gate PENDING', layout='image',
             visualLabel='Real frame: the empty board before any tower',
             cards=[{'label': 'Narrative · Characters', 'text': 'not applicable — nothing to port'},
                    {'label': 'World gate', 'text': 'PENDING'}]),
  cues=['numbered levels', 'Narrative']),
 dict(id='B15', act='BODY', kind='board', status='implemented',
  sections=['7. Systems', '12. Features', '13. Out of scope', '14. Technical'], lines=(527, 528),
  still=('poison', 300, 'Real frame: everything on screen is drawn in code'),
  narration=("Technically, it's almost all script. The only scene file is a stub: one node, one script. "
             "Seven systems, all stepped from one session loop. Everything on screen is "
             "drawn in code; no recovered art ships on main, and it doesn't look like the original. "
             "There's no audio at all — the Unity extract contained none."),
  props=dict(title='One Scene File, Everything Drawn', section='7 Systems · 12 Features · 13 Out of scope · 14 Technical',
             status='IMPLEMENTED · asset level L0 · silent build', layout='image',
             visualLabel='Real frame: no image or audio files ship in the game',
             cards=[{'label': 'main.tscn', 'text': 'one Node2D + session.gd'},
                    {'label': 'Out of scope', 'text': 'audio · recovered art · more levels'}]),
  cues=['Seven systems', 'no audio']),
 dict(id='B16', act='BODY', kind='board', status='pending',
  sections=['16. Open questions', 'Appendix A — Acceptance tests and traceability',
            'Appendix B — Provenance', 'Appendix C — Conflicts between documents and HEAD',
            'Appendix D — Changes'], lines=(631, 631),
  narration=("It ends on questions, and every one belongs to a person. What is this game for? Should a "
             "game with no damage types keep the word elemental? Is three-times speed right, or just the "
             "first thing that worked? The appendices tie each check to a rule, list what was read, and "
             "log five stale claims — since corrected by the owner."),
  props=dict(title='What the Document Cannot Decide', section='16. Open questions · Appendices A–D',
             status='PENDING · 10 open questions · every one a human decision', layout='cards',
             visualLabel='Selected from OQ-01 … OQ-10',
             cards=[{'label': 'OQ-01', 'text': 'What is this game for, beyond a faithful port?'},
                    {'label': 'OQ-03', 'text': 'Keep the word "elemental"?'},
                    {'label': 'OQ-04', 'text': 'Is 3× the right base speed?'},
                    {'label': 'Appendix C', 'text': '5 stale claims found; fixed in later commits'}]),
  cues=['What is this', 'elemental', 'three-times', 'appendices']),
 dict(id='B17', act='VERDICT', kind='verdict',
  narration=("Verdict. The AI organized the evidence: it traced every rule to a file, every check to a "
             "requirement, and caught the project's own stale numbers. What it can't do is the part that "
             "matters next. Whether this game is fair, readable, or worth a second run is a human call — "
             "and right now, nobody has made it."),
  props=dict(artifactTitle='Verdict', artifactHeading='Organized, not approved', brandLabel='@NikBearBrown',
             artifactLines=['Built and machine-checked: every ported system; 65 checks pass.',
                            'Human rulings on record: no damage matrix, no recovered art, endless mode, the no-seal rule.',
                            'Proposed only: the vision, eight experience goals, every pillar.',
                            'Pending a person: 0 of 22 playtest items, four unsigned design gates.'])),
 dict(id='B18', act='HANDOFF', kind='composer',
  narration=("Your turn. Paste this into Claude with your own game's design document: "
             "Pick one proposed experience goal. Rewrite it as a hypothesis a playtester could prove "
             "wrong. Then design the smallest test: the setup, what the tester does, what I measure, and "
             "the result that would make me change the design. Don't fill in a result. "
             "The last line matters most — a test with its answer pre-filled isn't a test. "
             "Liam, in for Bear."),
  props=dict(greeting='Your turn.', topic='WALKER · YOUR TURN', segment='Test One Design Hypothesis',
             command=("Here is my game's design document. Pick one proposed experience goal. Rewrite it as "
                      "a hypothesis a playtester could prove wrong. Then design the smallest test: the "
                      "setup, what the tester does, what I measure, and the result that would make me "
                      "change the design. Don't fill in a result."),
             runningText='paste this into Claude…',
             output=['Look for: a measurement, not an opinion.', 'Look for: a result that would change the design.'],
             folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
 dict(id='B19', act='OUTRO', kind='outro', tail=1.0,
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
                         'show': [{'at': 0.0, 'event': f"real gameplay, take '{spec['take']}', build caf082c"}]}
            b['qc'] = {'full_bleed': True, 'full_bleed_reason': ('The engine frame (3049x2160) fills the full '
                       'frame height by design: native 4K game pixels, not a title card. Our overlays sit inside '
                       'title-safe; the game HUD at the top edge is game UI.')}
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
        'source_doc': 'Walker-Godot-TowerDefense/GDD.md (v0.1, agent-drafted, unapproved) at caf082c',
        'game_build': {'commit': 'caf082c7968bca13cf8751983d27787107b46b2d', 'snapshot_sha256': rk.BUILD_ID,
                       'engine': 'Godot 4.7.2.stable.official.ed1daf0bf'},
        'note': ('godot-gdd walker film. Board excerpts are read verbatim from GDD.md by line. Gameplay '
                 'is scripted-input capture of the real main scene, same build; no human playtest exists. '
                 'No paid calls, no upload.'),
        'tags': ['Walker', 'Godot 4', 'game design document', 'tower defense', 'Claude', 'Kokoro', 'Remotion'],
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
                rk.still(take, frame, png)
                props['image'] = rk.data_uri(png)
                evidence.append({'path': f'evidence/{png.name}', 'sha256': rk.sha256(png),
                                 'method': f'engine viewport frame {frame} of take "{take}" (scripted input, '
                                           f'build caf082c), bars cropped',
                                 'supports': f'{bid}: {label}'})
    # copy the takes used as evidence into the reel and hash them
    for take in sorted({s['take'] for s in BEATS if s['kind'] == 'clip'}):
        for suffix in ('.mp4', '-inputs.jsonl'):
            src = rk.TAKES / f'{take}{suffix}'
            dst = REEL / f'capture/{take}{suffix}'
            shutil.copy2(src, dst)
        evidence.append({'path': f'capture/{take}.mp4', 'sha256': rk.sha256(REEL / f'capture/{take}.mp4'),
                         'method': 'scripted-input capture of the real main scene; engine viewport saved per '
                                   'frame at --fixed-fps 30; padded to 16:9 (see CAPTURE.md)',
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
              'document': {'path': '../../Walker-Godot-TowerDefense/GDD.md', 'sha256': rk.sha256(GDD),
                           'version': 'v0.1 agent draft, unapproved', 'commit': 'caf082c'},
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
