SLUG = 'claude-liam-nightyard-walkthrough'
TITLE = 'Night Yard, Every Feature, Played'

ASK = ('Please use Walker to convert my game design document about a 2.5D brawler-platformer — a night shift in '
       'a container yard, three Y Bots to choose from, ledges, wall jumps, an axe and a hammer, and a Forewoman '
       'at the end — into a playable Godot project.')

GREETING_NARR = ("Hola, this is Liam, in for Bear. This is how Walker is meant to be asked: a game design document in, "
                 "a playable Godot project out. The prompt is a reconstruction. This game was a Unity platformer with "
                 "scripts and art but no levels, rebuilt in Godot with six.")
OUTPUT = ['Built: 6 levels, 3 Y Bots, 17 scripts, 5,215 lines.',
          'Played here: 3 scripted-input takes, 78 of 78 assertions passing.']

BLUF_NARR = ("Night Yard is a side-view brawler-platformer. You climb container stacks and fight yard bots to reach the "
             "Forewoman. Every feature here is played by a script: the game's own bot brain decides, and its decisions "
             "go in as real key presses. Nobody has played it by hand yet.")
BLUF_PROPS = dict(text=("Night Yard\nis a racing game.\nSix levels, one boss."),
                  triggerWords='a racing game', replacementWords='a brawler-platformer',
                  seed='nightyard-walkthrough-2026-11')

C, D, E = 'campaign', 'defeat', 'extras'

CLIPS = [
 dict(id='B02', take=C, start=45, end=297, lead=0.3,
  narration=("The main menu, over the yard at night. How to play lists the keys, the moves and the controller. Back, "
             "then New game.")),
 dict(id='B03', take=C, start=414, end=700, lead=0.3,
  narration=("The character select, ported from Unity: a light follows the cursor over each Y Bot. A click picks "
             "Yellow, and Play starts the shift.")),
 dict(id='B04', take=C, start=700, end=1000, lead=0.3,
  narration=("Level one, Clock In. A hint teaches each key as you reach it. The script walks, jumps onto the block, "
             "and the first yard light is plus ten.")),
 dict(id='B05', take=C, start=1000, end=1330, lead=0.3,
  narration=("A ledge too high to jump: the player grabs it and climbs. A yard bot on top. A running attack is a flying "
             "kick, and the bot goes down: ten more points.")),
 dict(id='B06', take=C, start=1330, end=1700, lead=0.3,
  narration=("Another ledge, more lights. At a hundred points the gate opens, and the HUD says so. The green lamp is a "
             "checkpoint.")),
 dict(id='B07', take=C, start=1700, end=2036, lead=0.3,
  narration=("Past the spike plates to the gate. Walking through it ends the level: the Level Clear panel shows the "
             "time, the score, bots knocked out, and times K.O.'d. Next level.")),
 dict(id='B08', take=C, start=2036, end=2420, lead=0.3,
  narration=("Level two, Stacks. Container stacks, grabbed and climbed one after another. A long drop ends in a roll.")),
 dict(id='B09', take=C, start=2420, end=2775, lead=0.3,
  narration=("Bots at the foot of the shaft: jab, cross and kick. Then the shaft itself. Hold into the wall and the fall "
             "slows. Jump, and the player kicks off to the other wall and grabs the top.")),
 dict(id='B10', take=C, start=2820, end=3054, lead=0.3,
  narration=("More bots, more stacks. The script fights whatever stands between it and the next light, and climbs on.")),
 dict(id='B11', take=C, start=3420, end=3640, lead=0.3,
  narration=("Down to the gate, and level two is clear. The panel's best time is saved for level select.")),
 dict(id='B12', take=C, start=3827, end=4120, lead=0.3,
  narration=("Level three, Axe to Grind. Stand on the axe and attack to pick it up. Run and attack, and it's thrown: it "
             "flies straight, spinning, into the bot.")),
 dict(id='B13', take=C, start=4120, end=4371, lead=0.3,
  narration=("Bots on the catwalks above. The script climbs up to them, fights on the narrow steel, and finds the second "
             "axe.")),
 dict(id='B14', take=C, start=4760, end=4999, lead=0.3,
  narration=("Ledge grabs work with the axe in hand. Up on the catwalk, run and attack throws it again, from a "
             "distance.")),
 dict(id='B15', take=C, start=5320, end=5603, lead=0.3,
  narration=("Down and attack on the ground brings down the hammer: a ground shock that throws the bots around it, and "
             "then a nine second recharge.")),
 dict(id='B16', take=C, start=5720, end=5879, lead=0.3,
  narration=("The last ledge, the gate, and level three is clear.")),
 dict(id='B17', take=C, start=6157, end=6454, lead=0.3,
  narration=("Level four, Spike Alley. Plates to jump. Then a tunnel one metre high: run, press down, and the player "
             "slides through.")),
 dict(id='B18', take=C, start=6520, end=6741, lead=0.3,
  narration=("A bot ahead, and the hammer again. The HUD's hammer charge counts back to ready.")),
 dict(id='B19', take=C, start=6900, end=7341, lead=0.3,
  narration=("A climb, and then a bot with its back turned. It hasn't noticed the player, so an attack from behind is a "
             "takedown: a paired animation, and the bot is out.")),
 dict(id='B20', take=C, start=7400, end=7531, lead=0.3,
  narration=("The gate, and level four is clear.")),
 dict(id='B21', take=C, start=7615, end=7859, lead=0.3,
  narration=("Level five, Hangar Brawl: fourteen bots. The hammer clears a crowd, and the score climbs ten at a time.")),
 dict(id='B22', take=C, start=8000, end=8255, lead=0.3,
  narration=("Amy blocks and combos back; the yard bots swarm. The script keeps its hammer for the crowds and kicks the "
             "rest.")),
 dict(id='B23', take=C, start=8460, end=8706, lead=0.3,
  narration=("Up onto the containers, a flying kick from above, and the hammer twice more. No K.O. in this level.")),
 dict(id='B24', take=C, start=9000, end=9133, lead=0.3,
  narration=("Fourteen of fourteen, and the gate.")),
 dict(id='B25', take=C, start=9296, end=9570, lead=0.3,
  narration=("Level six, The Forewoman. Her name and health bar sit at the bottom of the screen. Lights first; an axe "
             "is picked up on the way.")),
 dict(id='B26', take=C, start=11400, end=11760, lead=0.3,
  narration=("Something the film doesn't hide. On the first try, the script stood on a container for a minute and made no "
             "progress, so the driver's stall guard restarted the level from the pause menu.")),
 dict(id='B27', take=C, start=11760, end=12069, lead=0.3,
  narration=("Second try. This time the axe goes to the boss: four swings, and her bar drops from twelve to ten. She "
             "blocks often, and shrugs off light hits.")),
 dict(id='B28', take=C, start=12260, end=12674, lead=0.3,
  narration=("Kicks, and her hammer comes back at the player. K.O.: back to the checkpoint, with full HP.")),
 dict(id='B29', take=C, start=12720, end=13100, lead=0.3,
  narration=("The script comes straight back, and she knocks it out again. Each round, her bar is a little shorter.")),
 dict(id='B30', take=C, start=13520, end=13970, lead=0.3,
  narration=("More K.O.s, five in all, and then the last kicks land. The Forewoman goes down, and the gate opens.")),
 dict(id='B31', take=C, start=14560, end=14840, lead=0.3,
  narration=("Through the gate, and You Win: five K.O.s, one minute forty four. Credits.")),
 dict(id='B32', take=C, start=14850, end=15022, lead=0.3,
  narration=("The credits roll over the yard, then the game returns to the menu.")),
 dict(id='B33', take=D, start=45, end=278, lead=0.3,
  narration=("A second take. The menu now offers Continue. Select level lists all six with their best times.")),
 dict(id='B34', take=D, start=298, end=651, lead=0.3,
  narration=("Level one again, and a deliberate mistake: the script walks off the edge into the pit. A fall is a K.O., "
             "and the player is back at the start.")),
 dict(id='B35', take=D, start=1483, end=1760, lead=0.3,
  narration=("At the checkpoint, a step onto the plate. It fires a moment later, the spikes kill, and the respawn is at "
             "the checkpoint, not the start.")),
 dict(id='B36', take=D, start=1760, end=1925, lead=0.3,
  narration=("Escape pauses. R, while paused, restarts the level.")),
 dict(id='B37', take=D, start=1960, end=2313, lead=0.3,
  narration=("Now a defect. Options from the pause menu, Back, Resume, then Escape. The pause panel appears, but the game "
             "is still running behind it: a hidden options panel is taking the key.")),
 dict(id='B38', take=E, start=45, end=254, lead=0.3,
  narration=("A third take. The main menu's Options: volumes, quality, screen shake and hints.")),
 dict(id='B39', take=E, start=254, end=560, lead=0.3,
  narration=("Change fighter, with the arrow keys: Red, Green. But the arrows also move the button focus, so Enter lands "
             "on Back. The game returns to the menu, and the choice is lost.")),
 dict(id='B40', take=E, start=560, end=755, lead=0.3,
  narration=("Select level shows the best times saved by the first take. Level one.")),
 dict(id='B41', take=E, start=790, end=1037, lead=0.3,
  narration=("The move list, by key. J twice: jab and cross. Up and J: uppercut. K blocks. Down and J: the hammer.")),
 dict(id='B42', take=E, start=1044, end=1191, lead=0.3,
  narration=("Shift runs, and down while running slides.")),
 dict(id='B43', take=E, start=1191, end=1433, lead=0.3,
  narration=("Then a synthetic gamepad. The left stick walks, A jumps, X attacks, and Start pauses. Quit to menu.")),
 dict(id='B44', take=E, start=1472, end=1720, lead=0.3,
  narration=("Credits from the menu, and Escape leaves them.")),
]

FEATURES = [
 ('main-menu', 'B02', C, 60, 'Main menu over the night yard.', 'Added menu.'),
 ('how-to-play', 'B02', C, 250, 'How to play lists keys, moves and controller.', 'Added page.'),
 ('select-hover', 'B03', C, 520, 'A hover light follows the cursor over each Y Bot.', 'CharacterHoverLight.'),
 ('select-click', 'B03', C, 609, 'A click selects Yellow.', 'CharacterSelect / MouseControl.'),
 ('play', 'B03', C, 688, 'Play starts level 1.', 'PlayGame.'),
 ('level-banner', 'B04', C, 720, 'The level banner names the level.', 'Added banner.'),
 ('hints', 'B04', C, 820, 'Hints teach each key at the map cell.', 'Map hints.'),
 ('jump', 'B04', C, 940, 'Space jumps onto a 2 m block.', 'Jump, apex 2.1 m.'),
 ('pickup-light', 'B04', C, 985, 'A yard light is +10.', 'PickupItem.scoreValue 10.'),
 ('ledge-grab', 'B05', C, 1152, 'A ledge is grabbed and climbed.', 'LedgeChecker.'),
 ('flying-kick', 'B05', C, 1187, 'Run + attack is a flying kick.', 'AITriggerAttack.FlyingKick.'),
 ('bot-ko', 'B05', C, 1300, 'A bot knocked out is +10.', 'Added scoring.'),
 ('gate-open', 'B06', C, 1610, 'At 100 points the gate opens.', 'ScoreManager.maxScore 100.'),
 ('checkpoint', 'B06', C, 1690, 'A checkpoint lamp lights.', 'Added checkpoint.'),
 ('level-clear', 'B07', C, 2000, 'Level Clear: time, best, score, KOs, deaths.', 'Added panel.'),
 ('climb-stacks', 'B08', C, 2254, 'Container stacks climbed ledge by ledge.', 'Ledge climb.'),
 ('roll', 'B08', C, 2411, 'A long drop ends in a roll.', 'Landing roll above 3.2 m.'),
 ('combo', 'B09', C, 2470, 'Jab, cross, kick chain on repeated attacks.', 'TransitionIndexer combo.'),
 ('wall-slide', 'B09', C, 2734, 'Holding into a wall slows the fall.', 'WallSlide 2.2 m/s.'),
 ('wall-jump', 'B09', C, 2736, 'Jump kicks off the wall to the other side.', 'WallJumpPrep.'),
 ('axe-pickup', 'B12', C, 3984, 'Attack while standing on the axe picks it up.', 'WeaponPickUp.'),
 ('axe-throw', 'B12', C, 4002, 'Run + attack throws the axe.', 'WeaponThrow.'),
 ('ledge-with-axe', 'B14', C, 4817, 'A ledge grab with the axe in hand.', 'Added.'),
 ('hammer', 'B15', C, 5550, 'Down + attack brings down the hammer.', 'SpawnObject HAMMER.'),
 ('slide', 'B17', C, 6434, 'Run + down slides through a 1 m tunnel.', 'Slide.'),
 ('hammer-charge', 'B18', C, 6721, 'The HUD hammer charge counts down.', 'HUD.'),
 ('takedown', 'B19', C, 7321, 'Attack behind an unaware bot is a takedown.', 'InstaKill.'),
 ('crowd', 'B21', C, 7747, 'A crowd of 14 bots; the hammer clears it.', 'Level 5.'),
 ('amy', 'B22', C, 8100, 'Amy blocks and combos back.', 'Added brawler.'),
 ('boss-bar', 'B25', C, 9400, "The Forewoman's health bar.", 'Added boss bar.'),
 ('stall-restart', 'B26', C, 11610, 'Restart level from the pause menu (the driver, after a stall).', 'Pause menu.'),
 ('axe-on-boss', 'B27', C, 11994, 'The axe on the boss: 12 → 10 HP.', 'Axe 1.0 a swing.'),
 ('ko-screen', 'B28', C, 12654, "K.O.: back to the checkpoint.", 'Respawn 2.6 s.'),
 ('boss-down', 'B30', C, 13950, 'The Forewoman goes down; the gate opens.', 'Boss level gate.'),
 ('you-win', 'B31', C, 14800, 'You Win panel; Credits.', 'Last level.'),
 ('credits', 'B32', C, 15000, 'The credits roll, then the menu.', 'Credits.'),
 ('continue-button', 'B33', D, 60, 'Continue offers the furthest level.', 'Saved progress.'),
 ('select-level', 'B33', D, 160, 'Select level lists best times.', 'Saved best times.'),
 ('fall-ko', 'B34', D, 631, 'A fall into the pit is a K.O.; back to the start.', 'FALL_Y −3.'),
 ('spike-death', 'B35', D, 1645, 'A spike plate fires and kills.', 'TrapSpikes.'),
 ('checkpoint-respawn', 'B35', D, 1740, 'Respawn at the checkpoint.', 'Checkpoints.'),
 ('pause', 'B36', D, 1800, 'Esc pauses.', 'Pause.'),
 ('restart-key', 'B36', D, 1845, 'R while paused restarts the level.', 'Restart action.'),
 ('options-in-pause', 'B37', D, 1980, 'Options from the pause menu.', 'OptionsPanel.'),
 ('options-defect', 'B37', D, 2234, 'After Options, Esc shows the panel but does not pause.', 'Defect R-01.'),
 ('options-menu', 'B38', E, 150, 'Options: volumes, quality, screen shake, hints.', 'OptionsPanel.'),
 ('select-arrows', 'B39', E, 360, 'Arrow keys choose a Y Bot.', 'Added keys.'),
 ('select-enter-defect', 'B39', E, 505, 'Enter lands on Back; the choice is not saved.', 'Defect R-02.'),
 ('uppercut', 'B41', E, 852, 'Up + attack is an uppercut.', 'Uppercut 1.0.'),
 ('block', 'B41', E, 910, 'K blocks.', 'Block.'),
 ('run-slide', 'B42', E, 1161, 'Shift runs; down while running slides.', 'Slide.'),
 ('pad-move', 'B43', E, 1210, 'The left stick walks.', 'Joypad.'),
 ('pad-attack', 'B43', E, 1290, 'X attacks.', 'Joypad.'),
 ('pad-start', 'B43', E, 1360, 'Start pauses.', 'Joypad.'),
 ('credits-esc', 'B44', E, 1700, 'Esc leaves the credits.', 'Credits input.'),
]

NOT_SHOWN = [
 ('red-green-fighters', 'Red and Green were chosen on the select screen but never played: the choice was lost to defect R-02, and every level ran with Yellow.'),
 ('stomp-dragon-sweep', 'The stomp, dragon punch, sweep and air smash were not singled out; the bot brain chose its own attacks.'),
 ('mouse-attack-block', 'The left and right mouse buttons were not used to attack or block; J and K were.'),
 ('double-tap-run', 'The double-tap run was not used (timed on the wall clock; see CAPTURE.md); Shift was.'),
 ('options-changes', 'No option value was changed.'),
 ('fullscreen', 'F11 / Alt+Enter was not pressed, to keep the fixed capture window.'),
 ('exit', 'The Exit button was not clicked.'),
 ('game-audio', 'The game has synthesized music and sound effects; game audio was not captured. Narration only.'),
]

VERDICT_NARR = ("Verdict. All six levels, the Forewoman, the credits, the failures and the other inputs play through real "
                "key presses, and seventy-eight assertions pass. Two defects: after Options, the pause key stops pausing, "
                "and at the character select, the arrow keys can send Enter to Back. Whether it's fair, or fun, is a "
                "person's call.")
VERDICT_LINES = ['Observed: menu → select → 6 levels → credits; and falls, spikes, pause, restart.',
                 "Checks: 78 of 78 film-capture assertions pass; the game's own playtest passes.",
                 'Defects: the pause key stops after Options; arrows send Enter to Back.',
                 'Untested: a human playtest, Windows, Red and Green in play, game audio.']
