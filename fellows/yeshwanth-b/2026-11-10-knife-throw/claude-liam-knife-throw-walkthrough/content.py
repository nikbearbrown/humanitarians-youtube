SLUG = 'claude-liam-knife-throw-walkthrough'
TITLE = 'Gino: Knife Throw, Every Feature, Played'

ASK = ('Please use Walker to convert my game design document about a 2D action platformer — guide Gino home '
       'through three hostile valleys with a sword combo, three throwing knives and three hearts — into a '
       'playable Godot project.')

GREETING_NARR = ("Hola, this is Liam, in for Bear. This is how Walker is meant to be asked: a game design document in, "
                 "a playable Godot project out. The prompt is a reconstruction. This game was a Unity platformer with "
                 "scripts and art but no levels, rebuilt in Godot with three.")
OUTPUT = ['Built: 3 levels, 3 enemy types, 14 scripts and a shader.',
          'Played here: 3 scripted-input takes, 46 of 46 assertions passing.']

BLUF_NARR = ("Gino: Knife Throw is a side-scrolling action platformer: a sword combo, three knives, three hearts, "
             "and a door at the end of each level. Every feature here is played through real key, mouse and "
             "gamepad input, by a script. Nobody has played it by hand yet.")
BLUF_PROPS = dict(text=("Gino: Knife Throw\nis an endless runner.\nThree levels and a door."),
                  triggerWords='an endless runner', replacementWords='an action platformer',
                  seed='knife-throw-walkthrough-2026-11')

CLIPS = [
 dict(id='B02', take='campaign', start=0, end=314, lead=0.3,
  narration=('The main menu, best score zero. How to Play lists every key, the controller, and the rules. Escape steps back. New Game.')),
 dict(id='B03', take='campaign', start=314, end=600, lead=0.3,
  narration=('Level one, Rocky Outskirts, the tutorial. A crystal stops play with a hint: A and D run, Space jumps. Enter closes it.')),
 dict(id='B04', take='campaign', start=600, end=1000, lead=0.3,
  narration=("A walker, the green fish-cat, turns to face Gino and runs at him. The script waits for it to come into sword range, then slashes with J. It flashes white on every hit, and a few slashes later it's gone: twenty-five points.")),
 dict(id='B05', take='campaign', start=1000, end=1490, lead=0.3,
  narration=("A glowing dagger refills the knife count, shown under the hearts. Then the bat. It wakes when Gino "
             "gets close and swoops in, and the sword brings it down. Diamonds, ten points small and fifty big, "
             "sit on floating ledges.")),
 dict(id='B06', take='campaign', start=1490, end=2000, lead=0.3,
  narration=('Spikes cost half a heart; a pit costs the level. K throws a knife: straight, thirty damage. The sword finishes the walker. Two snapper plants are left alone: their snap outreaches the blade. Then the door, and W.')),
 dict(id='B07', take='campaign', start=2000, end=2300, lead=0.3,
  narration=('Level complete: a hundred thirty-five points, three of five enemies. Thorn Hollow, under a red moon. Bats curl up before they strike.')),
 dict(id='B08', take='campaign', start=2300, end=2850, lead=0.3,
  narration=("A walker waits below a rock to bite Gino on landing. So the script leaps long, lands past it, and fights on the flat: the script's rule, not the game's. Then a rope bridge over a spike pit, a bat on the far side, and another glowing dagger for the knife count.")),
 dict(id='B09', take='campaign', start=2850, end=3460, lead=0.3,
  narration=('A knife at a bat, then the sword finishes it. Then the climb: one-way ledges that Gino jumps up through from below, onto a long cliff top. Another bat is waiting up there. The second hint says knives fly straight and far, so thin the herd before you drop back down.')),
 dict(id='B10', take='campaign', start=3460, end=3940, lead=0.3,
  narration=("The drop off the cliff lands near the last walker. The script steps off the rim instead of jumping, "
             "so it lands short and the walker has to come to it. Defeated, then the door: level two, with all "
             "three hearts.")),
 dict(id='B11', take='campaign', start=3940, end=4330, lead=0.3,
  narration=("Four hundred and seventy points, seventeen of twenty-two diamonds. Level three, Moonlit Depths: the "
             "dark tileset, music for the cave, and stalactites. Mind your jumps. Twelve enemies live down "
             "here.")),
 dict(id='B12', take='campaign', start=4330, end=4980, lead=0.3,
  narration=('Walkers and bats, one at a time, each one a few slashes. The script stands still and lets each enemy come to it, because both chase slower than Gino runs. Here Gino runs onto floor spikes: half a heart, and a knockback. The heart bar shows the half. Then a knife at a plant, thrown from outside its reach.')),
 dict(id='B13', take='campaign', start=4980, end=5520, lead=0.3,
  narration=("Rock pillars between spike pits. A walker waits across the gap, and it won't cross: walkers never step off a ledge. Gino jumps the gap and lands past it, but the bite still lands: a full heart. A heart and a half left. The walker goes down anyway, and there's another dagger.")),
 dict(id='B14', take='campaign', start=5520, end=6100, lead=0.3,
  narration=("The rope bridge hint: the bridge holds, the spikes below don't forgive. A knife for the plant, and a "
             "fight on the bridge. Its right end stops one tile short of the rock: a sixteen pixel hole. "
             "In a trial run, Gino fell through it.")),
 dict(id='B15', take='campaign', start=6100, end=6720, lead=0.3,
  narration=("Near the end, a plant rears up and snaps as Gino runs past: a full heart, and one half heart left. A person would slow down here. The script doesn't know it's close. Two more enemies, the last hint, the way out, and the door. Level three, cleared on one half heart.")),
 dict(id='B16', take='campaign', start=6720, end=7100, lead=0.3,
  narration=("Eight hundred and five points, nine of twelve enemies, a minute nineteen. Finish rolls the credits: "
             "The End, the final score, diamonds and enemies for the whole run, and the best score.")),
 dict(id='B17', take='campaign', start=7100, end=7686, lead=0.3,
  narration=('The credits list the art pack, the fonts from the original project, the sound synthesized for this rebuild, and the three levels. Then they fade, and the main menu is back, now with Continue, level three, and a best score of eight oh five. Progress is saved.')),
 dict(id='B18', take='defeat', start=0, end=640, lead=0.3,
  narration=('A second take, for the failure path. The menu now offers Continue, but the script picks New Game. Escape pauses: Resume, Restart, Sound and Main Menu. Resume. Then the take replays the start of level one: the same hints, the first walker, the first bat.')),
 dict(id='B19', take='defeat', start=640, end=1440, lead=0.3,
  narration=("Each slash shows its own arc and a hit flash. The script lands single slashes and short chains. The full four-hit combo, with the magic blast as its fourth hit, never appears in these takes, because each hit knocks the enemy back out of reach. The game's own playtest checks the four-hit chain, off screen. A dagger, the bat, and the spike hint.")),
 dict(id='B20', take='defeat', start=1440, end=1662, lead=0.3,
  narration=('Now on purpose: the script runs Gino into a pit. Gino is down. Retry starts the level over.')),
 dict(id='B21', take='defeat', start=1662, end=1973, lead=0.3,
  narration=('Escape, then R restarts the level, but the log shows a script error at level dot g d, line seven sixty-one.')),
 dict(id='B22', take='extras', start=0, end=439, lead=0.3,
  narration=('A third take covers the other inputs. On the menu, the Sound button turns sound off, then on again. In play, the arrow keys run instead of A and D, and Space still jumps. M toggles sound anywhere, without a menu.')),
 dict(id='B23', take='extras', start=439, end=807, lead=0.3,
  narration=("Now a simulated gamepad, not a real controller. The left stick runs Gino into a hint, and the pad's A button closes it. Start pauses and Start resumes. Escape, then Main Menu.")),
]

FEATURES = [
 ('main-menu', 'B02', 'campaign', 40, 'Main menu: New Game, How to Play, Sound: On, Quit, best score 0.', 'An empty save shows no Continue.'),
 ('how-to-play', 'B02', 'campaign', 150, 'How to Play: keys, controller, the rules.', 'One page holds every control.'),
 ('escape-back', 'B02', 'campaign', 253, 'Esc on How to Play returns to the main menu.', 'The pause action doubles as back.'),
 ('new-game', 'B03', 'campaign', 315, 'New Game loads level 1.', 'Score and knives reset.'),
 ('level-intro', 'B03', 'campaign', 330, 'LEVEL 1 ROCKY OUTSKIRTS banner.', 'Each level opens with its name.'),
 ('hint-crystal', 'B03', 'campaign', 380, 'A crystal opens a hint; Enter closes it.', 'Unity Hint.cs; delay 1.2 s here.'),
 ('move-jump', 'B03', 'campaign', 450, 'A / D run, Space jumps.', 'Hold Space for a higher jump.'),
 ('walker', 'B04', 'campaign', 760, 'A walker runs at Gino and is slashed four times.', 'Enemy2.cs port.'),
 ('slash', 'B04', 'campaign', 731, 'J slashes; the enemy flashes white.', '20 damage per slash.'),
 ('kill-points', 'B04', 'campaign', 833, 'Defeated enemy: +25.', 'POINTS 25.'),
 ('dagger-pickup', 'B05', 'campaign', 1299, 'A dagger refills the knife count to 1.', 'Capped at 3.'),
 ('bat', 'B05', 'campaign', 1250, 'A bat swoops in and is slashed down.', 'Enemy1.cs port, no A*.'),
 ('diamonds', 'B05', 'campaign', 1100, 'Diamonds on ledges add 10 or 50.', 'Coin.changeScore.'),
 ('knife-throw', 'B06', 'campaign', 1610, 'K throws a knife that flies straight.', '30 damage.'),
 ('plants-avoided', 'B06', 'campaign', 1800, 'Two plants are passed, not fought.', 'Their snap outreaches the sword.'),
 ('door', 'B06', 'campaign', 1996, 'W at the door finishes the level.', 'Unity Door.cs.'),
 ('level-complete', 'B07', 'campaign', 2100, 'LEVEL COMPLETE: 135, 6/10 diamonds, 3/5 enemies, 0:43.', 'A panel the Unity UI had as a victory screen.'),
 ('next-level', 'B07', 'campaign', 2160, 'Next Level loads Thorn Hollow.', 'Knives and score carry over.'),
 ('moon', 'B07', 'campaign', 2200, 'Level 2 under the red moon.', 'Lifted from the menu background.'),
 ('rope-bridge', 'B08', 'campaign', 2700, 'A rope bridge over a spike pit.', 'Built from the bridge sprite.'),
 ('one-way-ledges', 'B09', 'campaign', 3200, 'Gino jumps up through one-way ledges.', 'Grid value 2.'),
 ('high-road', 'B09', 'campaign', 3300, 'A long cliff top with a bat.', 'Level 2 design.'),
 ('level-2-clear', 'B10', 'campaign', 3912, 'Level 2 cleared with full health.', 'Health 6 at the door.'),
 ('level-3', 'B11', 'campaign', 4100, 'Moonlit Depths: dark tiles, stalactites.', 'Level 3 design.'),
 ('spike-damage', 'B12', 'campaign', 4816, 'Floor spikes: half a heart and knockback.', 'Spike.cs.'),
 ('half-heart', 'B12', 'campaign', 4830, 'The heart bar shows a half heart.', 'HeartUI.cs halves.'),
 ('enemy-bite', 'B13', 'campaign', 5366, 'A walker bite costs a full heart.', 'EnemyAttack dmg = 2.'),
 ('bridge-hole', 'B14', 'campaign', 6000, 'The level 3 bridge stops one tile short of the rock.', 'Defect R-01; the take jumps it.'),
 ('plant-snap', 'B15', 'campaign', 6368, 'A plant snap: one half heart left.', 'Enemy3.cs port.'),
 ('level-3-clear', 'B15', 'campaign', 6694, 'Level 3 cleared on health 1.', 'Close.'),
 ('finish-credits', 'B16', 'campaign', 6900, 'Finish rolls the credits: THE END and run totals.', 'Credit.cs.'),
 ('credits-return', 'B17', 'campaign', 7592, 'The credits fade to the main menu.', 'Back to the start.'),
 ('continue-best', 'B17', 'campaign', 7640, 'Main menu offers Continue (Level 3); best score 805.', 'Saved to the capture copy only.'),
 ('pause-esc', 'B18', 'defeat', 160, 'Esc opens PAUSED: Resume, Restart, Sound, Main Menu.', 'Pause stops play.'),
 ('resume', 'B18', 'defeat', 232, 'Resume closes the pause menu.', 'Back to play.'),
 ('slash-effects', 'B19', 'defeat', 700, 'Slash arcs and hit flashes.', 'Only short chains in the takes.'),
 ('pit-death', 'B20', 'defeat', 1487, 'Falling into a pit loses the level.', 'Hole.cs.'),
 ('game-over', 'B20', 'defeat', 1560, 'GINO IS DOWN: Retry, Main Menu.', 'Score kept from entering the level.'),
 ('retry', 'B20', 'defeat', 1659, 'Retry restarts level 1 with full health.', 'Asserted.'),
 ('r-restart', 'B21', 'defeat', 1784, 'R on the pause menu restarts; SCRIPT ERROR at level.gd:761.', 'Works, with an error.'),
 ('pause-main-menu', 'B21', 'defeat', 1926, 'Main Menu from the pause menu.', 'Back to the start.'),
 ('menu-sound', 'B22', 'extras', 69, 'The menu Sound button toggles On / Off.', 'Audio autoload.'),
 ('arrow-keys', 'B22', 'extras', 250, 'Arrow keys run.', 'Second key set.'),
 ('m-sound', 'B22', 'extras', 375, 'M toggles sound in play.', 'GameState global key.'),
 ('pad-stick', 'B23', 'extras', 460, 'The left stick runs Gino.', 'Synthetic joypad events.'),
 ('pad-a-hint', 'B23', 'extras', 609, 'Pad A closes a hint.', 'confirm is bound to A.'),
 ('pad-start', 'B23', 'extras', 640, 'Start pauses and Start resumes.', 'Pad pause binding.'),
]

NOT_SHOWN = [
 ('four-hit-combo', 'The full four-hit chain and the Attack4 magic blast never occur in the takes; the game playtest checks it.'),
 ('air-attack', 'The jump attack (J in the air) was not pressed.'),
 ('heart-pickup', 'Heart pickups were not collected in the takes.'),
 ('alt-attack-keys', 'X to slash, C to throw, pad X / Y / B slashing and throwing in play were not exercised.'),
 ('fullscreen', 'F11 / Alt+Enter was not pressed, to keep the fixed capture window.'),
 ('quit', 'The Quit button was not clicked.'),
 ('focus-loss-pause', 'The game pauses when its window loses focus; avoided while recording.'),
 ('game-audio', 'The game has synthesized music and sound effects; game audio was not captured. Narration only.'),
]

VERDICT_NARR = ("Verdict. Every level, the credits, defeat and retry play through real input, and forty-six assertions "
                "pass. Two defects: level three's bridge has a hole at one end, and R on a menu logs a script error. "
                "And the script finished level three on half a heart. Whether that's tense or unfair is a person's "
                "call.")
VERDICT_LINES = ['Observed: menu → 3 levels → credits → Continue; and pit → game over → retry.',
                 'Checks: 46 of 46 film-capture assertions pass; the game\'s own playtest passes.',
                 'Defects: a 16 px hole at the end of level 3\'s bridge; R logs a SCRIPT ERROR (level.gd:761).',
                 'Untested: a human playtest, the four-hit combo on screen, Windows, game audio.']
