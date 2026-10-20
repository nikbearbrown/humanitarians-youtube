# FACTCHECK — Basketball Blaster: Inside the Godot Code

Code panels show verbatim lines of the game at build `8f86cc8`. The checker verifies each one against the file. Every code beat is followed by real engine output of the same build.

| Beat | Claim | Evidence |
|---|---|---|
| B01 | 8 scene files of 7–12 lines; 2,408 lines of GDScript + shader | `wc -l` |
| B02 | Saved scene: 1 node. The live tree has World, five layers, platforms, spotlights, nests, camera and two CanvasLayers; nodes are mostly unnamed | `evidence/tree_probe.txt` (headless probe, no input) |
| B05 | Arena 3 values (44 tiles, 2.2 s, cap 18, 4 HP, 16 platforms, 7 eggs) | `game.gd:147-160` |
| B07 | Inputs are registered in code; `project.godot` has no `[input]` section | `game_state.gd:71-96`; `project.godot` |
| B09 | Buffer 0.12 s, coyote 0.15 s (Unity 0.5 s), one air jump, drop-through 0.25 s | `player.gd`; `PlayerController.cs` |
| B11 | Jetpack declared in Unity, unread; 1.6 s fuel, 430 px/s cap | `PlayerInput.cs:44`; `player.gd:241-249` |
| B13 | Fire 0.4 s (Unity 0.5 s); grenade 0.8 s; signals to the arena | `player.gd:261-270`; `Gun.cs` |
| B15 | 3 blinks over 3 s; early explosion on chicken contact | `grenade.gd:59-85` |
| B17 | One shader: `tint` and `flash` uniforms | `hit_flash.gdshader` |
| B19 | Mega kill window, as in Unity's AudioManager | `game.gd:460-479`; `AudioManager.cs` |
| B21 | Contact is a 58 px distance check | `game.gd:481-497` |
| B23 | Eggs: 62 px, backwards loop, win at the arena total | `game.gd:549-562` |
| B25, B26 | Clicks swallowed by the shade ColorRect (default mouse filter STOP) | `intro_briefing.gd:46-68`; assertions in take `campaign` |
| B27, B28 | Bars measure 80×34 at runtime, asked for 80×14. Cause: size set before `show_percentage = false` (stated as likely, not proven) | `evidence/bar_probe.txt`; `game.gd:715-722` |
| B29 | 56 images, 3 fonts, 14 sounds; six images and the gixel font are never used; no tests | file listing; grep of `scripts/` and `scenes/` |
