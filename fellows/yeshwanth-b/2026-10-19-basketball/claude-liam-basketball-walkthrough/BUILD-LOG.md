# BUILD-LOG — Basketball Blaster: Every Feature, Played

**Built by Claude in Claude Code.** The game was not modified. No paid calls, no upload.

- **Coverage gap closed.** The campaign autopilot never used S+Space, F, G, pad LB/RB, Esc on How to Play, Restart Arena or Quit. A third take, `extras`, was recorded to show them.
- **Not shown, and listed in `coverage.json`:** F11 fullscreen, Play Again, Exit Game on the defeat screen, game audio.
- **Clips.** 14 consecutive windows of the three takes, cut exact-frame. Narration that runs past a window ends on a labelled held frame. The decoder seeks with `-ss`, verified byte-identical to `select` at frames 1795, 3977 and 4622.
- **Gate V.** Gameplay beats declare `contrast_regions` for our disclosure strip; in the vertical, `full_bleed` for the full-width game.
- **Greeting (2026-10-19).** At the presenter's request, B00 now opens "Hola, this is Liam" (was Bonjour / Namaste / Konnichiwa). Only B00 narration and its composer card changed; both aspects were re-rendered and re-checked.
- **Vertical.** The writer text was shortened and enlarged for the portrait floors; the verdict is a portrait card.
- **Checks.** `./art godot-waikthrough --check` PASS. GATE T PASS and Gate V clean, both aspects. Frames reviewed by eye.
