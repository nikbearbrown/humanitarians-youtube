import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'inside-captures'))
from clips import CLIPS, FACTS  # noqa: E402  (exact take windows, chosen by looking at the takes)

SLUG = 'claude-liam-nightyard-gdd'
TITLE = 'Night Yard: The Design Document Came Last'

ASK_COMMAND = ('Please use Walker to convert my game design document about a 2.5D brawler-platformer — a night shift in '
               'a container yard, three Y Bots to choose from, ledges, wall jumps, an axe and a hammer, and a Forewoman '
               'at the end — into a playable Godot project.')


def clip(name, **kw):
    c = CLIPS[name]
    return dict(kind='clip', status='observed', take=c['take'], segments=c['segments'], lead=0.3, **kw)


BEATS = [
 dict(id='B00', act='ASK', kind='composer',
  narration=("Hola, this is Liam, in for Bear. This is how Walker is meant to be asked: hand it a game design document, "
             "get back a playable Godot project. The prompt on screen is a reconstruction, not a transcript, because this "
             "game was rebuilt first, and its document came after."),
  props=dict(greeting='Hola, Liam', topic='WALKER · GODOT · GDD', segment='The Design Document',
             command=ASK_COMMAND, runningText='illustrative reconstruction — not the historical prompt',
             output=['What happened: a Unity platformer with no levels was rebuilt in Godot first.',
                     'GDD.md was written afterwards, from the evidence.'],
             folderLabel='@NikBearBrown', modelLabel='Opus 5.5', effortLabel='High')),
 dict(id='B01', act='BLUF', kind='writer', lead=0.8, tail=1.5,
  narration=("Night Yard came before its design document. Unity left a hundred and fifty scripts and a yard full of art, "
             "but no scenes, no levels and no sound. The rebuild made all six levels. The document was written last, "
             "and nothing in it is signed off."),
  props=dict(text=("Night Yard\nwas built from its design document.\n"
                   "Unity left scripts and art,\nbut no levels at all.\n"
                   "The document was written last,\nand nothing in it is signed off."),
             triggerWords='was built from', replacementWords='came before',
             fontSize=92, lineSpacing=1.3, charMs=22, mistakeRate=3, hesitateWithin=1, hesitateBetween=6,
             seed='nightyard-gdd-2026-11', ink='#3D3929', accent='#D97757', bg='#FAF9F5', face='serif',
             align='center', brandLabel='@NikBearBrown')),
 dict(id='B02', act='BODY', kind='board', status='comparison',
  sections=['Status vocabulary', '1. Metadata'], lines=(8, 8),
  narration=("The document separates six kinds of claim: recovered from the Unity code, invented for the rebuild, built, "
             "observed, proposed, or still waiting on a person. Built: seventeen scripts, five thousand lines. Observed: "
             f"the game's own playtest passes, and {FACTS['asserts_words']} assertions pass in this film's three scripted "
             "takes. Human playtests: zero."),
  props=dict(title='How the Document Labels a Claim', section='Status vocabulary · 1. Metadata',
             status='COMPARISON · built ≠ observed ≠ approved',
             visualLabel="Labels from the GDD's six-term vocabulary", layout='cards',
             cards=[{'label': 'Source · Authored', 'text': 'recovered from the Unity C#, or new in the rebuild'},
                    {'label': 'Implemented', 'text': '17 GDScript files, 5,215 lines'},
                    {'label': 'Observed', 'text': f"the game's playtest passes · {FACTS['asserts']} film-capture assertions"},
                    {'label': 'Pending', 'text': '0 human playtests · no section signed off'}]),
  cues=['recovered from', 'Built:', 'Observed:', 'Human']),
 dict(id='B03', act='BODY', kind='board', status='pending',
  sections=['2. Vision', '3. Pillars (PROPOSED)'], lines=(37, 37),
  narration=("The vision is a proposal: a night shift in a container yard. Climb the stacks, fight past the yard bots, "
             "take down the Forewoman. Who it's for is left open. The pillars are read off the code: move like a "
             "stuntman, fight with what you have, and read the yard."),
  props=dict(title='A Vision Nobody Signed', section='2. Vision · 3. Pillars',
             status='PROPOSED vision · audience PENDING', layout='cards',
             visualLabel='Pillars, proposed from the code',
             cards=[{'label': 'Move like a stuntman', 'text': 'ledge grab · wall jump · slide · running jump'},
                    {'label': 'Fight with what you have', 'text': 'a three-hit combo · the axe · the hammer'},
                    {'label': 'Read the yard', 'text': 'lights · spike plates · backs turned'}]),
  cues=['The vision', 'move like', 'fight with', 'read the yard']),
 clip('core_loop', id='B04', act='BODY', sections=['4. Core loop (IMPLEMENTED, OBSERVED)'],
  narration=("Here's the core loop on the real build, played by a script, not a person. The banner. A yard light is "
             "ten points. A bot knocked out is ten more. At a hundred the gate opens, the player walks through, and the "
             "panel shows the time.")),
 dict(id='B05', act='BODY', kind='board', status='proposed',
  sections=['5. Player-experience goals (PROPOSED, all PENDING a human playtest)'], lines=(61, 64),
  narration=("Four experience goals, all proposed, each with a test a person has to run. The captures can only hint. "
             "The script never fell in level one's pit by accident, because it knows the map. And it was knocked out "
             f"{FACTS['boss_kos_words']} by the Forewoman before it won. Whether that feels fair is a person's call."),
  props=dict(title='Goals Nobody Has Tested', section='5. Player-experience goals',
             status='PROPOSED · 4 goals · all PENDING a playtest', layout='cards',
             visualLabel='What the scripted run can and cannot say',
             cards=[{'label': 'PX-01 · the first ledge', 'text': 'script: knew the map in advance'},
                    {'label': 'PX-04 · a fight, not a wall', 'text': f"script: K.O.'d {FACTS['boss_kos']}× by the boss"}]),
  cues=['The captures', 'And it was']),
 dict(id='B06', act='BODY', kind='board', status='comparison',
  sections=['6. Mechanics'], lines=(70, 70),
  narration=("Movement follows Unity's controller: walk, run, a running turn, a double tap that runs. The rebuild "
             "measured the walking clip's stride, one point six five metres a second, and runs at five point two. "
             "One catch: the double tap is timed on the wall clock, not game time."),
  props=dict(title='Walking at the Speed of the Clip', section='M-01 · Movement',
             status='SOURCE vs IMPLEMENTED', layout='cards',
             visualLabel='Unity source vs. the Godot rebuild',
             cards=[{'label': 'Unity · MoveForward, CheckTurbo', 'text': 'walk · turbo run · double tap'},
                    {'label': 'Godot · fighter.gd', 'text': 'walk 1.65 m/s · run 5.2 m/s · 0.18 s double tap'}]),
  cues=['Movement follows', 'The rebuild', 'One catch']),
 clip('moves_run', id='B07', act='BODY', sections=['6. Mechanics'],
  narration=("In play: walk, run with Shift, and jump.")),
 dict(id='B08', act='BODY', kind='board', status='comparison',
  sections=['6. Mechanics'], lines=(74, 74),
  narration=("Jumping is tuned to the grid. A jump peaks at about two point one metres, so a two metre step can be "
             "jumped onto, and a three or four metre wall needs the ledge grab. A running jump clears a three wide gap. "
             "Holding into a wall while falling slows the fall, and jump kicks off it."),
  props=dict(title='Two Metres Up, Three Across', section='M-02 · Jumping and climbing',
             status='SOURCE moves · IMPLEMENTED numbers', layout='cards',
             visualLabel='From fighter.gd and the levels.gd movement rules',
             cards=[{'label': 'Unity · Jump, LedgeChecker, WallSlide', 'text': 'prep · jump · grab · slide · kick off'},
                    {'label': 'Godot · fighter.gd', 'text': 'apex 2.1 m · ledge for 3–4 m · 3-wide running jump'}]),
  cues=['Jumping is', 'A running jump', 'Holding into']),
 clip('shaft', id='B09', act='BODY', sections=['6. Mechanics'],
  narration=("Level two's shaft, in play: a wall slide, a kick off, the other wall, and up and out.")),
 dict(id='B10', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(83, 88),
  narration=("Combat ports Unity's attack system. Sixteen attacks, each with its own clip window and the hands, feet "
             "or blade that must actually touch. Three presses chain jab, cross and kick. The hammer does nine damage to "
             "a bot, can't be blocked, and recharges in nine seconds."),
  props=dict(title='Sixteen Attacks, Measured from the Clips', section='M-03 · Combat',
             status='SOURCE system · IMPLEMENTED table', layout='cards',
             visualLabel='From fighter.gd ATTACKS',
             cards=[{'label': 'Jab → cross → kick', 'text': 'attack ×3 · 0.34 → 0.34 → 0.5'},
                    {'label': 'Hammer', 'text': 'down + attack · 9.0 · unblockable · 9 s'}]),
  cues=['Combat ports', 'Three presses', 'The hammer']),
 clip('combo', id='B11', act='BODY', sections=['6. Mechanics'],
  narration=("In play: the combo, the uppercut, a block, and the hammer coming down.")),
 dict(id='B12', act='BODY', kind='board', status='comparison',
  sections=['6. Mechanics'], lines=(92, 92),
  narration=("Weapons come straight from Unity's scripts. Stand on the axe and attack to pick it up. Attack swings it, "
             "run and attack throws it, and down and attack puts it down. The thrown axe flies straight and spins."),
  props=dict(title='An Axe You Can Throw', section='M-04 · Weapons',
             status='SOURCE weapons · IMPLEMENTED inputs', layout='cards',
             visualLabel='From weapon.gd and fighter.gd',
             cards=[{'label': 'Unity · WeaponPickUp, WeaponThrow', 'text': 'pick up · swing · throw · put down'},
                    {'label': 'Godot · weapon.gd', 'text': 'run + attack throws · flies straight, spinning'}]),
  cues=['Weapons come', 'Attack swings', 'The thrown']),
 clip('axe_throw', id='B13', act='BODY', sections=['6. Mechanics'],
  narration=("Level three, in play: the axe picked up, and thrown.")),
 dict(id='B14', act='BODY', kind='board', status='comparison',
  sections=['6. Mechanics'], lines=(100, 100),
  narration=("The rules are Unity's numbers: a hundred HP, ten points a light, a hundred to win. A K.O., a spike plate or "
             "a fall sends you back to the last checkpoint. The plate fires point four seconds after something steps on "
             "it, and kills whoever is still standing there."),
  props=dict(title='A Hundred Points, a Hundred HP', section='M-05 · M-06 · Health, score, spike plates',
             status='SOURCE numbers · IMPLEMENTED plates', layout='cards',
             visualLabel='From HPManager, ScoreManager and spike_trap.gd',
             cards=[{'label': 'Unity · HPManager, ScoreManager', 'text': 'maxHP 100 · maxScore 100 · light 10'},
                    {'label': 'Godot · spike_trap.gd', 'text': 'fires 0.4 s after a step · retracts after 1.5 s'}]),
  cues=["The rules", 'A K.O.', 'The plate']),
 clip('spikes', id='B15', act='BODY', sections=['6. Mechanics'],
  narration=("A deliberate step onto the plate, in play: the spikes fire, and the player is back at the checkpoint.")),
 dict(id='B16', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(105, 105),
  narration=("The bots run Unity's AI: path over the level's links, jump or drop, attack in range, re-roll the attack "
             "every two seconds. New: they start unaware, which is what makes a takedown possible. The Forewoman has "
             "twelve HP, blocks often, and swings the hammer too."),
  props=dict(title='Bots That Have to Notice You', section='M-07 · The bots and the Forewoman',
             status='SOURCE AI · AUTHORED awareness and boss', layout='cards',
             visualLabel='From ai.gd and nav.gd',
             cards=[{'label': 'Unity · AIController, AIProgress', 'text': 'path links · attack in range · 2 s re-roll'},
                    {'label': 'Rebuild', 'text': 'unaware at start · Forewoman 12 HP, blocks, hammer'}]),
  cues=["The bots run", 'New:', 'The Forewoman']),
 clip('boss', id='B17', act='BODY', sections=['6. Mechanics'],
  narration=("The Forewoman, in play. The script gets knocked out, comes back from the checkpoint, and keeps hitting until "
             "the boss bar runs out.")),
 dict(id='B18', act='BODY', kind='board', status='implemented',
  sections=['6. Mechanics'], lines=(111, 116),
  narration=("Unity delivered no levels. All six are new, each built around one move: the first ledge, the wall jump "
             "shaft, the axe, the slide tunnel and the takedown, the hammer against a crowd of fourteen, and the boss. "
             "They're text maps on a one metre grid."),
  props=dict(title='Six Levels Unity Never Had', section='M-08 · Levels',
             status='AUTHORED · 6 text maps', layout='cards',
             visualLabel='From scripts/levels.gd',
             cards=[{'label': 'Maps', 'text': 'ASCII on a 1 m grid · built at runtime'},
                    {'label': 'One move each', 'text': 'ledge · wall jump · axe · slide · hammer · boss'}]),
  cues=['Unity delivered', 'each built', "They're text"]),
 dict(id='B19', act='BODY', kind='board', status='comparison',
  sections=['6. Mechanics'], lines=(123, 126),
  narration=("The menus port Unity's character select: hover a Y Bot and a light follows the mouse, click to choose, "
             "Enter to play. Around it, the rebuild adds the main menu, level select with best times, a pause menu with "
             "a restart key, and options."),
  props=dict(title='Pick Your Y Bot', section='M-09 · Menus, pause and scenes',
             status='SOURCE select · IMPLEMENTED menus', layout='cards',
             visualLabel='From character_select.gd, main_menu.gd and hud.gd',
             cards=[{'label': 'Unity · CharacterSelect, PlayGame', 'text': 'hover light · click · Return plays'},
                    {'label': 'Rebuild', 'text': 'menu · select level · pause · options'}]),
  cues=["The menus", 'Around it']),
 clip('select', id='B20', act='BODY', sections=['6. Mechanics'],
  narration=("In play: the hover light follows the cursor across the three Y Bots, a click chooses Yellow, and Play "
             "starts the shift.")),
 dict(id='B21', act='BODY', kind='board', status='implemented',
  sections=['7. World (AUTHORED)', '8. Art and audio'], lines=(130, 132),
  narration=("The world is authored: a yard at night on a side-view grid, with the industrial pack behind the lane, "
             "placed from a seed. Blocks between the camera and the player fade out. The three characters share every "
             "clip through Godot's humanoid retargeting. And the sound is new: the Unity export had none."),
  props=dict(title='Kit Art, Retargeted, Synthesized Sound', section='7. World · 8. Art and audio',
             status='AUTHORED world · art from the source folder', layout='cards',
             visualLabel='What the folders supplied',
             cards=[{'label': 'World', 'text': '1 m grid · seeded backdrop · cutaway fades'},
                    {'label': 'Art and audio', 'text': '3 rigs share 55 clips · 31 sounds synthesized'}]),
  cues=['The world', 'Blocks between', 'The three', 'And the sound']),
 dict(id='B22', act='BODY', kind='board', status='implemented',
  sections=['9. UI (IMPLEMENTED)', '10. Out of scope', '11. Technical'], lines=(155, 157),
  narration=("Under the hood, one class runs every fighter, the player and every bot, with the same eight input flags. "
             "The player's come from the keyboard; a bot's come from its brain. Out of scope, by decision: Unity's "
             "editor tools and demo code."),
  props=dict(title='One Fighter Class, Eight Flags', section='9. UI · 10. Out of scope · 11. Technical',
             status='IMPLEMENTED · scope set by the rebuild', layout='cards',
             visualLabel='From fighter.gd and level.gd',
             cards=[{'label': 'fighter.gd', 'text': 'player and bots · 8 input flags'},
                    {'label': 'Out of scope', 'text': 'editor tools · demo code · unused art'}]),
  cues=['Under the hood', "The player's", 'Out of scope']),
 dict(id='B23', act='BODY', kind='board', status='pending',
  sections=['12. Risks and known defects'], lines=(164, 164),
  narration=("The risks section records a defect the captures found. Open Options from the pause menu, go back, "
             "resume, and the pause key stops working: a hidden options panel keeps taking the key, so the game runs on "
             "with the pause panel drawn over it."),
  props=dict(title='A Pause Key That Stops Pausing', section='12. Risks and known defects',
             status='R-01 · found while capturing', layout='cards',
             visualLabel='From hud.gd and options_panel.gd',
             cards=[{'label': 'R-01', 'text': 'after Options, Esc no longer pauses'},
                    {'label': 'Cause', 'text': 'options_panel.gd:52-55 checks its own visible'}]),
  cues=['The risks', 'Open Options']),
 clip('r01', id='B24', act='BODY', sections=['12. Risks and known defects'],
  narration=("In play: Options, Back, Resume, then Esc. The pause panel comes back, but the game keeps running behind it.")),
 dict(id='B25', act='BODY', kind='board', status='pending',
  sections=['13. Acceptance tests (OBSERVED)', '14. Provenance', '15. Open questions (PENDING)'], lines=(172, 173),
  narration=("The game's own test plays every level, but it wires the bot brain straight into the player. The captures "
             "keep the player on the keyboard: the same brain decides, and its decisions become key presses. Five "
             "questions remain for a person, including whether the boss is fair."),
  props=dict(title='What a Person Still Has to Decide', section='13 · 14 · 15',
             status='PENDING · 5 open questions · 0 human playtests', layout='cards',
             visualLabel='Tests and open questions',
             cards=[{'label': 'Playtest', 'text': 'brain wired into the player · 418 s · PASS'},
                    {'label': 'Captures', 'text': 'same brain · key presses only'}]),
  cues=["The game's own", 'The captures', 'Five']),
 dict(id='B26', act='VERDICT', kind='verdict',
  narration=("Verdict. This document organizes; it doesn't approve. The loop runs end to end on real key presses, "
             "through six levels, the Forewoman and the credits, and through the failures. The rebuild's own levels are "
             "labelled. One defect slipped past the game's own test. What's left is a person's call: the audience, the "
             "story, and whether the boss is fair."),
  props=dict(artifactTitle='Verdict', artifactHeading='Organized, not approved', brandLabel='@NikBearBrown',
             artifactLines=['Observed end to end: menu → select → 6 levels → credits; falls, spikes, pause.',
                            f"Checks: the game's playtest passes · {FACTS['asserts']} film-capture assertions pass.",
                            'Found: after Options, the pause key stops pausing (R-01).',
                            'Pending a person: audience, story, boss fairness, 0 playtests.'])),
 dict(id='B27', act='HANDOFF', kind='composer',
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
 dict(id='B28', act='OUTRO', kind='outro', tail=1.0,
  narration=f'{TITLE}. At Nik Bear Brown.',
  props=dict(title=TITLE, slug=SLUG, handle='@NikBearBrown', subline='')),
]
