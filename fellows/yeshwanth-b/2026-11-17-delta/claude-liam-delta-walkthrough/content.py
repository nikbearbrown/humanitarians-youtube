SLUG = 'claude-liam-delta-walkthrough'
TITLE = 'Delta, Every Feature, Played'

ASK = ('Please use Walker to convert my game design document about a first-person puzzle game — a space station '
       'folded into two layers, energy cells carried between machines, and an unstable core taken past two '
       'guardians — into a playable Godot project.')

GREETING_NARR = ("Hola, this is Liam, in for Bear. This is how Walker is meant to be asked: a game design document in, "
                 "a playable Godot project out. The prompt is a reconstruction. This game was a Unity first-person "
                 "puzzle game with scripts and art but no levels, rebuilt in Godot with twelve.")
OUTPUT = ['Built: 12 levels, 2 station layers, 27 scripts and 3 shaders.',
          'Played here: 4 scripted-input takes, 90 of 90 assertions passing.']

BLUF_NARR = ("Delta is a first-person puzzle game. A space station folded into two layers, fifty metres apart, and "
             "you shift between them carrying energy cells. Every feature here is played through real keyboard, "
             "mouse and gamepad input, by a script. Nobody has played it by hand yet.")
BLUF_PROPS = dict(text=("Delta\nis a space shooter.\nTwelve levels, two layers."),
                  triggerWords='a space shooter', replacementWords='a puzzle game',
                  seed='delta-walkthrough-2026-11')

C1, C2, D, E = 'campaign1', 'campaign2', 'defeat', 'extras'

CLIPS = [
 dict(id='B02', take=C1, start=0, end=301, lead=0.3,
  narration=("The main menu. How to play lists the keys and the controller. Back, then New game.")),
 dict(id='B03', take=C1, start=304, end=600, lead=0.3,
  narration=("Level one, Cold Start. The narrator, VEGA, speaks in subtitles: the Unity export had no voice files. "
             "Look at the energy cell, and F picks it up.")),
 dict(id='B04', take=C1, start=615, end=1012, lead=0.3,
  narration=("Look at the socket beside the door, and the prompt says E. The cell goes in, the socket glows, and "
             "the door opens. The exit lift ends the level.")),
 dict(id='B05', take=C1, start=1110, end=1803, lead=0.3,
  narration=("Continue. Level two, Fold. The corridor ahead is a wall up here. Q shifts the whole view down fifty "
             "metres into Lower Delta, tinted warm, where the corridor exists. Walk it, shift back up, and the "
             "lift is on the other side.")),
 dict(id='B06', take=C1, start=2700, end=3039, lead=0.3,
  narration=("Level three, Flat. This cell is empty. E puts it in the charging station: seven hundred and fifty "
             "units a second until it holds three thousand. Then E takes it back, full.")),
 dict(id='B07', take=C1, start=3601, end=4040, lead=0.3,
  narration=('Level four, Dead Weight. Pressure plates. A crate, carried with F and dropped on the first plate, holds the first door open. Items you carry still collide, so the crate is pulled along, not glued to the view.')),
 dict(id='B08', take=C1, start=5100, end=5635, lead=0.3,
  narration=('The second door needs two weights at once. Another crate goes on one plate. The script walks round to the cell, which counts as weight too, and picks it up with F.')),
 dict(id='B09', take=C1, start=6150, end=6623, lead=0.3,
  narration=('The cell goes on the second plate. Both plates down, the second door slides open, and its indicator lamps turn on, one per plate. The lift is through it.')),
 dict(id='B10', take=C1, start=6729, end=7130, lead=0.3,
  narration=("Level five, Arc. A charged cell, and an arc gate. Walk into it holding the cell, and the gate "
             "throws the cell back.")),
 dict(id='B11', take=C1, start=7580, end=8080, lead=0.3,
  narration=("So pick it up again and drain it. The discharger empties it at fifteen hundred a second, and the cell's glow fades with its charge. E takes it back out. A flat cell will pass the gate.")),
 dict(id='B12', take=C1, start=8840, end=9040, lead=0.3,
  narration=("Beyond the gate, the charging station fills it again.")),
 dict(id='B13', take=C1, start=9440, end=9865, lead=0.3,
  narration=('Into the socket. The door opens, and the script walks through to the exit lift. Every level ends on a lift like this one, and the panel records the time and the best time.')),
 dict(id='B14', take=C1, start=9971, end=10620, lead=0.3,
  narration=("Level six, Span, the first outdoor deck, with asteroids drifting past. VEGA warns that if you fall, the station's catch field puts you back, but it doesn't do that for cells. A cell in this socket extends the bridge across the gap.")),
 dict(id='B15', take=C1, start=10620, end=11379, lead=0.3,
  narration=('Across the bridge, a shuttle platform that never stops moving. The script waits for it, boards it, stays near the middle, and steps off at the far deck. Standing still, the player creeps ahead of a moving deck, so the script makes small corrections. Then the lift.')),
 dict(id='B16', take=C2, start=0, end=260, lead=0.3,
  narration=("A second take. The menu now offers Continue, at level seven, Crosswire. A cell to carry.")),
 dict(id='B17', take=C2, start=540, end=955, lead=0.3,
  narration=("The door up here is fed from a socket in Lower Delta. Shift down holding the cell: it comes along. "
             "Socket it, and shift back up.")),
 dict(id='B18', take=C2, start=1290, end=1565, lead=0.3,
  narration=("The door is open, but plasma blocks the corridor up here. It only exists in this layer, so the "
             "script shifts down past it, and back up.")),
 dict(id='B19', take=C2, start=1700, end=2255, lead=0.3,
  narration=("Level eight, Echo. Two sockets, one cell. The cell goes in the duplicator's cradle. A button beside it copies the cell, and the copy appears next to it. Then E takes the original back out of the cradle.")),
 dict(id='B20', take=C2, start=3100, end=3706, lead=0.3,
  narration=('The original is already in the first socket. The script picks up the copy and puts it in the second socket. Both lamps light, and the door opens. The duplicator only ever keeps one copy: make another, and the first disappears.')),
 dict(id='B21', take=C2, start=3940, end=4420, lead=0.3,
  narration=('Level nine, Relay. The cell is sealed in a glass vault. E at the console scans it onto the teleporter pad, and a hologram of it spins there. The button sends the real cell out.')),
 dict(id='B22', take=C2, start=4700, end=5184, lead=0.3,
  narration=('The cell lands on this side of the glass. Picked up, socketed, and the door opens. Then the lift, and the panel.')),
 dict(id='B23', take=C2, start=5450, end=6080, lead=0.3,
  narration=('Level ten, Overload. The charger is in Lower Delta and the arc gate is up here. The script carries the cell to a spot where both layers have floor, shifts down with it, and puts it in the charger.')),
 dict(id='B24', take=C2, start=6400, end=6890, lead=0.3,
  narration=('Charged, the cell is taken back out. A shuttle carries it across the gap in Lower Delta. Then the script shifts back up past the gate, puts the cell in the socket, and walks out.')),
 dict(id='B25', take=C2, start=6996, end=7530, lead=0.3,
  narration=('Level eleven, Unstable. The red thing is a sample of the reactor core. Pick it up and shift, on purpose here: it hurts you, explodes out of your hands, and a moment later rebuilds itself where it started. Then the script fetches a cell.')),
 dict(id='B26', take=C2, start=8200, end=8510, lead=0.3,
  narration=("So the core travels without shifting. With the cell already powering a socket in Lower Delta, the "
             "script shifts back up, takes the core, and carries it straight to the lift.")),
 dict(id='B27', take=C2, start=8610, end=9400, lead=0.3,
  narration=("Level twelve, Delta. Two guardians, one in each layer, attack the layer you're in every twenty seconds. This is a strike: red sparks follow you for five seconds, then lock in place, and lightning hits that spot three seconds later. The warning says get clear, and the script does, by more than the three metre radius.")),
 dict(id='B28', take=C2, start=9500, end=9950, lead=0.3,
  narration=('The other attack is a shockwave ring spreading from the middle of the deck. The warning says jump, and the script jumps it as it arrives. Then a cell goes in the first generator, which overcharges.')),
 dict(id='B29', take=C2, start=10700, end=11570, lead=0.3,
  narration=('In Lower Delta, another cell. Another strike locks on the script, and it gets clear again. The cell goes in the charger, comes out full, and into the second generator. With both generators overcharged, the vault around the core opens.')),
 dict(id='B30', take=C2, start=13300, end=13650, lead=0.3,
  narration=("A shield still covers the final bridge. The script stands beside its generator and waits for a "
             "strike to lock on it, then steps clear. The lightning destroys the shield.")),
 dict(id='B31', take=C2, start=13950, end=14480, lead=0.3,
  narration=('One more shockwave, jumped. The core is picked up, and the script carries it onto the final bridge, where the shield was. The trigger at the end lifts you two hundred metres to the stabiliser stage.')),
 dict(id='B32', take=C2, start=15150, end=16102, lead=0.3,
  narration=('On the stabiliser stage, two hundred metres up, the core goes into the stabiliser. VEGA says both layers are realigning, and to hold on. The screen shakes, goes black, the power-down sound plays, and the logo fades in. The station is whole again, with the sum of the best level times underneath.')),
 dict(id='B33', take=C2, start=16102, end=16560, lead=0.3,
  narration=('The credits roll: ported from the Unity scripts, twelve levels designed for the rebuild, the art from the Unity project, the fonts, and sound synthesized for this rebuild. They end on the main menu.')),
 dict(id='B34', take=D, start=177, end=495, lead=0.3,
  narration=("A third take, for failures. Q here is refused: Lower Delta has no floor under this spot, and the "
             "toast says something solid is in the way.")),
 dict(id='B35', take=D, start=1880, end=2045, lead=0.3,
  narration=("Plasma is fatal. The screen fades red and the level restarts.")),
 dict(id='B36', take=D, start=2063, end=2540, lead=0.3,
  narration=("Escape pauses. Here's a defect: a mouse click on Resume does nothing, because an invisible container "
             "for the options panel sits on top of the menu. Arrows and Enter work. And R, meant to restart while "
             "paused, does nothing either. Restart level, from the menu, does.")),
 dict(id='B37', take=D, start=2540, end=2751, lead=0.3,
  narration=("Skip level loads the next one. Main menu.")),
 dict(id='B38', take=D, start=5110, end=5299, lead=0.3,
  narration=("A cell dropped off the deck falls into space, and comes back to where it started.")),
 dict(id='B39', take=D, start=5680, end=5850, lead=0.3,
  narration=("And the player walking off the edge lands back at the checkpoint.")),
 dict(id='B40', take=E, start=0, end=410, lead=0.3,
  narration=("Last, the other inputs. Options: four volumes, quality, mouse sensitivity, invert Y. Credits from "
             "the menu, and Escape leaves them.")),
 dict(id='B41', take=E, start=440, end=730, lead=0.3,
  narration=("Select level shows every best time. In level one, the mouse turns the view, Shift runs, and Space "
             "jumps.")),
 dict(id='B42', take=E, start=735, end=1357, lead=0.3,
  narration=('Now a simulated gamepad, not a real controller. Y picks up the cell, X puts it in the socket, and the door opens. The left stick walks toward it, and the keys finish the route to the lift.')),
]

FEATURES = [
 ('main-menu', 'B02', C1, 30, 'Main menu: New game, Select level, How to play, Options, Credits, Exit.', 'Empty save: no Continue.'),
 ('how-to-play', 'B02', C1, 150, 'How to play: keys, controller, the goal.', 'One page.'),
 ('new-game', 'B02', C1, 300, 'New game loads level 1.', 'Fresh run.'),
 ('narrator', 'B03', C1, 400, "VEGA's lines appear as subtitles.", 'No narrator audio in the Unity export.'),
 ('pickup', 'B03', C1, 594, 'F picks up the energy cell.', 'InteractionManager 3 m ray.'),
 ('socket-door', 'B04', C1, 802, 'E places the cell; the socket powers the door.', 'EnergyCellSocket + SlidingDoor.'),
 ('exit-lift', 'B04', C1, 1011, 'The exit lift completes the level.', 'LevelGoal.'),
 ('complete-panel', 'B05', C1, 1112, 'LEVEL COMPLETE: time, best, resets; Continue.', 'Added panel.'),
 ('shift', 'B05', C1, 1250, 'Q shifts to Lower Delta, tinted warm.', 'DimensionSwitcher: ±50 m.'),
 ('charger', 'B06', C1, 2757, 'The charging station fills an empty cell.', '750 per second.'),
 ('crate-pad', 'B07', C1, 3979, 'A crate on a pressure plate opens a door.', 'ActivationPadTrigger.'),
 ('two-plates', 'B08', C1, 5602, 'Two weights at once: a crate and the cell.', 'Any item counts.'),
 ('arc-gate', 'B10', C1, 7115, 'The arc gate throws a charged cell back.', 'ElectricGate 0.3 s arc.'),
 ('discharger', 'B11', C1, 7977, 'The discharger empties the cell.', '1500 per second.'),
 ('bridge', 'B14', C1, 10544, 'A socket extends the bridge.', 'ExtendedPlatform.'),
 ('shuttle', 'B15', C1, 11128, 'An oscillating shuttle carries the player.', 'MovingPlatform.'),
 ('continue', 'B16', C2, 59, 'Continue resumes at level 7.', 'Saved progress.'),
 ('shift-with-cell', 'B17', C2, 562, 'A held cell shifts with the player.', 'Held item offset.'),
 ('cross-layer-power', 'B17', C2, 767, 'A socket in Lower Delta opens a door in Upper Delta.', 'Power ports across layers.'),
 ('plasma-layer', 'B18', C2, 1302, 'Plasma exists only in Upper Delta; shifting passes it.', 'PlasmaBall per layer.'),
 ('duplicator', 'B19', C2, 2022, 'A button copies the cell in the duplicator.', 'ObjectDuplicator.'),
 ('two-sockets', 'B20', C2, 3334, 'Two sockets powered by a cell and its copy open the door.', 'Door needs every port.'),
 ('teleporter', 'B21', C2, 4394, 'Console scan, then the button teleports the cell.', 'Teleporter.'),
 ('charger-other-layer', 'B23', C2, 5929, 'Charging in Lower Delta.', 'Layer puzzle.'),
 ('core-explodes', 'B25', C2, 7198, 'Shifting with the core makes it explode and rebuild.', 'UnstableObject.'),
 ('core-carry', 'B26', C2, 8304, 'The core is carried to the lift without shifting.', 'goal_needs_core.'),
 ('guardian-strike', 'B27', C2, 9270, 'A strike locks; the player gets clear.', 'Sparks 5 s, lock 3 s.'),
 ('shockwave', 'B28', C2, 9764, 'A shockwave ring is jumped.', 'Jump over the ring.'),
 ('generator-1', 'B28', C2, 9907, 'A cell overcharges the first generator.', 'Generator.'),
 ('generator-2', 'B29', C2, 11499, 'The second generator overcharges; the vault opens.', 'overcharged == 2.'),
 ('shield-down', 'B30', C2, 13560, 'A strike destroys the shield generator.', 'ShieldGenerator.'),
 ('final-stage', 'B31', C2, 14466, 'Carrying the core onto the final bridge lifts the player to the stabiliser.', 'FinalStageTrigger.'),
 ('stabiliser-ending', 'B32', C2, 15437, 'The stabiliser accepts the core; the ending plays.', 'Stabilizer.'),
 ('credits', 'B33', C2, 16200, 'The credits roll.', 'Credit scroll.'),
 ('shift-refused', 'B34', D, 450, 'A shift with no floor in the other layer is refused with a toast.', 'Added check.'),
 ('plasma-death', 'B35', D, 1963, 'Plasma kills; the level restarts.', 'Die() reloads.'),
 ('pause-click-defect', 'B36', D, 2125, 'A mouse click on Resume does not register.', 'Defect R-01.'),
 ('options-in-pause', 'B36', D, 2230, 'Options opens from the pause menu by keyboard.', 'OptionsPanel.'),
 ('r-paused-defect', 'B36', D, 2440, 'R while paused does nothing.', 'Defect R-02.'),
 ('restart-menu', 'B36', D, 2470, 'Restart level from the pause menu restarts it.', 'Keyboard: Down, Enter.'),
 ('skip-level', 'B37', D, 2600, 'Skip level loads level 8.', 'PauseMenu next level.'),
 ('cell-falls-back', 'B38', D, 5187, 'A cell dropped into space returns to its spawn point.', 'Item respawn.'),
 ('player-falls-back', 'B39', D, 5804, 'Falling puts the player back at the checkpoint.', 'RespawnTrigger.'),
 ('options-menu', 'B40', E, 120, 'Options: volumes, quality, sensitivity, invert Y.', 'OptionsMenuController.'),
 ('credits-esc', 'B40', E, 392, 'Esc leaves the credits.', 'Credits input.'),
 ('select-level', 'B41', E, 500, 'Select level lists best times.', 'Saved best times.'),
 ('mouse-look', 'B41', E, 600, 'The mouse turns the view.', 'Captured mouse.'),
 ('sprint-jump', 'B41', E, 697, 'Shift runs; Space jumps.', '6 m/s; jump height 1.2.'),
 ('pad-y', 'B42', E, 918, 'Pad Y picks up.', 'Unity bindings.'),
 ('pad-x', 'B42', E, 1126, 'Pad X uses the socket.', 'Unity bindings.'),
 ('pad-stick', 'B42', E, 1200, 'The left stick walks.', 'Synthetic joypad events.'),
]

NOT_SHOWN = [
 ('right-mouse-shift', 'Right mouse to shift, and the left mouse button to pick up, were not pressed; Q and F were.'),
 ('pad-shift-jump', 'Pad A (jump), RB (shift), LT (run) and Start (pause) were not pressed.'),
 ('options-changes', 'No option value was changed.'),
 ('fullscreen', 'F11 / Alt+Enter was not pressed, to keep the fixed capture window.'),
 ('exit', 'The Exit button was not clicked.'),
 ('focus-loss-pause', 'The game pauses when its window loses focus; avoided while recording.'),
 ('strike-death', 'Death by a guardian strike, and a shockwave knocking the core loose, were avoided, not shown.'),
 ('game-audio', 'The game has synthesized music and sound effects; game audio was not captured. Narration only.'),
]

VERDICT_NARR = ("Verdict. All twelve levels, the ending, the failures and the other inputs play through real input, and "
                "ninety assertions pass. Two defects in the pause menu: mouse clicks don't reach it, and R and N don't "
                "work while paused. And standing still, you creep ahead on a moving shuttle. Whether the puzzles are "
                "fair, or fun, is a person's call.")
VERDICT_LINES = ['Observed: menu → 12 levels → ending → credits; and refusals, plasma, falls, pause.',
                 "Checks: 90 of 90 film-capture assertions pass; the game's own playtest passes.",
                 'Defects: pause menu ignores clicks; R, N and Esc dead while paused; shuttle creep.',
                 'Untested: a human playtest, Windows, pad shift and jump, game audio.']
