# RIFF — Stage Runner: Every Feature, Played

- **The autopilot (B09).** It cleared stages 1 and 2 without a hit. The riff says what that means: a script that sees every position, not a verdict on difficulty.
- **The restart error (B18).** Found in the take's run log, not on screen. Traced to `game.gd:606` before saying it aloud.
- **The heart (B20).** Heart drops only roll while a life is missing (`game.gd:513`). The take sets that up with one labelled, deliberate hit.
