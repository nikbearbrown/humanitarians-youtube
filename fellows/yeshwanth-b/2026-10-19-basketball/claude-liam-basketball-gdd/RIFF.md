# RIFF — Basketball Blaster: The Design Document Came Last

Riffs were written only after inspecting the takes and the source:

- **Eggs, not kills (B04, B05).** The input log shows the egg routes finishing in 12.6 to 18.7 s, while 25.6 s of fighting yielded no eggs. The riff calls that a reason to playtest, not a verdict on difficulty.
- **The unwired jetpack (B06).** Grep found one `Jetpack` declaration in the Unity scripts and no reader. The riff credits the port with the feature and labels it AUTHORED.
- **The fairness patch (B10).** `game.gd:522` comments "so the respawn is fair". Unity's `Fade.cs` has no equivalent. The riff names it the port's own rule.
- **The dead click (B16).** First found by a failed assertion in a dry run, then by reading `intro_briefing.gd:65-68`.
